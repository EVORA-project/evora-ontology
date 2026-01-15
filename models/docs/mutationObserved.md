

# Slot: mutation observed (mutationObserved) 


_Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it contains mutations (no frameshift, no unexpected STOP codon) if set to true._





URI: [EVORAO:mutationObserved](https://w3id.org/evorao/mutationObserved)
Alias: mutationObserved

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Recommended: True





## Comments

* Except for non-sequenced nucleic acids, for which mutations cannot be assessed, it is strongly recommended to determine whether any mutations are present in the provided sequenced nucleic acid.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:mutationObserved |
| native | EVORAO:mutationObserved |




## LinkML Source

<details>
```yaml
name: mutationObserved
description: Indicates if the current nucleic acid has No mutation compared to the
  reference sequence if the value is set to false or if it contains mutations (no
  frameshift, no unexpected STOP codon) if set to true.
title: mutation observed
comments:
- Except for non-sequenced nucleic acids, for which mutations cannot be assessed,
  it is strongly recommended to determine whether any mutations are present in the
  provided sequenced nucleic acid.
from_schema: https://w3id.org/evorao/
rank: 1000
alias: mutationObserved
domain_of:
- NucleicAcid
range: boolean
required: false
recommended: true
multivalued: false

```
</details>