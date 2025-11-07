

# Slot: login token name (loginTokenName) 


_The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query._





URI: [EVORAO:loginTokenName](https://w3id.org/evorao/loginTokenName)
Alias: loginTokenName

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
| self | EVORAO:loginTokenName |
| native | EVORAO:loginTokenName |
| close | dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: loginTokenName
description: The name of the token, unique identifier of an interaction session, that
  will have to be reused as credential in the query.
title: login token name
from_schema: https://w3id.org/evorao/
close_mappings:
- dcat:endpointDescription
rank: 1000
alias: loginTokenName
domain_of:
- DataProvider
range: string
required: false
multivalued: false

```
</details>