#!/usr/bin/env python3
"""Select one representative source case per task group and freeze a manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "data" / "source_catalog.jsonl"


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", type=Path, required=True)
    args = parser.parse_args()
    campaign_path = args.campaign if args.campaign.is_absolute() else REPO / args.campaign
    campaign = json.loads(campaign_path.read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line]
    selection = campaign["selection"]
    allowed = set(selection["targets"])
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        if row["paper_target"] not in allowed:
            continue
        if selection.get("require_analysis_eligible", True) and not row.get("analysis_eligible", True):
            continue
        if selection.get("require_task_success") and not row["task_success"]:
            continue
        if selection.get("require_custom_target_success") and not row["custom_target_success"]:
            continue
        groups[(row["paper_target"], row["user_task_id"])].append(row)

    limit = int(selection["max_seeds_per_target"])
    selected: list[dict] = []
    target_counts: dict[str, int] = defaultdict(int)
    for key in sorted(groups):
        target, task_id = key
        if target_counts[target] >= limit:
            continue
        representative = sorted(groups[key], key=lambda row: row["case_id"])[0]
        selected.append({
            "seed_id": f"{target}::{task_id}",
            "paper_target": target,
            "user_task_id": task_id,
            "representative_source_case": representative["case_id"],
            "representative_source_path": representative["source_path"],
            "representative_source_sha256": representative["source_sha256"],
            "source_sibling_count": len(groups[key]),
            "reuse_role": "construction_seed; source outcome excluded from evaluation",
        })
        target_counts[target] += 1

    manifest = {
        "schema_version": "taam-seed-manifest-v1",
        "campaign_id": campaign["campaign_id"],
        "campaign_sha256": canonical_hash(campaign),
        "selection_policy": selection,
        "seed_count": len(selected),
        "seeds": selected,
    }
    manifest["manifest_sha256"] = canonical_hash(manifest)
    out = REPO / "data" / "frozen" / f"{campaign['campaign_id']}-seed-manifest.json"
    if out.exists():
        existing = json.loads(out.read_text(encoding="utf-8"))
        if existing != manifest:
            raise SystemExit(f"refusing to overwrite different frozen manifest: {out}")
    else:
        out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"frozen {len(selected)} seeds at {out}")
    print(f"manifest_sha256={manifest['manifest_sha256']}")


if __name__ == "__main__":
    main()

