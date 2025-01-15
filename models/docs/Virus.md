
# Class: Virus

The virus as a biological material

URI: [EVORA:Virus](https://evora-project.eu/Virus)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirusName],[VirusName]<coInfectingViruses%200..*-++[Virus&#124;contaminationWithCoInfectingViruses:boolean;mycoplasmicContent:boolean;cultivability(i):string;clinicalInformation(i):string%20%3F;identificationTechnique(i):string%20%3F;infectivity(i):string;infectivityTest(i):string%20%3F;isolationTechnique(i):string%20%3F;isolationConditions(i):string%20%3F;letterOfAuthority(i):string;passage(i):string%20%3F;sequencing(i):string;titer(i):string;shippingConditions(i):string;storageConditions(i):string;thirdPartyDistributionConsent(i):boolean%20%3F;usageRestrictions(i):string%20%3F;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[Pathogen]^-[Virus],[TransmissionMethod],[Sequence],[RiskGroup],[Provider],[PropagationHost],[ProductionCellLine],[ProductCategory],[PathogenIdentification],[Pathogen],[Originator],[MSDS],[Keyword],[IsolationHost],[Image],[IATAClassification],[GeographicalOrigin],[ExternalRelatedReference],[Document],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirusName],[VirusName]<coInfectingViruses%200..*-++[Virus&#124;contaminationWithCoInfectingViruses:boolean;mycoplasmicContent:boolean;cultivability(i):string;clinicalInformation(i):string%20%3F;identificationTechnique(i):string%20%3F;infectivity(i):string;infectivityTest(i):string%20%3F;isolationTechnique(i):string%20%3F;isolationConditions(i):string%20%3F;letterOfAuthority(i):string;passage(i):string%20%3F;sequencing(i):string;titer(i):string;shippingConditions(i):string;storageConditions(i):string;thirdPartyDistributionConsent(i):boolean%20%3F;usageRestrictions(i):string%20%3F;accessPointURL(i):uri;refSKU(i):string;unitDefinition(i):string%20%3F;unitCost(i):string;qualityGrading(i):string%20%3F;biosafetyRestrictions(i):string%20%3F;canItBeUsedToProduceGMO(i):boolean%20%3F;availability(i):string;technicalRecommendation(i):string%20%3F;internalReference(i):string%20%3F;note(i):string%20%3F;name(i):string;description(i):string%20%3F],[Pathogen]^-[Virus],[TransmissionMethod],[Sequence],[RiskGroup],[Provider],[PropagationHost],[ProductionCellLine],[ProductCategory],[PathogenIdentification],[Pathogen],[Originator],[MSDS],[Keyword],[IsolationHost],[Image],[IATAClassification],[GeographicalOrigin],[ExternalRelatedReference],[Document],[DOI],[ContactPoint],[Collection],[Certification],[BiologicalMaterialOrigin])

## Parents

 *  is_a: [Pathogen](Pathogen.md) - Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus

## Referenced by Class


## Attributes


### Own

 * [Virus➞coInfectingViruses](Virus_coInfectingViruses.md)  <sub>0..\*</sub>
     * Description: Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.
     * Range: [VirusName](VirusName.md)
 * [Virus➞contaminationWithCoInfectingViruses](Virus_contaminationWithCoInfectingViruses.md)  <sub>1..1</sub>
     * Description: A boolean value indicating whether there is contamination with co-infecting viruses
     * Range: [Boolean](types/Boolean.md)
 * [Virus➞mycoplasmicContent](Virus_mycoplasmicContent.md)  <sub>1..1</sub>
     * Description: Indicates the presence of mycoplasma contamination within the sample
     * Range: [Boolean](types/Boolean.md)

### Inherited from Pathogen:

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
 * [Product➞thirdPartyDistributionConsent](Product_thirdPartyDistributionConsent.md)  <sub>0..1</sub>
     * Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
     * Range: [Boolean](types/Boolean.md)
 * [Product➞usageRestrictions](Product_usageRestrictions.md)  <sub>0..1</sub>
     * Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
     * Range: [String](types/String.md)
 * [Pathogen➞biologicalMaterialOrigin](Pathogen_biologicalMaterialOrigin.md)  <sub>1..1</sub>
     * Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
     * Range: [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)
 * [Pathogen➞suspectedEpidemiologicalOrigin](Pathogen_suspectedEpidemiologicalOrigin.md)  <sub>0..\*</sub>
     * Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
     * Range: [GeographicalOrigin](GeographicalOrigin.md)
 * [Pathogen➞isolationHost](Pathogen_isolationHost.md)  <sub>0..\*</sub>
     * Description: The host organism from which the pathogen was originally isolated
     * Range: [IsolationHost](IsolationHost.md)
 * [Pathogen➞productionCellLine](Pathogen_productionCellLine.md)  <sub>0..\*</sub>
     * Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
     * Range: [ProductionCellLine](ProductionCellLine.md)
 * [Pathogen➞propagationHost](Pathogen_propagationHost.md)  <sub>0..\*</sub>
     * Description: The host organism that propagates the pathogen
     * Range: [PropagationHost](PropagationHost.md)
 * [Pathogen➞transmissionMethod](Pathogen_transmissionMethod.md)  <sub>0..\*</sub>
     * Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
     * Range: [TransmissionMethod](TransmissionMethod.md)
 * [Pathogen➞sequence](Pathogen_sequence.md)  <sub>1..\*</sub>
     * Description: The related sequence information from a sequence provider or in fasta format
     * Range: [Sequence](Sequence.md)
 * [Pathogen➞cultivability](Pathogen_cultivability.md)  <sub>1..1</sub>
     * Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
     * Range: [String](types/String.md)
 * [Pathogen➞clinicalInformation](Pathogen_clinicalInformation.md)  <sub>0..1</sub>
     * Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
     * Range: [String](types/String.md)
 * [Pathogen➞identificationTechnique](Pathogen_identificationTechnique.md)  <sub>0..1</sub>
     * Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
     * Range: [String](types/String.md)
 * [Pathogen➞infectivity](Pathogen_infectivity.md)  <sub>1..1</sub>
     * Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
     * Range: [String](types/String.md)
 * [Pathogen➞infectivityTest](Pathogen_infectivityTest.md)  <sub>0..1</sub>
     * Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
     * Range: [String](types/String.md)
 * [Pathogen➞isolationTechnique](Pathogen_isolationTechnique.md)  <sub>0..1</sub>
     * Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
     * Range: [String](types/String.md)
 * [Pathogen➞isolationConditions](Pathogen_isolationConditions.md)  <sub>0..1</sub>
     * Description: The environmental and procedural conditions under which the pathogen was isolated
     * Range: [String](types/String.md)
 * [Pathogen➞letterOfAuthority](Pathogen_letterOfAuthority.md)  <sub>1..1</sub>
     * Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
     * Range: [String](types/String.md)
 * [Pathogen➞passage](Pathogen_passage.md)  <sub>0..1</sub>
     * Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
     * Range: [String](types/String.md)
 * [Pathogen➞sequencing](Pathogen_sequencing.md)  <sub>1..1</sub>
     * Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
     * Range: [String](types/String.md)
 * [Pathogen➞titer](Pathogen_titer.md)  <sub>1..1</sub>
     * Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Virus |
| **Close Mappings:** | | wd:Q808 |