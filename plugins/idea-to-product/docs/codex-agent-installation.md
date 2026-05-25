# Codex Agent Installation Notes

Codex can install plugin skills and hook definitions through the plugin package, but custom reviewer agents may not be natively installed by every Codex runtime or marketplace surface.

## What Works As Plugin Content

- skills from `./skills/`
- hooks from `./hooks/hooks.json`
- documentation, templates, workflows, commands, and examples as plugin files

## Reviewer Agents

Reviewer agents live in:

```text
./agents/
```

If the active Codex runtime supports plugin-provided agents, install them directly from that directory.

If not, use the agents as instruction files. The workflow and hooks can still reference them by name, and the runtime can read the matching markdown file when a review is needed.

## Manual Helper

Use `scripts/install-agents.sh` only when the local runtime expects agent markdown files in a separate directory.

The helper copies agent markdown files. It does not create credentials, tokens, secrets, or MCP configuration.
