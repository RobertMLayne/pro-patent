
import argparse
import json
import os
import re
import stat
from pathlib import Path
from typing import List

from pfw_client import PFWClient
from pfw_client.client import validate_document_identifier

_WINDOWS_DEVICE_NAMES = (
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{n}" for n in range(1, 10)}
    | {f"LPT{n}" for n in range(1, 10)}
)
_APPLICATION_NUMBER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
_SECTION_NAMES = {
    "meta", "adjustment", "assignment", "attorney", "continuity", "foreign",
    "transactions", "documents", "associated",
}


def validate_application_number(application_number: str) -> str:
    """Keep the API token intact while refusing ambiguous path components."""
    if (
        not isinstance(application_number, str)
        or not _APPLICATION_NUMBER.fullmatch(application_number)
        or application_number.endswith(".")
        or application_number.split(".", 1)[0].upper() in _WINDOWS_DEVICE_NAMES
    ):
        raise ValueError("Application number must be one portable ASCII token")
    return application_number


def _is_link(info: os.stat_result) -> bool:
    # lstat exposes Windows junctions/reparse points as well as POSIX links.
    return bool(
        stat.S_ISLNK(info.st_mode)
        or getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def _application_directory(output_root: Path, application_number: str) -> Path:
    root = output_root.resolve()
    candidate = root / validate_application_number(application_number)
    try:
        info = candidate.lstat()
    except FileNotFoundError:
        info = None
    if info is not None and (_is_link(info) or not stat.S_ISDIR(info.st_mode)):
        raise ValueError("Application output directory must be an ordinary directory")
    if candidate.resolve().parent != root:
        raise ValueError("Application output must remain in the selected output root")
    return candidate


def _section_path(app_dir: Path, section: str) -> Path:
    if section not in _SECTION_NAMES:
        raise ValueError("Unknown application data section")
    destination = app_dir / f"{section}.json"
    try:
        info = destination.lstat()
    except FileNotFoundError:
        info = None
    if info is not None and (
        _is_link(info) or not stat.S_ISREG(info.st_mode) or info.st_nlink != 1
    ):
        raise ValueError("Section JSON must be an ordinary file with one link")
    if destination.resolve().parent != app_dir.resolve():
        raise ValueError("Section JSON must remain in its application directory")
    return destination


def _document_filename(identifier: str, extension: str) -> str:
    """Build one portable filename from an opaque document identifier."""
    identifier = validate_document_identifier(identifier)
    if extension not in ("", ".pdf", ".json", ".xml"):
        raise ValueError("Unsupported document file extension")
    filename = identifier + extension
    # Windows treats device names specially even when a suffix is present.
    device_name = filename.split(".", 1)[0].upper()
    if (
        device_name in _WINDOWS_DEVICE_NAMES
        or filename.endswith(".")
    ):
        raise ValueError("Document identifier is not a portable filename")
    return filename


def save_document(app_dir: Path, identifier: str, extension: str, blob: bytes) -> Path:
    """Create a contained document file without overwriting an existing entry."""
    filename = _document_filename(identifier, extension)
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
    identifiers = []
    with open(p, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            identifier = line.rstrip("\r\n")
            if not identifier:
                continue
            try:
                identifiers.append(validate_application_number(identifier))
            except ValueError:
                raise ValueError(
                    f"Invalid application number on IDs-file line {line_number}"
                ) from None
    return identifiers

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--ids", required=True, help="text file of application numbers, one per line")
    ap.add_argument("--sections", default="meta,transactions,documents,associated", 
                    help="comma list: meta,adjustment,assignment,attorney,continuity,foreign,transactions,documents,associated")
    args = ap.parse_args()

    # Validate the entire batch before creating outputs or constructing a
    # client. Selecting an IDs file does not make its contents trustworthy.
    application_numbers = load_ids(args.ids)
    output_root = Path(args.outdir).resolve()
    selected = [s.strip() for s in args.sections.split(",") if s.strip()]
    application_directories = [
        (appno, _application_directory(output_root, appno))
        for appno in application_numbers
    ]
    for _, app_dir in application_directories:
        # documents.json is also read when document metadata was retained
        # from an earlier run. Refuse static aliases before any request.
        for section in (set(selected) & _SECTION_NAMES) | {"documents"}:
            _section_path(app_dir, section)
    output_root.mkdir(parents=True, exist_ok=True)
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
    for appno, app_dir in application_directories:
        print(f"== {appno}")
        _application_directory(output_root, appno)
        app_dir.mkdir(parents=True, exist_ok=True)

        for s in selected:
            fn = section_map.get(s)
            if not fn:
                continue
            try:
                data = fn(appno)
                with open(_section_path(app_dir, s), "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                print(f"[{appno}] saved {s}.json")
            except Exception as e:
                print(f"[{appno}] ERROR {s}: {e}")

        # If documents.json present, attempt raw file downloads by identifier
        docs_json = _section_path(app_dir, "documents")
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
