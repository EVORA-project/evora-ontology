

# Slot: alternate name (alternateName) 


_Any other name under which the entity can be known._





URI: [EVORAO:alternateName](https://w3id.org/evorao/alternateName)
Alias: alternateName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [ResearchInfrastructure](ResearchInfrastructure.md) | A research infrastructure (RI) |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  yes  |
| [ClinicalGroup](ClinicalGroup.md) | A syndromic grouping of pathogens, based on typical disease manifestation, cl... |  yes  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  yes  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to someth... |  yes  |







## Properties

* Range: [AlternateName](AlternateName.md)

* Multivalued: True





## Comments

* This includes previous names, acronyms, former taxonomic terms, and other variations.
* This information can serve as keywords for search purposes and as a bridge with other projects that use different naming systems or taxonomies.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:alternateName |
| native | EVORAO:alternateName |
| exact | schema:alternateName, dct:alternative, iao:0000118 |
| close | wdp:P4970 |




## LinkML Source

<details>
```yaml
name: alternateName
description: Any other name under which the entity can be known.
title: alternate name
comments:
- This includes previous names, acronyms, former taxonomic terms, and other variations.
- This information can serve as keywords for search purposes and as a bridge with
  other projects that use different naming systems or taxonomies.
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:alternateName
- dct:alternative
- iao:0000118
close_mappings:
- wdp:P4970
rank: 1000
alias: alternateName
domain_of:
- CommonName
- AlternateName
- Taxon
- ClinicalGroup
- Organization
range: AlternateName
required: false
multivalued: true

```
</details>