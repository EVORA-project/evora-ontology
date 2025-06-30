

# Slot: rank (rank) 


_Relative level or position of the identified taxon in the taxonomy_





URI: [EVORAO:rank](https://w3id.org/evorao/rank)
Alias: rank

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |
| [Taxonomy](Taxonomy.md) | Science of naming, defining and classifying organisms |  yes  |







## Properties

* Range: [TaxonomicRank](TaxonomicRank.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:rank |
| native | EVORAO:rank |
| exact | dwc:taxonRank |




## LinkML Source

<details>
```yaml
name: rank
description: Relative level or position of the identified taxon in the taxonomy
title: rank
from_schema: https://w3id.org/evorao/
exact_mappings:
- dwc:taxonRank
rank: 1000
alias: rank
domain_of:
- Taxonomy
- Taxon
range: TaxonomicRank
required: true
multivalued: false

```
</details>