from __future__ import annotations

from contextlib import redirect_stdout
import importlib.machinery
import importlib.util
import io
import itertools
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from urllib.error import HTTPError
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = REPO_ROOT / "zoho-crm-toolkit" / "cli" / "zoho-cli"
MODULE_COUNTER = itertools.count()


class FakeResponse:
    def __init__(self, *, status=200, body="", headers=None):
        self.status = status
        self._body = body.encode("utf-8")
        self.headers = headers or {}

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def build_http_error(url, status, body):
    return HTTPError(
        url=url,
        code=status,
        msg="error",
        hdrs={"Content-Type": "application/json"},
        fp=io.BytesIO(body.encode("utf-8")),
    )


def load_cli_module():
    module_name = f"zoho_cli_auth_test_{next(MODULE_COUNTER)}"
    loader = importlib.machinery.SourceFileLoader(module_name, str(CLI_PATH))
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


class ZohoCliAuthTests(unittest.TestCase):
    def test_load_env_files_reads_root_env_file(self):
        cli = load_cli_module()
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / ".env").write_text(
                "\n".join(
                    [
                        "ZOHO_CLIENT_ID=test-client-id",
                        "ZOHO_CLIENT_SECRET=test-client-secret",
                        "ZOHO_REFRESH_TOKEN=test-refresh-token",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            with mock.patch.object(cli, "ROOT", root):
                with mock.patch.dict(os.environ, {}, clear=True):
                    loaded = cli.load_env_files()

                    self.assertEqual(loaded, root / ".env")
                    self.assertEqual(os.environ["ZOHO_CLIENT_ID"], "test-client-id")
                    self.assertEqual(os.environ["ZOHO_CLIENT_SECRET"], "test-client-secret")
                    self.assertEqual(os.environ["ZOHO_REFRESH_TOKEN"], "test-refresh-token")

    def test_load_env_files_does_not_override_existing_environment(self):
        cli = load_cli_module()
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / ".env").write_text("ZOHO_CLIENT_ID=file-client-id\n", encoding="utf-8")
            with mock.patch.object(cli, "ROOT", root):
                with mock.patch.dict(os.environ, {"ZOHO_CLIENT_ID": "shell-client-id"}, clear=True):
                    cli.load_env_files()
                    self.assertEqual(os.environ["ZOHO_CLIENT_ID"], "shell-client-id")

    def test_auto_mode_prefers_refresh_credentials_over_direct_access_token(self):
        cli = load_cli_module()
        with TemporaryDirectory() as temp_dir:
            cache_path = Path(temp_dir) / "token-cache.json"
            env = {
                "ZOHO_AUTH_MODE": "auto",
                "ZOHO_ACCESS_TOKEN": "stale-direct-token",
                "ZOHO_CLIENT_ID": "client-id",
                "ZOHO_CLIENT_SECRET": "client-secret",
                "ZOHO_REFRESH_TOKEN": "refresh-token",
                "ZOHO_TOKEN_CACHE_FILE": str(cache_path),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(
                    cli,
                    "urlopen",
                    return_value=FakeResponse(
                        body=json.dumps(
                            {
                                "access_token": "fresh-token",
                                "api_domain": "https://www.zohoapis.com",
                                "expires_in": 3600,
                            }
                        )
                    ),
                ) as mocked_urlopen:
                    cli.AUTH_CONTEXT = None
                    auth_context = cli.resolve_auth_context()

            self.assertEqual(auth_context["source"], "refresh_token")
            self.assertEqual(auth_context["access_token"], "fresh-token")
            self.assertTrue(cache_path.exists())
            cached_payload = json.loads(cache_path.read_text(encoding="utf-8"))
            self.assertEqual(cached_payload["access_token"], "fresh-token")
            self.assertEqual(mocked_urlopen.call_count, 1)

    def test_refresh_token_cache_is_reused_without_refreshing(self):
        cli = load_cli_module()
        with TemporaryDirectory() as temp_dir:
            cache_path = Path(temp_dir) / "token-cache.json"
            cache_path.write_text(
                json.dumps(
                    {
                        "access_token": "cached-token",
                        "api_domain": "https://www.zohoapis.com",
                        "expires_at": cli.current_time() + 600,
                        "refreshed_at": cli.current_time(),
                    }
                ),
                encoding="utf-8",
            )
            env = {
                "ZOHO_AUTH_MODE": "auto",
                "ZOHO_CLIENT_ID": "client-id",
                "ZOHO_CLIENT_SECRET": "client-secret",
                "ZOHO_REFRESH_TOKEN": "refresh-token",
                "ZOHO_TOKEN_CACHE_FILE": str(cache_path),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(
                    cli,
                    "urlopen",
                    side_effect=AssertionError("Cached token should avoid refresh HTTP calls."),
                ):
                    cli.AUTH_CONTEXT = None
                    auth_context = cli.resolve_auth_context()

            self.assertEqual(auth_context["source"], "refresh_token_cache")
            self.assertEqual(auth_context["access_token"], "cached-token")

    def test_execute_request_refreshes_once_after_invalid_token_response(self):
        cli = load_cli_module()
        endpoint = {"method": "GET", "path": "/Leads", "request_body": {}}

        with TemporaryDirectory() as temp_dir:
            cache_path = Path(temp_dir) / "token-cache.json"
            cache_path.write_text(
                json.dumps(
                    {
                        "access_token": "expired-token",
                        "api_domain": "https://www.zohoapis.com",
                        "expires_at": cli.current_time() + 600,
                        "refreshed_at": cli.current_time(),
                    }
                ),
                encoding="utf-8",
            )
            env = {
                "ZOHO_AUTH_MODE": "auto",
                "ZOHO_CLIENT_ID": "client-id",
                "ZOHO_CLIENT_SECRET": "client-secret",
                "ZOHO_REFRESH_TOKEN": "refresh-token",
                "ZOHO_TOKEN_CACHE_FILE": str(cache_path),
            }
            requests = []

            def fake_urlopen(request):
                url = request.full_url
                auth_header = request.headers.get("Authorization")
                requests.append((url, auth_header))
                if url.endswith("/oauth/v2/token"):
                    return FakeResponse(
                        body=json.dumps(
                            {
                                "access_token": "fresh-token",
                                "api_domain": "https://www.zohoapis.com",
                                "expires_in": 3600,
                            }
                        )
                    )
                if auth_header == "Zoho-oauthtoken expired-token":
                    raise build_http_error(
                        url,
                        401,
                        json.dumps(
                            {
                                "code": "INVALID_OAUTH_TOKEN",
                                "message": "invalid oauth token",
                            }
                        ),
                    )
                if auth_header == "Zoho-oauthtoken fresh-token":
                    return FakeResponse(body=json.dumps({"data": []}))
                raise AssertionError(f"Unexpected request: {url} {auth_header}")

            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(cli, "urlopen", side_effect=fake_urlopen):
                    cli.AUTH_CONTEXT = None
                    status, _, body, _, request_headers = cli.execute_request(
                        endpoint,
                        {},
                        {},
                        {},
                        None,
                    )

            self.assertEqual(status, 200)
            self.assertEqual(json.loads(body), {"data": []})
            self.assertEqual(request_headers["Authorization"], "Zoho-oauthtoken fresh-token")
            self.assertEqual(
                requests,
                [
                    ("https://www.zohoapis.com/crm/v8/Leads", "Zoho-oauthtoken expired-token"),
                    ("https://accounts.zoho.com/oauth/v2/token", None),
                    ("https://www.zohoapis.com/crm/v8/Leads", "Zoho-oauthtoken fresh-token"),
                ],
            )
            cached_payload = json.loads(cache_path.read_text(encoding="utf-8"))
            self.assertEqual(cached_payload["access_token"], "fresh-token")

    def test_command_check_reports_success(self):
        cli = load_cli_module()
        spec = [
            {
                "slug": "getorganization",
                "title": "Get Organization data",
                "method": "GET",
                "path": "/org",
            }
        ]
        stdout = io.StringIO()
        args = type("Args", (), {"selector": "getorganization", "json": False})()
        with mock.patch.object(cli, "load_spec", return_value=spec):
            with mock.patch.object(
                cli,
                "execute_request",
                return_value=(
                    200,
                    {},
                    json.dumps({"org": [{"company_name": "Acme", "id": "123", "type": "production"}]}),
                    "https://www.zohoapis.com/crm/v8/org",
                    {},
                ),
            ):
                with mock.patch.object(cli, "resolve_auth_context", return_value={"source": "refresh_token_cache"}):
                    with redirect_stdout(stdout):
                        cli.command_check(args)

        output = stdout.getvalue()
        self.assertIn("PASS\tZoho connection verified", output)
        self.assertIn("Check: getorganization", output)
        self.assertIn("company_name: Acme", output)
        self.assertIn("org_id: 123", output)

    def test_command_check_falls_back_after_scope_failure(self):
        cli = load_cli_module()
        spec = [
            {
                "slug": "getorganization",
                "title": "Get Organization data",
                "method": "GET",
                "path": "/org",
            },
            {
                "slug": "getavailableapis",
                "title": "List available REST APIs",
                "method": "GET",
                "path": "/__apis",
            },
        ]
        stdout = io.StringIO()
        args = type("Args", (), {"selector": None, "json": False})()
        execute_results = [
            (
                403,
                {},
                json.dumps({"code": "NO_PERMISSION", "message": "required oauth scope is missing"}),
                "https://www.zohoapis.com/crm/v8/org",
                {},
            ),
            (
                200,
                {},
                json.dumps({"__apis": [{"path": "/crm/v8/org"}, {"path": "/crm/v8/Leads"}]}),
                "https://www.zohoapis.com/crm/v8/__apis",
                {},
            ),
        ]
        with mock.patch.object(cli, "load_spec", return_value=spec):
            with mock.patch.object(cli, "execute_request", side_effect=execute_results):
                with mock.patch.object(cli, "resolve_auth_context", return_value={"source": "refresh_token"}):
                    with redirect_stdout(stdout):
                        cli.command_check(args)

        output = stdout.getvalue()
        self.assertIn("PASS\tZoho connection verified", output)
        self.assertIn("Check: getavailableapis", output)
        self.assertIn("available_api_count: 2", output)


if __name__ == "__main__":
    unittest.main()
