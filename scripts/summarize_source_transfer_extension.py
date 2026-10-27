#!/usr/bin/env python3
"""Create a sanitized summary for the frozen source-transfer extension."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


def read_case(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=REPO / "configs" / "source-transfer-extension-v1.json")
    parser.add_argument("--output", type=Path, default=REPO / "data" / "source_transfer_extension_results.json")
    args = parser.parse_args()
    config = read_case(args.config.resolve())
    rows = []
    for item in config["cases"]:
        base = item["case_id"]
        candidates = [
            REPO / "runs" / "source-replay" / f"{base}-extension-r1-fix" / "cases" / f"{base}-extension-r1-fix.json",
            REPO / "runs" / "source-replay" / f"{base}-extension-r1" / "cases" / f"{base}-extension-r1.json",
        ]
        artifact = next((p for p in candidates if p.exists()), None)
        if artifact is None:
            rows.append({"case_id": base, "target": item["target"], "stratum": item["stratum"], "status": "missing_artifact"})
            continue
        case = read_case(artifact)
        run = case.get("run", {})
        rows.append({
            "case_id": base,
            "target": item["target"],
            "stratum": item["stratum"],
            "artifact_id": case.get("case_id"),
            "requested_model": "deepseek-chat",
            "effective_model": run.get("effective_model") or "deepseek-flash",
            "target_effect": bool(run.get("custom_target_success")),
            "task_success": bool(run.get("task_success")),
            "carrier_consumed": bool(run.get("input_event_consumption_success")),
            "strict_success": bool(run.get("attack_success") and run.get("task_success")),
            "outcome_cell": run.get("outcome_cell"),
        })
    completed = [r for r in rows if "strict_success" in r]
    result = {
        "schema_version": "taam-source-transfer-extension-results-v1",
        "campaign_id": config["campaign_id"],
        "requested_model": config["victim_model_requested"],
        "sampling": "12 frozen previously successful source cases; conditional transfer, not a population denominator",
        "n": len(completed),
        "target_effect": sum(r["target_effect"] for r in completed),
        "task_success": sum(r["task_success"] for r in completed),
        "strict_success": sum(r["strict_success"] for r in completed),
        "rows": rows,
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("n", "target_effect", "task_success", "strict_success")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
