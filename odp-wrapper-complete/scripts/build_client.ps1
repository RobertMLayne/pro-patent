param(
  [string]$SpecPath = ".\api-spec\odp_wrapper.yaml",
  [string]$OutDir = ".\src\odp_client"
)
& .\scripts\env_java.ps1 | Out-Host
openapi-generator-cli generate `
  -i $SpecPath `
  -g python `
  -o $OutDir
