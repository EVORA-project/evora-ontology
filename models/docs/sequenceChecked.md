

# Slot: sequence checked (sequenceChecked) 


_Tell whether or not the sequence of the product was controlled, which is expected for sequenced nucleic acids and especially important for cloned ones._





URI: [EVORAO:sequenceChecked](https://w3id.org/evorao/sequenceChecked)
Alias: sequenceChecked

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Recommended: True





## Comments

* For non-sequenced nucleic acids, the sequenceChecked value cannot be assessed. In all other cases, it is strongly recommended to indicate whether the sequence verification has been performed or not. For cloned products in particular, providing this information is especially meaningful, as sequence verification is a key element in confirming the integrity of the cloned construct and is therefore expected to be documented whenever available.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequenceChecked |
| native | EVORAO:sequenceChecked |
| related | iceo:0000336 |




## LinkML Source

<details>
```yaml
name: sequenceChecked
description: Tell whether or not the sequence of the product was controlled, which
  is expected for sequenced nucleic acids and especially important for cloned ones.
title: sequence checked
comments:
- For non-sequenced nucleic acids, the sequenceChecked value cannot be assessed. In
  all other cases, it is strongly recommended to indicate whether the sequence verification
  has been performed or not. For cloned products in particular, providing this information
  is especially meaningful, as sequence verification is a key element in confirming
  the integrity of the cloned construct and is therefore expected to be documented
  whenever available.
from_schema: https://w3id.org/evorao/
related_mappings:
- iceo:0000336
rank: 1000
alias: sequenceChecked
domain_of:
- NucleicAcid
range: boolean
required: false
recommended: true
multivalued: false

```
</details>