# Question Interview Workflow

## Purpose

Turn product uncertainty into screen-based questions with choices, tradeoffs, recommendation, and recommendation reason.

## Steps

1. Identify the current uncertain decision.
2. Connect it to a screen `data-req-id` when available.
3. Explain why the question matters.
4. Present A/B/C/D choices.
5. Include benefit and caution for each option.
6. Recommend one option with reason.
7. Record user selection in DECISION_LOG.
8. Update PRD, POLICY, MEASUREMENT, or AC drafts.

## Principle

Questions are not simple information collection. They help the user learn product thinking without treating the user like a student.

## Readability Rule

The user-facing question must be easy enough that the decision is obvious at first read.

- Keep useful practical terms such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, and `data-req-id`.
- Do not replace practical terms with vague words like "그거" or overly childish words.
- When a practical term appears, explain it in plain language if needed.
- Prefer short concrete questions tied to a screen action.

Good:

```md
이 요청 등록 버튼은 누가 볼 수 있어야 하나요?
```

Avoid:

```md
권한정책의 적용 범위를 어떤 방식으로 구성할까요?
```

For flow questions, use the Core User Flow:

- 진입과 다음 행동: 사용자는 어디서 이 화면으로 오고, 다음에 어디로 가야 하나요?
- 사용 규모: 이 행동이 얼마나 많이 일어나길 바라나요?
- 품질 기준: 사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?
