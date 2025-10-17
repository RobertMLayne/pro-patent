import os, argparse, requests

def load_patents(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def fetch_wrapper_metadata(patent_number: str):
    url = f"https://data.uspto.gov/patent-file-wrapper/search?patentNumber={patent_number}"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()

def fetch_and_save_documents(patent_number: str, outdir: str):
    data = fetch_wrapper_metadata(patent_number)
    entries = data.get("results", [])
    pdir = os.path.join(outdir, patent_number)
    os.makedirs(pdir, exist_ok=True)
    count = 0
    for entry in entries:
        for doc in entry.get("documents", []):
            doc_id = doc.get("documentIdentifier") or doc.get("documentId")
            if not doc_id:
                continue
            doc_url = f"https://data.uspto.gov/patent-file-wrapper/documents/{doc_id}"
            r = requests.get(doc_url, timeout=60)
            if r.status_code != 200:
                continue
            ext = ".pdf"
            ct = r.headers.get("Content-Type","").lower()
            if "json" in ct: ext = ".json"
            elif "xml" in ct: ext = ".xml"
            with open(os.path.join(pdir, f"{doc_id}{ext}"), "wb") as f:
                f.write(r.content)
            count += 1
            print(f"[{patent_number}] saved {doc_id}{ext}")
    if count == 0:
        print(f"[{patent_number}] no documents saved.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--patents", default="patents.txt")
    args = ap.parse_args()
    for p in load_patents(args.patents):
        print(f"== {p}")
        try: fetch_and_save_documents(p, args.outdir)
        except Exception as e: print(f"[{p}] ERROR: {e}")

if __name__ == "__main__":
    main()
