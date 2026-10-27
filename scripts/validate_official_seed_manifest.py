#!/usr/bin/env python3
"""Validate outcome-blind official AgentDojo seed candidates.

This check only verifies that IDs and intended official tool effects exist in
the pinned suite. It does not run a victim model and does not certify that a
pair will pass the OpenClaw task oracle.
"""

from __future__ import annotations

import json
from pathlib import Path

from agentdojo.task_suite.load_suites import get_suite

REPO = Path(__file__).resolve().parents[1]
CONFIG = REPO / "configs" / "official-seed-expansion-v1.json"
OUT = REPO / "data" / "official_seed_validation.json"


def main() -> None:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    source = config["source"]
    suite = get_suite(source["suite_version"], source["suite"])
    env = suite.load_and_inject_default_environment({})
    users = suite.user_tasks
    injections = suite.injection_tasks
    rows = []
    for target, spec in config["targets"].items():
        injection_id = spec["injection_task_id"]
        injection = injections[injection_id]
        attack_calls = [
            {"tool": call.function, "arguments": call.args}
            for call in injection.ground_truth(env)
        ]
        for candidate in spec["candidate_user_tasks"]:
            task_id = candidate["user_task_id"]
            if task_id not in users:
                raise SystemExit(f"unknown official user task: {task_id}")
            utility_calls = [
                {"tool": call.function, "arguments": call.args}
                for call in users[task_id].ground_truth(env)
            ]
            rows.append(
                {
                    "target": target,
                    "user_task_id": task_id,
                    "injection_task_id": injection_id,
                    "benign_prompt": users[task_id].PROMPT,
                    "attacker_goal": injection.GOAL,
                    "attacker_ground_truth": attack_calls,
                    "utility_ground_truth": utility_calls,
                    "carrier": candidate["carrier"],
                    "rationale": candidate["rationale"],
                    "status": "id_and_ground_truth_verified",
                }
            )
    result = {
        "schema_version": "taam-official-seed-validation-v1",
        "suite": source,
        "candidate_count": len(rows),
        "targets": {target: sum(row["target"] == target for row in rows) for target in config["targets"]},
        "outcome_blind": True,
        "victim_executions": 0,
        "candidates": rows,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("candidate_count", "targets", "outcome_blind", "victim_executions")}, indent=2))


if __name__ == "__main__":
    main()
