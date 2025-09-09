

# Slot: unit cost (unitCost) 


_The cost per access for one unit as defined by the unit definition_





URI: [EVORAO:unitCost](https://w3id.org/evorao/unitCost)
Alias: unitCost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* The cost per access may not be defined or be specific to a request, so it has to be a xsd:string instead of an xsd:float as initialy suggested to permit description of cost as conditional to what is requested

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:unitCost |
| native | EVORAO:unitCost |




## LinkML Source

<details>
```yaml
name: unitCost
description: The cost per access for one unit as defined by the unit definition
title: unit cost
comments:
- The cost per access may not be defined or be specific to a request, so it has to
  be a xsd:string instead of an xsd:float as initialy suggested to permit description
  of cost as conditional to what is requested
from_schema: https://w3id.org/evorao/
rank: 1000
ifabsent: string(on request)
alias: unitCost
domain_of:
- ProductOrService
range: string
required: true
recommended: true
multivalued: false

```
</details>