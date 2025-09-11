

# Slot: license (license) 


_Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions_





URI: [dct:license](http://purl.org/dc/terms/license)
Alias: license

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |







## Properties

* Range: [License](License.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:license |
| native | EVORAO:license |
| exact | schema:license, dct:license |
| close | wdp:P275 |




## LinkML Source

<details>
```yaml
name: license
description: Information about terms and conditions under which the subject can be
  used, shared, or distributed, indicating any restrictions or permissions
title: license
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:license
- dct:license
close_mappings:
- wdp:P275
rank: 1000
slot_uri: dct:license
alias: license
domain_of:
- DataProvider
- File
range: License
required: false
multivalued: false

```
</details>