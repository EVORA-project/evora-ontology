

# Slot: provided entity type (providedEntityType) 


_Identifies the type of entity (ontology class) described by the response to a query. Values should be expressed as IRIs (e.g., from an ontology)._





URI: [EVORAO:providedEntityType](https://w3id.org/evorao/providedEntityType)
Alias: providedEntityType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Uri](Uri.md)

* Multivalued: True

* Required: True





## Comments

* This property defines what the response is about, independent of its serialization. Values should be ontology class IRIs (e.g. https://w3id.org/evorao/Virus).

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:providedEntityType |
| native | EVORAO:providedEntityType |
| related | dcat:servesDataset |
| close | dct:type, schema:additionalType |




## LinkML Source

<details>
```yaml
name: providedEntityType
description: Identifies the type of entity (ontology class) described by the response
  to a query. Values should be expressed as IRIs (e.g., from an ontology).
title: provided entity type
comments:
- This property defines what the response is about, independent of its serialization.
  Values should be ontology class IRIs (e.g. https://w3id.org/evorao/Virus).
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:type
- schema:additionalType
related_mappings:
- dcat:servesDataset
rank: 1000
alias: providedEntityType
domain_of:
- DataProvider
range: uri
required: true
multivalued: true

```
</details>