

# Slot: alpha 2 code (alpha2Code) 


_Two-letter country codes from ISO 3166-1 alpha-2_





URI: [EVORAO:alpha2Code](https://w3id.org/evorao/alpha2Code)
Alias: alpha2Code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Country](Country.md) | The country as of ISO3166 |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:alpha2Code |
| native | EVORAO:alpha2Code |
| exact | geo:000000023 |
| related | obib:0000620, ncit:C54641 |
| close | schema:addressCountry |




## LinkML Source

<details>
```yaml
name: alpha2Code
description: Two-letter country codes from ISO 3166-1 alpha-2
title: alpha 2 code
from_schema: https://w3id.org/evorao/
exact_mappings:
- geo:000000023
close_mappings:
- schema:addressCountry
related_mappings:
- obib:0000620
- ncit:C54641
rank: 1000
alias: alpha2Code
domain_of:
- Country
range: string
required: true
multivalued: false

```
</details>