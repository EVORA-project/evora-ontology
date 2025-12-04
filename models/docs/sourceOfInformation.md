

# Slot: source of information (sourceOfInformation) 


_The name of the origin from which knowledge is obtained. This can include any entity that provides information._





URI: [EVORAO:sourceOfInformation](https://w3id.org/evorao/sourceOfInformation)
Alias: sourceOfInformation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to someth... |  yes  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sourceOfInformation |
| native | EVORAO:sourceOfInformation |
| related | sio:000253 |
| close | wdp:P248, wdp:P248 |




## LinkML Source

<details>
```yaml
name: sourceOfInformation
description: The name of the origin from which knowledge is obtained. This can include
  any entity that provides information.
title: source of information
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P248
- wdp:P248
related_mappings:
- sio:000253
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