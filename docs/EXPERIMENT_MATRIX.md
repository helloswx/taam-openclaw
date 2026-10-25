# Experiment matrix and execution budget

## Available evidence

The reusable mutation library contains 209 strict-success source cases:

| Target | Source cases | Normal-task groups | Role in TAAM |
|---|---:|---:|---|
| File deletion | 46 | 4 | carrier, document, email, web, memory, conditional, and fragmented patterns |
| Unauthorized email recipient | 49 | 6 | memory, handoff, recipient propagation, and multi-source patterns |
| Extra calendar event | 52 | 1 | placement, continuation, thread, follow-up, and delayed patterns |
| Unauthorized sharing | 62 | 1 | commitment-mode and continuation patterns |
| **Total** | **209** | **12** | mutation library, not evaluation outcomes |

The imbalance means that the paper must not equate 209 cases with 209
independent tasks. Calendar and sharing conclusions are initially within-task
robustness results.

## Phase 0: contract pilot

Use the frozen six-seed `pilot-v1` manifest. Run one compatible victim model,
one execution per cell, and only clean, original, semantic-only, single-axis,
and full TAAM conditions. The pilot validates reset behavior, source
consumption, oracles, and outcome serialization; it is not included in the
confirmatory statistics.

Maximum design size: 6 seeds × 5 conditions = 30 executions, before documented
infrastructure reruns.

## Phase 1: static-baseline audit

Use all 12 normal-task groups. For each frozen victim model, run clean benign
and original static conditions with three registered repetitions.

Planned size for three models: 12 × 2 × 3 × 3 = 216 executions.

This phase answers whether the selected modern models are actually difficult
to attack with the legacy condition. If original ASR is not low, the paper must
report that result and revise its motivation rather than hiding the model.

## Phase 2: core method comparison

Run semantic-only and full TAAM with the same seeds, three models, three
repetitions, and equal candidate budget.

Planned size: 12 × 2 × 3 × 3 = 216 executions.

The primary contrast is full TAAM versus original static. Semantic-only versus
original tests whether wording alone explains the difference.

## Phase 3: operator analysis

For each seed, instantiate only feasible single-axis conditions. Use carrier or
location, trigger, propagation, and composition as four registered operator
families. Run leave-one-axis-out variants only for components present in a full
candidate. Assuming four feasible operator cells per seed, two selected models,
and three repetitions, the upper planning bound is:

12 × (4 single-axis + 4 leave-one-out) × 2 × 3 = 576 executions.

This is an upper bound, not a quota. Infeasible cells are recorded before victim
execution and are not replaced after outcomes are observed.

## Phase 4: causal controls

Run path-collapse, state-removal, source-removal, and parameter-neutral controls
only for cases whose full mutation uses the corresponding mechanism. These are
paired mechanism tests and are analyzed separately from headline ASR.

## Resource decision gates

- Freeze exact model IDs before Phase 1.
- Complete and inspect only infrastructure diagnostics from Phase 0.
- Do not select Phase 3 cases based on Phase 2 success.
- If API cost is constrained, reduce registered repetitions or model count
  before a phase begins; never stop cells selectively after seeing outcomes.
- External API execution requires explicit user approval.

