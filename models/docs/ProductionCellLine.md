

# Class: Production cell line (ProductionCellLine) 


_A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances_





URI: [EVORAO:ProductionCellLine](https://w3id.org/evorao/ProductionCellLine)






```mermaid
 classDiagram
    class ProductionCellLine
    click ProductionCellLine href "../ProductionCellLine"
      Term <|-- ProductionCellLine
        click Term href "../Term"
      
      ProductionCellLine : description
        
      ProductionCellLine : inVocabulary
        
          
    
    
    ProductionCellLine --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      ProductionCellLine : title
        
      ProductionCellLine : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **ProductionCellLine**



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
| [Pathogen](Pathogen.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Virus](Virus.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Bacterium](Bacterium.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Fungus](Fungus.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Protozoan](Protozoan.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Viroid](Viroid.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |
| [Prion](Prion.md) | [productionCellLine](productionCellLine.md) | range | [ProductionCellLine](ProductionCellLine.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:ProductionCellLine |
| native | EVORAO:ProductionCellLine |
| close | wd:Q21014462, wd:Q21014462 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProductionCellLine
description: A population of cells that originates from a primary culture, adapted
  to grow and divide under laboratory conditions. Used in biotechnology to consistently
  produce biological substances
title: Production cell line
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q21014462
- wd:Q21014462
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: ProductionCellLine
description: A population of cells that originates from a primary culture, adapted
  to grow and divide under laboratory conditions. Used in biotechnology to consistently
  produce biological substances
title: Production cell line
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q21014462
- wd:Q21014462
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
    owner: ProductionCellLine
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
    owner: ProductionCellLine
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
    owner: ProductionCellLine
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
    owner: ProductionCellLine
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>