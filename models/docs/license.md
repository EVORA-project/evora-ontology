

# Slot: license



URI: [EVORA:license](https://evora-project.eu/license)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:license |
| native | EVORA:license |




## LinkML Source

<details>
```yaml
name: license
from_schema: https://evora-project.eu/
rank: 1000
alias: license
domain_of:
- DataProvider
- File
range: string

```
</details>