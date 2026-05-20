# Zoho Agent Workflow

Use this toolkit when a coding agent needs the full Zoho CRM API surface without loading large MCP schemas into prompt context.

Recommended workflow:
1. Read the attached requirements file and extract the target modules, workflows, layouts, fields, and expected behaviors.
2. Confirm auth and connectivity with `./cli/zoho-cli check`.
3. Search the local API index with `./cli/zoho-cli search <terms>`.
4. Inspect exact endpoint details with `./cli/zoho-cli catalog show <slug>`.
5. Generate starter payloads with `./cli/zoho-cli template <slug> --kind request`.
6. Apply changes with `./cli/zoho-cli call <slug> ...`.
7. Verify with read-back calls or `./cli/zoho-cli verify <manifest.json>`.
8. Write manual test steps for the human operator after the automated checks pass.
