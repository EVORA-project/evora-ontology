# EVORAO deterministic QA

`qa/run_qa.sh` is the local and CI entrypoint for generated ontology quality checks. It requires Docker and runs the same tool images as the generation workflow.

The QA gate checks:

- ontology structure and metadata consistency in `models/owl/evora_ontology.owl.ttl`
- SPARQL competency questions against `qa/fixtures/valid_catalogue.ttl`
- SHACL validation with one valid fixture and one intentionally invalid fixture
- OWL reasoning with ROBOT/ELK on the ontology and on the ontology merged with the valid fixture
- a non-blocking ROBOT/JFact report for stricter OWL DL diagnostics

Reports are written to `qa/reports/`, which is ignored by Git. In CI, these reports are uploaded as workflow artifacts. If the QA gate fails, the workflow stops before committing generated files.

## Fixtures

The fixtures are synthetic examples declared as `owl:NamedIndividual` resources. They cover catalogue patterns used by EVORAO, including pathogen discovery, provider routing, collection context, biosafety information, access conditions, and licensing.

The live EVORA Portal exposes CC-BY-SA 4.0 catalogue data. If real portal records are added to the QA fixtures, their attribution and license must be documented with the fixture data.

When the schema changes, update the fixtures and expected SPARQL CSV outputs in the same pull request. The invalid fixture should remain invalid for one clear reason so the gate continues to test required metadata constraints.
