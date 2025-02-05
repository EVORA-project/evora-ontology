

# Slot: accession number (accessionNumber)


_The sequence ID that permits to retrieve the sequence information from the sequence provider_





URI: [EVORAO:accessionNumber](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#accessionNumber)



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
| self | EVORAO:accessionNumber |
| native | EVORAO:accessionNumber |
| close | dct:identifier |




## LinkML Source

<details>
```yaml
name: accessionNumber
description: The sequence ID that permits to retrieve the sequence information from
  the sequence provider
title: accession number
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:identifier
rank: 1000
alias: accessionNumber
domain_of:
- SequenceReference
range: string
required: true
multivalued: false

```
</details>