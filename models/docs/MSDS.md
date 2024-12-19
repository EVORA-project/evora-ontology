
# Class: MSDS

A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product

URI: [EVORA:MSDS](https://evora-project.eu/MSDS)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Product],[ContactPoint]<msdsContact%201..1-++[MSDS&#124;physicalChemicalProperties:string%20%3F;hazardsIdentification:string%20%3F;firstAidMeasures:string%20%3F;fireFightingMeasures:string%20%3F;accidentalReleaseMeasures:string%20%3F;handlingAndStorage:string%20%3F;exposureControlsPersonalProtection:string%20%3F;stabilityAndReactivity:string%20%3F;toxicologicalInformation:string%20%3F;ecologicalInformation:string%20%3F;disposalConsiderations:string%20%3F;transportInformation:string%20%3F;regulatoryInformation:string%20%3F;furtherInformation:string%20%3F],[Product]++-%20materialSafetyDataSheet%200..1>[MSDS],[Dataset]^-[MSDS],[Dataset],[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[Product],[ContactPoint]<msdsContact%201..1-++[MSDS&#124;physicalChemicalProperties:string%20%3F;hazardsIdentification:string%20%3F;firstAidMeasures:string%20%3F;fireFightingMeasures:string%20%3F;accidentalReleaseMeasures:string%20%3F;handlingAndStorage:string%20%3F;exposureControlsPersonalProtection:string%20%3F;stabilityAndReactivity:string%20%3F;toxicologicalInformation:string%20%3F;ecologicalInformation:string%20%3F;disposalConsiderations:string%20%3F;transportInformation:string%20%3F;regulatoryInformation:string%20%3F;furtherInformation:string%20%3F],[Product]++-%20materialSafetyDataSheet%200..1>[MSDS],[Dataset]^-[MSDS],[Dataset],[ContactPoint])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[Product](Product.md)** *[Product➞materialSafetyDataSheet](Product_materialSafetyDataSheet.md)*  <sub>0..1</sub>  **[MSDS](MSDS.md)**

## Attributes


### Own

 * [MSDS➞msdsContact](MSDS_msdsContact.md)  <sub>1..1</sub>
     * Description: The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.
     * Range: [ContactPoint](ContactPoint.md)
 * [MSDS➞physicalChemicalProperties](MSDS_physicalChemicalProperties.md)  <sub>0..1</sub>
     * Description: Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage
     * Range: [String](types/String.md)
 * [MSDS➞hazardsIdentification](MSDS_hazardsIdentification.md)  <sub>0..1</sub>
     * Description: Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.
     * Range: [String](types/String.md)
 * [MSDS➞firstAidMeasures](MSDS_firstAidMeasures.md)  <sub>0..1</sub>
     * Description: Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.
     * Range: [String](types/String.md)
 * [MSDS➞fireFightingMeasures](MSDS_fireFightingMeasures.md)  <sub>0..1</sub>
     * Description: Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.
     * Range: [String](types/String.md)
 * [MSDS➞accidentalReleaseMeasures](MSDS_accidentalReleaseMeasures.md)  <sub>0..1</sub>
     * Description: Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.
     * Range: [String](types/String.md)
 * [MSDS➞handlingAndStorage](MSDS_handlingAndStorage.md)  <sub>0..1</sub>
     * Description: Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.
     * Range: [String](types/String.md)
 * [MSDS➞exposureControlsPersonalProtection](MSDS_exposureControlsPersonalProtection.md)  <sub>0..1</sub>
     * Description: Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.
     * Range: [String](types/String.md)
 * [MSDS➞stabilityAndReactivity](MSDS_stabilityAndReactivity.md)  <sub>0..1</sub>
     * Description: Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.
     * Range: [String](types/String.md)
 * [MSDS➞toxicologicalInformation](MSDS_toxicologicalInformation.md)  <sub>0..1</sub>
     * Description: Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure
     * Range: [String](types/String.md)
 * [MSDS➞ecologicalInformation](MSDS_ecologicalInformation.md)  <sub>0..1</sub>
     * Description: Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.
     * Range: [String](types/String.md)
 * [MSDS➞disposalConsiderations](MSDS_disposalConsiderations.md)  <sub>0..1</sub>
     * Description: Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.
     * Range: [String](types/String.md)
 * [MSDS➞transportInformation](MSDS_transportInformation.md)  <sub>0..1</sub>
     * Description: Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.
     * Range: [String](types/String.md)
 * [MSDS➞regulatoryInformation](MSDS_regulatoryInformation.md)  <sub>0..1</sub>
     * Description: Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.
     * Range: [String](types/String.md)
 * [MSDS➞furtherInformation](MSDS_furtherInformation.md)  <sub>0..1</sub>
     * Description: Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | MSDS |
| **Close Mappings:** | | wd:Q222067 |