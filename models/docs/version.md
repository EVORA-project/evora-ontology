

# Slot: version (version) 


_The version indicator (name or identifier) of a resource_





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | A collection of data, published or curated by a single agent, and available f... |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field |  no  |
| [Catalogue](Catalogue.md) | A curated collection of metadata about resources |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of bi... |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Collection](Collection.md) | Set of products and services with some common characteristics |  no  |
| [Version](Version.md) | Numeric code assigned to identify a particular historical version of a work (... |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:version |
| native | EVORAO:version |
| close | wdp:P393, schema:version, wdp:P393, schema:version |




## LinkML Source

<details>
```yaml
name: version
description: The version indicator (name or identifier) of a resource
title: version
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P393
- schema:version
- wdp:P393
- schema:version
rank: 1000
slot_uri: dcat:version
alias: version
domain_of:
- Dataset
- Version
- Taxonomy
range: string
required: true
recommended: true
multivalued: false

```
</details>