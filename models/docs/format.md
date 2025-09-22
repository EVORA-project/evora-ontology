

# Slot: format (format) 


_The file type or format that indicates how the data within the file is structured_





URI: [EVORAO:format](https://w3id.org/evorao/format)
Alias: format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:format |
| native | EVORAO:format |
| exact | schema:fileFormat, dct:format |
| close | schema:encodingFormat |




## LinkML Source

<details>
```yaml
name: format
description: The file type or format that indicates how the data within the file is
  structured
title: format
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:fileFormat
- dct:format
close_mappings:
- schema:encodingFormat
rank: 1000
alias: format
domain_of:
- File
range: string
required: true
multivalued: false

```
</details>