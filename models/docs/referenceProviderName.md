

# Slot: reference provider name (referenceProviderName)


_The name for the reference provider_





URI: [EVORAO:referenceProviderName](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#referenceProviderName)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve an item from an external provider |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:referenceProviderName |
| native | EVORAO:referenceProviderName |
| close | dct:publisher |




## LinkML Source

<details>
```yaml
name: referenceProviderName
description: The name for the reference provider
title: reference provider name
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:publisher
rank: 1000
alias: referenceProviderName
domain_of:
- ExternalRelatedReference
range: string
required: true
multivalued: false

```
</details>