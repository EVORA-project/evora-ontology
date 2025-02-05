

# Slot: type of functional Characterization (typeOfFunctionalCharacterization)


_Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include 'Enzymatic' (the protein has been characterized for its enzyme activity) and 'Antigenic' (the protein has been characterized for its ability to elicit an immune response)._





URI: [EVORAO:typeOfFunctionalCharacterization](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#typeOfFunctionalCharacterization)



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
| self | EVORAO:typeOfFunctionalCharacterization |
| native | EVORAO:typeOfFunctionalCharacterization |




## LinkML Source

<details>
```yaml
name: typeOfFunctionalCharacterization
description: Refers to the classification of a protein based on the specific type
  of functional analysis performed to determine its biological activities and roles.
  Possible values include 'Enzymatic' (the protein has been characterized for its
  enzyme activity) and 'Antigenic' (the protein has been characterized for its ability
  to elicit an immune response).
title: type of functional Characterization
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: typeOfFunctionalCharacterization
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- Enzymatic
- Antigenic

```
</details>