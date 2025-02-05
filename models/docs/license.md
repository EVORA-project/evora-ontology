

# Slot: license (license)


_Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions_





URI: [EVORAO:license](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#license)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [License](License.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:license |
| native | EVORAO:license |
| exact | dct:license |




## LinkML Source

<details>
```yaml
name: license
description: Information about terms and conditions under which the subject can be
  used, shared, or distributed, indicating any restrictions or permissions
title: license
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dct:license
rank: 1000
alias: license
domain_of:
- DataProvider
- File
range: License
required: false
multivalued: false

```
</details>