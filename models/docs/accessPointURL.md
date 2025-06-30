

# Slot: access point URL (accessPointURL) 


_The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry_





URI: [EVORAO:accessPointURL](https://w3id.org/evorao/accessPointURL)
Alias: accessPointURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:accessPointURL |
| native | EVORAO:accessPointURL |
| exact | dcat:landingPage |




## LinkML Source

<details>
```yaml
name: accessPointURL
description: The URL that permits to access to the product/service detailed description
  page on the provider's website and/or allows to place an order about it or at least
  describe the process to place an order/enquiry
title: access point URL
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:landingPage
rank: 1000
alias: accessPointURL
domain_of:
- ProductOrService
range: uri
required: true
multivalued: false

```
</details>