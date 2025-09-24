

# Slot: biological material origin (biologicalMaterialOrigin) 


_Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol_





URI: [EVORAO:biologicalMaterialOrigin](https://w3id.org/evorao/biologicalMaterialOrigin)
Alias: biologicalMaterialOrigin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biologicalMaterialOrigin |
| native | EVORAO:biologicalMaterialOrigin |
| related | sepio:0000058 |




## LinkML Source

<details>
```yaml
name: biologicalMaterialOrigin
description: Information about the origin of the biological material, essential for
  access, utilization, and benefit-sharing of genetic resources in compliance with
  the Nagoya Protocol
title: biological material origin
from_schema: https://w3id.org/evorao/
related_mappings:
- sepio:0000058
rank: 1000
alias: biologicalMaterialOrigin
domain_of:
- Protein
- NucleicAcid
- Pathogen
range: BiologicalMaterialOrigin
required: true
multivalued: false

```
</details>