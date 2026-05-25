# Codex Install

Recommended install:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --codex
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="codex"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

Local testing after cloning the repo:

```bash
./install.sh --codex
```

```powershell
.\install.ps1 -Target codex
```

Interactive flow:

```text
/plugins
```

Then select the local or marketplace Idea to Product plugin entry.

The installer is a wrapper around the Codex marketplace flow. It registers `idea-to-product-marketplace`, installs `idea-to-product`, and refreshes an existing registration when needed.

Before enabling automatic review gates, run the Codex hooks trust review when the active runtime supports hook configuration. This plugin includes lifecycle scripts that inspect prompts, wireframe changes, document generation, and final outputs. The user should explicitly trust or approve those hooks before they run automatically.

After install:

1. Start with the `start` command.
2. Use `add-feature` whenever a user wants to add a new feature.
3. Use `generate-docs` only after the completeness gate has run or the user accepts draft generation.

## Agent Installation Limitation

Some Codex runtime surfaces can read plugin skills and hooks but may not natively install custom reviewer agents.

If reviewer agents are not installed automatically, keep using the plugin and read agent markdown files from:

```text
./agents/
```

For local runtimes that expect a separate agents directory, use:

```bash
plugins/idea-to-product/scripts/install-agents.sh
```
