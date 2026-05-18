# zoho-crm-toolkit

This toolkit exposes the Zoho CRM API surface to a coding agent without loading huge MCP schemas into prompt context.

- Endpoints indexed: 381
- Sections indexed: 97
- Groups indexed: 97
- OpenAPI source files vendored: 99
- Postman collections vendored: 0

Primary commands:
- `./cli/zoho-api search "module workflow"`
- `./cli/zoho-api show getrecords`
- `./cli/zoho-api template createrecords --kind request`
- `./cli/zoho-api call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `./cli/zoho-api verify tests/zoho-smoke.json`
