

# Slot: taxon (taxon) 


_Scientifically classified group or entity within the reference taxonomy_





URI: [EVORAO:taxon](https://w3id.org/evorao/taxon)
Alias: taxon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of bi... |  yes  |
| [PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation o... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Required: True





## Comments

* The taxon of the highest rank known that can be used to classify a pathogen or group of pathogens (e.g viruses) in the reference taxonomy

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxon |
| native | EVORAO:taxon |
| related | dwc:Taxon, dwc:Taxon |
| close | schema:taxonomicRange, dwc:taxonID, dwc:toTaxon, schema:taxonomicRange, dwc:taxonID, dwc:toTaxon |




## LinkML Source

<details>
```yaml
name: taxon
description: Scientifically classified group or entity within the reference taxonomy
title: taxon
comments:
- The taxon of the highest rank known that can be used to classify a pathogen or group
  of pathogens (e.g viruses) in the reference taxonomy
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:taxonomicRange
- dwc:taxonID
- dwc:toTaxon
- schema:taxonomicRange
- dwc:taxonID
- dwc:toTaxon
related_mappings:
- dwc:Taxon
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