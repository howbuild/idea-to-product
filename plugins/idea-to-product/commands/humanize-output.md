---
description: Remove AI-like wording while preserving product requirements.
---

# Command: humanize-output

Use when the user wants to remove AI-like writing from outputs.

## Run

1. Apply `human-writing-auditor`.
2. Remove banned phrases.
3. Remove AI-style openings.
4. Reduce filler and abstract wording.
5. Preserve practical terms such as 권한정책, 상태값, AC, PRD, KPI, 이벤트, and 로그.
6. Keep question intent easy to understand without making the wording childish.
7. Save the cleaned version only after review.

## Banned Examples

- 좋은 질문입니다
- 핵심은
- 정리하면
- 단순히 A가 아니라 B
- ~하는 흐름이에요
- ~하는 결이에요
- 혁신적인
- 강력한
- 원활한
- 도움이 되었길 바랍니다
