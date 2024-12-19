
# Class: TransmissionMethod

The process by which the pathogen spreads between hosts

URI: [EVORA:TransmissionMethod](https://evora-project.eu/TransmissionMethod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Pathogen]++-%20transmissionMethod%200..*>[TransmissionMethod&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[TransmissionMethod],[Term],[Pathogen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Pathogen]++-%20transmissionMethod%200..*>[TransmissionMethod&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[TransmissionMethod],[Term],[Pathogen])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[Pathogen](Pathogen.md)** *[Pathogen➞transmissionMethod](Pathogen_transmissionMethod.md)*  <sub>0..\*</sub>  **[TransmissionMethod](TransmissionMethod.md)**

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
| **Aliases:** | | Transmission method |