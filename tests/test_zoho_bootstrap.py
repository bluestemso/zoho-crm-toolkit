from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import unittest

import zoho_bootstrap


FIXTURES = Path(__file__).parent / "fixtures"


class ZohoBootstrapTests(unittest.TestCase):
    def test_parse_catalog_and_details(self):
        catalog_url = (FIXTURES / "api-references.html").as_uri()
        endpoints = zoho_bootstrap.build_spec(
            docs_url=catalog_url,
            catalog_url=catalog_url,
            with_details=True,
        )

        self.assertEqual(len(endpoints), 2)
        records = next(item for item in endpoints if item.slug == "get-records")
        self.assertEqual(records.method, "GET")
        self.assertEqual(records.path, "/{module_api_name}")
        self.assertIn("fields string, mandatory", records.parameters)

        module = next(item for item in endpoints if item.slug == "get-a-specific-module")
        self.assertEqual(module.method, "GET")
        self.assertEqual(module.path, "/settings/modules/{module_API_name}")

    def test_build_spec_from_openapi_source(self):
        source = str(FIXTURES / "openapi-records.json")
        endpoints = zoho_bootstrap.build_spec_from_openapi_sources([source])
        self.assertEqual(len(endpoints), 2)

        endpoint = next(item for item in endpoints if item.slug == "getrecords")
        self.assertEqual(endpoint.method, "GET")
        self.assertEqual(endpoint.path, "/{module}")
        self.assertIn("module string (path, required)", endpoint.parameters)
        self.assertIn("fields string (query, optional)", endpoint.parameters)
        self.assertIn("Leads", endpoint.supported_modules)

        create = next(item for item in endpoints if item.slug == "createrecords")
        self.assertEqual(create.method, "POST")
        self.assertEqual(create.request_body["content_type"], "application/json")
        self.assertIn("data", create.request_body["schema"]["properties"])

    def test_build_spec_from_postman_source(self):
        source = str(FIXTURES / "postman-collection.json")
        endpoints = zoho_bootstrap.build_spec_from_postman_sources([source])
        self.assertEqual(len(endpoints), 1)
        endpoint = endpoints[0]
        self.assertEqual(endpoint.slug, "get-records")
        self.assertEqual(endpoint.method, "GET")
        self.assertEqual(endpoint.path, "/crm/v8/:module")
        self.assertIn("fields string (query, optional)", endpoint.parameters)

    def test_scaffold_writes_expected_files(self):
        catalog_url = (FIXTURES / "api-references.html").as_uri()
        with TemporaryDirectory() as temp_dir:
            exit_code = zoho_bootstrap.main(
                [
                    "scaffold",
                    "--docs-url",
                    catalog_url,
                    "--catalog-url",
                    catalog_url,
                    "--output",
                    temp_dir,
                    "--name",
                    "zoho-crm-test",
                ]
            )

            self.assertEqual(exit_code, 0)
            output_dir = Path(temp_dir)
            self.assertTrue((output_dir / "spec" / "endpoints.json").exists())
            self.assertTrue((output_dir / "skill" / "SKILL.md").exists())
            self.assertTrue((output_dir / "cli" / "zoho-api").exists())

            payload = json.loads((output_dir / "spec" / "endpoints.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload), 2)
            self.assertEqual(payload[0]["section"], "Metadata APIs")

    def test_scaffold_writes_openapi_files_and_cli_works(self):
        with TemporaryDirectory() as temp_dir:
            exit_code = zoho_bootstrap.main(
                [
                    "scaffold",
                    "--openapi-file",
                    str(FIXTURES / "openapi-records.json"),
                    "--output",
                    temp_dir,
                    "--name",
                    "zoho-openapi-test",
                ]
            )

            self.assertEqual(exit_code, 0)
            output_dir = Path(temp_dir)
            payload = json.loads((output_dir / "spec" / "endpoints.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload), 2)
            self.assertEqual(payload[0]["section"], "Records")
            self.assertTrue((output_dir / "sources" / "openapi" / "openapi-records.json").exists())
            env_example = (output_dir / ".env.example").read_text(encoding="utf-8")
            self.assertIn("ZOHO_REFRESH_TOKEN=", env_example)
            self.assertIn("ZOHO_CLIENT_ID=", env_example)

            cli_output = subprocess.check_output(
                [str(output_dir / "cli" / "zoho-api"), "template", "createrecords", "--kind", "body"],
                text=True,
            )
            body_template = json.loads(cli_output)
            self.assertIn("data", body_template)

    def test_parse_detail_handles_split_bullets(self):
        text = "\n".join(
            [
                "# Modules API",
                "#### Endpoints",
                "*",
                "GET /settings/modules",
                "Copy full URL",
                "#### Parameters",
                "* status string, optional",
                "* visible - not a parameter definition",
            ]
        )
        detail = zoho_bootstrap.parse_detail(text)
        self.assertEqual(detail["method"], "GET")
        self.assertEqual(detail["path"], "/settings/modules")
        self.assertEqual(detail["parameters"], ["status string, optional"])

    def test_discover_openapi_sources_from_html(self):
        html = (FIXTURES / "zoho-oas-index.html").read_text(encoding="utf-8")
        urls = zoho_bootstrap.discover_openapi_sources_from_html(
            html,
            "https://github.com/zoho/crm-oas/tree/main/v8.0",
        )
        self.assertEqual(
            urls,
            [
                "https://raw.githubusercontent.com/zoho/crm-oas/main/v8.0/apis.json",
                "https://raw.githubusercontent.com/zoho/crm-oas/main/v8.0/modules.json",
                "https://raw.githubusercontent.com/zoho/crm-oas/main/v8.0/record.json",
            ],
        )


if __name__ == "__main__":
    unittest.main()
