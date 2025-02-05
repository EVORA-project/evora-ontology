

# Slot: query method (queryMethod)


_The http request method used to access the requested query url_





URI: [EVORAO:queryMethod](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#queryMethod)



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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:queryMethod |
| native | EVORAO:queryMethod |
| close | dcat:endpointDescription |




## LinkML Source

<details>
```yaml
name: queryMethod
description: The http request method used to access the requested query url
title: query method
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dcat:endpointDescription
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