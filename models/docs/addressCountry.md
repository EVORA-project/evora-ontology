

# Slot: address Country (addressCountry)


_The country as of  ISO 3166_





URI: [EVORAO:addressCountry](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#addressCountry)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [Country](Country.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:addressCountry |
| native | EVORAO:addressCountry |
| close | schema:addressCountry, vcard:hasCountryName |




## LinkML Source

<details>
```yaml
name: addressCountry
description: The country as of  ISO 3166
title: address Country
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- schema:addressCountry
- vcard:hasCountryName
rank: 1000
alias: addressCountry
domain_of:
- ContactPoint
range: Country
required: false
multivalued: false

```
</details>