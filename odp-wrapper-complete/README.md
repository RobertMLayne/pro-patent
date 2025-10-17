# ODP Wrapper Fetcher (Windows PowerShell 7.5.3)
Targets: Python 3.14, Java 21, openapi-generator-cli 7.16.0.

## Quick start
```powershell
cd <unzipped>\odp-wrapper-complete

# 0) optional: clean venv
if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }

# 1) venv
python -m venv venv
.env\Scripts\Activate.ps1

# 2) deps
pip install -r requirements.txt

# 3) ensure Java 21 in PATH (or run .\scripts\env_java.ps1)
java --version

# 4) generate client
openapi-generator-cli generate `
  -i .\api-spec\odp_wrapper.yaml `
  -g python `
  -o .\src\odp_client

# 5) run
python .\src\download_wrapper.py --outdir .\out
```
