

# Class: Fungus (Fungus)


_The fungus as a biological material_





URI: [EVORAO:Fungus](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Fungus)






```mermaid
 classDiagram
    class Fungus
    click Fungus href "../Fungus"
      Pathogen <|-- Fungus
        click Pathogen href "../Pathogen"
      
      Fungus : accessPointURL
        
      Fungus : additionalCategory
        
          
    
    
    Fungus --> "* _recommended_" ProductCategory : additionalCategory
    click ProductCategory href "../ProductCategory"

        
      Fungus : availability
        
      Fungus : biologicalMaterialOrigin
        
          
    
    
    Fungus --> "1" BiologicalMaterialOrigin : biologicalMaterialOrigin
    click BiologicalMaterialOrigin href "../BiologicalMaterialOrigin"

        
      Fungus : biosafetyRestrictions
        
      Fungus : canItBeUsedToProduceGMO
        
      Fungus : category
        
          
    
    
    Fungus --> "1" ProductCategory : category
    click ProductCategory href "../ProductCategory"

        
      Fungus : certification
        
          
    
    
    Fungus --> "*" Certification : certification
    click Certification href "../Certification"

        
      Fungus : clinicalInformation
        
      Fungus : collection
        
          
    
    
    Fungus --> "1..*" Collection : collection
    click Collection href "../Collection"

        
      Fungus : complementaryDocument
        
          
    
    
    Fungus --> "*" Document : complementaryDocument
    click Document href "../Document"

        
      Fungus : contactPoint
        
          
    
    
    Fungus --> "0..1 _recommended_" ContactPoint : contactPoint
    click ContactPoint href "../ContactPoint"

        
      Fungus : cultivability
        
          
    
    
    Fungus --> "1" CultivabilityEnumeration : cultivability
    click CultivabilityEnumeration href "../CultivabilityEnumeration"

        
      Fungus : description
        
      Fungus : externalRelatedReference
        
          
    
    
    Fungus --> "*" ExternalRelatedReference : externalRelatedReference
    click ExternalRelatedReference href "../ExternalRelatedReference"

        
      Fungus : genomeSequencing
        
          
    
    
    Fungus --> "1" GenomeSequencingEnumeration : genomeSequencing
    click GenomeSequencingEnumeration href "../GenomeSequencingEnumeration"

        
      Fungus : hasIATAClassification
        
          
    
    
    Fungus --> "1" IATAClassification : hasIATAClassification
    click IATAClassification href "../IATAClassification"

        
      Fungus : identificationTechnique
        
      Fungus : infectivity
        
          
    
    
    Fungus --> "1" InfectivityEnumeration : infectivity
    click InfectivityEnumeration href "../InfectivityEnumeration"

        
      Fungus : infectivityTest
        
      Fungus : internalReference
        
      Fungus : isolationConditions
        
      Fungus : isolationHost
        
          
    
    
    Fungus --> "*" IsolationHost : isolationHost
    click IsolationHost href "../IsolationHost"

        
      Fungus : isolationTechnique
        
      Fungus : keywords
        
          
    
    
    Fungus --> "1..* _recommended_" Keyword : keywords
    click Keyword href "../Keyword"

        
      Fungus : letterOfAuthority
        
          
    
    
    Fungus --> "1" LetterOfAuthorityEnumeration : letterOfAuthority
    click LetterOfAuthorityEnumeration href "../LetterOfAuthorityEnumeration"

        
      Fungus : materialSafetyDataSheet
        
          
    
    
    Fungus --> "0..1" MSDS : materialSafetyDataSheet
    click MSDS href "../MSDS"

        
      Fungus : name
        
      Fungus : note
        
      Fungus : originator
        
          
    
    
    Fungus --> "0..1" Originator : originator
    click Originator href "../Originator"

        
      Fungus : passage
        
      Fungus : pathogenIdentification
        
          
    
    
    Fungus --> "1..*" PathogenIdentification : pathogenIdentification
    click PathogenIdentification href "../PathogenIdentification"

        
      Fungus : productionCellLine
        
          
    
    
    Fungus --> "*" ProductionCellLine : productionCellLine
    click ProductionCellLine href "../ProductionCellLine"

        
      Fungus : productPicture
        
          
    
    
    Fungus --> "*" Image : productPicture
    click Image href "../Image"

        
      Fungus : propagationHost
        
          
    
    
    Fungus --> "*" PropagationHost : propagationHost
    click PropagationHost href "../PropagationHost"

        
      Fungus : provider
        
          
    
    
    Fungus --> "1" Provider : provider
    click Provider href "../Provider"

        
      Fungus : qualityGrading
        
      Fungus : refSKU
        
      Fungus : relatedDOI
        
          
    
    
    Fungus --> "*" DOI : relatedDOI
    click DOI href "../DOI"

        
      Fungus : riskGroup
        
          
    
    
    Fungus --> "0..1 _recommended_" RiskGroup : riskGroup
    click RiskGroup href "../RiskGroup"

        
      Fungus : sequence
        
          
    
    
    Fungus --> "1..*" Sequence : sequence
    click Sequence href "../Sequence"

        
      Fungus : shippingConditions
        
      Fungus : storageConditions
        
      Fungus : suspectedEpidemiologicalOrigin
        
          
    
    
    Fungus --> "*" GeographicalOrigin : suspectedEpidemiologicalOrigin
    click GeographicalOrigin href "../GeographicalOrigin"

        
      Fungus : technicalRecommendation
        
      Fungus : thirdPartyDistributionConsent
        
      Fungus : titer
        
      Fungus : transmissionMethod
        
          
    
    
    Fungus --> "*" TransmissionMethod : transmissionMethod
    click TransmissionMethod href "../TransmissionMethod"

        
      Fungus : unitCost
        
      Fungus : unitDefinition
        
      Fungus : usageRestrictions
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [ProductOrService](ProductOrService.md)
            * [Product](Product.md)
                * [Pathogen](Pathogen.md)
                    * **Fungus**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [biologicalMaterialOrigin](biologicalMaterialOrigin.md) | 1 <br/> [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, essential for access... | [Pathogen](Pathogen.md) |
| [suspectedEpidemiologicalOrigin](suspectedEpidemiologicalOrigin.md) | * <br/> [GeographicalOrigin](GeographicalOrigin.md) | The potential geographical or environmental source from which the pathogen is... | [Pathogen](Pathogen.md) |
| [isolationHost](isolationHost.md) | * <br/> [IsolationHost](IsolationHost.md) | The host organism from which the pathogen was originally isolated | [Pathogen](Pathogen.md) |
| [productionCellLine](productionCellLine.md) | * <br/> [ProductionCellLine](ProductionCellLine.md) | The cell line used for the production or propagation of the pathogen, detaili... | [Pathogen](Pathogen.md) |
| [propagationHost](propagationHost.md) | * <br/> [PropagationHost](PropagationHost.md) | The host organism that propagates the pathogen | [Pathogen](Pathogen.md) |
| [transmissionMethod](transmissionMethod.md) | * <br/> [TransmissionMethod](TransmissionMethod.md) | The method or route through which the pathogen is transmitted from one host t... | [Pathogen](Pathogen.md) |
| [sequence](sequence.md) | 1..* <br/> [Sequence](Sequence.md) | The related sequence information from a sequence provider or in fasta format | [Pathogen](Pathogen.md) |
| [cultivability](cultivability.md) | 1 <br/> [CultivabilityEnumeration](CultivabilityEnumeration.md) | The ability of the pathogen to be cultivated or grown in laboratory condition... | [Pathogen](Pathogen.md) |
| [clinicalInformation](clinicalInformation.md) | 0..1 <br/> [String](String.md) | Details about the clinical aspects of the pathogen, including symptoms, sever... | [Pathogen](Pathogen.md) |
| [identificationTechnique](identificationTechnique.md) | 0..1 <br/> [String](String.md) | The method or technique used to identify and confirm the presence of the path... | [Pathogen](Pathogen.md) |
| [infectivity](infectivity.md) | 1 <br/> [InfectivityEnumeration](InfectivityEnumeration.md) | Indicates the ability of the pathogen to establish an infection in a host org... | [Pathogen](Pathogen.md) |
| [infectivityTest](infectivityTest.md) | 0..1 <br/> [String](String.md) | The description of the completed infectivity test, providing details on the m... | [Pathogen](Pathogen.md) |
| [isolationTechnique](isolationTechnique.md) | 0..1 <br/> [String](String.md) | The specific method or procedure used to isolate the pathogen from a host org... | [Pathogen](Pathogen.md) |
| [isolationConditions](isolationConditions.md) | 0..1 <br/> [String](String.md) | The environmental and procedural conditions under which the pathogen was isol... | [Pathogen](Pathogen.md) |
| [letterOfAuthority](letterOfAuthority.md) | 1 <br/> [LetterOfAuthorityEnumeration](LetterOfAuthorityEnumeration.md) | Indicate whether a Letter of Authority is required, confirming the necessity ... | [Pathogen](Pathogen.md) |
| [passage](passage.md) | 0..1 <br/> [String](String.md) | The number of times the pathogen was cultured through serial passage, a proce... | [Pathogen](Pathogen.md) |
| [genomeSequencing](genomeSequencing.md) | 1 <br/> [GenomeSequencingEnumeration](GenomeSequencingEnumeration.md) | The extent of the pathogen's genetic material that has been sequenced, with p... | [Pathogen](Pathogen.md) |
| [titer](titer.md) | 1 <br/> [String](String.md) | The titer value, its corresponding unit, and the method of quantification (e | [Pathogen](Pathogen.md) |
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
| [relatedDOI](relatedDOI.md) | * <br/> [DOI](DOI.md) | Any DOI that can be related | [ProductOrService](ProductOrService.md) |
| [riskGroup](riskGroup.md) | 0..1 _recommended_ <br/> [RiskGroup](RiskGroup.md) | The highest risk group related to this resource | [ProductOrService](ProductOrService.md) |
| [biosafetyRestrictions](biosafetyRestrictions.md) | 0..1 <br/> [String](String.md) | Information about guidelines and regulations designed to prevent the exposure... | [ProductOrService](ProductOrService.md) |
| [canItBeUsedToProduceGMO](canItBeUsedToProduceGMO.md) | 0..1 _recommended_ <br/> [Boolean](Boolean.md) | Indicates if the current service or product can be used to produce GMO | [ProductOrService](ProductOrService.md) |
| [provider](provider.md) | 1 <br/> [Provider](Provider.md) | A provider of this product or service, as a specific organization | [ProductOrService](ProductOrService.md) |
| [collection](collection.md) | 1..* <br/> [Collection](Collection.md) | The collection(s) to which belongs this item | [ProductOrService](ProductOrService.md) |
| [keywords](keywords.md) | 1..* _recommended_ <br/> [Keyword](Keyword.md) | List of terms used to tag and categorize this Item | [ProductOrService](ProductOrService.md) |
| [availability](availability.md) | 1 <br/> [String](String.md) | The state or condition in which this item is accessible and ready for use or ... | [ProductOrService](ProductOrService.md) |
| [complementaryDocument](complementaryDocument.md) | * <br/> [Document](Document.md) | Any complementary document that can be related to this Item | [ProductOrService](ProductOrService.md) |
| [technicalRecommendation](technicalRecommendation.md) | 0..1 <br/> [String](String.md) | Expert advice or guidelines provided to ensure the optimal use, performance, ... | [ProductOrService](ProductOrService.md) |
| [productPicture](productPicture.md) | * <br/> [Image](Image.md) | A picture that can represent the item | [ProductOrService](ProductOrService.md) |
| [externalRelatedReference](externalRelatedReference.md) | * <br/> [ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve another related item from an external pr... | [ProductOrService](ProductOrService.md) |
| [certification](certification.md) | * <br/> [Certification](Certification.md) | Any certification related to the current product or service; e | [ProductOrService](ProductOrService.md) |
| [internalReference](internalReference.md) | 0..1 <br/> [String](String.md) | Any reference or indication to be used for local retrieval purpose | [ProductOrService](ProductOrService.md) |
| [note](note.md) | 0..1 <br/> [String](String.md) | An aditional information as a textual comment | [ProductOrService](ProductOrService.md) |
| [contactPoint](contactPoint.md) | 0..1 _recommended_ <br/> [ContactPoint](ContactPoint.md) | An information that allows someone to establish communication | [ProductOrService](ProductOrService.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Fungus |
| native | EVORAO:Fungus |
| close | wd:Q764 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fungus
description: The fungus as a biological material
title: Fungus
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q764
is_a: Pathogen

```
</details>

### Induced

<details>
```yaml
name: Fungus
description: The fungus as a biological material
title: Fungus
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q764
is_a: Pathogen
attributes:
  biologicalMaterialOrigin:
    name: biologicalMaterialOrigin
    description: Information about the origin of the biological material, essential
      for access, utilization, and benefit-sharing of genetic resources in compliance
      with the Nagoya Protocol.
    title: Biological Material origin
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: biologicalMaterialOrigin
    owner: Fungus
    domain_of:
    - Protein
    - Nucleic Acid
    - Pathogen
    range: BiologicalMaterialOrigin
    required: true
    multivalued: false
  suspectedEpidemiologicalOrigin:
    name: suspectedEpidemiologicalOrigin
    description: The potential geographical or environmental source from which the
      pathogen is believed to have originated or been transmitted
    title: suspected epidemiological origin
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - dct:spatial
    rank: 1000
    alias: suspectedEpidemiologicalOrigin
    owner: Fungus
    domain_of:
    - Pathogen
    range: GeographicalOrigin
    required: false
    multivalued: true
  isolationHost:
    name: isolationHost
    description: The host organism from which the pathogen was originally isolated
    title: isolation host
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: isolationHost
    owner: Fungus
    domain_of:
    - Pathogen
    range: IsolationHost
    required: false
    multivalued: true
  productionCellLine:
    name: productionCellLine
    description: The cell line used for the production or propagation of the pathogen,
      detailing the cellular environment employed in its cultivation and study
    title: production cell line
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: productionCellLine
    owner: Fungus
    domain_of:
    - Pathogen
    range: ProductionCellLine
    required: false
    multivalued: true
  propagationHost:
    name: propagationHost
    description: The host organism that propagates the pathogen
    title: propagation host
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: propagationHost
    owner: Fungus
    domain_of:
    - Pathogen
    range: PropagationHost
    required: false
    multivalued: true
  transmissionMethod:
    name: transmissionMethod
    description: The method or route through which the pathogen is transmitted from
      one host to another, detailing the mechanisms of infection spread.
    title: transmission method
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: transmissionMethod
    owner: Fungus
    domain_of:
    - Pathogen
    range: TransmissionMethod
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
    owner: Fungus
    domain_of:
    - RecombinantPartIdentification
    - Protein
    - Nucleic Acid
    - Pathogen
    range: Sequence
    required: true
    multivalued: true
  cultivability:
    name: cultivability
    description: The ability of the pathogen to be cultivated or grown in laboratory
      conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen"
      or "Inactivated pathogen"
    title: cultivability
    comments:
    - Might also be related to a product sub-category that helps filtering
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    ifabsent: string(Cultivable)
    alias: cultivability
    owner: Fungus
    domain_of:
    - Pathogen
    range: cultivabilityEnumeration
    required: true
    multivalued: false
  clinicalInformation:
    name: clinicalInformation
    description: Details about the clinical aspects of the pathogen, including symptoms,
      severity, treatment protocols, and patient outcomes
    title: clinical information
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: clinicalInformation
    owner: Fungus
    domain_of:
    - Pathogen
    range: string
    required: false
    multivalued: false
  identificationTechnique:
    name: identificationTechnique
    description: The method or technique used to identify and confirm the presence
      of the pathogen, detailing the specific procedures and tools employed in the
      detection process
    title: identification technique
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: identificationTechnique
    owner: Fungus
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
    required: false
    multivalued: false
  infectivity:
    name: infectivity
    description: Indicates the ability of the pathogen to establish an infection in
      a host organism, with possible values detailing whether infectivity has been
      tested, quantified, or cannot be tested due to non-cultivable nature.
    title: infectivity
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: infectivity
    owner: Fungus
    domain_of:
    - Pathogen
    range: infectivityEnumeration
    required: true
    multivalued: false
  infectivityTest:
    name: infectivityTest
    description: The description of the completed infectivity test, providing details
      on the methods, conditions, and results of the test used to assess the pathogen's
      ability to infect a host organism
    title: infectivity Test
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: infectivityTest
    owner: Fungus
    domain_of:
    - Pathogen
    range: string
    required: false
    multivalued: false
  isolationTechnique:
    name: isolationTechnique
    description: The specific method or procedure used to isolate the pathogen from
      a host organism or sample, detailing the techniques and tools employed in the
      isolation process
    title: isolation technique
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: isolationTechnique
    owner: Fungus
    domain_of:
    - Pathogen
    range: string
    required: false
    multivalued: false
  isolationConditions:
    name: isolationConditions
    description: The environmental and procedural conditions under which the pathogen
      was isolated
    title: isolation conditions
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: isolationConditions
    owner: Fungus
    domain_of:
    - Pathogen
    range: string
    required: false
    multivalued: false
  letterOfAuthority:
    name: letterOfAuthority
    description: Indicate whether a Letter of Authority is required, confirming the
      necessity of formal authorization. The possible values are "N/A", "NOT Required",
      "Required for customers in the EU" or "Required"
    title: letter of authority
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    ifabsent: string(Not applicable)
    alias: letterOfAuthority
    owner: Fungus
    domain_of:
    - Pathogen
    range: letterOfAuthorityEnumeration
    required: true
    multivalued: false
  passage:
    name: passage
    description: The number of times the pathogen was cultured through serial passage,
      a process used to increase the stock but which can also lead to the evolution
      of the original pathogen.
    title: passage
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: passage
    owner: Fungus
    domain_of:
    - Pathogen
    range: string
    required: false
    multivalued: false
  genomeSequencing:
    name: genomeSequencing
    description: The extent of the pathogen's genetic material that has been sequenced,
      with possible values including "Complete genome" for the entire genome, "Complete
      coding sequence" for all coding regions, and "Partial sequence" for only a portion
      of the genetic material
    title: genome sequencing
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: genomeSequencing
    owner: Fungus
    domain_of:
    - Pathogen
    range: genomeSequencingEnumeration
    required: true
    multivalued: false
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
    owner: Fungus
    domain_of:
    - Nucleic Acid
    - Pathogen
    range: string
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    - e.g, could be a xsd:string in enumeration ("Freeze Dried", "Liquid Nitrogen",
      "Viral Storage Medium -20C", "Viral Storage Medium -80C", "Living plant material
      (>= +4°C)", "Gas Phase", "Ethanol -20C", "Ethanol -80C", "Dried")
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: storageConditions
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
    domain_of:
    - ProductOrService
    range: PathogenIdentification
    required: true
    multivalued: true
  relatedDOI:
    name: relatedDOI
    description: Any DOI that can be related
    title: DOI
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P356
    rank: 1000
    alias: relatedDOI
    owner: Fungus
    domain_of:
    - Publication
    - ProductOrService
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
    domain_of:
    - ProductOrService
    range: boolean
    required: false
    recommended: true
    multivalued: false
  provider:
    name: provider
    description: A provider of this product or service, as a specific organization
    title: provider
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: provider
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
    domain_of:
    - ProductOrService
    range: string
    required: true
    multivalued: false
  complementaryDocument:
    name: complementaryDocument
    description: Any complementary document that can be related to this Item
    title: complementary document
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: complementaryDocument
    owner: Fungus
    domain_of:
    - ProductOrService
    - Bundle
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
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
    owner: Fungus
    domain_of:
    - PersonOrOrganization
    - ProductOrService
    range: ContactPoint
    required: false
    recommended: true
    multivalued: false
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Fungus
    domain_of:
    - Nameable
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
      present the item.

      '
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Fungus
    domain_of:
    - Nameable
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>