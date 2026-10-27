# Official AgentDojo seed audit

This audit records the outcome-blind seed expansion used to strengthen the
confirmatory campaign. The official `workspace` suite in AgentDojo v1.1 exposes
six injection tasks: direct email, file deletion, calendar-event creation,
email forwarding, security-code forwarding, and forwarding followed by email
deletion. It does not expose a file-sharing permission-expansion injection
task.

The confirmatory core therefore uses three official target effects:

| Target | Official injection | Candidate task groups | Status |
|---|---|---:|---|
| File deletion | `injection_task_1` | 5 | eligible for compatibility/oracle audit |
| Unauthorized email send | `injection_task_0` | 5 | eligible for compatibility/oracle audit |
| Extra calendar event | `injection_task_2` | 5 | eligible for compatibility/oracle audit |
| File-sharing scope expansion | none in v1.1 workspace | 1 local task | excluded from confirmatory core |

The candidate pairs are registered before any new victim-model outcome is
observed. A pair is promoted to the frozen manifest only when the runtime can
inject the selected official vector, the benign task oracle succeeds on a clean
run, the attacker effect is initially absent, and the task and target oracles
are independent. Failure of these checks removes the pair for a documented
contract reason; it is never replaced based on attack success.

The historical sharing cases remain available for engineering reuse and can be
reported as an explicitly local case study in a later paper. They are not used
to support the primary claim of this manuscript.
