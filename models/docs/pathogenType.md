

# Slot: pathogen type (pathogenType) 


_Identification of the specific type of pathogen among the listed categories e.g. 'Virus','Viroid','Bacterium'..._





URI: [EVORAO:pathogenType](https://w3id.org/evorao/pathogenType)
Alias: pathogenType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation o... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:pathogenType |
| native | EVORAO:pathogenType |




## LinkML Source

<details>
```yaml
name: pathogenType
description: Identification of the specific type of pathogen among the listed categories
  e.g. 'Virus','Viroid','Bacterium'...
title: pathogen type
from_schema: https://w3id.org/evorao/
rank: 1000
alias: pathogenType
domain_of:
- PathogenIdentification
range: string
required: true
multivalued: false
equals_string_in:
- Virus
- Bacterium
- Fungus
- Protozoan
- Viroid
- Prion

```
</details>