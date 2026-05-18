# Zoho Agent Workflow

Use this toolkit when a coding agent needs the full Zoho CRM API surface without loading large MCP schemas into prompt context.

Recommended workflow:
1. Read the attached requirements file and extract the target modules, workflows, layouts, fields, and expected behaviors.
2. Search the local API index with `./cli/zoho-api search <terms>`.
3. Inspect exact endpoint details with `./cli/zoho-api show <slug>`.
4. Generate starter payloads with `./cli/zoho-api template <slug> --kind request`.
5. Apply changes with `./cli/zoho-api call <slug> ...`.
6. Verify with read-back calls or `./cli/zoho-api verify <manifest.json>`.
7. Write manual test steps for the human operator after the automated checks pass.
