& .\scripts\env_java.ps1 | Out-Host
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
openapi-generator-cli generate `
  -i .\api-spec\odp_wrapper.yaml `
  -g python `
  -o .\src\odp_client
python .\src\download_wrapper.py --outdir .\out
