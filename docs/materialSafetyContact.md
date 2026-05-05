

# Slot: material safety contact (materialSafetyContact) 


_The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product._





URI: [EVORAO:materialSafetyContact](https://w3id.org/evorao/materialSafetyContact)
Alias: materialSafetyContact


## Inheritance

* [contactPoint](contactPoint.md)
    * **materialSafetyContact**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialSafetyDataSheet](MaterialSafetyDataSheet.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... |  yes  |







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
| broad | schema:contactPoint |




## LinkML Source

<details>
```yaml
name: materialSafetyContact
description: The designated contact point responsible for providing information related
  to the safety, handling, and regulatory compliance of the biological product.
title: material safety contact
from_schema: https://w3id.org/evorao/
broad_mappings:
- schema:contactPoint
rank: 1000
is_a: contactPoint
alias: materialSafetyContact
domain_of:
- MaterialSafetyDataSheet
range: ContactPoint
required: true
recommended: true
multivalued: false

```
</details>