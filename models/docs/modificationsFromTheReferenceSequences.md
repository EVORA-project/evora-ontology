

# Slot: modifications from the reference sequence(s) (modificationsFromTheReferenceSequences) 


_Set to TRUE if there was is any modification made from the reference sequence_





URI: [EVORAO:modificationsFromTheReferenceSequences](https://w3id.org/evorao/modificationsFromTheReferenceSequences)
Alias: modificationsFromTheReferenceSequences

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SyntheticPartOrigin](SyntheticPartOrigin.md) | Information on the origin of a synthetic part that composes the biological ma... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:modificationsFromTheReferenceSequences |
| native | EVORAO:modificationsFromTheReferenceSequences |
| related | geno:0000967 |




## LinkML Source

<details>
```yaml
name: modificationsFromTheReferenceSequences
description: Set to TRUE if there was is any modification made from the reference
  sequence
title: modifications from the reference sequence(s)
from_schema: https://w3id.org/evorao/
related_mappings:
- geno:0000967
rank: 1000
alias: modificationsFromTheReferenceSequences
domain_of:
- SyntheticPartOrigin
range: boolean
required: true
multivalued: false

```
</details>