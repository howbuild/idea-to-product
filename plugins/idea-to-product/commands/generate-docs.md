---
description: Generate PRD, policy, measurement, AC, decision log, and review outputs.
---

# Command: generate-docs

Use when the user wants to create the final output documents.

## Run

1. Run `completeness-gate.py`.
2. Generate `PRD.md`.
3. Generate `POLICY.md`.
4. Generate `MEASUREMENT.md`.
5. Generate `AC.md`.
6. Generate `DECISION_LOG.md`.
7. Generate `COMPLETENESS.md`.
8. Generate `REVIEW_REPORT.md` from review gate results.
9. Run `cross-document-consistency-review.py`.
10. Run `human-writing-final-pass.py`.
11. Save final files.

Final documents should be easy to read, but use professional product wording. Do not leave interview questions as PRD content unless they are explicitly marked as unresolved items.

PRD, POLICY, MEASUREMENT, AC, DECISION_LOG, and REVIEW_REPORT must use the same requirement names, priority, operating intent, scalability, and decision state.

If the user asks for Claude Design handoff, also generate:

- `DESIGN_HANDOFF_BRIEF.md`
- `CLAUDE_DESIGN_PROMPT.md`

These design handoff outputs must preserve the same requirement names, priority, operating intent, and scalability. Nice-to-have items stay out of the prototype unless the user explicitly asks to visualize them.

## Required Warning

If total completeness is below 70, warn the user and show missing question candidates. Draft generation is allowed only if the user accepts the draft state.
