

# Slot: protein tag (proteinTag) 


_A DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids_





URI: [EVORAO:proteinTag](https://w3id.org/evorao/proteinTag)
Alias: proteinTag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [ProteinTag](ProteinTag.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:proteinTag |
| native | EVORAO:proteinTag |




## LinkML Source

<details>
```yaml
name: proteinTag
description: A DNA coding sequence or corresponding peptide/protein sequence fused
  to a sequence of interest, used to facilitate experimental operations such as purification,
  detection, localization, tracking, solubility enhancement, or selection. Applicable
  to both proteins and nucleic acids
title: protein tag
from_schema: https://w3id.org/evorao/
rank: 1000
alias: proteinTag
domain_of:
- Protein
- NucleicAcid
range: ProteinTag
required: true
multivalued: false

```
</details>