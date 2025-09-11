

# Slot: reference provider prefix (referenceProviderPrefix) 


_The url prefix that once completed with the reference will lead to the linked external resource_





URI: [EVORAO:referenceProviderPrefix](https://w3id.org/evorao/referenceProviderPrefix)
Alias: referenceProviderPrefix

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


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:referenceProviderPrefix |
| native | EVORAO:referenceProviderPrefix |
| related | dcat:landingPage, iao:0000599 |




## LinkML Source

<details>
```yaml
name: referenceProviderPrefix
description: The url prefix that once completed with the reference will lead to the
  linked external resource
title: reference provider prefix
from_schema: https://w3id.org/evorao/
related_mappings:
- dcat:landingPage
- iao:0000599
rank: 1000
alias: referenceProviderPrefix
domain_of:
- ExternalRelatedReference
range: string
required: true
multivalued: false

```
</details>