

# Slot: endpoint URL (endpointUrl) 


_The URL template that allows to get the content._





URI: [dcat:endpointURL](http://www.w3.org/ns/dcat#endpointURL)
Alias: endpointUrl


## Inheritance

* [identifier](identifier.md)
    * [iri](iri.md)
        * **endpointUrl**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |







## Properties

* Range: [Uri](Uri.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:endpointURL |
| native | EVORAO:endpointUrl |
| exact | schema:urlTemplate |
| close | wdp:P1630 |




## LinkML Source

<details>
```yaml
name: endpointUrl
description: The URL template that allows to get the content.
title: endpoint URL
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:urlTemplate
close_mappings:
- wdp:P1630
rank: 1000
is_a: iri
slot_uri: dcat:endpointURL
alias: endpointUrl
domain_of:
- DataService
range: uri
required: true
multivalued: true

```
</details>