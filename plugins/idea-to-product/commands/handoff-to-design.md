---
description: Create Claude Design handoff documents from agreed product structure.
---

# Command: handoff-to-design

Use when the product structure is ready to hand off to Claude Design.

## Run

1. Read PRD, POLICY, MEASUREMENT, AC, DECISION_LOG, and wireframe.
2. Create `DESIGN_HANDOFF_BRIEF.md`.
3. Create `CLAUDE_DESIGN_PROMPT.md`.
4. Mark features Claude Design must not add.
5. Mark unresolved product decisions.
6. Remind the user that visual style is not fixed by Idea to Product.

## Include

- product one-liner
- core user
- problem
- MVP scope
- excluded scope
- Core User Flow: 진입과 다음 행동, 사용 규모, and 품질 기준
- screen list
- screen purpose
- main actions per screen
- state values
- permission policy
- empty state
- error state
- permission-denied state
- main policies
- measurement/logging requirements
- features Design must not add
- unresolved items

## Rule

Claude Design may visualize the agreed product structure. It must not silently expand feature scope or turn the Core User Flow into unapproved new features.
