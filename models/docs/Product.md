
# Class: Product

A product

URI: [EVORA:Product](https://evora-project.eu/Product)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RiskGroup],[Provider],[Protein],[ProductOrService],[ProductCategory],[Originator]<originator%200..1-++[Product&#124;shippingConditions:string;storageConditions:string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[MSDS]<materialSafetyDataSheet%200..1-++[Product],[IATAClassification]<hasIATAClassification%201..1-++[Product],[Bundle]++-%20productsOfTheBundle%201..*>[Product],[Product]^-[Protein],[Product]^-[Pathogen],[Product]^-[NucleicAcid],[Product]^-[DetectionKit],[Product]^-[Bundle],[Product]^-[Antibody],[ProductOrService]^-[Product],[PathogenIdentification],[Pathogen],[Originator],[NucleicAcid],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[Document],[DetectionKit],[DOI],[ContactPoint],[Collection],[Certification],[Bundle],[Antibody])](https://yuml.me/diagram/nofunky;dir:TB/class/[RiskGroup],[Provider],[Protein],[ProductOrService],[ProductCategory],[Originator]<originator%200..1-++[Product&#124;shippingConditions:string;storageConditions:string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[MSDS]<materialSafetyDataSheet%200..1-++[Product],[IATAClassification]<hasIATAClassification%201..1-++[Product],[Bundle]++-%20productsOfTheBundle%201..*>[Product],[Product]^-[Protein],[Product]^-[Pathogen],[Product]^-[NucleicAcid],[Product]^-[DetectionKit],[Product]^-[Bundle],[Product]^-[Antibody],[ProductOrService]^-[Product],[PathogenIdentification],[Pathogen],[Originator],[NucleicAcid],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[Document],[DetectionKit],[DOI],[ContactPoint],[Collection],[Certification],[Bundle],[Antibody])

## Parents

 *  is_a: [ProductOrService](ProductOrService.md) - A product or a service

## Children

 * [Antibody](Antibody.md) - Protein that can bind to certain types of foreign bodies, such as pathogens
 * [Bundle](Bundle.md) - A group of products
 * [DetectionKit](DetectionKit.md) - A detection kit for specific pathogens
 * [NucleicAcid](NucleicAcid.md) - Nucleic acid related to a pathogen. It can be extracted or synthetic
 * [Pathogen](Pathogen.md) - Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus
 * [Protein](Protein.md) - A protein as a derived product from a pathogen

## Referenced by Class

 *  **[Bundle](Bundle.md)** *[Bundle➞productsOfTheBundle](Bundle_productsOfTheBundle.md)*  <sub>1..\*</sub>  **[Product](Product.md)**

## Attributes


### Own

 * [Product➞hasIATAClassification](Product_hasIATAClassification.md)  <sub>1..1</sub>
     * Description: The corresponding International Air Transport Association (IATA)'s category for this Product
     * Range: [IATAClassification](IATAClassification.md)
 * [Product➞shippingConditions](Product_shippingConditions.md)  <sub>1..1</sub>
     * Description: Specification of the terms and parameters for transporting

     * Range: [String](types/String.md)
 * [Product➞materialSafetyDataSheet](Product_materialSafetyDataSheet.md)  <sub>0..1</sub>
     * Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
     * Range: [MSDS](MSDS.md)
 * [Product➞originator](Product_originator.md)  <sub>0..1</sub>
     * Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
     * Range: [Originator](Originator.md)
 * [Product➞storageConditions](Product_storageConditions.md)  <sub>1..1</sub>
     * Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
     * Range: [String](types/String.md)

### Inherited from ProductOrService:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)
 * [ProductOrService➞accessPointURL](ProductOrService_accessPointURL.md)  <sub>1..1</sub>
     * Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
     * Range: [Uri](types/Uri.md)
 * [ProductOrService➞refSKU](ProductOrService_refSKU.md)  <sub>1..1</sub>
     * Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
     * Range: [String](types/String.md)
 * [ProductOrService➞unitDefinition](ProductOrService_unitDefinition.md)  <sub>0..1</sub>
     * Description: A short description of what will be delivered by ordering one unit of this item
     * Range: [String](types/String.md)
 * [ProductOrService➞category](ProductOrService_category.md)  <sub>1..1</sub>
     * Description: The main category of the service or product
     * Range: [ProductCategory](ProductCategory.md)
 * [ProductOrService➞additionalCategory](ProductOrService_additionalCategory.md)  <sub>0..\*</sub>
     * Description: Any category apart from its main category in which this product or service can fit
     * Range: [ProductCategory](ProductCategory.md)
 * [ProductOrService➞unitCost](ProductOrService_unitCost.md)  <sub>1..1</sub>
     * Description: The cost per access for one unit as defined by the unit definition
     * Range: [String](types/String.md)
 * [ProductOrService➞qualityGrading](ProductOrService_qualityGrading.md)  <sub>0..1</sub>
     * Description: Information that permits to assess the quality level of what will be provided
     * Range: [String](types/String.md)
 * [ProductOrService➞pathogenIdentification](ProductOrService_pathogenIdentification.md)  <sub>1..\*</sub>
     * Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
     * Range: [PathogenIdentification](PathogenIdentification.md)
 * [ProductOrService➞relatedDOI](ProductOrService_relatedDOI.md)  <sub>0..\*</sub>
     * Description: Any DOI that can be related
     * Range: [DOI](DOI.md)
 * [ProductOrService➞riskGroup](ProductOrService_riskGroup.md)  <sub>0..1</sub>
     * Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
     * Range: [RiskGroup](RiskGroup.md)
 * [ProductOrService➞biosafetyRestrictions](ProductOrService_biosafetyRestrictions.md)  <sub>0..1</sub>
     * Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
     * Range: [String](types/String.md)
 * [ProductOrService➞canItBeUsedToProduceGMO](ProductOrService_canItBeUsedToProduceGMO.md)  <sub>0..1</sub>
     * Description: Indicates if the current service or product can be used to produce GMO
     * Range: [Boolean](types/Boolean.md)
 * [ProductOrService➞provider](ProductOrService_provider.md)  <sub>1..1</sub>
     * Description: A provider of this product or service, as a specific organization
     * Range: [Provider](Provider.md)
 * [ProductOrService➞collection](ProductOrService_collection.md)  <sub>1..\*</sub>
     * Description: The collection(s) to which belongs this item
     * Range: [Collection](Collection.md)
 * [ProductOrService➞keywords](ProductOrService_keywords.md)  <sub>1..\*</sub>
     * Description: List of terms used to tag and categorize this Item
     * Range: [Keyword](Keyword.md)
 * [ProductOrService➞availability](ProductOrService_availability.md)  <sub>1..1</sub>
     * Description: The state or condition in which this item is accessible and ready for use or can be obtained
     * Range: [String](types/String.md)
 * [ProductOrService➞complementaryDocument](ProductOrService_complementaryDocument.md)  <sub>0..\*</sub>
     * Description: Any complementary document that can be related to this Item
     * Range: [Document](Document.md)
 * [ProductOrService➞technicalRecommendation](ProductOrService_technicalRecommendation.md)  <sub>0..1</sub>
     * Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
     * Range: [String](types/String.md)
 * [ProductOrService➞productPicture](ProductOrService_productPicture.md)  <sub>0..\*</sub>
     * Description: A picture that can represent the item
     * Range: [Image](Image.md)
 * [ProductOrService➞externalRelatedReference](ProductOrService_externalRelatedReference.md)  <sub>0..\*</sub>
     * Description: A reference that permits to retrieve another related item from an external provider
     * Range: [ExternalRelatedReference](ExternalRelatedReference.md)
 * [ProductOrService➞certification](ProductOrService_certification.md)  <sub>0..\*</sub>
     * Description: Any certification related to the current product or service; e.g., ISO certification
     * Range: [Certification](Certification.md)
 * [ProductOrService➞internalReference](ProductOrService_internalReference.md)  <sub>0..1</sub>
     * Description: Any reference or indication to be used for local retrieval purpose
     * Range: [String](types/String.md)
 * [ProductOrService➞note](ProductOrService_note.md)  <sub>0..1</sub>
     * Description: An aditional information as a textual comment
     * Range: [String](types/String.md)
 * [ProductOrService➞contactPoint](ProductOrService_contactPoint.md)  <sub>0..1</sub>
     * Description: An information that allows someone to establish communication
     * Range: [ContactPoint](ContactPoint.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Product |
| **Close Mappings:** | | wd:Q2424752 |