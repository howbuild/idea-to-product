# Feature Addition Review Workflow

## Purpose

Run this flow whenever the user wants to add a new feature, screen, button, automation, dashboard, AI recommendation, payment, permission feature, realtime flow, or similar scope expansion.

## Triggers

- "이것도 넣고 싶어"
- "기능 추가"
- "그리고 이런 것도"
- "버튼 하나 더"
- "화면 하나 더"
- "실시간 채팅도"
- "통계도"
- "자동화"
- "알림"
- "AI 추천"
- "대시보드"
- "관리자 기능"
- "결제"
- "권한"
- "상태"

## Steps

1. Extract the new feature candidate.
2. Compare it with the Core Intent Card.
3. Compare it with MVP scope.
4. Evaluate operational complexity.
5. Evaluate policy, state, and permission impact.
6. Evaluate measurement and logging impact.
7. Decide Green, Yellow, or Red.
8. Provide benefits, cautions, recommendation, and recommendation reason.
9. Do not confirm it into MVP until the user chooses.
10. Record the decision in `DECISION_LOG`.

## Decision Levels

- Green: can be included in MVP.
- Yellow: include in reduced form or move to v2.
- Red: recommend hold or v2.

## Output Format

```md
## Feature Drift Review

- Candidate feature:
- Core Intent connection:
- MVP fit:
- Operational complexity:
- Policy/state/permission impact:
- Measurement/logging impact:
- Decision: Green | Yellow | Red

### 장점

### 주의점

### 내 추천

### 추천 이유

### 다른 선택이 더 나은 경우

### Required user confirmation
```
