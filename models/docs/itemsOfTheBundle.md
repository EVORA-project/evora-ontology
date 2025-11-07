

# Slot: items of the bundle (itemsOfTheBundle) 


_Specifies the constituent products and/or services that are part of the bundle._





URI: [EVORAO:itemsOfTheBundle](https://w3id.org/evorao/itemsOfTheBundle)
Alias: itemsOfTheBundle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  yes  |







## Properties

* Range: [Product](Product.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:itemsOfTheBundle |
| native | EVORAO:itemsOfTheBundle |
| close | schema:includesObject |




## LinkML Source

<details>
```yaml
name: itemsOfTheBundle
description: Specifies the constituent products and/or services that are part of the
  bundle.
title: items of the bundle
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:includesObject
rank: 1000
alias: itemsOfTheBundle
domain_of:
- Bundle
range: Product
required: true
multivalued: true

```
</details>