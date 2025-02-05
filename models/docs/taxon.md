

# Slot: taxon (taxon)


_Scientifically classified group or entity within the reference taxonomy_





URI: [EVORAO:taxon](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#taxon)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxonomy](Taxonomy.md) | Science of naming, defining and classifying organisms |  yes  |
| [PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation o... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Required: True





## Comments

* The taxon of the highest rank known that can be used to classify a pathogen or group of pathogens (e.g viruses) in the reference taxonomy

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxon |
| native | EVORAO:taxon |
| close | dwc:Taxon |




## LinkML Source

<details>
```yaml
name: taxon
description: Scientifically classified group or entity within the reference taxonomy
title: taxon
comments:
- The taxon of the highest rank known that can be used to classify a pathogen or group
  of pathogens (e.g viruses) in the reference taxonomy
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dwc:Taxon
rank: 1000
alias: taxon
domain_of:
- Taxonomy
- PathogenIdentification
range: Taxon
required: true
multivalued: false

```
</details>