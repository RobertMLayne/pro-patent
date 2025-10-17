# 01_export_icloud_root_structure.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Root,
    [Parameter(Mandatory = $true)][string]$OutCsv
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Enumerate everything once; use PSIsContainer to tell files vs. folders
$items = Get-ChildItem -LiteralPath $Root -Force -Recurse

$rows = foreach ($it in $items) {
    $isDir = $it.PSIsContainer
    [pscustomobject]@{
        Type         = if ($isDir) { 'Directory' } else { 'File' }
        FullName     = $it.FullName
        Name         = $it.Name
        Extension    = if ($isDir) { '' } else { [IO.Path]::GetExtension($it.Name) }
        Directory    = if ($isDir) { $it.FullName } else { $it.DirectoryName }
        Length       = if ($isDir) { '' } else { $it.Length }
        FullNameLen  = $it.FullName.Length
        Depth        = ($it.FullName.Substring($Root.TrimEnd('\').Length).TrimStart('\') -split '\\').Count
        LastWriteUtc = $it.LastWriteTimeUtc
    }
}

$rows | Export-Csv -LiteralPath $OutCsv -NoTypeInformation -Encoding UTF8
Write-Host "Wrote structure: $OutCsv"
