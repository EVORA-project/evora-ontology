

# Slot: production cell line (productionCellLine)


_The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study_





URI: [EVORAO:productionCellLine](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#productionCellLine)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [ProductionCellLine](ProductionCellLine.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: productionCellLine
domain_of:
- Pathogen
range: ProductionCellLine
required: false
multivalued: true

```
</details>