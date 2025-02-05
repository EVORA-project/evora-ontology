

# Slot: ID (ID)


_The version identifier_





URI: [EVORAO:ID](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#ID)



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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:ID |
| native | EVORAO:ID |
| close | wdp:P393, schema:version |




## LinkML Source

<details>
```yaml
name: ID
description: The version identifier
title: ID
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wdp:P393
- schema:version
rank: 1000
alias: ID
domain_of:
- Version
range: string
required: true
multivalued: false

```
</details>