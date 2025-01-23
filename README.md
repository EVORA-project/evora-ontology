<img src="https://evora-project.eu/assets/images/logo/logo.svg" width="219" height="auto" alt="EVORA logo"/>

[![CI- Rebuild of EVORA ontology files when Google sheet metadata file is updated](https://github.com/EVORA-project/evora-ontology/actions/workflows/generate_schema_models.yml/badge.svg?branch=staging)](https://github.com/EVORA-project/evora-ontology/actions)

# The European Viral Outbreak Response Alliance Ontology: EVORAO 


The **EVORAO** harmonizes metadata in virology to describe viral resources, their derived products, and services. It aligns with FAIR principles to ensure interoperability, accessibility, and reusability across various projects. The EVORAO Ontology aims to support preparedness and response to pandemics.

The **EVORAO** is the result of a concerted approach from the [EVORA project](https://evora-project.eu/)'s three partner research infrastructures:  [EVA](https://www.european-virus-archive.com/), [ERINHA ](https://erinha.eu/) and [ELIXIR](https://elixir-europe.org/)

The generation of **EVORAO** is derived from a [Google Sheet](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI) using [schemasheets](https://github.com/linkml/schemasheets)



## OWL File of the EVORAO

The EVORAO ontology file is provided as an OWL Turtle format and is available in the [/models/owl](https://github.com/EVORA-project/evora-ontology/tree/main/models/owl) directory of this repository.
The current EVORAO namespace is the source OWL file of the main branch of this repository

https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#

The EVORAO can also be browsed from the [OLS (Ontology Lookup Service)](https://www.ebi.ac.uk/ols4)

## Documentation

The documentation for the EVORAO can be found at [https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/](https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/).

This documentation is aimed at consumers and developers of data and metadata in virology, for describing viral resources, their derived products, and services.

The EVORAO [index](https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/index.md) file is a good start for browsing this documentation.



## Subsidiary data models

Apart from the EVORAO ontology, this repository also provides different models of the EVORAO metadata that rely on a [LinkML](https://github.com/linkml/linkml) schema for their generation. They are available in the [/models/subsidiary_models](https://github.com/EVORA-project/evora-ontology/tree/main/models/subsidiary_models) directory and contain material to help start building a data model based on the EVORAO:

- excel
- go
- graphql
- java
- jsonld
- jsonschema
- prefixmap
- protobuf
- pydantic
- python
- rdf
- shacl
- shex
- sparql
- sqlalchemy
- sqlschema

  ## Extending EVORAO
  ... to be completed ... 
