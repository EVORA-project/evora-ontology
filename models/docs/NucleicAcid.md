
# Class: Nucleic Acid

Nucleic acid related to a pathogen. It can be extracted or synthetic

URI: [EVORA:NucleicAcid](https://evora-project.eu/NucleicAcid)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[RiskGroup],[Provider],[ProteinTag],[ProductCategory],[Product],[PlasmidSelection],[PathogenIdentification],[Originator],[ProteinTag]<hasTAG%201..1-++[NucleicAcid&#124;isItAClonedNucleicAcid:boolean;regionEncompassedInThisProduct:string;mutationObserved:boolean;observedMutations:string%20%3F;identificationTechnique:string%20%3F;sequencing:string;titer:string%20%3F;sequenceChecked:boolean;shippingConditions(i):string;storageConditions(i):string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[PlasmidSelection]<pasmidSelection%200..*-++[NucleicAcid],[ExpressionVector]<clonedIntoPlasmid%200..1-++[NucleicAcid],[Sequence]<sequence%201..*-++[NucleicAcid],[Data]<hasGbFileOfTheConstruct%200..*-++[NucleicAcid],[BiologicalMaterialOrigin]<biologicalMaterialOrigin%201..1-++[NucleicAcid],[Product]^-[NucleicAcid],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[ExpressionVector],[Document],[Data],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[RiskGroup],[Provider],[ProteinTag],[ProductCategory],[Product],[PlasmidSelection],[PathogenIdentification],[Originator],[ProteinTag]<hasTAG%201..1-++[NucleicAcid&#124;isItAClonedNucleicAcid:boolean;regionEncompassedInThisProduct:string;mutationObserved:boolean;observedMutations:string%20%3F;identificationTechnique:string%20%3F;sequencing:string;titer:string%20%3F;sequenceChecked:boolean;shippingConditions(i):string;storageConditions(i):string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[PlasmidSelection]<pasmidSelection%200..*-++[NucleicAcid],[ExpressionVector]<clonedIntoPlasmid%200..1-++[NucleicAcid],[Sequence]<sequence%201..*-++[NucleicAcid],[Data]<hasGbFileOfTheConstruct%200..*-++[NucleicAcid],[BiologicalMaterialOrigin]<biologicalMaterialOrigin%201..1-++[NucleicAcid],[Product]^-[NucleicAcid],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[ExpressionVector],[Document],[Data],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])

## Parents

 *  is_a: [Product](Product.md) - A product

## Referenced by Class


## Attributes


### Own

 * [Nucleic Acid➞biologicalMaterialOrigin](Nucleic_Acid_biologicalMaterialOrigin.md)  <sub>1..1</sub>
     * Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
     * Range: [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)
 * [Nucleic Acid➞hasGbFileOfTheConstruct](Nucleic_Acid_hasGbFileOfTheConstruct.md)  <sub>0..\*</sub>
     * Description: A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct
     * Range: [Data](Data.md)
 * [Nucleic Acid➞sequence](Nucleic_Acid_sequence.md)  <sub>1..\*</sub>
     * Description: The related sequence information from a sequence provider or in fasta format
     * Range: [Sequence](Sequence.md)
 * [Nucleic Acid➞isItAClonedNucleicAcid](Nucleic_Acid_isItAClonedNucleicAcid.md)  <sub>1..1</sub>
     * Description: Indicates that the nucleic acid sequence has been inserted into a plasmid vector for propagation or expression in a host organism
     * Range: [Boolean](types/Boolean.md)
 * [Nucleic Acid➞clonedIntoPlasmid](Nucleic_Acid_clonedIntoPlasmid.md)  <sub>0..1</sub>
     * Description: The plasmid into which the nucleic acid has been cloned
     * Range: [ExpressionVector](ExpressionVector.md)
 * [Nucleic Acid➞pasmidSelection](Nucleic_Acid_pasmidSelection.md)  <sub>0..\*</sub>
     * Description: Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid
     * Range: [PlasmidSelection](PlasmidSelection.md)
 * [Nucleic Acid➞hasTAG](Nucleic_Acid_hasTAG.md)  <sub>1..1</sub>
     * Description: TAG sequence used for purposes such as purification, detection, or localization
     * Range: [ProteinTag](ProteinTag.md)
 * [Nucleic Acid➞regionEncompassedInThisProduct](Nucleic_Acid_regionEncompassedInThisProduct.md)  <sub>1..1</sub>
     * Description: The specific region encompassed in the product
     * Range: [String](types/String.md)
 * [Nucleic Acid➞mutationObserved](Nucleic_Acid_mutationObserved.md)  <sub>1..1</sub>
     * Description: Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it
 contains mutations (no frameshift, no unexpected STOP codon) if set to true
     * Range: [Boolean](types/Boolean.md)
 * [Nucleic Acid➞observedMutations](Nucleic_Acid_observedMutations.md)  <sub>0..1</sub>
     * Description: The specific mutations that have been identified and documented in the nucleic acid sequence
     * Range: [String](types/String.md)
 * [Nucleic Acid➞identificationTechnique](Nucleic_Acid_identificationTechnique.md)  <sub>0..1</sub>
     * Description: The method used to identify the nucleic acid sequence or its associated constructs, such as PCR, sequencing, or hybridization
     * Range: [String](types/String.md)
 * [Nucleic Acid➞sequencing](Nucleic_Acid_sequencing.md)  <sub>1..1</sub>
     * Description: Refers to the level of sequencing performed on the nucleic acid. Possible values include "Not sequenced" (no sequencing has been performed), "Partly sequenced" (only a portion of the nucleic acid sequence has been determined), and "Fully sequenced" (the entire nucleic acid sequence has been determined).
     * Range: [String](types/String.md)
 * [Nucleic Acid➞titer](Nucleic_Acid_titer.md)  <sub>0..1</sub>
     * Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
     * Range: [String](types/String.md)
 * [Nucleic Acid➞sequenceChecked](Nucleic_Acid_sequenceChecked.md)  <sub>1..1</sub>
     * Description: Tell whether or not the sequence of the product was controlled (compulsory for cloned products)
     * Range: [Boolean](types/Boolean.md)

### Inherited from Product:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Nucleic Acid |
| **Close Mappings:** | | wd:Q123619 |