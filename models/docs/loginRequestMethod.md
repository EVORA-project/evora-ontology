

# Slot: login request method (loginRequestMethod) 


_The http request method used to acces the login request url_





URI: [EVORAO:loginRequestMethod](https://w3id.org/evorao/loginRequestMethod)
Alias: loginRequestMethod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:loginRequestMethod |
| native | EVORAO:loginRequestMethod |
| close | dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: loginRequestMethod
description: The http request method used to acces the login request url
title: login request method
from_schema: https://w3id.org/evorao/
close_mappings:
- dcat:endpointDescription
rank: 1000
ifabsent: string(GET)
alias: loginRequestMethod
domain_of:
- DataProvider
range: string
required: false
multivalued: false
equals_string_in:
- GET
- POST

```
</details>