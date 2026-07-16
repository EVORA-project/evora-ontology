

# Slot: antibody characterization method (antibodyCharacterizationMethod) 


_A method used to determine the specificity, affinity, or functionality of an antibody or antiserum._





URI: [EVORAO:antibodyCharacterizationMethod](https://w3id.org/evorao/antibodyCharacterizationMethod)
Alias: antibodyCharacterizationMethod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:antibodyCharacterizationMethod |
| native | EVORAO:antibodyCharacterizationMethod |




## LinkML Source

<details>
```yaml
name: antibodyCharacterizationMethod
description: A method used to determine the specificity, affinity, or functionality
  of an antibody or antiserum.
title: antibody characterization method
from_schema: https://w3id.org/evorao/
rank: 1000
alias: antibodyCharacterizationMethod
domain_of:
- Antibody
range: string
required: false
multivalued: true
equals_string_in:
- Western blot
- ELISA
- IFA
- Neutralisation
- Immunoprecipitation
- Biophysical method

```
</details>