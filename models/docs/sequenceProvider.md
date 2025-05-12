

# Slot: sequence provider (sequenceProvider) 


_The name of the sequence provider within the list of accepted sequence providers_





URI: [EVORAO:sequenceProvider](https://w3id.org/evorao/sequenceProvider)
Alias: sequenceProvider

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


* from schema: https://w3id.org/evorao/




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
from_schema: https://w3id.org/evorao/
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