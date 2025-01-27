

# Slot: sourceOfInformation



URI: [EVORAO:sourceOfInformation](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#sourceOfInformation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |  no  |
| [AlternateName](AlternateName.md) | List of alternate names for things |  yes  |
| [CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an org... |  yes  |
| [VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sourceOfInformation |
| native | EVORAO:sourceOfInformation |




## LinkML Source

<details>
```yaml
name: sourceOfInformation
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: sourceOfInformation
domain_of:
- CommonName
- AlternateName
range: string

```
</details>