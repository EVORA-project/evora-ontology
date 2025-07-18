

# Class: Data Service (DataService) 


_A collection of operations that provides access to one or more datasets or data processing functions_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [dcat:DataService](http://www.w3.org/ns/dcat#DataService)






```mermaid
 classDiagram
    class DataService
    click DataService href "../DataService"
      Resource <|-- DataService
        click Resource href "../Resource"
      

      DataService <|-- DataProvider
        click DataProvider href "../DataProvider"
      
      
      DataService : description
        
      DataService : endpointURL
        
      DataService : title
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **DataService**
        * [DataProvider](DataProvider.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | direct |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | direct |
| [endpointURL](endpointURL.md) | 1 <br/> [Uri](Uri.md) | The URL template that allows to get the content | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:DataService |
| native | EVORAO:DataService |
| close | wd:Q193424, schema:WebAPI, wd:Q193424, schema:WebAPI |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataService
description: A collection of operations that provides access to one or more datasets
  or data processing functions
title: Data Service
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q193424
- schema:WebAPI
- wd:Q193424
- schema:WebAPI
is_a: Resource
abstract: true
slots:
- title
- description
- endpointURL
slot_usage:
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
    close_mappings:
    - rdfs:label
    - schema:name
    slot_uri: dct:title
    domain_of:
    - DataService
    - Dataset
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
    exact_mappings:
    - schema:description
    slot_uri: dct:description
    domain_of:
    - DataService
    - Dataset
    - Term
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  endpointURL:
    name: endpointURL
    description: The URL template that allows to get the content
    title: endpoint URL
    close_mappings:
    - wdp:P1630
    slot_uri: dcat:endpointURL
    domain_of:
    - DataService
    range: uri
    required: true
    multivalued: false
class_uri: dcat:DataService

```
</details>

### Induced

<details>
```yaml
name: DataService
description: A collection of operations that provides access to one or more datasets
  or data processing functions
title: Data Service
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q193424
- schema:WebAPI
- wd:Q193424
- schema:WebAPI
is_a: Resource
abstract: true
slot_usage:
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
    close_mappings:
    - rdfs:label
    - schema:name
    slot_uri: dct:title
    domain_of:
    - DataService
    - Dataset
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
    exact_mappings:
    - schema:description
    slot_uri: dct:description
    domain_of:
    - DataService
    - Dataset
    - Term
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  endpointURL:
    name: endpointURL
    description: The URL template that allows to get the content
    title: endpoint URL
    close_mappings:
    - wdp:P1630
    slot_uri: dcat:endpointURL
    domain_of:
    - DataService
    range: uri
    required: true
    multivalued: false
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
    owner: DataService
    domain_of:
    - DataService
    - Dataset
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
    owner: DataService
    domain_of:
    - DataService
    - Dataset
    - Term
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  endpointURL:
    name: endpointURL
    description: The URL template that allows to get the content
    title: endpoint URL
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - wdp:P1630
    rank: 1000
    slot_uri: dcat:endpointURL
    alias: endpointURL
    owner: DataService
    domain_of:
    - DataService
    range: uri
    required: true
    multivalued: false
class_uri: dcat:DataService

```
</details>