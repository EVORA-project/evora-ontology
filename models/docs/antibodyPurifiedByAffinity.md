

# Slot: antibody purified by affinity (antibodyPurifiedByAffinity) 


_Indicates whether or not if the antibody was purified by affinity._





URI: [EVORAO:antibodyPurifiedByAffinity](https://w3id.org/evorao/antibodyPurifiedByAffinity)
Alias: antibodyPurifiedByAffinity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:antibodyPurifiedByAffinity |
| native | EVORAO:antibodyPurifiedByAffinity |




## LinkML Source

<details>
```yaml
name: antibodyPurifiedByAffinity
description: Indicates whether or not if the antibody was purified by affinity.
title: antibody purified by affinity
from_schema: https://w3id.org/evorao/
rank: 1000
alias: antibodyPurifiedByAffinity
domain_of:
- Antibody
range: boolean
required: true
multivalued: false

```
</details>