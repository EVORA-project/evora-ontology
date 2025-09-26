

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
        
      ContactPoint : dateIssued
        
      ContactPoint : dateModified
        
      ContactPoint : description
        
      ContactPoint : email
        
      ContactPoint : identifier
        
      ContactPoint : iri
        
      ContactPoint : keyword
        
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
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |
| [identifier](identifier.md) | * <br/> [String](String.md) | A unique identifier of the resource being described or cataloged | [Resource](Resource.md) |
| [iri](iri.md) | * <br/> [Uri](Uri.md) | International Resource Identifier (IRI) that uniquely identifies or refers to... | [Resource](Resource.md) |





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
| exact | schema:ContactPoint, vcard:Kind, schema:ContactPoint, vcard:Kind |
| narrow | schema:PostalAddress, schema:PostalAddress |
| related | vcard:Contact, vcard:Contact |
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
- vcard:Kind
- schema:ContactPoint
- vcard:Kind
close_mappings:
- wd:Q30322502
- wd:Q30322502
related_mappings:
- vcard:Contact
- vcard:Contact
narrow_mappings:
- schema:PostalAddress
- schema:PostalAddress
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
    - vcard:fn
    close_mappings:
    - rdfs:label
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
    - foaf:mbox
    close_mappings:
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
    close_mappings:
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
    exact_mappings:
    - schema:streetAddress
    - vcard:street-address
    close_mappings:
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
    exact_mappings:
    - schema:addressLocality
    - vcard:locality
    close_mappings:
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
    exact_mappings:
    - schema:addressRegion
    - vcard:region
    close_mappings:
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
    exact_mappings:
    - schema:postalCode
    - vcard:postal-code
    close_mappings:
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
    exact_mappings:
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
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
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
- vcard:Kind
- schema:ContactPoint
- vcard:Kind
close_mappings:
- wd:Q30322502
- wd:Q30322502
related_mappings:
- vcard:Contact
- vcard:Contact
narrow_mappings:
- schema:PostalAddress
- schema:PostalAddress
is_a: Resource
slot_usage:
  name:
    name: name
    description: A word or set of words used to identify and refer to an entity
    title: name
    exact_mappings:
    - schema:name
    - vcard:fn
    close_mappings:
    - rdfs:label
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
    - foaf:mbox
    close_mappings:
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
    close_mappings:
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
    exact_mappings:
    - schema:streetAddress
    - vcard:street-address
    close_mappings:
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
    exact_mappings:
    - schema:addressLocality
    - vcard:locality
    close_mappings:
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
    exact_mappings:
    - schema:addressRegion
    - vcard:region
    close_mappings:
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
    exact_mappings:
    - schema:postalCode
    - vcard:postal-code
    close_mappings:
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
    exact_mappings:
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
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
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
    - vcard:fn
    close_mappings:
    - rdfs:label
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
    - foaf:mbox
    close_mappings:
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
    close_mappings:
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
    exact_mappings:
    - schema:streetAddress
    - vcard:street-address
    close_mappings:
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
    exact_mappings:
    - schema:addressLocality
    - vcard:locality
    close_mappings:
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
    exact_mappings:
    - schema:addressRegion
    - vcard:region
    close_mappings:
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
    exact_mappings:
    - schema:postalCode
    - vcard:postal-code
    close_mappings:
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
    exact_mappings:
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
    - wdp:P496
    - reproduceme:ORCID
    related_mappings:
    - iao:0000708
    - edam:4022
    rank: 1000
    is_a: identifier
    alias: orcidId
    owner: ContactPoint
    domain_of:
    - ContactPoint
    - Person
    range: string
    required: false
    recommended: true
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: ContactPoint
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  dateIssued:
    name: dateIssued
    description: Date of formal issuance (e.g., publication) of the resource
    title: date issued
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000051
    close_mappings:
    - schema:datePublished
    - schema:dateCreated
    rank: 1000
    slot_uri: dct:issued
    alias: dateIssued
    owner: ContactPoint
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  dateModified:
    name: dateModified
    description: Most recent date on which the resource was changed, updated or modified
    title: date modified
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000036
    close_mappings:
    - schema:dateModified
    rank: 1000
    slot_uri: dct:modified
    alias: dateModified
    owner: ContactPoint
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  identifier:
    name: identifier
    description: A unique identifier of the resource being described or cataloged
    title: identifier
    comments:
    - The identifier is a text string which is assigned to the resource to provide
      an unambiguous reference within a particular context. Persistent identifiers
      should be provided as HTTP URIs
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dct:identifier
    alias: identifier
    owner: ContactPoint
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  iri:
    name: iri
    description: International Resource Identifier (IRI) that uniquely identifies
      or refers to the resource. IRIs include URIs, and URIs include URLs
    title: IRI
    comments:
    - An IRI is a global identifier standardized by IETF RFC 3987. It may or may not
      be resolvable on the web. IRIs include URIs, and URIs include URLs
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - biolink:iri
    related_mappings:
    - mi:url
    narrow_mappings:
    - schema:url
    rank: 1000
    is_a: identifier
    alias: iri
    owner: ContactPoint
    domain_of:
    - Resource
    range: uri
    required: false
    multivalued: true

```
</details>