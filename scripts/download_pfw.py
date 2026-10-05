
import argparse
import os
import json
from pathlib import Path
from typing import List
from pfw_client import PFWClient
from pfw_client.client import validate_document_identifier


def save_document(app_dir: Path, identifier: str, extension: str, blob: bytes) -> Path:
    """Create a contained document file without overwriting an existing entry."""
    identifier = validate_document_identifier(identifier)
    if extension not in ("", ".pdf", ".json", ".xml"):
        raise ValueError("Unsupported document file extension")
    filename = identifier + extension
    # Windows treats device names specially even when a suffix is present.
    device_name = filename.split(".", 1)[0].upper()
    if (
        device_name in {"CON", "PRN", "AUX", "NUL"}
        or device_name in {f"COM{n}" for n in range(1, 10)}
        or device_name in {f"LPT{n}" for n in range(1, 10)}
        or filename.endswith(".")
    ):
        raise ValueError("Document identifier is not a portable filename")
    parent = app_dir.resolve(strict=True)
    destination = parent / filename
    if destination.resolve().parent != parent:
        raise ValueError("Document output must remain in its application directory")
    # Exclusive creation refuses existing files, links and name collisions.
    # The caller chooses the application directory; it must remain trusted.
    with destination.open("xb") as handle:
        handle.write(blob)
    return destination

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
                        save_document(app_dir, did, ext or "", blob)
                        print(f"[{appno}] saved {did}{ext or ''}")
                    except Exception as e:
                        print(f"[{appno}] download miss {did}: {e}")
            except Exception as e:
                print(f"[{appno}] unable to process documents.json: {e}")

if __name__ == "__main__":
    main()
