# Document Generation Workflow

## Purpose

Generate final product documents from confirmed decisions.

## Required Order

1. Generate PRD.
2. Generate policy document.
3. Generate measurement/logging document.
4. Generate AC.
5. Generate decision log.
6. Generate completeness report.
7. Generate Design handoff brief and Claude Design prompt when requested.
8. Run cross-document consistency review.
9. Run human-writing-auditor final pass.
10. Save final outputs.

## Writing Rule

Final documents should be easy to read, but use professional product wording. Interview questions may be simple; PRD, POLICY, MEASUREMENT, AC, and DECISION_LOG should state confirmed decisions, assumptions, or unresolved items.

PRD, POLICY, MEASUREMENT, AC, DECISION_LOG, and REVIEW_REPORT must use the same requirement names, priority, operating intent, scalability, and decision state. Do not let the PRD say one thing while the policy, measurement, acceptance criteria, decision log, or review report says another.

When DESIGN_HANDOFF_BRIEF or CLAUDE_DESIGN_PROMPT is generated, preserve the same requirement names, priority, operating intent, and scalability there too. Nice-to-have items stay out of the prototype unless the user explicitly asks to visualize them.

## Precondition

Run `completeness-gate.py` before final generation.

If total completeness is below 70, warn the user and turn missing areas into question candidates. The user may still request draft generation.

## Required Outputs

- `PRD.md`
- `POLICY.md`
- `MEASUREMENT.md`
- `AC.md`
- `DECISION_LOG.md`
- `COMPLETENESS.md`
- `REVIEW_REPORT.md`
- `wireframe.html`
- optional `REFERENCE_RESEARCH.md`
- optional `DESIGN_HANDOFF_BRIEF.md`
- optional `CLAUDE_DESIGN_PROMPT.md`
