param(
  [ValidateSet("all", "codex", "claude")]
  [string]$Target = $(if ($env:ITP_INSTALL_TARGET) { $env:ITP_INSTALL_TARGET } else { "all" }),
  [string]$Source = $env:MARKETPLACE_SOURCE
)

$ErrorActionPreference = "Stop"

$PluginName = "idea-to-product"
$MarketplaceName = "idea-to-product-marketplace"
$DefaultRemoteSource = "https://github.com/howbuild/idea-to-product"

if ([string]::IsNullOrWhiteSpace($Source)) {
  $LocalMarketplace = Join-Path (Get-Location).Path ".agents/plugins/marketplace.json"
  $LocalPlugin = Join-Path (Get-Location).Path "plugins/$PluginName"

  if ((Test-Path -LiteralPath $LocalMarketplace) -and (Test-Path -LiteralPath $LocalPlugin)) {
    $Source = (Get-Location).Path
  } else {
    $Source = $DefaultRemoteSource
  }
}

function Invoke-Checked {
  param(
    [Parameter(Mandatory = $true)][string]$Command,
    [Parameter(Mandatory = $true)][string[]]$Arguments
  )

  & $Command @Arguments
  if ($LASTEXITCODE -ne 0) {
    throw "Command failed: $Command $($Arguments -join ' ')"
  }
}

function Resolve-CommandPath {
  param([Parameter(Mandatory = $true)][string]$Name)

  $Command = Get-Command $Name -ErrorAction SilentlyContinue
  if ($Command) {
    return $Command.Source
  }
  return $null
}

function Resolve-Codex {
  if ($env:CODEX_BIN -and (Test-Path -LiteralPath $env:CODEX_BIN)) {
    return $env:CODEX_BIN
  }

  return Resolve-CommandPath "codex"
}

function Resolve-Claude {
  if ($env:CLAUDE_BIN -and (Test-Path -LiteralPath $env:CLAUDE_BIN)) {
    return $env:CLAUDE_BIN
  }

  return Resolve-CommandPath "claude"
}

function Install-CodexPlugin {
  $Codex = Resolve-Codex
  if (-not $Codex) {
    Write-Warning "Skipping Codex: codex CLI was not found."
    return
  }

  Write-Host "Installing $PluginName for Codex from: $Source"

  $Marketplaces = & $Codex plugin marketplace list 2>$null
  if ($LASTEXITCODE -ne 0) {
    throw "Unable to list Codex marketplaces."
  }

  if ($Marketplaces -match "^$([regex]::Escape($MarketplaceName))\s") {
    Invoke-Checked -Command $Codex -Arguments @("plugin", "marketplace", "remove", $MarketplaceName)
  }

  Invoke-Checked -Command $Codex -Arguments @("plugin", "marketplace", "add", $Source)
  Invoke-Checked -Command $Codex -Arguments @("plugin", "add", "$PluginName@$MarketplaceName")
}

function Install-ClaudePlugin {
  $Claude = Resolve-Claude
  if (-not $Claude) {
    Write-Warning "Skipping Claude Code: claude CLI was not found."
    return
  }

  Write-Host "Installing $PluginName for Claude Code from: $Source"

  $Marketplaces = & $Claude plugin marketplace list 2>$null
  if ($LASTEXITCODE -ne 0) {
    throw "Unable to list Claude Code marketplaces."
  }

  if ($Marketplaces -match [regex]::Escape($MarketplaceName)) {
    Invoke-Checked -Command $Claude -Arguments @("plugin", "marketplace", "remove", $MarketplaceName)
  }

  Invoke-Checked -Command $Claude -Arguments @("plugin", "marketplace", "add", $Source)

  $Installed = & $Claude plugin list 2>$null
  if ($LASTEXITCODE -ne 0) {
    throw "Unable to list Claude Code plugins."
  }

  if ($Installed -match [regex]::Escape("$PluginName@$MarketplaceName")) {
    Invoke-Checked -Command $Claude -Arguments @("plugin", "update", "$PluginName@$MarketplaceName")
  } else {
    Invoke-Checked -Command $Claude -Arguments @("plugin", "install", "$PluginName@$MarketplaceName")
  }
}

switch ($Target) {
  "all" {
    Install-CodexPlugin
    Install-ClaudePlugin
  }
  "codex" {
    Install-CodexPlugin
  }
  "claude" {
    Install-ClaudePlugin
  }
}

Write-Host "Done."
