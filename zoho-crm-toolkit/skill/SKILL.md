---
name: zoho-crm-toolkit
description: Use for Zoho CRM buildout, configuration, and verification tasks. Search the local Zoho API index first, inspect the exact endpoint schema second, then apply and verify changes with the generic CLI.
---

Use this skill when a task involves large-scale Zoho CRM configuration or testing.

Workflow:
1. Read the attached requirements file or local spec file.
2. Confirm auth and connectivity with `./cli/zoho-cli check`.
3. Search the local API index with `./cli/zoho-cli search <terms>`.
4. Inspect exact endpoint contracts with `./cli/zoho-cli catalog show <slug>`.
5. Generate request templates with `./cli/zoho-cli template <slug> --kind request`.
6. Apply changes with `./cli/zoho-cli call <slug> ...`.
7. Verify with read-back calls or `./cli/zoho-cli verify <manifest.json>`.
8. Finish by writing clear manual test instructions for the user.

Important rules:
- Do not ask the user to locate API docs sections.
- Prefer the local `sources/openapi/` files and `spec/endpoints.json` over public docs.
- Use the generic CLI even for unfamiliar endpoint families; search and inspect first.
- Save repeatable payloads and verification manifests under `configs/` or `tests/`.

Common commands:
- `./cli/zoho-cli check`
- `./cli/zoho-cli search "workflow transitions"`
- `./cli/zoho-cli catalog show getrecords`
- `./cli/zoho-cli template createrecords --kind request`
- `./cli/zoho-cli call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `./cli/zoho-cli verify tests/zoho-smoke.json`

References:
- `references/catalog.md`
- `references/workflow.md`
- `spec/endpoints.json`
- `sources/openapi/`
