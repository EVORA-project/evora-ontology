

# Slot: email (email) 


_The email address._





URI: [EVORAO:email](https://w3id.org/evorao/email)
Alias: email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:email |
| native | EVORAO:email |
| exact | schema:email, foaf:mbox |
| close | vcard:email |




## LinkML Source

<details>
```yaml
name: email
description: The email address.
title: email
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:email
- foaf:mbox
close_mappings:
- vcard:email
rank: 1000
alias: email
domain_of:
- ContactPoint
range: string
required: false
recommended: true
multivalued: false

```
</details>