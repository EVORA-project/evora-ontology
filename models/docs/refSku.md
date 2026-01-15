

# Slot: ref SKU (refSku) 


_The reference or the stock keeping unit of the service or item provided in the provider's catalogue._





URI: [EVORAO:refSku](https://w3id.org/evorao/refSku)
Alias: refSku


## Inheritance

* [identifier](identifier.md)
    * **refSku**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:refSku |
| native | EVORAO:refSku |
| exact | schema:sku |
| broad | dct:identifier, schema:identifier |
| close | dwc:catalogNumber |




## LinkML Source

<details>
```yaml
name: refSku
description: The reference or the stock keeping unit of the service or item provided
  in the provider's catalogue.
title: ref SKU
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:sku
close_mappings:
- dwc:catalogNumber
broad_mappings:
- dct:identifier
- schema:identifier
rank: 1000
is_a: identifier
alias: refSku
domain_of:
- ProductOrService
range: string
required: true
multivalued: true

```
</details>