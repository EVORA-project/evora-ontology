
# Class: IATAClassification

The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air

URI: [EVORA:IATAClassification](https://evora-project.eu/IATAClassification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Product],[Product]++-%20hasIATAClassification%201..1>[IATAClassification&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[IATAClassification])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Product],[Product]++-%20hasIATAClassification%201..1>[IATAClassification&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[IATAClassification])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[Product](Product.md)** *[Product➞hasIATAClassification](Product_hasIATAClassification.md)*  <sub>1..1</sub>  **[IATAClassification](IATAClassification.md)**

## Attributes


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
| **Aliases:** | | IATA classification |