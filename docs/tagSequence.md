

# Slot: tag sequence (tagSequence) 


_The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids._





URI: [EVORAO:tagSequence](https://w3id.org/evorao/tagSequence)
Alias: tagSequence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [TagSequence](TagSequence.md)

* Recommended: True





## Comments

* The tagSequence is strongly recommended for cloned nucleic acids and proteins but may be absent in certain cases, such as for some non-cloned nucleic acids.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:tagSequence |
| native | EVORAO:tagSequence |
| exact | bao:0002796 |




## LinkML Source

<details>
```yaml
name: tagSequence
description: The name of the DNA coding sequence or corresponding peptide/protein
  sequence fused to a sequence of interest, used to facilitate experimental operations
  such as purification, detection, localization, tracking, solubility enhancement,
  or selection. Applicable to both proteins and nucleic acids.
title: tag sequence
comments:
- The tagSequence is strongly recommended for cloned nucleic acids and proteins but
  may be absent in certain cases, such as for some non-cloned nucleic acids.
from_schema: https://w3id.org/evorao/
exact_mappings:
- bao:0002796
rank: 1000
alias: tagSequence
domain_of:
- Protein
- NucleicAcid
range: TagSequence
required: false
recommended: true
multivalued: false

```
</details>