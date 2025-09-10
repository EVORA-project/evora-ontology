

# Slot: provided entity type (providedEntityType) 


_The identification of the entity type (Class) described by the response to the query_





URI: [EVORAO:providedEntityType](https://w3id.org/evorao/providedEntityType)
Alias: providedEntityType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Comments

* This property defines what the response is about, independent of its serialization. It should reference an ontology class such as EVORAO:Virus, EVORAO:Protein, etc

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:providedEntityType |
| native | EVORAO:providedEntityType |
| related | dcat:servesDataset |




## LinkML Source

<details>
```yaml
name: providedEntityType
description: The identification of the entity type (Class) described by the response
  to the query
title: provided entity type
comments:
- This property defines what the response is about, independent of its serialization.
  It should reference an ontology class such as EVORAO:Virus, EVORAO:Protein, etc
from_schema: https://w3id.org/evorao/
related_mappings:
- dcat:servesDataset
rank: 1000
alias: providedEntityType
domain_of:
- DataProvider
range: string
required: true
multivalued: true

```
</details>