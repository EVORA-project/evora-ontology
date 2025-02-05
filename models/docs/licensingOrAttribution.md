

# Slot: licensing or attribution (licensingOrAttribution)


_A text or html code that provides any related data sharing licence and/or attribution_





URI: [EVORAO:licensingOrAttribution](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#licensingOrAttribution)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:licensingOrAttribution |
| native | EVORAO:licensingOrAttribution |
| exact | dct:rights |
| close | schema:license |




## LinkML Source

<details>
```yaml
name: licensingOrAttribution
description: A text or html code that provides any related data sharing licence and/or
  attribution
title: licensing or attribution
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dct:rights
close_mappings:
- schema:license
rank: 1000
alias: licensingOrAttribution
domain_of:
- License
range: string
required: false
multivalued: false

```
</details>