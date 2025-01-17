# Enum: CultivabilityEnumeration



URI: [CultivabilityEnumeration](CultivabilityEnumeration.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Cultivable | None | The pathogen can be grown using standard culture techniques |
| Uncultivable | None | The pathogen cannot be grown in a laboratory using standard culture technique... |
| Inactivated | None | The pathogen has been killed or rendered inactive so it cannot cause disease |




## Slots

| Name | Description |
| ---  | --- |
| [cultivability](cultivability.md) | The ability of the pathogen to be cultivated or grown in laboratory condition... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#






## LinkML Source

<details>
```yaml
name: cultivabilityEnumeration
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
permissible_values:
  Cultivable:
    text: Cultivable
    description: The pathogen can be grown using standard culture techniques
  Uncultivable:
    text: Uncultivable
    description: The pathogen cannot be grown in a laboratory using standard culture
      techniques and often requires special methods for study
  Inactivated:
    text: Inactivated
    description: The pathogen has been killed or rendered inactive so it cannot cause
      disease

```
</details>
