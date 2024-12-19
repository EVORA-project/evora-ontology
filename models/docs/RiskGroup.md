
# Class: RiskGroup

Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence

URI: [EVORA:RiskGroup](https://evora-project.eu/RiskGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[ProductOrService]++-%20riskGroup%200..1>[RiskGroup&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[RiskGroup],[ProductOrService])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[ProductOrService]++-%20riskGroup%200..1>[RiskGroup&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[RiskGroup],[ProductOrService])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞riskGroup](ProductOrService_riskGroup.md)*  <sub>0..1</sub>  **[RiskGroup](RiskGroup.md)**

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
| **Aliases:** | | Risk group |
| **Comments:** | | Use of Data provider if any or manual import of information from wd:Q125449389, wd:Q125449412, wd:Q125449429, wd:Q125449439 |
| **Close Mappings:** | | wd:Q125449255 |