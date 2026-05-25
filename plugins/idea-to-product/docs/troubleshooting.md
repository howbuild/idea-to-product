# Troubleshooting

## Python command not found

Windows may use `py` or `python` instead of `python3`.

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/validate.ps1
```

## Hooks do not run

Check:

- runtime hook trust/review status
- plugin root path
- `CLAUDE_PLUGIN_ROOT` availability
- Python availability
- `hooks.claude.json` or `hooks.codex.json` path in plugin manifest

## Codex agents do not install

Some Codex runtime surfaces may not install custom agents natively. Use the reviewer markdown files in `agents/` or run `scripts/install-agents.sh` for a local agent directory.

## Claude Design adds new features

Run `import-design-feedback` and review scope before accepting any new feature.

## Domain assumptions look too certain

Domain packs are question candidates. Mark unconfirmed domain content as assumptions or unresolved items.
