

# Slot: collected before date (collectedBeforeDate) 


_Set to TRUE if a proxy date for the collection date is used._





URI: [EVORAO:collectedBeforeDate](https://w3id.org/evorao/collectedBeforeDate)
Alias: collectedBeforeDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:collectedBeforeDate |
| native | EVORAO:collectedBeforeDate |
| related | sepio:0000105, ro:0002089 |




## LinkML Source

<details>
```yaml
name: collectedBeforeDate
description: Set to TRUE if a proxy date for the collection date is used.
title: collected before date
from_schema: https://w3id.org/evorao/
related_mappings:
- sepio:0000105
- ro:0002089
rank: 1000
ifabsent: 'false'
alias: collectedBeforeDate
domain_of:
- NaturalPartOrigin
range: boolean
required: false
recommended: true
multivalued: false

```
</details>