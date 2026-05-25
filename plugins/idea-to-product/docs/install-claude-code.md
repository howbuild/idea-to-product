# Install: Claude Code

Claude Code is a first-class runtime for Idea to Product.

## Local Marketplace

Root marketplace file:

```text
.claude-plugin/marketplace.json
```

Plugin source:

```text
./plugins/idea-to-product
```

## Local Test

```bash
claude --plugin-dir ./plugins/idea-to-product
```

## Recommended Install

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --claude
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

Local testing after cloning:

```bash
./install.sh --claude
```

```powershell
.\install.ps1 -Target claude
```

The installer wraps the Claude Code marketplace flow and refreshes an existing `idea-to-product-marketplace` registration when needed.

## Provided Capabilities

- plugin manifest
- commands
- hooks
- agents
- workflows
- skills
- Python review gates
- MCP suggestions

## Hook Trust

Claude Code should ask the user to review/trust hook commands before automatic execution. Hook commands run Python scripts from the plugin root.
