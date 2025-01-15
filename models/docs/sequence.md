

# Slot: sequence



URI: [EVORA:sequence](https://evora-project.eu/sequence)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [RecombinantPartIdentification](RecombinantPartIdentification.md) | Identification of a recombinant part |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:sequence |
| native | EVORA:sequence |




## LinkML Source

<details>
```yaml
name: sequence
from_schema: https://evora-project.eu/
rank: 1000
alias: sequence
domain_of:
- RecombinantPartIdentification
- Protein
- Nucleic Acid
- Pathogen
range: string

```
</details>