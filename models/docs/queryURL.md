

# Slot: query URL (queryURL)


_The URL template that allows to get the content_





URI: [EVORAO:queryURL](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#queryURL)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:queryURL |
| native | EVORAO:queryURL |
| exact | dcat:endpointURL |
| close | wdp:P1630 |




## LinkML Source

<details>
```yaml
name: queryURL
description: The URL template that allows to get the content
title: query URL
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:endpointURL
close_mappings:
- wdp:P1630
rank: 1000
alias: queryURL
domain_of:
- DataProvider
range: uri
required: true
multivalued: false

```
</details>