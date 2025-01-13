

# Slot: alternateName



URI: [EVORA:alternateName](https://evora-project.eu/alternateName)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  yes  |
| [AlternateName](AlternateName.md) | List of alternate names for things |  yes  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  yes  |
| [RI](RI.md) | A research infrastructure |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:alternateName |
| native | EVORA:alternateName |




## LinkML Source

<details>
```yaml
name: alternateName
from_schema: https://evora-project.eu/
rank: 1000
alias: alternateName
domain_of:
- CommonName
- AlternateName
- Organization
range: string

```
</details>