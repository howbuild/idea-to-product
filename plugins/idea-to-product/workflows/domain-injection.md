# Domain Injection Workflow

## Purpose

Inject external domain context without making the core plugin domain-specific.

## Supported Modes

1. Path-based injection
2. Alias-based injection
3. Conversation-based injection
4. Document-based injection
5. MCP-based injection

## Rules

- A domain pack is a source of question candidates.
- A domain pack is not confirmed policy.
- User confirmation is required before any domain-derived item becomes a requirement.
- Unconfirmed items must be marked as assumptions or unresolved.
- Core repo must not include concrete domain packs.

## Validation

Run `domain-pack-validator.py` for path-based or alias-based domain packs.

Required files:

- `domain.yaml`
- `glossary.md`
- `question-bank.md`
- `policy-checklist.md`
- `measurement-checklist.md`
- `wireframe-patterns.md`
- `design-handoff-notes.md`
- `mcp-suggestions.md`
- `reference-sources.md`
