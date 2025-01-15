

# Slot: productPicture



URI: [EVORA:productPicture](https://evora-project.eu/productPicture)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Service](Service.md) | A service |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
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
| self | EVORA:productPicture |
| native | EVORA:productPicture |




## LinkML Source

<details>
```yaml
name: productPicture
from_schema: https://evora-project.eu/
rank: 1000
alias: productPicture
domain_of:
- ProductOrService
range: string

```
</details>