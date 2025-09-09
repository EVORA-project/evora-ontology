

# Slot: infectivity (infectivity) 


_Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature._





URI: [EVORAO:infectivity](https://w3id.org/evorao/infectivity)
Alias: infectivity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:infectivity |
| native | EVORAO:infectivity |




## LinkML Source

<details>
```yaml
name: infectivity
description: Indicates the ability of the pathogen to establish an infection in a
  host organism, with possible values detailing whether infectivity has been tested,
  quantified, or cannot be tested due to non-cultivable nature.
title: infectivity
from_schema: https://w3id.org/evorao/
rank: 1000
alias: infectivity
domain_of:
- Pathogen
range: string
required: true
multivalued: false
equals_string_in:
- Infectivity tested
- Infectivity tested and quantified
- Non cultivable sample, infectivity cannot be tested

```
</details>