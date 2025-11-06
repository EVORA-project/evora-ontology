

# Slot: unit cost (unitCost) 


_The cost per access for one unit as defined by the unit definition_





URI: [EVORAO:unitCost](https://w3id.org/evorao/unitCost)
Alias: unitCost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |







## Properties

* Range: [Decimal](Decimal.md)

* Recommended: True





## Comments

* The cost per access may not always be defined as a fixed numerical value. In some cases, the price is conditional or available only upon request. To accommodate such cases, descriptive information should be provided through the property EVORAO:unitCostNote (xsd:string). This allows handling of cost statements such as “on request,” “depends on volume,” or “free access for academics,” which cannot be captured by a simple numeric value.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:unitCost |
| native | EVORAO:unitCost |
| close | schema:price |




## LinkML Source

<details>
```yaml
name: unitCost
description: The cost per access for one unit as defined by the unit definition
title: unit cost
comments:
- The cost per access may not always be defined as a fixed numerical value. In some
  cases, the price is conditional or available only upon request. To accommodate such
  cases, descriptive information should be provided through the property EVORAO:unitCostNote
  (xsd:string). This allows handling of cost statements such as “on request,” “depends
  on volume,” or “free access for academics,” which cannot be captured by a simple
  numeric value.
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:price
rank: 1000
alias: unitCost
domain_of:
- ProductOrService
range: decimal
required: false
recommended: true
multivalued: false

```
</details>