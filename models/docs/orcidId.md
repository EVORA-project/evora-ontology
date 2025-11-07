

# Slot: ORCID id (orcidId) 


_Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation._





URI: [EVORAO:orcidId](https://w3id.org/evorao/orcidId)
Alias: orcidId


## Inheritance

* [identifier](identifier.md)
    * **orcidId**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |
| [Person](Person.md) | An individual |  yes  |







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
| self | EVORAO:orcidId |
| native | EVORAO:orcidId |
| exact | wdp:P496, reproduceme:ORCID, wdp:P496, reproduceme:ORCID |
| related | iao:0000708, edam:4022, iao:0000708, edam:4022 |




## LinkML Source

<details>
```yaml
name: orcidId
description: Unique persistent identifier for a person, provided by the Open Researcher
  and Contributor ID (ORCID) organisation.
title: ORCID id
from_schema: https://w3id.org/evorao/
exact_mappings:
- wdp:P496
- reproduceme:ORCID
- wdp:P496
- reproduceme:ORCID
related_mappings:
- iao:0000708
- edam:4022
- iao:0000708
- edam:4022
rank: 1000
is_a: identifier
alias: orcidId
domain_of:
- Person
- ContactPoint
range: string
required: false
recommended: true
multivalued: true

```
</details>