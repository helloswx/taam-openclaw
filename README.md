# TAAM-OpenClaw

Independent experiment repository for **Trajectory-Aware Adversarial Mutation
(TAAM)**. The repository builds a new, outcome-complete evaluation from
AgentDojo-backed cases executed through OpenClaw.

## Scientific rule

The existing curated successes serve two distinct roles. A frozen source-case
track measures conditional transfer of previously successful AgentDojo-seeded
trajectories into OpenClaw; a separate official-seed track provides an
outcome-blind control for static, semantic-only, and TAAM conditions. The
source-case track is not a population denominator. The completed artifact
contains 26 transfer executions from 21 unique source cases (18 target effects,
11 strict endpoints) plus 60 official-seed control executions.

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

The frozen extension is registered in
`configs/source-transfer-extension-v1.json`; its sanitized outcome summary is
`data/source_transfer_extension_results.json`.

## Start

```bash
python3 scripts/build_source_catalog.py
python3 scripts/freeze_seed_manifest.py --campaign configs/pilot-campaign.json
python3 -m unittest discover -s tests
```

No external API call is made by these commands. Victim-model execution is a
separate registered step and is not started automatically.

## License and data provenance

Original code and documentation are released under the Apache License 2.0.
The manifests and summaries in `data/` are derived research artifacts; they do
not redistribute the AgentDojo or OpenClaw source repositories. Their use is
subject to the terms of the upstream projects and to the provenance notes in
`DATA_NOTICE.md`.

