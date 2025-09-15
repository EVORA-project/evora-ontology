

# Class: Originator (Originator) 


_The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample_





URI: [EVORAO:Originator](https://w3id.org/evorao/Originator)






```mermaid
 classDiagram
    class Originator
    click Originator href "../Originator"
      PersonOrOrganization <|-- Originator
        click PersonOrOrganization href "../PersonOrOrganization"
      
      Originator : contactPoint
        
          
    
    
    Originator --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Originator : description
        
      Originator : homePage
        
      Originator : keyword
        
      Originator : logo
        
          
    
    
    Originator --> "0..1" Image : logo
    click Image href "../Image"

        
      Originator : name
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * **Originator**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | [PersonOrOrganization](PersonOrOrganization.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [PersonOrOrganization](PersonOrOrganization.md) |
| [homePage](homePage.md) | 0..1 <br/> [Uri](Uri.md) | A web page that serves as the main or introductory page | [PersonOrOrganization](PersonOrOrganization.md) |
| [contactPoint](contactPoint.md) | 0..1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [PersonOrOrganization](PersonOrOrganization.md) |
| [logo](logo.md) | 0..1 <br/> [Image](Image.md) | A path or URL to the related logo | [PersonOrOrganization](PersonOrOrganization.md) |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Product](Product.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Antibody](Antibody.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Hybridoma](Hybridoma.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Protein](Protein.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [NucleicAcid](NucleicAcid.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [DetectionKit](DetectionKit.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Bundle](Bundle.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Pathogen](Pathogen.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Virus](Virus.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Bacterium](Bacterium.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Fungus](Fungus.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Protozoan](Protozoan.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Viroid](Viroid.md) | [originator](originator.md) | range | [Originator](Originator.md) |
| [Prion](Prion.md) | [originator](originator.md) | range | [Originator](Originator.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Originator |
| native | EVORAO:Originator |
| related | foaf:Organization, foaf:Agent, foaf:Organization, foaf:Agent |
| close | dct:ProvenanceStatement, dct:ProvenanceStatement |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Originator
description: The individual or organization responsible for the original discovery,
  isolation, or creation of an item, providing information about the source or origin
  of the sample
title: Originator
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:ProvenanceStatement
- dct:ProvenanceStatement
related_mappings:
- foaf:Organization
- foaf:Agent
- foaf:Organization
- foaf:Agent
is_a: PersonOrOrganization

```
</details>

### Induced

<details>
```yaml
name: Originator
description: The individual or organization responsible for the original discovery,
  isolation, or creation of an item, providing information about the source or origin
  of the sample
title: Originator
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:ProvenanceStatement
- dct:ProvenanceStatement
related_mappings:
- foaf:Organization
- foaf:Agent
- foaf:Organization
- foaf:Agent
is_a: PersonOrOrganization
attributes:
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
    owner: Originator
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
    owner: Originator
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
    owner: Originator
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
    owner: Originator
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
    owner: Originator
    domain_of:
    - PersonOrOrganization
    - License
    - Certification
    range: Image
    required: false
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: Originator
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true

```
</details>