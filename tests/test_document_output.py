"""Offline remote-identifier output boundaries, using synthetic bytes only."""

import os
from pathlib import Path
import tempfile
import unittest

from scripts.download_pfw import save_document


class DocumentOutputTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pro-patent-download-")
        self.root = Path(self.temporary.name).resolve()
        # Cleanup is limited to the independently created test directory.
        self.assertEqual(self.root.parent, Path(tempfile.gettempdir()).resolve())
        self.assertTrue(self.root.name.startswith("pro-patent-download-"))
        self.addCleanup(self.temporary.cleanup)
        self.app = self.root / "application"
        self.app.mkdir()

    def test_safe_filename_preserves_identifier(self):
        for identifier in ("LDXBTPQ7XBLUEX3", "DOC1", "doc-uuid-1", "OFFICE_ACTION_NON_FINAL", "doc.v1"):
            with self.subTest(identifier=identifier):
                path = save_document(self.app, identifier, ".pdf", b"offline PDF")
                self.assertEqual(path, self.app / (identifier + ".pdf"))
                self.assertEqual(path.read_bytes(), b"offline PDF")

    def test_invalid_identifier_cannot_create_outside_file(self):
        for identifier in ("../outside", "a/b", "a\\b", ".", "..", "a?query", "a#fragment", "a%2foutside"):
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    save_document(self.app, identifier, ".pdf", b"offline")
                self.assertEqual(list(self.app.iterdir()), [])
                self.assertFalse((self.root / "outside.pdf").exists())

    def test_extension_is_selected_not_a_path(self):
        for extension in ("/outside", ".pdf/../../outside", ".exe", None):
            with self.subTest(extension=extension):
                with self.assertRaises(ValueError):
                    save_document(self.app, "DOC1", extension, b"offline")
                self.assertEqual(list(self.app.iterdir()), [])

    def test_windows_device_names_are_refused(self):
        for identifier in ("CON", "con", "CON.extra", "PRN", "AUX", "NUL", "COM1", "COM9", "LPT1", "LPT9"):
            with self.subTest(identifier=identifier):
                with self.assertRaises(ValueError):
                    save_document(self.app, identifier, ".pdf", b"offline")
                self.assertEqual(list(self.app.iterdir()), [])

    def test_empty_extension_cannot_leave_windows_trailing_dot(self):
        with self.assertRaises(ValueError):
            save_document(self.app, "DOC1.", "", b"offline")
        self.assertEqual(list(self.app.iterdir()), [])

    def test_existing_file_is_preserved(self):
        path = self.app / "DOC1.pdf"
        path.write_bytes(b"existing evidence")
        with self.assertRaises(FileExistsError):
            save_document(self.app, "DOC1", ".pdf", b"replacement")
        self.assertEqual(path.read_bytes(), b"existing evidence")

    def test_existing_directory_is_preserved(self):
        path = self.app / "DOC1.pdf"
        path.mkdir()
        with self.assertRaises(OSError):
            save_document(self.app, "DOC1", ".pdf", b"replacement")
        self.assertTrue(path.is_dir())

    def test_existing_symlink_target_is_preserved(self):
        outside = self.root / "outside.pdf"
        outside.write_bytes(b"outside evidence")
        link = self.app / "DOC1.pdf"
        try:
            link.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"Local symlink creation unavailable: {exc}")
        with self.assertRaises(ValueError):
            save_document(self.app, "DOC1", ".pdf", b"replacement")
        self.assertEqual(outside.read_bytes(), b"outside evidence")
        self.assertTrue(link.is_symlink())

    def test_existing_hardlink_target_is_preserved(self):
        outside = self.root / "outside.pdf"
        outside.write_bytes(b"outside evidence")
        link = self.app / "DOC1.pdf"
        os.link(outside, link)
        with self.assertRaises(FileExistsError):
            save_document(self.app, "DOC1", ".pdf", b"replacement")
        self.assertEqual(outside.read_bytes(), b"outside evidence")


if __name__ == "__main__":
    unittest.main()
