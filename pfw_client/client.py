
import os
import time
import json
import re
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
import requests

BASE_URL = "https://api.uspto.gov"
_DOCUMENT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
_DOCUMENT_REDIRECTS = {301, 302, 303, 307, 308}
_MAX_DOCUMENT_REDIRECTS = 3


def validate_document_identifier(document_identifier: str) -> str:
    # Identifiers are opaque tokens, not URLs or paths. Do not assume a UUID
    # format: retained PFW examples also use alphanumeric document identifiers.
    if (
        not isinstance(document_identifier, str)
        or not _DOCUMENT_ID.fullmatch(document_identifier)
    ):
        raise ValueError(
            "Document identifier must be a single ASCII token using "
            "letters, digits, '.', '_' or '-'"
        )
    return document_identifier


def _document_url(document_identifier: str) -> str:
    identifier = validate_document_identifier(document_identifier)
    return (
        "https://data.uspto.gov/patent-file-wrapper/documents/"
        + quote(identifier, safe="")
    )


def _document_redirect(url: str, location: str) -> str:
    if (
        not isinstance(location, str)
        or not location
        or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in location)
        or "\\" in location
        or "#" in location
    ):
        raise HTTPError("Invalid document download redirect")
    try:
        target = urlsplit(urljoin(url, location))
        if (
            target.scheme != "https"
            or target.hostname != "data.uspto.gov"
            or target.port not in (None, 443)
            or target.username is not None
            or target.password is not None
            or target.fragment
        ):
            raise ValueError("Unapproved origin")
    except ValueError:
        # Do not expose a Location value, which can contain signed parameters.
        raise HTTPError(
            "Document download redirect must remain on HTTPS data.uspto.gov"
        ) from None
    return urlunsplit(("https", "data.uspto.gov", target.path, target.query, ""))

def _api_key() -> str:
    key = os.getenv("ODP_API_KEY") or ""
    if not key:
        raise RuntimeError("ODP_API_KEY not set")
    return key

def _headers() -> Dict[str, str]:
    key = _api_key()
    return {
        "X-API-KEY": key,
        "USPTO-API-KEY": key,
        "Accept": "application/json",
    }

class HTTPError(Exception):
    pass

class PFWClient:
    """
    Lightweight client for USPTO Patent File Wrapper API.
    Only endpoints used by the GUI are implemented.
    """
    def __init__(self, base_url: str = BASE_URL, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    # ---- search ----
    def search_applications(self, payload: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        POST /api/v1/patent/applications/search with JSON payload when provided.
        If params is provided, does GET with query parameters.
        If both None, POST {}.
        """
        path = "/api/v1/patent/applications/search"
        url = f"{self.base_url}{path}"
        try:
            if params is not None:
                r = requests.get(url, headers=_headers(), params=params, timeout=self.timeout)
            else:
                r = requests.post(url, headers=_headers(), json=(payload or {}), timeout=self.timeout)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise HTTPError(f"{e} :: {getattr(e.response,'text', '')[:200]}")
        ct = r.headers.get("Content-Type","")
        if "json" not in ct.lower():
            raise HTTPError(f"Non-JSON response: {ct} :: {r.text[:200]}")
        return r.json()

    # ---- sections for a given application ----
    def _get(self, path: str) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        r = requests.get(url, headers=_headers(), timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def meta_data(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/meta-data")

    def adjustment(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/adjustment")

    def assignment(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/assignment")

    def attorney(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/attorney")

    def continuity(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/continuity")

    def foreign_priority(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/foreign-priority")

    def transactions(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/transactions")

    def associated_documents(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/associated-documents")

    def documents(self, application_number_text: str) -> Dict[str, Any]:
        return self._get(f"/api/v1/patent/applications/{application_number_text}/documents")

    # ---- document bytes ----
    def download_document(self, document_identifier: str) -> Tuple[bytes, str]:
        """
        Try the retained PFW content endpoint with one document identifier.
        Follow at most three HTTPS redirects within data.uspto.gov.
        Returns: (bytes, suggested_extension)
        """
        url = _document_url(document_identifier)
        for redirects in range(_MAX_DOCUMENT_REDIRECTS + 1):
            # Validate each hop before sending it. Automatic redirects would
            # bypass the origin restriction when a remote response changes host.
            r = requests.get(url, timeout=self.timeout, allow_redirects=False)
            if r.status_code not in _DOCUMENT_REDIRECTS:
                break
            location = r.headers.get("Location")
            r.close()
            if redirects == _MAX_DOCUMENT_REDIRECTS:
                raise HTTPError("Document download exceeded three redirects")
            url = _document_redirect(url, location)

        try:
            if r.status_code == 200:
                ct = r.headers.get("Content-Type","").lower()
                if "pdf" in ct:
                    return r.content, ".pdf"
                if "json" in ct:
                    return r.content, ".json"
                if "xml" in ct:
                    return r.content, ".xml"
                return r.content, ""

            raise HTTPError(f"Could not download document {document_identifier}: {r.status_code}")
        finally:
            r.close()
