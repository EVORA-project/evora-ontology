

# Class: IPLC origin (IPLCOrigin) 


_The IPLC area (Indigenous People and Local Communities) from which a physical item originates_





URI: [EVORAO:IPLCOrigin](https://w3id.org/evorao/IPLCOrigin)






```mermaid
 classDiagram
    class IPLCOrigin
    click IPLCOrigin href "../IPLCOrigin"
      GeographicalOrigin <|-- IPLCOrigin
        click GeographicalOrigin href "../GeographicalOrigin"
      
      IPLCOrigin : description
        
      IPLCOrigin : inVocabulary
        
          
    
    
    IPLCOrigin --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      IPLCOrigin : title
        
      IPLCOrigin : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * [GeographicalOrigin](GeographicalOrigin.md)
            * **IPLCOrigin**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NaturalPartOrigin](NaturalPartOrigin.md) | [indigenousPoepleAndLocalCommunityOrigin](indigenousPoepleAndLocalCommunityOrigin.md) | range | [IPLCOrigin](IPLCOrigin.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:IPLCOrigin |
| native | EVORAO:IPLCOrigin |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IPLCOrigin
description: The IPLC area (Indigenous People and Local Communities) from which a
  physical item originates
title: IPLC origin
from_schema: https://w3id.org/evorao/
is_a: GeographicalOrigin

```
</details>

### Induced

<details>
```yaml
name: IPLCOrigin
description: The IPLC area (Indigenous People and Local Communities) from which a
  physical item originates
title: IPLC origin
from_schema: https://w3id.org/evorao/
is_a: GeographicalOrigin
attributes:
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - rdfs:label
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: IPLCOrigin
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
    - 'Describe this item in few lines. This description will serve as a summary to
      present the resource.

      '
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: IPLCOrigin
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
    owner: IPLCOrigin
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
    rank: 1000
    alias: inVocabulary
    owner: IPLCOrigin
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>