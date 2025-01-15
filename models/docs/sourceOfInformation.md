

# Slot: sourceOfInformation



URI: [EVORA:sourceOfInformation](https://evora-project.eu/sourceOfInformation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [AlternateName](AlternateName.md) | List of alternate names for things |  yes  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:sourceOfInformation |
| native | EVORA:sourceOfInformation |




## LinkML Source

<details>
```yaml
name: sourceOfInformation
from_schema: https://evora-project.eu/
rank: 1000
alias: sourceOfInformation
domain_of:
- CommonName
- AlternateName
range: string

```
</details>