
# Class: Protein

A protein as a derived product from a pathogen

URI: [EVORA:Protein](https://evora-project.eu/Protein)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialFeature],[Sequence],[RiskGroup],[Provider],[ProteinTag],[ProteinTag]<proteinTAG%200..*-++[Protein&#124;domain:string%20*;expressedAs:string%20*;inclusionBodiesType:string%20*;expressionSystem:string%20*;functionalCharacterization:string%20*;functionalTechnicalDescription:string%20*;proteinPurification:string%20*;theTAGStatusOfTheSolubilizedProtein:string%20*;typeOfFunctionalCharacterization:string%20*;shippingConditions(i):string;storageConditions(i):string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[SpecialFeature]<specialFeature%200..*-++[Protein],[PDBReference]<relatedPDB%200..*-++[Protein],[Sequence]<sequence%201..*-++[Protein],[BiologicalMaterialOrigin]<biologicalMaterialOrigin%201..1-++[Protein],[Product]^-[Protein],[ProductCategory],[Product],[PathogenIdentification],[PDBReference],[Originator],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[Document],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialFeature],[Sequence],[RiskGroup],[Provider],[ProteinTag],[ProteinTag]<proteinTAG%200..*-++[Protein&#124;domain:string%20*;expressedAs:string%20*;inclusionBodiesType:string%20*;expressionSystem:string%20*;functionalCharacterization:string%20*;functionalTechnicalDescription:string%20*;proteinPurification:string%20*;theTAGStatusOfTheSolubilizedProtein:string%20*;typeOfFunctionalCharacterization:string%20*;shippingConditions(i):string;storageConditions(i):string;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[SpecialFeature]<specialFeature%200..*-++[Protein],[PDBReference]<relatedPDB%200..*-++[Protein],[Sequence]<sequence%201..*-++[Protein],[BiologicalMaterialOrigin]<biologicalMaterialOrigin%201..1-++[Protein],[Product]^-[Protein],[ProductCategory],[Product],[PathogenIdentification],[PDBReference],[Originator],[MSDS],[Keyword],[Image],[IATAClassification],[ExternalRelatedReference],[Document],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])

## Parents

 *  is_a: [Product](Product.md) - A product

## Referenced by Class


## Attributes


### Own

 * [Protein➞biologicalMaterialOrigin](Protein_biologicalMaterialOrigin.md)  <sub>1..1</sub>
     * Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
     * Range: [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)
 * [Protein➞sequence](Protein_sequence.md)  <sub>1..\*</sub>
     * Description: The related sequence information from a sequence provider or in fasta format
     * Range: [Sequence](Sequence.md)
 * [Protein➞relatedPDB](Protein_relatedPDB.md)  <sub>0..\*</sub>
     * Description: Identifier for 3D structural data as per the PDB (Protein Data Bank) database
     * Range: [PDBReference](PDBReference.md)
 * [Protein➞specialFeature](Protein_specialFeature.md)  <sub>0..\*</sub>
     * Description: Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
     * Range: [SpecialFeature](SpecialFeature.md)
 * [Protein➞proteinTAG](Protein_proteinTAG.md)  <sub>0..\*</sub>
     * Description: Peptide sequences genetically grafted onto a recombinant protein
     * Range: [ProteinTag](ProteinTag.md)
 * [Protein➞domain](Protein_domain.md)  <sub>0..\*</sub>
     * Description: A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function
     * Range: [String](types/String.md)
 * [Protein➞expressedAs](Protein_expressedAs.md)  <sub>0..\*</sub>
     * Description: Refers to the form in which the protein is produced and manifested in a biological system. Possible values include "Soluble" (proteins that are dissolved in the cellular or extracellular fluid) and "Inclusion bodies" (aggregated proteins that are insoluble and form within the cell)
     * Range: [String](types/String.md)
 * [Protein➞inclusionBodiesType](Protein_inclusionBodiesType.md)  <sub>0..\*</sub>
     * Description: Refers to the state of aggregated proteins within a cell. Possible values include "Denatured" (proteins are in an unfolded, inactive state) and "Refolded" (proteins have been processed to regain their functional, active conformation).
     * Range: [String](types/String.md)
 * [Protein➞expressionSystem](Protein_expressionSystem.md)  <sub>0..\*</sub>
     * Description: The host organism or cellular environment used to produce a protein from a specific gene. Possible values include "E. coli" (bacterial system), "Insect cells" (using baculovirus vectors), and "Mammalian cells" (mammalian cell lines).
     * Range: [String](types/String.md)
 * [Protein➞functionalCharacterization](Protein_functionalCharacterization.md)  <sub>0..\*</sub>
     * Description: The process of determining and describing the specific biological activities and roles of a protein. Possible values include "Functionally characterized" (the protein's functions have been identified and described) and "No functional characterization" (the protein's functions have not been identified or described).
     * Range: [String](types/String.md)
 * [Protein➞functionalTechnicalDescription](Protein_functionalTechnicalDescription.md)  <sub>0..\*</sub>
     * Description: Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.
     * Range: [String](types/String.md)
 * [Protein➞proteinPurification](Protein_proteinPurification.md)  <sub>0..\*</sub>
     * Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
     * Range: [String](types/String.md)
 * [Protein➞theTAGStatusOfTheSolubilizedProtein](Protein_theTAGStatusOfTheSolubilizedProtein.md)  <sub>0..\*</sub>
     * Description: Indicates the presence and condition of a tag on the protein after solubilization. Possible values include "Uncleaved Tag" (the tag is still attached to the protein), "Cleaved Tag" (the tag has been removed from the protein), and "No Tag" (the protein does not have a tag)
     * Range: [String](types/String.md)
 * [Protein➞typeOfFunctionalCharacterization](Protein_typeOfFunctionalCharacterization.md)  <sub>0..\*</sub>
     * Description: Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include "Enzymatic" (the protein has been characterized for its enzyme activity) and "Antigenic" (the protein has been characterized for its ability to elicit an immune response).
     * Range: [String](types/String.md)

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
| **Aliases:** | | Protein |
| **Close Mappings:** | | wd:Q8054 |