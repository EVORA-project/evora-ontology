

# Slot: login request method (loginRequestMethod)


_The http request method used to acces the login request url_





URI: [EVORAO:loginRequestMethod](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#loginRequestMethod)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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