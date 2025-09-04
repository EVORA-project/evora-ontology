

# Slot: query method (queryMethod) 


_The http request method used to access the requested query url_





URI: [EVORAO:queryMethod](https://w3id.org/evorao/queryMethod)
Alias: queryMethod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:queryMethod |
| native | EVORAO:queryMethod |
| broad | schema:httpMethod |
| close | dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: queryMethod
description: The http request method used to access the requested query url
title: query method
from_schema: https://w3id.org/evorao/
close_mappings:
- dcat:endpointDescription
broad_mappings:
- schema:httpMethod
rank: 1000
alias: queryMethod
domain_of:
- DataProvider
range: string
required: true
multivalued: false
equals_string_in:
- GET
- POST

```
</details>