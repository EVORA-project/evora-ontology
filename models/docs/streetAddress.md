

# Slot: street address (streetAddress) 


_The building/apartment number and the street name_





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
| close | schema:streetAddress, vcard:hasStreetAddress |




## LinkML Source

<details>
```yaml
name: streetAddress
description: The building/apartment number and the street name
title: street address
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:streetAddress
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