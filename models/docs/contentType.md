

# Slot: content type (contentType)


_The content type of the response to the queries_





URI: [EVORAO:contentType](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#contentType)



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
| self | EVORAO:contentType |
| native | EVORAO:contentType |
| close | dct:format |




## LinkML Source

<details>
```yaml
name: contentType
description: The content type of the response to the queries
title: content type
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:format
rank: 1000
ifabsent: string(JSON)
alias: contentType
domain_of:
- DataProvider
range: string
required: true
multivalued: false

```
</details>