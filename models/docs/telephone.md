

# Slot: telephone (telephone)


_The telephone number_





URI: [EVORAO:telephone](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#telephone)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:telephone |
| native | EVORAO:telephone |
| close | schema:telephone, vcard:telephone |




## LinkML Source

<details>
```yaml
name: telephone
description: The telephone number
title: telephone
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- schema:telephone
- vcard:telephone
rank: 1000
alias: telephone
domain_of:
- ContactPoint
range: string
required: false
recommended: true
multivalued: false

```
</details>