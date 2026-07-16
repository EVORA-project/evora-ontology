<img src="https://evora-project.eu/assets/images/logo/logo.svg" width="219" height="auto" alt="EVORA logo"/>

[![CI- Rebuild of EVORA ontology files when Google sheet metadata file is updated](https://github.com/EVORA-project/evora-ontology/actions/workflows/generate_schema_models.yml/badge.svg?branch=staging)](https://github.com/EVORA-project/evora-ontology/actions)


# The European Viral Outbreak Response Alliance Ontology (EVORAO)


The **EVORAO** Ontology provides a structured and harmonized vocabulary for describing shareable pathogens as characterized biological materials, along with their derived products and associated services, organized into collections. Developed within the EVORA project, it supports consistent metadata annotation across research infrastructures, promoting findability, accessibility, interoperability, and reusability (FAIR). By aligning with relevant standards and ontologies, EVORAO facilitates cross-domain collaboration, integration, and sharing of pathogenic resources and services to enhance pandemic preparedness and response. While initially focused on virology, EVORAO is designed to be extensible and also supports metadata harmonization for other pathogens.

**EVORAO** is compatible with [DCAT](https://www.w3.org/TR/vocab-dcat-3/), making it well-suited for efficiently cataloguing pathogen collections and related resources.

**EVORAO** results from a collaborative effort within the [EVORA project](https://evora-project.eu/), involving three research infrastructures: [EVA](https://www.european-virus-archive.com/), [ERINHA](https://erinha.eu/) and [ELIXIR](https://elixir-europe.org/).



## EVORAO Ontology file

The EVORAO ontology is available in **OWL Turtle** format in the [/models/owl](https://github.com/EVORA-project/evora-ontology/tree/main/models/owl) directory. The latest stable version can be accessed directly from the main branch of this repository, while the staging branch is used to simulate ontology generation before publication.

**Ontology / vocabulary IRI:** https://w3id.org/evorao/

**Namespace IRI (for classes/properties):** https://w3id.org/evorao/

**OWL Turtle serialization:** https://w3id.org/evorao/owl.ttl

**GitHub source file:** https://github.com/EVORA-project/evora-ontology/blob/main/models/owl/evora_ontology.owl.ttl

**Release archive:** https://github.com/EVORA-project/evora-ontology/releases

The ontology also declares publication metadata, including title, description, version, license, publisher, preferred namespace prefix/URI, documentation URL, prior release, download URL, and term status/provenance metadata.

For vocabulary registry submissions and metadata assessments, use the ontology / vocabulary IRI `https://w3id.org/evorao/`. The `/owl.ttl` URL is the concrete Turtle serialization.

The ontology can also be browsed using the [OLS (Ontology Lookup Service)](https://www.ebi.ac.uk/ols4/ontologies/evorao).


## Documentation

The documentation files for EVORAO can be found in the [/docs](https://github.com/EVORA-project/evora-ontology/tree/main/docs) directory and are intended to be published with GitHub Pages:

**HTML documentation:** https://evora-project.github.io/evora-ontology/

It provides detailed information for consumers and developers working with EVORAO metadata.

Start exploring via the [index file](https://github.com/EVORA-project/evora-ontology/blob/main/docs/index.md).

OLS remains a useful ontology browser, but the GitHub Pages documentation is the canonical human-readable documentation linked from the ontology metadata for vocabulary publication.


## EVORAO generation process

EVORAO is generated from a [Google Sheet](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI) using [schemasheets](https://github.com/linkml/schemasheets) and processed with [LinkML](https://github.com/linkml/linkml), which compiles the schema into multiple formats.

The generation workflow is tested on the `staging` branch. It regenerates the LinkML schema, OWL Turtle file, root `/docs` documentation, and subsidiary models. After OWL generation, the workflow adds publication metadata that is not emitted by the standard LinkML OWL generator.

Publication from `main` is handled separately: documentation is deployed to GitHub Pages, and a GitHub release is created from the schema version with the generated OWL Turtle and LinkML schema attached as release assets.


## EVORAO quality gate

The staging generation workflow runs a deterministic QA gate before committing or pushing generated artefacts. The same gate can be started locally with Docker using:

```bash
./qa/run_qa.sh
```

The gate validates the generated ontology structure, runs OWL reasoning with ROBOT/ELK, checks generated SHACL against positive and negative catalogue fixtures, executes SPARQL competency queries, and writes reports under `qa/reports/`. In CI these reports are uploaded as workflow artifacts and the generated commit is blocked when a deterministic check fails.



## Subsidiary data models

In addition to the core ontology, the repository includes subsidiary data models generated with [LinkML](https://github.com/linkml/linkml) from the [EVORAO LinkML schema](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml). These models can be found in the [/models/subsidiary_models](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models) directory and provide starting points for using EVORAO metadata in different technical environments:

- **Programming models**: Python ([Pydantic](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/pydantic), [Python classes](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/python), [SQLAlchemy](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sqlalchemy)), [Java](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/java), [Go](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/go)
- **Database structure**: [SQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sqlschema)
- **Serialization formats**: [JSON](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/jsonschema), [JSON-LD](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/jsonld), [RDF](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/rdf), [Protobuf](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/protobuf)
- **Validation models**: [SHACL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/shacl), [ShEx](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/shex)
- **Querying tools**: [SPARQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sparql), [GraphQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/graphql)
- **Spreadsheet template**: [Excel](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/excel)



These models facilitate integration of EVORAO metadata into diverse research workflows.

For a comprehensive overview, refer to the [Google Sheet document](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI), reviewed by scientists from the partner research infrastructures, and to its derived YAML-based LinkML schema ([/models/evora_schema.yaml](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml)).


## Reusing and Extending EVORAO Metadata

EVORAO is designed to be reused, extended, and adapted to evolving research needs. Reuse and extension can include:

1. **Contributing to EVORAO**: Community-driven contributions are encouraged when the proposed change remains within the scope of pandemic preparedness and response. Contributions can be proposed through GitHub issues or pull requests, as described in the contribution guidelines.

2. **Creating custom ontologies**: If a use case requires terms or structures beyond the current EVORAO scope, EVORAO can be imported and extended in a separate ontology.

3. **Mapping to EVORAO**: EVORAO terms can be referenced alongside other ontologies or vocabularies by declaring the EVORAO prefix and using the relevant EVORAO IRIs in mappings.

When importing, extending, or mapping to EVORAO, declare the EVORAO prefix:

```yaml
prefixes:
      EVORAO: https://w3id.org/evorao/
```

For guidance on extending EVORAO by contribution, please refer to the [contribution guidelines](https://github.com/EVORA-project/evora-ontology/blob/main/CONTRIBUTING.md).

## How to Contribute

**Scientists and developers** are welcome to contribute semantic improvements to EVORAO:

- By proposing new terms, relationships, and metadata refinements via GitHub issues.
- By suggesting revisions to parent classes or concepts for better domain coverage.


**Developers** are also invited to contribute technical improvements that affect how output files, data models, and documentation are generated:

- Improve the CI generation workflow in the [.github/](https://github.com/EVORA-project/evora-ontology/tree/main/.github/workflows) directory.
- Improve the Google Sheet triggering process in the [/GScript](https://github.com/EVORA-project/evora-ontology/tree/main/Gscript) directory.
- Improve this README or the contribution guidelines.
- Improve the generation of the LinkML schema ([/models/evora_schema.yaml](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml)) from the Google Sheet by contributing to the [schemasheets GitHub repository](https://github.com/linkml/schemasheets).
- Improve generated outputs such as OWL, JSON-LD, SQL, Python, Java, or Go by contributing to the [LinkML GitHub repository](https://github.com/linkml/linkml).

For guidance on extending EVORAO by contribution, please refer to the [contribution guidelines](https://github.com/EVORA-project/evora-ontology/blob/main/CONTRIBUTING.md).

## License

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

EVORAO is released under the **Creative Commons Universal (CC0 1.0)** license, ensuring unrestricted reuse and alignment with FAIR principles. This allows:

- Free use, modification, and integration into other projects.
- Promotion of broad adoption and interoperability within the scientific community.
  
A recommended best practice for extending or reusing EVORAO is to contribute to the ontology as a community member. If the project scope differs, EVORAO can be imported partially for specific use cases; see [Reusing and Extending EVORAO Metadata](#reusing-and-extending-evorao-metadata).

For more information about the EVORA project, visit [https://evora-project.eu](https://evora-project.eu).
