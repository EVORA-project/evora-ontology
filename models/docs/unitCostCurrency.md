

# Slot: unit cost currency (unitCostCurrency) 


_The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)._





URI: [EVORAO:unitCostCurrency](https://w3id.org/evorao/unitCostCurrency)
Alias: unitCostCurrency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:unitCostCurrency |
| native | EVORAO:unitCostCurrency |
| close | schema:priceCurrency |




## LinkML Source

<details>
```yaml
name: unitCostCurrency
description: The currency in which the unit cost is expressed, following ISO 4217
  three-letter codes (e.g., EUR, USD).
title: unit cost currency
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:priceCurrency
rank: 1000
ifabsent: string(EUR)
alias: unitCostCurrency
domain_of:
- ProductOrService
range: string
required: false
recommended: true
multivalued: false

```
</details>