

# Slot: taxonomy



URI: [EVORA:taxonomy](https://evora-project.eu/taxonomy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |  yes  |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:taxonomy |
| native | EVORA:taxonomy |




## LinkML Source

<details>
```yaml
name: taxonomy
from_schema: https://evora-project.eu/
rank: 1000
alias: taxonomy
domain_of:
- TaxonomicRank
- Taxon
range: string

```
</details>