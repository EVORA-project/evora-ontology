

# Slot: expressed as (expressedAs) 


_Refers to the form in which the protein is produced and manifested in a biological system. Possible values include 'Soluble' (proteins that are dissolved in the cellular or extracellular fluid) and 'Inclusion bodies' (aggregated proteins that are insoluble and form within the cell)_





URI: [EVORAO:expressedAs](https://w3id.org/evorao/expressedAs)
Alias: expressedAs

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
| self | EVORAO:expressedAs |
| native | EVORAO:expressedAs |




## LinkML Source

<details>
```yaml
name: expressedAs
description: Refers to the form in which the protein is produced and manifested in
  a biological system. Possible values include 'Soluble' (proteins that are dissolved
  in the cellular or extracellular fluid) and 'Inclusion bodies' (aggregated proteins
  that are insoluble and form within the cell)
title: expressed as
from_schema: https://w3id.org/evorao/
rank: 1000
alias: expressedAs
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- Soluble
- Inclusion bodies

```
</details>