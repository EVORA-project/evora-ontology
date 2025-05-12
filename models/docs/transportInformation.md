

# Slot: transport information (transportInformation) 


_Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit._





URI: [EVORAO:transportInformation](https://w3id.org/evorao/transportInformation)
Alias: transportInformation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MSDS](MSDS.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:transportInformation |
| native | EVORAO:transportInformation |




## LinkML Source

<details>
```yaml
name: transportInformation
description: Details the regulations and guidelines for safely transporting the product,
  including classifications for road, air, sea, or rail transport, UN numbers, packaging
  requirements, and any special precautions to ensure safe transit.
title: transport information
from_schema: https://w3id.org/evorao/
rank: 1000
alias: transportInformation
domain_of:
- MSDS
range: string
required: false
recommended: true
multivalued: false

```
</details>