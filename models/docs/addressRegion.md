

# Slot: region (addressRegion) 


_The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division_





URI: [EVORAO:addressRegion](https://w3id.org/evorao/addressRegion)
Alias: addressRegion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:addressRegion |
| native | EVORAO:addressRegion |
| exact | schema:addressRegion, vcard:region |
| close | vcard:hasRegion |




## LinkML Source

<details>
```yaml
name: addressRegion
description: The region in which the locality is, and which is in the country. For
  example, California or another appropriate first-level Administrative division
title: region
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:addressRegion
- vcard:region
close_mappings:
- vcard:hasRegion
rank: 1000
alias: addressRegion
domain_of:
- ContactPoint
range: string
required: false
multivalued: false

```
</details>