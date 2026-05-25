# Hook Map

| Situation | Hook | Reviewer agent | Output | Blocks? |
|---|---|---|---|---|
| 세션 시작 | session-start.py | none | 안내 문구 | No |
| 사용자 프롬프트 제출 | user-prompt-scope-router.py | scope-guard | intent route | No |
| 기능 추가 감지 | feature-drift-gate.py | scope-guard, pm-reviewer | feature-drift-review.md | Yellow/Red needs confirmation |
| 와이어프레임 변경 | wireframe-change-review.py | product-flow-reviewer | wireframe-change-review.md | Conditional |
| 정책 변경 | policy-consistency-review.py | policy-reviewer | policy-review.md | Conditional |
| 상태값 변경 | policy-consistency-review.py | policy-reviewer | policy-review.md | Conditional |
| 버튼/상태 추가 | measurement-coverage-review.py | measurement-reviewer | measurement-review.md | No, but warns |
| 문서 생성 전 | completeness-gate.py | pm-reviewer | completeness-review.md | Warn if <70 |
| 문서 생성 후 | cross-document-consistency-review.py | qa-reviewer, tech-reviewer | consistency-review.md | Conditional |
| 최종 저장 전 | human-writing-final-pass.py | human-writing-editor | final-writing-review.md | Warn |
| 도메인팩 주입 | domain-pack-validator.py | pm-reviewer | domain-pack-validation.md | Warn |
| 레퍼런스 조사 요청 | reference-gap-review.py | reference-researcher | reference-gap-review.md | No |
| 경쟁제품 패턴 반영 | copy-risk-review.py | competitive-pattern-reviewer | copy-risk-review.md | Warn |
| 문서 생성 전 레퍼런스 미검토 | reference-gap-review.py | pm-reviewer | reference-gap-review.md | No |
| 외부 출처 사용 | source-quality-review.py | reference-researcher | source-quality-review.md | Warn |
| Claude Design handoff 생성 | none | design-handoff-writer | DESIGN_HANDOFF_BRIEF.md, CLAUDE_DESIGN_PROMPT.md | No |
| Claude Design feedback 반영 | feature-drift-gate.py | scope-guard, product-flow-reviewer | feature-drift-review.md | Conditional |
