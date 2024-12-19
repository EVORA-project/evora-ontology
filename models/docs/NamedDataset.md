
# Class: NamedDataset

A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access

URI: [EVORA:NamedDataset](https://evora-project.eu/NamedDataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[ProductOrService],[NamedDataset&#124;name(i):string;description(i):string%20%3F]^-[Term],[NamedDataset]^-[ProductOrService],[Nameable]^-[NamedDataset],[Nameable])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[ProductOrService],[NamedDataset&#124;name(i):string;description(i):string%20%3F]^-[Term],[NamedDataset]^-[ProductOrService],[Nameable]^-[NamedDataset],[Nameable])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Children

 * [ProductOrService](ProductOrService.md) - A product or a service
 * [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class


## Attributes


### Inherited from Nameable:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Named Dataset |
| **Exact Mappings:** | | dcat:Dataset |
| **Close Mappings:** | | wd:Q1172284 |
|  | | schema:DataCatalog |