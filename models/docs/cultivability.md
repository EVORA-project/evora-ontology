

# Slot: cultivability (cultivability)


_The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'_





URI: [EVORAO:cultivability](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#cultivability)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* Might also be related to a product sub-category that helps filtering

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:cultivability |
| native | EVORAO:cultivability |




## LinkML Source

<details>
```yaml
name: cultivability
description: The ability of the pathogen to be cultivated or grown in laboratory conditions.
  Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated
  pathogen'
title: cultivability
comments:
- Might also be related to a product sub-category that helps filtering
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
ifabsent: string(Cultivable)
alias: cultivability
domain_of:
- Pathogen
range: string
required: true
multivalued: false
equals_string_in:
- Cultivable
- Uncultivable
- Inactivated

```
</details>