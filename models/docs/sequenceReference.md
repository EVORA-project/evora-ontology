

# Slot: sequenceReference



URI: [EVORA:sequenceReference](https://evora-project.eu/sequenceReference)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sequence](Sequence.md) | A nucleic acid or protein sequence information |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:sequenceReference |
| native | EVORA:sequenceReference |




## LinkML Source

<details>
```yaml
name: sequenceReference
from_schema: https://evora-project.eu/
rank: 1000
alias: sequenceReference
domain_of:
- Sequence
- Antibody
range: string

```
</details>