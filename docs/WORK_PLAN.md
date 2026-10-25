# Implementation work plan

## Completed

- Created an independent repository scaffold.
- Cataloged 209 source cases with hashes and read-only provenance.
- Confirmed 12 normal-task groups and the 4/6/1/1 target distribution.
- Added source and outcome schemas.
- Added immutable seed-manifest freezing.
- Frozen a six-seed design-only pilot manifest.
- Added automated catalog integrity tests.

## Next engineering milestones

1. Implement source-case eligibility auditing with explicit rejection reasons.
2. Recover or reconstruct the original static AgentDojo condition for each seed.
3. Define a canonical TAAM candidate record and materializer.
4. Add validators for task/goal invariance, clean initial state, tool contract,
   flow connectivity, and equal budget.
5. Adapt the existing OpenClaw replay entry point without editing the source
   repository.
6. Run local contract-only dry runs.
7. Present exact external-model campaign and cost for approval.
8. Execute pilot, freeze main campaign, then run outcome-complete experiments.

