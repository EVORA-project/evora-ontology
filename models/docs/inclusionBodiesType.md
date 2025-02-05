

# Slot: inclusion bodies type (inclusionBodiesType)


_Refers to the state of aggregated proteins within a cell. Possible values include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded' (proteins have been processed to regain their functional, active conformation)._





URI: [EVORAO:inclusionBodiesType](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#inclusionBodiesType)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:inclusionBodiesType |
| native | EVORAO:inclusionBodiesType |




## LinkML Source

<details>
```yaml
name: inclusionBodiesType
description: Refers to the state of aggregated proteins within a cell. Possible values
  include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded'
  (proteins have been processed to regain their functional, active conformation).
title: inclusion bodies type
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: inclusionBodiesType
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- Denatured
- Refolded

```
</details>