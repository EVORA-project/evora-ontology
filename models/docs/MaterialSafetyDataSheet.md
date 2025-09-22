

# Class: Material safety data sheet (MaterialSafetyDataSheet) 


_A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product_





URI: [EVORAO:MaterialSafetyDataSheet](https://w3id.org/evorao/MaterialSafetyDataSheet)






```mermaid
 classDiagram
    class MaterialSafetyDataSheet
    click MaterialSafetyDataSheet href "../MaterialSafetyDataSheet"
      Resource <|-- MaterialSafetyDataSheet
        click Resource href "../Resource"
      
      MaterialSafetyDataSheet : accidentalReleaseMeasures
        
      MaterialSafetyDataSheet : dateIssued
        
      MaterialSafetyDataSheet : dateModified
        
      MaterialSafetyDataSheet : disposalConsiderations
        
      MaterialSafetyDataSheet : ecologicalInformation
        
      MaterialSafetyDataSheet : exposureControlsPersonalProtection
        
      MaterialSafetyDataSheet : fireFightingMeasures
        
      MaterialSafetyDataSheet : firstAidMeasures
        
      MaterialSafetyDataSheet : furtherInformation
        
      MaterialSafetyDataSheet : handlingAndStorage
        
      MaterialSafetyDataSheet : hazardsIdentification
        
      MaterialSafetyDataSheet : keyword
        
      MaterialSafetyDataSheet : materialSafetyContact
        
          
    
    
    MaterialSafetyDataSheet --> "1 _recommended_" ContactPoint : materialSafetyContact
    click ContactPoint href "../ContactPoint"

        
      MaterialSafetyDataSheet : physicalChemicalProperties
        
      MaterialSafetyDataSheet : regulatoryInformation
        
      MaterialSafetyDataSheet : stabilityAndReactivity
        
      MaterialSafetyDataSheet : toxicologicalInformation
        
      MaterialSafetyDataSheet : transportInformation
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **MaterialSafetyDataSheet**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [materialSafetyContact](materialSafetyContact.md) | 1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | The designated contact point responsible for providing information related to... | direct |
| [physicalChemicalProperties](physicalChemicalProperties.md) | 0..1 _recommended_ <br/> [String](String.md) | Key characteristics of the product, such as physical state, appearance, solub... | direct |
| [hazardsIdentification](hazardsIdentification.md) | 0..1 _recommended_ <br/> [String](String.md) | Outlines the potential risks and dangers associated with handling the product... | direct |
| [firstAidMeasures](firstAidMeasures.md) | 0..1 _recommended_ <br/> [String](String.md) | Instructions on immediate actions to take in case of exposure to the product,... | direct |
| [fireFightingMeasures](fireFightingMeasures.md) | 0..1 _recommended_ <br/> [String](String.md) | Guidance on how to safely extinguish a fire involving the product, including ... | direct |
| [accidentalReleaseMeasures](accidentalReleaseMeasures.md) | 0..1 _recommended_ <br/> [String](String.md) | Guidelines for safely managing spills or leaks of the product, including cont... | direct |
| [handlingAndStorage](handlingAndStorage.md) | 0..1 _recommended_ <br/> [String](String.md) | Instructions on the safe handling practices and storage conditions for the pr... | direct |
| [exposureControlsPersonalProtection](exposureControlsPersonalProtection.md) | 0..1 _recommended_ <br/> [String](String.md) | Specifies measures to limit exposure to the product, including recommended en... | direct |
| [stabilityAndReactivity](stabilityAndReactivity.md) | 0..1 _recommended_ <br/> [String](String.md) | Describes the product’s stability under normal conditions and its potential t... | direct |
| [toxicologicalInformation](toxicologicalInformation.md) | 0..1 _recommended_ <br/> [String](String.md) | Details on the potential health effects of the product, including routes of e... | direct |
| [ecologicalInformation](ecologicalInformation.md) | 0..1 _recommended_ <br/> [String](String.md) | Details the potential environmental impact of the product, including its effe... | direct |
| [disposalConsiderations](disposalConsiderations.md) | 0..1 _recommended_ <br/> [String](String.md) | Guidance on the safe and environmentally responsible disposal of the product,... | direct |
| [transportInformation](transportInformation.md) | 0..1 _recommended_ <br/> [String](String.md) | Details the regulations and guidelines for safely transporting the product, i... | direct |
| [regulatoryInformation](regulatoryInformation.md) | 0..1 _recommended_ <br/> [String](String.md) | Lists applicable laws, regulations, and standards governing the product, incl... | direct |
| [furtherInformation](furtherInformation.md) | 0..1 _recommended_ <br/> [String](String.md) | Provides any additional details or clarifications not covered in other sectio... | direct |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:MaterialSafetyDataSheet |
| native | EVORAO:MaterialSafetyDataSheet |
| close | wd:Q222067, wd:Q222067 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialSafetyDataSheet
description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized
  document that contains crucial occupational safety and health information related
  to the product
title: Material safety data sheet
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q222067
- wd:Q222067
is_a: Resource
slots:
- materialSafetyContact
- physicalChemicalProperties
- hazardsIdentification
- firstAidMeasures
- fireFightingMeasures
- accidentalReleaseMeasures
- handlingAndStorage
- exposureControlsPersonalProtection
- stabilityAndReactivity
- toxicologicalInformation
- ecologicalInformation
- disposalConsiderations
- transportInformation
- regulatoryInformation
- furtherInformation
slot_usage:
  materialSafetyContact:
    name: materialSafetyContact
    description: The designated contact point responsible for providing information
      related to the safety, handling, and regulatory compliance of the biological
      product.
    title: material safety contact
    broad_mappings:
    - schema:contactPoint
    is_a: contactPoint
    domain_of:
    - MaterialSafetyDataSheet
    range: ContactPoint
    required: true
    multivalued: false
  physicalChemicalProperties:
    name: physicalChemicalProperties
    description: Key characteristics of the product, such as physical state, appearance,
      solubility, pH, chemical composition, and molecular weight, essential for safe
      handling and storage
    title: physical and chemical properties and information on ingredients
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  hazardsIdentification:
    name: hazardsIdentification
    description: Outlines the potential risks and dangers associated with handling
      the product, including its physical, chemical, and health hazards. This section
      provides information on toxicity, flammability, reactivity, and other relevant
      risks for safe use.
    title: hazards identification
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  firstAidMeasures:
    name: firstAidMeasures
    description: Instructions on immediate actions to take in case of exposure to
      the product, including inhalation, ingestion, skin, or eye contact. This section
      outlines steps to minimize harm before medical help is available.
    title: first aid measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  fireFightingMeasures:
    name: fireFightingMeasures
    description: Guidance on how to safely extinguish a fire involving the product,
      including suitable extinguishing agents, special protective equipment for firefighters,
      and any specific hazards from combustion.
    title: fire fighting measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  accidentalReleaseMeasures:
    name: accidentalReleaseMeasures
    description: Guidelines for safely managing spills or leaks of the product, including
      containment, cleanup procedures, and precautions to prevent harm to people,
      property, and the environment.
    title: accidental release measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  handlingAndStorage:
    name: handlingAndStorage
    description: Instructions on the safe handling practices and storage conditions
      for the product, including precautions to prevent accidents, degradation, or
      contamination, as well as recommended temperature, humidity, and container requirements.
    title: handling and storage
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  exposureControlsPersonalProtection:
    name: exposureControlsPersonalProtection
    description: Specifies measures to limit exposure to the product, including recommended
      engineering controls (e.g., ventilation) and personal protective equipment (PPE)
      such as gloves, masks, goggles, and clothing to ensure safe handling.
    title: exposure controls/personal protection
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  stabilityAndReactivity:
    name: stabilityAndReactivity
    description: Describes the product’s stability under normal conditions and its
      potential to react with other substances. This section includes information
      on hazardous reactions, conditions to avoid, and incompatible materials that
      could cause degradation or dangerous reactions.
    title: stability and reactivity
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  toxicologicalInformation:
    name: toxicologicalInformation
    description: Details on the potential health effects of the product, including
      routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic
      toxicity and symptoms of exposure
    title: toxicological information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  ecologicalInformation:
    name: ecologicalInformation
    description: Details the potential environmental impact of the product, including
      its effects on ecosystems, persistence, degradability, bioaccumulation potential,
      and toxicity to aquatic and terrestrial organisms.
    title: ecological information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  disposalConsiderations:
    name: disposalConsiderations
    description: Guidance on the safe and environmentally responsible disposal of
      the product, including recommended disposal methods, regulatory requirements,
      and precautions to avoid harm to people and the environment during disposal.
    title: disposal considerations
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  transportInformation:
    name: transportInformation
    description: Details the regulations and guidelines for safely transporting the
      product, including classifications for road, air, sea, or rail transport, UN
      numbers, packaging requirements, and any special precautions to ensure safe
      transit.
    title: transport information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  regulatoryInformation:
    name: regulatoryInformation
    description: Lists applicable laws, regulations, and standards governing the product,
      including local, national, or international requirements for its handling, use,
      transportation, and disposal, ensuring compliance with legal obligations.
    title: regulatory information
    related_mappings:
    - rdfs:seeAlso
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  furtherInformation:
    name: furtherInformation
    description: Provides any additional details or clarifications not covered in
      other sections of the MSDS, such as references, supporting documents, or specific
      instructions for safe handling and use of the product.
    title: further information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: MaterialSafetyDataSheet
description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized
  document that contains crucial occupational safety and health information related
  to the product
title: Material safety data sheet
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q222067
- wd:Q222067
is_a: Resource
slot_usage:
  materialSafetyContact:
    name: materialSafetyContact
    description: The designated contact point responsible for providing information
      related to the safety, handling, and regulatory compliance of the biological
      product.
    title: material safety contact
    broad_mappings:
    - schema:contactPoint
    is_a: contactPoint
    domain_of:
    - MaterialSafetyDataSheet
    range: ContactPoint
    required: true
    multivalued: false
  physicalChemicalProperties:
    name: physicalChemicalProperties
    description: Key characteristics of the product, such as physical state, appearance,
      solubility, pH, chemical composition, and molecular weight, essential for safe
      handling and storage
    title: physical and chemical properties and information on ingredients
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  hazardsIdentification:
    name: hazardsIdentification
    description: Outlines the potential risks and dangers associated with handling
      the product, including its physical, chemical, and health hazards. This section
      provides information on toxicity, flammability, reactivity, and other relevant
      risks for safe use.
    title: hazards identification
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  firstAidMeasures:
    name: firstAidMeasures
    description: Instructions on immediate actions to take in case of exposure to
      the product, including inhalation, ingestion, skin, or eye contact. This section
      outlines steps to minimize harm before medical help is available.
    title: first aid measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  fireFightingMeasures:
    name: fireFightingMeasures
    description: Guidance on how to safely extinguish a fire involving the product,
      including suitable extinguishing agents, special protective equipment for firefighters,
      and any specific hazards from combustion.
    title: fire fighting measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  accidentalReleaseMeasures:
    name: accidentalReleaseMeasures
    description: Guidelines for safely managing spills or leaks of the product, including
      containment, cleanup procedures, and precautions to prevent harm to people,
      property, and the environment.
    title: accidental release measures
    related_mappings:
    - schema:Recommendation
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  handlingAndStorage:
    name: handlingAndStorage
    description: Instructions on the safe handling practices and storage conditions
      for the product, including precautions to prevent accidents, degradation, or
      contamination, as well as recommended temperature, humidity, and container requirements.
    title: handling and storage
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  exposureControlsPersonalProtection:
    name: exposureControlsPersonalProtection
    description: Specifies measures to limit exposure to the product, including recommended
      engineering controls (e.g., ventilation) and personal protective equipment (PPE)
      such as gloves, masks, goggles, and clothing to ensure safe handling.
    title: exposure controls/personal protection
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  stabilityAndReactivity:
    name: stabilityAndReactivity
    description: Describes the product’s stability under normal conditions and its
      potential to react with other substances. This section includes information
      on hazardous reactions, conditions to avoid, and incompatible materials that
      could cause degradation or dangerous reactions.
    title: stability and reactivity
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  toxicologicalInformation:
    name: toxicologicalInformation
    description: Details on the potential health effects of the product, including
      routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic
      toxicity and symptoms of exposure
    title: toxicological information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  ecologicalInformation:
    name: ecologicalInformation
    description: Details the potential environmental impact of the product, including
      its effects on ecosystems, persistence, degradability, bioaccumulation potential,
      and toxicity to aquatic and terrestrial organisms.
    title: ecological information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  disposalConsiderations:
    name: disposalConsiderations
    description: Guidance on the safe and environmentally responsible disposal of
      the product, including recommended disposal methods, regulatory requirements,
      and precautions to avoid harm to people and the environment during disposal.
    title: disposal considerations
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  transportInformation:
    name: transportInformation
    description: Details the regulations and guidelines for safely transporting the
      product, including classifications for road, air, sea, or rail transport, UN
      numbers, packaging requirements, and any special precautions to ensure safe
      transit.
    title: transport information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  regulatoryInformation:
    name: regulatoryInformation
    description: Lists applicable laws, regulations, and standards governing the product,
      including local, national, or international requirements for its handling, use,
      transportation, and disposal, ensuring compliance with legal obligations.
    title: regulatory information
    related_mappings:
    - rdfs:seeAlso
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  furtherInformation:
    name: furtherInformation
    description: Provides any additional details or clarifications not covered in
      other sections of the MSDS, such as references, supporting documents, or specific
      instructions for safe handling and use of the product.
    title: further information
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
  materialSafetyContact:
    name: materialSafetyContact
    description: The designated contact point responsible for providing information
      related to the safety, handling, and regulatory compliance of the biological
      product.
    title: material safety contact
    from_schema: https://w3id.org/evorao/
    broad_mappings:
    - schema:contactPoint
    rank: 1000
    is_a: contactPoint
    alias: materialSafetyContact
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: ContactPoint
    required: true
    recommended: true
    multivalued: false
  physicalChemicalProperties:
    name: physicalChemicalProperties
    description: Key characteristics of the product, such as physical state, appearance,
      solubility, pH, chemical composition, and molecular weight, essential for safe
      handling and storage
    title: physical and chemical properties and information on ingredients
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: physicalChemicalProperties
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  hazardsIdentification:
    name: hazardsIdentification
    description: Outlines the potential risks and dangers associated with handling
      the product, including its physical, chemical, and health hazards. This section
      provides information on toxicity, flammability, reactivity, and other relevant
      risks for safe use.
    title: hazards identification
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: hazardsIdentification
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  firstAidMeasures:
    name: firstAidMeasures
    description: Instructions on immediate actions to take in case of exposure to
      the product, including inhalation, ingestion, skin, or eye contact. This section
      outlines steps to minimize harm before medical help is available.
    title: first aid measures
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - schema:Recommendation
    rank: 1000
    alias: firstAidMeasures
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  fireFightingMeasures:
    name: fireFightingMeasures
    description: Guidance on how to safely extinguish a fire involving the product,
      including suitable extinguishing agents, special protective equipment for firefighters,
      and any specific hazards from combustion.
    title: fire fighting measures
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - schema:Recommendation
    rank: 1000
    alias: fireFightingMeasures
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  accidentalReleaseMeasures:
    name: accidentalReleaseMeasures
    description: Guidelines for safely managing spills or leaks of the product, including
      containment, cleanup procedures, and precautions to prevent harm to people,
      property, and the environment.
    title: accidental release measures
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - schema:Recommendation
    rank: 1000
    alias: accidentalReleaseMeasures
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  handlingAndStorage:
    name: handlingAndStorage
    description: Instructions on the safe handling practices and storage conditions
      for the product, including precautions to prevent accidents, degradation, or
      contamination, as well as recommended temperature, humidity, and container requirements.
    title: handling and storage
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: handlingAndStorage
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  exposureControlsPersonalProtection:
    name: exposureControlsPersonalProtection
    description: Specifies measures to limit exposure to the product, including recommended
      engineering controls (e.g., ventilation) and personal protective equipment (PPE)
      such as gloves, masks, goggles, and clothing to ensure safe handling.
    title: exposure controls/personal protection
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: exposureControlsPersonalProtection
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  stabilityAndReactivity:
    name: stabilityAndReactivity
    description: Describes the product’s stability under normal conditions and its
      potential to react with other substances. This section includes information
      on hazardous reactions, conditions to avoid, and incompatible materials that
      could cause degradation or dangerous reactions.
    title: stability and reactivity
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: stabilityAndReactivity
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  toxicologicalInformation:
    name: toxicologicalInformation
    description: Details on the potential health effects of the product, including
      routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic
      toxicity and symptoms of exposure
    title: toxicological information
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: toxicologicalInformation
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  ecologicalInformation:
    name: ecologicalInformation
    description: Details the potential environmental impact of the product, including
      its effects on ecosystems, persistence, degradability, bioaccumulation potential,
      and toxicity to aquatic and terrestrial organisms.
    title: ecological information
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: ecologicalInformation
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  disposalConsiderations:
    name: disposalConsiderations
    description: Guidance on the safe and environmentally responsible disposal of
      the product, including recommended disposal methods, regulatory requirements,
      and precautions to avoid harm to people and the environment during disposal.
    title: disposal considerations
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: disposalConsiderations
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  transportInformation:
    name: transportInformation
    description: Details the regulations and guidelines for safely transporting the
      product, including classifications for road, air, sea, or rail transport, UN
      numbers, packaging requirements, and any special precautions to ensure safe
      transit.
    title: transport information
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: transportInformation
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  regulatoryInformation:
    name: regulatoryInformation
    description: Lists applicable laws, regulations, and standards governing the product,
      including local, national, or international requirements for its handling, use,
      transportation, and disposal, ensuring compliance with legal obligations.
    title: regulatory information
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - rdfs:seeAlso
    rank: 1000
    alias: regulatoryInformation
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  furtherInformation:
    name: furtherInformation
    description: Provides any additional details or clarifications not covered in
      other sections of the MSDS, such as references, supporting documents, or specific
      instructions for safe handling and use of the product.
    title: further information
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: furtherInformation
    owner: MaterialSafetyDataSheet
    domain_of:
    - MaterialSafetyDataSheet
    range: string
    required: false
    recommended: true
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: MaterialSafetyDataSheet
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  dateIssued:
    name: dateIssued
    description: Date of formal issuance (e.g., publication) of the resource
    title: date issued
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000051
    close_mappings:
    - schema:datePublished
    - schema:dateCreated
    rank: 1000
    slot_uri: dct:issued
    alias: dateIssued
    owner: MaterialSafetyDataSheet
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  dateModified:
    name: dateModified
    description: Most recent date on which the resource was changed, updated or modified
    title: date modified
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000036
    close_mappings:
    - schema:dateModified
    rank: 1000
    slot_uri: dct:modified
    alias: dateModified
    owner: MaterialSafetyDataSheet
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false

```
</details>