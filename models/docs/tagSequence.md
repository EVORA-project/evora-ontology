

# Slot: tag sequence (tagSequence) 


_The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids._





URI: [EVORAO:tagSequence](https://w3id.org/evorao/tagSequence)
Alias: tagSequence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [TagSequence](TagSequence.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:tagSequence |
| native | EVORAO:tagSequence |
| exact | bao:0002796, bao:0002796 |




## LinkML Source

<details>
```yaml
name: tagSequence
description: The name of the DNA coding sequence or corresponding peptide/protein
  sequence fused to a sequence of interest, used to facilitate experimental operations
  such as purification, detection, localization, tracking, solubility enhancement,
  or selection. Applicable to both proteins and nucleic acids.
title: tag sequence
from_schema: https://w3id.org/evorao/
exact_mappings:
- bao:0002796
- bao:0002796
rank: 1000
alias: tagSequence
domain_of:
- Protein
- NucleicAcid
range: TagSequence
required: true
multivalued: false

```
</details>