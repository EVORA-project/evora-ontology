

# Class: Nucleic Acid (Nucleic Acid)


_Nucleic acid related to a pathogen. It can be extracted or synthetic_





URI: [EVORAO:NucleicAcid](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#NucleicAcid)






```mermaid
 classDiagram
    class NucleicAcid
    click NucleicAcid href "../NucleicAcid"
      Product <|-- NucleicAcid
        click Product href "../Product"
      
      NucleicAcid : accessPointURL
        
      NucleicAcid : additionalCategory
        
          
    
    
    NucleicAcid --> "* _recommended_" ProductCategory : additionalCategory
    click ProductCategory href "../ProductCategory"

        
      NucleicAcid : availability
        
      NucleicAcid : biologicalMaterialOrigin
        
          
    
    
    NucleicAcid --> "1" BiologicalMaterialOrigin : biologicalMaterialOrigin
    click BiologicalMaterialOrigin href "../BiologicalMaterialOrigin"

        
      NucleicAcid : biosafetyRestrictions
        
      NucleicAcid : canItBeUsedToProduceGMO
        
      NucleicAcid : category
        
          
    
    
    NucleicAcid --> "1" ProductCategory : category
    click ProductCategory href "../ProductCategory"

        
      NucleicAcid : certification
        
          
    
    
    NucleicAcid --> "*" Certification : certification
    click Certification href "../Certification"

        
      NucleicAcid : clonedIntoPlasmid
        
          
    
    
    NucleicAcid --> "0..1 _recommended_" ExpressionVector : clonedIntoPlasmid
    click ExpressionVector href "../ExpressionVector"

        
      NucleicAcid : collection
        
          
    
    
    NucleicAcid --> "1..*" Collection : collection
    click Collection href "../Collection"

        
      NucleicAcid : complementaryDocument
        
          
    
    
    NucleicAcid --> "*" Document : complementaryDocument
    click Document href "../Document"

        
      NucleicAcid : contactPoint
        
          
    
    
    NucleicAcid --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      NucleicAcid : description
        
      NucleicAcid : externalRelatedReference
        
          
    
    
    NucleicAcid --> "*" ExternalRelatedReference : externalRelatedReference
    click ExternalRelatedReference href "../ExternalRelatedReference"

        
      NucleicAcid : hasGbFileOfTheConstruct
        
          
    
    
    NucleicAcid --> "*" Data : hasGbFileOfTheConstruct
    click Data href "../Data"

        
      NucleicAcid : hasIATAClassification
        
          
    
    
    NucleicAcid --> "1" IATAClassification : hasIATAClassification
    click IATAClassification href "../IATAClassification"

        
      NucleicAcid : hasTAG
        
          
    
    
    NucleicAcid --> "1" ProteinTag : hasTAG
    click ProteinTag href "../ProteinTag"

        
      NucleicAcid : identificationTechnique
        
      NucleicAcid : internalReference
        
      NucleicAcid : isItAClonedNucleicAcid
        
      NucleicAcid : keywords
        
          
    
    
    NucleicAcid --> "1..* _recommended_" Keyword : keywords
    click Keyword href "../Keyword"

        
      NucleicAcid : materialSafetyDataSheet
        
          
    
    
    NucleicAcid --> "0..1" MSDS : materialSafetyDataSheet
    click MSDS href "../MSDS"

        
      NucleicAcid : mutationObserved
        
      NucleicAcid : note
        
      NucleicAcid : observedMutations
        
      NucleicAcid : originator
        
          
    
    
    NucleicAcid --> "0..1" Originator : originator
    click Originator href "../Originator"

        
      NucleicAcid : pasmidSelection
        
          
    
    
    NucleicAcid --> "* _recommended_" PlasmidSelection : pasmidSelection
    click PlasmidSelection href "../PlasmidSelection"

        
      NucleicAcid : pathogenIdentification
        
          
    
    
    NucleicAcid --> "1..*" PathogenIdentification : pathogenIdentification
    click PathogenIdentification href "../PathogenIdentification"

        
      NucleicAcid : productPicture
        
          
    
    
    NucleicAcid --> "*" Image : productPicture
    click Image href "../Image"

        
      NucleicAcid : provider
        
          
    
    
    NucleicAcid --> "1" Provider : provider
    click Provider href "../Provider"

        
      NucleicAcid : qualityGrading
        
      NucleicAcid : refSKU
        
      NucleicAcid : regionEncompassedInThisProduct
        
      NucleicAcid : relatedDOI
        
          
    
    
    NucleicAcid --> "*" DOI : relatedDOI
    click DOI href "../DOI"

        
      NucleicAcid : riskGroup
        
          
    
    
    NucleicAcid --> "0..1 _recommended_" RiskGroup : riskGroup
    click RiskGroup href "../RiskGroup"

        
      NucleicAcid : sequence
        
          
    
    
    NucleicAcid --> "1..* _recommended_" Sequence : sequence
    click Sequence href "../Sequence"

        
      NucleicAcid : sequenceChecked
        
      NucleicAcid : sequencing
        
      NucleicAcid : shippingConditions
        
      NucleicAcid : storageConditions
        
      NucleicAcid : technicalRecommendation
        
      NucleicAcid : thirdPartyDistributionConsent
        
      NucleicAcid : titer
        
      NucleicAcid : title
        
      NucleicAcid : unitCost
        
      NucleicAcid : unitDefinition
        
      NucleicAcid : usageRestrictions
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Dataset](Dataset.md)
        * [ProductOrService](ProductOrService.md)
            * [Product](Product.md)
                * **NucleicAcid**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [biologicalMaterialOrigin](biologicalMaterialOrigin.md) | 1 <br/> [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, essential for access... | direct |
| [hasGbFileOfTheConstruct](hasGbFileOfTheConstruct.md) | * <br/> [Data](Data.md) | A GenBank formatted file that contains detailed sequence and annotation infor... | direct |
| [sequence](sequence.md) | 1..* _recommended_ <br/> [Sequence](Sequence.md) | The related sequence information from a sequence provider or in fasta format | direct |
| [isItAClonedNucleicAcid](isItAClonedNucleicAcid.md) | 1 <br/> [Boolean](Boolean.md) | Indicates that the nucleic acid sequence has been inserted into a plasmid vec... | direct |
| [clonedIntoPlasmid](clonedIntoPlasmid.md) | 0..1 _recommended_ <br/> [ExpressionVector](ExpressionVector.md) | The plasmid into which the nucleic acid has been cloned | direct |
| [pasmidSelection](pasmidSelection.md) | * _recommended_ <br/> [PlasmidSelection](PlasmidSelection.md) | Specific selectable markers in the plasmid, such as antibiotic resistance gen... | direct |
| [hasTAG](hasTAG.md) | 1 <br/> [ProteinTag](ProteinTag.md) | TAG sequence used for purposes such as purification, detection, or localizati... | direct |
| [regionEncompassedInThisProduct](regionEncompassedInThisProduct.md) | 1 <br/> [String](String.md) | The specific region encompassed in the product | direct |
| [mutationObserved](mutationObserved.md) | 1 <br/> [Boolean](Boolean.md) | Indicates if the current nucleic acid has No mutation compared to the referen... | direct |
| [observedMutations](observedMutations.md) | 0..1 <br/> [String](String.md) | The specific mutations that have been identified and documented in the nuclei... | direct |
| [identificationTechnique](identificationTechnique.md) | 0..1 <br/> [String](String.md) | A method or procedure used to detect, identify, and confirm the presence of a... | direct |
| [sequencing](sequencing.md) | 1 <br/> [String](String.md) | Refers to the level of sequencing performed on the nucleic acid | direct |
| [titer](titer.md) | 0..1 <br/> [String](String.md) | The titer value, its corresponding unit, and the method of quantification (e | direct |
| [sequenceChecked](sequenceChecked.md) | 1 <br/> [Boolean](Boolean.md) | Tell whether or not the sequence of the product was controlled (compulsory fo... | direct |
| [hasIATAClassification](hasIATAClassification.md) | 1 <br/> [IATAClassification](IATAClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... | [Product](Product.md) |
| [shippingConditions](shippingConditions.md) | 1 <br/> [String](String.md) | Specification of the terms and parameters for transporting | [Product](Product.md) |
| [materialSafetyDataSheet](materialSafetyDataSheet.md) | 0..1 <br/> [MSDS](MSDS.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... | [Product](Product.md) |
| [originator](originator.md) | 0..1 <br/> [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... | [Product](Product.md) |
| [storageConditions](storageConditions.md) | 1 <br/> [String](String.md) | Specifies the conditions under which the product has to be stored to maintain... | [Product](Product.md) |
| [thirdPartyDistributionConsent](thirdPartyDistributionConsent.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the biological material can be distributed without restrict... | [Product](Product.md) |
| [usageRestrictions](usageRestrictions.md) | 0..1 <br/> [String](String.md) | Specifies any limitations or conditions on the use of the biological material... | [Product](Product.md) |
| [accessPointURL](accessPointURL.md) | 1 <br/> [Uri](Uri.md) | The URL that permits to access to the product/service detailed description pa... | [ProductOrService](ProductOrService.md) |
| [refSKU](refSKU.md) | 1 <br/> [String](String.md) | The reference or the stock keeping unit of the service or item provided in th... | [ProductOrService](ProductOrService.md) |
| [unitDefinition](unitDefinition.md) | 0..1 _recommended_ <br/> [String](String.md) | A short description of what will be delivered by ordering one unit of this it... | [ProductOrService](ProductOrService.md) |
| [category](category.md) | 1 <br/> [ProductCategory](ProductCategory.md) | The main category of the service or product | [ProductOrService](ProductOrService.md) |
| [additionalCategory](additionalCategory.md) | * _recommended_ <br/> [ProductCategory](ProductCategory.md) | Any category apart from its main category in which this product or service ca... | [ProductOrService](ProductOrService.md) |
| [unitCost](unitCost.md) | 1 _recommended_ <br/> [String](String.md) | The cost per access for one unit as defined by the unit definition | [ProductOrService](ProductOrService.md) |
| [qualityGrading](qualityGrading.md) | 0..1 <br/> [String](String.md) | Information that permits to assess the quality level of what will be provided | [ProductOrService](ProductOrService.md) |
| [pathogenIdentification](pathogenIdentification.md) | 1..* <br/> [PathogenIdentification](PathogenIdentification.md) | The identification of the pathogen or group of pathogens (e | [ProductOrService](ProductOrService.md) |
| [relatedDOI](relatedDOI.md) | * <br/> [DOI](DOI.md) | Any Digital Object Identifier that can be related | [ProductOrService](ProductOrService.md) |
| [riskGroup](riskGroup.md) | 0..1 _recommended_ <br/> [RiskGroup](RiskGroup.md) | The highest risk group related to this resource | [ProductOrService](ProductOrService.md) |
| [biosafetyRestrictions](biosafetyRestrictions.md) | 0..1 <br/> [String](String.md) | Information about guidelines and regulations designed to prevent the exposure... | [ProductOrService](ProductOrService.md) |
| [canItBeUsedToProduceGMO](canItBeUsedToProduceGMO.md) | 1 _recommended_ <br/> [Boolean](Boolean.md) | Indicates if the current service or product can be used to produce GMO | [ProductOrService](ProductOrService.md) |
| [provider](provider.md) | 1 <br/> [Provider](Provider.md) | A provider of this product or service, as a specific organization | [ProductOrService](ProductOrService.md) |
| [collection](collection.md) | 1..* <br/> [Collection](Collection.md) | The collection(s) to which belongs this item | [ProductOrService](ProductOrService.md) |
| [keywords](keywords.md) | 1..* _recommended_ <br/> [Keyword](Keyword.md) | List of terms used to tag and categorize this Item | [ProductOrService](ProductOrService.md) |
| [availability](availability.md) | 1 <br/> [String](String.md) | The state or condition in which this item is accessible and ready for use or ... | [ProductOrService](ProductOrService.md) |
| [complementaryDocument](complementaryDocument.md) | * <br/> [Document](Document.md) | Any additional documents that provide supplementary information, instructions... | [ProductOrService](ProductOrService.md) |
| [technicalRecommendation](technicalRecommendation.md) | 0..1 <br/> [String](String.md) | Expert advice or guidelines provided to ensure the optimal use, performance, ... | [ProductOrService](ProductOrService.md) |
| [productPicture](productPicture.md) | * <br/> [Image](Image.md) | A picture that can represent the item | [ProductOrService](ProductOrService.md) |
| [externalRelatedReference](externalRelatedReference.md) | * <br/> [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve another related item from an external pr... | [ProductOrService](ProductOrService.md) |
| [certification](certification.md) | * <br/> [Certification](Certification.md) | Any certification related to the current product or service; e | [ProductOrService](ProductOrService.md) |
| [internalReference](internalReference.md) | 0..1 <br/> [String](String.md) | Any reference or indication to be used for local retrieval purpose | [ProductOrService](ProductOrService.md) |
| [note](note.md) | 0..1 <br/> [String](String.md) | An aditional information as a textual comment | [ProductOrService](ProductOrService.md) |
| [contactPoint](contactPoint.md) | 0..1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [ProductOrService](ProductOrService.md) |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Dataset](Dataset.md) |
| [description](description.md) | 1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Dataset](Dataset.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:NucleicAcid |
| native | EVORAO:NucleicAcid |
| close | wd:Q123619, wd:Q123619 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Nucleic Acid
description: Nucleic acid related to a pathogen. It can be extracted or synthetic
title: Nucleic Acid
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q123619
- wd:Q123619
is_a: Product
slots:
- biologicalMaterialOrigin
- hasGbFileOfTheConstruct
- sequence
- isItAClonedNucleicAcid
- clonedIntoPlasmid
- pasmidSelection
- hasTAG
- regionEncompassedInThisProduct
- mutationObserved
- observedMutations
- identificationTechnique
- sequencing
- titer
- sequenceChecked
slot_usage:
  biologicalMaterialOrigin:
    name: biologicalMaterialOrigin
    description: Information about the origin of the biological material, essential
      for access, utilization, and benefit-sharing of genetic resources in compliance
      with the Nagoya Protocol
    title: Biological Material origin
    domain_of:
    - Nucleic Acid
    - Protein
    - Pathogen
    range: BiologicalMaterialOrigin
    required: true
    multivalued: false
  hasGbFileOfTheConstruct:
    name: hasGbFileOfTheConstruct
    description: A GenBank formatted file that contains detailed sequence and annotation
      information of a nucleic acid construct
    title: has .gb file of the construct
    domain_of:
    - Nucleic Acid
    range: Data
    required: false
    multivalued: true
  sequence:
    name: sequence
    description: The related sequence information from a sequence provider or in fasta
      format
    title: sequence
    domain_of:
    - Nucleic Acid
    - RecombinantPartIdentification
    - Protein
    - Pathogen
    range: Sequence
    required: true
    multivalued: true
  isItAClonedNucleicAcid:
    name: isItAClonedNucleicAcid
    description: Indicates that the nucleic acid sequence has been inserted into a
      plasmid vector for propagation or expression in a host organism
    title: is it a Cloned Nucleic Acid?
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  clonedIntoPlasmid:
    name: clonedIntoPlasmid
    description: The plasmid into which the nucleic acid has been cloned
    title: cloned into plasmid
    domain_of:
    - Nucleic Acid
    range: ExpressionVector
    required: false
    recommended: true
    multivalued: false
  pasmidSelection:
    name: pasmidSelection
    description: Specific selectable markers in the plasmid, such as antibiotic resistance
      genes, used to identify and maintain cells that contain the plasmid
    title: plasmid selection
    domain_of:
    - Nucleic Acid
    range: PlasmidSelection
    required: false
    recommended: true
    multivalued: true
  hasTAG:
    name: hasTAG
    description: TAG sequence used for purposes such as purification, detection, or
      localization
    title: TAG
    domain_of:
    - Nucleic Acid
    range: ProteinTag
    required: true
    multivalued: false
  regionEncompassedInThisProduct:
    name: regionEncompassedInThisProduct
    description: The specific region encompassed in the product
    title: region encompassed in this Product
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
  mutationObserved:
    name: mutationObserved
    description: "Indicates if the current nucleic acid has No mutation compared to\
      \ the reference sequence if the value is set to false or if it\n contains mutations\
      \ (no frameshift, no unexpected STOP codon) if set to true"
    title: mutation observed
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  observedMutations:
    name: observedMutations
    description: The specific mutations that have been identified and documented in
      the nucleic acid sequence
    title: observed mutations
    domain_of:
    - Nucleic Acid
    range: string
    required: false
    multivalued: false
  identificationTechnique:
    name: identificationTechnique
    description: A method or procedure used to detect, identify, and confirm the presence
      of a specific nucleic acid sequence, pathogen, or associated constructs. This
      may involve various techniques such as PCR, sequencing, hybridization, or other
      molecular methods, utilizing specific tools and procedures for accurate detection
      and analysis
    title: identification technique
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequencing:
    name: sequencing
    description: Refers to the level of sequencing performed on the nucleic acid.
      Possible values include 'Not sequenced' (no sequencing has been performed),
      'Partly sequenced' (only a portion of the nucleic acid sequence has been determined),
      and 'Fully sequenced' (the entire nucleic acid sequence has been determined).
    title: sequencing
    comments:
    - Cloned products have to be sequenced
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
  titer:
    name: titer
    description: The titer value, its corresponding unit, and the method of quantification
      (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present
      in the sample. The titer corresponds to the highest dilution factor that still
      yields a positive reading
    title: titer
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequenceChecked:
    name: sequenceChecked
    description: Tell whether or not the sequence of the product was controlled (compulsory
      for cloned products)
    title: sequence checked
    comments:
    - Sequence check is mandatory for cloned products
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Nucleic Acid
description: Nucleic acid related to a pathogen. It can be extracted or synthetic
title: Nucleic Acid
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q123619
- wd:Q123619
is_a: Product
slot_usage:
  biologicalMaterialOrigin:
    name: biologicalMaterialOrigin
    description: Information about the origin of the biological material, essential
      for access, utilization, and benefit-sharing of genetic resources in compliance
      with the Nagoya Protocol
    title: Biological Material origin
    domain_of:
    - Nucleic Acid
    - Protein
    - Pathogen
    range: BiologicalMaterialOrigin
    required: true
    multivalued: false
  hasGbFileOfTheConstruct:
    name: hasGbFileOfTheConstruct
    description: A GenBank formatted file that contains detailed sequence and annotation
      information of a nucleic acid construct
    title: has .gb file of the construct
    domain_of:
    - Nucleic Acid
    range: Data
    required: false
    multivalued: true
  sequence:
    name: sequence
    description: The related sequence information from a sequence provider or in fasta
      format
    title: sequence
    domain_of:
    - Nucleic Acid
    - RecombinantPartIdentification
    - Protein
    - Pathogen
    range: Sequence
    required: true
    multivalued: true
  isItAClonedNucleicAcid:
    name: isItAClonedNucleicAcid
    description: Indicates that the nucleic acid sequence has been inserted into a
      plasmid vector for propagation or expression in a host organism
    title: is it a Cloned Nucleic Acid?
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  clonedIntoPlasmid:
    name: clonedIntoPlasmid
    description: The plasmid into which the nucleic acid has been cloned
    title: cloned into plasmid
    domain_of:
    - Nucleic Acid
    range: ExpressionVector
    required: false
    recommended: true
    multivalued: false
  pasmidSelection:
    name: pasmidSelection
    description: Specific selectable markers in the plasmid, such as antibiotic resistance
      genes, used to identify and maintain cells that contain the plasmid
    title: plasmid selection
    domain_of:
    - Nucleic Acid
    range: PlasmidSelection
    required: false
    recommended: true
    multivalued: true
  hasTAG:
    name: hasTAG
    description: TAG sequence used for purposes such as purification, detection, or
      localization
    title: TAG
    domain_of:
    - Nucleic Acid
    range: ProteinTag
    required: true
    multivalued: false
  regionEncompassedInThisProduct:
    name: regionEncompassedInThisProduct
    description: The specific region encompassed in the product
    title: region encompassed in this Product
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
  mutationObserved:
    name: mutationObserved
    description: "Indicates if the current nucleic acid has No mutation compared to\
      \ the reference sequence if the value is set to false or if it\n contains mutations\
      \ (no frameshift, no unexpected STOP codon) if set to true"
    title: mutation observed
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  observedMutations:
    name: observedMutations
    description: The specific mutations that have been identified and documented in
      the nucleic acid sequence
    title: observed mutations
    domain_of:
    - Nucleic Acid
    range: string
    required: false
    multivalued: false
  identificationTechnique:
    name: identificationTechnique
    description: A method or procedure used to detect, identify, and confirm the presence
      of a specific nucleic acid sequence, pathogen, or associated constructs. This
      may involve various techniques such as PCR, sequencing, hybridization, or other
      molecular methods, utilizing specific tools and procedures for accurate detection
      and analysis
    title: identification technique
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequencing:
    name: sequencing
    description: Refers to the level of sequencing performed on the nucleic acid.
      Possible values include 'Not sequenced' (no sequencing has been performed),
      'Partly sequenced' (only a portion of the nucleic acid sequence has been determined),
      and 'Fully sequenced' (the entire nucleic acid sequence has been determined).
    title: sequencing
    comments:
    - Cloned products have to be sequenced
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
  titer:
    name: titer
    description: The titer value, its corresponding unit, and the method of quantification
      (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present
      in the sample. The titer corresponds to the highest dilution factor that still
      yields a positive reading
    title: titer
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequenceChecked:
    name: sequenceChecked
    description: Tell whether or not the sequence of the product was controlled (compulsory
      for cloned products)
    title: sequence checked
    comments:
    - Sequence check is mandatory for cloned products
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
attributes:
  biologicalMaterialOrigin:
    name: biologicalMaterialOrigin
    description: Information about the origin of the biological material, essential
      for access, utilization, and benefit-sharing of genetic resources in compliance
      with the Nagoya Protocol
    title: Biological Material origin
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: biologicalMaterialOrigin
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    - Protein
    - Pathogen
    range: BiologicalMaterialOrigin
    required: true
    multivalued: false
  hasGbFileOfTheConstruct:
    name: hasGbFileOfTheConstruct
    description: A GenBank formatted file that contains detailed sequence and annotation
      information of a nucleic acid construct
    title: has .gb file of the construct
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: hasGbFileOfTheConstruct
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: Data
    required: false
    multivalued: true
  sequence:
    name: sequence
    description: The related sequence information from a sequence provider or in fasta
      format
    title: sequence
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: sequence
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    - RecombinantPartIdentification
    - Protein
    - Pathogen
    range: Sequence
    required: true
    recommended: true
    multivalued: true
  isItAClonedNucleicAcid:
    name: isItAClonedNucleicAcid
    description: Indicates that the nucleic acid sequence has been inserted into a
      plasmid vector for propagation or expression in a host organism
    title: is it a Cloned Nucleic Acid?
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: isItAClonedNucleicAcid
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  clonedIntoPlasmid:
    name: clonedIntoPlasmid
    description: The plasmid into which the nucleic acid has been cloned
    title: cloned into plasmid
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: clonedIntoPlasmid
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: ExpressionVector
    required: false
    recommended: true
    multivalued: false
  pasmidSelection:
    name: pasmidSelection
    description: Specific selectable markers in the plasmid, such as antibiotic resistance
      genes, used to identify and maintain cells that contain the plasmid
    title: plasmid selection
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: pasmidSelection
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: PlasmidSelection
    required: false
    recommended: true
    multivalued: true
  hasTAG:
    name: hasTAG
    description: TAG sequence used for purposes such as purification, detection, or
      localization
    title: TAG
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: hasTAG
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: ProteinTag
    required: true
    multivalued: false
  regionEncompassedInThisProduct:
    name: regionEncompassedInThisProduct
    description: The specific region encompassed in the product
    title: region encompassed in this Product
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: regionEncompassedInThisProduct
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
  mutationObserved:
    name: mutationObserved
    description: "Indicates if the current nucleic acid has No mutation compared to\
      \ the reference sequence if the value is set to false or if it\n contains mutations\
      \ (no frameshift, no unexpected STOP codon) if set to true"
    title: mutation observed
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: mutationObserved
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  observedMutations:
    name: observedMutations
    description: The specific mutations that have been identified and documented in
      the nucleic acid sequence
    title: observed mutations
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: observedMutations
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: string
    required: false
    multivalued: false
  identificationTechnique:
    name: identificationTechnique
    description: A method or procedure used to detect, identify, and confirm the presence
      of a specific nucleic acid sequence, pathogen, or associated constructs. This
      may involve various techniques such as PCR, sequencing, hybridization, or other
      molecular methods, utilizing specific tools and procedures for accurate detection
      and analysis
    title: identification technique
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: identificationTechnique
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequencing:
    name: sequencing
    description: Refers to the level of sequencing performed on the nucleic acid.
      Possible values include 'Not sequenced' (no sequencing has been performed),
      'Partly sequenced' (only a portion of the nucleic acid sequence has been determined),
      and 'Fully sequenced' (the entire nucleic acid sequence has been determined).
    title: sequencing
    comments:
    - Cloned products have to be sequenced
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: sequencing
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: string
    required: true
    multivalued: false
    equals_string_in:
    - Not sequenced
    - Partly sequenced
    - Fully sequenced
  titer:
    name: titer
    description: The titer value, its corresponding unit, and the method of quantification
      (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present
      in the sample. The titer corresponds to the highest dilution factor that still
      yields a positive reading
    title: titer
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wd:Q2166189
    rank: 1000
    alias: titer
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  sequenceChecked:
    name: sequenceChecked
    description: Tell whether or not the sequence of the product was controlled (compulsory
      for cloned products)
    title: sequence checked
    comments:
    - Sequence check is mandatory for cloned products
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: sequenceChecked
    owner: Nucleic Acid
    domain_of:
    - Nucleic Acid
    range: boolean
    required: true
    multivalued: false
  hasIATAClassification:
    name: hasIATAClassification
    description: The corresponding International Air Transport Association (IATA)'s
      category for this Product
    title: IATA classification
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: hasIATAClassification
    owner: Nucleic Acid
    domain_of:
    - Product
    range: IATAClassification
    required: true
    multivalued: false
  shippingConditions:
    name: shippingConditions
    description: 'Specification of the terms and parameters for transporting

      '
    title: shipping conditions
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: shippingConditions
    owner: Nucleic Acid
    domain_of:
    - Product
    range: string
    required: true
    multivalued: false
  materialSafetyDataSheet:
    name: materialSafetyDataSheet
    description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is
      a standardized document that contains crucial occupational safety and health
      information related to the product
    title: material safety data sheet
    comments:
    - The MSD  is a document that provides detailed information about the properties,
      hazards, handling, storage, and emergency procedures related to the use of a
      chemical or substance
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: materialSafetyDataSheet
    owner: Nucleic Acid
    domain_of:
    - Product
    range: MSDS
    required: false
    multivalued: false
  originator:
    name: originator
    description: The individual or organization responsible for the original discovery,
      isolation, or creation of an item, providing information about the source or
      origin of the sample
    title: originator
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: originator
    owner: Nucleic Acid
    domain_of:
    - Product
    range: Originator
    required: false
    multivalued: false
  storageConditions:
    name: storageConditions
    description: Specifies the conditions under which the product has to be stored
      to maintain stability and integrity, such as temperature, buffer, and other
      environmental factors.
    title: storage conditions
    comments:
    - e.g, could be a xsd:string in enumeration ('Freeze Dried', 'Liquid Nitrogen',
      'Viral Storage Medium -20C', 'Viral Storage Medium -80C', 'Living plant material
      (>= +4°C)', 'Gas Phase', 'Ethanol -20C', 'Ethanol -80C', 'Dried')
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: storageConditions
    owner: Nucleic Acid
    domain_of:
    - Product
    range: string
    required: true
    multivalued: false
  thirdPartyDistributionConsent:
    name: thirdPartyDistributionConsent
    description: Indicates whether the biological material can be distributed without
      restriction to third parties, as indicated by the ABS permit, in case an ABS
      permit is required
    title: third party distribution consent
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: thirdPartyDistributionConsent
    owner: Nucleic Acid
    domain_of:
    - Product
    range: boolean
    required: false
    multivalued: false
  usageRestrictions:
    name: usageRestrictions
    description: Specifies any limitations or conditions on the use of the biological
      material, including restrictions on research, commercial use, or distribution,
      considering any potential concerns about the related genetic material
    title: usage restrictions
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: usageRestrictions
    owner: Nucleic Acid
    domain_of:
    - Product
    range: string
    required: false
    multivalued: false
  accessPointURL:
    name: accessPointURL
    description: The URL that permits to access to the product/service detailed description
      page on the provider's website and/or allows to place an order about it or at
      least describe the process to place an order/enquiry
    title: access point URL
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:landingPage
    rank: 1000
    alias: accessPointURL
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: uri
    required: true
    multivalued: false
  refSKU:
    name: refSKU
    description: The reference or the stock keeping unit of the service or item provided
      in the provider's catalogue
    title: ref-SKU
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:identifier
    rank: 1000
    alias: refSKU
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  unitDefinition:
    name: unitDefinition
    description: A short description of what will be delivered by ordering one unit
      of this item
    title: unit definition
    comments:
    - 'The description of what will be delivered to the end-user (e.g.: packaging,
      quantity...)'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: unitDefinition
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    recommended: true
    multivalued: false
  category:
    name: category
    description: The main category of the service or product
    title: category
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:theme
    rank: 1000
    alias: category
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: ProductCategory
    required: true
    multivalued: false
  additionalCategory:
    name: additionalCategory
    description: Any category apart from its main category in which this product or
      service can fit
    title: additional category
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:theme
    rank: 1000
    alias: additionalCategory
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: ProductCategory
    required: false
    recommended: true
    multivalued: true
  unitCost:
    name: unitCost
    description: The cost per access for one unit as defined by the unit definition
    title: unit cost
    comments:
    - The cost per access may not be defined or be specific to a request, so it has
      to be a xsd:string instead of an xsd:float as initialy suggested to permit description
      of cost as conditional to what is requested
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    ifabsent: string(on request)
    alias: unitCost
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: true
    recommended: true
    multivalued: false
  qualityGrading:
    name: qualityGrading
    description: Information that permits to assess the quality level of what will
      be provided
    title: quality grading
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: qualityGrading
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  pathogenIdentification:
    name: pathogenIdentification
    description: The identification of the pathogen or group of pathogens (e.g; name,
      taxon identification, etc.) related to the current item.
    title: pathogen identification
    comments:
    - 'The pathogen identification contains information about name and taxon but in
      some cases(e.g: FAIRSHARING) there may have no direct pathogen related but simply
      a taxonomic information .... the default value should be the root of virology:
      Viruses'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: pathogenIdentification
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: PathogenIdentification
    required: true
    multivalued: true
  relatedDOI:
    name: relatedDOI
    description: Any Digital Object Identifier that can be related
    title: DOI
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P356
    rank: 1000
    alias: relatedDOI
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    - Publication
    range: DOI
    required: false
    multivalued: true
  riskGroup:
    name: riskGroup
    description: The highest risk group related to this resource. The risk group of
      a biological agent guiding its initial handling in labs according to the risk
      group classification defined by the WHO laboratory biosafety manual
    title: risk group
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P12663
    rank: 1000
    alias: riskGroup
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: RiskGroup
    required: false
    recommended: true
    multivalued: false
  biosafetyRestrictions:
    name: biosafetyRestrictions
    description: Information about guidelines and regulations designed to prevent
      the exposure to or release of potentially harmful biological agents. It thereby
      contributes to protecting people and the environment from biohazards while accessing
      this product or service
    title: biosafety restrictions
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: biosafetyRestrictions
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  canItBeUsedToProduceGMO:
    name: canItBeUsedToProduceGMO
    description: Indicates if the current service or product can be used to produce
      GMO
    title: can it be used to produce GMO
    comments:
    - Set to TRUE if it can produce GMO. It is recommended to have a value for this
      field, no value will be understood as unknown
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: canItBeUsedToProduceGMO
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: boolean
    required: true
    recommended: true
    multivalued: false
  provider:
    name: provider
    description: A provider of this product or service, as a specific organization
    title: provider
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: provider
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Provider
    required: true
    multivalued: false
  collection:
    name: collection
    description: The collection(s) to which belongs this item
    title: collection
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: collection
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Collection
    required: true
    multivalued: true
  keywords:
    name: keywords
    description: List of terms used to tag and categorize this Item
    title: keywords
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:keyword
    rank: 1000
    alias: keywords
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Keyword
    required: true
    recommended: true
    multivalued: true
  availability:
    name: availability
    description: The state or condition in which this item is accessible and ready
      for use or can be obtained
    title: availability
    comments:
    - Possible availabilities may differ from a project to another
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    ifabsent: string(on request)
    alias: availability
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  complementaryDocument:
    name: complementaryDocument
    description: Any additional documents that provide supplementary information,
      instructions, or guidelines relevant to the use of this item
    title: complementary document
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: complementaryDocument
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Document
    required: false
    multivalued: true
  technicalRecommendation:
    name: technicalRecommendation
    description: Expert advice or guidelines provided to ensure the optimal use, performance,
      and maintenance of what is provided, including best practices, troubleshooting
      tips, and procedural instructions
    title: technical recommendation
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: technicalRecommendation
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  productPicture:
    name: productPicture
    description: A picture that can represent the item
    title: product picture
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: productPicture
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Image
    required: false
    multivalued: true
  externalRelatedReference:
    name: externalRelatedReference
    description: A reference that permits to retrieve another related item from an
      external provider
    title: external related reference
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: externalRelatedReference
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: ExternalRelatedReference
    required: false
    multivalued: true
  certification:
    name: certification
    description: Any certification related to the current product or service; e.g.,
      ISO certification
    title: certification
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:conformsTo
    rank: 1000
    alias: certification
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: Certification
    required: false
    multivalued: true
  internalReference:
    name: internalReference
    description: Any reference or indication to be used for local retrieval purpose
    title: internal reference
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: internalReference
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  note:
    name: note
    description: An aditional information as a textual comment
    title: note
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: note
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    range: string
    required: false
    multivalued: false
  contactPoint:
    name: contactPoint
    description: An information that allows someone to establish communication
    title: contact point
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dcat:contactPoint
    rank: 1000
    alias: contactPoint
    owner: Nucleic Acid
    domain_of:
    - ProductOrService
    - PersonOrOrganization
    range: ContactPoint
    required: false
    recommended: true
    multivalued: false
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - rdfs:label
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: Nucleic Acid
    domain_of:
    - Dataset
    - DataService
    - Publication
    - Term
    - License
    - Certification
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    title: description
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the resource.

      '
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Nucleic Acid
    domain_of:
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: true
    recommended: true
    multivalued: false

```
</details>