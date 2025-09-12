

# Slot: alt text (altText) 


_An alternate text for the image, if the image cannot be displayed_





URI: [EVORAO:altText](https://w3id.org/evorao/altText)
Alias: altText

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:altText |
| native | EVORAO:altText |
| exact | schema:caption |




## LinkML Source

<details>
```yaml
name: altText
description: An alternate text for the image, if the image cannot be displayed
title: alt text
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:caption
rank: 1000
alias: altText
domain_of:
- Image
range: string
required: false
recommended: true
multivalued: false

```
</details>