

# Slot: sequence reference (sequenceReference) 


_A reference that permits to retrieve the sequence information from a sequence provider._





URI: [EVORAO:sequenceReference](https://w3id.org/evorao/sequenceReference)
Alias: sequenceReference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |
| [Sequence](Sequence.md) | A nucleic acid or protein sequence information |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |







## Properties

* Range: [SequenceReference](SequenceReference.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequenceReference |
| native | EVORAO:sequenceReference |




## LinkML Source

<details>
```yaml
name: sequenceReference
description: A reference that permits to retrieve the sequence information from a
  sequence provider.
title: sequence reference
from_schema: https://w3id.org/evorao/
rank: 1000
alias: sequenceReference
domain_of:
- Sequence
- Antibody
range: SequenceReference
required: false
recommended: true
multivalued: true

```
</details>