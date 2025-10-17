
import os
import time
import json
from typing import Any, Dict, List, Optional, Tuple
import requests

BASE_URL = "https://api.uspto.gov"

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
        Tries the documented PFW content endpoint under data.uspto.gov.
        Falls back to any downloadUrl if present in meta.
        Returns: (bytes, suggested_extension)
        """
        # Known content endpoint pattern:
        url = f"https://data.uspto.gov/patent-file-wrapper/documents/{document_identifier}"
        r = requests.get(url, timeout=self.timeout)
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
