

# Slot: version (version) 


_The version indicator (name or identifier) of a resource_





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Collection](Collection.md) | Set of products and services with some common characteristics |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Catalogue](Catalogue.md) | A curated collection of metadata about resources |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Dataset](Dataset.md) | A collection of data, published or curated by a single agent, and available f... |  yes  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field |  no  |
| [Version](Version.md) | Numeric code assigned to identify a particular historical version of a work (... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of bi... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







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