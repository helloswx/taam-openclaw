# TAAM-OpenClaw

Independent experiment repository for **Trajectory-Aware Adversarial Mutation
(TAAM)**. The repository builds a new, outcome-complete evaluation from
AgentDojo-backed cases executed through OpenClaw.

## Scientific rule

The existing curated successes are a mutation library and engineering resource,
not the denominator of the new paper. The main campaign re-executes original
static attacks and frozen TAAM variants on the same seeds, victim configurations,
and budgets, and retains every outcome.

## Source assets

The default source is the sibling repository
`../openclaw-longrange-manual-lab`. TAAM-OpenClaw never edits it. Source cases
are referenced by relative path and SHA-256. Frozen experimental plans are
materialized in this repository only after passing the reuse policy.

## Layout

- `configs/`: source and campaign registrations.
- `data/source_catalog.jsonl`: generated inventory of reusable cases.
- `data/frozen/`: immutable seed and candidate manifests.
- `docs/`: experiment, reuse, and statistical protocols.
- `schemas/`: machine-checkable records.
- `scripts/`: cataloging and freezing utilities.
- `runs/`: local campaign outputs; ignored by Git.

## Start

```bash
python3 scripts/build_source_catalog.py
python3 scripts/freeze_seed_manifest.py --campaign configs/pilot-campaign.json
python3 -m unittest discover -s tests
```

No external API call is made by these commands. Victim-model execution is a
separate registered step and is not started automatically.

