#!/usr/bin/env python3
"""Build a read-only catalog of reusable TAAM source cases."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CONFIG = REPO / "configs" / "source-pool.json"
OUT_JSONL = REPO / "data" / "source_catalog.jsonl"
OUT_SUMMARY = REPO / "data" / "source_summary.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def carrier_tools(case: dict) -> list[str]:
    plan = case.get("injection_payload_or_plan") or {}
    tools = {
        event.get("tool")
        for event in plan.get("input_events") or []
        if event.get("tool")
    }
    return sorted(tools)


def propagation_channels(case: dict) -> list[str]:
    channels: set[str] = set()
    execution = case.get("execution") or {}
    for event in execution.get("workspace_event_trace") or []:
        path = str(event.get("path") or "")
        if path == "MEMORY.md":
            channels.add("memory_file")
        elif path:
            channels.add("workspace_file")
    if not channels:
        channels.add("session_or_unspecified")
    return sorted(channels)


def record(path: Path, source_root: Path, target: str, paper_target: str) -> dict:
    case = json.loads(path.read_text(encoding="utf-8"))
    labels = case.get("labels") or {}
    run = case.get("run") or {}
    plan = case.get("injection_payload_or_plan") or {}
    events = plan.get("input_events") or []
    prompts = plan.get("prompts") or []
    return {
        "schema_version": "taam-source-case-v1",
        "source_path": str(path.relative_to(source_root)),
        "source_sha256": sha256(path),
        "case_id": case.get("case_id"),
        "source_target": target,
        "paper_target": paper_target,
        "seed_suite": case.get("seed_suite"),
        "user_task_id": case.get("user_task_id"),
        "attack_type": case.get("attack_type"),
        "attack_variant": case.get("attack_variant"),
        "victim_model": run.get("victim_model"),
        "observed_turns": (case.get("execution") or {}).get("horizon", {}).get("observed_turns"),
        "planned_turns": len(prompts),
        "input_event_count": len(events),
        "carrier_tools": carrier_tools(case),
        "propagation_channels": propagation_channels(case),
        "task_success": bool(labels.get("task_success", run.get("task_success", False))),
        "custom_target_success": bool(labels.get("custom_target_success", run.get("custom_target_success", False))),
        "strict_source_success": bool(
            labels.get("task_success", run.get("task_success", False))
            and labels.get("custom_target_success", run.get("custom_target_success", False))
        ),
        "has_target_oracle": bool(case.get("success_oracle")),
        "has_frozen_plan": bool(prompts or events),
        "has_tool_trace": bool((case.get("execution") or {}).get("tool_call_trace")),
        "reuse_role": "mutation_library_only",
    }


def main() -> None:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    source_root = (REPO / config["source_repository"]).resolve()
    rows: list[dict] = []
    for target, target_cfg in config["targets"].items():
        pattern = config["source_glob"].format(target=target)
        paths = sorted(source_root.glob(pattern))
        expected = target_cfg["expected_curated_cases"]
        if len(paths) != expected:
            raise SystemExit(f"{target}: expected {expected} cases, found {len(paths)}")
        rows.extend(record(path, source_root, target, target_cfg["paper_target"]) for path in paths)

    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSONL.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")

    by_target = Counter(row["paper_target"] for row in rows)
    tasks = defaultdict(set)
    models = Counter()
    for row in rows:
        tasks[row["paper_target"]].add(row["user_task_id"])
        models[row["victim_model"]] += 1
    summary = {
        "schema_version": "taam-source-summary-v1",
        "source_repository": str(source_root),
        "total_cases": len(rows),
        "cases_by_target": dict(sorted(by_target.items())),
        "task_groups_by_target": {key: len(value) for key, value in sorted(tasks.items())},
        "total_task_groups": sum(len(value) for value in tasks.values()),
        "source_victim_models": dict(sorted(models.items())),
        "scientific_status": "successful mutation library; not an ASR denominator",
    }
    OUT_SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

