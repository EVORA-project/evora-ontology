

# Class: Natural part origin (NaturalPartOrigin)


_Information on the origin of a natural part that composes the biological material_





URI: [EVORAO:NaturalPartOrigin](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#NaturalPartOrigin)






```mermaid
 classDiagram
    class NaturalPartOrigin
    click NaturalPartOrigin href "../NaturalPartOrigin"
      BiologicalPartOrigin <|-- NaturalPartOrigin
        click BiologicalPartOrigin href "../BiologicalPartOrigin"
      
      NaturalPartOrigin : accessToPhysicalGeneticResource
        
      NaturalPartOrigin : beforeDate
        
      NaturalPartOrigin : collectionDate
        
      NaturalPartOrigin : countryOfCollection
        
          
    
    
    NaturalPartOrigin --> "1" Country : countryOfCollection
    click Country href "../Country"

        
      NaturalPartOrigin : indigenousPoepleAndLocalCommunityOrigin
        
          
    
    
    NaturalPartOrigin --> "0..1" IPLCOrigin : indigenousPoepleAndLocalCommunityOrigin
    click IPLCOrigin href "../IPLCOrigin"

        
      NaturalPartOrigin : permitIdentifierForABS
        
      NaturalPartOrigin : recombinantPartIdentification
        
          
    
    
    NaturalPartOrigin --> "0..1" RecombinantPartIdentification : recombinantPartIdentification
    click RecombinantPartIdentification href "../RecombinantPartIdentification"

        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Dataset](Dataset.md)
        * [BiologicalPartOrigin](BiologicalPartOrigin.md)
            * **NaturalPartOrigin**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [countryOfCollection](countryOfCollection.md) | 1 <br/> [Country](Country.md) | The geographical location where the sample was collected in situ | direct |
| [indigenousPoepleAndLocalCommunityOrigin](indigenousPoepleAndLocalCommunityOrigin.md) | 0..1 <br/> [IPLCOrigin](IPLCOrigin.md) | The specific IPLC area (Indigenous People and Local Communities) from which t... | direct |
| [collectionDate](collectionDate.md) | 1 <br/> [Datetime](Datetime.md) | The date when the sample was collected in situ | direct |
| [beforeDate](beforeDate.md) | 1 <br/> [Boolean](Boolean.md) | Set to TRUE if a proxy date for the collection date is used | direct |
| [permitIdentifierForABS](permitIdentifierForABS.md) | 0..1 <br/> [String](String.md) | Reference of the permit identifiers for access to the genetic resource, appli... | direct |
| [recombinantPartIdentification](recombinantPartIdentification.md) | 0..1 <br/> [RecombinantPartIdentification](RecombinantPartIdentification.md) | Identification of a recombinant part | [BiologicalPartOrigin](BiologicalPartOrigin.md) |
| [accessToPhysicalGeneticResource](accessToPhysicalGeneticResource.md) | 1 <br/> [Boolean](Boolean.md) | Indicate if the biological part was produced with access to a physical geneti... | [BiologicalPartOrigin](BiologicalPartOrigin.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:NaturalPartOrigin |
| native | EVORAO:NaturalPartOrigin |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NaturalPartOrigin
description: Information on the origin of a natural part that composes the biological
  material
title: Natural part origin
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: BiologicalPartOrigin
slots:
- countryOfCollection
- indigenousPoepleAndLocalCommunityOrigin
- collectionDate
- beforeDate
- permitIdentifierForABS
slot_usage:
  countryOfCollection:
    name: countryOfCollection
    description: The geographical location where the sample was collected in situ.
      Used for Nagoya/CBD; equivalent to "country of origin".
    title: country of collection
    close_mappings:
    - dct:spatial
    - dwc:country
    domain_of:
    - NaturalPartOrigin
    range: Country
    required: true
    multivalued: false
  indigenousPoepleAndLocalCommunityOrigin:
    name: indigenousPoepleAndLocalCommunityOrigin
    description: The specific IPLC area (Indigenous People and Local Communities)
      from which this sample/element was sampled, if relevant
    title: indigenous people and local community origin
    domain_of:
    - NaturalPartOrigin
    range: IPLCOrigin
    required: false
    multivalued: false
  collectionDate:
    name: collectionDate
    description: The date when the sample was collected in situ. If unknown/private,
      use a proxy date such as "date received" and indicate this by setting to true
      the before date property
    title: collection date
    domain_of:
    - NaturalPartOrigin
    range: datetime
    required: true
    multivalued: false
  beforeDate:
    name: beforeDate
    description: Set to TRUE if a proxy date for the collection date is used
    title: before date
    ifabsent: 'false'
    domain_of:
    - NaturalPartOrigin
    range: boolean
    required: true
    multivalued: false
  permitIdentifierForABS:
    name: permitIdentifierForABS
    description: Reference of the permit identifiers for access to the genetic resource,
      applicable if the genetic resource falls under Access and Benefit-Sharing (ABS)
      regulations
    title: permit identifier for ABS
    domain_of:
    - NaturalPartOrigin
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: NaturalPartOrigin
description: Information on the origin of a natural part that composes the biological
  material
title: Natural part origin
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: BiologicalPartOrigin
slot_usage:
  countryOfCollection:
    name: countryOfCollection
    description: The geographical location where the sample was collected in situ.
      Used for Nagoya/CBD; equivalent to "country of origin".
    title: country of collection
    close_mappings:
    - dct:spatial
    - dwc:country
    domain_of:
    - NaturalPartOrigin
    range: Country
    required: true
    multivalued: false
  indigenousPoepleAndLocalCommunityOrigin:
    name: indigenousPoepleAndLocalCommunityOrigin
    description: The specific IPLC area (Indigenous People and Local Communities)
      from which this sample/element was sampled, if relevant
    title: indigenous people and local community origin
    domain_of:
    - NaturalPartOrigin
    range: IPLCOrigin
    required: false
    multivalued: false
  collectionDate:
    name: collectionDate
    description: The date when the sample was collected in situ. If unknown/private,
      use a proxy date such as "date received" and indicate this by setting to true
      the before date property
    title: collection date
    domain_of:
    - NaturalPartOrigin
    range: datetime
    required: true
    multivalued: false
  beforeDate:
    name: beforeDate
    description: Set to TRUE if a proxy date for the collection date is used
    title: before date
    ifabsent: 'false'
    domain_of:
    - NaturalPartOrigin
    range: boolean
    required: true
    multivalued: false
  permitIdentifierForABS:
    name: permitIdentifierForABS
    description: Reference of the permit identifiers for access to the genetic resource,
      applicable if the genetic resource falls under Access and Benefit-Sharing (ABS)
      regulations
    title: permit identifier for ABS
    domain_of:
    - NaturalPartOrigin
    required: false
    multivalued: false
attributes:
  countryOfCollection:
    name: countryOfCollection
    description: The geographical location where the sample was collected in situ.
      Used for Nagoya/CBD; equivalent to "country of origin".
    title: country of collection
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:spatial
    - dwc:country
    rank: 1000
    alias: countryOfCollection
    owner: NaturalPartOrigin
    domain_of:
    - NaturalPartOrigin
    range: Country
    required: true
    multivalued: false
  indigenousPoepleAndLocalCommunityOrigin:
    name: indigenousPoepleAndLocalCommunityOrigin
    description: The specific IPLC area (Indigenous People and Local Communities)
      from which this sample/element was sampled, if relevant
    title: indigenous people and local community origin
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: indigenousPoepleAndLocalCommunityOrigin
    owner: NaturalPartOrigin
    domain_of:
    - NaturalPartOrigin
    range: IPLCOrigin
    required: false
    multivalued: false
  collectionDate:
    name: collectionDate
    description: The date when the sample was collected in situ. If unknown/private,
      use a proxy date such as "date received" and indicate this by setting to true
      the before date property
    title: collection date
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: collectionDate
    owner: NaturalPartOrigin
    domain_of:
    - NaturalPartOrigin
    range: datetime
    required: true
    multivalued: false
  beforeDate:
    name: beforeDate
    description: Set to TRUE if a proxy date for the collection date is used
    title: before date
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    ifabsent: 'false'
    alias: beforeDate
    owner: NaturalPartOrigin
    domain_of:
    - NaturalPartOrigin
    range: boolean
    required: true
    multivalued: false
  permitIdentifierForABS:
    name: permitIdentifierForABS
    description: Reference of the permit identifiers for access to the genetic resource,
      applicable if the genetic resource falls under Access and Benefit-Sharing (ABS)
      regulations
    title: permit identifier for ABS
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: permitIdentifierForABS
    owner: NaturalPartOrigin
    domain_of:
    - NaturalPartOrigin
    range: string
    required: false
    multivalued: false
  recombinantPartIdentification:
    name: recombinantPartIdentification
    description: Identification of a recombinant part
    title: recombinant part identification
    comments:
    - Information not required if the current biological part constitutes the complete
      biological material
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: recombinantPartIdentification
    owner: NaturalPartOrigin
    domain_of:
    - BiologicalPartOrigin
    range: RecombinantPartIdentification
    required: false
    multivalued: false
  accessToPhysicalGeneticResource:
    name: accessToPhysicalGeneticResource
    description: Indicate if the biological part was produced with access to a physical
      genetic resource
    title: access to physical genetic resource
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: accessToPhysicalGeneticResource
    owner: NaturalPartOrigin
    domain_of:
    - BiologicalPartOrigin
    range: boolean
    required: true
    multivalued: false

```
</details>