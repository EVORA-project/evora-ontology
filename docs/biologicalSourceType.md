

# Slot: biological source type (biologicalSourceType) 


_Indicates whether the biological material includes any part originally collected from a natural source (true) or is composed exclusively of synthetic parts (false)._





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

* It makes sense that only recombinant biological materials can have a mixed material origin! Mixed origin (natural + synthetic) is represented by EVORAO:recombinantMaterial = true and EVORAO:biologicalSourceType = true, together with both EVORAO:NaturalPartOrigin and EVORAO:SyntheticPartOrigin instances linked via EVORAO:biologicalPartOrigin

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
description: Indicates whether the biological material includes any part originally
  collected from a natural source (true) or is composed exclusively of synthetic parts
  (false).
title: biological source type
comments:
- It makes sense that only recombinant biological materials can have a mixed material
  origin! Mixed origin (natural + synthetic) is represented by EVORAO:recombinantMaterial
  = true and EVORAO:biologicalSourceType = true, together with both EVORAO:NaturalPartOrigin
  and EVORAO:SyntheticPartOrigin instances linked via EVORAO:biologicalPartOrigin
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