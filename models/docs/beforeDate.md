

# Slot: before date (beforeDate)


_Set to TRUE if a proxy date for the collection date is used_





URI: [EVORAO:beforeDate](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#beforeDate)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:beforeDate |
| native | EVORAO:beforeDate |




## LinkML Source

<details>
```yaml
name: beforeDate
description: Set to TRUE if a proxy date for the collection date is used
title: before date
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
ifabsent: 'false'
alias: beforeDate
domain_of:
- NaturalPartOrigin
range: boolean
required: true
multivalued: false

```
</details>