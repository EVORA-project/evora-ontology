

# Slot: regulatory information (regulatoryInformation) 


_Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations._





URI: [EVORAO:regulatoryInformation](https://w3id.org/evorao/regulatoryInformation)
Alias: regulatoryInformation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialSafetyDataSheet](MaterialSafetyDataSheet.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:regulatoryInformation |
| native | EVORAO:regulatoryInformation |
| related | rdfs:seeAlso |




## LinkML Source

<details>
```yaml
name: regulatoryInformation
description: Lists applicable laws, regulations, and standards governing the product,
  including local, national, or international requirements for its handling, use,
  transportation, and disposal, ensuring compliance with legal obligations.
title: regulatory information
from_schema: https://w3id.org/evorao/
related_mappings:
- rdfs:seeAlso
rank: 1000
alias: regulatoryInformation
domain_of:
- MaterialSafetyDataSheet
range: string
required: false
recommended: true
multivalued: false

```
</details>