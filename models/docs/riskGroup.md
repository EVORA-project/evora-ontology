

# Slot: risk group (riskGroup) 


_The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual_





URI: [EVORAO:riskGroup](https://w3id.org/evorao/riskGroup)
Alias: riskGroup

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Service](Service.md) | A service |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Product](Product.md) | A product |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [RiskGroup](RiskGroup.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:riskGroup |
| native | EVORAO:riskGroup |
| close | wdp:P12663 |




## LinkML Source

<details>
```yaml
name: riskGroup
description: The highest risk group related to this resource. The risk group of a
  biological agent guiding its initial handling in labs according to the risk group
  classification defined by the WHO laboratory biosafety manual
title: risk group
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P12663
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