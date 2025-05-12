

# Slot: country of collection (countryOfCollection) 


_The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to 'country of origin'._





URI: [EVORAO:countryOfCollection](https://w3id.org/evorao/countryOfCollection)
Alias: countryOfCollection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological mate... |  yes  |







## Properties

* Range: [Country](Country.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:countryOfCollection |
| native | EVORAO:countryOfCollection |
| close | dct:spatial, dwc:country |




## LinkML Source

<details>
```yaml
name: countryOfCollection
description: The geographical location where the sample was collected in situ. Used
  for Nagoya/CBD; equivalent to 'country of origin'.
title: country of collection
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:spatial
- dwc:country
rank: 1000
alias: countryOfCollection
domain_of:
- NaturalPartOrigin
range: Country
required: true
multivalued: false

```
</details>