

# Class: Service


_A service_





URI: [EVORA:Service](https://evora-project.eu/Service)






```mermaid
 classDiagram
    class Service
    click Service href "../Service"
      ProductOrService <|-- Service
        click ProductOrService href "../ProductOrService"
      
      Service : accessPointURL
        
      Service : additionalCategory
        
          
    
    
    Service --> "*" ProductCategory : additionalCategory
    click ProductCategory href "../ProductCategory"

        
      Service : availability
        
      Service : biosafetyRestrictions
        
      Service : canItBeUsedToProduceGMO
        
      Service : category
        
          
    
    
    Service --> "1" ProductCategory : category
    click ProductCategory href "../ProductCategory"

        
      Service : certification
        
          
    
    
    Service --> "*" Certification : certification
    click Certification href "../Certification"

        
      Service : collection
        
          
    
    
    Service --> "1..*" Collection : collection
    click Collection href "../Collection"

        
      Service : complementaryDocument
        
          
    
    
    Service --> "*" Document : complementaryDocument
    click Document href "../Document"

        
      Service : contactPoint
        
          
    
    
    Service --> "0..1" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Service : description
        
      Service : externalRelatedReference
        
          
    
    
    Service --> "*" ExternalRelatedReference : externalRelatedReference
    click ExternalRelatedReference href "../ExternalRelatedReference"

        
      Service : internalReference
        
      Service : keywords
        
          
    
    
    Service --> "1..*" Keyword : keywords
    click Keyword href "../Keyword"

        
      Service : modelSpecies
        
      Service : modelType
        
      Service : name
        
      Service : note
        
      Service : pathogenIdentification
        
          
    
    
    Service --> "1..*" PathogenIdentification : pathogenIdentification
    click PathogenIdentification href "../PathogenIdentification"

        
      Service : productPicture
        
          
    
    
    Service --> "*" Image : productPicture
    click Image href "../Image"

        
      Service : provider
        
          
    
    
    Service --> "1" Provider : provider
    click Provider href "../Provider"

        
      Service : qualityGrading
        
      Service : refSKU
        
      Service : relatedDOI
        
          
    
    
    Service --> "*" DOI : relatedDOI
    click DOI href "../DOI"

        
      Service : riskGroup
        
          
    
    
    Service --> "0..1" RiskGroup : riskGroup
    click RiskGroup href "../RiskGroup"

        
      Service : technicalRecommendation
        
      Service : unitCost
        
      Service : unitDefinition
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [ProductOrService](ProductOrService.md)
            * **Service**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [modelSpecies](modelSpecies.md) | 0..1 <br/> [String](String.md) | The species of the infected organism in the experiment | direct |
| [modelType](modelType.md) | 0..1 <br/> [String](String.md) | The specific name of the infected organism, including its modification if nec... | direct |
| [accessPointURL](accessPointURL.md) | 1 <br/> [Uri](Uri.md) | The URL that permits to access to the product/service detailed description pa... | [ProductOrService](ProductOrService.md) |
| [refSKU](refSKU.md) | 1 <br/> [String](String.md) | The reference or the stock keeping unit of the service or item provided in th... | [ProductOrService](ProductOrService.md) |
| [unitDefinition](unitDefinition.md) | 0..1 <br/> [String](String.md) | A short description of what will be delivered by ordering one unit of this it... | [ProductOrService](ProductOrService.md) |
| [category](category.md) | 1 <br/> [ProductCategory](ProductCategory.md) | The main category of the service or product | [ProductOrService](ProductOrService.md) |
| [additionalCategory](additionalCategory.md) | * <br/> [ProductCategory](ProductCategory.md) | Any category apart from its main category in which this product or service ca... | [ProductOrService](ProductOrService.md) |
| [unitCost](unitCost.md) | 1 <br/> [String](String.md) | The cost per access for one unit as defined by the unit definition | [ProductOrService](ProductOrService.md) |
| [qualityGrading](qualityGrading.md) | 0..1 <br/> [String](String.md) | Information that permits to assess the quality level of what will be provided | [ProductOrService](ProductOrService.md) |
| [pathogenIdentification](pathogenIdentification.md) | 1..* <br/> [PathogenIdentification](PathogenIdentification.md) | The identification of the pathogen or group of pathogens (e | [ProductOrService](ProductOrService.md) |
| [relatedDOI](relatedDOI.md) | * <br/> [DOI](DOI.md) | Any DOI that can be related | [ProductOrService](ProductOrService.md) |
| [riskGroup](riskGroup.md) | 0..1 <br/> [RiskGroup](RiskGroup.md) | The highest risk group related to this resource | [ProductOrService](ProductOrService.md) |
| [biosafetyRestrictions](biosafetyRestrictions.md) | 0..1 <br/> [String](String.md) | Information about guidelines and regulations designed to prevent the exposure... | [ProductOrService](ProductOrService.md) |
| [canItBeUsedToProduceGMO](canItBeUsedToProduceGMO.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the current service or product can be used to produce GMO | [ProductOrService](ProductOrService.md) |
| [provider](provider.md) | 1 <br/> [Provider](Provider.md) | A provider of this product or service, as a specific organization | [ProductOrService](ProductOrService.md) |
| [collection](collection.md) | 1..* <br/> [Collection](Collection.md) | The collection(s) to which belongs this item | [ProductOrService](ProductOrService.md) |
| [keywords](keywords.md) | 1..* <br/> [Keyword](Keyword.md) | List of terms used to tag and categorize this Item | [ProductOrService](ProductOrService.md) |
| [availability](availability.md) | 1 <br/> [String](String.md) | The state or condition in which this item is accessible and ready for use or ... | [ProductOrService](ProductOrService.md) |
| [complementaryDocument](complementaryDocument.md) | * <br/> [Document](Document.md) | Any complementary document that can be related to this Item | [ProductOrService](ProductOrService.md) |
| [technicalRecommendation](technicalRecommendation.md) | 0..1 <br/> [String](String.md) | Expert advice or guidelines provided to ensure the optimal use, performance, ... | [ProductOrService](ProductOrService.md) |
| [productPicture](productPicture.md) | * <br/> [Image](Image.md) | A picture that can represent the item | [ProductOrService](ProductOrService.md) |
| [externalRelatedReference](externalRelatedReference.md) | * <br/> [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve another related item from an external pr... | [ProductOrService](ProductOrService.md) |
| [certification](certification.md) | * <br/> [Certification](Certification.md) | Any certification related to the current product or service; e | [ProductOrService](ProductOrService.md) |
| [internalReference](internalReference.md) | 0..1 <br/> [String](String.md) | Any reference or indication to be used for local retrieval purpose | [ProductOrService](ProductOrService.md) |
| [note](note.md) | 0..1 <br/> [String](String.md) | An aditional information as a textual comment | [ProductOrService](ProductOrService.md) |
| [contactPoint](contactPoint.md) | 0..1 <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [ProductOrService](ProductOrService.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |







## Aliases


* Service



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Service |
| native | EVORA:Service |
| close | wd:Q7406919 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Service
description: A service
from_schema: https://evora-project.eu/
aliases:
- Service
close_mappings:
- wd:Q7406919
is_a: ProductOrService
slots:
- modelSpecies
- modelType
slot_usage:
  modelSpecies:
    name: modelSpecies
    description: The species of the infected organism in the experiment
    aliases:
    - model species
    range: string
    required: false
    multivalued: false
  modelType:
    name: modelType
    description: The specific name of the infected organism, including its modification
      if necessary
    aliases:
    - model type
    range: string
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Service
description: A service
from_schema: https://evora-project.eu/
aliases:
- Service
close_mappings:
- wd:Q7406919
is_a: ProductOrService
slot_usage:
  modelSpecies:
    name: modelSpecies
    description: The species of the infected organism in the experiment
    aliases:
    - model species
    range: string
    required: false
    multivalued: false
  modelType:
    name: modelType
    description: The specific name of the infected organism, including its modification
      if necessary
    aliases:
    - model type
    range: string
    required: false
    multivalued: false
attributes:
  modelSpecies:
    name: modelSpecies
    description: The species of the infected organism in the experiment
    from_schema: https://evora-project.eu/
    aliases:
    - model species
    rank: 1000
    alias: modelSpecies
    owner: Service
    domain_of:
    - Service
    range: string
    required: false
    multivalued: false
  modelType:
    name: modelType
    description: The specific name of the infected organism, including its modification
      if necessary
    from_schema: https://evora-project.eu/
    aliases:
    - model type
    rank: 1000
    alias: modelType
    owner: Service
    domain_of:
    - Service
    range: string
    required: false
    multivalued: false
  accessPointURL:
    name: accessPointURL
    description: The URL that permits to access to the product/service detailed description
      page on the provider's website and/or allows to place an order about it or at
      least describe the process to place an order/enquiry
    from_schema: https://evora-project.eu/
    aliases:
    - access point URL
    exact_mappings:
    - dcat:landingPage
    rank: 1000
    alias: accessPointURL
    owner: Service
    domain_of:
    - ProductOrService
    range: uri
    required: true
    multivalued: false
  refSKU:
    name: refSKU
    description: The reference or the stock keeping unit of the service or item provided
      in the provider's catalogue
    from_schema: https://evora-project.eu/
    aliases:
    - ref-SKU
    exact_mappings:
    - dct:identifier
    rank: 1000
    alias: refSKU
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  unitDefinition:
    name: unitDefinition
    description: A short description of what will be delivered by ordering one unit
      of this item
    comments:
    - 'The description of what will be delivered to the end-user (e.g.: packaging,
      quantity...)'
    from_schema: https://evora-project.eu/
    aliases:
    - unit definition
    rank: 1000
    alias: unitDefinition
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  category:
    name: category
    description: The main category of the service or product
    from_schema: https://evora-project.eu/
    aliases:
    - category
    exact_mappings:
    - dcat:theme
    rank: 1000
    alias: category
    owner: Service
    domain_of:
    - ProductOrService
    range: ProductCategory
    required: true
    multivalued: false
  additionalCategory:
    name: additionalCategory
    description: Any category apart from its main category in which this product or
      service can fit
    from_schema: https://evora-project.eu/
    aliases:
    - additional category
    exact_mappings:
    - dcat:theme
    rank: 1000
    alias: additionalCategory
    owner: Service
    domain_of:
    - ProductOrService
    range: ProductCategory
    required: false
    multivalued: true
  unitCost:
    name: unitCost
    description: The cost per access for one unit as defined by the unit definition
    comments:
    - The cost per access may not be defined or be specific to a request, so it has
      to be a xsd:string instead of an xsd:float as initialy suggested to permit description
      of cost as conditional to what is requested
    from_schema: https://evora-project.eu/
    aliases:
    - unit cost
    rank: 1000
    ifabsent: string(on request)
    alias: unitCost
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  qualityGrading:
    name: qualityGrading
    description: Information that permits to assess the quality level of what will
      be provided
    from_schema: https://evora-project.eu/
    aliases:
    - quality grading
    rank: 1000
    alias: qualityGrading
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  pathogenIdentification:
    name: pathogenIdentification
    description: The identification of the pathogen or group of pathogens (e.g; name,
      taxon identification, etc.) related to the current item.
    comments:
    - 'The pathogen identification contains information about name and taxon but in
      some cases(e.g: FAIRSHARING) there may have no direct pathogen related but simply
      a taxonomic information .... the default value should be the root of virology:
      Viruses'
    from_schema: https://evora-project.eu/
    aliases:
    - pathogen identification
    rank: 1000
    alias: pathogenIdentification
    owner: Service
    domain_of:
    - ProductOrService
    range: PathogenIdentification
    required: true
    multivalued: true
  relatedDOI:
    name: relatedDOI
    description: Any DOI that can be related
    from_schema: https://evora-project.eu/
    aliases:
    - DOI
    close_mappings:
    - wdp:P356
    rank: 1000
    alias: relatedDOI
    owner: Service
    domain_of:
    - Publication
    - ProductOrService
    range: DOI
    required: false
    multivalued: true
  riskGroup:
    name: riskGroup
    description: The highest risk group related to this resource. The risk group of
      a biological agent guiding its initial handling in labs according to the risk
      group classification defined by the WHO laboratory biosafety manual
    from_schema: https://evora-project.eu/
    aliases:
    - risk group
    close_mappings:
    - wdp:P12663
    rank: 1000
    alias: riskGroup
    owner: Service
    domain_of:
    - ProductOrService
    range: RiskGroup
    required: false
    multivalued: false
  biosafetyRestrictions:
    name: biosafetyRestrictions
    description: Information about guidelines and regulations designed to prevent
      the exposure to or release of potentially harmful biological agents. It thereby
      contributes to protecting people and the environment from biohazards while accessing
      this product or service
    from_schema: https://evora-project.eu/
    aliases:
    - biosafety restrictions
    rank: 1000
    alias: biosafetyRestrictions
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  canItBeUsedToProduceGMO:
    name: canItBeUsedToProduceGMO
    description: Indicates if the current service or product can be used to produce
      GMO
    comments:
    - Set to TRUE if it can produce GMO
    from_schema: https://evora-project.eu/
    aliases:
    - can it be used to produce GMO
    rank: 1000
    alias: canItBeUsedToProduceGMO
    owner: Service
    domain_of:
    - ProductOrService
    range: boolean
    required: false
    multivalued: false
  provider:
    name: provider
    description: A provider of this product or service, as a specific organization
    from_schema: https://evora-project.eu/
    aliases:
    - provider
    rank: 1000
    alias: provider
    owner: Service
    domain_of:
    - ProductOrService
    range: Provider
    required: true
    multivalued: false
  collection:
    name: collection
    description: The collection(s) to which belongs this item
    from_schema: https://evora-project.eu/
    aliases:
    - collection
    rank: 1000
    alias: collection
    owner: Service
    domain_of:
    - ProductOrService
    range: Collection
    required: true
    multivalued: true
  keywords:
    name: keywords
    description: List of terms used to tag and categorize this Item
    from_schema: https://evora-project.eu/
    aliases:
    - keywords
    exact_mappings:
    - dcat:keyword
    rank: 1000
    alias: keywords
    owner: Service
    domain_of:
    - ProductOrService
    range: Keyword
    required: true
    multivalued: true
  availability:
    name: availability
    description: The state or condition in which this item is accessible and ready
      for use or can be obtained
    comments:
    - Possible availabilities may differ from a project to another
    from_schema: https://evora-project.eu/
    aliases:
    - availability
    rank: 1000
    ifabsent: string(on request)
    alias: availability
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  complementaryDocument:
    name: complementaryDocument
    description: Any complementary document that can be related to this Item
    from_schema: https://evora-project.eu/
    aliases:
    - complementary document
    rank: 1000
    alias: complementaryDocument
    owner: Service
    domain_of:
    - ProductOrService
    - Bundle
    range: Document
    required: false
    multivalued: true
  technicalRecommendation:
    name: technicalRecommendation
    description: Expert advice or guidelines provided to ensure the optimal use, performance,
      and maintenance of what is provided, including best practices, troubleshooting
      tips, and procedural instructions
    from_schema: https://evora-project.eu/
    aliases:
    - technical recommendation
    rank: 1000
    alias: technicalRecommendation
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  productPicture:
    name: productPicture
    description: A picture that can represent the item
    from_schema: https://evora-project.eu/
    aliases:
    - product picture
    rank: 1000
    alias: productPicture
    owner: Service
    domain_of:
    - ProductOrService
    range: Image
    required: false
    multivalued: true
  externalRelatedReference:
    name: externalRelatedReference
    description: A reference that permits to retrieve another related item from an
      external provider
    from_schema: https://evora-project.eu/
    aliases:
    - external related reference
    rank: 1000
    alias: externalRelatedReference
    owner: Service
    domain_of:
    - ProductOrService
    range: ExternalRelatedReference
    required: false
    multivalued: true
  certification:
    name: certification
    description: Any certification related to the current product or service; e.g.,
      ISO certification
    from_schema: https://evora-project.eu/
    aliases:
    - certification
    close_mappings:
    - dct:conformsTo
    rank: 1000
    alias: certification
    owner: Service
    domain_of:
    - ProductOrService
    range: Certification
    required: false
    multivalued: true
  internalReference:
    name: internalReference
    description: Any reference or indication to be used for local retrieval purpose
    from_schema: https://evora-project.eu/
    aliases:
    - internal reference
    rank: 1000
    alias: internalReference
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  note:
    name: note
    description: An aditional information as a textual comment
    from_schema: https://evora-project.eu/
    aliases:
    - note
    rank: 1000
    alias: note
    owner: Service
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  contactPoint:
    name: contactPoint
    description: An information that allows someone to establish communication
    from_schema: https://evora-project.eu/
    aliases:
    - contact point
    exact_mappings:
    - dcat:contactPoint
    rank: 1000
    alias: contactPoint
    owner: Service
    domain_of:
    - PersonOrOrganization
    - ProductOrService
    range: ContactPoint
    required: false
    multivalued: false
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
    owner: Service
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
    owner: Service
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>