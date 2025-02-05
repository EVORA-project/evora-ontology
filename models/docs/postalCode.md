

# Slot: postal code (postalCode)


_The postal code_





URI: [EVORAO:postalCode](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#postalCode)



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
| self | EVORAO:postalCode |
| native | EVORAO:postalCode |
| close | schema:postalCode, vcard:hasPostalCode |




## LinkML Source

<details>
```yaml
name: postalCode
description: The postal code
title: postal code
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- schema:postalCode
- vcard:hasPostalCode
rank: 1000
alias: postalCode
domain_of:
- ContactPoint
range: string
required: false
multivalued: false

```
</details>