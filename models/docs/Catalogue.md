
# Class: Catalogue

A curated collection of metadata about resources

URI: [EVORA:Catalogue](https://evora-project.eu/Catalogue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Taxonomy],[Nameable],[Collection],[Catalogue&#124;name(i):string;description(i):string%20%3F]^-[Vocabulary],[Catalogue]^-[Taxonomy],[Catalogue]^-[Collection],[Nameable]^-[Catalogue])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Taxonomy],[Nameable],[Collection],[Catalogue&#124;name(i):string;description(i):string%20%3F]^-[Vocabulary],[Catalogue]^-[Taxonomy],[Catalogue]^-[Collection],[Nameable]^-[Catalogue])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Children

 * [Collection](Collection.md) - Set of products and services with some common characteristics
 * [Taxonomy](Taxonomy.md) - Science of naming, defining and classifying organisms
 * [Vocabulary](Vocabulary.md) - A subset of words or phrases specific to a particular subject or field

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
| **Aliases:** | | Catalogue |
| **Exact Mappings:** | | dcat:Catalog |
| **Close Mappings:** | | wd:Q2352616 |
|  | | schema:Dataset |