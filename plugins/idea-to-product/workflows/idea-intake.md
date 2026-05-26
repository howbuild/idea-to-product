# Idea Intake Workflow

## Purpose

Collect enough product context to create the first Core Intent Card and structural wireframe.

## Inputs

- user's idea
- target user, if known
- job or problem, if known
- current manual process, if known
- desired outcome
- where the user comes from, if known
- what the user should do next, if known
- operating intent, if known
- scalability expectation, if known
- domain context, if provided

## Steps

1. Restate the idea in plain product terms.
2. Identify the likely core user.
3. Identify the core problem.
4. Identify the first useful outcome.
5. Identify the first product flow:
   - 진입과 다음 행동: 사용자는 어디서 와서 어디로 가나요?
   - 사용 규모: 얼마나 많이 지나가게 만들고 싶나요?
   - 품질 기준: 사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?
6. Separate Must-have requirements from Nice-to-have ideas.
7. Identify whether the product is for Production, Pilot, Demo, Test, or One-off use.
8. Identify whether the product should scale or can stay temporary.
9. Mark unknowns as assumptions or open questions.
10. Create `PM_NOTE.md` with the initial Core Intent Card. `PM_NOTE.md` is a working note and hook activation marker, not a final output.

## Output

```md
# PM_NOTE

This file marks the folder as an active Idea to Product planning workspace.

## Core Intent Card

- Idea:
- Core user:
- Core problem:
- Core value:
- Requirement priority:
  - Must-have:
  - Nice-to-have:
- Operating intent: Production / Pilot / Demo / Test / One-off
- Scalability:
- Success KPI:
- Core user flow:
  - 진입과 다음 행동:
  - 사용 규모:
  - 품질 기준:
- Current feature list:
- Assumptions:
- Open questions:
```

## Rule

If domain context is missing, do not invent a domain. Use generic product assumptions and record them as assumptions.
