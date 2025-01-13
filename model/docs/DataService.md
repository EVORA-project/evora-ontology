

# Class: DataService


_A collection of operations that provides access to one or more datasets or data processing functions_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [EVORA:DataService](https://evora-project.eu/DataService)






```mermaid
 classDiagram
    class DataService
    click DataService href "../DataService"
      Nameable <|-- DataService
        click Nameable href "../Nameable"
      

      DataService <|-- DataProvider
        click DataProvider href "../DataProvider"
      
      
      DataService : description
        
      DataService : name
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * **DataService**
        * [DataProvider](DataProvider.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |







## Aliases


* Data Service



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:DataService |
| native | EVORA:DataService |
| exact | dcat:DataService |
| close | wd:Q193424, schema:WebAPI |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataService
description: A collection of operations that provides access to one or more datasets
  or data processing functions
from_schema: https://evora-project.eu/
aliases:
- Data Service
exact_mappings:
- dcat:DataService
close_mappings:
- wd:Q193424
- schema:WebAPI
is_a: Nameable
abstract: true

```
</details>

### Induced

<details>
```yaml
name: DataService
description: A collection of operations that provides access to one or more datasets
  or data processing functions
from_schema: https://evora-project.eu/
aliases:
- Data Service
exact_mappings:
- dcat:DataService
close_mappings:
- wd:Q193424
- schema:WebAPI
is_a: Nameable
abstract: true
attributes:
  name:
    name: name
    description: The label that allows humans to identify the current item
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    aliases:
    - name
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: DataService
    domain_of:
    - Nameable
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the item.

      '
    from_schema: https://evora-project.eu/
    aliases:
    - description
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: DataService
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>