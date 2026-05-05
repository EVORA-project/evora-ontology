

# Slot: version Of (versionOf) 


_Identifier of what type of entities the version qualifies._





URI: [EVORAO:versionOf](https://w3id.org/evorao/versionOf)
Alias: versionOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Version](Version.md) | Numeric code assigned to identify a particular historical version of a work (... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:versionOf |
| native | EVORAO:versionOf |
| related | dct:isVersionOf |




## LinkML Source

<details>
```yaml
name: versionOf
description: Identifier of what type of entities the version qualifies.
title: version Of
from_schema: https://w3id.org/evorao/
related_mappings:
- dct:isVersionOf
rank: 1000
alias: versionOf
domain_of:
- Version
range: string
required: true
multivalued: false

```
</details>