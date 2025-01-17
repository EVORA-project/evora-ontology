

# Slot: alternateName



URI: [EVORAO:alternateName](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#alternateName)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  yes  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  yes  |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [RI](RI.md) | A research infrastructure |  no  |
| [AlternateName](AlternateName.md) | List of alternate names for things |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:alternateName |
| native | EVORAO:alternateName |




## LinkML Source

<details>
```yaml
name: alternateName
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: alternateName
domain_of:
- CommonName
- AlternateName
- Organization
range: string

```
</details>