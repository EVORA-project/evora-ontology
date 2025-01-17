# Enum: ExpressionSystemEnumeration



URI: [ExpressionSystemEnumeration](ExpressionSystemEnumeration.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| E. coli | wd:Q25419 | Expressed in E |
| Insect cells | wd:Q108929499 | Expressed in insect cells |
| Mammalian cells | None | Expressed in mammalian cells |




## Slots

| Name | Description |
| ---  | --- |
| [expressionSystem](expressionSystem.md) | The host organism or cellular environment used to produce a protein from a sp... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#






## LinkML Source

<details>
```yaml
name: expressionSystemEnumeration
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
permissible_values:
  E. coli:
    text: E. coli
    description: Expressed in E. Coli bacteria
    meaning: wd:Q25419
  Insect cells:
    text: Insect cells
    description: Expressed in insect cells
    meaning: wd:Q108929499
  Mammalian cells:
    text: Mammalian cells
    description: Expressed in mammalian cells

```
</details>
