

# Slot: mutation observed (mutationObserved)


_Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it_

_ contains mutations (no frameshift, no unexpected STOP codon) if set to true_





URI: [EVORAO:mutationObserved](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#mutationObserved)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:mutationObserved |
| native | EVORAO:mutationObserved |




## LinkML Source

<details>
```yaml
name: mutationObserved
description: "Indicates if the current nucleic acid has No mutation compared to the\
  \ reference sequence if the value is set to false or if it\n contains mutations\
  \ (no frameshift, no unexpected STOP codon) if set to true"
title: mutation observed
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: mutationObserved
domain_of:
- Nucleic Acid
range: boolean
required: true
multivalued: false

```
</details>