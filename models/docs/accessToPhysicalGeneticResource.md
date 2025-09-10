

# Slot: access to physical genetic resource (accessToPhysicalGeneticResource) 


_Indicate if the biological part was produced with access to a physical genetic resource_





URI: [EVORAO:accessToPhysicalGeneticResource](https://w3id.org/evorao/accessToPhysicalGeneticResource)
Alias: accessToPhysicalGeneticResource

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  no  |
| [BiologicalPartOrigin](BiologicalPartOrigin.md) | Information on the origin of a unitary, cohesive part that is part of, or con... |  yes  |
| [SyntheticPartOrigin](SyntheticPartOrigin.md) | Information on the origin of a synthetic part that composes the biological ma... |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:accessToPhysicalGeneticResource |
| native | EVORAO:accessToPhysicalGeneticResource |




## LinkML Source

<details>
```yaml
name: accessToPhysicalGeneticResource
description: Indicate if the biological part was produced with access to a physical
  genetic resource
title: access to physical genetic resource
from_schema: https://w3id.org/evorao/
rank: 1000
alias: accessToPhysicalGeneticResource
domain_of:
- BiologicalPartOrigin
range: boolean
required: true
multivalued: false

```
</details>