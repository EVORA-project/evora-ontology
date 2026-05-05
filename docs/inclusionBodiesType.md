

# Slot: inclusion bodies type (inclusionBodiesType) 


_Refers to the state of aggregated proteins within a cell. Possible values include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded' (proteins have been processed to regain their functional, active conformation)._





URI: [EVORAO:inclusionBodiesType](https://w3id.org/evorao/inclusionBodiesType)
Alias: inclusionBodiesType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




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
from_schema: https://w3id.org/evorao/
rank: 1000
alias: inclusionBodiesType
domain_of:
- Protein
range: string
required: false
multivalued: false
equals_string_in:
- Denatured
- Refolded

```
</details>