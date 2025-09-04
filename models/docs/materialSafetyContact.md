

# Slot: material safety contact (materialSafetyContact) 


_The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product._





URI: [EVORAO:materialSafetyContact](https://w3id.org/evorao/materialSafetyContact)
Alias: materialSafetyContact

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MSDS](MSDS.md) |  |  yes  |







## Properties

* Range: [ContactPoint](ContactPoint.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:materialSafetyContact |
| native | EVORAO:materialSafetyContact |
| exact | dcat:contactPoint |




## LinkML Source

<details>
```yaml
name: materialSafetyContact
description: The designated contact point responsible for providing information related
  to the safety, handling, and regulatory compliance of the biological product.
title: material safety contact
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:contactPoint
rank: 1000
alias: materialSafetyContact
domain_of:
- MSDS
range: ContactPoint
required: true
multivalued: false

```
</details>