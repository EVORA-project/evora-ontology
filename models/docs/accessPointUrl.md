

# Slot: access point URL (accessPointUrl) 


_The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry_





URI: [EVORAO:accessPointUrl](https://w3id.org/evorao/accessPointUrl)
Alias: accessPointUrl

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:accessPointUrl |
| native | EVORAO:accessPointUrl |
| exact | schema:serviceURL |
| broad | schema:url |
| related | dcat:landingPage |




## LinkML Source

<details>
```yaml
name: accessPointUrl
description: The URL that permits to access to the product/service detailed description
  page on the provider's website and/or allows to place an order about it or at least
  describe the process to place an order/enquiry
title: access point URL
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:serviceURL
related_mappings:
- dcat:landingPage
broad_mappings:
- schema:url
rank: 1000
alias: accessPointUrl
domain_of:
- ProductOrService
range: uri
required: true
multivalued: false

```
</details>