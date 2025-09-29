

# Slot: specificity documented (specificityDocumented) 


_Boolean value indicating whether the specificity of the product has been formally documented_





URI: [EVORAO:specificityDocumented](https://w3id.org/evorao/specificityDocumented)
Alias: specificityDocumented

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:specificityDocumented |
| native | EVORAO:specificityDocumented |




## LinkML Source

<details>
```yaml
name: specificityDocumented
description: Boolean value indicating whether the specificity of the product has been
  formally documented
title: specificity documented
from_schema: https://w3id.org/evorao/
rank: 1000
alias: specificityDocumented
domain_of:
- Antibody
- DetectionKit
range: boolean
required: true
multivalued: false

```
</details>