

# Slot: resource URL (resourceUrl) 


_The web address or location where the details or content is stored and can be accessed or downloaded._





URI: [EVORAO:resourceUrl](https://w3id.org/evorao/resourceUrl)
Alias: resourceUrl


## Inheritance

* [identifier](identifier.md)
    * [iri](iri.md)
        * **resourceUrl**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |







## Properties

* Range: [Uri](Uri.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:resourceUrl |
| native | EVORAO:resourceUrl |
| exact | dct:license, schema:archivedAt |
| broad | schema:url, schema:url |




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
- schema:archivedAt
broad_mappings:
- schema:url
- schema:url
rank: 1000
is_a: iri
alias: resourceUrl
domain_of:
- License
- Certification
range: uri
required: false
multivalued: true

```
</details>