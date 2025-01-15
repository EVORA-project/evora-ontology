

# Class: Vocabulary (Vocabulary)


_A subset of words or phrases specific to a particular subject or field_





URI: [EVORA:Vocabulary](https://evora-project.eu/Vocabulary)






```mermaid
 classDiagram
    class Vocabulary
    click Vocabulary href "../Vocabulary"
      Catalogue <|-- Vocabulary
        click Catalogue href "../Catalogue"
      
      Vocabulary : description
        
      Vocabulary : name
        
      Vocabulary : term
        
          
    
    
    Vocabulary --> "*" Term : term
    click Term href "../Term"

        
      Vocabulary : termDataProvider
        
          
    
    
    Vocabulary --> "0..1" DataProvider : termDataProvider
    click DataProvider href "../DataProvider"

        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [Catalogue](Catalogue.md)
        * **Vocabulary**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [termDataProvider](termDataProvider.md) | 0..1 <br/> [DataProvider](DataProvider.md) | An external API or Endpoint that permits to retrieve the terms of this vocabu... | direct |
| [term](term.md) | * <br/> [Term](Term.md) | The terms related to this vocabulary | direct |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Term](Term.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [CommonName](CommonName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [VirusName](VirusName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [AlternateName](AlternateName.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [RiskGroup](RiskGroup.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [DOI](DOI.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Journal](Journal.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PDBReference](PDBReference.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Keyword](Keyword.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ProteinTag](ProteinTag.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [SpecialFeature](SpecialFeature.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ExpressionVector](ExpressionVector.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PlasmidSelection](PlasmidSelection.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [PropagationHost](PropagationHost.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [TransmissionMethod](TransmissionMethod.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ProductionCellLine](ProductionCellLine.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [ProductCategory](ProductCategory.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IsolationHost](IsolationHost.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [GeographicalOrigin](GeographicalOrigin.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IPLCOrigin](IPLCOrigin.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Country](Country.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [IATAClassification](IATAClassification.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Variant](Variant.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [TaxonomicRank](TaxonomicRank.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |
| [Taxon](Taxon.md) | [inVocabulary](inVocabulary.md) | range | [Vocabulary](Vocabulary.md) |




## Aliases


* vocabulary



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Vocabulary |
| native | EVORA:Vocabulary |
| close | wd:Q6499736, skos:Collection |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vocabulary
description: A subset of words or phrases specific to a particular subject or field
title: Vocabulary
from_schema: https://evora-project.eu/
aliases:
- vocabulary
close_mappings:
- wd:Q6499736
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
    range: DataProvider
    required: false
    multivalued: false
  term:
    name: term
    description: The terms related to this vocabulary
    title: term
    range: Term
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Vocabulary
description: A subset of words or phrases specific to a particular subject or field
title: Vocabulary
from_schema: https://evora-project.eu/
aliases:
- vocabulary
close_mappings:
- wd:Q6499736
- skos:Collection
is_a: Catalogue
slot_usage:
  termDataProvider:
    name: termDataProvider
    description: An external API or Endpoint that permits to retrieve the terms of
      this vocabulary
    title: term data provider
    range: DataProvider
    required: false
    multivalued: false
  term:
    name: term
    description: The terms related to this vocabulary
    title: term
    range: Term
    required: false
    multivalued: true
attributes:
  termDataProvider:
    name: termDataProvider
    description: An external API or Endpoint that permits to retrieve the terms of
      this vocabulary
    title: term data provider
    from_schema: https://evora-project.eu/
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
    from_schema: https://evora-project.eu/
    rank: 1000
    alias: term
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: Term
    required: false
    multivalued: true
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Vocabulary
    domain_of:
    - Nameable
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    title: description
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the item.

      '
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Vocabulary
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>