

# Slot: suspected epidemiological origin (suspectedEpidemiologicalOrigin) 


_The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted._





URI: [EVORAO:suspectedEpidemiologicalOrigin](https://w3id.org/evorao/suspectedEpidemiologicalOrigin)
Alias: suspectedEpidemiologicalOrigin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [GeographicalOrigin](GeographicalOrigin.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:suspectedEpidemiologicalOrigin |
| native | EVORAO:suspectedEpidemiologicalOrigin |
| related | schema:countryOfOrigin, dct:spatial |




## LinkML Source

<details>
```yaml
name: suspectedEpidemiologicalOrigin
description: The potential geographical or environmental source from which the pathogen
  is believed to have originated or been transmitted.
title: suspected epidemiological origin
from_schema: https://w3id.org/evorao/
related_mappings:
- schema:countryOfOrigin
- dct:spatial
rank: 1000
alias: suspectedEpidemiologicalOrigin
domain_of:
- Pathogen
range: GeographicalOrigin
required: false
multivalued: true

```
</details>