

# Class: Provider (Provider) 


_A provider of products or services, as a specific organization_





URI: [EVORAO:Provider](https://w3id.org/evorao/Provider)






```mermaid
 classDiagram
    class Provider
    click Provider href "../Provider"
      Organization <|-- Provider
        click Organization href "../Organization"
      
      Provider : alternateName
        
          
    
    
    Provider --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      Provider : contactPoint
        
          
    
    
    Provider --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Provider : country
        
          
    
    
    Provider --> "0..1 _recommended_" Country : country
    click Country href "../Country"

        
      Provider : description
        
      Provider : homePage
        
      Provider : logo
        
          
    
    
    Provider --> "0..1" Image : logo
    click Image href "../Image"

        
      Provider : memberOfRi
        
          
    
    
    Provider --> "*" ReasearchInfrastructure : memberOfRi
    click ReasearchInfrastructure href "../ReasearchInfrastructure"

        
      Provider : name
        
      Provider : rorId
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * [Organization](Organization.md)
            * **Provider**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [memberOfRi](memberOfRi.md) | * <br/> [ReasearchInfrastructure](ReasearchInfrastructure.md) | The research infrastructure of which this organization is a member | direct |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any other name under which the entity can be known | [Organization](Organization.md) |
| [country](country.md) | 0..1 _recommended_ <br/> [Country](Country.md) | The country of the organization | [Organization](Organization.md) |
| [rorId](rorId.md) | 0..1 _recommended_ <br/> [String](String.md) | The corresponding organization's persistent identifier from the Research Orga... | [Organization](Organization.md) |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | [PersonOrOrganization](PersonOrOrganization.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [PersonOrOrganization](PersonOrOrganization.md) |
| [homePage](homePage.md) | 0..1 <br/> [Uri](Uri.md) | A web page that serves as the main or introductory page | [PersonOrOrganization](PersonOrOrganization.md) |
| [contactPoint](contactPoint.md) | 0..1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [PersonOrOrganization](PersonOrOrganization.md) |
| [logo](logo.md) | 0..1 <br/> [Image](Image.md) | A path or URL to the related logo | [PersonOrOrganization](PersonOrOrganization.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProductOrService](ProductOrService.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Service](Service.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Product](Product.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Antibody](Antibody.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Hybridoma](Hybridoma.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Protein](Protein.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [NucleicAcid](NucleicAcid.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [DetectionKit](DetectionKit.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Bundle](Bundle.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Pathogen](Pathogen.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Virus](Virus.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Bacterium](Bacterium.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Fungus](Fungus.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Protozoan](Protozoan.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Viroid](Viroid.md) | [provider](provider.md) | range | [Provider](Provider.md) |
| [Prion](Prion.md) | [provider](provider.md) | range | [Provider](Provider.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Provider |
| native | EVORAO:Provider |
| related | foaf:Organization, dct:ProvenanceStatement, foaf:Organization, dct:ProvenanceStatement |
| close | ncit:C37900, ncit:C37900 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Provider
description: A provider of products or services, as a specific organization
title: Provider
from_schema: https://w3id.org/evorao/
close_mappings:
- ncit:C37900
- ncit:C37900
related_mappings:
- foaf:Organization
- dct:ProvenanceStatement
- foaf:Organization
- dct:ProvenanceStatement
is_a: Organization
slots:
- memberOfRi
slot_usage:
  memberOfRi:
    name: memberOfRi
    description: The research infrastructure of which this organization is a member
    title: member of RI
    broad_mappings:
    - schema:memberOf
    domain_of:
    - Provider
    range: ReasearchInfrastructure
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Provider
description: A provider of products or services, as a specific organization
title: Provider
from_schema: https://w3id.org/evorao/
close_mappings:
- ncit:C37900
- ncit:C37900
related_mappings:
- foaf:Organization
- dct:ProvenanceStatement
- foaf:Organization
- dct:ProvenanceStatement
is_a: Organization
slot_usage:
  memberOfRi:
    name: memberOfRi
    description: The research infrastructure of which this organization is a member
    title: member of RI
    broad_mappings:
    - schema:memberOf
    domain_of:
    - Provider
    range: ReasearchInfrastructure
    required: false
    multivalued: true
attributes:
  memberOfRi:
    name: memberOfRi
    description: The research infrastructure of which this organization is a member
    title: member of RI
    from_schema: https://w3id.org/evorao/
    broad_mappings:
    - schema:memberOf
    rank: 1000
    alias: memberOfRi
    owner: Provider
    domain_of:
    - Provider
    range: ReasearchInfrastructure
    required: false
    multivalued: true
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    rank: 1000
    alias: alternateName
    owner: Provider
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
    owner: Provider
    domain_of:
    - Organization
    range: Country
    required: false
    recommended: true
    multivalued: false
  rorId:
    name: rorId
    description: The corresponding organization's persistent identifier from the Research
      Organization Registry (ROR)
    title: ROR iD
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - wdp:P6782
    related_mappings:
    - dwc:institutionCode
    rank: 1000
    alias: rorId
    owner: Provider
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
    - vcard:fn
    close_mappings:
    - rdfs:label
    - dct:title
    rank: 1000
    slot_uri: foaf:name
    alias: name
    owner: Provider
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
    owner: Provider
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
    owner: Provider
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
    owner: Provider
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
    owner: Provider
    domain_of:
    - PersonOrOrganization
    - License
    - Certification
    range: Image
    required: false
    multivalued: false

```
</details>