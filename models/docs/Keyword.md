

# Class: Keyword (Keyword) 


_A term or phrase used to tag and categorize content_





URI: [EVORAO:Keyword](https://w3id.org/evorao/Keyword)






```mermaid
 classDiagram
    class Keyword
    click Keyword href "../Keyword"
      Term <|-- Keyword
        click Term href "../Term"
      
      Keyword : description
        
      Keyword : inVocabulary
        
          
    
    
    Keyword --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Keyword : keyword
        
      Keyword : title
        
      Keyword : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **Keyword**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProductOrService](ProductOrService.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Service](Service.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Product](Product.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Antibody](Antibody.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Hybridoma](Hybridoma.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Protein](Protein.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [NucleicAcid](NucleicAcid.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [DetectionKit](DetectionKit.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Bundle](Bundle.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Pathogen](Pathogen.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Virus](Virus.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Bacterium](Bacterium.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Fungus](Fungus.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Protozoan](Protozoan.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Viroid](Viroid.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |
| [Prion](Prion.md) | [keywords](keywords.md) | range | [Keyword](Keyword.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Keyword |
| native | EVORAO:Keyword |
| exact | wd:Q1128340, sio:000147, edam:0968, schema:DefinedTerm, wd:Q1128340, sio:000147, edam:0968, schema:DefinedTerm |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Keyword
description: A term or phrase used to tag and categorize content
title: Keyword
from_schema: https://w3id.org/evorao/
exact_mappings:
- wd:Q1128340
- sio:000147
- edam:0968
- schema:DefinedTerm
- wd:Q1128340
- sio:000147
- edam:0968
- schema:DefinedTerm
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: Keyword
description: A term or phrase used to tag and categorize content
title: Keyword
from_schema: https://w3id.org/evorao/
exact_mappings:
- wd:Q1128340
- sio:000147
- edam:0968
- schema:DefinedTerm
- wd:Q1128340
- sio:000147
- edam:0968
- schema:DefinedTerm
is_a: Term
attributes:
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
    owner: Keyword
    domain_of:
    - Term
    - Dataset
    - DataService
    - Publication
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
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Keyword
    domain_of:
    - Term
    - Dataset
    - DataService
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0
    title: weight
    comments:
    - The lowest weighted Data providers are triggered first, this may be usefull
      to populate at first entities that are referenced by others (e.g. Version ahead
      of Rank ahead of Taxon)
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: Keyword
    domain_of:
    - Term
    - DataProvider
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary
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
    owner: Keyword
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: Keyword
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true

```
</details>