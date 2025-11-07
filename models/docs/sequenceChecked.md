

# Slot: sequence checked (sequenceChecked) 


_Tell whether or not the sequence of the product was controlled (compulsory for cloned products)._





URI: [EVORAO:sequenceChecked](https://w3id.org/evorao/sequenceChecked)
Alias: sequenceChecked

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Comments

* Sequence check is mandatory for cloned products.

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
description: Tell whether or not the sequence of the product was controlled (compulsory
  for cloned products).
title: sequence checked
comments:
- Sequence check is mandatory for cloned products.
from_schema: https://w3id.org/evorao/
related_mappings:
- iceo:0000336
rank: 1000
alias: sequenceChecked
domain_of:
- NucleicAcid
range: boolean
required: true
multivalued: false

```
</details>