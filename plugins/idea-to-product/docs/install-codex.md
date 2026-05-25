# Install: Codex

Codex is a first-class runtime for Idea to Product.

## Marketplace File

```text
.agents/plugins/marketplace.json
```

The plugin source path is:

```text
./plugins/idea-to-product
```

## Interactive Install

Use the Codex plugin UI when available:

```text
/plugins
```

## Recommended Install

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --codex
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

Local testing after cloning:

```bash
./install.sh --codex
```

```powershell
.\install.ps1 -Target codex
```

The installer wraps the Codex marketplace flow and refreshes an existing `idea-to-product-marketplace` registration when needed.

## Provided Capabilities

- `.codex-plugin/plugin.json`
- skills
- hook scripts and hook maps as review-gate files
- MCP example
- commands/workflows/docs as plugin files

## Hook Trust

Codex hooks may require trust/review before automatic execution. Do not remove Codex support when a runtime surface requires setup; document the limitation and use manual review checkpoints when needed.

## Agents

Custom reviewer agents may not be natively installed by every Codex runtime surface. See `codex-agent-installation.md`.
