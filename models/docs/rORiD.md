

# Slot: ROR iD (rORiD)


_The corresponding organization's persistent identifier from the Research Organization Registry (ROR)_





URI: [EVORAO:rORiD](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#rORiD)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RI](RI.md) | A research infrastructure |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  yes  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:rORiD |
| native | EVORAO:rORiD |
| exact | wdp:P6782 |




## LinkML Source

<details>
```yaml
name: rORiD
description: The corresponding organization's persistent identifier from the Research
  Organization Registry (ROR)
title: ROR iD
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- wdp:P6782
rank: 1000
alias: rORiD
domain_of:
- Organization
range: string
required: false
recommended: true
multivalued: false

```
</details>