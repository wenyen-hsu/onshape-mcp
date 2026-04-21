"""Onshape MCP server — exposes a small set of Onshape API tools."""

from __future__ import annotations

import functools
import os
import re
import time
from pathlib import Path
from typing import Annotated, Any

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from .client import OnshapeClient, OnshapeError

_ENV_FILE = Path(__file__).resolve().parents[2] / ".env"
if _ENV_FILE.exists():
    load_dotenv(_ENV_FILE)

ACCESS_KEY = os.environ.get("ONSHAPE_ACCESS_KEY")
SECRET_KEY = os.environ.get("ONSHAPE_SECRET_KEY")
BASE_URL = os.environ.get("ONSHAPE_BASE_URL", "https://cad.onshape.com")

if not ACCESS_KEY or not SECRET_KEY:
    raise RuntimeError(
        "ONSHAPE_ACCESS_KEY and ONSHAPE_SECRET_KEY must be set (via .env or env vars)."
    )

client = OnshapeClient(ACCESS_KEY, SECRET_KEY, BASE_URL)
mcp = FastMCP("onshape")


def _safe(fn):
    """Wrap a tool so Onshape errors return a readable dict rather than crashing MCP."""

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except OnshapeError as e:
            return {"error": str(e), "status": e.status, "body": e.body}

    return wrapper


@mcp.tool()
@_safe
def onshape_whoami() -> dict:
    """Return the authenticated Onshape user (useful to confirm credentials work)."""
    return client.get("/api/v10/users/sessioninfo")


@mcp.tool()
@_safe
def onshape_list_documents(
    limit: Annotated[int, "Max items to return, 1-100"] = 20,
    query: Annotated[str, "Filter by document name substring"] = "",
    owner_only: Annotated[bool, "Only include documents you own"] = False,
) -> dict:
    """List Onshape documents visible to the authenticated user."""
    params: dict[str, Any] = {"limit": max(1, min(limit, 100))}
    if query:
        params["q"] = query
    if owner_only:
        params["filter"] = 0  # 0 = my documents
    data = client.get("/api/v10/documents", params=params)
    items = [
        {
            "id": d["id"],
            "name": d["name"],
            "owner": (d.get("owner") or {}).get("name"),
            "modifiedAt": d.get("modifiedAt"),
            "defaultWorkspace": (d.get("defaultWorkspace") or {}).get("id"),
            "href": d.get("href"),
        }
        for d in data.get("items", [])
    ]
    return {"count": len(items), "documents": items}


@mcp.tool()
@_safe
def onshape_get_document(document_id: str) -> dict:
    """Get details for a single Onshape document."""
    return client.get(f"/api/v10/documents/{document_id}")


@mcp.tool()
@_safe
def onshape_list_elements(document_id: str, workspace_id: str) -> list[dict]:
    """List elements (Part Studios, Assemblies, Drawings) in a document workspace."""
    data = client.get(
        f"/api/v10/documents/d/{document_id}/w/{workspace_id}/elements"
    )
    return [
        {
            "id": e["id"],
            "name": e["name"],
            "elementType": e.get("elementType"),
            "dataType": e.get("dataType"),
        }
        for e in data
    ]


@mcp.tool()
@_safe
def onshape_get_parts(
    document_id: str, workspace_id: str, element_id: str
) -> list[dict]:
    """List parts inside a Part Studio."""
    data = client.get(
        f"/api/v10/parts/d/{document_id}/w/{workspace_id}/e/{element_id}"
    )
    return [
        {
            "partId": p["partId"],
            "name": p["name"],
            "bodyType": p.get("bodyType"),
            "material": (p.get("material") or {}).get("displayName"),
            "appearance": p.get("appearance"),
        }
        for p in data
    ]


@mcp.tool()
@_safe
def onshape_get_mass_properties(
    document_id: str,
    workspace_id: str,
    element_id: str,
    part_id: Annotated[str | None, "Optional partId; omit for whole Part Studio"] = None,
) -> dict:
    """Get mass / volume / centroid for a part (or the whole Part Studio)."""
    path = (
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}"
        "/massproperties"
    )
    params = {"partId": part_id} if part_id else None
    return client.get(path, params=params)


@mcp.tool()
def onshape_parse_url(url: str) -> dict:
    """Parse an Onshape document URL into document_id / workspace_id / element_id.

    Handles workspace (w), version (v) and microversion (m) URL forms.
    """
    m = re.search(
        r"/documents/(?P<did>[^/?#]+)"
        r"(?:/(?P<wtype>[wvm])/(?P<wid>[^/?#]+))?"
        r"(?:/e/(?P<eid>[^/?#]+))?",
        url,
    )
    if not m:
        return {"error": "Not a recognizable Onshape URL"}
    type_map = {"w": "workspace", "v": "version", "m": "microversion"}
    return {
        "document_id": m.group("did"),
        "workspace_type": type_map.get(m.group("wtype") or ""),
        "workspace_id": m.group("wid"),
        "element_id": m.group("eid"),
    }


@mcp.tool()
@_safe
def onshape_export_part_studio(
    document_id: str,
    workspace_id: str,
    element_id: str,
    format_name: Annotated[
        str, "Export format: STEP, STL, PARASOLID, IGES, SOLIDWORKS, ACIS"
    ] = "STEP",
    part_ids: Annotated[
        str | None, "Comma-separated partIds; omit to export all parts"
    ] = None,
    output_path: Annotated[
        str | None, "Where to save the file (default: ./<element_id>.<ext>)"
    ] = None,
    poll_timeout_seconds: int = 120,
) -> dict:
    """Export a Part Studio (or selected parts) to a file.

    Creates an async translation, polls until done, then downloads the result.
    """
    fmt = format_name.upper()
    payload: dict[str, Any] = {"formatName": fmt, "storeInDocument": False}
    if part_ids:
        payload["partIds"] = part_ids

    job = client.post(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}"
        "/translations",
        json=payload,
    )
    translation_id = job["id"]

    deadline = time.time() + poll_timeout_seconds
    status: dict = {}
    while time.time() < deadline:
        status = client.get(f"/api/v10/translations/{translation_id}")
        state = status.get("requestState")
        if state == "DONE":
            break
        if state == "FAILED":
            return {
                "error": "translation failed",
                "reason": status.get("failureReason"),
                "status": status,
            }
        time.sleep(2)
    else:
        return {"error": "translation timed out", "translation_id": translation_id}

    external_ids = status.get("resultExternalDataIds") or []
    if not external_ids:
        return {"error": "no resultExternalDataIds in translation result", "status": status}
    foreign_id = external_ids[0]

    r = client.request(
        "GET",
        f"/api/v10/documents/d/{document_id}/externaldata/{foreign_id}",
        accept="application/octet-stream",
    )

    if output_path is None:
        output_path = f"./{element_id}.{fmt.lower()}"
    out = Path(output_path).expanduser().resolve()
    out.write_bytes(r.content)
    return {"saved_to": str(out), "bytes": len(r.content), "format": fmt}


@mcp.tool()
@_safe
def onshape_create_feature_studio(
    document_id: str,
    workspace_id: str,
    name: Annotated[str, "Display name for the new Feature Studio"] = "Custom Features",
) -> dict:
    """Create a new empty Feature Studio element in a workspace.

    Returns the new element's id; use it as `feature_studio_id` in later calls.
    """
    data = client.post(
        f"/api/v10/featurestudios/d/{document_id}/w/{workspace_id}",
        json={"name": name},
    )
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "elementType": data.get("elementType"),
        "raw": data,
    }


@mcp.tool()
@_safe
def onshape_get_feature_studio_code(
    document_id: str, workspace_id: str, element_id: str
) -> dict:
    """Read the FeatureScript source of a Feature Studio."""
    data = client.get(
        f"/api/v10/featurestudios/d/{document_id}/w/{workspace_id}/e/{element_id}"
    )
    return {
        "contents": data.get("contents"),
        "microversionId": data.get("microversionId"),
        "isModifiable": data.get("isModifiable"),
    }


@mcp.tool()
@_safe
def onshape_update_feature_studio_code(
    document_id: str,
    workspace_id: str,
    element_id: str,
    contents: Annotated[str, "Full FeatureScript source for the Feature Studio"],
) -> dict:
    """Replace the FeatureScript source of a Feature Studio.

    The returned payload includes any compile notices from Onshape. Always
    inspect `notices` — an empty list means the FS compiled cleanly.
    """
    data = client.post(
        f"/api/v10/featurestudios/d/{document_id}/w/{workspace_id}/e/{element_id}",
        json={"contents": contents},
    )
    notices = data.get("notices") or []
    return {
        "ok": not any(_is_error_notice(n) for n in notices),
        "microversionId": data.get("microversionId"),
        "notices": notices,
        "raw": data,
    }


@mcp.tool()
@_safe
def onshape_get_feature_studio_spec(
    document_id: str, workspace_id: str, element_id: str
) -> dict:
    """Get all feature specs visible to a Part Studio (built-in + custom).

    `element_id` must be the **Part Studio** element id. The response lists
    every custom feature defined in any Feature Studio in the same document,
    with the `featureTypeHash`, `namespace`, and parameter schema Onshape
    expects in `add_feature` payloads. Call this after
    `update_feature_studio_code`.
    """
    data = client.get(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}/featurespecs"
    )
    return data


@mcp.tool()
@_safe
def onshape_list_features(
    document_id: str,
    workspace_id: str,
    element_id: str,
    include_raw: Annotated[
        bool,
        "When True, return the full Onshape payload (features with all parameters, "
        "imports, defaultFeatures) — use this to learn the exact JSON shape a "
        "custom-feature add_feature call needs, per Onshape's 'inspect existing "
        "Part Studios' guidance.",
    ] = False,
) -> dict:
    """List every feature in a Part Studio plus the Part Studio's imports.

    The summary mode (default) returns featureId / name / featureType /
    status for each feature, and every `BTMImport-136` the Part Studio
    references (Onshape's standard library and any Feature Studios that have
    been imported). Use `include_raw=True` to see full feature parameters —
    necessary when reverse-engineering a custom-feature payload from a
    Part Studio you set up manually.
    """
    data = client.get(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}/features"
    )
    features = data.get("features") or []
    feature_states = data.get("featureStates") or {}
    summary = []
    for f in features:
        # v10 GET /features returns flat feature objects; older/POST payloads
        # wrap fields under "message". Read flat first, fall back to message.
        msg = f.get("message") or {}
        fid = f.get("featureId") or msg.get("featureId")
        state_raw = feature_states.get(fid) or {}
        state = state_raw.get("message") or state_raw
        summary.append(
            {
                "featureId": fid,
                "name": f.get("name") or msg.get("name"),
                "featureType": f.get("featureType") or msg.get("featureType"),
                "namespace": f.get("namespace") or msg.get("namespace"),
                "suppressed": f.get("suppressed")
                if f.get("suppressed") is not None
                else msg.get("suppressed"),
                "status": state.get("featureStatus"),
                "statusMessage": state.get("message"),
            }
        )
    result = {
        "count": len(summary),
        "features": summary,
        "imports": data.get("imports") or [],
        "sourceMicroversion": data.get("sourceMicroversion"),
    }
    if include_raw:
        result["raw"] = data
    return result


@mcp.tool()
@_safe
def onshape_delete_feature(
    document_id: str,
    workspace_id: str,
    element_id: str,
    feature_id: Annotated[str, "The featureId returned from list_features"],
) -> dict:
    """Delete a single feature from a Part Studio. Undo after a bad FS attempt."""
    return client.delete(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}"
        f"/features/featureid/{feature_id}"
    )


@mcp.tool()
@_safe
def onshape_add_feature(
    document_id: str,
    workspace_id: str,
    element_id: Annotated[str, "Part Studio element id (the target, not the Feature Studio)"],
    feature: Annotated[
        dict,
        "Full BT feature object. For custom features, build this from "
        "`get_feature_studio_spec` — copy the btType, featureType, "
        "featureTypeHash, namespace, and parameter schema from the spec.",
    ],
) -> dict:
    """Add a feature to a Part Studio (built-in or custom).

    Returns `{ok, feature_id, status, notices, raw}`. IMPORTANT: Onshape returns
    HTTP 200 even when the feature fails to regenerate — always check `ok` and
    `notices` before assuming success.
    """
    data = client.post(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}/features",
        json={"feature": feature},
    )
    return _summarize_feature_response(data)


@mcp.tool()
@_safe
def onshape_post_feature_definition_call(
    document_id: str,
    workspace_id: str,
    element_id: str,
    body: Annotated[
        dict,
        "Full POST body for /features. Usually a BTFeatureDefinitionCall-1406, "
        "but can carry extra keys like 'imports' alongside 'feature'. Use this "
        "when the bare add_feature wrapper isn't enough (e.g. bootstrap-import "
        "experiments).",
    ],
) -> dict:
    """Low-level POST to `/partstudios/.../features` — dev/experimental escape hatch."""
    data = client.post(
        f"/api/v10/partstudios/d/{document_id}/w/{workspace_id}/e/{element_id}/features",
        json=body,
    )
    return data


@mcp.tool()
@_safe
def onshape_raw_post(
    path: Annotated[str, "Full Onshape API path starting with /api/v10/..."],
    body: dict | None = None,
) -> dict:
    """Low-level authenticated POST to any Onshape endpoint — dev/experimental."""
    return client.post(path, json=body)


@mcp.tool()
@_safe
def onshape_raw_get(
    path: Annotated[str, "Full Onshape API path starting with /api/v10/..."],
) -> dict:
    """Low-level authenticated GET to any Onshape endpoint — dev/experimental."""
    return client.get(path)


def _is_error_notice(notice: dict) -> bool:
    level = (notice.get("level") or notice.get("severity") or "").upper()
    return level in {"ERROR", "FAIL", "FAILURE"}


def _summarize_feature_response(data: dict) -> dict:
    """Extract feature id + regen status + any FS notices from an add-feature reply."""
    feature_raw = data.get("feature") or {}
    feature_msg = feature_raw.get("message") or feature_raw
    feature_id = feature_msg.get("featureId")

    state_raw = data.get("featureState") or {}
    state_msg = state_raw.get("message") or state_raw
    status = state_msg.get("featureStatus")
    status_message = state_msg.get("message")

    notices = data.get("notices") or state_msg.get("notices") or []
    has_error = status == "ERROR" or any(_is_error_notice(n) for n in notices)

    return {
        "ok": not has_error,
        "feature_id": feature_id,
        "feature_name": feature_msg.get("name"),
        "status": status,
        "status_message": status_message,
        "notices": notices,
        "raw": data,
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
