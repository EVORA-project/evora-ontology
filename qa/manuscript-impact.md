# QA and Release Impact Note

This QA gate makes the ontology release process more reproducible without changing the scientific scope of EVORAO. It adds deterministic checks that run after LinkML generation and metadata enrichment, and before generated artefacts are committed from CI.

Expected impact for releases:

- A generated release candidate must parse as RDF and remain structurally consistent with the LinkML schema version and EVORAO namespace policy.
- ROBOT/ELK must complete reasoning on the generated OWL file, giving an explicit OWL reasoner check before publication. A non-blocking ROBOT/JFact report is also preserved for stricter OWL DL profile review.
- SHACL fixtures verify that generated validation shapes accept a representative catalogue record and reject a record missing required metadata.
- SPARQL competency questions provide regression coverage for user-facing catalogue queries.
- QA reports are preserved as CI artifacts, making release checks easier to review in pull requests and manuscript/review material.

This is technical quality control. Vocabulary semantics still need domain review when labels, definitions, hierarchy, deprecation, or mappings change.
