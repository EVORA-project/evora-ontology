

# Slot: infectivity Test (infectivityTest) 


_The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism._





URI: [EVORAO:infectivityTest](https://w3id.org/evorao/infectivityTest)
Alias: infectivityTest

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:infectivityTest |
| native | EVORAO:infectivityTest |
| related | cido:0001195 |




## LinkML Source

<details>
```yaml
name: infectivityTest
description: The description of the completed infectivity test, providing details
  on the methods, conditions, and results of the test used to assess the pathogen's
  ability to infect a host organism.
title: infectivity Test
from_schema: https://w3id.org/evorao/
related_mappings:
- cido:0001195
rank: 1000
alias: infectivityTest
domain_of:
- Pathogen
range: string
required: false
multivalued: false

```
</details>