

# Slot: risk group (riskGroup) 


_The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual._





URI: [EVORAO:riskGroup](https://w3id.org/evorao/riskGroup)
Alias: riskGroup

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |







## Properties

* Range: [RiskGroup](RiskGroup.md)

* Recommended: True





## Comments

* The Risk Group (RG) assignments to an item are jurisdiction-dependent and may differ between countries/regions and by material form (e.g., live isolate, inactivated preparation, nucleic acid). Assignments can also change over time. We store here a single reference assignment; users must verify the current, locally applicable assignment with their competent authority.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:riskGroup |
| native | EVORAO:riskGroup |
| exact | wdp:P12663 |
| related | bao:0002826 |




## LinkML Source

<details>
```yaml
name: riskGroup
description: The highest risk group related to this resource. The risk group of a
  biological agent guiding its initial handling in labs according to the risk group
  classification defined by the WHO laboratory biosafety manual.
title: risk group
comments:
- The Risk Group (RG) assignments to an item are jurisdiction-dependent and may differ
  between countries/regions and by material form (e.g., live isolate, inactivated
  preparation, nucleic acid). Assignments can also change over time. We store here
  a single reference assignment; users must verify the current, locally applicable
  assignment with their competent authority.
from_schema: https://w3id.org/evorao/
exact_mappings:
- wdp:P12663
related_mappings:
- bao:0002826
rank: 1000
alias: riskGroup
domain_of:
- ProductOrService
range: RiskGroup
required: false
recommended: true
multivalued: false

```
</details>