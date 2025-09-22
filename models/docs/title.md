

# Slot: title (title) 


_A name given to the resource_





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in lab... |  no  |
| [TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  no  |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |
| [PdbReference](PdbReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |  no  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [IataClassification](IataClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [IplcOrigin](IplcOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical... |  no  |
| [Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field |  no  |
| [IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |  no  |
| [TagSequence](TagSequence.md) | The name of the DNA coding sequence or corresponding peptide/protein sequence... |  no  |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  no  |
| [GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is natur... |  no  |
| [Catalogue](Catalogue.md) | A curated collection of metadata about resources |  no  |
| [Doi](Doi.md) | A unique string identifier assigned to a digital object, providing a permanen... |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  no  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Journal](Journal.md) | Periodical journal publishing scientific research |  no  |
| [Country](Country.md) | The country as of ISO3166 |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of bi... |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |
| [Term](Term.md) | Word or phrase from a specialized area of knowledge |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Dataset](Dataset.md) | A collection of data, published or curated by a single agent, and available f... |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow... |  no  |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  no  |
| [Publication](Publication.md) | A scientific publication |  yes  |
| [ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance... |  no  |
| [Keyword](Keyword.md) | A term or phrase used to tag and categorize content |  no  |
| [Collection](Collection.md) | Set of products and services with some common characteristics |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditio... |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmi... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* The title of the item should be as short and descriptive as possible. E.g. for virus products it should basically be based on the following Pattern: 'Virus name', 'virus host type', 'collection year', 'country of collection' ex 'suspected epidemiological origin', 'genotype', 'strain', 'variant name or specific feature

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | EVORAO:title |
| exact | schema:name, rdfs:label |




## LinkML Source

<details>
```yaml
name: title
description: A name given to the resource
title: title
comments:
- 'The title of the item should be as short and descriptive as possible. E.g. for
  virus products it should basically be based on the following Pattern: ''Virus name'',
  ''virus host type'', ''collection year'', ''country of collection'' ex ''suspected
  epidemiological origin'', ''genotype'', ''strain'', ''variant name or specific feature'
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:name
- rdfs:label
rank: 1000
slot_uri: dct:title
alias: title
domain_of:
- Dataset
- DataService
- Publication
- Term
- License
- Certification
range: string
required: true
multivalued: false

```
</details>