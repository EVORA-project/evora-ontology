

# Class: Catalogue (Catalogue) 


_A curated collection of metadata about resources_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [dcat:Catalog](http://www.w3.org/ns/dcat#Catalog)






```mermaid
 classDiagram
    class Catalogue
    click Catalogue href "../Catalogue"
      Dataset <|-- Catalogue
        click Dataset href "../Dataset"
      

      Catalogue <|-- Taxonomy
        click Taxonomy href "../Taxonomy"
      Catalogue <|-- Vocabulary
        click Vocabulary href "../Vocabulary"
      Catalogue <|-- Collection
        click Collection href "../Collection"
      
      
      Catalogue : description
        
      Catalogue : title
        
      Catalogue : version
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Dataset](Dataset.md)
        * **Catalogue**
            * [Taxonomy](Taxonomy.md)
            * [Vocabulary](Vocabulary.md)
            * [Collection](Collection.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Dataset](Dataset.md) |
| [description](description.md) | 1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Dataset](Dataset.md) |
| [version](version.md) | 0..1 _recommended_ <br/> [String](String.md) | The version indicator (name or identifier) of a resource | [Dataset](Dataset.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Catalog |
| native | EVORAO:Catalogue |
| exact | schema:DataCatalog, schema:DataCatalog |
| close | wd:Q2352616, wd:Q2352616 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Catalogue
description: A curated collection of metadata about resources
title: Catalogue
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:DataCatalog
- schema:DataCatalog
close_mappings:
- wd:Q2352616
- wd:Q2352616
is_a: Dataset
abstract: true
class_uri: dcat:Catalog

```
</details>

### Induced

<details>
```yaml
name: Catalogue
description: A curated collection of metadata about resources
title: Catalogue
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:DataCatalog
- schema:DataCatalog
close_mappings:
- wd:Q2352616
- wd:Q2352616
is_a: Dataset
abstract: true
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
    owner: Catalogue
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
    owner: Catalogue
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
    close_mappings:
    - wdp:P393
    - schema:version
    rank: 1000
    slot_uri: dcat:version
    alias: version
    owner: Catalogue
    domain_of:
    - Dataset
    - Version
    - Taxonomy
    range: string
    required: false
    recommended: true
    multivalued: false
class_uri: dcat:Catalog

```
</details>