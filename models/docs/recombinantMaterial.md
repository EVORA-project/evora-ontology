

# Slot: recombinant material (recombinantMaterial) 


_Indicates if this biological material is a recombinant biological material._





URI: [EVORAO:recombinantMaterial](https://w3id.org/evorao/recombinantMaterial)
Alias: recombinantMaterial

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, compulsory for acces... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:recombinantMaterial |
| native | EVORAO:recombinantMaterial |




## LinkML Source

<details>
```yaml
name: recombinantMaterial
description: Indicates if this biological material is a recombinant biological material.
title: recombinant material
from_schema: https://w3id.org/evorao/
rank: 1000
ifabsent: 'false'
alias: recombinantMaterial
domain_of:
- BiologicalMaterialOrigin
range: boolean
required: true
multivalued: false

```
</details>