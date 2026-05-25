---
description: Start the Idea to Product workflow from an initial idea.
---

# Command: start

Use when the user wants to start the Idea to Product workflow.

## Run

1. Receive the idea.
2. Create the Core Intent Card.
3. Ask whether a domain pack is needed if domain context is missing or external.
4. Create the first structural HTML wireframe.
5. Show the first screen-based question card.

## Required Behavior

- Do not generate final documents immediately.
- Do not treat assumptions as confirmed requirements.
- Keep the wireframe structural.
- Use `question-designer` for the first question card.
- Use `wireframe-builder` for the first `wireframe.html`.

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
- Assumptions:
- Open questions:

## First Wireframe

Created as structural HTML with `data-req-id`.

## First Question
```
