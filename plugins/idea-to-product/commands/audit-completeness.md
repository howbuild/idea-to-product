---
description: Check whether the current product documents are complete enough.
---

# Command: audit-completeness

Use when the user wants to check PRD completeness.

## Run

1. Score each completeness category.
2. Show missing or weak categories.
3. Convert weak categories into next question candidates.
4. Warn if total score is under 70.

## Scoring

- 문제와 배경: 10
- 핵심 사용자: 10
- 핵심 가치와 KPI: 10
- 핵심 화면과 사용자 여정: 10
- 핵심 유저 플로우: 10
- 기능 요구사항, 우선순위, 운영 의도, 확장 가능성: 20
- 정책 정의: 10
- 상태, 권한, 예외: 10
- 측정/기록 설계: 10
- AC 작성: 5
- 결정근거 정리: 5

The hook normalizes the category total to 100.

Do not score by document length.
