# Claude Code Install

Recommended install:

```bash
curl -fsSL https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.sh | sh -s -- --claude
```

Windows PowerShell:

```powershell
$env:ITP_INSTALL_TARGET="claude"; irm https://raw.githubusercontent.com/howbuild/idea-to-product/main/install.ps1 | iex; Remove-Item Env:ITP_INSTALL_TARGET
```

Local testing after cloning the repo:

```bash
./install.sh --claude
```

```powershell
.\install.ps1 -Target claude
```

The installer is a wrapper around the Claude Code marketplace flow. It registers `idea-to-product-marketplace`, installs `idea-to-product`, and refreshes an existing registration when needed.

After install:

1. Start with `start.md` or the runtime command mapped to it.
2. Review lifecycle hooks before enabling them.
3. Keep domain packs external unless the user injects one.

Runtime syntax can differ by installed Claude Code version. If local syntax differs, keep the plugin root unchanged and adjust only the runtime install command.
