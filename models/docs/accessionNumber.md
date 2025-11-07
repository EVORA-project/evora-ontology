

# Slot: accession number (accessionNumber) 


_The sequence ID that permits to retrieve the sequence information from the sequence provider._





URI: [EVORAO:accessionNumber](https://w3id.org/evorao/accessionNumber)
Alias: accessionNumber


## Inheritance

* [identifier](identifier.md)
    * **accessionNumber**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceReference](SequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:accessionNumber |
| native | EVORAO:accessionNumber |
| narrow | ncit:P102 |
| broad | schema:identifier |
| related | dct:identifier |




## LinkML Source

<details>
```yaml
name: accessionNumber
description: The sequence ID that permits to retrieve the sequence information from
  the sequence provider.
title: accession number
from_schema: https://w3id.org/evorao/
related_mappings:
- dct:identifier
narrow_mappings:
- ncit:P102
broad_mappings:
- schema:identifier
rank: 1000
is_a: identifier
alias: accessionNumber
domain_of:
- SequenceReference
range: string
required: true
multivalued: true

```
</details>