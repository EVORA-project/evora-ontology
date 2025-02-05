

# Slot: functional characterization (functionalCharacterization)


_The process of determining and describing the specific biological activities and roles of a protein. Possible values include 'Functionally characterized' (the protein's functions have been identified and described) and 'No functional characterization' (the protein's functions have not been identified or described)._





URI: [EVORAO:functionalCharacterization](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#functionalCharacterization)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:functionalCharacterization |
| native | EVORAO:functionalCharacterization |




## LinkML Source

<details>
```yaml
name: functionalCharacterization
description: The process of determining and describing the specific biological activities
  and roles of a protein. Possible values include 'Functionally characterized' (the
  protein's functions have been identified and described) and 'No functional characterization'
  (the protein's functions have not been identified or described).
title: functional characterization
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: functionalCharacterization
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- Functionally characterized
- No functional characterization

```
</details>