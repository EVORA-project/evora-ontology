

# Slot: production system (productionSystem) 


_The biological and technological methods and processes used to produce the antibody._





URI: [EVORAO:productionSystem](https://w3id.org/evorao/productionSystem)
Alias: productionSystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:productionSystem |
| native | EVORAO:productionSystem |




## LinkML Source

<details>
```yaml
name: productionSystem
description: The biological and technological methods and processes used to produce
  the antibody.
title: production system
from_schema: https://w3id.org/evorao/
rank: 1000
alias: productionSystem
domain_of:
- Antibody
range: string
required: false
recommended: true
multivalued: false

```
</details>