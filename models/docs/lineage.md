

# Slot: lineage (lineage) 


_An ordered list of textual taxon names representing the taxonomic lineage of the current taxon, normally from the highest known ancestor to the immediate parent. This property provides a flattened, display-oriented view of the lineage and does not replace the parentTaxon relation._





URI: [EVORAO:lineage](https://w3id.org/evorao/lineage)
Alias: lineage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Comments

* This property is intended for display, indexing, and search optimisation purposes. It represents a denormalised view of the taxonomic lineage and is typically derived automatically from successive parentTaxon relations. It MUST NOT be considered authoritative for taxonomic reasoning.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:lineage |
| native | EVORAO:lineage |




## LinkML Source

<details>
```yaml
name: lineage
description: An ordered list of textual taxon names representing the taxonomic lineage
  of the current taxon, normally from the highest known ancestor to the immediate
  parent. This property provides a flattened, display-oriented view of the lineage
  and does not replace the parentTaxon relation.
title: lineage
comments:
- This property is intended for display, indexing, and search optimisation purposes.
  It represents a denormalised view of the taxonomic lineage and is typically derived
  automatically from successive parentTaxon relations. It MUST NOT be considered authoritative
  for taxonomic reasoning.
from_schema: https://w3id.org/evorao/
rank: 1000
alias: lineage
domain_of:
- Taxon
range: string
required: false
multivalued: true

```
</details>