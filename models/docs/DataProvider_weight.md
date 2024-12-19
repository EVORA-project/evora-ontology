
# Slot: weight

A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0

URI: [EVORA:DataProvider_weight](https://evora-project.eu/DataProvider_weight)


## Domain and Range

[DataProvider](DataProvider.md) &#8594;  <sub>1..1</sub> [Integer](types/Integer.md)

## Parents

 *  is_a: [weight](weight.md)

## Children


## Used by

 * [DataProvider](DataProvider.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | weight |
| **Comments:** | | The lowest weighted Data providers are triggered first, this may be usefull to populate at first entities that are referenced by others (e.g. Version ahead of Rank ahead of Taxon) |
| **Close Mappings:** | | adms:status |