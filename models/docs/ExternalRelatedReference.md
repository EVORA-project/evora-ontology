
# Class: ExternalRelatedReference

A reference that permits to retrieve an item from an external provider

URI: [EVORA:ExternalRelatedReference](https://evora-project.eu/ExternalRelatedReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[ProductOrService]++-%20externalRelatedReference%200..*>[ExternalRelatedReference&#124;reference:string;referenceLabel:string;referenceProviderPrefix:string;referenceProviderName:string],[Dataset]^-[ExternalRelatedReference],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[ProductOrService]++-%20externalRelatedReference%200..*>[ExternalRelatedReference&#124;reference:string;referenceLabel:string;referenceProviderPrefix:string;referenceProviderName:string],[Dataset]^-[ExternalRelatedReference],[Dataset])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞externalRelatedReference](ProductOrService_externalRelatedReference.md)*  <sub>0..\*</sub>  **[ExternalRelatedReference](ExternalRelatedReference.md)**

## Attributes


### Own

 * [ExternalRelatedReference➞reference](ExternalRelatedReference_reference.md)  <sub>1..1</sub>
     * Description: The identifier reference of the connected external item
     * Range: [String](types/String.md)
 * [ExternalRelatedReference➞referenceLabel](ExternalRelatedReference_referenceLabel.md)  <sub>1..1</sub>
     * Description: The label informing what this reference is about
     * Range: [String](types/String.md)
 * [ExternalRelatedReference➞referenceProviderPrefix](ExternalRelatedReference_referenceProviderPrefix.md)  <sub>1..1</sub>
     * Description: The url prefix that once completed with the reference will lead to the linked external resource
     * Range: [String](types/String.md)
 * [ExternalRelatedReference➞referenceProviderName](ExternalRelatedReference_referenceProviderName.md)  <sub>1..1</sub>
     * Description: The name for the reference provider
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | External related reference |