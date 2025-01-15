

# Class: Originator (Originator)


_The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample_





URI: [EVORA:Originator](https://evora-project.eu/Originator)






```mermaid
 classDiagram
    class Originator
    click Originator href "../Originator"
      PersonOrOrganization <|-- Originator
        click PersonOrOrganization href "../PersonOrOrganization"
      
      Originator : contactPoint
        
          
    
    
    Originator --> "0..1" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Originator : description
        
      Originator : homePage
        
      Originator : logo
        
          
    
    
    Originator --> "0..1" Image : logo
    click Image href "../Image"

        
      Originator : name
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
        * **Originator**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [homePage](homePage.md) | 0..1 <br/> [String](String.md) | Refers to the degree of purity achieved for a protein sample | [PersonOrOrganization](PersonOrOrganization.md) |
| [contactPoint](contactPoint.md) | 0..1 <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [PersonOrOrganization](PersonOrOrganization.md) |
| [logo](logo.md) | 0..1 <br/> [Image](Image.md) | A path or URL to the related logo | [PersonOrOrganization](PersonOrOrganization.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





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


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Originator |
| native | EVORA:Originator |
| close | dct:ProvenanceStatement |







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
from_schema: https://evora-project.eu/
close_mappings:
- dct:ProvenanceStatement
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
from_schema: https://evora-project.eu/
close_mappings:
- dct:ProvenanceStatement
is_a: PersonOrOrganization
attributes:
  homePage:
    name: homePage
    description: Refers to the degree of purity achieved for a protein sample. Possible
      values include ">95%" (the protein is highly purified, with more than 95% purity)
      and "Unpurified expression host lysate or partly purified protein" (the protein
      is either unpurified and present in the host cell lysate or only partially purified).
    title: home page
    from_schema: https://evora-project.eu/
    rank: 1000
    alias: homePage
    owner: Originator
    domain_of:
    - PersonOrOrganization
    range: string
    required: false
    multivalued: false
  contactPoint:
    name: contactPoint
    description: An information that allows someone to establish communication
    title: contact point
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dcat:contactPoint
    rank: 1000
    alias: contactPoint
    owner: Originator
    domain_of:
    - PersonOrOrganization
    - ProductOrService
    range: ContactPoint
    required: false
    multivalued: false
  logo:
    name: logo
    description: A path or URL to the related logo
    title: logo
    from_schema: https://evora-project.eu/
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
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Originator
    domain_of:
    - Nameable
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
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Originator
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>