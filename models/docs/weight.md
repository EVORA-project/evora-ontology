

# Slot: weight (weight)


_A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0_





URI: [EVORAO:weight](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#weight)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  no  |
| [GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is natur... |  no  |
| [IPLCOrigin](IPLCOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical... |  no  |
| [TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |  no  |
| [IATAClassification](IATAClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |  no  |
| [Term](Term.md) | Word or phrase from a specialized area of knowledge |  yes  |
| [ProteinTag](ProteinTag.md) | Peptide sequence genetically grafted onto a recombinant protein |  no  |
| [PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmi... |  no  |
| [Journal](Journal.md) | Periodical journal publishing scientific research |  no  |
| [IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |  no  |
| [PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditio... |  no  |
| [DOI](DOI.md) | A unique string identifier assigned to a digital object, providing a permanen... |  no  |
| [ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow... |  no  |
| [ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics... |  no  |
| [SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |  no  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  no  |
| [Country](Country.md) | The country as of ISO3166 |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in lab... |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  no  |
| [ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance... |  no  |
| [PDBReference](PDBReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |  no  |
| [Keyword](Keyword.md) | A term or phrase used to tag and categorize content |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  yes  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





## Comments

* The lowest weighted Data providers are triggered first, this may be usefull to populate at first entities that are referenced by others (e.g. Version ahead of Rank ahead of Taxon)

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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