$ErrorActionPreference = 'Stop'
$slidevTaskRoot = $PSScriptRoot
$slidevTaskNode = Get-Command node -ErrorAction SilentlyContinue
if (-not $slidevTaskNode) {
    $slidevTaskBundled = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
    if (Test-Path -LiteralPath $slidevTaskBundled) { $slidevTaskNodePath = $slidevTaskBundled }
    else { throw 'Install Node.js 22 or later, then run this launcher again.' }
} else { $slidevTaskNodePath = $slidevTaskNode.Source }
Write-Host 'Open http://127.0.0.1:3033 in your browser. Press Ctrl+C here to stop.'
& $slidevTaskNodePath (Join-Path $slidevTaskRoot 'scripts/serve.mjs')
