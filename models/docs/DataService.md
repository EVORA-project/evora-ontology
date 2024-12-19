
# Class: DataService

A collection of operations that provides access to one or more datasets or data processing functions

URI: [EVORA:DataService](https://evora-project.eu/DataService)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Nameable],[DataService&#124;name(i):string;description(i):string%20%3F]^-[DataProvider],[Nameable]^-[DataService],[DataProvider])](https://yuml.me/diagram/nofunky;dir:TB/class/[Nameable],[DataService&#124;name(i):string;description(i):string%20%3F]^-[DataProvider],[Nameable]^-[DataService],[DataProvider])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Children

 * [DataProvider](DataProvider.md) - An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources

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
| **Aliases:** | | Data Service |
| **Exact Mappings:** | | dcat:DataService |
| **Close Mappings:** | | wd:Q193424 |
|  | | schema:WebAPI |