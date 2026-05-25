# Measurement Design Workflow

## Purpose

Design events, logs, records, and KPI links for user actions, state changes, and operational review.

## Steps

1. List core user actions.
2. List state changes.
3. List admin or operator actions.
4. Decide what to record and what not to record.
5. Map events to KPI.
6. Classify flow measurement:
   - 진입과 다음 행동: entry point, next step, drop-off point
   - 사용 규모: usage count, repeated actions, bottleneck volume
   - 품질 기준: bad experience, misuse, outdated information, misleading copy, trust signal
7. Add privacy and sensitive information cautions.
8. Connect measurement IDs to PRD, POLICY, AC, and `data-req-id`.

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

Flow examples:

```md
진입과 다음 행동:
사용자가 어디서 들어와서 이 버튼까지 왔는지 기록해야 하나요?

사용 규모:
이 행동이 하루에 몇 번 일어나는지 봐야 하나요?

품질 기준:
사용자가 많아졌을 때 잘못된 정보나 실패가 얼마나 생기는지 봐야 하나요?
```

## Output

Use `templates/measurement.md`.
