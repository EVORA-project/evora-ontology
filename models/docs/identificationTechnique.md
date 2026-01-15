

# Slot: identification technique (identificationTechnique) 


_A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis._





URI: [EVORAO:identificationTechnique](https://w3id.org/evorao/identificationTechnique)
Alias: identificationTechnique

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:identificationTechnique |
| native | EVORAO:identificationTechnique |




## LinkML Source

<details>
```yaml
name: identificationTechnique
description: A method or procedure used to detect, identify, and confirm the presence
  of a specific nucleic acid sequence, pathogen, or associated constructs. This may
  involve various techniques such as PCR, sequencing, hybridization, or other molecular
  methods, utilizing specific tools and procedures for accurate detection and analysis.
title: identification technique
from_schema: https://w3id.org/evorao/
rank: 1000
alias: identificationTechnique
domain_of:
- NucleicAcid
- Pathogen
range: string
required: false
multivalued: false

```
</details>