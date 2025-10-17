# Hardened apply (iCloud root)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSDefaultParameterValues = @{'*:ErrorAction' = 'Stop'; 'Get-ChildItem:Force' = $true }

$mapPath = 'C:\Users\WorkstationAdmin\OneDrive\Desktop\icloud_root_mapping_after_clean.csv'
$root = 'C:\Users\WorkstationAdmin\iCloudDrive'
$errorLog = 'C:\Users\WorkstationAdmin\OneDrive\Desktop\apply_errors.txt'
New-Item -ItemType File -Path $errorLog -Force | Out-Null
function Write-Err([string]$m) { Add-Content -LiteralPath $errorLog -Value ("[{0:yyyy-MM-dd HH:mm:ss}] {1}" -f (Get-Date), $m) }

$map = Import-Csv -LiteralPath $mapPath | Where-Object { $_.OldFullName -and $_.NewFullName -and ($_.OldFullName -ne $_.NewFullName) }

# 1) Files: LIVE
$files = $map | Where-Object Type -eq 'File'
foreach ($f in $files) {
    try {
        if (-not (Test-Path -LiteralPath $f.OldFullName)) { Write-Err "Missing file: $($f.OldFullName)"; continue }
        $destDir = [IO.Path]::GetDirectoryName($f.NewFullName)
        if (-not (Test-Path -LiteralPath $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
        if (     (Test-Path -LiteralPath $f.NewFullName)) { Write-Err "Exists, skip: $($f.NewFullName)"; continue }
        Move-Item -LiteralPath $f.OldFullName -Destination $f.NewFullName
    }
    catch { Write-Err ("FILE '{0}' -> '{1}': {2}" -f $f.OldFullName, $f.NewFullName, $_.Exception.Message) }
}

# 2) Directories: PREVIEW (dry-run)
$dirs = $map | Where-Object Type -eq 'Directory' | Sort-Object { $_.OldFullName.Length } -Descending
foreach ($d in $dirs) {
    try {
        if (-not (Test-Path -LiteralPath $d.OldFullName)) { Write-Err "Missing dir: $($d.OldFullName)"; continue }
        $newParent = [IO.Path]::GetDirectoryName($d.NewFullName)
        $newLeaf = [IO.Path]::GetFileName($d.NewFullName)
        if (-not (Test-Path -LiteralPath $newParent)) { New-Item -ItemType Directory -Path $newParent -Force | Out-Null }
        if (     (Test-Path -LiteralPath $d.NewFullName)) { Write-Err "Dir exists, skip: $($d.NewFullName)"; continue }
        $oldParent = [IO.Path]::GetDirectoryName($d.OldFullName)
        if ($oldParent -ieq $newParent) { Rename-Item -LiteralPath $d.OldFullName -NewName $newLeaf }
        else { Move-Item   -LiteralPath $d.OldFullName -Destination $d.NewFullName }
    }
    catch { Write-Err ("DIR '{0}' -> '{1}': {2}" -f $d.OldFullName, $d.NewFullName, $_.Exception.Message) }
}

# 3) Prune empties under root: PREVIEW
Get-ChildItem -LiteralPath $root -Recurse -Directory |
Sort-Object FullName -Descending |
Where-Object { -not (Get-ChildItem -LiteralPath $_.FullName -Force -Recurse | Select-Object -First 1) } |
Remove-Item -Force
