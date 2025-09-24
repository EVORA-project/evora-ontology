

# Slot: recombinant part identification (recombinantPartIdentification) 


_Identification of a recombinant part_





URI: [EVORAO:recombinantPartIdentification](https://w3id.org/evorao/recombinantPartIdentification)
Alias: recombinantPartIdentification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SyntheticPartOrigin](SyntheticPartOrigin.md) | Information on the origin of a synthetic part that composes the biological ma... |  no  |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  no  |
| [BiologicalPartOrigin](BiologicalPartOrigin.md) | Information on the origin of a unitary, cohesive part that is part of, or con... |  yes  |







## Properties

* Range: [RecombinantPartIdentification](RecombinantPartIdentification.md)





## Comments

* Information not required if the current biological part constitutes the complete biological material

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:recombinantPartIdentification |
| native | EVORAO:recombinantPartIdentification |




## LinkML Source

<details>
```yaml
name: recombinantPartIdentification
description: Identification of a recombinant part
title: recombinant part identification
comments:
- Information not required if the current biological part constitutes the complete
  biological material
from_schema: https://w3id.org/evorao/
rank: 1000
alias: recombinantPartIdentification
domain_of:
- BiologicalPartOrigin
range: RecombinantPartIdentification
required: false
multivalued: false

```
</details>