

# Slot: transmission method (transmissionMethod) 


_The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread._





URI: [EVORAO:transmissionMethod](https://w3id.org/evorao/transmissionMethod)
Alias: transmissionMethod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [TransmissionMethod](TransmissionMethod.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:transmissionMethod |
| native | EVORAO:transmissionMethod |
| close | schema:transmissionMethod |




## LinkML Source

<details>
```yaml
name: transmissionMethod
description: The method or route through which the pathogen is transmitted from one
  host to another, detailing the mechanisms of infection spread.
title: transmission method
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:transmissionMethod
rank: 1000
alias: transmissionMethod
domain_of:
- Pathogen
range: TransmissionMethod
required: false
multivalued: true

```
</details>