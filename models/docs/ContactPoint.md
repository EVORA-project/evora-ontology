

# Class: Contact Point (ContactPoint) 


_Entity serving as focal point of information_





URI: [EVORAO:ContactPoint](https://w3id.org/evorao/ContactPoint)






```mermaid
 classDiagram
    class ContactPoint
    click ContactPoint href "../ContactPoint"
      Resource <|-- ContactPoint
        click Resource href "../Resource"
      
      ContactPoint : addressCountry
        
          
    
    
    ContactPoint --> "0..1" Country : addressCountry
    click Country href "../Country"

        
      ContactPoint : addressLocality
        
      ContactPoint : addressRegion
        
      ContactPoint : description
        
      ContactPoint : email
        
      ContactPoint : name
        
      ContactPoint : orcidId
        
      ContactPoint : postalCode
        
      ContactPoint : streetAddress
        
      ContactPoint : telephone
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **ContactPoint**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | direct |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | direct |
| [email](email.md) | 0..1 _recommended_ <br/> [String](String.md) | Email address | direct |
| [telephone](telephone.md) | 0..1 _recommended_ <br/> [String](String.md) | The telephone number | direct |
| [streetAddress](streetAddress.md) | 0..1 <br/> [String](String.md) | The building/apartment number and the street name | direct |
| [addressLocality](addressLocality.md) | 0..1 <br/> [String](String.md) | The locality in which the street address is, and which is in the region | direct |
| [addressRegion](addressRegion.md) | 0..1 <br/> [String](String.md) | The region in which the locality is, and which is in the country | direct |
| [postalCode](postalCode.md) | 0..1 <br/> [String](String.md) | The postal code | direct |
| [addressCountry](addressCountry.md) | 0..1 <br/> [Country](Country.md) | The country as of  ISO 3166 | direct |
| [orcidId](orcidId.md) | 0..1 _recommended_ <br/> [String](String.md) | Unique persistent identifier for a person, provided by the Open Researcher an... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonOrOrganization](PersonOrOrganization.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Person](Person.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Organization](Organization.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Provider](Provider.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Originator](Originator.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [ProductOrService](ProductOrService.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Service](Service.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Product](Product.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Antibody](Antibody.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Hybridoma](Hybridoma.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Protein](Protein.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [NucleicAcid](NucleicAcid.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [DetectionKit](DetectionKit.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Bundle](Bundle.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Pathogen](Pathogen.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Virus](Virus.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Bacterium](Bacterium.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Fungus](Fungus.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Protozoan](Protozoan.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Viroid](Viroid.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [Prion](Prion.md) | [contactPoint](contactPoint.md) | range | [ContactPoint](ContactPoint.md) |
| [MaterialSafetyDataSheet](MaterialSafetyDataSheet.md) | [materialSafetyContact](materialSafetyContact.md) | range | [ContactPoint](ContactPoint.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:ContactPoint |
| native | EVORAO:ContactPoint |
| exact | schema:ContactPoint, vcard:Contact, schema:ContactPoint, vcard:Contact |
| close | wd:Q30322502, wd:Q30322502 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContactPoint
description: Entity serving as focal point of information
title: Contact Point
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:ContactPoint
- vcard:Contact
- schema:ContactPoint
- vcard:Contact
close_mappings:
- wd:Q30322502
- wd:Q30322502
is_a: Resource
slots:
- name
- description
- email
- telephone
- streetAddress
- addressLocality
- addressRegion
- postalCode
- addressCountry
- orcidId
slot_usage:
  name:
    name: name
    description: A word or set of words used to identify and refer to an entity
    title: name
    exact_mappings:
    - schema:name
    close_mappings:
    - dct:title
    slot_uri: foaf:name
    domain_of:
    - ContactPoint
    - PersonOrOrganization
    - File
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
    exact_mappings:
    - schema:description
    slot_uri: dct:description
    domain_of:
    - ContactPoint
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - File
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  email:
    name: email
    description: Email address
    title: email
    exact_mappings:
    - schema:email
    - vcard:email
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  telephone:
    name: telephone
    description: The telephone number
    title: telephone
    exact_mappings:
    - schema:telephone
    - vcard:telephone
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  streetAddress:
    name: streetAddress
    description: The building/apartment number and the street name
    title: street address
    close_mappings:
    - schema:streetAddress
    - vcard:hasStreetAddress
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressLocality:
    name: addressLocality
    description: The locality in which the street address is, and which is in the
      region. e.g, the city
    title: locality/city
    close_mappings:
    - schema:addressLocality
    - vcard:hasLocality
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressRegion:
    name: addressRegion
    description: The region in which the locality is, and which is in the country.
      For example, California or another appropriate first-level Administrative division
    title: region
    close_mappings:
    - schema:addressRegion
    - vcard:hasRegion
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  postalCode:
    name: postalCode
    description: The postal code
    title: postal code
    close_mappings:
    - schema:postalCode
    - vcard:hasPostalCode
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressCountry:
    name: addressCountry
    description: The country as of  ISO 3166
    title: address Country
    close_mappings:
    - schema:addressCountry
    - vcard:hasCountryName
    domain_of:
    - ContactPoint
    range: Country
    required: false
    multivalued: false
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    exact_mappings:
    - iao:0000708
    domain_of:
    - ContactPoint
    - Person
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: ContactPoint
description: Entity serving as focal point of information
title: Contact Point
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:ContactPoint
- vcard:Contact
- schema:ContactPoint
- vcard:Contact
close_mappings:
- wd:Q30322502
- wd:Q30322502
is_a: Resource
slot_usage:
  name:
    name: name
    description: A word or set of words used to identify and refer to an entity
    title: name
    exact_mappings:
    - schema:name
    close_mappings:
    - dct:title
    slot_uri: foaf:name
    domain_of:
    - ContactPoint
    - PersonOrOrganization
    - File
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
    exact_mappings:
    - schema:description
    slot_uri: dct:description
    domain_of:
    - ContactPoint
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - File
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  email:
    name: email
    description: Email address
    title: email
    exact_mappings:
    - schema:email
    - vcard:email
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  telephone:
    name: telephone
    description: The telephone number
    title: telephone
    exact_mappings:
    - schema:telephone
    - vcard:telephone
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  streetAddress:
    name: streetAddress
    description: The building/apartment number and the street name
    title: street address
    close_mappings:
    - schema:streetAddress
    - vcard:hasStreetAddress
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressLocality:
    name: addressLocality
    description: The locality in which the street address is, and which is in the
      region. e.g, the city
    title: locality/city
    close_mappings:
    - schema:addressLocality
    - vcard:hasLocality
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressRegion:
    name: addressRegion
    description: The region in which the locality is, and which is in the country.
      For example, California or another appropriate first-level Administrative division
    title: region
    close_mappings:
    - schema:addressRegion
    - vcard:hasRegion
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  postalCode:
    name: postalCode
    description: The postal code
    title: postal code
    close_mappings:
    - schema:postalCode
    - vcard:hasPostalCode
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressCountry:
    name: addressCountry
    description: The country as of  ISO 3166
    title: address Country
    close_mappings:
    - schema:addressCountry
    - vcard:hasCountryName
    domain_of:
    - ContactPoint
    range: Country
    required: false
    multivalued: false
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    exact_mappings:
    - iao:0000708
    domain_of:
    - ContactPoint
    - Person
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
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
    owner: ContactPoint
    domain_of:
    - ContactPoint
    - PersonOrOrganization
    - File
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
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: ContactPoint
    domain_of:
    - ContactPoint
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - File
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  email:
    name: email
    description: Email address
    title: email
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:email
    - vcard:email
    rank: 1000
    alias: email
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  telephone:
    name: telephone
    description: The telephone number
    title: telephone
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:telephone
    - vcard:telephone
    rank: 1000
    alias: telephone
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    recommended: true
    multivalued: false
  streetAddress:
    name: streetAddress
    description: The building/apartment number and the street name
    title: street address
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:streetAddress
    - vcard:hasStreetAddress
    rank: 1000
    alias: streetAddress
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressLocality:
    name: addressLocality
    description: The locality in which the street address is, and which is in the
      region. e.g, the city
    title: locality/city
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:addressLocality
    - vcard:hasLocality
    rank: 1000
    alias: addressLocality
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressRegion:
    name: addressRegion
    description: The region in which the locality is, and which is in the country.
      For example, California or another appropriate first-level Administrative division
    title: region
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:addressRegion
    - vcard:hasRegion
    rank: 1000
    alias: addressRegion
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  postalCode:
    name: postalCode
    description: The postal code
    title: postal code
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:postalCode
    - vcard:hasPostalCode
    rank: 1000
    alias: postalCode
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: string
    required: false
    multivalued: false
  addressCountry:
    name: addressCountry
    description: The country as of  ISO 3166
    title: address Country
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:addressCountry
    - vcard:hasCountryName
    rank: 1000
    alias: addressCountry
    owner: ContactPoint
    domain_of:
    - ContactPoint
    range: Country
    required: false
    multivalued: false
  orcidId:
    name: orcidId
    description: Unique persistent identifier for a person, provided by the Open Researcher
      and Contributor ID (ORCID) organisation
    title: ORCID id
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - iao:0000708
    related_mappings:
    - iao:0000708
    - edam:4022
    rank: 1000
    alias: orcidId
    owner: ContactPoint
    domain_of:
    - ContactPoint
    - Person
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>