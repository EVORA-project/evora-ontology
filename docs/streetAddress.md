

# Slot: street address (streetAddress) 


_The building/apartment number and the street name._





URI: [EVORAO:streetAddress](https://w3id.org/evorao/streetAddress)
Alias: streetAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:streetAddress |
| native | EVORAO:streetAddress |
| exact | schema:streetAddress, vcard:street-address |
| close | vcard:hasStreetAddress |




## LinkML Source

<details>
```yaml
name: streetAddress
description: The building/apartment number and the street name.
title: street address
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:streetAddress
- vcard:street-address
close_mappings:
- vcard:hasStreetAddress
rank: 1000
alias: streetAddress
domain_of:
- ContactPoint
range: string
required: false
multivalued: false

```
</details>