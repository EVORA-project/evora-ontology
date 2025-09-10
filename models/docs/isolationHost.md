

# Slot: isolation host (isolationHost) 


_The host organism from which the pathogen was originally isolated_





URI: [EVORAO:isolationHost](https://w3id.org/evorao/isolationHost)
Alias: isolationHost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [IsolationHost](IsolationHost.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:isolationHost |
| native | EVORAO:isolationHost |




## LinkML Source

<details>
```yaml
name: isolationHost
description: The host organism from which the pathogen was originally isolated
title: isolation host
from_schema: https://w3id.org/evorao/
rank: 1000
alias: isolationHost
domain_of:
- Pathogen
range: IsolationHost
required: false
multivalued: true

```
</details>