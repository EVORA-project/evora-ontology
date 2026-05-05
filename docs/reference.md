

# Slot: reference (reference) 


_The identifier reference of the connected external item._





URI: [EVORAO:reference](https://w3id.org/evorao/reference)
Alias: reference


## Inheritance

* [identifier](identifier.md)
    * **reference**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve an item from an external provider |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:reference |
| native | EVORAO:reference |
| close | dct:identifier, dct:references |




## LinkML Source

<details>
```yaml
name: reference
description: The identifier reference of the connected external item.
title: reference
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:identifier
- dct:references
rank: 1000
is_a: identifier
alias: reference
domain_of:
- ExternalRelatedReference
range: string
required: true
multivalued: true

```
</details>