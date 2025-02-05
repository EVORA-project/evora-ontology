

# Slot: sequence provider (sequenceProvider)


_The name of the sequence provider within the list of accepted sequence providers_





URI: [EVORAO:sequenceProvider](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#sequenceProvider)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceReference](SequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequenceProvider |
| native | EVORAO:sequenceProvider |
| close | dct:publisher |




## LinkML Source

<details>
```yaml
name: sequenceProvider
description: The name of the sequence provider within the list of accepted sequence
  providers
title: sequence provider
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:publisher
rank: 1000
alias: sequenceProvider
domain_of:
- SequenceReference
range: string
required: true
multivalued: false
equals_string_in:
- ENA
- GenBank

```
</details>