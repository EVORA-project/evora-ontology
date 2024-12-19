
# Class: Collection

Set of products and services with some common characteristics

URI: [EVORA:Collection](https://evora-project.eu/Collection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[DataProvider],[DataProvider]<collectionDataProvider%200..1-++[Collection&#124;name(i):string;description(i):string%20%3F],[ProductOrService]<collectionItem%200..*-++[Collection],[ProductOrService]++-%20collection%201..*>[Collection],[Catalogue]^-[Collection],[Catalogue])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[DataProvider],[DataProvider]<collectionDataProvider%200..1-++[Collection&#124;name(i):string;description(i):string%20%3F],[ProductOrService]<collectionItem%200..*-++[Collection],[ProductOrService]++-%20collection%201..*>[Collection],[Catalogue]^-[Collection],[Catalogue])

## Parents

 *  is_a: [Catalogue](Catalogue.md) - A curated collection of metadata about resources

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞collection](ProductOrService_collection.md)*  <sub>1..\*</sub>  **[Collection](Collection.md)**

## Attributes


### Own

 * [Collection➞collectionItem](Collection_collectionItem.md)  <sub>0..\*</sub>
     * Description: An item of the collection
     * Range: [ProductOrService](ProductOrService.md)
 * [Collection➞collectionDataProvider](Collection_collectionDataProvider.md)  <sub>0..1</sub>
     * Description: The provider of the data of the collection
     * Range: [DataProvider](DataProvider.md)

### Inherited from Catalogue:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Collection |
| **Close Mappings:** | | wd:Q2668072 |