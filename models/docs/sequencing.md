

# Slot: sequencing (sequencing) 


_Refers to the level of sequencing performed on the nucleic acid. Possible values include 'Not sequenced' (no sequencing has been performed), 'Partly sequenced' (only a portion of the nucleic acid sequence has been determined), and 'Fully sequenced' (the entire nucleic acid sequence has been determined)._





URI: [EVORAO:sequencing](https://w3id.org/evorao/sequencing)
Alias: sequencing

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* Cloned products have to be sequenced

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequencing |
| native | EVORAO:sequencing |




## LinkML Source

<details>
```yaml
name: sequencing
description: Refers to the level of sequencing performed on the nucleic acid. Possible
  values include 'Not sequenced' (no sequencing has been performed), 'Partly sequenced'
  (only a portion of the nucleic acid sequence has been determined), and 'Fully sequenced'
  (the entire nucleic acid sequence has been determined).
title: sequencing
comments:
- Cloned products have to be sequenced
from_schema: https://w3id.org/evorao/
rank: 1000
alias: sequencing
domain_of:
- NucleicAcid
range: string
required: true
multivalued: false
equals_string_in:
- Not sequenced
- Partly sequenced
- Fully sequenced

```
</details>