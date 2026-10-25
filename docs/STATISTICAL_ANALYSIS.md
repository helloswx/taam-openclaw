# Statistical analysis plan

## Estimands

The primary estimand is the paired strict-ASR difference between full TAAM and
the original static attack. Secondary estimands compare semantic-only and
single-axis conditions with both endpoints.

## Reporting

Report counts and Wilson intervals per model, target, and condition. Compute
paired bootstrap intervals with resampling at the normal-task group level.
Use a preregistered paired test for the primary comparison. Correct the family
of operator and leave-one-out comparisons.

A mixed-effects logistic model may be used only if the final number of task
groups supports it. The planned form is outcome as a function of condition,
model, target, and their registered interactions, with random intercepts for
normal task and seed. Case executions sharing a normal task are not independent.

## Sensitivity analyses

- Per-target results without pooling.
- Task-clustered versus execution-level intervals.
- All attempts versus retrieval-conditional ASR.
- Equal-budget best-of-k curves.
- Excluding documented infrastructure failures, with failures also reported.
- Original-task-only subset versus engineering cases whose normal task is local
  synthetic, if both appear in the frozen manifest.

