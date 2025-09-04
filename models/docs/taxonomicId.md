

# Slot: taxonomic ID (taxonomicId) 


_The taxonomic identifier as a persistent identifier accross releases_





URI: [EVORAO:taxonomicId](https://w3id.org/evorao/taxonomicId)
Alias: taxonomicId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxonomicId |
| native | EVORAO:taxonomicId |
| exact | dwc:taxonID |
| broad | schema:identifier |




## LinkML Source

<details>
```yaml
name: taxonomicId
description: The taxonomic identifier as a persistent identifier accross releases
title: taxonomic ID
from_schema: https://w3id.org/evorao/
exact_mappings:
- dwc:taxonID
broad_mappings:
- schema:identifier
rank: 1000
alias: taxonomicId
domain_of:
- Taxon
range: string
required: true
multivalued: false

```
</details>