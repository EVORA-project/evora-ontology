

# Slot: collection date (collectionDate)


_The date when the sample was collected in situ. If unknown/private, use a proxy date such as 'date received' and indicate this by setting to true the before date property_





URI: [EVORAO:collectionDate](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#collectionDate)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:collectionDate |
| native | EVORAO:collectionDate |




## LinkML Source

<details>
```yaml
name: collectionDate
description: The date when the sample was collected in situ. If unknown/private, use
  a proxy date such as 'date received' and indicate this by setting to true the before
  date property
title: collection date
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: collectionDate
domain_of:
- NaturalPartOrigin
range: datetime
required: true
multivalued: false

```
</details>