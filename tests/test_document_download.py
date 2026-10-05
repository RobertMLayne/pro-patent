"""Offline request-boundary regressions for the retained PFW downloader."""

import traceback
import unittest
from unittest.mock import call, patch

from pfw_client.client import HTTPError, PFWClient


class Response:
    def __init__(self, status=200, content_type="application/pdf", location=None):
        """Provide a response fixture that records explicit closure."""
        self.status_code = status
        self.headers = {"Content-Type": content_type}
        if location is not None:
            self.headers["Location"] = location
        self.content = b"offline document fixture"
        self.close_count = 0

    def close(self):
        self.close_count += 1


class DocumentDownloadTests(unittest.TestCase):
    def setUp(self):
        # Any unmocked request or API-key lookup must fail instead of reaching a
        # production service or inspecting the user's credential environment.
        self.network = patch("requests.sessions.Session.request", side_effect=AssertionError("Network forbidden"))
        self.key = patch("pfw_client.client._api_key", side_effect=AssertionError("Credential access forbidden"))
        self.get = patch("pfw_client.client.requests.get")
        self.network.start()
        self.key.start()
        self.mock_get = self.get.start()
        self.addCleanup(self.network.stop)
        self.addCleanup(self.key.stop)
        self.addCleanup(self.get.stop)
        self.client = PFWClient(timeout=7)

    def test_safe_opaque_identifier_forms(self):
        # LDXBTPQ7XBLUEX3 is a retained pyUSPTO PFW fixture; the other cases
        # exercise token compatibility, not a claim about live USPTO validation.
        for identifier in ("LDXBTPQ7XBLUEX3", "100012345", "DOC1", "doc-uuid-1",
                           "OFFICE_ACTION_NON_FINAL", "doc.v1", "123e4567-e89b-12d3-a456-426614174000"):
            with self.subTest(identifier=identifier):
                self.mock_get.reset_mock()
                response = Response()
                self.mock_get.return_value = response
                self.assertEqual(self.client.download_document(identifier), (response.content, ".pdf"))
                self.mock_get.assert_called_once_with(
                    "https://data.uspto.gov/patent-file-wrapper/documents/" + identifier,
                    timeout=7, allow_redirects=False,
                )
                self.assertEqual(response.close_count, 1)

    def test_invalid_identifiers_never_send(self):
        for identifier in ("", None, 123, True, {}, ".", "..", "../private", "a/../b", "a\\b",
                           "a?query=1", "a#fragment", "a%2Fprivate", "a%252Fprivate", "https://elsewhere.invalid",
                           "//elsewhere.invalid", " a", "a ", "a\n", "a\x00", "a／b", "café"):
            with self.subTest(identifier=identifier):
                self.mock_get.reset_mock()
                with self.assertRaises(ValueError):
                    self.client.download_document(identifier)
                self.mock_get.assert_not_called()

    def test_relative_https_redirect_and_bytes(self):
        first = Response(status=302, location="/content/DOC1?download=1")
        final = Response(content_type="application/xml")
        self.mock_get.side_effect = [first, final]
        self.assertEqual(self.client.download_document("DOC1"), (final.content, ".xml"))
        self.assertEqual(self.mock_get.call_args_list, [
            call("https://data.uspto.gov/patent-file-wrapper/documents/DOC1", timeout=7, allow_redirects=False),
            call("https://data.uspto.gov/content/DOC1?download=1", timeout=7, allow_redirects=False),
        ])
        self.assertEqual((first.close_count, final.close_count), (1, 1))

    def test_each_redirect_status_is_manual(self):
        for status in (301, 302, 303, 307, 308):
            with self.subTest(status=status):
                self.mock_get.reset_mock()
                first = Response(status=status, location="https://data.uspto.gov:443/content/DOC1")
                final = Response()
                self.mock_get.side_effect = [first, final]
                self.client.download_document("DOC1")
                self.assertEqual(self.mock_get.call_count, 2)
                self.assertEqual(self.mock_get.call_args.kwargs, {"timeout": 7, "allow_redirects": False})
                self.assertEqual(self.mock_get.call_args.args, ("https://data.uspto.gov/content/DOC1",))

    def test_unapproved_redirect_never_sends_second_request(self):
        for location in ("http://data.uspto.gov/content/DOC1", "https://elsewhere.invalid/DOC1",
                         "https://data.uspto.gov.elsewhere.invalid/DOC1", "https://data.uspto.gov:444/DOC1",
                         "https://user:password@data.uspto.gov/DOC1", "https://data.uspto.gov./DOC1",
                         "https://data.uspto.gov/DOC1#fragment", "file:///private", "//127.0.0.1/private",
                         "/content\\private", "\t/content/DOC1", "https://data.uspto.gov:invalid/DOC1",
                         "https://data-documents.uspto.gov/DOC1", "/content\x00DOC1"):
            with self.subTest(location=location):
                self.mock_get.reset_mock()
                response = Response(status=302, location=location)
                self.mock_get.side_effect = None
                self.mock_get.return_value = response
                with self.assertRaises(HTTPError):
                    self.client.download_document("DOC1")
                self.assertEqual(self.mock_get.call_count, 1)
                self.assertEqual(response.close_count, 1)

    def test_missing_redirect_location_closes_response(self):
        for location in (None, ""):
            with self.subTest(location=location):
                self.mock_get.return_value = Response(status=302, location=location)
                with self.assertRaises(HTTPError):
                    self.client.download_document("DOC1")
                self.assertEqual(self.mock_get.return_value.close_count, 1)

    def test_three_redirects_can_finish(self):
        responses = [Response(status=302, location="/content/DOC1") for _ in range(3)] + [Response()]
        self.mock_get.side_effect = responses
        self.assertEqual(self.client.download_document("DOC1"), (responses[-1].content, ".pdf"))
        self.assertEqual(self.mock_get.call_count, 4)
        self.assertTrue(all(r.close_count == 1 for r in responses))

    def test_fourth_redirect_is_refused(self):
        responses = [Response(status=302, location="/content/DOC1") for _ in range(4)]
        self.mock_get.side_effect = responses
        with self.assertRaisesRegex(HTTPError, "exceeded three redirects"):
            self.client.download_document("DOC1")
        self.assertEqual(self.mock_get.call_count, 4)
        self.assertTrue(all(r.close_count == 1 for r in responses))

    def test_content_extensions_are_preserved(self):
        for content_type, extension in (("application/pdf", ".pdf"), ("application/json", ".json"),
                                        ("application/xml", ".xml"), ("application/octet-stream", "")):
            with self.subTest(content_type=content_type):
                response = Response(content_type=content_type)
                self.mock_get.return_value = response
                self.assertEqual(self.client.download_document("DOC1"), (response.content, extension))
                self.assertEqual(response.close_count, 1)

    def test_non_success_closes_response(self):
        for status in (304, 400, 404, 500):
            with self.subTest(status=status):
                response = Response(status=status)
                self.mock_get.return_value = response
                with self.assertRaisesRegex(HTTPError, str(status)):
                    self.client.download_document("DOC1")
                self.assertEqual(response.close_count, 1)

    def test_api_base_override_does_not_change_document_origin(self):
        response = Response()
        self.mock_get.return_value = response
        client = PFWClient(base_url="https://elsewhere.invalid", timeout=7)
        client.download_document("DOC1")
        self.mock_get.assert_called_once_with(
            "https://data.uspto.gov/patent-file-wrapper/documents/DOC1", timeout=7, allow_redirects=False,
        )

    def test_signed_redirect_value_is_not_in_error(self):
        location = "https://elsewhere.invalid/content?signature=offline-secret"
        self.mock_get.return_value = Response(status=302, location=location)
        with self.assertRaises(HTTPError) as raised:
            self.client.download_document("DOC1")
        self.assertNotIn("offline-secret", str(raised.exception))

    def test_malformed_signed_redirect_value_is_not_in_traceback(self):
        location = "https://data.uspto.gov:offline-secret/content"
        self.mock_get.return_value = Response(status=302, location=location)
        try:
            self.client.download_document("DOC1")
        except HTTPError as exc:
            self.assertNotIn(
                "offline-secret",
                "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
            )
        else:
            self.fail("Malformed redirect should have been refused")

    def test_protocol_relative_approved_redirect(self):
        first = Response(status=302, location="//DATA.USPTO.GOV/content/DOC1")
        final = Response()
        self.mock_get.side_effect = [first, final]
        self.client.download_document("DOC1")
        self.assertEqual(self.mock_get.call_args.args, ("https://data.uspto.gov/content/DOC1",))


if __name__ == "__main__":
    unittest.main()
