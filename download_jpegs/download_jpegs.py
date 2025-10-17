#!/usr/bin/env python3
"""
Batch‑download JPEGs listed in urls.txt with parallel workers.

Usage:
    python download_jpegs.py
"""

from __future__ import annotations

import pathlib
import concurrent.futures
import logging
import sys
from typing import Final

import requests

# Constants -------------------------------------------------------------------
URL_FILE: Final = pathlib.Path("urls.txt")
DEST_DIR: Final = pathlib.Path("downloads")
MAX_WORKERS: Final = 8
TIMEOUT_S: Final = 30

# Configure logging -----------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)

# Helper functions ------------------------------------------------------------
def download(url: str) -> str:
    """Download *url* into DEST_DIR and return the local filename."""
    filename = DEST_DIR / pathlib.Path(url).name
    try:
        resp = requests.get(url, timeout=TIMEOUT_S)
        resp.raise_for_status()
        filename.write_bytes(resp.content)
        logging.info("✔  %s", filename.name)
    except Exception as exc:  # noqa: BLE001  (broad exception logged)
        logging.error("✘  %s — %s", url, exc)
    return filename.name


def main() -> None:
    """Main entry point."""
    DEST_DIR.mkdir(exist_ok=True)
    urls = [line.strip() for line in URL_FILE.read_text().splitlines() if line.strip()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
        list(exe.map(download, urls))


if __name__ == "__main__":
    main()
