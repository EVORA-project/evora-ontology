

# Class: IATA classification (IataClassification) 


_The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air_





URI: [EVORAO:IataClassification](https://w3id.org/evorao/IataClassification)






```mermaid
 classDiagram
    class IataClassification
    click IataClassification href "../IataClassification"
      Term <|-- IataClassification
        click Term href "../Term"
      
      IataClassification : description
        
      IataClassification : inVocabulary
        
          
    
    
    IataClassification --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      IataClassification : title
        
      IataClassification : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **IataClassification**



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
| [Product](Product.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Antibody](Antibody.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Hybridoma](Hybridoma.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Protein](Protein.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [NucleicAcid](NucleicAcid.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [DetectionKit](DetectionKit.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Bundle](Bundle.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Pathogen](Pathogen.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Virus](Virus.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Bacterium](Bacterium.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Fungus](Fungus.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Protozoan](Protozoan.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Viroid](Viroid.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Prion](Prion.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:IataClassification |
| native | EVORAO:IataClassification |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IataClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for dangerous goods that are transported by air
title: IATA classification
from_schema: https://w3id.org/evorao/
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: IataClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for dangerous goods that are transported by air
title: IATA classification
from_schema: https://w3id.org/evorao/
is_a: Term
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
    - schema:name
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: IataClassification
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
    exact_mappings:
    - schema:description
    close_mappings:
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>