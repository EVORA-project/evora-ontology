# Enum: SequenceProviderEnumeration



URI: [SequenceProviderEnumeration](SequenceProviderEnumeration.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ENA | wd:Q5412874 | The European Nucleotide Archive |
| GenBank | wd:Q901755 | The NIH genetic sequence database, an annotated collection of all publicly av... |




## Slots

| Name | Description |
| ---  | --- |
| [sequenceProvider](sequenceProvider.md) | The name of the sequence provider within the list of accepted sequence provid... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#






## LinkML Source

<details>
```yaml
name: sequenceProviderEnumeration
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
permissible_values:
  ENA:
    text: ENA
    description: The European Nucleotide Archive
    meaning: wd:Q5412874
  GenBank:
    text: GenBank
    description: The NIH genetic sequence database, an annotated collection of all
      publicly available DNA sequences
    meaning: wd:Q901755

```
</details>
