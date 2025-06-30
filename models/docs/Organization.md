

# Class: Organization (Organization) 


_A social entity established to meet needs or pursue specific goals_





URI: [foaf:Organization](http://xmlns.com/foaf/0.1/Organization)






```mermaid
 classDiagram
    class Organization
    click Organization href "../Organization"
      PersonOrOrganization <|-- Organization
        click PersonOrOrganization href "../PersonOrOrganization"
      

      Organization <|-- RI
        click RI href "../RI"
      Organization <|-- Provider
        click Provider href "../Provider"
      
      
      Organization : alternateName
        
          
    
    
    Organization --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      Organization : contactPoint
        
          
    
    
    Organization --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Organization : country
        
          
    
    
    Organization --> "0..1 _recommended_" Country : country
    click Country href "../Country"

        
      Organization : description
        
      Organization : homePage
        
      Organization : logo
        
          
    
    
    Organization --> "0..1" Image : logo
    click Image href "../Image"

        
      Organization : name
        
      Organization : rORiD
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * **Organization**
            * [RI](RI.md)
            * [Provider](Provider.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any other name under which the entity can be known | direct |
| [country](country.md) | 0..1 _recommended_ <br/> [Country](Country.md) | The country of the organization | direct |
| [rORiD](rORiD.md) | 0..1 _recommended_ <br/> [String](String.md) | The corresponding organization's persistent identifier from the Research Orga... | direct |
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
| self | foaf:Organization |
| native | EVORAO:Organization |
| close | wd:Q43229, vcard:Organization, wd:Q43229, vcard:Organization |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: A social entity established to meet needs or pursue specific goals
title: Organization
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q43229
- vcard:Organization
- wd:Q43229
- vcard:Organization
is_a: PersonOrOrganization
slots:
- alternateName
- country
- rORiD
slot_usage:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    close_mappings:
    - wdp:P4970
    - schema:alternateName
    domain_of:
    - Organization
    - CommonName
    - AlternateName
    range: AlternateName
    required: false
    multivalued: true
  country:
    name: country
    description: The country of the organization
    title: country
    domain_of:
    - Organization
    range: Country
    required: false
    recommended: true
    multivalued: false
  rORiD:
    name: rORiD
    description: The corresponding organization's persistent identifier from the Research
      Organization Registry (ROR)
    title: ROR iD
    exact_mappings:
    - wdp:P6782
    domain_of:
    - Organization
    range: string
    required: false
    recommended: true
    multivalued: false
class_uri: foaf:Organization

```
</details>

### Induced

<details>
```yaml
name: Organization
description: A social entity established to meet needs or pursue specific goals
title: Organization
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q43229
- vcard:Organization
- wd:Q43229
- vcard:Organization
is_a: PersonOrOrganization
slot_usage:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    close_mappings:
    - wdp:P4970
    - schema:alternateName
    domain_of:
    - Organization
    - CommonName
    - AlternateName
    range: AlternateName
    required: false
    multivalued: true
  country:
    name: country
    description: The country of the organization
    title: country
    domain_of:
    - Organization
    range: Country
    required: false
    recommended: true
    multivalued: false
  rORiD:
    name: rORiD
    description: The corresponding organization's persistent identifier from the Research
      Organization Registry (ROR)
    title: ROR iD
    exact_mappings:
    - wdp:P6782
    domain_of:
    - Organization
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - wdp:P4970
    - schema:alternateName
    rank: 1000
    alias: alternateName
    owner: Organization
    domain_of:
    - Organization
    - CommonName
    - AlternateName
    range: AlternateName
    required: false
    multivalued: true
  country:
    name: country
    description: The country of the organization
    title: country
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: country
    owner: Organization
    domain_of:
    - Organization
    range: Country
    required: false
    recommended: true
    multivalued: false
  rORiD:
    name: rORiD
    description: The corresponding organization's persistent identifier from the Research
      Organization Registry (ROR)
    title: ROR iD
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - wdp:P6782
    rank: 1000
    alias: rORiD
    owner: Organization
    domain_of:
    - Organization
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
    close_mappings:
    - dct:title
    rank: 1000
    slot_uri: foaf:name
    alias: name
    owner: Organization
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
    owner: Organization
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
    rank: 1000
    slot_uri: foaf:homepage
    alias: homePage
    owner: Organization
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
    - dcat:contactPoint
    rank: 1000
    alias: contactPoint
    owner: Organization
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
    rank: 1000
    alias: logo
    owner: Organization
    domain_of:
    - PersonOrOrganization
    - License
    - Certification
    range: Image
    required: false
    multivalued: false
class_uri: foaf:Organization

```
</details>