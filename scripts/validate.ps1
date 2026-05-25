$ErrorActionPreference = "Stop"

$pythonCandidates = @("py", "python", "python3")
$python = $null

foreach ($candidate in $pythonCandidates) {
  $cmd = Get-Command $candidate -ErrorAction SilentlyContinue
  if ($cmd) {
    $python = $candidate
    break
  }
}

if (-not $python) {
  throw "Python was not found. Install Python and make py or python available in PATH."
}

& $python scripts/validate-manifests.py
& $python scripts/validate-python-hooks.py
& $python plugins/idea-to-product/hooks/output-validator.py --manifest
