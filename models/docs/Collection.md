

# Class: Collection (Collection)


_Set of products and services with some common characteristics_





URI: [EVORA:Collection](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Collection)






```mermaid
 classDiagram
    class Collection
    click Collection href "../Collection"
      Catalogue <|-- Collection
        click Catalogue href "../Catalogue"
      
      Collection : collectionDataProvider
        
          
    
    
    Collection --> "0..1" DataProvider : collectionDataProvider
    click DataProvider href "../DataProvider"

        
      Collection : collectionItem
        
          
    
    
    Collection --> "*" ProductOrService : collectionItem
    click ProductOrService href "../ProductOrService"

        
      Collection : description
        
      Collection : name
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [Catalogue](Catalogue.md)
        * **Collection**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [collectionItem](collectionItem.md) | * <br/> [ProductOrService](ProductOrService.md) | An item of the collection | direct |
| [collectionDataProvider](collectionDataProvider.md) | 0..1 <br/> [DataProvider](DataProvider.md) | The provider of the data of the collection | direct |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProductOrService](ProductOrService.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Service](Service.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Product](Product.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Antibody](Antibody.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Hybridoma](Hybridoma.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Protein](Protein.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [NucleicAcid](NucleicAcid.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [DetectionKit](DetectionKit.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Bundle](Bundle.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Pathogen](Pathogen.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Virus](Virus.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Bacterium](Bacterium.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Fungus](Fungus.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Protozoan](Protozoan.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Viroid](Viroid.md) | [collection](collection.md) | range | [Collection](Collection.md) |
| [Prion](Prion.md) | [collection](collection.md) | range | [Collection](Collection.md) |




## Aliases


* collection



## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Collection |
| native | EVORA:Collection |
| close | wd:Q2668072 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Collection
description: Set of products and services with some common characteristics
title: Collection
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
aliases:
- collection
close_mappings:
- wd:Q2668072
is_a: Catalogue
slots:
- collectionItem
- collectionDataProvider
slot_usage:
  collectionItem:
    name: collectionItem
    description: An item of the collection
    title: collection item
    close_mappings:
    - dcat:resource
    range: ProductOrService
    required: false
    multivalued: true
  collectionDataProvider:
    name: collectionDataProvider
    description: The provider of the data of the collection
    title: collection data provider
    close_mappings:
    - dct:isReferencedBy
    range: DataProvider
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Collection
description: Set of products and services with some common characteristics
title: Collection
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
aliases:
- collection
close_mappings:
- wd:Q2668072
is_a: Catalogue
slot_usage:
  collectionItem:
    name: collectionItem
    description: An item of the collection
    title: collection item
    close_mappings:
    - dcat:resource
    range: ProductOrService
    required: false
    multivalued: true
  collectionDataProvider:
    name: collectionDataProvider
    description: The provider of the data of the collection
    title: collection data provider
    close_mappings:
    - dct:isReferencedBy
    range: DataProvider
    required: false
    multivalued: false
attributes:
  collectionItem:
    name: collectionItem
    description: An item of the collection
    title: collection item
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dcat:resource
    rank: 1000
    alias: collectionItem
    owner: Collection
    domain_of:
    - Collection
    range: ProductOrService
    required: false
    multivalued: true
  collectionDataProvider:
    name: collectionDataProvider
    description: The provider of the data of the collection
    title: collection data provider
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:isReferencedBy
    rank: 1000
    alias: collectionDataProvider
    owner: Collection
    domain_of:
    - Collection
    range: DataProvider
    required: false
    multivalued: false
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Collection
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Collection
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>