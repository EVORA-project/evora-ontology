

# Slot: login URL (loginURL) 


_The URL template that allows to log in if required_





URI: [EVORAO:loginURL](https://w3id.org/evorao/loginURL)
Alias: loginURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Uri](Uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:loginURL |
| native | EVORAO:loginURL |
| close | wdp:P1630, dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: loginURL
description: The URL template that allows to log in if required
title: login URL
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P1630
- dcat:endpointDescription
rank: 1000
alias: loginURL
domain_of:
- DataProvider
range: uri
required: false
multivalued: false

```
</details>