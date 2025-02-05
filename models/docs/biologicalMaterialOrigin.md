

# Slot: Biological Material origin (biologicalMaterialOrigin)


_Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol_





URI: [EVORAO:biologicalMaterialOrigin](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#biologicalMaterialOrigin)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biologicalMaterialOrigin |
| native | EVORAO:biologicalMaterialOrigin |




## LinkML Source

<details>
```yaml
name: biologicalMaterialOrigin
description: Information about the origin of the biological material, essential for
  access, utilization, and benefit-sharing of genetic resources in compliance with
  the Nagoya Protocol
title: Biological Material origin
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: biologicalMaterialOrigin
domain_of:
- Protein
- Nucleic Acid
- Pathogen
range: BiologicalMaterialOrigin
required: true
multivalued: false

```
</details>