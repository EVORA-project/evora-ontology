

# Slot: content URL (contentUrl) 


_The web address or location where the file content is stored and can be accessed or downloaded._





URI: [EVORAO:contentUrl](https://w3id.org/evorao/contentUrl)
Alias: contentUrl


## Inheritance

* [identifier](identifier.md)
    * [iri](iri.md)
        * **contentUrl**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |







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
| self | EVORAO:contentUrl |
| native | EVORAO:contentUrl |
| exact | schema:contentUrl |




## LinkML Source

<details>
```yaml
name: contentUrl
description: The web address or location where the file content is stored and can
  be accessed or downloaded.
title: content URL
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:contentUrl
rank: 1000
is_a: iri
alias: contentUrl
domain_of:
- File
range: uri
required: true
multivalued: true

```
</details>