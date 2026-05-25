# Idea to Product Workflow

This is the top-level orchestration document for the plugin.

Skills are not the main workflow. They are support modules called by this workflow, commands, hooks, and reviewer agents.

## Purpose

Turn a non-developer's idea into developer-ready product requirements while helping the user naturally learn product thinking through screen-based questions, choices, recommendations, policy decisions, state definitions, measurement design, and scope review.

## Core Principle

Do not think instead of the user. Help the user make product decisions.

Questions must be easy to understand, but not childish.

Write the question so that the decision is clear even to a young child. Keep practical product terms when they matter, such as PRD, AC, KPI, 권한정책, 상태값, 이벤트, 로그, and `data-req-id`. If a term may be unfamiliar, keep the term and explain it with one plain sentence.

Questions must reveal why a product decision matters:

- who can act
- what state changes
- what exceptions exist
- what should be measured
- what belongs in MVP
- what should move to v2
- what developers need to implement

## Core User Flow

Use this structure after the Core Intent Card and throughout wireframe, policy, measurement, and review work.

- 진입과 다음 행동: 사용자는 어디서 와서 어디로 가나요?
- 사용 규모: 얼마나 많이 지나가게 만들고 싶나요?
- 품질 기준: 사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?

Do not use abstract wording as the user-facing question. For example, ask "사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?" instead of "흐름이 커졌을 때 무엇을 지켜야 하나요?"

Use the Core User Flow to create:

- entry point and next-step questions
- bottleneck and usage-volume questions
- trust, misuse, outdated-content, misleading-copy, and quality-rule questions
- measurement candidates for entry and next action, usage scale, and quality criteria

## Required Flow

1. Idea Intake
2. Create Core Intent Card
3. Apply Core User Flow
4. Check whether reference discovery or domain pack injection is needed
5. Check Domain Pack
6. Create first structural HTML Wireframe
7. Ask screen-based questions
8. Provide choice and recommendation cards
9. Extract policies
10. Design measurement and records
11. Run hook review when features are added
12. Check PRD completeness
13. Generate documents
14. Generate Claude Design handoff when requested
15. Run cross-document consistency review
16. Run human writing final pass
17. Save final outputs

## Core Intent Card

Maintain this card throughout the session:

- product idea
- target user
- core problem
- core value
- MVP scope
- excluded scope
- success KPI
- core user flow
- current feature list
- open questions

Feature additions must be compared against this card.

## Question Card Rule

Every product question should include:

- question number
- screen location using `wireframe.html` and `data-req-id`
- question
- why it is asked
- A/B/C/D choices
- benefit per choice
- caution per choice
- recommendation
- recommendation reason
- answer method

Question text must keep the decision concrete. Prefer "이 버튼은 누가 볼 수 있어야 하나요?" over "권한정책 적용 대상을 정의할까요?"

## Recommendation Rule

Do not present one option as the only answer. Show tradeoffs.

Required format:

- 선택지
- 장점
- 주의점
- 내 추천
- 추천 이유
- 다른 선택이 더 나은 경우

## Hook Gate Rule

When the user asks for a new feature or new screen, do not add it directly to MVP.

Run `feature-drift-gate.py` and use `scope-guard` plus `pm-reviewer`.

Yellow or Red decisions require explicit user confirmation before MVP inclusion.

## Reference Research Rule

Reference research is a support layer, not the product.

Use it to create:

- question candidates
- policy candidates
- state candidates
- permission candidates
- measurement/logging candidates
- MVP or excluded-scope judgments
- AC candidates

Do not copy competitors. Record sources, check dates, observed patterns, application decisions, and limitations when outside references are used.

## Final Outputs

- `PRD.md`
- `AC.md`
- `POLICY.md`
- `MEASUREMENT.md`
- `DECISION_LOG.md`
- `COMPLETENESS.md`
- `REVIEW_REPORT.md`
- `wireframe.html`
- `DESIGN_HANDOFF_BRIEF.md` when Design handoff is requested
- `CLAUDE_DESIGN_PROMPT.md` when Design handoff is requested
