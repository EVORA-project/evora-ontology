

# Slot: taxonomy (taxonomy) 


_The taxonomy release(s) in which this entity exists_





URI: [EVORAO:taxonomy](https://w3id.org/evorao/taxonomy)
Alias: taxonomy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  yes  |







## Properties

* Range: [Taxonomy](Taxonomy.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxonomy |
| native | EVORAO:taxonomy |




## LinkML Source

<details>
```yaml
name: taxonomy
description: The taxonomy release(s) in which this entity exists
title: taxonomy
from_schema: https://w3id.org/evorao/
rank: 1000
alias: taxonomy
domain_of:
- TaxonomicRank
- Taxon
range: Taxonomy
required: false
recommended: true
multivalued: true

```
</details>