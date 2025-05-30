

# Slot: collection item (collectionItem) 


_An item of the collection_





URI: [EVORAO:collectionItem](https://w3id.org/evorao/collectionItem)
Alias: collectionItem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Collection](Collection.md) | Set of products and services with some common characteristics |  yes  |







## Properties

* Range: [ProductOrService](ProductOrService.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:collectionItem |
| native | EVORAO:collectionItem |
| close | dcat:resource |




## LinkML Source

<details>
```yaml
name: collectionItem
description: An item of the collection
title: collection item
from_schema: https://w3id.org/evorao/
close_mappings:
- dcat:resource
rank: 1000
alias: collectionItem
domain_of:
- Collection
range: ProductOrService
required: false
recommended: true
multivalued: true

```
</details>