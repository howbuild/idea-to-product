# Install: macOS

macOS is a supported operating system for Idea to Product.

## Validate

From the repo root:

```bash
./scripts/validate.sh
```

Or run directly:

```bash
python3 scripts/validate-manifests.py
python3 scripts/validate-python-hooks.py
python3 plugins/idea-to-product/hooks/output-validator.py --manifest
```

## Claude Code

Use `install-claude-code.md`.

## Codex

Use `install-codex.md`.

## Claude Cowork + Design

Use `install-cowork-design.md`.

## macOS Notes

- `python3` is the preferred command.
- Hook commands use quoted paths.
- Runtime hook trust/review may be required before automatic execution.
