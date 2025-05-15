

# Slot: endpoint URL (endpointURL) 


_The URL template that allows to get the content_





URI: [dcat:endpointURL](http://www.w3.org/ns/dcat#endpointURL)
Alias: endpointURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |







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
| native | EVORAO:endpointURL |
| close | wdp:P1630 |




## LinkML Source

<details>
```yaml
name: endpointURL
description: The URL template that allows to get the content
title: endpoint URL
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P1630
rank: 1000
slot_uri: dcat:endpointURL
alias: endpointURL
domain_of:
- DataService
range: uri
required: true
multivalued: false

```
</details>