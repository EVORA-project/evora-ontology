

# Slot: domain (domain) 


_A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function_





URI: [EVORAO:domain](https://w3id.org/evorao/domain)
Alias: domain

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:domain |
| native | EVORAO:domain |
| close | uniprotrdfs:domain |




## LinkML Source

<details>
```yaml
name: domain
description: A distinct structural and functional unit within the protein, often capable
  of independent folding and stability, which contributes to the protein's overall
  function
title: domain
from_schema: https://w3id.org/evorao/
close_mappings:
- uniprotrdfs:domain
rank: 1000
alias: domain
domain_of:
- Protein
range: string
required: false
multivalued: true

```
</details>