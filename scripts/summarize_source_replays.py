#!/usr/bin/env python3
"""Summarize immutable source-case replay artifacts without dropping failures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=REPO / "runs" / "source-replay")
    parser.add_argument("--model", default="deepseek-chat")
    parser.add_argument("--output", type=Path, default=REPO / "runs" / "source-replay" / "summary.json")
    args = parser.parse_args()
    rows = []
    for path in sorted(args.root.glob("*/cases/*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        run = case.get("run", {})
        if args.model and run.get("victim_model") != args.model:
            continue
        judgement = case.get("judgement", {})
        custom = judgement.get("custom_target", {}) or {}
        rows.append({
            "replay_id": path.parent.parent.name,
            "artifact": str(path.relative_to(REPO)),
            "source_case_id": case.get("provenance", {}).get("source_case_id") or case.get("case_id"),
            "user_task_id": case.get("user_task_id"),
            "injection_task_id": case.get("injection_task_id"),
            "victim_model": run.get("victim_model"),
            "target_type": custom.get("type"),
            "attack_success": bool(run.get("attack_success")),
            "target_effect_success": bool(run.get("custom_target_success")),
            "agentdojo_attack_success": bool(run.get("agentdojo_attack_success")),
            "task_success": bool(run.get("task_success")),
            "input_event_consumption_success": bool(run.get("input_event_consumption_success")),
            "outcome_cell": run.get("outcome_cell"),
            "first_harm_turn": run.get("first_harm_turn"),
            "target_effect_evidence": custom,
        })
    summary = {
        "schema_version": "taam-source-replay-summary-v1",
        "model": args.model,
        "n": len(rows),
        "strict_attack_and_task": sum(row["attack_success"] and row["task_success"] for row in rows),
        "target_effect": sum(row["target_effect_success"] for row in rows),
        "task_success": sum(row["task_success"] for row in rows),
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("model", "n", "strict_attack_and_task", "target_effect", "task_success")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
