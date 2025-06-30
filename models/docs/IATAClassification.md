

# Class: IATA classification (IATAClassification) 


_The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air_





URI: [EVORAO:IATAClassification](https://w3id.org/evorao/IATAClassification)






```mermaid
 classDiagram
    class IATAClassification
    click IATAClassification href "../IATAClassification"
      Term <|-- IATAClassification
        click Term href "../Term"
      
      IATAClassification : description
        
      IATAClassification : inVocabulary
        
          
    
    
    IATAClassification --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      IATAClassification : title
        
      IATAClassification : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **IATAClassification**



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
| [Product](Product.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Antibody](Antibody.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Hybridoma](Hybridoma.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Protein](Protein.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [NucleicAcid](NucleicAcid.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [DetectionKit](DetectionKit.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Bundle](Bundle.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Pathogen](Pathogen.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Virus](Virus.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Bacterium](Bacterium.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Fungus](Fungus.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Protozoan](Protozoan.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Viroid](Viroid.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |
| [Prion](Prion.md) | [hasIATAClassification](hasIATAClassification.md) | range | [IATAClassification](IATAClassification.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:IATAClassification |
| native | EVORAO:IATAClassification |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IATAClassification
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
name: IATAClassification
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
    owner: IATAClassification
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
    owner: IATAClassification
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
    owner: IATAClassification
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
    owner: IATAClassification
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>