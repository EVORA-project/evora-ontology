

# Slot: host type (hostType) 


_Indication of the possible host(s) for the identified pathogens among the listed main categories_





URI: [EVORAO:hostType](https://w3id.org/evorao/hostType)
Alias: hostType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation o... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:hostType |
| native | EVORAO:hostType |




## LinkML Source

<details>
```yaml
name: hostType
description: Indication of the possible host(s) for the identified pathogens among
  the listed main categories
title: host type
from_schema: https://w3id.org/evorao/
rank: 1000
alias: hostType
domain_of:
- PathogenIdentification
range: string
required: false
recommended: true
multivalued: true
equals_string_in:
- Animal
- Human
- Plant

```
</details>