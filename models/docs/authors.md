

# Slot: authors (authors) 


_The list of authors_





URI: [EVORAO:authors](https://w3id.org/evorao/authors)
Alias: authors

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | A scientific publication |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:authors |
| native | EVORAO:authors |
| related | sio:001315, iao:0000321 |
| close | wdp:P2093, schema:author |




## LinkML Source

<details>
```yaml
name: authors
description: The list of authors
title: authors
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P2093
- schema:author
related_mappings:
- sio:001315
- iao:0000321
rank: 1000
alias: authors
domain_of:
- Publication
range: string
required: true
multivalued: false

```
</details>