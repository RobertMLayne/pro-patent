"""Offline batch application paths, using only disposable fixtures and fake clients."""

import contextlib
import io
import json
import os
import stat
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from scripts import download_pfw


class ApplicationInputTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pro-application-input-")
        self.outer = Path(self.temporary.name).resolve()
        self.assertEqual(self.outer.parent, Path(tempfile.gettempdir()).resolve())
        self.assertTrue(self.outer.name.startswith("pro-application-input-"))
        self.addCleanup(self.temporary.cleanup)
        self.ids = self.outer / "ids.txt"
        self.output = self.outer / "output"
        for target in (
            "requests.sessions.Session.request",
            "pfw_client.client._api_key",
            "socket.create_connection",
            "socket.getaddrinfo",
        ):
            patch = mock.patch(
                target, side_effect=AssertionError("Transport/key lookup forbidden")
            )
            patch.start()
            self.addCleanup(patch.stop)

    def run_main(self, client, sections="meta"):
        argv = [
            "download_pfw",
            "--ids",
            str(self.ids),
            "--outdir",
            str(self.output),
            "--sections",
            sections,
        ]
        with (
            mock.patch("sys.argv", argv),
            mock.patch.object(
                download_pfw, "PFWClient", return_value=client
            ) as constructor,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            self.constructor = constructor
            download_pfw.main()
        return constructor

    def fake_client(self):
        return SimpleNamespace(
            **{
                name: mock.Mock(return_value={})
                for name in (
                    "meta_data",
                    "adjustment",
                    "assignment",
                    "attorney",
                    "continuity",
                    "foreign_priority",
                    "transactions",
                    "documents",
                    "associated_documents",
                )
            }
        )

    def test_safe_tokens_keep_text_and_leading_zeroes(self):
        for value in (
            "9232158",
            "10292138",
            "00001234",
            "US20240001234A1",
            "D123456",
            "app-1_v2.3",
        ):
            with self.subTest(value=value):
                self.assertEqual(download_pfw.validate_application_number(value), value)

    def test_unsafe_components_are_refused(self):
        for value in (
            "../escaped",
            "a/b",
            "a\\b",
            "/absolute",
            "C:relative",
            "C:\\absolute",
            "\\\\server\\share",
            ".",
            "..",
            "CON",
            "con.txt",
            "COM1",
            "LPT9",
            "123.",
            "123 ",
            " 123",
            "12\t3",
            "12\x003",
            "12\x1f3",
            "12?3",
            "12#3",
            "12%2f3",
            "１２３",
            "",
            None,
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                download_pfw.validate_application_number(value)

    def test_line_endings_and_blank_lines_preserve_valid_entries(self):
        self.ids.write_bytes(b"9232158\r\n\r\n00001234\n\n")
        self.assertEqual(download_pfw.load_ids(str(self.ids)), ["9232158", "00001234"])

    def test_invalid_later_entry_refuses_whole_batch_before_output_or_client(self):
        for value in (
            "../escaped",
            "a/b",
            "C:relative",
            "CON",
            "123 ",
            "12\t3",
            "\x1f",
            " ",
        ):
            with self.subTest(value=value):
                self.ids.write_text("12345678\n" + value + "\n", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "line 2"):
                    self.run_main(self.fake_client())
                self.constructor.assert_not_called()
                self.assertFalse(self.output.exists())
                self.assertFalse((self.outer / "escaped").exists())

    def test_valid_batch_uses_same_api_tokens_and_contained_directories(self):
        self.ids.write_text("9232158\n00001234\n", encoding="utf-8")
        client = self.fake_client()
        self.run_main(client)
        self.assertEqual(
            client.meta_data.call_args_list,
            [mock.call("9232158"), mock.call("00001234")],
        )
        for value in ("9232158", "00001234"):
            path = self.output / value / "meta.json"
            self.assertEqual(path.parent.parent, self.output)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {})

    def test_existing_ordinary_section_file_is_overwritten_on_rerun(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        app = self.output / "9232158"
        app.mkdir(parents=True)
        (app / "meta.json").write_text('{"old": true}', encoding="utf-8")
        client = self.fake_client()
        client.meta_data.return_value = {"current": True}
        self.run_main(client)
        self.assertEqual(json.loads((app / "meta.json").read_text()), {"current": True})

    def test_existing_application_symlink_is_refused_before_client(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        self.output.mkdir()
        outside = self.outer / "outside"
        outside.mkdir()
        try:
            (self.output / "9232158").symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Directory symlink unavailable: {exc}")
        with self.assertRaises(ValueError):
            self.run_main(self.fake_client())
        self.constructor.assert_not_called()
        self.assertEqual(list(outside.iterdir()), [])

    def test_existing_section_symlink_is_refused_before_client(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        app = self.output / "9232158"
        app.mkdir(parents=True)
        outside = self.outer / "outside.json"
        outside.write_bytes(b"preserve")
        try:
            (app / "meta.json").symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"File symlink unavailable: {exc}")
        with self.assertRaises(ValueError):
            self.run_main(self.fake_client())
        self.constructor.assert_not_called()
        self.assertEqual(outside.read_bytes(), b"preserve")

    def test_existing_section_hardlink_is_refused_before_client(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        app = self.output / "9232158"
        app.mkdir(parents=True)
        outside = self.outer / "outside.json"
        outside.write_bytes(b"preserve")
        os.link(outside, app / "meta.json")
        with self.assertRaises(ValueError):
            self.run_main(self.fake_client())
        self.constructor.assert_not_called()
        self.assertEqual(outside.read_bytes(), b"preserve")

    def test_retained_document_json_alias_is_refused_even_when_not_selected(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        app = self.output / "9232158"
        app.mkdir(parents=True)
        outside = self.outer / "documents.json"
        outside.write_text('{"documents": []}', encoding="utf-8")
        os.link(outside, app / "documents.json")
        with self.assertRaises(ValueError):
            self.run_main(self.fake_client(), sections="meta")
        self.constructor.assert_not_called()
        self.assertFalse((app / "meta.json").exists())

    def test_section_link_created_by_response_is_refused_before_write(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        outside = self.outer / "outside.json"
        outside.write_bytes(b"preserve")
        client = self.fake_client()

        def response(_application_number):
            os.link(outside, self.output / "9232158" / "meta.json")
            return {"current": True}

        client.meta_data.side_effect = response
        self.run_main(client)
        client.meta_data.assert_called_once_with("9232158")
        self.assertEqual(outside.read_bytes(), b"preserve")

    def test_windows_reparse_directory_is_a_link(self):
        flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", None)
        if flag is None:
            self.skipTest("Windows reparse attributes unavailable")
        info = SimpleNamespace(st_mode=stat.S_IFDIR, st_file_attributes=flag)
        self.assertTrue(download_pfw._is_link(info))

    def test_section_path_refuses_unknown_section(self):
        with self.assertRaises(ValueError):
            download_pfw._section_path(self.output, "../escaped")

    def test_existing_application_file_is_refused_without_overwrite(self):
        self.ids.write_text("9232158\n", encoding="utf-8")
        self.output.mkdir()
        child = self.output / "9232158"
        child.write_bytes(b"preserve")
        with self.assertRaises(ValueError):
            self.run_main(self.fake_client())
        self.constructor.assert_not_called()
        self.assertEqual(child.read_bytes(), b"preserve")


if __name__ == "__main__":
    unittest.main()
