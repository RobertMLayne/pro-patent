# 02_build_icloud_mapping.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Root,      # e.g. C:\Users\...\iCloudDrive
    [Parameter(Mandatory = $true)][string]$InCsv,     # from step 1
    [Parameter(Mandatory = $true)][string]$OutCsv     # proposed mapping
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Helpers
function Get-ShortHash {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string]$InputString,
        [int]$Length = 6
    )
    $md5 = [System.Security.Cryptography.MD5]::Create()
    $hex = -join ($md5.ComputeHash([Text.Encoding]::UTF8.GetBytes($InputString)) |
        ForEach-Object { $_.ToString('x2') })
    return $hex.Substring(0, [Math]::Min($Length, $hex.Length))
}

$invalidRe = '[\"*:<>?/\\|]'            # Windows/OneDrive disallowed chars
$reservedRe = '^(con|prn|aux|nul|com[1-9]|lpt[1-9])$'
$segmentMax = 80
$targetMax = 240

function ConvertTo-SafeSegment {
    [CmdletBinding()]
    param([Parameter(Mandatory = $true)][string]$Segment)

    if ([string]::IsNullOrWhiteSpace($Segment)) {
        return ('_{0}' -f (Get-ShortHash -InputString ([guid]::NewGuid().ToString())))
    }

    $s = $Segment -replace $invalidRe, '-'
    $s = $s.Trim().Trim('.')
    $s = ($s -replace '\s+', ' ')
    if ($s -match $reservedRe) { $s = "${s}_" }

    if ($s.Length -le $segmentMax) { return $s }

    $base = $s.Substring(0, [Math]::Min(60, $s.Length))
    return ('{0}~{1}' -f $base, (Get-ShortHash -InputString $s -Length 8))
}

function Compress-PathToLength {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][string[]]$Segments,
        [Parameter(Mandatory = $true)][int]$MaxLength,
        [Parameter(Mandatory = $true)][string]$BasePath
    )

    # ensure array semantics
    $Segments = @($Segments)
    $base = $BasePath.TrimEnd([char]'\')
    $cur = if ($Segments.Count -gt 0) { $base + '\' + ($Segments -join '\') } else { $base }
    if ($cur.Length -le $MaxLength) { return $Segments }

    $idxs = 0..($Segments.Count - 1)
    while ($cur.Length -gt $MaxLength -and $Segments.Count -gt 0) {
        $i = ($idxs | Sort-Object { $Segments[$_].Length } -Descending | Select-Object -First 1)
        $seg = $Segments[$i]
        if ($seg.Length -le 16) { break } # can't safely shrink further
        $Segments[$i] = ($seg.Substring(0, [Math]::Min(12, $seg.Length)) + '~' +
            (Get-ShortHash -InputString $seg -Length 6))
        $cur = $base + '\' + ($Segments -join '\')
    }
    return $Segments
}

# Build mapping
$rootNorm = $Root.TrimEnd([char]'\')
$rows = Import-Csv -LiteralPath $InCsv
$seenTargets = [System.Collections.Generic.HashSet[string]]::new()

$map = foreach ($r in $rows) {
    if (-not $r.FullName) { continue }
    if ($r.FullName -notlike "$rootNorm*") { continue }

    $rel = $r.FullName.Substring($rootNorm.Length).TrimStart([char]'\')
    if ([string]::IsNullOrEmpty($rel)) { continue }

    $parts = $rel -split '\\'
    $newParts = @(
        foreach ($p in $parts) { ConvertTo-SafeSegment -Segment $p }
    )
    $newParts = Compress-PathToLength -Segments $newParts -MaxLength $targetMax -BasePath $rootNorm

    $newFull = $rootNorm + '\' + ($newParts -join '\')

    # De-dupe targets deterministically
    $cand = $newFull
    if ($seenTargets.Contains($cand)) {
        $newParts = @($newParts) # ensure array
        $leaf = [string]$newParts[-1]
        $newParts[-1] = ('{0}-{1}' -f $leaf.TrimEnd('.'), (Get-ShortHash -InputString $cand -Length 6))
        $cand = $rootNorm + '\' + ($newParts -join '\')
    }
    $null = $seenTargets.Add($cand)

    if ($r.FullName -ne $cand) {
        [pscustomobject]@{
            Type        = $r.Type
            OldFullName = $r.FullName
            NewFullName = $cand
        }
    }
}

$map | Export-Csv -LiteralPath $OutCsv -NoTypeInformation -Encoding UTF8
