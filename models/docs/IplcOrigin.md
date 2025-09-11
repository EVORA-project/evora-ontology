

# Class: IPLC origin (IplcOrigin) 


_The IPLC area (Indigenous People and Local Communities) from which a physical item originates_





URI: [EVORAO:IplcOrigin](https://w3id.org/evorao/IplcOrigin)






```mermaid
 classDiagram
    class IplcOrigin
    click IplcOrigin href "../IplcOrigin"
      GeographicalOrigin <|-- IplcOrigin
        click GeographicalOrigin href "../GeographicalOrigin"
      
      IplcOrigin : description
        
      IplcOrigin : inVocabulary
        
          
    
    
    IplcOrigin --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      IplcOrigin : title
        
      IplcOrigin : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * [GeographicalOrigin](GeographicalOrigin.md)
            * **IplcOrigin**



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
| [NaturalPartOrigin](NaturalPartOrigin.md) | [indigenousPeopleAndLocalCommunityOrigin](indigenousPeopleAndLocalCommunityOrigin.md) | range | [IplcOrigin](IplcOrigin.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:IplcOrigin |
| native | EVORAO:IplcOrigin |
| related | dct:Location, vcard:Location, dct:Location, vcard:Location |
| close | ncit:C41152, mesh:D000081034, ncit:C41152, mesh:D000081034 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IplcOrigin
description: The IPLC area (Indigenous People and Local Communities) from which a
  physical item originates
title: IPLC origin
from_schema: https://w3id.org/evorao/
close_mappings:
- ncit:C41152
- mesh:D000081034
- ncit:C41152
- mesh:D000081034
related_mappings:
- dct:Location
- vcard:Location
- dct:Location
- vcard:Location
is_a: GeographicalOrigin

```
</details>

### Induced

<details>
```yaml
name: IplcOrigin
description: The IPLC area (Indigenous People and Local Communities) from which a
  physical item originates
title: IPLC origin
from_schema: https://w3id.org/evorao/
close_mappings:
- ncit:C41152
- mesh:D000081034
- ncit:C41152
- mesh:D000081034
related_mappings:
- dct:Location
- vcard:Location
- dct:Location
- vcard:Location
is_a: GeographicalOrigin
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
    owner: IplcOrigin
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
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: IplcOrigin
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
    owner: IplcOrigin
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
    owner: IplcOrigin
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>