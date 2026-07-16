# EVORAO deterministic QA

`qa/run_qa.sh` is the shared local and CI entrypoint for generated ontology quality checks. It expects Docker to be available and mounts the repository into the same images used by the workflow.

The gate currently performs:

- Structural checks on `models/owl/evora_ontology.owl.ttl`, including ontology IRI, namespace prefix/URI, version consistency, declaration counts, reused namespace counts, and mapping review.
- SPARQL competency queries over `qa/fixtures/valid_catalogue.ttl`, with expected CSV outputs committed next to each query.
- SHACL validation of a conforming fixture and an intentionally invalid fixture against `models/subsidiary_models/shacl/evora_schema.shacl.ttl`.
- OWL reasoning with ROBOT/ELK as the blocking gate, first on the ontology and then on the ontology merged with the valid fixture. The wrapper also records a non-blocking ROBOT/JFact DL explanation report so stricter OWL DL datatype/profile issues remain visible.

Reports are written to `qa/reports/` and are ignored by Git. The generation workflow uploads that directory as an artifact and stops before the generated commit/push step if the gate fails.

## Fixtures and competency questions

The fixture data are deliberately synthetic and are declared as `owl:NamedIndividual` resources. They exercise catalogue patterns that EVORAO users need in practice: resource discovery by pathogen, provider/request routing, collection context, biosafety information, and access/licensing conditions.

The live EVORA Portal API exposes CC-BY-SA 4.0 catalogue data and raw JSON-LD resources. If future tests use real portal records instead of synthetic fixtures, keep the CC-BY-SA attribution in the fixture metadata and test documentation.

When the schema evolves, update the fixture and expected CSV files in the same pull request as the vocabulary change. The invalid fixture should remain invalid for one clear reason so the gate proves that required metadata constraints are actually enforced.
