

# Slot: before date (beforeDate) 


_Set to TRUE if a proxy date for the collection date is used_





URI: [EVORAO:beforeDate](https://w3id.org/evorao/beforeDate)
Alias: beforeDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:beforeDate |
| native | EVORAO:beforeDate |
| related | sepio:0000105, ro:0002089 |




## LinkML Source

<details>
```yaml
name: beforeDate
description: Set to TRUE if a proxy date for the collection date is used
title: before date
from_schema: https://w3id.org/evorao/
related_mappings:
- sepio:0000105
- ro:0002089
rank: 1000
ifabsent: 'false'
alias: beforeDate
domain_of:
- NaturalPartOrigin
range: boolean
required: true
multivalued: false

```
</details>