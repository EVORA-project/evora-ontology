

# Class: Data provider (DataProvider)


_An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources_





URI: [EVORAO:DataProvider](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#DataProvider)






```mermaid
 classDiagram
    class DataProvider
    click DataProvider href "../DataProvider"
      DataService <|-- DataProvider
        click DataService href "../DataService"
      
      DataProvider : contentType
        
      DataProvider : description
        
      DataProvider : license
        
          
    
    
    DataProvider --> "0..1" License : license
    click License href "../License"

        
      DataProvider : loginRequestMethod
        
      DataProvider : loginTokenName
        
      DataProvider : loginURL
        
      DataProvider : name
        
      DataProvider : providedEntityType
        
          
    
    
    DataProvider --> "1" Dataset : providedEntityType
    click Dataset href "../Dataset"

        
      DataProvider : queryMethod
        
      DataProvider : queryURL
        
      DataProvider : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [DataService](DataService.md)
        * **DataProvider**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [license](license.md) | 0..1 <br/> [License](License.md) | Information about terms and conditions under which the subject can be used, s... | direct |
| [loginRequestMethod](loginRequestMethod.md) | 0..1 <br/> [String](String.md) | The http request method used to acces the login request url | direct |
| [loginURL](loginURL.md) | 0..1 <br/> [Uri](Uri.md) | The URL template that allows to log in if required | direct |
| [loginTokenName](loginTokenName.md) | 0..1 <br/> [String](String.md) | The name of the token, unique identifier of an interaction session, that will... | direct |
| [queryURL](queryURL.md) | 1 <br/> [Uri](Uri.md) | The URL template that allows to get the content | direct |
| [queryMethod](queryMethod.md) | 1 <br/> [String](String.md) | The http request method used to access the requested query url | direct |
| [contentType](contentType.md) | 1 <br/> [String](String.md) | The content type of the response to the queries | direct |
| [providedEntityType](providedEntityType.md) | 1 <br/> [Dataset](Dataset.md) | The identification of the entity type (Class) described by the response to th... | direct |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | direct |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [DataService](DataService.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [DataService](DataService.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Taxonomy](Taxonomy.md) | [taxonDataProvider](taxonDataProvider.md) | range | [DataProvider](DataProvider.md) |
| [Taxonomy](Taxonomy.md) | [versionDataProvider](versionDataProvider.md) | range | [DataProvider](DataProvider.md) |
| [Taxonomy](Taxonomy.md) | [rankDataProvider](rankDataProvider.md) | range | [DataProvider](DataProvider.md) |
| [Vocabulary](Vocabulary.md) | [termDataProvider](termDataProvider.md) | range | [DataProvider](DataProvider.md) |
| [Collection](Collection.md) | [collectionDataProvider](collectionDataProvider.md) | range | [DataProvider](DataProvider.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:DataProvider |
| native | EVORAO:DataProvider |
| close | wd:Q122625839, wd:Q122625839 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataProvider
description: An external API (Application Programming Interface) or Endpoint that
  permits to retrieve data from other sources
title: Data provider
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q122625839
- wd:Q122625839
is_a: DataService
slots:
- license
- loginRequestMethod
- loginURL
- loginTokenName
- queryURL
- queryMethod
- contentType
- providedEntityType
- weight
slot_usage:
  license:
    name: license
    description: Information about terms and conditions under which the subject can
      be used, shared, or distributed, indicating any restrictions or permissions
    title: license
    exact_mappings:
    - dct:license
    domain_of:
    - DataProvider
    - File
    range: License
    required: false
    multivalued: false
  loginRequestMethod:
    name: loginRequestMethod
    description: The http request method used to acces the login request url
    title: login request method
    close_mappings:
    - dcat:endpointDescription
    ifabsent: string(GET)
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
  loginURL:
    name: loginURL
    description: The URL template that allows to log in if required
    title: login URL
    close_mappings:
    - wdp:P1630
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: uri
    required: false
    multivalued: false
  loginTokenName:
    name: loginTokenName
    description: The name of the token, unique identifier of an interaction session,
      that will have to be reused as credential in the query
    title: login token name
    close_mappings:
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
  queryURL:
    name: queryURL
    description: The URL template that allows to get the content
    title: query URL
    exact_mappings:
    - dcat:endpointURL
    close_mappings:
    - wdp:P1630
    domain_of:
    - DataProvider
    range: uri
    required: true
    multivalued: false
  queryMethod:
    name: queryMethod
    description: The http request method used to access the requested query url
    title: query method
    close_mappings:
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
  contentType:
    name: contentType
    description: The content type of the response to the queries
    title: content type
    close_mappings:
    - dct:format
    ifabsent: string(JSON)
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
  providedEntityType:
    name: providedEntityType
    description: The identification of the entity type (Class) described by the response
      to the query
    title: provided entity type
    exact_mappings:
    - dcat:servesDataset
    domain_of:
    - DataProvider
    range: Dataset
    required: true
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
    close_mappings:
    - adms:status
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: DataProvider
description: An external API (Application Programming Interface) or Endpoint that
  permits to retrieve data from other sources
title: Data provider
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q122625839
- wd:Q122625839
is_a: DataService
slot_usage:
  license:
    name: license
    description: Information about terms and conditions under which the subject can
      be used, shared, or distributed, indicating any restrictions or permissions
    title: license
    exact_mappings:
    - dct:license
    domain_of:
    - DataProvider
    - File
    range: License
    required: false
    multivalued: false
  loginRequestMethod:
    name: loginRequestMethod
    description: The http request method used to acces the login request url
    title: login request method
    close_mappings:
    - dcat:endpointDescription
    ifabsent: string(GET)
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
  loginURL:
    name: loginURL
    description: The URL template that allows to log in if required
    title: login URL
    close_mappings:
    - wdp:P1630
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: uri
    required: false
    multivalued: false
  loginTokenName:
    name: loginTokenName
    description: The name of the token, unique identifier of an interaction session,
      that will have to be reused as credential in the query
    title: login token name
    close_mappings:
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
  queryURL:
    name: queryURL
    description: The URL template that allows to get the content
    title: query URL
    exact_mappings:
    - dcat:endpointURL
    close_mappings:
    - wdp:P1630
    domain_of:
    - DataProvider
    range: uri
    required: true
    multivalued: false
  queryMethod:
    name: queryMethod
    description: The http request method used to access the requested query url
    title: query method
    close_mappings:
    - dcat:endpointDescription
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
  contentType:
    name: contentType
    description: The content type of the response to the queries
    title: content type
    close_mappings:
    - dct:format
    ifabsent: string(JSON)
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
  providedEntityType:
    name: providedEntityType
    description: The identification of the entity type (Class) described by the response
      to the query
    title: provided entity type
    exact_mappings:
    - dcat:servesDataset
    domain_of:
    - DataProvider
    range: Dataset
    required: true
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
    close_mappings:
    - adms:status
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false
attributes:
  license:
    name: license
    description: Information about terms and conditions under which the subject can
      be used, shared, or distributed, indicating any restrictions or permissions
    title: license
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:license
    rank: 1000
    alias: license
    owner: DataProvider
    domain_of:
    - DataProvider
    - File
    range: License
    required: false
    multivalued: false
  loginRequestMethod:
    name: loginRequestMethod
    description: The http request method used to acces the login request url
    title: login request method
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dcat:endpointDescription
    rank: 1000
    ifabsent: string(GET)
    alias: loginRequestMethod
    owner: DataProvider
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
    equals_string_in:
    - GET
    - POST
  loginURL:
    name: loginURL
    description: The URL template that allows to log in if required
    title: login URL
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P1630
    - dcat:endpointDescription
    rank: 1000
    alias: loginURL
    owner: DataProvider
    domain_of:
    - DataProvider
    range: uri
    required: false
    multivalued: false
  loginTokenName:
    name: loginTokenName
    description: The name of the token, unique identifier of an interaction session,
      that will have to be reused as credential in the query
    title: login token name
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dcat:endpointDescription
    rank: 1000
    alias: loginTokenName
    owner: DataProvider
    domain_of:
    - DataProvider
    range: string
    required: false
    multivalued: false
  queryURL:
    name: queryURL
    description: The URL template that allows to get the content
    title: query URL
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:endpointURL
    close_mappings:
    - wdp:P1630
    rank: 1000
    alias: queryURL
    owner: DataProvider
    domain_of:
    - DataProvider
    range: uri
    required: true
    multivalued: false
  queryMethod:
    name: queryMethod
    description: The http request method used to access the requested query url
    title: query method
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dcat:endpointDescription
    rank: 1000
    alias: queryMethod
    owner: DataProvider
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
    equals_string_in:
    - GET
    - POST
  contentType:
    name: contentType
    description: The content type of the response to the queries
    title: content type
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:format
    rank: 1000
    ifabsent: string(JSON)
    alias: contentType
    owner: DataProvider
    domain_of:
    - DataProvider
    range: string
    required: true
    multivalued: false
  providedEntityType:
    name: providedEntityType
    description: The identification of the entity type (Class) described by the response
      to the query
    title: provided entity type
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:servesDataset
    rank: 1000
    alias: providedEntityType
    owner: DataProvider
    domain_of:
    - DataProvider
    range: Dataset
    required: true
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: DataProvider
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false
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
    owner: DataProvider
    domain_of:
    - DataService
    - Catalogue
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
    owner: DataProvider
    domain_of:
    - DataService
    - Catalogue
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