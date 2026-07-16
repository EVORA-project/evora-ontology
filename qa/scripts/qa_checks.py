#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import DCAT, DCTERMS, OWL, SH, SKOS, XSD


ROOT = Path(".")
ONTOLOGY = ROOT / "models/owl/evora_ontology.owl.ttl"
SCHEMA = ROOT / "models/evora_schema.yaml"
SHACL = ROOT / "models/subsidiary_models/shacl/evora_schema.shacl.ttl"
REPORTS = ROOT / "qa/reports"
FIXTURES = ROOT / "qa/fixtures"
CQ_DIR = ROOT / "qa/competency_questions"

EVORAO = Namespace("https://w3id.org/evorao/")
VANN = Namespace("http://purl.org/vocab/vann/")
VOAF = Namespace("http://purl.org/vocommons/voaf#")
VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")

DECLARATION_TYPES = {
    OWL.Class: "classes",
    OWL.ObjectProperty: "object_properties",
    OWL.DatatypeProperty: "data_properties",
    OWL.AnnotationProperty: "annotation_properties",
}

MAPPING_PREDICATES = {
    SKOS.exactMatch,
    SKOS.closeMatch,
    SKOS.broadMatch,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
    OWL.equivalentClass,
    OWL.equivalentProperty,
}


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def ensure_reports() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)


def parse_graph(path: Path, fmt: str = "turtle") -> Graph:
    graph = Graph()
    graph.parse(path, format=fmt)
    return graph


def load_schema() -> dict:
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_name(uri: URIRef) -> str:
    value = str(uri)
    if "#" in value:
        return value.rsplit("#", 1)[1]
    return value.rstrip("/").rsplit("/", 1)[-1]


def namespace_of(uri: URIRef) -> str:
    value = str(uri)
    if "#" in value:
        return value.rsplit("#", 1)[0] + "#"
    return value.rstrip("/").rsplit("/", 1)[0] + "/"


def graph_values(graph: Graph, subject: URIRef, predicate: URIRef) -> list[str]:
    return [str(value) for value in graph.objects(subject, predicate)]


def structural() -> None:
    ensure_reports()
    graph = parse_graph(ONTOLOGY)
    schema = load_schema()
    errors: list[str] = []
    warnings: list[str] = []

    ontology_iri = URIRef(str(EVORAO))
    schema_version = str(schema.get("version", "")).strip()
    ontology_version = graph.value(ontology_iri, OWL.versionInfo)
    expected_version_iri = URIRef(
        f"https://github.com/EVORA-project/evora-ontology/releases/tag/v{schema_version.removeprefix('v')}"
    )

    if (ontology_iri, RDF.type, OWL.Ontology) not in graph:
        errors.append("Ontology resource https://w3id.org/evorao/ is not declared owl:Ontology.")
    if str(ontology_version or "") != schema_version:
        errors.append(f"Ontology versionInfo {ontology_version!r} does not match schema version {schema_version!r}.")
    if graph.value(ontology_iri, OWL.versionIRI) != expected_version_iri:
        errors.append(f"owl:versionIRI must be {expected_version_iri}.")
    prior_version = graph.value(ontology_iri, OWL.priorVersion)
    if not prior_version:
        errors.append("owl:priorVersion is missing.")
    elif prior_version == expected_version_iri:
        errors.append("owl:priorVersion must not point to the current release.")
    if graph.value(ontology_iri, VANN.preferredNamespacePrefix) != Literal("evorao"):
        errors.append('vann:preferredNamespacePrefix must be "evorao".')
    if graph.value(ontology_iri, VANN.preferredNamespaceUri) != Literal(str(EVORAO)):
        errors.append(f"vann:preferredNamespaceUri must be {EVORAO}.")

    imports = sorted(str(value) for value in graph.objects(ontology_iri, OWL.imports))
    named_individuals = sorted(str(subject) for subject in graph.subjects(RDF.type, OWL.NamedIndividual))

    declared: dict[str, list[str]] = {}
    for rdf_type, key in DECLARATION_TYPES.items():
        declared[key] = sorted(str(subject) for subject in graph.subjects(RDF.type, rdf_type))

    evorao_counts = {
        "classes": sum(uri.startswith(str(EVORAO)) for uri in declared["classes"]),
        "object_properties": sum(uri.startswith(str(EVORAO)) for uri in declared["object_properties"]),
        "data_properties": sum(uri.startswith(str(EVORAO)) for uri in declared["data_properties"]),
    }

    reused: dict[str, int] = defaultdict(int)
    for uris in declared.values():
        for uri in uris:
            if not uri.startswith(str(EVORAO)):
                reused[namespace_of(URIRef(uri))] += 1

    local_iris = [URIRef(uri) for uris in declared.values() for uri in uris if uri.startswith(str(EVORAO))]
    malformed = [str(uri) for uri in local_iris if re.search(r"\s|[<>{}|\\^`]", str(uri))]
    if malformed:
        errors.append(f"Malformed local IRIs found: {malformed[:10]}")

    declaration_membership: dict[str, list[str]] = defaultdict(list)
    for rdf_type, key in DECLARATION_TYPES.items():
        for subject in graph.subjects(RDF.type, rdf_type):
            declaration_membership[str(subject)].append(key)
    duplicate_declarations = {
        subject: sorted(types)
        for subject, types in declaration_membership.items()
        if len(set(types)) > 1
    }

    mapping_report = mapping_checks(graph, declaration_membership)
    if mapping_report["errors"]:
        errors.extend(mapping_report["errors"])
    warnings.extend(mapping_report["warnings"])

    metrics = {
        "version": schema_version,
        "assessed_file_path": str(ONTOLOGY),
        "sha256": sha256(ONTOLOGY),
        "total_declared_classes": len(declared["classes"]),
        "total_object_properties": len(declared["object_properties"]),
        "total_data_properties": len(declared["data_properties"]),
        "evorao_namespace_classes": evorao_counts["classes"],
        "evorao_namespace_object_properties": evorao_counts["object_properties"],
        "evorao_namespace_data_properties": evorao_counts["data_properties"],
        "externally_reused_declarations_by_namespace": dict(sorted(reused.items())),
        "explicitly_declared_named_individuals": named_individuals,
        "ontology_imports": imports,
        "duplicate_declarations": duplicate_declarations,
        "reasoning_status": "pending",
        "shacl_validation_status": "pending",
        "competency_query_status": "pending",
        "mapping_status": "pass" if not mapping_report["errors"] else "fail",
    }

    (REPORTS / "ontology-metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (REPORTS / "mapping-review.json").write_text(json.dumps(mapping_report, indent=2) + "\n", encoding="utf-8")
    (REPORTS / "structural-checks.json").write_text(
        json.dumps({"status": "fail" if errors else "pass", "errors": errors, "warnings": warnings}, indent=2) + "\n",
        encoding="utf-8",
    )

    if errors:
        fail("Structural QA failed; see qa/reports/structural-checks.json", 2)


def mapping_checks(graph: Graph, declarations: dict[str, list[str]]) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    mappings: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()

    declared_subjects = set(declarations)
    for predicate in MAPPING_PREDICATES:
        for subject, obj in graph.subject_objects(predicate):
            triple = (str(subject), str(predicate), str(obj))
            if triple in seen:
                warnings.append(f"Duplicate mapping: {triple}")
            seen.add(triple)
            if str(subject).startswith(str(EVORAO)) and str(subject) not in declared_subjects:
                errors.append(f"Mapping source term is not declared in ontology: {subject}")
            if isinstance(obj, URIRef):
                parsed = urlparse(str(obj))
                if not parsed.scheme:
                    errors.append(f"Mapping target is not an absolute IRI: {obj}")
            else:
                errors.append(f"Mapping target is not an IRI: {subject} {predicate} {obj}")
            if predicate in {SKOS.exactMatch, OWL.equivalentClass, OWL.equivalentProperty}:
                warnings.append(f"Review strong equivalence mapping: {subject} {predicate} {obj}")
            mappings.append({"source": str(subject), "predicate": str(predicate), "target": str(obj)})

    return {"status": "pass" if not errors else "fail", "errors": errors, "warnings": warnings, "mappings": mappings}


def competency() -> None:
    ensure_reports()
    graph = parse_graph(FIXTURES / "valid_catalogue.ttl")
    status: dict[str, dict] = {}
    errors: list[str] = []

    for query_path in sorted(CQ_DIR.glob("*.rq")):
        expected_path = query_path.with_suffix(".expected.csv")
        actual_path = REPORTS / f"{query_path.stem}.actual.csv"
        rows = []
        result = graph.query(query_path.read_text(encoding="utf-8"))
        headers = [str(var) for var in result.vars]
        for row in result:
            rows.append([str(value) for value in row])
        rows.sort()
        write_csv(actual_path, headers, rows)
        expected = expected_path.read_text(encoding="utf-8") if expected_path.exists() else ""
        actual = actual_path.read_text(encoding="utf-8")
        passed = actual == expected
        status[query_path.name] = {"status": "pass" if passed else "fail", "rows": len(rows)}
        if not passed:
            errors.append(f"{query_path.name} returned bindings different from {expected_path.name}")

    (REPORTS / "competency-queries.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    if errors:
        fail("Competency query QA failed: " + "; ".join(errors), 3)


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


def shacl_summary() -> None:
    valid_human = (REPORTS / "shacl-valid.txt").read_text(encoding="utf-8", errors="replace")
    invalid_human = (REPORTS / "shacl-invalid.txt").read_text(encoding="utf-8", errors="replace")
    valid_ok = "Conforms: True" in valid_human
    invalid_ok = "Conforms: False" in invalid_human and "Less than 1 values" in invalid_human
    summary = {
        "valid_fixture": "pass" if valid_ok else "fail",
        "invalid_fixture": "pass" if invalid_ok else "fail",
        "expected_invalid_constraint": "missing required dct:description on EVORAO:Collection",
    }
    (REPORTS / "shacl-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if not (valid_ok and invalid_ok):
        fail("SHACL fixture QA failed; see qa/reports/shacl-summary.json", 4)


def final_summary() -> None:
    structural_status = json.loads((REPORTS / "structural-checks.json").read_text(encoding="utf-8"))["status"]
    cq_statuses = json.loads((REPORTS / "competency-queries.json").read_text(encoding="utf-8"))
    shacl_status = json.loads((REPORTS / "shacl-summary.json").read_text(encoding="utf-8"))
    reasoning_status = json.loads((REPORTS / "reasoning.json").read_text(encoding="utf-8"))
    fixture_reasoning_path = REPORTS / "reasoning-fixture.json"
    fixture_reasoning_status = json.loads(fixture_reasoning_path.read_text(encoding="utf-8")) if fixture_reasoning_path.exists() else {"status": "not-run"}
    strict_reasoning_path = REPORTS / "reasoning-strict.json"
    strict_reasoning_status = json.loads(strict_reasoning_path.read_text(encoding="utf-8")) if strict_reasoning_path.exists() else {"status": "not-run"}
    metrics = json.loads((REPORTS / "ontology-metrics.json").read_text(encoding="utf-8"))
    metrics["reasoning_status"] = reasoning_status["status"]
    metrics["fixture_reasoning_status"] = fixture_reasoning_status["status"]
    metrics["strict_dl_reasoning_status"] = strict_reasoning_status["status"]
    metrics["shacl_validation_status"] = "pass" if all(value == "pass" for value in shacl_status.values() if value in {"pass", "fail"}) else "fail"
    metrics["competency_query_status"] = "pass" if all(item["status"] == "pass" for item in cq_statuses.values()) else "fail"
    (REPORTS / "ontology-metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# EVORAO QA summary",
        "",
        f"- Structural checks: {structural_status}",
        f"- Blocking ROBOT reasoning ({reasoning_status.get('reasoner', 'unknown')}): {reasoning_status['status']}",
        f"- Fixture ROBOT reasoning ({fixture_reasoning_status.get('reasoner', 'unknown')}): {fixture_reasoning_status['status']}",
        f"- Non-blocking ROBOT DL check ({strict_reasoning_status.get('reasoner', 'unknown')}): {strict_reasoning_status['status']}",
        f"- SHACL valid fixture: {shacl_status['valid_fixture']}",
        f"- SHACL invalid fixture: {shacl_status['invalid_fixture']}",
        f"- Competency queries: {metrics['competency_query_status']}",
        f"- Ontology version: {metrics['version']}",
        f"- Declared classes: {metrics['total_declared_classes']}",
        f"- Object properties: {metrics['total_object_properties']}",
        f"- Data properties: {metrics['total_data_properties']}",
    ]
    (REPORTS / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        fail("Usage: qa_checks.py structural|competency|shacl-summary|final-summary")
    command = sys.argv[1]
    if command == "structural":
        structural()
    elif command == "competency":
        competency()
    elif command == "shacl-summary":
        shacl_summary()
    elif command == "final-summary":
        final_summary()
    else:
        fail(f"Unknown QA command: {command}")


if __name__ == "__main__":
    main()
