

# Slot: name (name)


_The label that allows humans to identify the current item_





URI: [EVORAO:name](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |  no  |
| [Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used... |  no  |
| [Catalogue](Catalogue.md) | A curated collection of metadata about resources |  yes  |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [File](File.md) | Digital document or record stored in a specific format that contains data or ... |  yes  |
| [GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is natur... |  no  |
| [IPLCOrigin](IPLCOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical... |  no  |
| [TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |  no  |
| [IATAClassification](IATAClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Term](Term.md) | Word or phrase from a specialized area of knowledge |  yes  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProteinTag](ProteinTag.md) | Peptide sequence genetically grafted onto a recombinant protein |  no  |
| [PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmi... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [RI](RI.md) | A research infrastructure |  no  |
| [Taxonomy](Taxonomy.md) | Science of naming, defining and classifying organisms |  no  |
| [Service](Service.md) | A service |  no  |
| [Document](Document.md) | Subclass of File representing textual or written files such as reports, manua... |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Journal](Journal.md) | Periodical journal publishing scientific research |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Collection](Collection.md) | Set of products and services with some common characteristics |  no  |
| [IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presen... |  no  |
| [PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditio... |  no  |
| [DataService](DataService.md) | A collection of operations that provides access to one or more datasets or da... |  yes  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [Product](Product.md) | A product |  no  |
| [DOI](DOI.md) | A unique string identifier assigned to a digital object, providing a permanen... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or i... |  no  |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |
| [Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field |  no  |
| [ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow... |  no  |
| [ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics... |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |  no  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [AlternateName](AlternateName.md) | List of other names for things |  no  |
| [Country](Country.md) | The country as of ISO3166 |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in lab... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  no  |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |
| [ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance... |  no  |
| [Person](Person.md) | An individual |  no  |
| [PDBReference](PDBReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Keyword](Keyword.md) | A term or phrase used to tag and categorize content |  no  |
| [DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits ... |  no  |







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
| self | EVORAO:name |
| native | EVORAO:name |
| exact | dct:title |
| close | rdfs:label |




## LinkML Source

<details>
```yaml
name: name
description: The label that allows humans to identify the current item
title: name
comments:
- 'The title of the item should be as short and descriptive as possible. E.g. for
  virus products it should basically be based on the following Pattern:

  ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
  ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant name
  or specific feature'
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dct:title
close_mappings:
- rdfs:label
rank: 1000
alias: name
domain_of:
- DataService
- Catalogue
- Term
- PersonOrOrganization
- ProductOrService
- File
- ContactPoint
- License
- Certification
range: string
required: true
multivalued: false

```
</details>