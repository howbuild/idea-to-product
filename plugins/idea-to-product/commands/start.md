---
description: Start the Idea to Product workflow from an initial idea.
---

# Command: start

Use when the user wants to start the Idea to Product workflow.

## Run

1. Receive the idea.
2. Create `PM_NOTE.md` to mark this folder as an active Idea to Product planning workspace.
3. Create the Core Intent Card.
4. Apply the Core User Flow.
5. Ask whether a domain pack is needed if domain context is missing or external.
6. Create the first structural HTML wireframe.
7. Show the first screen-based question card.

## Required Behavior

- Do not generate final documents immediately.
- `PM_NOTE.md` is a working note and hook activation marker, not a final output.
- Do not treat assumptions as confirmed requirements.
- Keep the wireframe structural.
- Use `question-designer` for the first question card.
- Use `wireframe-builder` for the first `wireframe.html`.
- Make the first question concrete and easy to understand.
- Keep useful practical terms such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, and `data-req-id`.

## First Output Shape

```md
# PM_NOTE

This file marks the folder as an active Idea to Product planning workspace.

## Core Intent Card

- Idea:
- Core user:
- Core problem:
- Core value:
- Requirement priority:
  - Must-have:
  - Nice-to-have:
- Operating intent: Production / Pilot / Demo / Test / One-off
- Scalability:
- Success KPI:
- Core user flow:
  - 진입과 다음 행동:
  - 사용 규모:
  - 품질 기준:
- Assumptions:
- Open questions:

## First Wireframe

Created as structural HTML with `data-req-id`.

## First Question
```
