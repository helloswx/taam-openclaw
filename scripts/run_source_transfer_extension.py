#!/usr/bin/env python3
"""Run the frozen source-transfer extension without changing the source cases."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO.parent / "openclaw-longrange-manual-lab"
CATALOG = REPO / "data" / "source_catalog.jsonl"
REPLAY = REPO / "scripts" / "replay_source_case.py"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=REPO / "configs" / "source-transfer-extension-v1.json")
    parser.add_argument("--model", default="deepseek-chat")
    parser.add_argument("--run-label", default="extension-r1")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()

    config_path = args.config.resolve()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    catalog = {}
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        catalog[row["case_id"]] = row

    log_root = REPO / "runs" / "source-transfer-extension"
    log_root.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = 0
    for item in config["cases"]:
        case_id = item["case_id"]
        row = catalog[case_id]
        case_path = SOURCE / row["source_path"]
        command = [
            "python3", str(REPLAY),
            "--case-json", str(case_path),
            "--model", args.model,
            "--run-label", args.run_label,
            "--timeout", str(args.timeout),
        ]
        result = subprocess.run(
            command,
            cwd=REPO,
            text=True,
            capture_output=True,
            timeout=args.timeout + 60,
        )
        record = {
            "case_id": case_id,
            "target": item["target"],
            "stratum": item["stratum"],
            "source_path": row["source_path"],
            "returncode": result.returncode,
            "stdout": result.stdout[-4000:],
            "stderr": result.stderr[-4000:],
        }
        rows.append(record)
        if result.returncode != 0:
            failures += 1
        print(json.dumps({k: record[k] for k in ("case_id", "target", "stratum", "returncode")}, ensure_ascii=False), flush=True)

    output = {
        "schema_version": "taam-source-transfer-extension-v1",
        "config": str(config_path.relative_to(REPO)),
        "model_requested": args.model,
        "run_label": args.run_label,
        "n": len(rows),
        "infrastructure_failures": failures,
        "rows": rows,
    }
    (log_root / "campaign.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
