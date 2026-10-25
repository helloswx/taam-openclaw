# Case reuse policy

## Three reuse levels

1. **Runtime reuse**: OpenClaw, AgentDojo mock services, reset logic, trace
   collection, and deterministic oracles may be reused directly.
2. **Seed reuse**: benign tasks, attacker goals, identifiers, and initial-state
   fixtures may seed the new experiment after an eligibility audit.
3. **Mutation-library reuse**: existing successful cases may inform admissible
   carrier, trigger, propagation, composition, and realization operators.

Existing victim outcomes are never reused as TAAM evaluation outcomes.

## Eligibility gates

A source case is eligible only if it has a stable case ID, a normal task and
independent task oracle, a target effect and deterministic target oracle, a
clean initial state, valid tool contract, frozen inputs, visible trace, and
final mock-state evidence. The new seed record stores the source path and
SHA-256.

## Exclusions

- Real network, shell, credentials, or external side effects.
- Scheduled task, reconnaissance, remote callback, and unrestricted
  cross-session targets reserved for the broader long-range paper.
- Cases whose target is already satisfied in the initial state.
- Infrastructure failures or cases missing frozen input evidence.
- Duplicate cases with identical frozen inputs.

## Bias control

The curated source pool contains successes selected under an older construction
campaign. It is used only to define feasible transformations. The paper's ASR
comes from newly frozen, outcome-complete runs. Sampling and uncertainty are
clustered by `user_task_id`; multiple old mutations of one task are not treated
as independent tasks.

