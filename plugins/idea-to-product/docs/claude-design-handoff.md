# Claude Design Handoff

Claude Design handoff turns confirmed product structure into a design brief and prompt.

## Inputs

- PRD
- AC
- POLICY
- MEASUREMENT
- DECISION_LOG
- wireframe
- Core User Flow: 진입과 다음 행동, 사용 규모, and 품질 기준
- unresolved items

## Outputs

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`

## Rules

- Do not force visual style.
- Do not force color, font, or layout taste.
- Do not expand feature scope.
- Preserve the confirmed Core User Flow without treating it as permission to add new features.
- Separate new feature ideas as suggestions.
- Import Design feedback through `import-design-feedback` before accepting product changes.
