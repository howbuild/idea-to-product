# Final Review Workflow

## Purpose

Check that the final output is internally consistent, readable, and complete enough for developer handoff.

## Steps

1. Run `cross-document-consistency-review.py`.
2. Run `human-writing-final-pass.py`.
3. Run `output-validator.py`.
4. Confirm unresolved assumptions remain marked.
5. Confirm no new MVP feature was added without drift review.
6. Confirm no concrete domain pack was added to the core repo.
7. Confirm Design handoff does not add unapproved features.

## Final Handoff Checklist

- PRD features have matching AC.
- Policies connect to features and screen IDs.
- Measurement events connect to features and KPI.
- Decision log explains why choices were made.
- Human-writing pass removed AI-like wording without removing practical terms.
- Wireframe is labeled as a structural prototype.
- Claude Design handoff is product structure, not final visual style.
