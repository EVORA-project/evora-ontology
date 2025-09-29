

# Slot: propagation host (propagationHost) 


_The host organism that propagates the pathogen_





URI: [EVORAO:propagationHost](https://w3id.org/evorao/propagationHost)
Alias: propagationHost

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [PropagationHost](PropagationHost.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:propagationHost |
| native | EVORAO:propagationHost |




## LinkML Source

<details>
```yaml
name: propagationHost
description: The host organism that propagates the pathogen
title: propagation host
from_schema: https://w3id.org/evorao/
rank: 1000
alias: propagationHost
domain_of:
- Pathogen
range: PropagationHost
required: false
multivalued: true

```
</details>