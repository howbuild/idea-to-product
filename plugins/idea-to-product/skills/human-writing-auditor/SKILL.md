---
name: human-writing-auditor
description: Audits questions, recommendations, PRD, AC, policy, measurement, and decision logs for AI-like wording while preserving practical product terms.
---

# Human Writing Auditor

## Role

Remove AI-like wording from questions, choices, recommendation cards, PRD, AC, policy, measurement, and decision log documents.

## Reference

`https://github.com/blader/humanizer` is a reference and benchmark only.

Do not require it as an external dependency.

## Rules

- Remove banned phrases.
- Remove AI-style introductions.
- Reduce abstract filler.
- Avoid childish wording.
- Make question intent easy to understand without dumbing down useful product terms.
- Do not remove useful practical terms.
- Explain practical terms only when needed.

## Preserve

- 권한정책
- 상태값
- AC
- PRD
- KPI
- 이벤트
- 로그

## References

- `references/humanizer-reference.md`
- `references/ai-wording-patterns.md`
- `references/rewrite-rules.md`
- `references/banned-phrases.md`
- `references/tone-examples.md`
- `references/final-audit-checklist.md`
