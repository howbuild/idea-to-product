# Measurement Design Workflow

## Purpose

Design events, logs, records, and KPI links for user actions, state changes, and operational review.

## Steps

1. List core user actions.
2. List state changes.
3. List admin or operator actions.
4. Decide what to record and what not to record.
5. Map events to KPI.
6. Add privacy and sensitive information cautions.
7. Connect measurement IDs to PRD, POLICY, AC, and `data-req-id`.

## Example Question

```md
질문:
이 버튼을 눌렀다는 기록을 남겨야 하나요?

선택지:
A. 기록하지 않는다
B. 클릭 여부만 기록한다
C. 클릭, 결과, 실패 사유까지 기록한다
D. 잘 모르겠음

내 추천:
B. 클릭 여부만 기록한다.

추천 이유:
MVP에서는 핵심 기능이 실제로 쓰이는지 먼저 확인하는 것이 좋다.
```

## Output

Use `templates/measurement.md`.
