

# Slot: name (name) 


_A word or set of words used to identify and refer to an entity_





URI: [foaf:name](http://xmlns.com/foaf/0.1/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Person](Person.md) | An individual |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI) |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:name |
| native | EVORAO:name |
| exact | schema:name, schema:name |
| close | dct:title, foaf:name, dct:title |




## LinkML Source

<details>
```yaml
name: name
description: A word or set of words used to identify and refer to an entity
title: name
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:name
- schema:name
close_mappings:
- dct:title
- foaf:name
- dct:title
rank: 1000
slot_uri: foaf:name
alias: name
domain_of:
- PersonOrOrganization
- File
- ContactPoint
range: string
required: true
multivalued: false

```
</details>