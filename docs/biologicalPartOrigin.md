

# Slot: biological part origin (biologicalPartOrigin) 


_Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved._





URI: [EVORAO:biologicalPartOrigin](https://w3id.org/evorao/biologicalPartOrigin)
Alias: biologicalPartOrigin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, compulsory for acces... |  yes  |







## Properties

* Range: [BiologicalPartOrigin](BiologicalPartOrigin.md)

* Multivalued: True

* Required: True





## Comments

* It can be multiple parts in case of a recombinant biological material.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biologicalPartOrigin |
| native | EVORAO:biologicalPartOrigin |
| related | schema:hasBioChemEntityPart |




## LinkML Source

<details>
```yaml
name: biologicalPartOrigin
description: Details the origin of one or more unitary parts that make up the biological
  material. In the case of recombinant biological material, multiple parts may be
  involved.
title: biological part origin
comments:
- It can be multiple parts in case of a recombinant biological material.
from_schema: https://w3id.org/evorao/
related_mappings:
- schema:hasBioChemEntityPart
rank: 1000
alias: biologicalPartOrigin
domain_of:
- BiologicalMaterialOrigin
range: BiologicalPartOrigin
required: true
multivalued: true

```
</details>