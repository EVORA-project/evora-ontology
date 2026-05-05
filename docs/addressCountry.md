

# Slot: address Country (addressCountry) 


_The country as of  ISO 3166._





URI: [EVORAO:addressCountry](https://w3id.org/evorao/addressCountry)
Alias: addressCountry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [Country](Country.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:addressCountry |
| native | EVORAO:addressCountry |
| exact | schema:addressCountry, vcard:hasCountryName |




## LinkML Source

<details>
```yaml
name: addressCountry
description: The country as of  ISO 3166.
title: address Country
from_schema: https://w3id.org/evorao/
exact_mappings:
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