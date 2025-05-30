

# Slot: biological source type (biologicalSourceType) 


_Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!_





URI: [EVORAO:biologicalSourceType](https://w3id.org/evorao/biologicalSourceType)
Alias: biologicalSourceType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, compulsory for acces... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Comments

* It makes sense that only recombinant biological materials can have a mixed material origin!

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biologicalSourceType |
| native | EVORAO:biologicalSourceType |




## LinkML Source

<details>
```yaml
name: biologicalSourceType
description: Defines if the current biological material is natural and was collected
  or if it is a synthetic biological material. It makes sense that only recombinant
  biological materials can have a mixed material origin!
title: biological source type
comments:
- It makes sense that only recombinant biological materials can have a mixed material
  origin!
from_schema: https://w3id.org/evorao/
rank: 1000
alias: biologicalSourceType
domain_of:
- BiologicalMaterialOrigin
range: boolean
required: true
multivalued: false

```
</details>