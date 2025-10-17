Param(
  [string]$PreferredJava21 = "C:\Program Files\RedHat\java-21-openjdk-21.0.8.0.9-1",
  [switch]$Persist
)
$bin = Join-Path $PreferredJava21 "bin"
if (-not (Test-Path $bin)) {
  $paths = & where.exe java 2>$null
  if ($paths) {
    $javaPath = $paths | Where-Object { $_ -like "*java-21*" } | Select-Object -First 1
    if ($javaPath) { $bin = Split-Path $javaPath -Parent }
    else { Write-Error "No Java 21 found. Install it."; exit 1 }
  } else { Write-Error "No java.exe found."; exit 1 }
}
$env:JAVA_HOME = Split-Path $bin -Parent
$env:Path = "$bin;" + $env:Path
java --version
if ($Persist) {
  [System.Environment]::SetEnvironmentVariable("JAVA_HOME", $env:JAVA_HOME, "User")
  $u = [System.Environment]::GetEnvironmentVariable("Path","User")
  if ($u -and $u.ToLower().StartsWith("$bin;") -eq $false) {
    [System.Environment]::SetEnvironmentVariable("Path", "$bin;$u", "User")
  }
}
