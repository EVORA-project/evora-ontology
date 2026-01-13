

# Slot: rank (rank) 


_Relative level or position of the identified taxon in the taxonomy._





URI: [EVORAO:rank](https://w3id.org/evorao/rank)
Alias: rank

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of bi... |  yes  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [TaxonomicRank](TaxonomicRank.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:rank |
| native | EVORAO:rank |
| exact | wdp:P105, wdp:P105 |
| related | taxrank:1000000, ncbitaxon:has_rank, taxrank:1000000, ncbitaxon:has_rank |
| close | dwc:taxonRank, schema:taxonRank, biolink:has_taxonomic_rank, dwc:taxonRank, schema:taxonRank, biolink:has_taxonomic_rank |




## LinkML Source

<details>
```yaml
name: rank
description: Relative level or position of the identified taxon in the taxonomy.
title: rank
from_schema: https://w3id.org/evorao/
exact_mappings:
- wdp:P105
- wdp:P105
close_mappings:
- dwc:taxonRank
- schema:taxonRank
- biolink:has_taxonomic_rank
- dwc:taxonRank
- schema:taxonRank
- biolink:has_taxonomic_rank
related_mappings:
- taxrank:1000000
- ncbitaxon:has_rank
- taxrank:1000000
- ncbitaxon:has_rank
rank: 1000
alias: rank
domain_of:
- Taxonomy
- Taxon
range: TaxonomicRank
required: false
recommended: true
multivalued: false

```
</details>