
import argparse
import os
import json
from pathlib import Path
from typing import List
from pfw_client import PFWClient, HTTPError

def load_ids(p: str) -> List[str]:
    with open(p, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--ids", required=True, help="text file of application numbers, one per line")
    ap.add_argument("--sections", default="meta,transactions,documents,associated", 
                    help="comma list: meta,adjustment,assignment,attorney,continuity,foreign,transactions,documents,associated")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    cli = PFWClient()

    section_map = {
        "meta": cli.meta_data,
        "adjustment": cli.adjustment,
        "assignment": cli.assignment,
        "attorney": cli.attorney,
        "continuity": cli.continuity,
        "foreign": cli.foreign_priority,
        "transactions": cli.transactions,
        "documents": cli.documents,
        "associated": cli.associated_documents,
    }
    selected = [s.strip() for s in args.sections.split(",") if s.strip()]

    for appno in load_ids(args.ids):
        print(f"== {appno}")
        app_dir = Path(args.outdir) / appno
        app_dir.mkdir(parents=True, exist_ok=True)

        for s in selected:
            fn = section_map.get(s)
            if not fn:
                continue
            try:
                data = fn(appno)
                with open(app_dir / f"{s}.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                print(f"[{appno}] saved {s}.json")
            except Exception as e:
                print(f"[{appno}] ERROR {s}: {e}")

        # If documents.json present, attempt raw file downloads by identifier
        docs_json = app_dir / "documents.json"
        if docs_json.exists():
            try:
                with open(docs_json, "r", encoding="utf-8") as f:
                    dj = json.load(f)
                # heuristic: find common key names
                identifiers = set()
                for item in dj.get("documents", []):
                    doc_id = item.get("documentIdentifier") or item.get("documentId") or item.get("document_id")
                    if doc_id:
                        identifiers.add(doc_id)
                for did in identifiers:
                    try:
                        blob, ext = cli.download_document(did)
                        with open(app_dir / f"{did}{ext or ''}", "wb") as f:
                            f.write(blob)
                        print(f"[{appno}] saved {did}{ext or ''}")
                    except Exception as e:
                        print(f"[{appno}] download miss {did}: {e}")
            except Exception as e:
                print(f"[{appno}] unable to process documents.json: {e}")

if __name__ == "__main__":
    main()
