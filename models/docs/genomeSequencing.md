

# Slot: genome sequencing (genomeSequencing) 


_The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material_





URI: [EVORAO:genomeSequencing](https://w3id.org/evorao/genomeSequencing)
Alias: genomeSequencing

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:genomeSequencing |
| native | EVORAO:genomeSequencing |
| close | bao:0002788 |




## LinkML Source

<details>
```yaml
name: genomeSequencing
description: The extent of the pathogen's genetic material that has been sequenced,
  with possible values including 'Complete genome' for the entire genome, 'Complete
  coding sequence' for all coding regions, and 'Partial sequence' for only a portion
  of the genetic material
title: genome sequencing
from_schema: https://w3id.org/evorao/
close_mappings:
- bao:0002788
rank: 1000
alias: genomeSequencing
domain_of:
- Pathogen
range: string
required: true
multivalued: false
equals_string_in:
- Complete genome
- Complete coding sequence
- Partial sequence

```
</details>