#!/usr/bin/env python3
"""Append LOV-oriented metadata to the generated EVORAO Turtle ontology."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path


MARKER_START = "# BEGIN EVORAO LOV metadata enrichment"
MARKER_END = "# END EVORAO LOV metadata enrichment"

TERM_PATTERN = re.compile(
    r"^EVORAO:([A-Za-z][A-Za-z0-9_]*)\s+a\s+owl:"
    r"(?:Class|DatatypeProperty|ObjectProperty|AnnotationProperty)\s*;",
    re.MULTILINE,
)


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


def read_keywords(schema_text: str) -> list[str]:
    lines = schema_text.splitlines()
    for index, line in enumerate(lines):
        if line != "keywords:":
            continue

        keywords: list[str] = []
        for continuation in lines[index + 1 :]:
            if not continuation.startswith("- "):
                break
            keywords.append(continuation[2:].strip().strip("\"'"))
        return keywords
    return []


def ttl_literal(value: str, lang: str | None = None) -> str:
    literal = json.dumps(value, ensure_ascii=True)
    if lang:
        return f"{literal}@{lang}"
    return literal


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


def term_metadata_block(ontology_text: str) -> str:
    terms = sorted(set(TERM_PATTERN.findall(ontology_text)), key=lambda term: (term.lower(), term))
    if not terms:
        return ""

    lines = ["# LOV term provenance and status metadata."]
    for term in terms:
        lines.extend(
            [
                f"EVORAO:{term} rdfs:isDefinedBy EVORAO: ;",
                '    vs:term_status "stable" .',
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def build_metadata_block(args: argparse.Namespace, schema_text: str, ontology_text: str) -> str:
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
    keywords = read_keywords(schema_text)

    version_tag = version if version.startswith("v") else f"v{version}"
    current_release_url = f"{args.repository_url}/releases/tag/{version_tag}"
    prior_release_url = f"{args.repository_url}/releases/tag/{args.prior_release_tag}"

    keyword_lines = ""
    if keywords:
        keyword_values = ",\n        ".join(ttl_literal(keyword, "en") for keyword in keywords)
        keyword_lines = f"    dcat:keyword {keyword_values} ;\n"

    term_block = term_metadata_block(ontology_text)
    term_block = f"\n\n{term_block}" if term_block else ""

    return f"""{MARKER_START}
@prefix cc: <http://creativecommons.org/ns#> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix voaf: <http://purl.org/vocommons/voaf#> .
@prefix vs: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .

EVORAO: a owl:Ontology,
        voaf:Vocabulary ;
    rdfs:label {ttl_literal(name, "en")} ;
    dct:title {ttl_literal(title, "en")} ;
    dct:description {ttl_literal(description, "en")} ;
    rdfs:comment {ttl_literal(description, "en")} ;
    dct:issued "{args.issued_date}"^^xsd:date ;
    dct:modified "{args.modified_date}"^^xsd:date ;
    owl:versionInfo {ttl_literal(version)} ;
    owl:versionIRI <{current_release_url}> ;
    owl:priorVersion <{prior_release_url}> ;
    pav:version {ttl_literal(version)} ;
    dct:creator <https://evora-project.eu/> ;
    dct:publisher <https://evora-project.eu/> ;
    dct:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
    cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
    dct:rights {ttl_literal("CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.", "en")} ;
    vann:preferredNamespacePrefix "evorao" ;
    vann:preferredNamespaceUri "https://w3id.org/evorao/" ;
    foaf:homepage <{args.docs_url}> ;
    dcat:landingPage <{args.docs_url}> ;
    dcat:downloadURL <{args.download_url}> ;
    rdfs:seeAlso <{args.docs_url}>,
        <https://www.ebi.ac.uk/ols4/ontologies/evorao>,
        <{args.repository_url}> ;
{keyword_lines}    skos:inScheme EVORAO: .

<https://evora-project.eu/> a foaf:Organization ;
    foaf:name "European Viral Outbreak Response Alliance" ;
    foaf:homepage <https://evora-project.eu/> .{term_block}
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
    block = build_metadata_block(args, schema_text, stripped)
    ontology_path.write_text(f"{stripped}\n{block}", encoding="utf-8")


if __name__ == "__main__":
    main()
