

# Slot: third party distribution consent (thirdPartyDistributionConsent) 


_Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required_





URI: [EVORAO:thirdPartyDistributionConsent](https://w3id.org/evorao/thirdPartyDistributionConsent)
Alias: thirdPartyDistributionConsent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  yes  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:thirdPartyDistributionConsent |
| native | EVORAO:thirdPartyDistributionConsent |




## LinkML Source

<details>
```yaml
name: thirdPartyDistributionConsent
description: Indicates whether the biological material can be distributed without
  restriction to third parties, as indicated by the ABS permit, in case an ABS permit
  is required
title: third party distribution consent
from_schema: https://w3id.org/evorao/
rank: 1000
alias: thirdPartyDistributionConsent
domain_of:
- Product
range: boolean
required: false
multivalued: false

```
</details>