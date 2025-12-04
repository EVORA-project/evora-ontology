

# Slot: in Vocabulary (inVocabulary) 


_Terms belong to a specific vocabulary._





URI: [EVORAO:inVocabulary](https://w3id.org/evorao/inVocabulary)
Alias: inVocabulary

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |  no  |
| [ClinicalGroup](ClinicalGroup.md) | A syndromic grouping of pathogens, based on typical disease manifestation, cl... |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [Country](Country.md) | The country as of ISO3166 |  no  |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  no  |
| [IplcOrigin](IplcOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical... |  no  |
| [GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is natur... |  no  |
| [RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in lab... |  no  |
| [Term](Term.md) | Word or phrase from a specialized area of knowledge |  yes  |
| [ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow... |  no  |
| [Keyword](Keyword.md) | A term or phrase used to tag and categorize content |  no  |
| [PdbReference](PdbReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |  no  |
| [Doi](Doi.md) | A unique string identifier assigned to a digital object, providing a permanen... |  no  |
| [PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmi... |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  no  |
| [SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |  no  |
| [IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |  no  |
| [PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditio... |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to someth... |  no  |
| [ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics... |  no  |
| [Journal](Journal.md) | Periodical journal publishing scientific research |  no  |
| [BiosafetyLevel](BiosafetyLevel.md) | The level of biocontainment required or applied in the facility where the bio... |  no  |
| [ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance... |  no  |
| [IataClassification](IataClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |  no  |
| [TagSequence](TagSequence.md) | The name of the DNA coding sequence or corresponding peptide/protein sequence... |  no  |







## Properties

* Range: [Vocabulary](Vocabulary.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:inVocabulary |
| native | EVORAO:inVocabulary |
| broad | dct:isPartOf |
| related | dct:isReferencedBy |
| close | wdp:P972 |




## LinkML Source

<details>
```yaml
name: inVocabulary
description: Terms belong to a specific vocabulary.
title: in Vocabulary
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P972
related_mappings:
- dct:isReferencedBy
broad_mappings:
- dct:isPartOf
rank: 1000
alias: inVocabulary
domain_of:
- Term
range: Vocabulary
required: true
multivalued: false

```
</details>