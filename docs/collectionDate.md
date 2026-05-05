

# Slot: collection date (collectionDate) 


_The date when the sample was collected in situ. If unknown/private, use a proxy date such as 'date received' and indicate this by setting to true the before date property._





URI: [EVORAO:collectionDate](https://w3id.org/evorao/collectionDate)
Alias: collectionDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:collectionDate |
| native | EVORAO:collectionDate |
| broad | dct:date |
| related | obib:0000714 |




## LinkML Source

<details>
```yaml
name: collectionDate
description: The date when the sample was collected in situ. If unknown/private, use
  a proxy date such as 'date received' and indicate this by setting to true the before
  date property.
title: collection date
from_schema: https://w3id.org/evorao/
related_mappings:
- obib:0000714
broad_mappings:
- dct:date
rank: 1000
alias: collectionDate
domain_of:
- NaturalPartOrigin
range: datetime
required: true
multivalued: false

```
</details>