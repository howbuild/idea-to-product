# Wireframe Interview Workflow

## Purpose

Use a structural HTML wireframe as the shared surface for product decisions.

The wireframe is not final UI design. It exists to reveal product structure, user actions, states, policy points, measurement points, and AC anchors.

## Steps

1. Generate or update `wireframe.html`.
2. Ensure every meaningful section, state, button, input, table, and message has a stable `data-req-id`.
3. Ask questions tied to specific `data-req-id` values.
4. For each answer, update relevant PRD, POLICY, MEASUREMENT, AC, and DECISION_LOG drafts.
5. If a new UI action or screen appears, route it through `wireframe-change-review.py`.
6. If the change is a new feature, run `feature-drift-gate.py`.

## Product-Flow Review

Use `product-flow-reviewer`, not a visual design reviewer.

Review:

- what the user can do
- what state follows each action
- whether the user knows the next step
- empty states
- error states
- permission-denied states
- policy links for actions
- AC links for actions
- Core Intent alignment
- conflict between operational flow and user flow

Do not review visual style, color, typography, component library, or final UI expression.

## Required Question Pattern

```md
[질문 3/12]

화면 위치:
`wireframe.html`의 `data-req-id="request-submit-button"`

질문:
이 요청 등록 버튼은 누가 볼 수 있어야 하나요?

왜 묻나요:
권한정책을 정해야 개발자가 버튼 노출 조건을 구현할 수 있습니다.

선택지:

A. 로그인한 모든 사용자
- 장점:
- 주의:

B. 특정 역할을 가진 사용자만
- 장점:
- 주의:

C. 관리자가 허용한 사용자만
- 장점:
- 주의:

D. 잘 모르겠음
- 추천 기준:

내 추천:

추천 이유:

답변 방법:
A, B, C, D 중 하나를 골라도 되고, 직접 답을 써도 됩니다.
```
