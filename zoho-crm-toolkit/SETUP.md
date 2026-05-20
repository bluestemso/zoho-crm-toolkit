# Zoho CRM Toolkit Setup

## What this folder is

This folder contains a local Zoho CRM API toolkit that a coding agent can use without loading a large MCP schema into prompt context.

Important files:

- `cli/zoho-cli`: Generic CLI for searching, inspecting, templating, calling, and verifying Zoho APIs.
- `spec/endpoints.json`: Searchable index of the Zoho CRM API surface.
- `sources/openapi/`: Vendored Zoho OpenAPI files.
- `skill/SKILL.md`: Short instructions for an agent that supports Codex-style skills.
- `references/workflow.md`: Recommended agent workflow.
- `tests/zoho-smoke.json`: Example verification manifest.
- `.env.example`: Required environment variables.

## Simplest way to use it

Keep the entire `zoho-crm-toolkit/` folder together.

The minimum working setup is:

1. Copy this folder into the repository or workspace where your coding agent will work.
2. Set either `ZOHO_ACCESS_TOKEN`, or the long-lived refresh-token credentials.
3. Tell the agent to use `./zoho-crm-toolkit/cli/zoho-cli` for all Zoho work.

## Environment setup

Example:

```bash
cd /path/to/your/project
cp /path/to/zoho-crm-toolkit/.env.example .env.zoho
```

Edit `.env.zoho` and set either a direct access token:

```bash
ZOHO_DC=com
ZOHO_API_VERSION=v8
ZOHO_AUTH_MODE=access_token
ZOHO_ACCESS_TOKEN=your_access_token_here
```

Or the preferred long-lived setup:

```bash
ZOHO_DC=com
ZOHO_API_VERSION=v8
ZOHO_AUTH_MODE=auto
ZOHO_CLIENT_ID=your_client_id_here
ZOHO_CLIENT_SECRET=your_client_secret_here
ZOHO_REFRESH_TOKEN=your_refresh_token_here
```

With the refresh-token setup, `zoho-cli` will automatically request a fresh access token when it needs one, cache it locally, and retry once if Zoho rejects an expired token.

## How auth selection works

The CLI now uses a simple precedence model:

1. `ZOHO_AUTH_MODE=auto`:
   - If refresh-token credentials exist, they win.
   - The CLI reuses a cached access token between runs to avoid hammering Zoho's token endpoint.
   - If Zoho returns an invalid-token auth error, the CLI refreshes once and retries the API call.
2. `ZOHO_AUTH_MODE=refresh_token`:
   - Ignore `ZOHO_ACCESS_TOKEN` and always use the refresh-token workflow.
3. `ZOHO_AUTH_MODE=access_token`:
   - Ignore refresh-token credentials and always use `ZOHO_ACCESS_TOKEN`.

This matters because `ZOHO_ACCESS_TOKEN` is short-lived. If you leave both token types set and keep `ZOHO_AUTH_MODE=auto`, the CLI will favor the more stable refresh-token workflow by default.

## Token cache

By default the CLI writes refresh-derived access tokens to:

```bash
./zoho-crm-toolkit/.zoho-token-cache.json
```

You can change that with `ZOHO_TOKEN_CACHE_FILE` if you want the cache somewhere else.

Then load it:

```bash
set -a
source .env.zoho
set +a
```

`zoho-cli` will also auto-load environment files on startup. It checks these locations in order and keeps any variables that are already exported in your shell:

1. `ZOHO_ENV_FILE` if you set it
2. `./.env.zoho`
3. `./.env`
4. `./zoho-crm-toolkit/.env.zoho`
5. `./zoho-crm-toolkit/.env`

## Quick CLI checks

Run these from the project directory:

```bash
./zoho-crm-toolkit/cli/zoho-cli check
./zoho-crm-toolkit/cli/zoho-cli search "module"
./zoho-crm-toolkit/cli/zoho-cli catalog show getmodules
./zoho-crm-toolkit/cli/zoho-cli template createrecords --kind request
./zoho-crm-toolkit/cli/zoho-cli call getmodules --parse-json
./zoho-crm-toolkit/cli/zoho-cli verify ./zoho-crm-toolkit/tests/zoho-smoke.json
```

If `check` works, the toolkit is connected correctly. `call` and `verify` are the next-level checks once you want to test a specific endpoint or workflow.

## Using with Claude Code

Claude Code does not use Codex `SKILL.md` files directly, so the easiest approach is:

1. Copy `zoho-crm-toolkit/` into your repo.
2. Add a short note to your repo-level agent instructions file such as `CLAUDE.md` or `AGENTS.md`.
3. Tell Claude to use the local CLI and local spec files instead of public docs.

Suggested instruction text:

```md
Use `./zoho-crm-toolkit/cli/zoho-cli` for all Zoho CRM work.
Search the local API index before making assumptions:
- `./zoho-crm-toolkit/cli/zoho-cli check`
- `./zoho-crm-toolkit/cli/zoho-cli search "<terms>"`
- `./zoho-crm-toolkit/cli/zoho-cli catalog show <slug>`
- `./zoho-crm-toolkit/cli/zoho-cli template <slug> --kind request`
- `./zoho-crm-toolkit/cli/zoho-cli call ...`
- `./zoho-crm-toolkit/cli/zoho-cli verify <manifest>`

Prefer these local files over public docs:
- `./zoho-crm-toolkit/spec/endpoints.json`
- `./zoho-crm-toolkit/sources/openapi/`
- `./zoho-crm-toolkit/references/workflow.md`
```

## Using with Codex

If you want Codex to load the skill directly, copy:

- `zoho-crm-toolkit/skill/SKILL.md`
- `zoho-crm-toolkit/skill/agents/openai.yaml`

into a skill folder under your Codex skills directory, or keep the toolkit in the repo and tell Codex to read `skill/SKILL.md`.

## Example prompt to the agent

```text
Read the attached Zoho requirements file.
Use the local Zoho toolkit in ./zoho-crm-toolkit.
Build the required module, fields, layouts, workflows, and supporting configuration.
Verify the result with read-back API calls and a verification manifest.
Then provide:
1. a summary of what you changed
2. any verification results
3. exact manual test steps I should run myself
```

## If you want stronger verification

Create a manifest file like:

```json
{
  "checks": [
    {
      "name": "Leads module responds",
      "selector": "getrecords",
      "path_params": {
        "module": "Leads"
      },
      "query": {
        "fields": "Last_Name,Email"
      },
      "expect_status": [200, 204]
    }
  ]
}
```

Then run:

```bash
./zoho-crm-toolkit/cli/zoho-cli verify path/to/manifest.json --verbose
```
