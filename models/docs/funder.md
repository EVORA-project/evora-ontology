

# Slot: funder (funder) 


_The organization providing the financial support._





URI: [EVORAO:funder](https://w3id.org/evorao/funder)
Alias: funder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FundingSource](FundingSource.md) | A program, grant, or project providing financial support for the access or us... |  yes  |







## Properties

* Range: [Organization](Organization.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:funder |
| native | EVORAO:funder |
| close | schema:funder |




## LinkML Source

<details>
```yaml
name: funder
description: The organization providing the financial support.
title: funder
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:funder
rank: 1000
alias: funder
domain_of:
- FundingSource
range: Organization
required: false
multivalued: false

```
</details>