

# Slot: production cell line (productionCellLine) 


_The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study_





URI: [EVORAO:productionCellLine](https://w3id.org/evorao/productionCellLine)
Alias: productionCellLine

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [ProductionCellLine](ProductionCellLine.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:productionCellLine |
| native | EVORAO:productionCellLine |




## LinkML Source

<details>
```yaml
name: productionCellLine
description: The cell line used for the production or propagation of the pathogen,
  detailing the cellular environment employed in its cultivation and study
title: production cell line
from_schema: https://w3id.org/evorao/
rank: 1000
alias: productionCellLine
domain_of:
- Pathogen
range: ProductionCellLine
required: false
multivalued: true

```
</details>