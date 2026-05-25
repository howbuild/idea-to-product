---
description: Review whether current scope still matches the core intent card.
---

# Command: review-scope

Use when the user wants to review whether the current product scope still matches the Core Intent Card.

## Run

1. Read Core Intent Card.
2. Read current feature list.
3. Compare each feature against the core user, core problem, MVP scope, excluded scope, and KPI.
4. Route unclear or expanding items through `feature-drift-gate.py`.
5. Return MVP 포함, 축소 포함, v2 이동, or 보류.

## Output

- feature
- Core Intent connection
- current scope status
- recommendation
- recommendation reason
- user confirmation question
