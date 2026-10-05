
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
python -m scripts.download_pfw --outdir .\out --ids .\ids.txt
```

The CLI validates the whole IDs file before creating output or making requests.
Each entry must be one ASCII token beginning with a letter or digit and using
only letters, digits, dots, underscores or hyphens. Leading zeroes and the token
text are preserved; this is a safe CLI path contract, not a numeric-format or
USPTO validity check. Paths, drive names, Windows device names, trailing dots,
surrounding spaces and control characters are refused. Blank lines and normal
LF/CRLF line endings are accepted.

Application directories stay directly beneath the selected output root. Existing
linked directories and linked section JSON files are refused, including hardlink
aliases for section files. Ordinary section JSON files can still be overwritten
on a rerun. The selected root remains caller-controlled and must be trusted;
these static checks do not isolate a run from concurrent directory replacement.

## Notes

- Both headers `X-API-KEY` and `USPTO-API-KEY` are added.
- When no query is supplied to search, the API returns the default top page.

## Document download boundaries

The retained document downloader accepts an opaque ASCII identifier beginning
with a letter or digit and containing only letters, digits, dots, underscores or
hyphens. It places that identifier in one escaped URL path segment; paths, URLs,
queries, fragments and pre-encoded input are refused before a request is sent.
This is the client's safe token contract, rather than a claim that every USPTO
identifier is a UUID or that these characters cover every future service format.

Downloads follow at most three redirects, each confined to HTTPS
`data.uspto.gov` on the standard HTTPS port. Other origins and protocols are
refused before the next request. The downloader retains its existing endpoint
pattern; compatibility with the current live service and any additional required
download origin has not been verified. It does not implement the old docstring's
claimed fallback to arbitrary `downloadUrl` values.

The batch downloader applies the same identifier validation to document output
names, confines each file to its selected application directory, and refuses
Windows device names and trailing-dot filenames. It creates new files
exclusively: existing files, links and filename collisions are reported as a
download miss and preserved. The locally selected output/application directory
must remain trusted; these checks do not provide isolation from another process
concurrently replacing that directory.

Run the offline request-boundary regressions with the existing Python and
Requests installation:

```powershell
python -B -m unittest discover -s tests -v
```

These tests substitute every request and forbid production network access and
API-key lookup. They cover supported token forms, rejected path/query/fragment
input, redirect origin checks and bounds, response cleanup and byte/extension
preservation. Application-input cases also check complete-batch validation,
contained output, link refusal and ordinary metadata reruns.
