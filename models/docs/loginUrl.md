

# Slot: login URL (loginUrl) 


_The URL template that allows to log in if required._





URI: [EVORAO:loginUrl](https://w3id.org/evorao/loginUrl)
Alias: loginUrl


## Inheritance

* [identifier](identifier.md)
    * [iri](iri.md)
        * **loginUrl**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Uri](Uri.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:loginUrl |
| native | EVORAO:loginUrl |
| broad | schema:urlTemplate |
| close | wdp:P1630, dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: loginUrl
description: The URL template that allows to log in if required.
title: login URL
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P1630
- dcat:endpointDescription
broad_mappings:
- schema:urlTemplate
rank: 1000
is_a: iri
alias: loginUrl
domain_of:
- DataProvider
range: uri
required: false
multivalued: true

```
</details>