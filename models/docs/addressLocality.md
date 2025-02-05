

# Slot: locality/city (addressLocality)


_The locality in which the street address is, and which is in the region. e.g, the city_





URI: [EVORAO:addressLocality](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#addressLocality)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:addressLocality |
| native | EVORAO:addressLocality |
| close | schema:addressLocality, vcard:hasLocality |




## LinkML Source

<details>
```yaml
name: addressLocality
description: The locality in which the street address is, and which is in the region.
  e.g, the city
title: locality/city
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- schema:addressLocality
- vcard:hasLocality
rank: 1000
alias: addressLocality
domain_of:
- ContactPoint
range: string
required: false
multivalued: false

```
</details>