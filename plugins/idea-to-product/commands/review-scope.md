---
description: Review whether current scope still matches the core intent card.
---

# Command: review-scope

Use when the user wants to review whether the current product scope still matches the Core Intent Card.

## Run

1. Read Core Intent Card.
2. Read current feature list.
3. Compare each feature against the core user, core problem, current Must-have requirements, Nice-to-have candidates, and KPI.
4. Route unclear or expanding items through `feature-drift-gate.py`.
5. Return Must-have, reduced Must-have, Nice-to-have, or Hold.

## Output

- feature
- Core Intent connection
- current scope status
- recommendation
- recommendation reason
- user confirmation question
