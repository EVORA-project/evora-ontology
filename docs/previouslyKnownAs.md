

# Slot: previously known as (previouslyKnownAs)  <span style="color: red;"><strong> (DEPRECATED) </strong> 


_Any historic version of this taxon having a different name._





URI: [EVORAO:previouslyKnownAs](https://w3id.org/evorao/previouslyKnownAs)
Alias: previouslyKnownAs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:previouslyKnownAs |
| native | EVORAO:previouslyKnownAs |
| broad | dwc:Taxon |
| related | schema:alternateName |




## LinkML Source

<details>
```yaml
name: previouslyKnownAs
description: Any historic version of this taxon having a different name.
title: previously known as
deprecated: Deprecated in favor of EVORAO:alternateName. Use EVORAO:alternateName
  for historical names, synonyms, and other alternative labels. EVORAO:previouslyKnownAs
  was limited to historical taxon names and required a Taxon value, which made it
  too narrow for broader naming use cases.
from_schema: https://w3id.org/evorao/
deprecated_element_has_possible_replacement: EVORAO:alternateName
related_mappings:
- schema:alternateName
broad_mappings:
- dwc:Taxon
rank: 1000
alias: previouslyKnownAs
domain_of:
- Taxon
range: Taxon
required: false
multivalued: true

```
</details>