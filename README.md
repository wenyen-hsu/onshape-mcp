# Onshape MCP Server

A Model Context Protocol (MCP) server that lets Claude (in Claude Code / Claude
Desktop) call the Onshape REST API via natural language. Read existing
documents, or drive FeatureScript upload + custom-feature invocation to create
parametric geometry from conversation.

## Prerequisites

- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) (`brew install uv` / `pipx install uv` / `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- An Onshape account with API keys from <https://dev-portal.onshape.com/keys>
- Claude Code or Claude Desktop installed

## Tools exposed

### Read-only

| Tool | What it does |
|---|---|
| `onshape_whoami` | Return the authenticated user (sanity check) |
| `onshape_list_documents` | List your documents (optional name filter) |
| `onshape_get_document` | Get a single document's metadata |
| `onshape_list_elements` | List Part Studios / Assemblies / Drawings in a workspace |
| `onshape_get_parts` | List parts inside a Part Studio |
| `onshape_get_mass_properties` | Mass / volume / centroid for a part or whole studio |
| `onshape_parse_url` | Parse an Onshape URL into `did` / `wid` / `eid` |
| `onshape_export_part_studio` | Export Part Studio to STEP / STL / PARASOLID / IGES |

### Write / FeatureScript workflow

| Tool | What it does |
|---|---|
| `onshape_create_feature_studio` | Create a new empty Feature Studio element |
| `onshape_get_feature_studio_code` | Read the FS source of a Feature Studio |
| `onshape_update_feature_studio_code` | Replace FS source; returns compile notices |
| `onshape_get_feature_studio_spec` | Get computed spec for every custom feature (use this to build `add_feature` payloads) |
| `onshape_list_features` | List features in a Part Studio + each feature's regen status |
| `onshape_add_feature` | Add a feature to a Part Studio; surfaces FS regen errors |
| `onshape_delete_feature` | Delete a single feature by id |

## Setup

### 1. Clone or extract this folder somewhere, then install dependencies

```bash
cd path/to/onshape-mcp
uv sync
```

### 2. Configure credentials

Copy `.env.example` to `.env` and fill in your Onshape API keys:

```bash
cp .env.example .env
```

Then edit `.env`:

```
ONSHAPE_ACCESS_KEY=...        # the username-like string
ONSHAPE_SECRET_KEY=...        # the longer secret
ONSHAPE_BASE_URL=https://cad.onshape.com
```

`.env` is git-ignored — never commit it.

### 3a. Register with Claude Code

```bash
claude mcp add onshape \
  --scope user \
  -- uv --directory /absolute/path/to/onshape-mcp run onshape-mcp
```

Replace `/absolute/path/to/onshape-mcp` with the actual absolute path on your
machine (for example `~/code/onshape-mcp` after `realpath`).

Restart Claude Code. Confirm with `/mcp` — `onshape` should appear as
connected.

### 3b. Or register with Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS) or the Windows equivalent:

```json
{
  "mcpServers": {
    "onshape": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/onshape-mcp",
        "run",
        "onshape-mcp"
      ]
    }
  }
}
```

Restart Claude Desktop.

## Example prompts

Once registered you can say things like:

- "List my Onshape documents."
- "In the document 'trashcan', what Part Studios does it contain?"
- "In this URL `https://cad.onshape.com/documents/.../w/.../e/...`, what's the mass of the first part?"
- "Export the main Part Studio of 'trashcan' as STEP to ~/Desktop."
- "Given this spec sheet, write a FeatureScript that creates the part in Part Studio X." _(see FeatureScript workflow below)_

## FeatureScript workflow (writing geometry from conversation)

The recommended flow for asking Claude to build a parametric part:

1. Parse an Onshape document URL → `onshape_parse_url` → yields `did` / `wid` / `eid`
2. Locate (or create) a Feature Studio: `onshape_list_elements` → if none, `onshape_create_feature_studio`
3. Claude writes FS source → `onshape_update_feature_studio_code`; inspect `notices` for compile errors and iterate
4. Fetch the computed spec → `onshape_get_feature_studio_spec`. This returns the canonical `featureTypeHash`, `namespace`, and parameter schema — use these to build the `add_feature` payload. **Don't hand-assemble the payload.**
5. Invoke the feature → `onshape_add_feature(feature=…)`. **Always check** `ok` and `notices` in the response — Onshape returns HTTP 200 even when a feature fails to regenerate.
6. If the feature failed, `onshape_delete_feature(feature_id)` and try again with fixed FS.
7. Verify with `onshape_list_features`.

## API usage limits

Onshape enforces annual API call quotas at the user / company level
(Free: 2,500 calls/user/year, Professional: 5,000, Enterprise: 10,000).
Exceeding the annual quota returns HTTP 402. Per-endpoint rate limits also
apply and return HTTP 429 with an `X-Rate-Limit-Remaining` header.

Every parametric-part build typically costs 3–5 API calls, so budget
accordingly. Full details: see `docs/onshape-api-docs.md` (§ API Limits) or
<https://onshape-public.github.io/docs/auth/limits/>.

## File layout

```
onshape-mcp/
├── .env.example            # copy to .env and fill in
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
├── docs/
│   └── onshape-api-docs.md   # local mirror of the Onshape developer docs
├── scripts/
│   └── debug_features.py     # manual API probe for debugging
└── src/onshape_mcp/
    ├── __init__.py
    ├── auth.py               # HMAC-SHA256 request signing
    ├── client.py             # httpx wrapper + 307 re-sign
    └── server.py             # FastMCP server + tool definitions
```

## Troubleshooting

- **`401 Unauthorized`** — check `.env` keys. Access Key is the shorter username-like string, Secret Key is the longer one.
- **`404` on a tool that expects `workspace_id`** — run `onshape_get_document` first and grab `defaultWorkspace.id`, or use `onshape_parse_url` on a document URL.
- **`429 Too Many Requests`** — you're hitting a per-endpoint rate cap; wait a minute and slow down. Watch `X-Rate-Limit-Remaining`.
- **`402 Payment Required`** — annual API quota exhausted. See API Limits above.
- **Clock skew** — the `Date` header must be within 5 minutes of Onshape's server. If your system clock is off, signing fails.
- **`onshape_add_feature` returns `ok: true` but the feature didn't appear** — double-check `notices` and `status` in the response. Onshape sometimes warns rather than errors.
- **Changes to `server.py` don't appear in Claude** — restart Claude Code / Desktop. MCP servers are only started at launch.

## License / credits

This server is a thin wrapper over the public Onshape REST API. You must
have your own Onshape account and API keys; the keys in `.env` stay local.
