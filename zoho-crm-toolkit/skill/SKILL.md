---
name: zoho-crm-toolkit
description: Use for Zoho CRM buildout, configuration, and verification tasks. Search the local Zoho API index first, inspect the exact endpoint schema second, then apply and verify changes with the generic CLI.
---

Use this skill when a task involves large-scale Zoho CRM configuration or testing.

Workflow:
1. Read the attached requirements file or local spec file.
2. Search the local API index with `./cli/zoho-api search <terms>`.
3. Inspect exact endpoint contracts with `./cli/zoho-api show <slug>`.
4. Generate request templates with `./cli/zoho-api template <slug> --kind request`.
5. Apply changes with `./cli/zoho-api call <slug> ...`.
6. Verify with read-back calls or `./cli/zoho-api verify <manifest.json>`.
7. Finish by writing clear manual test instructions for the user.

Important rules:
- Do not ask the user to locate API docs sections.
- Prefer the local `sources/openapi/` files and `spec/endpoints.json` over public docs.
- Use the generic CLI even for unfamiliar endpoint families; search and inspect first.
- Save repeatable payloads and verification manifests under `configs/` or `tests/`.

Common commands:
- `./cli/zoho-api search "workflow transitions"`
- `./cli/zoho-api show getrecords`
- `./cli/zoho-api template createrecords --kind request`
- `./cli/zoho-api call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `./cli/zoho-api verify tests/zoho-smoke.json`

References:
- `references/catalog.md`
- `references/workflow.md`
- `spec/endpoints.json`
- `sources/openapi/`
