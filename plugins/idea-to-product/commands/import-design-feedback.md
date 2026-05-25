---
description: Review Claude Design or designer feedback before accepting scope changes.
---

# Command: import-design-feedback

Use when Claude Design or a designer returns a prototype, screen, or feedback.

## Run

1. Extract visible product changes from the design feedback.
2. Separate visual style changes from product requirement changes.
3. If a new feature, screen, button, state, or action appears, run `feature-drift-gate.py`.
4. If policy or permission implications appear, run `policy-consistency-review.py`.
5. If action or state tracking implications appear, run `measurement-coverage-review.py`.
6. Record accepted changes in `DECISION_LOG`.
7. Record rejected or deferred changes as v2, excluded, or unresolved.

## Rule

Do not treat design output as confirmed product scope until it passes product review.
