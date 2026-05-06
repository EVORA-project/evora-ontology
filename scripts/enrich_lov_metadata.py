#!/usr/bin/env python3
"""Add LOV/FAIR-oriented metadata to the generated EVORAO Turtle ontology."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path


MARKER_START = "# BEGIN EVORAO LOV metadata enrichment"
MARKER_END = "# END EVORAO LOV metadata enrichment"

DEFAULT_ONTOLOGY_RESOURCE = "EVORAO:"
DEFAULT_DEFINED_BY_RESOURCE = "EVORAO:"
LEGACY_ONTOLOGY_RESOURCES = ("EVORAO:owl.ttl", "EVORAO:evorao.owl.ttl")

PREFIX_DECLARATIONS = {
    "bibo": "@prefix bibo: <http://purl.org/ontology/bibo/> .",
    "cc": "@prefix cc: <http://creativecommons.org/ns#> .",
    "vann": "@prefix vann: <http://purl.org/vocab/vann/> .",
    "voaf": "@prefix voaf: <http://purl.org/vocommons/voaf#> .",
    "vs": "@prefix vs: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .",
}

TERM_PATTERN = re.compile(
    r"^EVORAO:([A-Za-z][A-Za-z0-9_]*)\s+a\s+owl:"
    r"(?:Class|DatatypeProperty|ObjectProperty|AnnotationProperty)\s*;",
    re.MULTILINE,
)
SCHEMA_ELEMENT_SECTIONS = {"classes", "slots", "enums"}
DEPRECATION_FIELDS = {
    "deprecated",
    "deprecated_element_has_exact_replacement",
    "deprecated_element_has_possible_replacement",
}


def read_scalar(schema_text: str, key: str, default: str = "") -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", schema_text, re.MULTILINE)
    if not match:
        return default
    return match.group(1).strip().strip("\"'")


def read_description(schema_text: str, default: str = "") -> str:
    lines = schema_text.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue

        first = line.split(":", 1)[1].strip()
        parts = [first] if first else []
        for continuation in lines[index + 1 :]:
            if not continuation.startswith(" "):
                break
            parts.append(continuation.strip())
        return " ".join(part for part in parts if part)
    return default


def ttl_literal(value: str, lang: str | None = None) -> str:
    literal = json.dumps(value, ensure_ascii=True)
    if lang:
        return f"{literal}@{lang}"
    return literal


def clean_yaml_scalar(value: str) -> str:
    value = value.strip()
    if value in {"", "|", ">"}:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def yaml_field_value(
    lines: list[str],
    start: int,
    field_indent: int,
    element_indent: int,
) -> tuple[str | list[str], int]:
    line = lines[start]
    initial = line.split(":", 1)[1].strip()
    values: list[str] = []
    text_parts: list[str] = []

    if initial:
        text_parts.append(clean_yaml_scalar(initial))

    index = start + 1
    while index < len(lines):
        next_line = lines[index]
        stripped = next_line.strip()
        if not stripped:
            index += 1
            continue

        next_indent = line_indent(next_line)
        if next_indent <= element_indent:
            break
        if (
            next_indent == field_indent
            and not stripped.startswith("- ")
            and re.match(r"^[A-Za-z_][\w-]*:\s*", stripped)
        ):
            break

        if stripped.startswith("- "):
            values.append(clean_yaml_scalar(stripped[2:]))
        elif stripped:
            text_parts.append(clean_yaml_scalar(stripped))
        index += 1

    if values:
        return values, index
    return " ".join(part for part in text_parts if part), index


def schema_element_metadata(schema_text: str) -> dict[str, dict[str, str | list[str]]]:
    """Read LinkML element lifecycle metadata without requiring PyYAML at runtime."""
    metadata: dict[str, dict[str, str | list[str]]] = {}
    lines = schema_text.splitlines()
    section: str | None = None
    element: str | None = None
    element_indent = 0
    index = 0

    while index < len(lines):
        line = lines[index]
        top_level = re.match(r"^([A-Za-z][\w-]*):\s*$", line)
        if top_level:
            section_name = top_level.group(1)
            section = section_name if section_name in SCHEMA_ELEMENT_SECTIONS else None
            element = None
            index += 1
            continue

        if section:
            element_match = re.match(r"^  ([A-Za-z][A-Za-z0-9_]*)\s*:\s*$", line)
            if element_match:
                element = element_match.group(1)
                element_indent = 2
                metadata.setdefault(element, {})
                index += 1
                continue

            slot_usage_match = re.match(
                r"^      ([A-Za-z][A-Za-z0-9_]*)\s*:\s*$",
                line,
            )
            if slot_usage_match:
                element = slot_usage_match.group(1)
                element_indent = 6
                metadata.setdefault(element, {})
                index += 1
                continue

            field_match = re.match(r"^(\s+)([A-Za-z_][\w-]*):\s*", line)
            field_indent = len(field_match.group(1)) if field_match else 0
            field_name = field_match.group(2) if field_match else ""
            if (
                element
                and field_match
                and field_indent == element_indent + 2
                and field_name in DEPRECATION_FIELDS
            ):
                value, next_index = yaml_field_value(
                    lines,
                    index,
                    field_indent,
                    element_indent,
                )
                metadata.setdefault(element, {})[field_name] = value
                index = next_index
                continue

        index += 1

    return metadata


def rdf_resource(value: str) -> str:
    value = clean_yaml_scalar(value)
    if not value:
        return ""
    if value.startswith("<") and value.endswith(">"):
        return value
    if re.match(r"^https?://", value):
        return f"<{value}>"
    if ":" in value:
        return value
    return f"EVORAO:{value}"


def as_list(value: str | list[str] | None) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [item for item in value if item]
    return [value] if value else []


def validate_date(value: str, label: str) -> str:
    try:
        dt.date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"{label} must be an ISO date (YYYY-MM-DD), got {value!r}") from exc
    return value


def strip_existing_block(text: str) -> str:
    pattern = re.compile(
        rf"\n?{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}\n?",
        re.DOTALL,
    )
    return pattern.sub("\n", text).rstrip() + "\n"


def ensure_prefixes(text: str) -> str:
    existing = set(re.findall(r"^@prefix\s+([\w-]+):", text, re.MULTILINE))
    missing = [
        declaration
        for prefix, declaration in PREFIX_DECLARATIONS.items()
        if prefix not in existing
    ]
    if not missing:
        return text

    lines = text.splitlines()
    insert_at = 0
    while insert_at < len(lines) and lines[insert_at].startswith("@prefix "):
        insert_at += 1

    return "\n".join(lines[:insert_at] + missing + lines[insert_at:]) + "\n"


def normalize_ontology_resource(text: str, ontology_resource: str) -> str:
    resources = (*LEGACY_ONTOLOGY_RESOURCES, ontology_resource)
    for resource in resources:
        text = re.sub(
            rf"^{re.escape(resource)}\s+a\s+owl:Ontology\s*[,;]",
            f"{ontology_resource} a owl:Ontology ;",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def normalize_generated_metadata_values(text: str) -> str:
    return text.replace(
        'dct:license "https://creativecommons.org/publicdomain/zero/1.0/" ;',
        "dct:license <https://creativecommons.org/publicdomain/zero/1.0/> ;",
    )


def ontology_metadata_values(args: argparse.Namespace, schema_text: str) -> dict[str, object]:
    title = read_scalar(
        schema_text,
        "title",
        "European Viral Outbreak Response Alliance Ontology",
    )
    name = read_scalar(schema_text, "name", "EVORAO")
    version = read_scalar(schema_text, "version", "unreleased")
    description = read_description(
        schema_text,
        "The EVORAO Ontology provides a structured and harmonized vocabulary for "
        "describing shareable pathogens as biological materials.",
    )

    version_tag = version if version.startswith("v") else f"v{version}"
    current_release_url = f"{args.repository_url}/releases/tag/{version_tag}"
    prior_release_url = f"{args.repository_url}/releases/tag/{args.prior_release_tag}"
    citation = f"{title} ({name}) version {version}. {args.ontology_iri}"

    return {
        "title": title,
        "name": name,
        "version": version,
        "description": description,
        "current_release_url": current_release_url,
        "prior_release_url": prior_release_url,
        "citation": citation,
    }


def predicate_exists(block: str, predicate: str) -> bool:
    return re.search(rf"^\s*{re.escape(predicate)}\s+", block, re.MULTILINE) is not None


def replace_terminal_punctuation(line: str, new_punctuation: str) -> str:
    stripped = line.rstrip()
    if stripped.endswith((".", ";")):
        return f"{stripped[:-1]}{new_punctuation}"
    return f"{stripped}{new_punctuation}"


def ontology_statement_bounds(lines: list[str], ontology_resource: str) -> tuple[int, int]:
    start_pattern = re.compile(rf"^{re.escape(ontology_resource)}\s+a\s+owl:Ontology\b")
    start = next((index for index, line in enumerate(lines) if start_pattern.match(line)), None)
    if start is None:
        raise SystemExit(f"Could not find generated ontology statement for {ontology_resource}")

    for end in range(start, len(lines)):
        if lines[end].strip().endswith("."):
            return start, end

    raise SystemExit(f"Could not find end of ontology statement for {ontology_resource}")


def ontology_metadata_entries(args: argparse.Namespace, values: dict[str, object]) -> list[tuple[str, list[str]]]:
    description = str(values["description"])
    return [
        ("dct:identifier", [f"    dct:identifier {ttl_literal(args.ontology_iri)} ;"]),
        ("dct:description", [f"    dct:description {ttl_literal(description, 'en')} ;"]),
        ("dct:created", [f'    dct:created "{args.issued_date}"^^xsd:date ;']),
        ("dct:issued", [f'    dct:issued "{args.issued_date}"^^xsd:date ;']),
        ("dct:modified", [f'    dct:modified "{args.modified_date}"^^xsd:date ;']),
        ("owl:versionInfo", [f"    owl:versionInfo {ttl_literal(str(values['version']))} ;"]),
        ("owl:versionIRI", [f"    owl:versionIRI <{values['current_release_url']}> ;"]),
        ("owl:priorVersion", [f"    owl:priorVersion <{values['prior_release_url']}> ;"]),
        ("pav:previousVersion", [f"    pav:previousVersion <{values['prior_release_url']}> ;"]),
        ("dct:creator", ["    dct:creator <https://evora-project.eu/> ;"]),
        ("dct:publisher", ["    dct:publisher <https://evora-project.eu/> ;"]),
        ("cc:license", ["    cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;"]),
        (
            "dct:rights",
            [
                f"    dct:rights {ttl_literal('CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.', 'en')} ;",
            ],
        ),
        (
            "dct:accessRights",
            ["    dct:accessRights <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;"],
        ),
        ("vann:preferredNamespacePrefix", ['    vann:preferredNamespacePrefix "evorao" ;']),
        ("vann:preferredNamespaceUri", ['    vann:preferredNamespaceUri "https://w3id.org/evorao/" ;']),
        ("foaf:homepage", [f'    foaf:homepage "{args.docs_url}"^^xsd:anyURI ;']),
        ("dcat:landingPage", [f"    dcat:landingPage <{args.docs_url}> ;"]),
        ("dcat:downloadURL", [f"    dcat:downloadURL <{args.download_url}> ;"]),
        ("dct:format", ['    dct:format "text/turtle" ;']),
        (
            "dcat:distribution",
            [
                "    dcat:distribution [",
                "        a dcat:Distribution ;",
                f"        dcat:downloadURL <{args.download_url}> ;",
                '        dct:format "text/turtle"',
                "    ] ;",
            ],
        ),
        ("dct:bibliographicCitation", [f"    dct:bibliographicCitation {ttl_literal(str(values['citation']), 'en')} ;"]),
        ("dct:source", [f"    dct:source <{args.repository_url}> ;"]),
        ("prov:wasDerivedFrom", [f"    prov:wasDerivedFrom <{args.repository_url}> ;"]),
        ("bibo:status", ['    bibo:status "published" ;']),
        ("schema1:includedInDataCatalog", ["    schema1:includedInDataCatalog <https://www.ebi.ac.uk/ols4/> ;"]),
        (
            "rdfs:seeAlso",
            [
                f"    rdfs:seeAlso <{args.docs_url}>,",
                "        <https://www.ebi.ac.uk/ols4/ontologies/evorao>,",
                f"        <{args.repository_url}> ;",
            ],
        ),
    ]


def enrich_ontology_statement(text: str, args: argparse.Namespace, schema_text: str) -> str:
    values = ontology_metadata_values(args, schema_text)
    lines = text.splitlines()
    start, end = ontology_statement_bounds(lines, args.ontology_resource)

    continuation = start + 1
    while continuation <= end and lines[continuation].strip() in {
        "voaf:Vocabulary,",
        "schema1:DefinedTermSet ;",
    }:
        continuation += 1
    if continuation > start + 1:
        del lines[start + 1 : continuation]
        end -= continuation - (start + 1)

    type_lines = [
        f"{args.ontology_resource} a owl:Ontology,",
        "        voaf:Vocabulary,",
        "        schema1:DefinedTermSet ;",
    ]
    lines[start : start + 1] = type_lines
    end += len(type_lines) - 1

    block = "\n".join(lines[start : end + 1])
    additions: list[str] = []
    for predicate, entry_lines in ontology_metadata_entries(args, values):
        if entry_lines and not predicate_exists(block, predicate):
            additions.extend(entry_lines)

    if not additions:
        return "\n".join(lines) + "\n"

    lines[end] = replace_terminal_punctuation(lines[end], ";")
    additions[-1] = replace_terminal_punctuation(additions[-1], ".")
    lines[end + 1 : end + 1] = additions
    return "\n".join(lines) + "\n"


def term_metadata_block(ontology_text: str, schema_text: str, defined_by_resource: str) -> str:
    terms = sorted(set(TERM_PATTERN.findall(ontology_text)), key=lambda term: (term.lower(), term))
    if not terms:
        return ""

    lifecycle_metadata = schema_element_metadata(schema_text)
    lines = ["# Term provenance and status metadata."]
    for term in terms:
        term_lifecycle = lifecycle_metadata.get(term, {})
        deprecated = as_list(term_lifecycle.get("deprecated"))
        exact_replacements = as_list(
            term_lifecycle.get("deprecated_element_has_exact_replacement")
        )
        possible_replacements = as_list(
            term_lifecycle.get("deprecated_element_has_possible_replacement")
        )

        if deprecated:
            lines.append(f"EVORAO:{term} rdfs:isDefinedBy {defined_by_resource} ;")
            lines.append('    owl:deprecated "true"^^xsd:boolean ;')
            lines.append('    vs:term_status "deprecated" ;')
            lines.append(f"    skos:changeNote {ttl_literal(' '.join(deprecated), 'en')} ;")

            replacement_objects = [rdf_resource(value) for value in exact_replacements]
            replacement_objects = [value for value in replacement_objects if value]
            if replacement_objects:
                lines.append(
                    f"    dct:isReplacedBy {', '.join(replacement_objects)} ;"
                )

            related_replacements = [
                rdf_resource(value) for value in (*exact_replacements, *possible_replacements)
            ]
            related_replacements = [value for value in related_replacements if value]
            if related_replacements:
                lines.append(f"    rdfs:seeAlso {', '.join(related_replacements)} ;")

            lines[-1] = replace_terminal_punctuation(lines[-1], ".")
            lines.append("")
            continue

        lines.extend(
            [
                f"EVORAO:{term} rdfs:isDefinedBy {defined_by_resource} ;",
                '    vs:term_status "stable" .',
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def build_tail_block(args: argparse.Namespace, ontology_text: str, schema_text: str) -> str:
    term_block = term_metadata_block(ontology_text, schema_text, args.defined_by_resource)
    term_block = f"\n\n{term_block}" if term_block else ""

    return f"""{MARKER_START}
<https://evora-project.eu/> a foaf:Organization ;
    foaf:name "European Viral Outbreak Response Alliance" ;
    foaf:homepage "https://evora-project.eu/"^^xsd:anyURI ;
    schema1:url <https://evora-project.eu/> .{term_block}
{MARKER_END}
"""


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ontology",
        default="models/owl/evora_ontology.owl.ttl",
        help="Generated Turtle ontology to enrich.",
    )
    parser.add_argument(
        "--schema",
        default="models/evora_schema.yaml",
        help="Generated LinkML schema to read title/version metadata from.",
    )
    parser.add_argument(
        "--docs-url",
        default=os.environ.get(
            "EVORAO_DOCS_URL",
            "https://evora-project.github.io/evora-ontology/",
        ),
        help="Canonical HTML documentation URL.",
    )
    parser.add_argument(
        "--ontology-resource",
        default=os.environ.get("EVORAO_ONTOLOGY_RESOURCE", DEFAULT_ONTOLOGY_RESOURCE),
        help="Curie of the ontology resource to enrich in the generated Turtle.",
    )
    parser.add_argument(
        "--ontology-iri",
        default=os.environ.get("EVORAO_ONTOLOGY_IRI", "https://w3id.org/evorao/"),
        help="Canonical ontology/vocabulary IRI.",
    )
    parser.add_argument(
        "--defined-by-resource",
        default=os.environ.get("EVORAO_DEFINED_BY_RESOURCE", DEFAULT_DEFINED_BY_RESOURCE),
        help="Curie or IRI used as rdfs:isDefinedBy target for EVORAO terms.",
    )
    parser.add_argument(
        "--download-url",
        default=os.environ.get(
            "EVORAO_DOWNLOAD_URL",
            "https://raw.githubusercontent.com/EVORA-project/evora-ontology/main/models/owl/evora_ontology.owl.ttl",
        ),
        help="Canonical raw Turtle download URL.",
    )
    parser.add_argument(
        "--repository-url",
        default=os.environ.get(
            "EVORAO_REPOSITORY_URL",
            "https://github.com/EVORA-project/evora-ontology",
        ),
        help="GitHub repository URL.",
    )
    parser.add_argument(
        "--prior-release-tag",
        default=os.environ.get("EVORAO_PRIOR_RELEASE_TAG", "v1.1.0"),
        help="Previous GitHub release tag to expose through owl:priorVersion.",
    )
    parser.add_argument(
        "--issued-date",
        default=os.environ.get("EVORAO_ISSUED_DATE", "2024-12-12"),
        help="Initial public issue date for the vocabulary.",
    )
    parser.add_argument(
        "--modified-date",
        default=os.environ.get("EVORAO_MODIFIED_DATE", today),
        help="Current vocabulary modification date.",
    )
    args = parser.parse_args()
    args.issued_date = validate_date(args.issued_date, "issued-date")
    args.modified_date = validate_date(args.modified_date, "modified-date")
    return args


def main() -> None:
    args = parse_args()
    ontology_path = Path(args.ontology)
    schema_path = Path(args.schema)

    ontology_text = ontology_path.read_text(encoding="utf-8")
    schema_text = schema_path.read_text(encoding="utf-8")

    stripped = strip_existing_block(ontology_text)
    stripped = normalize_ontology_resource(stripped, args.ontology_resource)
    stripped = normalize_generated_metadata_values(stripped)
    stripped = ensure_prefixes(stripped)
    stripped = enrich_ontology_statement(stripped, args, schema_text)
    block = build_tail_block(args, stripped, schema_text)
    ontology_path.write_text(f"{stripped}\n{block}", encoding="utf-8")


if __name__ == "__main__":
    main()
