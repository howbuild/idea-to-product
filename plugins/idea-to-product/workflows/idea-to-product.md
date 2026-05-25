# Idea to Product Workflow

This is the top-level orchestration document for the plugin.

Skills are not the main workflow. They are support modules called by this workflow, commands, hooks, and reviewer agents.

## Purpose

Turn a non-developer's idea into developer-ready product requirements while helping the user naturally learn product thinking through screen-based questions, choices, recommendations, policy decisions, state definitions, measurement design, and scope review.

## Core Principle

Do not think instead of the user. Help the user make product decisions.

Questions must reveal why a product decision matters:

- who can act
- what state changes
- what exceptions exist
- what should be measured
- what belongs in MVP
- what should move to v2
- what developers need to implement

## Required Flow

1. Idea Intake
2. Create Core Intent Card
3. Check whether reference discovery or domain pack injection is needed
4. Check Domain Pack
5. Create first structural HTML Wireframe
6. Ask screen-based questions
7. Provide choice and recommendation cards
8. Extract policies
9. Design measurement and records
10. Run hook review when features are added
11. Check PRD completeness
12. Generate documents
13. Generate Claude Design handoff when requested
14. Run cross-document consistency review
15. Run human writing final pass
16. Save final outputs

## Core Intent Card

Maintain this card throughout the session:

- product idea
- target user
- core problem
- core value
- MVP scope
- excluded scope
- success KPI
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
