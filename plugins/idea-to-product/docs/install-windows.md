# Install: Windows

Windows is a supported operating system for Idea to Product.

## Quick Install

Install Codex and Claude Code support from Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex
```

Install only one runtime:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

For local testing after cloning the repo:

```powershell
.\install.ps1
.\install.ps1 -Target codex
.\install.ps1 -Target claude
```

## Python Command

Windows may use:

```powershell
py
python
python3
```

The validation script tries `py`, then `python`, then `python3`.

## Validate

From the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/validate.ps1
```

Or run directly:

```powershell
py scripts/validate-manifests.py
py scripts/validate-python-hooks.py
py plugins/idea-to-product/hooks/output-validator.py --manifest
```

## Windows Hook Config

Use the Windows hook configs when the runtime allows selecting a hook config file:

```text
plugins/idea-to-product/hooks/hooks.claude.windows.json
plugins/idea-to-product/hooks/hooks.codex.windows.json
```

These configs use `py -3` instead of `python3`.

## Claude Code

Use the Claude Code install flow in `install-claude-code.md`. If `python3` is unavailable, use `hooks.claude.windows.json` or use `scripts/run-hook.py` for manual hook validation.

## Codex

Use the Codex install flow in `install-codex.md`. Hooks may require trust/review before running.

## Claude Cowork + Design

Use `install-cowork-design.md` and the design handoff workflow.

## Windows Notes

- Paths may contain spaces, so commands quote paths.
- Do not require symlinks.
- Do not require `chmod`.
- Python hooks use `pathlib`.
- Files are UTF-8 markdown, JSON, YAML, and Python.
