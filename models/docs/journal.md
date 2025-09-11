

# Slot: journal (journal) 


_The scientific journal in which the publication was published_





URI: [EVORAO:journal](https://w3id.org/evorao/journal)
Alias: journal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | A scientific publication |  yes  |







## Properties

* Range: [Journal](Journal.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:journal |
| native | EVORAO:journal |
| close | wdp:P1433, biolink:published_in, uniprotrdfs:publishedIn |




## LinkML Source

<details>
```yaml
name: journal
description: The scientific journal in which the publication was published
title: journal
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P1433
- biolink:published_in
- uniprotrdfs:publishedIn
rank: 1000
alias: journal
domain_of:
- Publication
range: Journal
required: false
multivalued: false

```
</details>