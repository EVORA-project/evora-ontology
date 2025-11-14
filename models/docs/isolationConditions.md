

# Slot: isolation conditions (isolationConditions) 


_The environmental and procedural conditions under which the pathogen was isolated._





URI: [EVORAO:isolationConditions](https://w3id.org/evorao/isolationConditions)
Alias: isolationConditions

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

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:isolationConditions |
| native | EVORAO:isolationConditions |




## LinkML Source

<details>
```yaml
name: isolationConditions
description: The environmental and procedural conditions under which the pathogen
  was isolated.
title: isolation conditions
from_schema: https://w3id.org/evorao/
rank: 1000
alias: isolationConditions
domain_of:
- Pathogen
range: string
required: false
multivalued: false

```
</details>