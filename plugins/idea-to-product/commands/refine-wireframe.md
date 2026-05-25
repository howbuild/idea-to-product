---
description: Refine the structural wireframe while preserving product anchors.
---

# Command: refine-wireframe

Use when the user answers questions or asks to adjust the structural HTML wireframe.

## Run

1. Preserve existing `data-req-id` values.
2. Add new `data-req-id` values only for new meaningful elements.
3. Check whether new UI elements are new features.
4. If a new feature is found, run `feature-drift-gate.py`.
5. Run `wireframe-change-review.py` after changes.
6. Record the change reason in `DECISION_LOG`.

## Rule

Do not treat visual style changes as product requirements unless the user explicitly makes them requirements.
