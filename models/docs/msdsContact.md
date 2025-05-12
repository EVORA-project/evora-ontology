

# Slot: MSDS contact (msdsContact) 


_The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product._





URI: [EVORAO:msdsContact](https://w3id.org/evorao/msdsContact)
Alias: msdsContact

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MSDS](MSDS.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... |  yes  |







## Properties

* Range: [ContactPoint](ContactPoint.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:msdsContact |
| native | EVORAO:msdsContact |
| exact | dcat:contactPoint |




## LinkML Source

<details>
```yaml
name: msdsContact
description: The designated contact point responsible for providing information related
  to the safety, handling, and regulatory compliance of the biological product.
title: MSDS contact
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:contactPoint
rank: 1000
alias: msdsContact
domain_of:
- MSDS
range: ContactPoint
required: true
multivalued: false

```
</details>