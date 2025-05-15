

# Slot: content URL (contentURL) 


_The web address or location where the file content is stored and can be accessed or downloaded._





URI: [EVORAO:contentURL](https://w3id.org/evorao/contentURL)
Alias: contentURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:contentURL |
| native | EVORAO:contentURL |




## LinkML Source

<details>
```yaml
name: contentURL
description: The web address or location where the file content is stored and can
  be accessed or downloaded.
title: content URL
from_schema: https://w3id.org/evorao/
rank: 1000
alias: contentURL
domain_of:
- File
range: uri
required: true
multivalued: false

```
</details>