

# Slot: grant number (grantNumber) 


_A formal reference or agreement number assigned by the funding body._





URI: [EVORAO:grantNumber](https://w3id.org/evorao/grantNumber)
Alias: grantNumber


## Inheritance

* [identifier](identifier.md)
    * **grantNumber**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FundingSource](FundingSource.md) | A program, grant, or project providing financial support for the access or us... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:grantNumber |
| native | EVORAO:grantNumber |




## LinkML Source

<details>
```yaml
name: grantNumber
description: A formal reference or agreement number assigned by the funding body.
title: grant number
from_schema: https://w3id.org/evorao/
rank: 1000
is_a: identifier
alias: grantNumber
domain_of:
- FundingSource
range: string
required: false
multivalued: true

```
</details>