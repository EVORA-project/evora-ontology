

# Slot: reference label (referenceLabel) 


_The label informing what this reference is about_





URI: [EVORAO:referenceLabel](https://w3id.org/evorao/referenceLabel)
Alias: referenceLabel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve an item from an external provider |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* e.g., 'Infravec2 related product'

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:referenceLabel |
| native | EVORAO:referenceLabel |
| close | dct:title |




## LinkML Source

<details>
```yaml
name: referenceLabel
description: The label informing what this reference is about
title: reference label
comments:
- e.g., 'Infravec2 related product'
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:title
rank: 1000
alias: referenceLabel
domain_of:
- ExternalRelatedReference
range: string
required: true
multivalued: false

```
</details>