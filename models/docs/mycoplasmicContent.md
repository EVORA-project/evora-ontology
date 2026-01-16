

# Slot: mycoplasmic content (mycoplasmicContent) 


_Indicates whether the sample contains mycoplasma contamination. The possible values are 'Not tested', 'Mycoplasma free', 'Contains mycoplasmae', 'Contains mycoplasmae - A protocol to remove mycoplasmae is provided'_





URI: [EVORAO:mycoplasmicContent](https://w3id.org/evorao/mycoplasmicContent)
Alias: mycoplasmicContent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* When it can be assessed, it is recommended to indicate whether mycoplasma contamination was detected or if the test was not performed.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:mycoplasmicContent |
| native | EVORAO:mycoplasmicContent |




## LinkML Source

<details>
```yaml
name: mycoplasmicContent
description: Indicates whether the sample contains mycoplasma contamination. The possible
  values are 'Not tested', 'Mycoplasma free', 'Contains mycoplasmae', 'Contains mycoplasmae
  - A protocol to remove mycoplasmae is provided'
title: mycoplasmic content
comments:
- When it can be assessed, it is recommended to indicate whether mycoplasma contamination
  was detected or if the test was not performed.
from_schema: https://w3id.org/evorao/
rank: 1000
alias: mycoplasmicContent
domain_of:
- Virus
range: string
required: false
recommended: true
multivalued: false
equals_string_in:
- Not tested
- Mycoplasma free
- Contains mycoplasmae
- Contains mycoplasmae - A protocol to remove mycoplasmae is provided

```
</details>