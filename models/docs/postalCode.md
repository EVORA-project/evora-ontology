

# Slot: postal code (postalCode) 


_The postal code._





URI: [EVORAO:postalCode](https://w3id.org/evorao/postalCode)
Alias: postalCode

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
| self | EVORAO:postalCode |
| native | EVORAO:postalCode |
| exact | schema:postalCode, vcard:postal-code |
| close | vcard:hasPostalCode |




## LinkML Source

<details>
```yaml
name: postalCode
description: The postal code.
title: postal code
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:postalCode
- vcard:postal-code
close_mappings:
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