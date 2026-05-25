# Runtime Installation

## Claude Code

Recommended install:

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

## Codex

Recommended install:

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

Interactive flow:

```text
/plugins
```

Review hook trust before enabling lifecycle hooks. Hook scripts can read prompts and generate reports, so the user should explicitly approve them in the runtime.

Custom reviewer-agent support may differ by Codex runtime surface. If agents are not installed natively, use the markdown files in `./agents/` as reviewer instructions or run `scripts/install-agents.sh` for local agent directories.

## Installer vs Marketplace Commands

The install scripts are convenience wrappers around the runtime marketplace commands. They still use each runtime's marketplace registration and plugin install system internally.

- Use the installer for normal installation and refresh.
- Use direct marketplace commands only for debugging, custom sources, or manual runtime checks.
- ZIP packages are local build artifacts and should stay out of the repo.

## Claude Cowork + Claude Design

Use `install-cowork-design.md`.

Cowork supports the product-thinking workflow. Claude Design uses `DESIGN_HANDOFF_BRIEF.md` and `CLAUDE_DESIGN_PROMPT.md` to visualize the agreed product structure.

## Windows and macOS

Use:

```text
install-windows.md
install-macos.md
```

Limitations should be documented, not used to remove runtime support.
