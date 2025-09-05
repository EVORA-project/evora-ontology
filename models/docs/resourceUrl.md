

# Slot: resource URL (resourceUrl) 


_The web address or location where the details or content is stored and can be accessed or downloaded._





URI: [EVORAO:resourceUrl](https://w3id.org/evorao/resourceUrl)
Alias: resourceUrl

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |







## Properties

* Range: [Uri](Uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:resourceUrl |
| native | EVORAO:resourceUrl |
| exact | dct:license |
| close | schema:url, schema:url |




## LinkML Source

<details>
```yaml
name: resourceUrl
description: The web address or location where the details or content is stored and
  can be accessed or downloaded.
title: resource URL
from_schema: https://w3id.org/evorao/
exact_mappings:
- dct:license
close_mappings:
- schema:url
- schema:url
rank: 1000
alias: resourceUrl
domain_of:
- License
- Certification
range: uri
required: false
multivalued: false

```
</details>