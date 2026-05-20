# zoho-crm-toolkit

This toolkit exposes the Zoho CRM API surface to a coding agent without loading huge MCP schemas into prompt context.

- Endpoints indexed: 405
- Sections indexed: 103
- Groups indexed: 103
- OpenAPI source files vendored: 105
- Postman collections vendored: 0

Primary commands:
- `./cli/zoho-cli check`
- `./cli/zoho-cli search "module workflow"`
- `./cli/zoho-cli catalog show getrecords`
- `./cli/zoho-cli template createrecords --kind request`
- `./cli/zoho-cli call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `./cli/zoho-cli verify tests/zoho-smoke.json`
