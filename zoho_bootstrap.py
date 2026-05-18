#!/usr/bin/env python3
"""Build a compact Zoho CRM toolkit from OpenAPI, Postman, or HTML docs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen


DEFAULT_CATALOG_PAGE = "api-references.html"
DEFAULT_ZOHO_OAS_INDEX_URL = "https://github.com/zoho/crm-oas/tree/main/v8.0"
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}
PREFERRED_CONTENT_TYPES = ["application/json", "multipart/form-data"]


@dataclass
class Endpoint:
    slug: str
    title: str
    description: str
    section: str
    group: str
    url: str
    source_name: str
    source_kind: str
    method: Optional[str] = None
    path: Optional[str] = None
    request_url: Optional[str] = None
    purpose: Optional[str] = None
    scopes: List[str] = field(default_factory=list)
    supported_modules: List[str] = field(default_factory=list)
    parameters: List[str] = field(default_factory=list)
    parameter_details: List[Dict[str, Any]] = field(default_factory=list)
    request_body: Optional[Dict[str, Any]] = None
    responses: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)


class MarkdownishHTMLParser(HTMLParser):
    """Convert HTML to a line-oriented format that is easy to parse."""

    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        tag = tag.lower()
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self.parts.append("\n" + ("#" * level) + " ")
        elif tag == "li":
            self.parts.append("\n* ")
        elif tag in {"p", "div", "section", "article", "table", "tr"}:
            self.parts.append("\n")
        elif tag in {"br", "hr"}:
            self.parts.append("\n")
        elif tag in {"td", "th"}:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        if tag.lower() in {"h1", "h2", "h3", "h4", "h5", "h6", "li", "p", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        cleaned = data.replace("\xa0", " ")
        if cleaned.strip():
            self.parts.append(cleaned)

    def get_text(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        lines = [line.strip() for line in text.splitlines()]
        lines = [line for line in lines if line]
        return "\n".join(lines)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def fetch_text(url: str) -> str:
    with urlopen(url) as response:  # noqa: S310 - caller controls the URL.
        return response.read().decode("utf-8", errors="replace")


def read_text_source(source: str) -> str:
    if re.match(r"^(https?|file)://", source):
        return fetch_text(source)
    return Path(source).read_text(encoding="utf-8")


def read_json_source(source: str) -> Dict[str, Any]:
    return json.loads(read_text_source(source))


def write_file(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | 0o111)


def local_template_text(*relative_parts: str) -> str:
    path = Path(__file__).resolve().parent.joinpath(*relative_parts)
    return path.read_text(encoding="utf-8")


def source_basename(source: str) -> str:
    if re.match(r"^(https?|file)://", source):
        return Path(urlparse(source).path).name
    return Path(source).name


def dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen = set()
    unique: List[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        unique.append(value)
    return unique


def extract_links(html: str, base_url: str) -> Dict[str, str]:
    pattern = re.compile(
        r"<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>",
        flags=re.IGNORECASE | re.DOTALL,
    )
    links: Dict[str, str] = {}
    for href, inner in pattern.findall(html):
        label = re.sub(r"<[^>]+>", " ", inner)
        label = re.sub(r"\s+", " ", label).strip()
        if not label:
            continue
        links.setdefault(label, urljoin(base_url, href))
    return links


def html_to_text(html: str) -> str:
    parser = MarkdownishHTMLParser()
    parser.feed(html)
    return parser.get_text()


def parse_catalog(text: str, links: Dict[str, str]) -> List[Endpoint]:
    endpoints: List[Endpoint] = []
    current_section = ""
    current_group = ""
    ignored_sections = {"On this page"}

    for line in text.splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue
        if line.startswith("### "):
            current_group = line[4:].strip()
            continue
        if not line.startswith("* "):
            continue
        if current_section in ignored_sections:
            continue

        item = line[2:].strip()
        if " - " not in item:
            continue
        title, description = item.split(" - ", 1)
        url = links.get(title)
        if not url:
            continue

        endpoints.append(
            Endpoint(
                slug=slugify(title),
                title=title,
                description=description.strip(),
                section=current_section,
                group=current_group,
                url=url,
                source_name=source_basename(url),
                source_kind="html",
            )
        )

    unique: Dict[str, Endpoint] = {}
    for endpoint in endpoints:
        unique.setdefault(endpoint.slug, endpoint)
    return list(unique.values())


def collect_section(lines: List[str], header_names: Iterable[str]) -> List[str]:
    normalized = {name.lower() for name in header_names}
    for index, line in enumerate(lines):
        if line.lower() in normalized:
            section_lines: List[str] = []
            for candidate in lines[index + 1 :]:
                if candidate.startswith("#"):
                    break
                section_lines.append(candidate)
            return section_lines
    return []


def parse_detail(text: str) -> Dict[str, Any]:
    lines = text.splitlines()
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    detail: Dict[str, Any] = {"title": title}

    purpose_lines = collect_section(lines, {"#### Purpose", "### Purpose"})
    if purpose_lines:
        detail["purpose"] = " ".join(purpose_lines).strip()

    endpoint_lines = collect_section(lines, {"#### Endpoints", "### Endpoints"})
    method = None
    path = None
    for index, line in enumerate(endpoint_lines):
        candidate = line
        if candidate in {"*", "-"} and index + 1 < len(endpoint_lines):
            candidate = endpoint_lines[index + 1]
        if candidate.startswith("* "):
            candidate = candidate[2:].strip()
        match = re.match(r"([A-Z]+) ([^ ]+)", candidate)
        if match:
            method = match.group(1)
            path = match.group(2).replace("Copy", "").strip()
            break
    if method:
        detail["method"] = method
    if path:
        detail["path"] = path

    request_url_lines = collect_section(lines, {"#### Request URL", "### Request URL"})
    if request_url_lines:
        detail["request_url"] = request_url_lines[0]

    scope_lines = collect_section(lines, {"#### Scope", "### Scope"})
    scopes = []
    for line in scope_lines:
        if line.startswith("(") or line == "or":
            continue
        if line.startswith("* "):
            scopes.append(line[2:].strip())
        else:
            scopes.append(line.strip())
    scopes = [scope for scope in scopes if scope]
    if scopes:
        detail["scopes"] = scopes

    supported_lines = collect_section(
        lines,
        {
            "##### Supported modules",
            "#### Supported modules",
            "### Supported modules",
        },
    )
    if supported_lines:
        supported = re.split(r",|\band\b", supported_lines[0])
        detail["supported_modules"] = [item.strip() for item in supported if item.strip()]

    parameter_lines = collect_section(lines, {"##### Parameters", "#### Parameters"})
    parameters = []
    for line in parameter_lines:
        candidate = line[2:].strip() if line.startswith("* ") else line.strip()
        if re.match(
            r"^[A-Za-z_$][A-Za-z0-9_$]*\s+(string|integer|long|boolean|date|json|array|double)\b",
            candidate,
            flags=re.IGNORECASE,
        ):
            parameters.append(candidate)
    if parameters:
        detail["parameters"] = parameters

    return detail


def enrich_endpoints(endpoints: List[Endpoint], max_detail_pages: Optional[int] = None) -> List[Endpoint]:
    selected = endpoints
    if max_detail_pages is not None and max_detail_pages > 0:
        selected = endpoints[:max_detail_pages]

    for endpoint in selected:
        detail_html = fetch_text(endpoint.url)
        detail = parse_detail(html_to_text(detail_html))
        endpoint.method = detail.get("method")
        endpoint.path = detail.get("path")
        endpoint.request_url = detail.get("request_url")
        endpoint.purpose = detail.get("purpose")
        endpoint.scopes = list(detail.get("scopes", []))
        endpoint.supported_modules = list(detail.get("supported_modules", []))
        endpoint.parameters = list(detail.get("parameters", []))
    return endpoints


def render_server_url(server: Dict[str, Any]) -> str:
    url = str(server.get("url", ""))
    variables = server.get("variables", {})
    if not isinstance(variables, dict):
        return url
    for name, metadata in variables.items():
        if not isinstance(metadata, dict):
            continue
        enum_values = metadata.get("enum", [])
        default = metadata.get("default")
        if default is None and isinstance(enum_values, list) and enum_values:
            default = enum_values[0]
        if default is None:
            default = ""
        url = url.replace("{" + str(name) + "}", str(default))
    return url


def resolve_local_ref(document: Dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        return None
    current: Any = document
    for part in ref[2:].split("/"):
        key = part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def normalize_schema(document: Dict[str, Any], schema: Any) -> Dict[str, Any]:
    if not isinstance(schema, dict):
        return {}
    if "$ref" in schema:
        return normalize_schema(document, resolve_local_ref(document, str(schema["$ref"])))
    if "allOf" in schema and isinstance(schema["allOf"], list):
        merged: Dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        descriptions = []
        for item in schema["allOf"]:
            normalized = normalize_schema(document, item)
            if normalized.get("description"):
                descriptions.append(normalized["description"])
            if normalized.get("type") == "object":
                merged["properties"].update(normalized.get("properties", {}))
                merged["required"].extend(normalized.get("required", []))
        merged["required"] = dedupe_preserve_order(merged["required"])
        if descriptions:
            merged["description"] = " ".join(descriptions)
        return merged
    for composite in ("oneOf", "anyOf"):
        if composite in schema and isinstance(schema[composite], list):
            for item in schema[composite]:
                normalized = normalize_schema(document, item)
                schema_type = normalized.get("type")
                if schema_type and schema_type != "null":
                    return normalized
    normalized = dict(schema)
    schema_type = normalized.get("type")
    if isinstance(schema_type, list):
        normalized["type"] = next((item for item in schema_type if item != "null"), schema_type[0])
    return normalized


def simplify_schema(
    document: Dict[str, Any],
    schema: Any,
    *,
    max_depth: int = 4,
    depth: int = 0,
) -> Dict[str, Any]:
    normalized = normalize_schema(document, schema)
    if not normalized:
        return {}

    result: Dict[str, Any] = {}
    schema_type = normalized.get("type", "object")
    result["type"] = schema_type
    if normalized.get("description"):
        result["description"] = normalized["description"]
    if "enum" in normalized:
        result["enum"] = normalized["enum"]
    if "default" in normalized:
        result["default"] = normalized["default"]
    if "example" in normalized:
        result["example"] = normalized["example"]

    if depth >= max_depth:
        if "properties" in normalized:
            result["properties"] = sorted(normalized.get("properties", {}).keys())
        return result

    if schema_type == "object":
        properties = normalized.get("properties", {})
        required = normalized.get("required", [])
        simplified_properties: Dict[str, Any] = {}
        if isinstance(properties, dict):
            for name, value in properties.items():
                simplified_properties[name] = simplify_schema(
                    document,
                    value,
                    max_depth=max_depth,
                    depth=depth + 1,
                )
        result["properties"] = simplified_properties
        if required:
            result["required"] = required
    elif schema_type == "array":
        result["items"] = simplify_schema(
            document,
            normalized.get("items", {}),
            max_depth=max_depth,
            depth=depth + 1,
        )

    return result


def build_example_from_schema(schema: Dict[str, Any], include_optional: bool = True) -> Any:
    if not schema:
        return {}
    if "example" in schema:
        return schema["example"]
    if "default" in schema:
        return schema["default"]
    if "enum" in schema and schema["enum"]:
        return schema["enum"][0]

    schema_type = schema.get("type", "object")
    if schema_type == "object":
        properties = schema.get("properties", {})
        required = set(schema.get("required", []))
        if isinstance(properties, list):
            return {name: "<value>" for name in properties}
        output = {}
        for name, value in properties.items():
            if include_optional or name in required:
                output[name] = build_example_from_schema(value, include_optional=include_optional)
        return output
    if schema_type == "array":
        return [build_example_from_schema(schema.get("items", {}), include_optional=include_optional)]
    if schema_type == "integer":
        return 0
    if schema_type == "number":
        return 0
    if schema_type == "boolean":
        return False
    if schema_type == "string":
        return "<value>"
    return {}


def format_parameter(document: Dict[str, Any], parameter: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if "$ref" in parameter:
        resolved = resolve_local_ref(document, str(parameter["$ref"]))
        if not isinstance(resolved, dict):
            return None
        parameter = resolved
    schema = normalize_schema(document, parameter.get("schema", {}))
    detail: Dict[str, Any] = {
        "name": str(parameter.get("name", "param")),
        "in": str(parameter.get("in", "query")),
        "required": bool(parameter.get("required")),
        "type": schema.get("type", "object"),
        "description": str(parameter.get("description", "")).strip(),
    }
    if "enum" in schema:
        detail["enum"] = schema["enum"]
    if "default" in schema:
        detail["default"] = schema["default"]
    return detail


def parameter_summary(parameter: Dict[str, Any]) -> str:
    required = "required" if parameter.get("required") else "optional"
    return f"{parameter['name']} {parameter['type']} ({parameter['in']}, {required})"


def extract_scopes(security_requirements: Any) -> List[str]:
    scopes: List[str] = []
    if not isinstance(security_requirements, list):
        return scopes
    for requirement in security_requirements:
        if not isinstance(requirement, dict):
            continue
        for values in requirement.values():
            if isinstance(values, list):
                scopes.extend(str(value) for value in values)
    return dedupe_preserve_order(scopes)


def extract_supported_modules(scopes: List[str]) -> List[str]:
    modules = []
    for scope in scopes:
        match = re.search(r"ZohoCRM\.modules\.([A-Za-z0-9_]+)\.", scope)
        if not match:
            continue
        name = match.group(1)
        if name.upper() in {"ALL", "READ", "CREATE", "UPDATE", "DELETE"}:
            continue
        modules.append(name)
    return dedupe_preserve_order(modules)


def make_unique_slug(candidate: str, existing: set[str], fallback: str) -> str:
    base = slugify(candidate) or slugify(fallback) or "endpoint"
    slug = base
    counter = 2
    while slug in existing:
        slug = f"{base}-{counter}"
        counter += 1
    existing.add(slug)
    return slug


def pick_content_entry(content: Any) -> tuple[Optional[str], Optional[Dict[str, Any]]]:
    if not isinstance(content, dict) or not content:
        return None, None
    for preferred in PREFERRED_CONTENT_TYPES:
        entry = content.get(preferred)
        if isinstance(entry, dict):
            return preferred, entry
    first_type = next(iter(content))
    first_entry = content[first_type]
    if isinstance(first_entry, dict):
        return str(first_type), first_entry
    return None, None


def extract_request_body(document: Dict[str, Any], operation: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    request_body = operation.get("requestBody")
    if isinstance(request_body, dict) and "$ref" in request_body:
        resolved = resolve_local_ref(document, str(request_body["$ref"]))
        if isinstance(resolved, dict):
            request_body = resolved
    if not isinstance(request_body, dict):
        return None

    content_type, entry = pick_content_entry(request_body.get("content"))
    return {
        "required": bool(request_body.get("required")),
        "description": str(request_body.get("description", "")).strip(),
        "content_type": content_type,
        "schema": simplify_schema(document, entry.get("schema", {}) if entry else {}),
    }


def extract_responses(document: Dict[str, Any], operation: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    responses = operation.get("responses", {})
    if not isinstance(responses, dict):
        return {}
    extracted: Dict[str, Dict[str, Any]] = {}
    for status_code, response in responses.items():
        if isinstance(response, dict) and "$ref" in response:
            resolved = resolve_local_ref(document, str(response["$ref"]))
            if isinstance(resolved, dict):
                response = resolved
        if not isinstance(response, dict):
            continue
        content_type, entry = pick_content_entry(response.get("content"))
        extracted[str(status_code)] = {
            "description": str(response.get("description", "")).strip(),
            "content_type": content_type,
            "schema": simplify_schema(document, entry.get("schema", {}) if entry else {}, max_depth=3),
        }
    return extracted


def dedupe_parameter_details(parameter_details: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    unique: List[Dict[str, Any]] = []
    seen = set()
    for detail in parameter_details:
        key = (detail.get("name"), detail.get("in"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(detail)
    return unique


def build_spec_from_openapi_sources(sources: List[str]) -> List[Endpoint]:
    endpoints: List[Endpoint] = []
    existing_slugs: set[str] = set()

    for source in sources:
        document = read_json_source(source)
        info = document.get("info", {})
        source_name = source_basename(source)
        section = str(info.get("title", Path(source_name).stem))

        servers = document.get("servers", [])
        server_url = ""
        if isinstance(servers, list) and servers:
            first_server = servers[0]
            if isinstance(first_server, dict):
                server_url = render_server_url(first_server)

        paths = document.get("paths", {})
        if not isinstance(paths, dict):
            continue

        for path, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            common_parameters = path_item.get("parameters", [])
            if not isinstance(common_parameters, list):
                common_parameters = []

            for method, operation in path_item.items():
                if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                    continue

                title = str(
                    operation.get("summary")
                    or operation.get("operationId")
                    or f"{method.upper()} {path}"
                )
                description = str(operation.get("description") or title)
                tags = operation.get("tags", [])
                normalized_tags = [str(tag) for tag in tags] if isinstance(tags, list) else []
                group = normalized_tags[0] if normalized_tags else section

                parameter_details = []
                for parameter in list(common_parameters) + list(operation.get("parameters", [])):
                    if not isinstance(parameter, dict):
                        continue
                    formatted = format_parameter(document, parameter)
                    if formatted:
                        parameter_details.append(formatted)

                parameter_details = dedupe_parameter_details(parameter_details)
                scopes = extract_scopes(operation.get("security"))
                request_url = ""
                if server_url:
                    request_url = server_url.rstrip("/") + str(path)

                slug = make_unique_slug(
                    str(operation.get("operationId") or title),
                    existing_slugs,
                    f"{method}-{path}",
                )
                endpoints.append(
                    Endpoint(
                        slug=slug,
                        title=title,
                        description=description,
                        section=section,
                        group=group,
                        url=source,
                        source_name=source_name,
                        source_kind="openapi",
                        method=method.upper(),
                        path=str(path),
                        request_url=request_url or None,
                        purpose=description,
                        scopes=scopes,
                        supported_modules=extract_supported_modules(scopes),
                        parameters=[parameter_summary(item) for item in parameter_details],
                        parameter_details=parameter_details,
                        request_body=extract_request_body(document, operation),
                        responses=extract_responses(document, operation),
                        tags=normalized_tags,
                    )
                )

    return endpoints


def postman_items(collection_item: Any, trail: List[str]) -> Iterable[tuple[List[str], Dict[str, Any]]]:
    if not isinstance(collection_item, dict):
        return
    if "request" in collection_item and isinstance(collection_item["request"], dict):
        yield trail, collection_item
    children = collection_item.get("item", [])
    if not isinstance(children, list):
        return
    next_trail = trail
    name = collection_item.get("name")
    if isinstance(name, str) and name:
        next_trail = trail + [name]
    for child in children:
        yield from postman_items(child, next_trail)


def build_spec_from_postman_sources(sources: List[str]) -> List[Endpoint]:
    endpoints: List[Endpoint] = []
    existing_slugs: set[str] = set()

    for source in sources:
        document = read_json_source(source)
        info = document.get("info", {})
        root_name = str(info.get("name", "Postman Collection"))
        source_name = source_basename(source)
        items = document.get("item", [])
        if not isinstance(items, list):
            continue

        for item in items:
            for trail, request_item in postman_items(item, []):
                request = request_item.get("request", {})
                if not isinstance(request, dict):
                    continue
                method = str(request.get("method", "GET")).upper()
                url_object = request.get("url", {})
                raw_url = ""
                path = ""
                parameter_details: List[Dict[str, Any]] = []

                if isinstance(url_object, str):
                    raw_url = url_object
                    path = urlparse(url_object).path
                elif isinstance(url_object, dict):
                    raw_url = str(url_object.get("raw", ""))
                    path_segments = url_object.get("path", [])
                    if isinstance(path_segments, list) and path_segments:
                        path = "/" + "/".join(str(part) for part in path_segments)
                    else:
                        path = urlparse(raw_url).path
                    query_items = url_object.get("query", [])
                    if isinstance(query_items, list):
                        for query_item in query_items:
                            if not isinstance(query_item, dict):
                                continue
                            parameter_details.append(
                                {
                                    "name": str(query_item.get("key", "param")),
                                    "in": "query",
                                    "required": False,
                                    "type": "string",
                                    "description": "",
                                }
                            )

                name = str(request_item.get("name", f"{method} {path}")).strip()
                description = request.get("description") or request_item.get("description") or name
                if isinstance(description, dict):
                    description = description.get("content", name)

                group = trail[-1] if trail else root_name
                slug = make_unique_slug(name, existing_slugs, f"{method}-{path}")
                endpoints.append(
                    Endpoint(
                        slug=slug,
                        title=name,
                        description=str(description),
                        section=root_name,
                        group=group,
                        url=source,
                        source_name=source_name,
                        source_kind="postman",
                        method=method,
                        path=path or None,
                        request_url=raw_url or None,
                        purpose=str(description),
                        parameters=[parameter_summary(item) for item in parameter_details],
                        parameter_details=parameter_details,
                    )
                )

    return endpoints


def build_spec(
    docs_url: str,
    catalog_url: Optional[str],
    with_details: bool,
    max_detail_pages: Optional[int] = None,
) -> List[Endpoint]:
    if catalog_url is None:
        catalog_url = urljoin(docs_url, DEFAULT_CATALOG_PAGE)

    catalog_html = fetch_text(catalog_url)
    catalog_links = extract_links(catalog_html, catalog_url)
    endpoints = parse_catalog(html_to_text(catalog_html), catalog_links)
    if with_details:
        enrich_endpoints(endpoints, max_detail_pages=max_detail_pages)
    return endpoints


def discover_openapi_sources_from_html(html: str, index_url: str) -> List[str]:
    parsed = urlparse(index_url)
    match = re.match(r"^/([^/]+)/([^/]+)/tree/([^/]+)/(.+)$", parsed.path)
    if parsed.netloc != "github.com" or not match:
        raise ValueError(f"Unsupported GitHub tree URL: {index_url}")

    owner, repo, branch, directory = match.groups()
    href_pattern = re.compile(
        rf'href="/{re.escape(owner)}/{re.escape(repo)}/blob/{re.escape(branch)}/({re.escape(directory)}/[^"#?]+\.json)"'
    )
    raw_urls = []
    for path in href_pattern.findall(html):
        raw_urls.append(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}")
    return sorted(dedupe_preserve_order(raw_urls))


def discover_openapi_sources(index_url: str = DEFAULT_ZOHO_OAS_INDEX_URL) -> List[str]:
    return discover_openapi_sources_from_html(fetch_text(index_url), index_url)


def render_catalog_markdown(endpoints: List[Endpoint]) -> str:
    grouped: Dict[str, Dict[str, List[Endpoint]]] = {}
    for endpoint in endpoints:
        grouped.setdefault(endpoint.section, {}).setdefault(endpoint.group, []).append(endpoint)

    lines = ["# Zoho CRM Endpoint Catalog", ""]
    for section, groups in grouped.items():
        lines.append(f"## {section}")
        lines.append("")
        for group, items in groups.items():
            lines.append(f"### {group}")
            lines.append("")
            for item in sorted(items, key=lambda candidate: candidate.title):
                method = item.method or "?"
                path = item.path or "(see source)"
                lines.append(f"- `{item.slug}`: {item.title}")
                lines.append(f"  {item.description}")
                lines.append(f"  `{method} {path}`")
                if item.scopes:
                    lines.append(f"  Scopes: {', '.join(item.scopes[:3])}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_workflow_reference(cli_name: str) -> str:
    return f"""# Zoho Agent Workflow

Use this toolkit when a coding agent needs the full Zoho CRM API surface without loading large MCP schemas into prompt context.

Recommended workflow:
1. Read the attached requirements file and extract the target modules, workflows, layouts, fields, and expected behaviors.
2. Search the local API index with `{cli_name} search <terms>`.
3. Inspect exact endpoint details with `{cli_name} show <slug>`.
4. Generate starter payloads with `{cli_name} template <slug> --kind request`.
5. Apply changes with `{cli_name} call <slug> ...`.
6. Verify with read-back calls or `{cli_name} verify <manifest.json>`.
7. Write manual test steps for the human operator after the automated checks pass.
"""


def render_skill(project_name: str, cli_name: str) -> str:
    return f"""---
name: {project_name}
description: Use for Zoho CRM buildout, configuration, and verification tasks. Search the local Zoho API index first, inspect the exact endpoint schema second, then apply and verify changes with the generic CLI.
---

Use this skill when a task involves large-scale Zoho CRM configuration or testing.

Workflow:
1. Read the attached requirements file or local spec file.
2. Search the local API index with `{cli_name} search <terms>`.
3. Inspect exact endpoint contracts with `{cli_name} show <slug>`.
4. Generate request templates with `{cli_name} template <slug> --kind request`.
5. Apply changes with `{cli_name} call <slug> ...`.
6. Verify with read-back calls or `{cli_name} verify <manifest.json>`.
7. Finish by writing clear manual test instructions for the user.

Important rules:
- Do not ask the user to locate API docs sections.
- Prefer the local `sources/openapi/` files and `spec/endpoints.json` over public docs.
- Use the generic CLI even for unfamiliar endpoint families; search and inspect first.
- Save repeatable payloads and verification manifests under `configs/` or `tests/`.

Common commands:
- `{cli_name} search "workflow transitions"`
- `{cli_name} show getrecords`
- `{cli_name} template createrecords --kind request`
- `{cli_name} call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `{cli_name} verify tests/zoho-smoke.json`

References:
- `references/catalog.md`
- `references/workflow.md`
- `spec/endpoints.json`
- `sources/openapi/`
"""


def render_openai_yaml(project_name: str) -> str:
    return f"""display_name: {project_name}
short_description: Zoho CRM full-surface toolkit backed by a local searchable API index and generic CLI.
default_prompt: Use the local Zoho API index and generic CLI to plan, apply, verify, and explain Zoho CRM configuration work.
"""


def render_cli() -> str:
    return local_template_text("zoho-crm-toolkit", "cli", "zoho-api")


def render_env_example() -> str:
    return local_template_text("zoho-crm-toolkit", ".env.example")


def render_verify_example() -> str:
    return local_template_text("zoho-crm-toolkit", "tests", "zoho-smoke.json")


def render_summary(project_name: str, endpoints: List[Endpoint], source_manifest: Dict[str, List[str]]) -> str:
    sections = sorted({endpoint.section for endpoint in endpoints})
    groups = sorted({endpoint.group for endpoint in endpoints})
    return f"""# {project_name}

This toolkit exposes the Zoho CRM API surface to a coding agent without loading huge MCP schemas into prompt context.

- Endpoints indexed: {len(endpoints)}
- Sections indexed: {len(sections)}
- Groups indexed: {len(groups)}
- OpenAPI source files vendored: {len(source_manifest.get('openapi', []))}
- Postman collections vendored: {len(source_manifest.get('postman', []))}

Primary commands:
- `./cli/zoho-api search "module workflow"`
- `./cli/zoho-api show getrecords`
- `./cli/zoho-api template createrecords --kind request`
- `./cli/zoho-api call getrecords --path-param module=Leads --query fields=Last_Name,Email`
- `./cli/zoho-api verify tests/zoho-smoke.json`
"""


def materialize_sources(
    output_dir: Path,
    *,
    openapi_sources: List[str],
    postman_sources: List[str],
) -> Dict[str, List[str]]:
    manifest = {"openapi": [], "postman": []}
    for source in openapi_sources:
        target = output_dir / "sources" / "openapi" / source_basename(source)
        write_file(target, read_text_source(source))
        manifest["openapi"].append(str(target.relative_to(output_dir)))
    for source in postman_sources:
        target = output_dir / "sources" / "postman" / source_basename(source)
        write_file(target, read_text_source(source))
        manifest["postman"].append(str(target.relative_to(output_dir)))
    return manifest


def render_scaffold(
    output_dir: Path,
    project_name: str,
    endpoints: List[Endpoint],
    *,
    source_manifest: Dict[str, List[str]],
) -> None:
    cli_name = "./cli/zoho-api"
    write_file(output_dir / "spec" / "endpoints.json", json.dumps([asdict(endpoint) for endpoint in endpoints], indent=2) + "\n")
    write_file(output_dir / "spec" / "sources.json", json.dumps(source_manifest, indent=2) + "\n")
    write_file(output_dir / "references" / "catalog.md", render_catalog_markdown(endpoints))
    write_file(output_dir / "references" / "workflow.md", render_workflow_reference(cli_name))
    write_file(output_dir / "skill" / "SKILL.md", render_skill(project_name, cli_name))
    write_file(output_dir / "skill" / "agents" / "openai.yaml", render_openai_yaml(project_name))
    write_file(output_dir / "cli" / "zoho-api", render_cli(), executable=True)
    write_file(output_dir / ".env.example", render_env_example())
    write_file(output_dir / "tests" / "zoho-smoke.json", render_verify_example())
    write_file(output_dir / "configs" / "modules" / ".gitkeep", "")
    write_file(output_dir / "configs" / "workflows" / ".gitkeep", "")
    write_file(output_dir / "SUMMARY.md", render_summary(project_name, endpoints, source_manifest))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a Zoho CRM toolkit with a local API index and generic CLI."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold = subparsers.add_parser("scaffold", help="Fetch specs and generate the toolkit.")
    scaffold.add_argument("--docs-url", help="Docs root or index URL for HTML fallback mode.")
    scaffold.add_argument("--catalog-url", help="Optional API catalog URL under the docs root.")
    scaffold.add_argument("--name", default="zoho-crm-toolkit", help="Project name for the generated skill metadata.")
    scaffold.add_argument("--output", required=True, help="Output directory.")
    scaffold.add_argument("--skip-details", action="store_true", help="Skip HTML detail page parsing.")
    scaffold.add_argument("--max-detail-pages", type=int, help="Optional limit for HTML detail page enrichment.")
    scaffold.add_argument(
        "--discover-openapi-index-url",
        default=DEFAULT_ZOHO_OAS_INDEX_URL,
        help="GitHub tree URL used to auto-discover Zoho OAS JSON files.",
    )
    scaffold.add_argument("--openapi-file", action="append", default=[], help="Local OpenAPI JSON file.")
    scaffold.add_argument("--openapi-url", action="append", default=[], help="Remote OpenAPI JSON URL.")
    scaffold.add_argument("--postman-file", action="append", default=[], help="Local Postman collection JSON file.")
    scaffold.add_argument("--postman-url", action="append", default=[], help="Remote Postman collection JSON URL.")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "scaffold":
        openapi_sources = list(args.openapi_file) + list(args.openapi_url)
        postman_sources = list(args.postman_file) + list(args.postman_url)

        if not openapi_sources and not postman_sources and not args.docs_url:
            openapi_sources = discover_openapi_sources(args.discover_openapi_index_url)

        if openapi_sources:
            endpoints = build_spec_from_openapi_sources(openapi_sources)
        elif postman_sources:
            endpoints = build_spec_from_postman_sources(postman_sources)
        else:
            if not args.docs_url:
                print(
                    "Provide --docs-url for HTML mode, pass OpenAPI/Postman sources, or rely on auto-discovery.",
                    file=sys.stderr,
                )
                return 1
            endpoints = build_spec(
                docs_url=args.docs_url,
                catalog_url=args.catalog_url,
                with_details=not args.skip_details,
                max_detail_pages=args.max_detail_pages,
            )

        if not endpoints:
            print("No endpoints were parsed from the supplied inputs.", file=sys.stderr)
            return 1

        output_dir = Path(args.output)
        source_manifest = materialize_sources(
            output_dir,
            openapi_sources=openapi_sources,
            postman_sources=postman_sources,
        )
        render_scaffold(output_dir, args.name, endpoints, source_manifest=source_manifest)
        print(f"Generated toolkit with {len(endpoints)} endpoints at {args.output}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
