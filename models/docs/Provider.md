

# Class: Provider (Provider)


_A provider of products or services, as a specific organization_





URI: [EVORAO:Provider](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Provider)






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

        
      Provider : memberOfRI
        
          
    
    
    Provider --> "*" RI : memberOfRI
    click RI href "../RI"

        
      Provider : name
        
      Provider : rORiD
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * [Organization](Organization.md)
            * **Provider**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [memberOfRI](memberOfRI.md) | * <br/> [RI](RI.md) | The research infrastructure of which this organization is a member | direct |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any other name under which the entity can be known | [Organization](Organization.md) |
| [country](country.md) | 0..1 _recommended_ <br/> [Country](Country.md) | The country of the organization | [Organization](Organization.md) |
| [rORiD](rORiD.md) | 0..1 _recommended_ <br/> [String](String.md) | The corresponding organization's persistent identifier from the Research Orga... | [Organization](Organization.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [PersonOrOrganization](PersonOrOrganization.md) |
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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Provider |
| native | EVORAO:Provider |
| close | dct:ProvenanceStatement, dct:ProvenanceStatement |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Provider
description: A provider of products or services, as a specific organization
title: Provider
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:ProvenanceStatement
- dct:ProvenanceStatement
is_a: Organization
slots:
- memberOfRI
slot_usage:
  memberOfRI:
    name: memberOfRI
    description: The research infrastructure of which this organization is a member
    title: member of RI
    domain_of:
    - Provider
    range: RI
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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dct:ProvenanceStatement
- dct:ProvenanceStatement
is_a: Organization
slot_usage:
  memberOfRI:
    name: memberOfRI
    description: The research infrastructure of which this organization is a member
    title: member of RI
    domain_of:
    - Provider
    range: RI
    required: false
    multivalued: true
attributes:
  memberOfRI:
    name: memberOfRI
    description: The research infrastructure of which this organization is a member
    title: member of RI
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: memberOfRI
    owner: Provider
    domain_of:
    - Provider
    range: RI
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: country
    owner: Provider
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - wdp:P6782
    rank: 1000
    alias: rORiD
    owner: Provider
    domain_of:
    - Organization
    range: string
    required: false
    recommended: true
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
    owner: Provider
    domain_of:
    - PersonOrOrganization
    - DataService
    - Catalogue
    - Term
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
    owner: Provider
    domain_of:
    - PersonOrOrganization
    - DataService
    - Catalogue
    - Term
    - ProductOrService
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:contactPoint
    rank: 1000
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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