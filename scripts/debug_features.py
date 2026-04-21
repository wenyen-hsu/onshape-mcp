"""Dump the raw features response from Onshape to see its real JSON shape.

Fill in DID / WID / EID with a Part Studio in one of your own documents
(use `onshape_parse_url` on an Onshape URL, or run the MCP tool
`onshape_list_elements`) and run:

    uv run python scripts/debug_features.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from onshape_mcp.client import OnshapeClient  # noqa: E402

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

client = OnshapeClient(
    os.environ["ONSHAPE_ACCESS_KEY"],
    os.environ["ONSHAPE_SECRET_KEY"],
    os.environ.get("ONSHAPE_BASE_URL", "https://cad.onshape.com"),
)

DID = "<your_document_id>"
WID = "<your_workspace_id>"
EID = "<your_part_studio_element_id>"

if "<" in DID:
    sys.exit("Edit DID / WID / EID in this file before running.")

data = client.get(f"/api/v10/partstudios/d/{DID}/w/{WID}/e/{EID}/features")

print("top-level keys:", list(data.keys()))
features = data.get("features") or []
print("features count:", len(features))
if features:
    first = features[0]
    print("\n--- first feature top-level keys ---")
    print(list(first.keys()))
    print("\n--- first feature full JSON ---")
    print(json.dumps(first, indent=2)[:3000])
