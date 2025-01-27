

# Class: External related reference (ExternalRelatedReference)


_A reference that permits to retrieve an item from an external provider_





URI: [EVORAO:ExternalRelatedReference](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#ExternalRelatedReference)






```mermaid
 classDiagram
    class ExternalRelatedReference
    click ExternalRelatedReference href "../ExternalRelatedReference"
      Resource <|-- ExternalRelatedReference
        click Resource href "../Resource"
      
      ExternalRelatedReference : reference
        
      ExternalRelatedReference : referenceLabel
        
      ExternalRelatedReference : referenceProviderName
        
      ExternalRelatedReference : referenceProviderPrefix
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **ExternalRelatedReference**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [reference](reference.md) | 1 <br/> [String](String.md) | The identifier reference of the connected external item | direct |
| [referenceLabel](referenceLabel.md) | 1 <br/> [String](String.md) | The label informing what this reference is about | direct |
| [referenceProviderPrefix](referenceProviderPrefix.md) | 1 <br/> [String](String.md) | The url prefix that once completed with the reference will lead to the linked... | direct |
| [referenceProviderName](referenceProviderName.md) | 1 <br/> [String](String.md) | The name for the reference provider | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProductOrService](ProductOrService.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Service](Service.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Product](Product.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Antibody](Antibody.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Hybridoma](Hybridoma.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Protein](Protein.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [NucleicAcid](NucleicAcid.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [DetectionKit](DetectionKit.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Bundle](Bundle.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Pathogen](Pathogen.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Virus](Virus.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Bacterium](Bacterium.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Fungus](Fungus.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Protozoan](Protozoan.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Viroid](Viroid.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |
| [Prion](Prion.md) | [externalRelatedReference](externalRelatedReference.md) | range | [ExternalRelatedReference](ExternalRelatedReference.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:ExternalRelatedReference |
| native | EVORAO:ExternalRelatedReference |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExternalRelatedReference
description: A reference that permits to retrieve an item from an external provider
title: External related reference
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: Resource
slots:
- reference
- referenceLabel
- referenceProviderPrefix
- referenceProviderName
slot_usage:
  reference:
    name: reference
    description: The identifier reference of the connected external item
    title: reference
    close_mappings:
    - dct:identifier
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceLabel:
    name: referenceLabel
    description: The label informing what this reference is about
    title: reference label
    comments:
    - e.g., 'Infravec2 related product'
    close_mappings:
    - dct:title
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderPrefix:
    name: referenceProviderPrefix
    description: The url prefix that once completed with the reference will lead to
      the linked external resource
    title: reference provider prefix
    close_mappings:
    - dcat:landingPage
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderName:
    name: referenceProviderName
    description: The name for the reference provider
    title: reference provider name
    close_mappings:
    - dct:publisher
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: ExternalRelatedReference
description: A reference that permits to retrieve an item from an external provider
title: External related reference
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: Resource
slot_usage:
  reference:
    name: reference
    description: The identifier reference of the connected external item
    title: reference
    close_mappings:
    - dct:identifier
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceLabel:
    name: referenceLabel
    description: The label informing what this reference is about
    title: reference label
    comments:
    - e.g., 'Infravec2 related product'
    close_mappings:
    - dct:title
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderPrefix:
    name: referenceProviderPrefix
    description: The url prefix that once completed with the reference will lead to
      the linked external resource
    title: reference provider prefix
    close_mappings:
    - dcat:landingPage
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderName:
    name: referenceProviderName
    description: The name for the reference provider
    title: reference provider name
    close_mappings:
    - dct:publisher
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
attributes:
  reference:
    name: reference
    description: The identifier reference of the connected external item
    title: reference
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:identifier
    rank: 1000
    alias: reference
    owner: ExternalRelatedReference
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceLabel:
    name: referenceLabel
    description: The label informing what this reference is about
    title: reference label
    comments:
    - e.g., 'Infravec2 related product'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:title
    rank: 1000
    alias: referenceLabel
    owner: ExternalRelatedReference
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderPrefix:
    name: referenceProviderPrefix
    description: The url prefix that once completed with the reference will lead to
      the linked external resource
    title: reference provider prefix
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dcat:landingPage
    rank: 1000
    alias: referenceProviderPrefix
    owner: ExternalRelatedReference
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false
  referenceProviderName:
    name: referenceProviderName
    description: The name for the reference provider
    title: reference provider name
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:publisher
    rank: 1000
    alias: referenceProviderName
    owner: ExternalRelatedReference
    domain_of:
    - ExternalRelatedReference
    range: string
    required: true
    multivalued: false

```
</details>