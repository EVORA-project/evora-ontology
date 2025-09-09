

# Slot: endpoint URL (endpointUrl) 


_The URL template that allows to get the content_





URI: [dcat:endpointURL](http://www.w3.org/ns/dcat#endpointURL)
Alias: endpointUrl

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:endpointURL |
| native | EVORAO:endpointUrl |
| close | wdp:P1630 |




## LinkML Source

<details>
```yaml
name: endpointUrl
description: The URL template that allows to get the content
title: endpoint URL
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P1630
rank: 1000
slot_uri: dcat:endpointURL
alias: endpointUrl
domain_of:
- DataService
range: uri
required: true
multivalued: false

```
</details>