

# Slot: sequence (sequence) 


_The related sequence information from a sequence provider or in fasta format_





URI: [EVORAO:sequence](https://w3id.org/evorao/sequence)
Alias: sequence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [RecombinantPartIdentification](RecombinantPartIdentification.md) | Identification of a recombinant part |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [Sequence](Sequence.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequence |
| native | EVORAO:sequence |




## LinkML Source

<details>
```yaml
name: sequence
description: The related sequence information from a sequence provider or in fasta
  format
title: sequence
from_schema: https://w3id.org/evorao/
rank: 1000
alias: sequence
domain_of:
- RecombinantPartIdentification
- Protein
- NucleicAcid
- Pathogen
range: Sequence
required: true
recommended: true
multivalued: true

```
</details>