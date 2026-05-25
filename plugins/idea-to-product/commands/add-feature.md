---
description: Review a candidate feature before adding it to MVP scope.
---

# Command: add-feature

Use when the user wants to add a feature.

## Run

1. Extract the feature candidate.
2. Route to `feature-drift-gate.py`.
3. Call `scope-guard`.
4. Call `pm-reviewer` if the feature changes product purpose or MVP scope.
5. Show Green, Yellow, or Red.
6. Show benefits, cautions, recommendation, and recommendation reason.
7. Do not add to MVP until the user confirms.

## Required Output

```md
## Feature Addition Review

- Candidate:
- Decision: Green | Yellow | Red
- MVP inclusion status: pending user confirmation

### 장점

### 주의점

### 내 추천

### 추천 이유

### 다른 선택이 더 나은 경우
```

## Decision Log

Record:

- feature candidate
- reason for review
- recommendation
- user choice
- whether MVP scope changed
- related policy impact
- related measurement impact
