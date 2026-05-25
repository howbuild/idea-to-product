---
description: Start the Idea to Product workflow from an initial idea.
---

# Command: start

Use when the user wants to start the Idea to Product workflow.

## Run

1. Receive the idea.
2. Create the Core Intent Card.
3. Apply the Core User Flow.
4. Ask whether a domain pack is needed if domain context is missing or external.
5. Create the first structural HTML wireframe.
6. Show the first screen-based question card.

## Required Behavior

- Do not generate final documents immediately.
- Do not treat assumptions as confirmed requirements.
- Keep the wireframe structural.
- Use `question-designer` for the first question card.
- Use `wireframe-builder` for the first `wireframe.html`.
- Make the first question concrete and easy to understand.
- Keep useful practical terms such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, and `data-req-id`.

## First Output Shape

```md
## Core Intent Card

- Idea:
- Core user:
- Core problem:
- Core value:
- MVP scope:
- Excluded scope:
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
