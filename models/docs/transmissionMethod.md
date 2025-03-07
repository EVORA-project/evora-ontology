

# Slot: transmission method (transmissionMethod)


_The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread._





URI: [EVORAO:transmissionMethod](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#transmissionMethod)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [TransmissionMethod](TransmissionMethod.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:transmissionMethod |
| native | EVORAO:transmissionMethod |




## LinkML Source

<details>
```yaml
name: transmissionMethod
description: The method or route through which the pathogen is transmitted from one
  host to another, detailing the mechanisms of infection spread.
title: transmission method
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: transmissionMethod
domain_of:
- Pathogen
range: TransmissionMethod
required: false
multivalued: true

```
</details>