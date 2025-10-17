param(
    [Parameter(Mandatory = $true)][string]$MapCsv,
    [Parameter(Mandatory = $true)][string]$OutCleanCsv,
    [Parameter(Mandatory = $true)][string]$OutMissingCsv,
    [Parameter(Mandatory = $true)][string]$OutDupsCsv
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$map = Import-Csv -LiteralPath $MapCsv | Where-Object { $_.OldFullName -and $_.NewFullName -and ($_.OldFullName -ne $_.NewFullName) }
$missing = $map | Where-Object { -not (Test-Path -LiteralPath $_.OldFullName) }
$clean = $map | Where-Object { (Test-Path -LiteralPath $_.OldFullName) }
$dupsGrp = $clean | Group-Object NewFullName | Where-Object Count -gt 1
$dups = if ($dupsGrp) { $dupsGrp | ForEach-Object { $_.Group } } else { @() }

$missing | Export-Csv -LiteralPath $OutMissingCsv -NoTypeInformation -Encoding UTF8
$dups    | Export-Csv -LiteralPath $OutDupsCsv    -NoTypeInformation -Encoding UTF8
$clean   | Export-Csv -LiteralPath $OutCleanCsv   -NoTypeInformation -Encoding UTF8

'{0} kept; {1} missing; {2} dup-target groups' -f @($clean).Count, @($missing).Count, @($dupsGrp).Count
