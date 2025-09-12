

# Slot: ROR iD (rorId) 


_The corresponding organization's persistent identifier from the Research Organization Registry (ROR)_





URI: [EVORAO:rorId](https://w3id.org/evorao/rorId)
Alias: rorId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  yes  |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI) |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:rorId |
| native | EVORAO:rorId |
| exact | wdp:P6782 |
| related | dwc:institutionCode |




## LinkML Source

<details>
```yaml
name: rorId
description: The corresponding organization's persistent identifier from the Research
  Organization Registry (ROR)
title: ROR iD
from_schema: https://w3id.org/evorao/
exact_mappings:
- wdp:P6782
related_mappings:
- dwc:institutionCode
rank: 1000
alias: rorId
domain_of:
- Organization
range: string
required: false
recommended: true
multivalued: false

```
</details>