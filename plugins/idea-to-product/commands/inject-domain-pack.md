---
description: Read an external domain pack as question and policy candidates.
---

# Command: inject-domain-pack

Use when the user provides external domain context.

## Supported Modes

- path-based injection
- alias-based injection
- conversation-based injection
- document-based injection
- MCP-based injection

## Run

1. Identify injection mode.
2. If path or alias is used, run `domain-pack-validator.py`.
3. Read glossary, question bank, policy checklist, measurement checklist, wireframe patterns, and MCP suggestions when available.
4. Mark all domain-derived items as question candidates.
5. Ask for confirmation before turning a candidate into policy or scope.

## Rule

Domain context is not confirmed product truth until the user confirms it.
