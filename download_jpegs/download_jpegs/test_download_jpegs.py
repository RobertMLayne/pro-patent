# test_download_jpegs.py
import pathlib
from download_jpegs import download, DEST_DIR

def test_download(tmp_path, monkeypatch):
    monkeypatch.setattr("download_jpegs.DEST_DIR", tmp_path)
    fname = download("https://httpbin.org/image/jpeg")
    assert (tmp_path / pathlib.Path(fname)).is_file()
