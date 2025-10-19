
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Dict, Any, List, Optional
from pfw_client import PFWClient

SCHEMA_FILE = os.path.join("data","patent-data-schema.json")

def load_schema_fields() -> List[str]:
    # Accept either {"fields":[...]} or a flat list
    try:
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "fields" in data and isinstance(data["fields"], list):
            return list(sorted(set(str(x) for x in data["fields"])))
        if isinstance(data, list):
            return list(sorted(set(str(x) for x in data)))
    except Exception:
        pass
    # minimal defaults
    return [
        "applicationMetaData.applicationNumberText",
        "applicationMetaData.filingDate",
        "applicationMetaData.title",
    ]

class RowList:
    def __init__(self, parent, columns: List[str], field_choices: List[str] = None):
        self.frame = ttk.Frame(parent)
        self.rows: List[List[tk.Widget]] = []
        self.columns = columns
        self.field_choices = field_choices or []
        self.add_button = ttk.Button(self.frame, text="+ add", command=self.add_row)
        self.add_button.pack(anchor="w", pady=(0,4))
        self.rows_frame = ttk.Frame(self.frame)
        self.rows_frame.pack(fill="both", expand=True)

    def grid(self, **kw):
        self.frame.grid(**kw)

    def add_row(self, preset: Dict[str, str] = None):
        row = []
        row_frame = ttk.Frame(self.rows_frame)
        row_frame.pack(fill="x", pady=2)

        for col in self.columns:
            if col == "field" and self.field_choices:
                cb = ttk.Combobox(row_frame, values=self.field_choices, width=60)
                cb.set(preset.get(col,"") if preset else "")
                cb.pack(side="left", padx=2)
                row.append(cb)
            else:
                e = ttk.Entry(row_frame, width=25)
                e.insert(0, preset.get(col,"") if preset else "")
                e.pack(side="left", padx=2)
                row.append(e)

        rm = ttk.Button(row_frame, text="x", width=2, command=lambda rf=row_frame: self._remove(rf))
        rm.pack(side="left", padx=2)
        row.append(rm)
        self.rows.append(row)

    def _remove(self, rf):
        for i, row in enumerate(self.rows):
            if row[-1].master == rf:
                for w in row:
                    try:
                        w.destroy()
                    except Exception:
                        pass
                self.rows.pop(i)
                break

    def values(self) -> List[Dict[str,str]]:
        out = []
        for row in self.rows:
            vals = {}
            for name, widget in zip(self.columns, row[:-1]):
                vals[name] = widget.get().strip()
            if any(vals.values()):
                out.append(vals)
        return out

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USPTO PFW Search")
        self.geometry("1100x800")

        self.fields_list = load_schema_fields()
        self._build()

    def _build(self):
        top = ttk.Frame(self); top.pack(fill="x", padx=8, pady=6)
        ttk.Label(top, text="Base URL").pack(side="left")
        self.base_url = ttk.Entry(top, width=40)
        self.base_url.insert(0, "https://api.uspto.gov")
        self.base_url.pack(side="left", padx=6)
        ttk.Label(top, text="API Key (ODP_API_KEY used if blank)").pack(side="left", padx=(10,2))
        self.api_key = ttk.Entry(top, width=50, show="*")
        self.api_key.pack(side="left", padx=6)

        # Tabs
        nb = ttk.Notebook(self); nb.pack(fill="both", expand=True, padx=8, pady=8)

        # Filters
        filters_tab = ttk.Frame(nb); nb.add(filters_tab, text="Filters")
        self.filters = RowList(filters_tab, ["name","value","field"], field_choices=self.fields_list)
        self.filters.grid(row=0, column=0, sticky="nsew")

        # Range Filters
        rf_tab = ttk.Frame(nb); nb.add(rf_tab, text="Range Filters")
        self.range_filters = RowList(rf_tab, ["field","valueFrom","valueTo"], field_choices=self.fields_list)
        self.range_filters.grid(row=0, column=0, sticky="nsew")

        # Sort
        sort_tab = ttk.Frame(nb); nb.add(sort_tab, text="Sort")
        self.sort_rows = RowList(sort_tab, ["field","order"], field_choices=self.fields_list)
        self.sort_rows.grid(row=0, column=0, sticky="nsew")

        # Fields selection
        fields_tab = ttk.Frame(nb); nb.add(fields_tab, text="Fields")
        left = ttk.Frame(fields_tab); left.pack(side="left", fill="both", expand=True)
        right = ttk.Frame(fields_tab); right.pack(side="left", fill="y")
        ttk.Label(left, text="Select fields to include:").pack(anchor="w")
        self.fields_listbox = tk.Listbox(left, selectmode="extended")
        for f in self.fields_list:
            self.fields_listbox.insert("end", f)
        self.fields_listbox.pack(fill="both", expand=True, padx=4, pady=4)
        ttk.Label(right, text="Pagination").pack(anchor="w", pady=(12,4))
        ttk.Label(right, text="offset").pack(anchor="w")
        self.offset = ttk.Entry(right, width=10); self.offset.insert(0, "0"); self.offset.pack(anchor="w")
        ttk.Label(right, text="limit").pack(anchor="w")
        self.limit = ttk.Entry(right, width=10); self.limit.insert(0, "25"); self.limit.pack(anchor="w")
        ttk.Label(right, text="Facets (comma-separated)").pack(anchor="w", pady=(10,0))
        self.facets = ttk.Entry(right, width=35); self.facets.pack(anchor="w")

        # Bottom buttons and output
        bottom = ttk.Frame(self); bottom.pack(fill="x", padx=8, pady=8)
        ttk.Button(bottom, text="Search (POST)", command=self.do_search_post).pack(side="left")
        ttk.Button(bottom, text="Search (GET)", command=self.do_search_get).pack(side="left", padx=6)
        ttk.Button(bottom, text="Save Payload", command=self.save_payload).pack(side="left", padx=6)

        self.payload_text = tk.Text(self, height=14)
        self.payload_text.pack(fill="both", expand=False, padx=8, pady=(0,4))

        self.results_text = tk.Text(self, height=18)
        self.results_text.pack(fill="both", expand=True, padx=8, pady=(0,8))

    def build_payload(self) -> Dict[str, Any]:
        payload: Dict[str, Any] = {}
        fvals = self.filters.values()
        if fvals:
            payload["filters"] = [{"name": r.get("name",""), "value": r.get("value","")} for r in fvals if r.get("name") and r.get("value")]
        rfvals = self.range_filters.values()
        if rfvals:
            payload["rangefilters"] = [{"field": r.get("field",""), "valueFrom": r.get("valueFrom",""), "valueTo": r.get("valueTo","")} for r in rfvals if r.get("field")]
        svals = self.sort_rows.values()
        if svals:
            payload["sort"] = [{"field": r.get("field",""), "order": r.get("order","")} for r in svals if r.get("field")]
        selected_indices = self.fields_listbox.curselection()
        if selected_indices:
            payload["fields"] = [self.fields_list[i] for i in selected_indices]
        # pagination
        try:
            off = int(self.offset.get().strip() or "0")
        except ValueError:
            off = 0
        try:
            lim = int(self.limit.get().strip() or "25")
        except ValueError:
            lim = 25
        payload["pagination"] = {"offset": off, "limit": lim}
        # facets
        if self.facets.get().strip():
            payload["facets"] = [x.strip() for x in self.facets.get().split(",") if x.strip()]
        return payload

    def _client(self) -> PFWClient:
        if self.api_key.get().strip():
            os.environ["ODP_API_KEY"] = self.api_key.get().strip()
        return PFWClient(base_url=self.base_url.get().strip() or "https://api.uspto.gov")

    def do_search_post(self):
        payload = self.build_payload()
        self.payload_text.delete("1.0","end")
        self.payload_text.insert("1.0", json.dumps(payload, indent=2))
        try:
            data = self._client().search_applications(payload=payload)
            self.results_text.delete("1.0","end")
            self.results_text.insert("1.0", json.dumps(data, indent=2))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_search_get(self):
        payload = self.build_payload()
        self.payload_text.delete("1.0","end")
        self.payload_text.insert("1.0", json.dumps(payload, indent=2))
        # Convert to query params where feasible: we only support fields for demo
        params: Dict[str, Any] = {}
        # Flatten filters into q-like simple syntax "name:value"
        if "filters" in payload:
            qparts = [f"{f['name']}:{f['value']}" for f in payload["filters"]]
            if qparts:
                params["q"] = " AND ".join(qparts)
        if "pagination" in payload:
            params["offset"] = payload["pagination"].get("offset",0)
            params["limit"]  = payload["pagination"].get("limit",25)
        try:
            data = self._client().search_applications(params=params)
            self.results_text.delete("1.0","end")
            self.results_text.insert("1.0", json.dumps(data, indent=2))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_payload(self):
        payload = self.build_payload()
        fp = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON","*.json")])
        if not fp:
            return
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        messagebox.showinfo("Saved", fp)

if __name__ == "__main__":
    App().mainloop()
