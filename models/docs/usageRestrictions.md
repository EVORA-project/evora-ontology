

# Slot: usage restrictions (usageRestrictions) 


_Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material_





URI: [EVORAO:usageRestrictions](https://w3id.org/evorao/usageRestrictions)
Alias: usageRestrictions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:usageRestrictions |
| native | EVORAO:usageRestrictions |




## LinkML Source

<details>
```yaml
name: usageRestrictions
description: Specifies any limitations or conditions on the use of the biological
  material, including restrictions on research, commercial use, or distribution, considering
  any potential concerns about the related genetic material
title: usage restrictions
from_schema: https://w3id.org/evorao/
rank: 1000
alias: usageRestrictions
domain_of:
- Product
range: string
required: false
multivalued: false

```
</details>