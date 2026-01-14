

# Slot: name (name) 


_A word or set of words used to identify and refer to an entity._





URI: [foaf:name](http://xmlns.com/foaf/0.1/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | An individual |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [ResearchInfrastructure](ResearchInfrastructure.md) | A research infrastructure (RI) |  no  |







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
| exact | schema:name, vcard:fn |
| close | rdfs:label, dct:title |




## LinkML Source

<details>
```yaml
name: name
description: A word or set of words used to identify and refer to an entity.
title: name
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:name
- vcard:fn
close_mappings:
- rdfs:label
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