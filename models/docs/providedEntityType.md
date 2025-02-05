

# Slot: provided entity type (providedEntityType)


_The identification of the entity type (Class) described by the response to the query_





URI: [EVORAO:providedEntityType](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#providedEntityType)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Dataset](Dataset.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:providedEntityType |
| native | EVORAO:providedEntityType |
| exact | dcat:servesDataset |




## LinkML Source

<details>
```yaml
name: providedEntityType
description: The identification of the entity type (Class) described by the response
  to the query
title: provided entity type
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:servesDataset
rank: 1000
alias: providedEntityType
domain_of:
- DataProvider
range: Dataset
required: true
multivalued: false

```
</details>