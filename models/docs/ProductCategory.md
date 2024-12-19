
# Class: ProductCategory

A term used to classify a group of products that share common characteristics or functions, which helps in their organization

URI: [EVORA:ProductCategory](https://evora-project.eu/ProductCategory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[ProductOrService],[ProductCategory]<parentCategory%200..1-++[ProductCategory&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[ProductOrService]++-%20additionalCategory%200..*>[ProductCategory],[ProductOrService]++-%20category%201..1>[ProductCategory],[Term]^-[ProductCategory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[ProductOrService],[ProductCategory]<parentCategory%200..1-++[ProductCategory&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[ProductOrService]++-%20additionalCategory%200..*>[ProductCategory],[ProductOrService]++-%20category%201..1>[ProductCategory],[Term]^-[ProductCategory])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[ProductCategory](ProductCategory.md)** *[ProductCategory➞parentCategory](ProductCategory_parentCategory.md)*  <sub>0..1</sub>  **[ProductCategory](ProductCategory.md)**
 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞additionalCategory](ProductOrService_additionalCategory.md)*  <sub>0..\*</sub>  **[ProductCategory](ProductCategory.md)**
 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞category](ProductOrService_category.md)*  <sub>1..1</sub>  **[ProductCategory](ProductCategory.md)**

## Attributes


### Own

 * [ProductCategory➞parentCategory](ProductCategory_parentCategory.md)  <sub>0..1</sub>
     * Description: An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.
     * Range: [ProductCategory](ProductCategory.md)

### Inherited from Term:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)
 * [Term➞weight](Term_weight.md)  <sub>1..1</sub>
     * Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
     * Range: [Integer](types/Integer.md)
 * [Term➞inVocabulary](Term_inVocabulary.md)  <sub>1..1</sub>
     * Description: Terms belong to a specific vocabulary
     * Range: [Vocabulary](Vocabulary.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Product category |
| **Close Mappings:** | | wd:Q63981612 |