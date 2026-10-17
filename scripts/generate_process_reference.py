"""Generate reference/processes.qmd from the live FAO OpenEO /processes endpoint.

Usage: python scripts/generate_process_reference.py
"""

import json
import pathlib
import urllib.request

BACKEND = "https://data.fao.org/openeo"
OUTPUT = pathlib.Path(__file__).resolve().parent.parent / "reference" / "processes.qmd"

# Internal processes that are not documented for public use.
HIDDEN = {"reclassification", "calculate_msa"}

# Processes that are not part of the official openEO process catalogue.
FAO_PROCESSES = {
    "zonal_stats": "FAO zonal statistics with feature properties carried through.",
    "crtb_analysis": "Climate Risk Toolbox hazard, vulnerability, exposure and adaptive capacity.",
    "load_geojson_url": "Load polygons from a GeoJSON URL.",
    "load_fiona_feature_collection": "Load boundaries from the FAO geospatial catalogue.",
    "pixel_count": "Count occurrences of each pixel value.",
    "maze_varieties": "PLAN-T: maize varieties suitable for a location.",
    "planting_recommendation": "PLAN-T: whether a planting date is suitable.",
    "cs_assessment": "PLAN-T: climate stressors for a planting date.",
    "sign": "Alias of `sgn`.",
}

# Standard processes whose FAO behaviour is documented on fao_processes.qmd.
FAO_NOTES = {
    "aggregate_spatial": "aggregate_spatial-extension",
    "climatological_normal": "climatological_normal",
    "load_url": "load_url",
    "export_workspace": "export_workspace",
}

# Category order and display names; anything else goes under "Other".
CATEGORY_ORDER = [
    ("import", "Loading data"),
    ("export", "Saving and exporting"),
    ("filter", "Filtering"),
    ("cubes", "Data cube operations"),
    ("aggregate", "Aggregation"),
    ("climatology", "Climatology"),
    ("reducer", "Reducers and statistics"),
    ("comparison", "Comparison"),
    ("logic", "Logic"),
    ("math", "Math"),
    ("arrays", "Arrays"),
]


def esc(text):
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def schema_type(schema):
    schemas = schema if isinstance(schema, list) else schema.get("anyOf", [schema]) if isinstance(schema, dict) else []
    types = []
    for s in schemas:
        if not isinstance(s, dict):
            continue
        t = s.get("subtype") or s.get("type") or s.get("title")
        if "enum" in s:
            t = " / ".join(f"`{v}`" for v in s["enum"])
        if t and t not in types and t != "null":
            types.append(str(t))
    return ", ".join(types) or "any"


def param_table(process):
    rows = ["| Parameter | Type | Required | Default | Description |", "|---|---|---|---|---|"]
    for p in process.get("parameters", []):
        default = p.get("default", "")
        default = f"`{json.dumps(default)}`" if "default" in p and default not in ("", None) else ""
        rows.append(
            f"| `{p['name']}` | {esc(schema_type(p.get('schema', {})))} | "
            f"{'no' if p.get('optional') else 'yes'} | {esc(default)} | {esc(p.get('description'))} |"
        )
    return "\n".join(rows)


def category_of(process):
    cats = process.get("categories", [])
    for key, _ in CATEGORY_ORDER:
        if any(key in c for c in cats):
            return key
    return "other"


def main():
    with urllib.request.urlopen(f"{BACKEND}/processes", timeout=60) as resp:
        processes = [p for p in json.load(resp)["processes"] if p["id"] not in HIDDEN]
    by_id = {p["id"]: p for p in processes}

    out = [
        "---",
        'title: "Process Reference"',
        "---",
        "",
        f"This page lists the {len(processes)} processes available on "
        f"[`{BACKEND}`]({BACKEND}/processes). It is generated from the live `/processes` endpoint "
        "with `scripts/generate_process_reference.py`.",
        "",
        "Standard openEO processes behave as described in the "
        "[openEO process documentation](https://processes.openeo.org/); follow the links for full details. "
        "FAO-specific processes are described below. Standard processes with FAO notes link to [FAO Processes](fao_processes.qmd).",
        "",
        "In Python, call any process with `cube.process(\"<id>\", ...)` or "
        "`connection.datacube_from_process(\"<id>\", ...)`. In the Web Editor, search for the process ID in the process list.",
        "",
        "## FAO-specific processes",
        "",
        "These processes aren't part of the standard openEO catalogue. See [FAO Processes](fao_processes.qmd) for usage notes and examples.",
        "",
    ]
    for pid in FAO_PROCESSES:
        if pid not in by_id:
            continue
        p = by_id[pid]
        out += [f"### `{pid}`", "", FAO_PROCESSES[pid], "", param_table(p), ""]

    out += ["## Standard openEO processes", ""]
    groups = {}
    for p in processes:
        if p["id"] in FAO_PROCESSES:
            continue
        groups.setdefault(category_of(p), []).append(p)
    for key, title in CATEGORY_ORDER + [("other", "Other")]:
        if key not in groups:
            continue
        out += [f"### {title}", "", "| Process | Summary |", "|---|---|"]
        for p in sorted(groups[key], key=lambda x: x["id"]):
            note = f" ([FAO notes](fao_processes.qmd#{FAO_NOTES[p['id']]}))" if p["id"] in FAO_NOTES else ""
            out.append(f"| [`{p['id']}`](https://processes.openeo.org/#{p['id']}) | {esc(p.get('summary'))}{note} |")
        out.append("")

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text("\n".join(out))
    print(f"Wrote {OUTPUT} ({len(processes)} processes)")


if __name__ == "__main__":
    main()
