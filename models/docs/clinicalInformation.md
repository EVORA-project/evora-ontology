

# Slot: clinical information (clinicalInformation) 


_Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes._





URI: [EVORAO:clinicalInformation](https://w3id.org/evorao/clinicalInformation)
Alias: clinicalInformation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:clinicalInformation |
| native | EVORAO:clinicalInformation |
| related | ncit:C25398 |




## LinkML Source

<details>
```yaml
name: clinicalInformation
description: Details about the clinical aspects of the pathogen, including symptoms,
  severity, treatment protocols, and patient outcomes.
title: clinical information
from_schema: https://w3id.org/evorao/
related_mappings:
- ncit:C25398
rank: 1000
alias: clinicalInformation
domain_of:
- Pathogen
range: string
required: false
multivalued: false

```
</details>