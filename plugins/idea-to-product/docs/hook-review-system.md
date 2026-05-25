# Hook Review System

Hooks are automatic review gates.

Runtime hook definitions live in:

- `hooks/hooks.claude.json`
- `hooks/hooks.codex.json`
- `hooks/hooks.claude.windows.json`
- `hooks/hooks.codex.windows.json`
- `hooks/hooks.json` as a compatibility copy

They use a lifecycle map keyed by `SessionStart`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PostToolUse`, and `Stop`.

Every registered hook is a command hook that executes Python through `${CLAUDE_PLUGIN_ROOT}` so Claude Code and Claude-compatible Codex runtimes can resolve the plugin root.

macOS configs use `python3`. Windows configs use `py -3`.

`UserPromptExpansion` is kept in Claude configs. It is omitted from Codex configs because support can vary by Codex runtime surface.

## Gates

- `user-prompt-scope-router.py`: detects feature, scope, policy, wireframe, and document-generation intent
- `feature-drift-gate.py`: reviews new feature candidates
- `wireframe-change-review.py`: checks structural wireframe changes
- `policy-consistency-review.py`: checks policy, state, permission, and exception coverage
- `measurement-coverage-review.py`: checks events and records
- `completeness-gate.py`: checks PRD completeness before document generation
- `cross-document-consistency-review.py`: checks PRD, AC, POLICY, MEASUREMENT, and DECISION_LOG
- `human-writing-final-pass.py`: checks AI-like wording before final save
- `domain-pack-validator.py`: validates injected domain-pack structure
- `output-validator.py`: validates output files

## Blocking

- Yellow/Red feature reviews require user confirmation.
- Completeness under 70 warns before document generation.
- Consistency and policy issues are conditional blockers depending on runtime policy.
- Human-writing review warns before final save.
