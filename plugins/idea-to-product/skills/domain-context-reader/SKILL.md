---
name: domain-context-reader
description: Reads external domain packs or user-provided domain descriptions as question candidates, not confirmed policy, and marks unconfirmed items as assumptions or unresolved.
---

# Domain Context Reader

## Role

Read an external domain pack or user-provided domain explanation.

## Rules

- Do not create real domain packs in core.
- Treat domain packs as question candidates.
- Do not use domain-pack content as confirmed policy before user confirmation.
- Mark unconfirmed items as assumptions or unresolved.
- Treat `reference-sources.md` as reference types, not confirmed product facts.

## References

- `references/domain-pack-schema.md`
- `references/external-domain-pack-rules.md`
