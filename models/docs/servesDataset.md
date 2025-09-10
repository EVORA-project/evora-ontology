

# Slot: serves dataset (servesDataset) 


_A collection of data that this data service can distribute_





URI: [dcat:servesDataset](http://www.w3.org/ns/dcat#servesDataset)
Alias: servesDataset

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |







## Properties

* Range: [Dataset](Dataset.md)

* Multivalued: True

* Recommended: True





## Comments

* This property rather intends to point towards Catalogues as collections of Datasets

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:servesDataset |
| native | EVORAO:servesDataset |




## LinkML Source

<details>
```yaml
name: servesDataset
description: A collection of data that this data service can distribute
title: serves dataset
comments:
- This property rather intends to point towards Catalogues as collections of Datasets
from_schema: https://w3id.org/evorao/
rank: 1000
slot_uri: dcat:servesDataset
alias: servesDataset
domain_of:
- DataService
range: Dataset
required: false
recommended: true
multivalued: true

```
</details>