

# Slot: source of information (sourceOfInformation)


_The name of the origin from which knowledge is obtained. This can include any entity that provides information_





URI: [EVORAO:sourceOfInformation](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#sourceOfInformation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  yes  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  yes  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sourceOfInformation |
| native | EVORAO:sourceOfInformation |
| close | wdp:P248 |




## LinkML Source

<details>
```yaml
name: sourceOfInformation
description: The name of the origin from which knowledge is obtained. This can include
  any entity that provides information
title: source of information
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wdp:P248
rank: 1000
alias: sourceOfInformation
domain_of:
- CommonName
- AlternateName
range: string
required: false
multivalued: true

```
</details>