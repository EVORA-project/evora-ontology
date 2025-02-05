

# Slot: rank (rank)


_Relative level or position of the identified taxon in the taxonomy_





URI: [EVORAO:rank](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#rank)



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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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