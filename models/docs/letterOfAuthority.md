

# Slot: letter of authority (letterOfAuthority) 


_Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'_





URI: [EVORAO:letterOfAuthority](https://w3id.org/evorao/letterOfAuthority)
Alias: letterOfAuthority

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:letterOfAuthority |
| native | EVORAO:letterOfAuthority |




## LinkML Source

<details>
```yaml
name: letterOfAuthority
description: Indicate whether a Letter of Authority is required, confirming the necessity
  of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required
  for customers in the EU' or 'Required'
title: letter of authority
from_schema: https://w3id.org/evorao/
rank: 1000
ifabsent: string(Not applicable)
alias: letterOfAuthority
domain_of:
- Pathogen
range: string
required: true
multivalued: false
equals_string_in:
- Not applicable
- Not required
- Required for customers in the EU
- Required

```
</details>