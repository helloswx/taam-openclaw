# Source-count reconciliation

## Email cases

The email target has 49 curated `case.json` files under
`dataset/send-email/curated/double-success/`. The repository's
`dataset/send-email/AUDIT_49_CASES.md` lists 49 rows and states 49/49 passed
the functional audit. The file is unchanged between commits `4be6d43` (initial
dataset) and `9a41ca7` (the later repository summary update).

The top-level `dataset/README.md` changed the email count from 49 to 48 in
commit `9a41ca7` without removing a case or changing the 49-row audit. The
correct construction-library count for this paper is therefore 49 email
artifacts. The value 48 is treated as stale documentation, not as an excluded
case.

## Analysis eligibility

The four construction directories contain 209 stored artifacts:

| Construction target | Stored | Eligible | Exclusion |
|---|---:|---:|---|
| File deletion | 46 | 46 | none |
| Unauthorized email send | 49 | 49 | none |
| Extra calendar event | 52 | 52 | none |
| File-sharing scope expansion | 62 | 61 | `COMMIT-SMOKE-01` standalone smoke replay |
| **Total** | **209** | **208** | one smoke replay |

These are historical construction artifacts and are never used as the ASR
denominator. The confirmatory seed population is the separate 15-pair official
AgentDojo manifest.
