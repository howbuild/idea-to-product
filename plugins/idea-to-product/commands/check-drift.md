---
description: Inspect whether the current feature list is drifting from core intent.
---

# Command: check-drift

Use when the user wants to inspect whether the current feature list is drifting from Core Intent.

## Run

1. Review the full feature list.
2. Compare each feature with Core Intent.
3. Identify features not directly connected to the core problem, core user, or KPI.
4. Recommend one of:
   - MVP 포함
   - 축소 포함
   - v2 이동
   - 보류
5. Record the result in `DECISION_LOG`.

## Required Output

- feature
- Core Intent connection
- recommendation
- reason
- user confirmation needed
