

# Class: Person (Person) 


_An individual_





URI: [foaf:Person](http://xmlns.com/foaf/0.1/Person)






```mermaid
 classDiagram
    class Person
    click Person href "../Person"
      PersonOrOrganization <|-- Person
        click PersonOrOrganization href "../PersonOrOrganization"
      
      Person : contactPoint
        
          
    
    
    Person --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Person : description
        
      Person : homePage
        
      Person : logo
        
          
    
    
    Person --> "0..1" Image : logo
    click Image href "../Image"

        
      Person : name
        
      Person : orcidId
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * **Person**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [orcidId](orcidId.md) | 0..1 _recommended_ <br/> [String](String.md) | Unique persistent identifier for a person, provided by the Open Researcher an... | direct |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | [PersonOrOrganization](PersonOrOrganization.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [PersonOrOrganization](PersonOrOrganization.md) |
| [homePage](homePage.md) | 0..1 <br/> [Uri](Uri.md) | A web page that serves as the main or introductory page | [PersonOrOrganization](PersonOrOrganization.md) |
| [contactPoint](contactPoint.md) | 0..1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [PersonOrOrganization](PersonOrOrganization.md) |
| [logo](logo.md) | 0..1 <br/> [Image](Image.md) | A path or URL to the related logo | [PersonOrOrganization](PersonOrOrganization.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Person |
| native | EVORAO:Person |
| exact | schema:Person, schema:Person |
| close | wd:Q215627, vcard:Individual, wd:Q215627, vcard:Individual |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
description: An individual
title: Person
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:Person
- schema:Person
close_mappings:
- wd:Q215627
- vcard:Individual
- wd:Q215627
- vcard:Individual
is_a: PersonOrOrganization
slots:
- orcidId
slot_usage:
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    exact_mappings:
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
    domain_of:
    - Person
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
class_uri: foaf:Person

```
</details>

### Induced

<details>
```yaml
name: Person
description: An individual
title: Person
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:Person
- schema:Person
close_mappings:
- wd:Q215627
- vcard:Individual
- wd:Q215627
- vcard:Individual
is_a: PersonOrOrganization
slot_usage:
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    exact_mappings:
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
    domain_of:
    - Person
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
    rank: 1000
    alias: orcidId
    owner: Person
    domain_of:
    - Person
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  name:
    name: name
    description: A word or set of words used to identify and refer to an entity
    title: name
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:name
    - vcard:fn
    close_mappings:
    - rdfs:label
    - dct:title
    rank: 1000
    slot_uri: foaf:name
    alias: name
    owner: Person
    domain_of:
    - PersonOrOrganization
    - File
    - ContactPoint
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
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Person
    domain_of:
    - PersonOrOrganization
    - Dataset
    - DataService
    - Term
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  homePage:
    name: homePage
    description: A web page that serves as the main or introductory page
    title: home page
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - swo:0004006
    rank: 1000
    slot_uri: foaf:homepage
    alias: homePage
    owner: Person
    domain_of:
    - PersonOrOrganization
    range: uri
    required: false
    multivalued: false
  contactPoint:
    name: contactPoint
    description: An information that allows someone to establish communication
    title: contact point
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:contactPoint
    rank: 1000
    slot_uri: dcat:contactPoint
    alias: contactPoint
    owner: Person
    domain_of:
    - PersonOrOrganization
    - ProductOrService
    range: ContactPoint
    required: false
    recommended: true
    multivalued: false
  logo:
    name: logo
    description: A path or URL to the related logo
    title: logo
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:logo
    rank: 1000
    alias: logo
    owner: Person
    domain_of:
    - PersonOrOrganization
    - License
    - Certification
    range: Image
    required: false
    multivalued: false
class_uri: foaf:Person

```
</details>