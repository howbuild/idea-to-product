# File Manifest

This manifest records the intended marketplace-ready repository layout.

## Root

- `README.md`: product overview, installation, domain injection, assumptions
- `README.ko.md`: Korean overview and runtime support summary
- `AGENTS.md`: repository-level agent instructions
- `PLUGIN.md`: plugin architecture and runtime shape
- `FILE_MANIFEST.md`: file inventory
- `LICENSE`: MIT license
- `install.sh`: macOS/Linux/WSL/Git Bash installer wrapper for Codex and Claude Code
- `install.ps1`: Windows PowerShell installer wrapper for Codex and Claude Code
- `package.json`: package metadata
- `plugin.yaml`: root plugin marketplace metadata
- `.agents/plugins/marketplace.json`: repository marketplace registration metadata
- `.claude-plugin/marketplace.json`: Claude Code root marketplace registration metadata

## Plugin Root

- `plugins/idea-to-product/README.md`
- `plugins/idea-to-product/AGENTS.md`
- `plugins/idea-to-product/PLUGIN.md`
- `plugins/idea-to-product/FILE_MANIFEST.md`
- `plugins/idea-to-product/plugin.yaml`

## Runtime Metadata

- `plugins/idea-to-product/.claude-plugin/plugin.json`
- `plugins/idea-to-product/.claude-plugin/install.md`
- `plugins/idea-to-product/.codex-plugin/plugin.json`
- `plugins/idea-to-product/.codex-plugin/install.md`

## Core Components

- `workflows/`: PM process definitions
- `commands/`: user entrypoints
- `hooks/`: lifecycle hook scripts, maps, and prompts
- `agents/`: specialist reviewer instructions
- `skills/`: reusable supporting skills
- `domains/`: domain-pack template and registry example
- `templates/`: output document templates
- `mcp/`: MCP suggestions and example config
- `docs/`: operating guides and build criteria
- `examples/`: generic output sample
- `assets/`: placeholder marketplace assets
- `scripts/install-agents.sh`: optional helper for runtimes that need separate reviewer-agent installation
- `scripts/validate-manifests.py`: manifest validator
- `scripts/validate-python-hooks.py`: Python hook validator
- `scripts/package-claude-plugin.py`: Claude plugin package helper
- `scripts/package-codex-plugin.py`: Codex plugin package helper
- `scripts/run-hook.py`: OS-friendly manual hook runner
- `scripts/validate.sh`: macOS/Linux validation entrypoint
- `scripts/validate.ps1`: Windows PowerShell validation entrypoint

## Reference Research Components

- `workflows/reference-discovery.md`
- `workflows/competitive-pattern-review.md`
- `commands/research-references.md`
- `commands/compare-products.md`
- `hooks/reference-gap-review.py`
- `hooks/source-quality-review.py`
- `hooks/copy-risk-review.py`
- `agents/reference-researcher.md`
- `agents/competitive-pattern-reviewer.md`
- `skills/reference-synthesizer/`
- `skills/competitive-pattern-extractor/`
- `templates/reference-research.md`
- `templates/design-handoff-brief.md`
- `templates/claude-design-prompt.md`
- `templates/design-feedback-log.md`
- `domains/_template/reference-sources.md`
- `domains/_template/design-handoff-notes.md`

## Explicitly Excluded

The core repo must not include concrete domain packs such as:

- `domains/cs-commerce/`
- `domains/construction/`
- `domains/healthcare/`
- `domains/fintech/`
