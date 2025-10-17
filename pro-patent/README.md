
# PFW Wrapper GUI

Local tools for USPTO Patent File Wrapper search and retrieval.

## Install

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configure

Set your USPTO Open Data Portal API key:

```powershell
$env:ODP_API_KEY="YOUR_KEY"   # for current session
# or permanently:
setx ODP_API_KEY "YOUR_KEY"
```

## Run GUI

```powershell
python .\gui.py
```

## CLI: download documents for application IDs

Put application numbers in `ids.txt`, one per line, then run:

```powershell
python .\scripts\download_pfw.py --outdir .\out --ids .\ids.txt
```

## Notes

- Both headers `X-API-KEY` and `USPTO-API-KEY` are added.
- When no query is supplied to search, the API returns the default top page.
