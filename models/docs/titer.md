

# Slot: titer (titer) 


_The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading_





URI: [EVORAO:titer](https://w3id.org/evorao/titer)
Alias: titer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:titer |
| native | EVORAO:titer |
| close | wd:Q2166189 |




## LinkML Source

<details>
```yaml
name: titer
description: The titer value, its corresponding unit, and the method of quantification
  (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present
  in the sample. The titer corresponds to the highest dilution factor that still yields
  a positive reading
title: titer
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q2166189
rank: 1000
alias: titer
domain_of:
- NucleicAcid
- Pathogen
range: string
required: true
multivalued: false

```
</details>