

# Slot: content type (contentType) 


_The content type of the response to queries. It specifies the serialization, file type, or media type used to convey the resource, typically expressed as a MIME type following IANA media type registrations_





URI: [EVORAO:contentType](https://w3id.org/evorao/contentType)
Alias: contentType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* This property characterizes how the content is structured or encoded, independent of the entity type it represents. Values should use MIME types (e.g. application/json, text/csv, text/tab-separated-values, text/x-fasta, application/vnd.genbank)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:contentType |
| native | EVORAO:contentType |
| exact | schema:contentType, dct:format |




## LinkML Source

<details>
```yaml
name: contentType
description: The content type of the response to queries. It specifies the serialization,
  file type, or media type used to convey the resource, typically expressed as a MIME
  type following IANA media type registrations
title: content type
comments:
- This property characterizes how the content is structured or encoded, independent
  of the entity type it represents. Values should use MIME types (e.g. application/json,
  text/csv, text/tab-separated-values, text/x-fasta, application/vnd.genbank)
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:contentType
- dct:format
rank: 1000
ifabsent: string(application/json)
alias: contentType
domain_of:
- DataProvider
range: string
required: true
multivalued: false

```
</details>