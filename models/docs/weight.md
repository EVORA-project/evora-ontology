

# Slot: weight (weight) 


_A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0_





URI: [EVORAO:weight](https://w3id.org/evorao/weight)
Alias: weight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in lab... |  no  |
| [TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  no  |
| [PdbReference](PdbReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |  no  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [IataClassification](IataClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |  no  |
| [IplcOrigin](IplcOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical... |  no  |
| [IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |  no  |
| [TagSequence](TagSequence.md) | The name of the DNA coding sequence or corresponding peptide/protein sequence... |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  no  |
| [GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is natur... |  no  |
| [Doi](Doi.md) | A unique string identifier assigned to a digital object, providing a permanen... |  no  |
| [SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |  no  |
| [Journal](Journal.md) | Periodical journal publishing scientific research |  no  |
| [Country](Country.md) | The country as of ISO3166 |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |
| [Term](Term.md) | Word or phrase from a specialized area of knowledge |  yes  |
| [ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics... |  no  |
| [ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow... |  no  |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  no  |
| [ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance... |  no  |
| [Keyword](Keyword.md) | A term or phrase used to tag and categorize content |  no  |
| [PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditio... |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  no  |
| [PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmi... |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





## Comments

* The lowest weighted Data providers are triggered first, this may be usefull to populate at first entities that are referenced by others (e.g. Version ahead of Rank ahead of Taxon)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:weight |
| native | EVORAO:weight |
| close | adms:status, adms:status |




## LinkML Source

<details>
```yaml
name: weight
description: A numerical value indicating relative importance or priority, generally
  processed in ascending order. This weight helps prioritize content when organizing
  or processing data. Its value can be negative, with a default set to 0
title: weight
comments:
- The lowest weighted Data providers are triggered first, this may be usefull to populate
  at first entities that are referenced by others (e.g. Version ahead of Rank ahead
  of Taxon)
from_schema: https://w3id.org/evorao/
close_mappings:
- adms:status
- adms:status
rank: 1000
ifabsent: int(0)
alias: weight
domain_of:
- DataProvider
- Term
range: integer
required: true
multivalued: false

```
</details>