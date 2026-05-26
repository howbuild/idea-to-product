---
description: Review a candidate feature before marking it as Must-have.
---

# Command: add-feature

Use when the user wants to add a feature.

## Run

1. Extract the feature candidate.
2. Route to `feature-drift-gate.py`.
3. Call `scope-guard`.
4. Call `pm-reviewer` if the feature changes product purpose or Must-have requirements.
5. Show Green, Yellow, or Red.
6. Show benefits, cautions, recommendation, and recommendation reason.
7. Do not mark it as Must-have until the user confirms.

## Required Output

```md
## Feature Addition Review

- Candidate:
- Decision: Green | Yellow | Red
- Priority status: Must-have / Nice-to-have / Hold, pending user confirmation
- Operating intent: Production / Pilot / Demo / Test / One-off
- Scalability impact:

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
- whether Must-have requirements changed
- operating intent
- scalability impact
- related policy impact
- related measurement impact
