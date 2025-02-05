

# Slot: title (title)


_The descriptive word or phrase that identifies the current piece of work_





URI: [EVORAO:title](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#title)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | A scientific publication |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* The title of the item should be as short and descriptive as possible. E.g. for virus products it should basically be based on the following Pattern:
'Virus name', 'virus host type', 'collection year', 'country of collection' ex 'suspected epidemiological origin', 'genotype', 'strain', 'variant name or specific feature

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:title |
| native | EVORAO:title |
| exact | dct:title |




## LinkML Source

<details>
```yaml
name: title
description: The descriptive word or phrase that identifies the current piece of work
title: title
comments:
- 'The title of the item should be as short and descriptive as possible. E.g. for
  virus products it should basically be based on the following Pattern:

  ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
  ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant name
  or specific feature'
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dct:title
rank: 1000
alias: title
domain_of:
- Publication
range: string
required: true
multivalued: false

```
</details>