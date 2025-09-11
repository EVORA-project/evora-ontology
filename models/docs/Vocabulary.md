

# Class: Vocabulary (Vocabulary) 


_A subset of words or phrases specific to a particular subject or field_





URI: [EVORAO:Vocabulary](https://w3id.org/evorao/Vocabulary)






```mermaid
 classDiagram
    class Vocabulary
    click Vocabulary href "../Vocabulary"
      Catalogue <|-- Vocabulary
        click Catalogue href "../Catalogue"
      
      Vocabulary : description
        
      Vocabulary : term
        
          
    
    
    Vocabulary --> "* _recommended_" Term : term
    click Term href "../Term"

        
      Vocabulary : termDataProvider
        
          
    
    
    Vocabulary --> "0..1" DataProvider : termDataProvider
    click DataProvider href "../DataProvider"

        
      Vocabulary : title
        
      Vocabulary : version
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Dataset](Dataset.md)
        * [Catalogue](Catalogue.md)
            * **Vocabulary**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [termDataProvider](termDataProvider.md) | 0..1 <br/> [DataProvider](DataProvider.md) | An external API or Endpoint that permits to retrieve the terms of this vocabu... | direct |
| [term](term.md) | * _recommended_ <br/> [Term](Term.md) | The terms related to this vocabulary | direct |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Dataset](Dataset.md) |
| [description](description.md) | 1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Dataset](Dataset.md) |
| [version](version.md) | 0..1 _recommended_ <br/> [String](String.md) | The version indicator (name or identifier) of a resource | [Dataset](Dataset.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Term](Term.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [CommonName](CommonName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [VirusName](VirusName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [AlternateName](AlternateName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [RiskGroup](RiskGroup.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Doi](Doi.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Journal](Journal.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PdbReference](PdbReference.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Keyword](Keyword.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [TagSequence](TagSequence.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [SpecialFeature](SpecialFeature.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ExpressionVector](ExpressionVector.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PlasmidSelection](PlasmidSelection.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PropagationHost](PropagationHost.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [TransmissionMethod](TransmissionMethod.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ProductionCellLine](ProductionCellLine.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ProductCategory](ProductCategory.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IsolationHost](IsolationHost.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [GeographicalOrigin](GeographicalOrigin.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IplcOrigin](IplcOrigin.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Country](Country.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IataClassification](IataClassification.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Variant](Variant.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [TaxonomicRank](TaxonomicRank.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Taxon](Taxon.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Vocabulary |
| native | EVORAO:Vocabulary |
| exact | sio:001080, sio:001080 |
| broad | skos:Collection, skos:Collection |
| related | t4fs:0000335, wd:Q6499736, t4fs:0000335, wd:Q6499736 |
| close | wd:Q1391494, wd:Q6537693, wd:Q8380731, wd:Q1391494, wd:Q6537693, wd:Q8380731 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vocabulary
description: A subset of words or phrases specific to a particular subject or field
title: Vocabulary
from_schema: https://w3id.org/evorao/
exact_mappings:
- sio:001080
- sio:001080
close_mappings:
- wd:Q1391494
- wd:Q6537693
- wd:Q8380731
- wd:Q1391494
- wd:Q6537693
- wd:Q8380731
related_mappings:
- t4fs:0000335
- wd:Q6499736
- t4fs:0000335
- wd:Q6499736
broad_mappings:
- skos:Collection
- skos:Collection
is_a: Catalogue
slots:
- termDataProvider
- term
slot_usage:
  termDataProvider:
    name: termDataProvider
    description: An external API or Endpoint that permits to retrieve the terms of
      this vocabulary
    title: term data provider
    domain_of:
    - Vocabulary
    range: DataProvider
    required: false
    multivalued: false
  term:
    name: term
    description: The terms related to this vocabulary
    title: term
    related_mappings:
    - dct:hasPart
    domain_of:
    - Vocabulary
    range: Term
    required: false
    recommended: true
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Vocabulary
description: A subset of words or phrases specific to a particular subject or field
title: Vocabulary
from_schema: https://w3id.org/evorao/
exact_mappings:
- sio:001080
- sio:001080
close_mappings:
- wd:Q1391494
- wd:Q6537693
- wd:Q8380731
- wd:Q1391494
- wd:Q6537693
- wd:Q8380731
related_mappings:
- t4fs:0000335
- wd:Q6499736
- t4fs:0000335
- wd:Q6499736
broad_mappings:
- skos:Collection
- skos:Collection
is_a: Catalogue
slot_usage:
  termDataProvider:
    name: termDataProvider
    description: An external API or Endpoint that permits to retrieve the terms of
      this vocabulary
    title: term data provider
    domain_of:
    - Vocabulary
    range: DataProvider
    required: false
    multivalued: false
  term:
    name: term
    description: The terms related to this vocabulary
    title: term
    related_mappings:
    - dct:hasPart
    domain_of:
    - Vocabulary
    range: Term
    required: false
    recommended: true
    multivalued: true
attributes:
  termDataProvider:
    name: termDataProvider
    description: An external API or Endpoint that permits to retrieve the terms of
      this vocabulary
    title: term data provider
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: termDataProvider
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: DataProvider
    required: false
    multivalued: false
  term:
    name: term
    description: The terms related to this vocabulary
    title: term
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - dct:hasPart
    rank: 1000
    alias: term
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: Term
    required: false
    recommended: true
    multivalued: true
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern: ''Virus
      name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:name
    - rdfs:label
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: Vocabulary
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
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    title: description
    comments:
    - Describe this item in few lines. This description will serve as a summary to
      present the resource.
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:description
    close_mappings:
    - schema:description
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Vocabulary
    domain_of:
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: true
    recommended: true
    multivalued: false
  version:
    name: version
    description: The version indicator (name or identifier) of a resource
    title: version
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - pav:version
    close_mappings:
    - wdp:P393
    - schema:version
    related_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dcat:version
    alias: version
    owner: Vocabulary
    domain_of:
    - Dataset
    - Version
    - Taxonomy
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>