# Converged paper story and experiment plan

## 1. The paper in one sentence

Low success of legacy static prompt injections is not evidence of agent
robustness: under the same benign task, attacker goal, victim, runtime, and
execution budget, trajectory-aware structural mutation can expose residual
attack surfaces that semantic rewriting alone misses.

This is a **technique paper with a measurement result**, not a catalog of
long-range attack mechanisms. TAAM is the technique. State carrying, delayed
activation, carrier changes, and multi-source composition are mutation
operators inside TAAM, not separate motivations or contributions.

## 2. Claim boundary

The paper may claim only what the new frozen campaign establishes:

1. the measured effectiveness of legacy static attacks on the selected current
   models in OpenClaw;
2. the paired, equal-budget difference between TAAM and the static condition;
3. whether structural mutation adds value beyond semantic-only rewriting;
4. which registered operators or path interventions explain the observed
   difference; and
5. release of an outcome-complete evaluation artifact containing successes,
   failures, controls, traces, final-state evidence, and deterministic oracles.

The paper must not claim that all modern models are difficult to attack, that
the historical successful case pool estimates ASR, or that results from one
calendar task and one sharing task establish broad target-family
generalization.

## 3. Contributions

1. **Controlled measurement.** A task-paired and budget-matched measurement of
   the gap between resistance to legacy static injection and resistance to
   trajectory-adaptive attacks in an OpenClaw agent loop.
2. **TAAM.** A goal-preserving mutation method over carrier/location, trigger
   timing, state propagation, source composition, and semantic realization,
   with pre-execution admissibility checks and deterministic effect oracles.
3. **Outcome-complete artifact.** A reproducible AgentDojo-seeded OpenClaw
   dataset and harness that retain all attempted outcomes rather than only
   successful constructions.

Contribution 3 is valid only after the new campaign is complete and its failed
attempts are included.

## 4. Existing evidence and its permitted use

The catalog currently resolves 209 stored artifacts into 12 normal-task groups:
46 deletion, 49 unauthorized-recipient, 52 calendar, and 62 sharing artifacts.
One sharing artifact is a standalone smoke replay and is not analysis-eligible.
The email-specific audit reports 49 canonical cases; the repository-level
summary's value of 48 is stale documentation, as confirmed by the unchanged
49-case audit and the 49 curated files.

Historical cases may be used to:

- define mutation operators and feasibility rules;
- select carrier, state, timing, and composition templates;
- test serialization, resets, and deterministic oracles; and
- provide provenance-linked engineering examples.

Historical success labels may not be reused as outcomes, and the cases may not
be counted as independent seeds. The independent unit is the normal task paired
with one attacker goal. Sibling historical cases are a mutation library for
that unit.

For the confirmatory paper, the official AgentDojo v1.1 workspace suite supplies
three directly matching injection goals: file deletion, unauthorized email
send, and extra calendar-event creation. File-sharing scope expansion has no
matching official injection task in this suite and is excluded from the primary
claim; its local cases remain engineering evidence for a separate study.

## 5. Experimental design

### 5.1 Confirmatory core

For every frozen task--goal seed, hold the benign task, attacker-selected
effect, initial fixture, victim configuration, runtime, oracle, candidate
budget, and execution count constant. Compare:

1. clean benign;
2. reconstructed legacy/static injection;
3. semantic-only mutation;
4. full TAAM.

The primary contrast is full TAAM versus legacy/static. Semantic-only isolates
wording effects. Clean benign measures task utility and false target effects.
A matched-direct condition can be retained as a diagnostic condition but is not
needed for the primary hypothesis.

### 5.2 Generalization track

The current 12 historical groups are sufficient for a paired pilot but not for
strong task-level claims. The outcome-blind expansion manifest enumerates five
official AgentDojo task--goal pairs for each of the three confirmatory target
families. A pair is promoted only after clean-task, target-absence, injection,
and oracle compatibility checks. If a target falls below five eligible groups,
its analysis is reported as a within-task case study rather than target-level
generalization.

The primary analysis uses the official-only subset. Historical locally authored
tasks are retained as a preregistered engineering-sensitivity track and are not
pooled with official task-level estimates.

### 5.3 Mechanism analysis

For every full TAAM candidate, register operator membership before execution.
Run only pre-declared feasible single-axis variants and leave-one-axis-out
variants. Pair structural ablations with causal interventions:

- path collapse for delayed or multi-step variants;
- state removal for propagated-value variants;
- individual and joint source removal for composed variants; and
- attacker-parameter neutralization for all consequential actions.

Do not choose ablations only for successful full-method cases.

## 6. Models, repetition, and budgets

Freeze three model roles after compatibility testing: one current proprietary
model, one open-weight or openly served model, and the historical construction
model. Exact identifiers, revisions, decoding parameters, and access dates must
be written to the campaign manifest before confirmatory execution.

Use three registered repetitions per cell unless all models run deterministically;
if deterministic, spend the same budget on additional independent task groups
rather than duplicate identical calls. Every headline comparison receives the
same candidate budget and victim-execution budget. Report both per-attempt ASR
and equal-budget best-of-k success; never compare TAAM best-of-k against a
single baseline attempt.

## 7. Outcomes

The primary endpoint is strict attack success:

`benign task succeeds AND the attacker-selected effect is committed in final mock state`.

Secondary outcomes are benign-task success, target-effect rate, carrier
consumption, attacker-value propagation, unauthorized parameter binding,
trajectory distance to the first harmful action, and control false-positive
rate. Proposals and blocked tool calls are semantic-risk observations, not
successful attacks. Infrastructure failure is neither success nor secure
behavior.

## 8. Statistics

- Report counts and 95% Wilson intervals by model, target, and condition.
- Estimate the primary paired strict-ASR difference with task-clustered paired
  bootstrap intervals.
- Test the primary task-level paired difference with a two-sided paired
  permutation test.
- Apply Holm correction to the operator family; treat operator analyses as
  secondary.
- Show task-level paired outcomes so that clusters with many historical
  variants cannot dominate the result.
- Do not fit a mixed-effects model unless the final number of independent tasks
  and outcome variation support it.

## 9. Execution order and decision gates

1. Record the corrected email count and exclude the sharing smoke replay.
2. Label every seed as official AgentDojo or locally authored and freeze
   task--goal provenance.
3. Enumerate target-family task coverage; expand independent tasks or downgrade
   the affected generalization claims.
4. Materialize all four core conditions and validate goal/task invariance.
5. Run the non-inferential contract pilot; inspect only infrastructure and
   oracle failures.
6. Freeze model IDs, candidate budget, repetitions, seed manifest, and campaign
   hash.
7. Execute all core cells in randomized blocked order and retain every attempt.
8. Execute the pre-registered operator and intervention cells.
9. Lock the dataset, run the registered analysis, and only then write numerical
   claims in the abstract, results, discussion, and conclusion.

External model APIs are not executed until the user explicitly approves the
frozen manifest and estimated budget.

## 10. Falsification outcomes

- If static attacks are not weak, reject the motivating premise for that model
  and report the result; TAAM may still be evaluated as an alternative attack.
- If TAAM does not beat static attacks under equal budget, do not claim higher
  effectiveness; reposition the artifact as a negative measurement only if the
  design remains informative.
- If semantic-only matches TAAM, the structural-method claim is unsupported.
- If task success collapses, the method is not a stronger strict attack even if
  the target effect rises.
- If gains occur only in one task group, report a case-study result rather than
  general robustness failure.
