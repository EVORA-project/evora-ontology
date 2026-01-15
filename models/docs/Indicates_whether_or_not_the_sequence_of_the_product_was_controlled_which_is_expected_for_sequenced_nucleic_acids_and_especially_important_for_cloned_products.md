

# Slot: sequence checked (Indicates whether or not the sequence of the product was controlled, which is expected for sequenced nucleic acids and especially important for cloned products) 


_Tell whether or not the sequence of the product was controlled, which is expected for sequenced nucleic acids and especially important for cloned ones._





URI: [EVORAO:Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products](https://w3id.org/evorao/Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products)
Alias: Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  yes  |







## Properties

* Range: [Boolean](Boolean.md)

* Recommended: True





## Comments

* For non-sequenced nucleic acids, the sequenceChecked value cannot be assessed. In all other cases, it is strongly recommended to indicate whether the sequence verification has been performed or not. For cloned products in particular, providing this information is especially meaningful, as sequence verification is a key element in confirming the integrity of the cloned construct and is therefore expected to be documented whenever available.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products |
| native | EVORAO:Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products |
| related | iceo:0000336 |




## LinkML Source

<details>
```yaml
name: Indicates whether or not the sequence of the product was controlled, which is
  expected for sequenced nucleic acids and especially important for cloned products
description: Tell whether or not the sequence of the product was controlled, which
  is expected for sequenced nucleic acids and especially important for cloned ones.
title: sequence checked
comments:
- For non-sequenced nucleic acids, the sequenceChecked value cannot be assessed. In
  all other cases, it is strongly recommended to indicate whether the sequence verification
  has been performed or not. For cloned products in particular, providing this information
  is especially meaningful, as sequence verification is a key element in confirming
  the integrity of the cloned construct and is therefore expected to be documented
  whenever available.
from_schema: https://w3id.org/evorao/
related_mappings:
- iceo:0000336
rank: 1000
alias: Indicates_whether_or_not_the_sequence_of_the_product_was_controlled_which_is_expected_for_sequenced_nucleic_acids_and_especially_important_for_cloned_products
domain_of:
- NucleicAcid
range: boolean
required: false
recommended: true
multivalued: false

```
</details>