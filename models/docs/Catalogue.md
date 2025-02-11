

# Class: Catalogue (Catalogue)


_A curated collection of metadata about resources_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [EVORAO:Catalogue](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Catalogue)






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
        
      Catalogue : name
        
      
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
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | direct |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Catalogue |
| native | EVORAO:Catalogue |
| exact | dcat:Catalog, dcat:Catalog |
| close | wd:Q2352616, schema:Dataset, wd:Q2352616, schema:Dataset |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Catalogue
description: A curated collection of metadata about resources
title: Catalogue
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Catalog
- dcat:Catalog
close_mappings:
- wd:Q2352616
- schema:Dataset
- wd:Q2352616
- schema:Dataset
is_a: Dataset
abstract: true
slots:
- name
- description
slot_usage:
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
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
      present the item.

      '
    exact_mappings:
    - dct:description
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Catalogue
description: A curated collection of metadata about resources
title: Catalogue
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Catalog
- dcat:Catalog
close_mappings:
- wd:Q2352616
- schema:Dataset
- wd:Q2352616
- schema:Dataset
is_a: Dataset
abstract: true
slot_usage:
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
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
      present the item.

      '
    exact_mappings:
    - dct:description
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Catalogue
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
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
      present the item.

      '
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Catalogue
    domain_of:
    - Catalogue
    - DataService
    - Term
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>