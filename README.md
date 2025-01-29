<img src="https://evora-project.eu/assets/images/logo/logo.svg" width="219" height="auto" alt="EVORA logo"/>

[![CI- Rebuild of EVORA ontology files when Google sheet metadata file is updated](https://github.com/EVORA-project/evora-ontology/actions/workflows/generate_schema_models.yml/badge.svg?branch=staging)](https://github.com/EVORA-project/evora-ontology/actions)


# The European Viral Outbreak Response Alliance Ontology (EVORAO) 


The **EVORAO** harmonizes metadata in virology to describe viral resources, their derived products, and services. It aligns with FAIR principles to ensure interoperability, accessibility, and reusability across various projects. The EVORAO Ontology aims to support preparedness and response to pandemics.

EVORAO results from a collaborative effort within the [EVORA project](https://evora-project.eu/), comprising three research infrastructures:  [EVA](https://www.european-virus-archive.com/), [ERINHA ](https://erinha.eu/) and [ELIXIR](https://elixir-europe.org/)



## EVORAO Ontology File

The EVORAO ontology is available in **OWL Turtle** format in the [/models/owl](https://github.com/EVORA-project/evora-ontology/tree/main/models/owl) directory. The latest stable version can be accessed directly via the main branch of this rep, while other branches are used for development and staging purposes.
The URL address of this main branch source OWL file is also the current IRI of EVORAO, its namespace IRI ends with a #

**EVORAO IRI (Namespace)**: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#

The ontology can also be browsed using the [OLS (Ontology Lookup Service)](https://www.ebi.ac.uk/ols4)


## Documentation

The documentation files for the EVORAO can be found at [https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/](https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/).

It provides detailed information for consumers and developers working with EVORAO metadata.

Start exploring via the [index file](https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/index.md) 


## EVORAO generation process

EVORAO is generated from a [Google Sheet](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI) using [schemasheets](https://github.com/linkml/schemasheets) and processed with [Linkml](https://github.com/linkml/linkml) compiling the schema into multiple formats.


## Subsidiary data models

In addition to the core ontology, the repository includes subsidiary data models based on the [LinkML](https://github.com/linkml/linkml) tool for their generation, which provide interoperable data representations in various formats based on the corresponding [EVORAO LinkML schema](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml). These models can be found in the [/models/subsidiary_models](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models) directory and contain material to help start building a data model based on the EVORAO:

- **Programming models**: Python ([Pydantic](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/pydantic), [Python classes](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/python), [SQLAlchemy](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sqlalchemy)), [Java](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/java), [Go](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/go)
- **Database structure**: [SQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sqlschema)
- **Serialization formats**: [JSON](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/jsonschema), [JSON-LD](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/jsonld), [RDF](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/rdf), [Protobuf](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/protobuf)
- **Validation models**: [SHACL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/shacl), [ShEx](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/shex)
- **Querying tools**: [SPARQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/sparql), [GraphQL](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/graphql)
- **Spreadsheet template**: [Excel](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models/excel)



These models facilitate easy integration of EVORAO metadata into diverse research workflows.

For a comprehensive overview, refer to the [Google Sheet document](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI) that is reviewed by the scientist of our partner research infrastructures, and its derived YAML-based LinkML schema ([/models/evora_schema.yaml](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml)).


## Reusing and Extending EVORAO metadata

EVORAO is designed to be reused, extensible and adaptable to evolving research needs. Reuse and Extensions can include:

-1. **Contribute to EVORAO**: Is the way to be privileged if you intend to extend in the scope of preparedness and response, community-driven contributions are encouraged via pull requests for the development aspects, or via suggestion through github issues as explained in the contribution guidelines.

-2. **Create Custom Ontologies**: If your needs for new terms and structuration exceed the current scope, EVORAO can be imported, and additional terms added as required.

-3. **Mapping to EVORAO**: EVORAO terms can be referenced in conjunction with other ontologies or vocabularies(e.g. OBO, OLS) by adding EVORAO among your prefixes; then you can make reference to only specific EVORAO terms of interest and declare EVORAO IRIS in your mappings.

Therefore building uppon EVORAO by importing or mapping will makes you declare the EVORAO among your prefixes:
```YAML
prefixes:
      EVORAO: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
```

For guidance on extending EVORAO by contribution, please refer to the [contribution guidelines](https://github.com/EVORA-project/evora-ontology/blob/main/CONTRIBUTING.md).

## How to Contribute

**Scientists and developers** are welcome to contribute to the **semantic improvements** of the EVORAO
- By proposing new terms, relationships, and metadata refinements via GitHub issues.
- By suggesting restructuration of parent classes or concepts for better domain coverage.


**Developers** are also invited to contribute through **technical improvements** impacting the way our output files(data models, documentation ...) are generated by a standard pull request process
  -  For the CI generation workflow by suggesting improvements to the [.github/](https://github.com/EVORA-project/evora-ontology/tree/main/.github/workflows) directory of this repo
  -  For the CI triggering process from the google sheet by suggestion improvement the content of the [/GScript](https://github.com/EVORA-project/evora-ontology/tree/main/Gscript) directory
  -  For improving our this README and CONTRIBUTING description
  -  To improve how our LinkML schema ([/models/evora_schema.yaml](https://github.com/EVORA-project/evora-ontology/tree/main/models/evora_schema.yaml)) is generated from our Google Sheet of metadata, you can contribute directly through pull request on the corresponding [schemasheet github repository](https://github.com/linkml/schemasheets)
  -  To improve the other models outputs (OWL, JSON-LD, SQL, Python, Java, Go...) improvements can be made throught contributing to LinkML improvements y making a pull request on the corresponding [LinkML github repository](https://github.com/linkml/linkml)

For guidance on extending EVORAO by contribution, please refer to the [contribution guidelines](https://github.com/EVORA-project/evora-ontology/blob/main/CONTRIBUTING.md).

##  License

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)]([http://creativecommons.org/publicdomain/zero/1.0/](https://github.com/EVORA-project/evora-ontology/blob/main/LICENSE))

EVORAO is released under the **Creative Commons Universal (CC0 1.0)** license, ensuring unrestricted reuse and alignment with FAIR principles. This allows:

- Free use, modification, and integration into other projects.
- Promotion of broad adoption and interoperability within the scientific community.
  
A recommended best practice for extending or reusing EVORAO is to contribute to the ontology as a community member. If the project scope differs, EVORAO can be imported partially for specific use cases, see [## Reusing and Extending EVORAO metadata chapter](#reusing-and-extending-evorao-metadata)

##

For more information about the EVORA project, visit our website:[https://evora-project.eu](https://evora-project.eu).


