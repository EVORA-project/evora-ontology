
# EVORA


**metamodel version:** 1.7.0

**version:** 1.0.7341


The EVORA Ontology harmonizes metadata in virology to describe viral resources, their derived products, and services. It aligns with FAIR principles to ensure interoperability, accessibility, and reusability across various projects. The EVORA Ontology aims to support preparedness and response to pandemics.


### Classes

 * [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access
     * [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) - Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
     * [BiologicalPartOrigin](BiologicalPartOrigin.md) - Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material
         * [NaturalPartOrigin](NaturalPartOrigin.md) - Information on the origin of a natural part that composes the biological material
         * [SyntheticPartOrigin](SyntheticPartOrigin.md) - Information on the origin of a synthetic part that composes the biological material
     * [ExternalRelatedReference](ExternalRelatedReference.md) - A reference that permits to retrieve an item from an external provider
     * [MSDS](MSDS.md) - A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
     * [PathogenIdentification](PathogenIdentification.md) - A collection of distinguishing information that enables the differentiation of a pathogen from another
     * [Publication](Publication.md) - A scientific publication
     * [Sequence](Sequence.md) - A nucleic acid or protein sequence information
     * [SequenceReference](SequenceReference.md) - A reference that permits to retrieve the sequence information from a sequence provider
     * [Version](Version.md) - Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)
 * [Nameable](Nameable.md) - Any entity that has a name and can have a textual description
     * [Catalogue](Catalogue.md) - A curated collection of metadata about resources
         * [Collection](Collection.md) - Set of products and services with some common characteristics
         * [Taxonomy](Taxonomy.md) - Science of naming, defining and classifying organisms
         * [Vocabulary](Vocabulary.md) - A subset of words or phrases specific to a particular subject or field
     * [Certification](Certification.md) - Assurance given by an independent certification body that a product, service or system meets the requirements of a standard
     * [ContactPoint](ContactPoint.md) - Entity serving as focal point of information
     * [DataService](DataService.md) - A collection of operations that provides access to one or more datasets or data processing functions
         * [DataProvider](DataProvider.md) - An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources
     * [File](File.md) - Digital document or record stored in a specific format that contains data or information
         * [Audio](Audio.md) - Subclass of File representing sound recordings or audio tracks
         * [Data](Data.md) - Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information
         * [Document](Document.md) - Subclass of File representing textual or written files such as reports, manuals, or forms
         * [Image](Image.md) - Subclass of File representing visual content such as pictures, diagrams, or illustrations
         * [Video](Video.md) - Subclass of File representing moving visual media, such as recordings, presentations, or movies
     * [License](License.md) - The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
     * [NamedDataset](NamedDataset.md) - A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access
         * [ProductOrService](ProductOrService.md) - A product or a service
             * [Product](Product.md) - A product
                 * [Antibody](Antibody.md) - Protein that can bind to certain types of foreign bodies, such as pathogens
                     * [Hybridoma](Hybridoma.md) - An hybridoma that provides antibodies that can be related to a pathogen
                 * [Bundle](Bundle.md) - A group of products
                 * [DetectionKit](DetectionKit.md) - A detection kit for specific pathogens
                 * [NucleicAcid](NucleicAcid.md) - Nucleic acid related to a pathogen. It can be extracted or synthetic
                 * [Pathogen](Pathogen.md) - Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus
                     * [Bacterium](Bacterium.md) - The bacterium as a biological material
                     * [Fungus](Fungus.md) - The fungus as a biological material
                     * [Prion](Prion.md) - The prion as a biological material
                     * [Protozoan](Protozoan.md) - The protozoan as a biological material
                     * [Viroid](Viroid.md) - The viroid as a biological material
                     * [Virus](Virus.md) - The virus as a biological material
                 * [Protein](Protein.md) - A protein as a derived product from a pathogen
             * [Service](Service.md) - A service
         * [Term](Term.md) - Word or phrase from a specialized area of knowledge
             * [AlternateName](AlternateName.md) - List of alternate names for things
             * [CommonName](CommonName.md) - Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name
                 * [Variant](Variant.md) - An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
                 * [VirusName](VirusName.md) - A virus vernacular name or a name that describes a group of viruses
             * [Country](Country.md) - The country as of ISO3166
             * [DOI](DOI.md) - A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard
             * [ExpressionVector](ExpressionVector.md) - A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression
             * [GeographicalOrigin](GeographicalOrigin.md) - The specific location or region where a physical item, originates or is naturally found
                 * [IPLCOrigin](IPLCOrigin.md) - The IPLC area (Indigenous People and Local Communities) from which a physical item originates
             * [IATAClassification](IATAClassification.md) - The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air
             * [IsolationHost](IsolationHost.md) - Host organism from which the pathogen was isolated
             * [Journal](Journal.md) - Periodical journal publishing scientific research
             * [Keyword](Keyword.md) - A term or phrase used to tag and categorize content
             * [PDBReference](PDBReference.md) - Identifier for 3D structural data as per the PDB (Protein Data Bank) database
             * [PlasmidSelection](PlasmidSelection.md) - The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers
             * [ProductCategory](ProductCategory.md) - A term used to classify a group of products that share common characteristics or functions, which helps in their organization
             * [ProductionCellLine](ProductionCellLine.md) - A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances
             * [PropagationHost](PropagationHost.md) - The organism used to grow and multiply the pathogen under controlled conditions
             * [ProteinTag](ProteinTag.md) - Peptide sequence genetically grafted onto a recombinant protein
             * [RiskGroup](RiskGroup.md) - Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence
             * [SpecialFeature](SpecialFeature.md) - Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
             * [Taxon](Taxon.md) - Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit
             * [TaxonomicRank](TaxonomicRank.md) - The possible taxonomic ranks and their description
             * [TransmissionMethod](TransmissionMethod.md) - The process by which the pathogen spreads between hosts
     * [PersonOrOrganization](PersonOrOrganization.md) - A person or an organization
         * [Organization](Organization.md) - A social entity established to meet needs or pursue specific goals
             * [Provider](Provider.md) - A provider of products or services, as a specific organization
             * [RI](RI.md) - A research infrastructure
         * [Originator](Originator.md) - The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
         * [Person](Person.md) - An individual
 * [RecombinantPartIdentification](RecombinantPartIdentification.md) - Identification of a recombinant part

### Mixins


### Slots

 * [ID](ID.md)
     * [Version➞ID](Version_ID.md) - The version identifier
 * [abstract](abstract.md)
     * [Publication➞abstract](Publication_abstract.md) - Concise summary of the publication
 * [accessPointURL](accessPointURL.md)
     * [ProductOrService➞accessPointURL](ProductOrService_accessPointURL.md) - The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
 * [accessToPhysicalGeneticResource](accessToPhysicalGeneticResource.md)
     * [BiologicalPartOrigin➞accessToPhysicalGeneticResource](BiologicalPartOrigin_accessToPhysicalGeneticResource.md) - Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
 * [accessionNumber](accessionNumber.md)
     * [SequenceReference➞accessionNumber](SequenceReference_accessionNumber.md) - The sequence ID that permits to retrieve the sequence information from the sequence provider
 * [accidentalReleaseMeasures](accidentalReleaseMeasures.md)
     * [MSDS➞accidentalReleaseMeasures](MSDS_accidentalReleaseMeasures.md) - Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.
 * [additionalCategory](additionalCategory.md)
     * [ProductOrService➞additionalCategory](ProductOrService_additionalCategory.md) - Any category apart from its main category in which this product or service can fit
 * [addressCountry](addressCountry.md)
     * [ContactPoint➞addressCountry](ContactPoint_addressCountry.md) - The country as of  ISO 3166
 * [addressLocality](addressLocality.md)
     * [ContactPoint➞addressLocality](ContactPoint_addressLocality.md) - The locality in which the street address is, and which is in the region. e.g, the city
 * [addressRegion](addressRegion.md)
     * [ContactPoint➞addressRegion](ContactPoint_addressRegion.md) - The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division
 * [alpha2Code](alpha2Code.md)
     * [Country➞alpha2Code](Country_alpha2Code.md) - Two-letter country codes from ISO 3166-1 alpha-2
 * [altText](altText.md)
     * [Image➞altText](Image_altText.md) - An alternate text for the image, if the image cannot be displayed
 * [alternateName](alternateName.md)
     * [AlternateName➞alternateName](AlternateName_alternateName.md) - Any known alternate name related to this name
     * [CommonName➞alternateName](CommonName_alternateName.md) - Any known alternate name related to this name
     * [Organization➞alternateName](Organization_alternateName.md) - An alternate name or acronym
 * [antibodyPurifiedByAffinity](antibodyPurifiedByAffinity.md)
     * [Antibody➞antibodyPurifiedByAffinity](Antibody_antibodyPurifiedByAffinity.md) - Indicates whether or not if the antibody was purified by affinity
 * [authors](authors.md)
     * [Publication➞authors](Publication_authors.md) - The list of authors
 * [availability](availability.md)
     * [ProductOrService➞availability](ProductOrService_availability.md) - The state or condition in which this item is accessible and ready for use or can be obtained
 * [beforeDate](beforeDate.md)
     * [NaturalPartOrigin➞beforeDate](NaturalPartOrigin_beforeDate.md) - Set to TRUE if a proxy date for the collection date is used
 * [biologicalMaterialOrigin](biologicalMaterialOrigin.md)
     * [Nucleic Acid➞biologicalMaterialOrigin](Nucleic_Acid_biologicalMaterialOrigin.md) - Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
     * [Pathogen➞biologicalMaterialOrigin](Pathogen_biologicalMaterialOrigin.md) - Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
     * [Protein➞biologicalMaterialOrigin](Protein_biologicalMaterialOrigin.md) - Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
 * [biologicalPartOrigin](biologicalPartOrigin.md)
     * [BiologicalMaterialOrigin➞biologicalPartOrigin](BiologicalMaterialOrigin_biologicalPartOrigin.md) - Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.
 * [biologicalSourceType](biologicalSourceType.md)
     * [BiologicalMaterialOrigin➞biologicalSourceType](BiologicalMaterialOrigin_biologicalSourceType.md) - Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!
 * [biosafetyRestrictions](biosafetyRestrictions.md)
     * [ProductOrService➞biosafetyRestrictions](ProductOrService_biosafetyRestrictions.md) - Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
 * [canItBeUsedToProduceGMO](canItBeUsedToProduceGMO.md)
     * [ProductOrService➞canItBeUsedToProduceGMO](ProductOrService_canItBeUsedToProduceGMO.md) - Indicates if the current service or product can be used to produce GMO
 * [category](category.md)
     * [ProductOrService➞category](ProductOrService_category.md) - The main category of the service or product
 * [certification](certification.md)
     * [ProductOrService➞certification](ProductOrService_certification.md) - Any certification related to the current product or service; e.g., ISO certification
 * [certificationDocument](certificationDocument.md)
     * [Certification➞certificationDocument](Certification_certificationDocument.md) - The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.
 * [clinicalInformation](clinicalInformation.md)
     * [Pathogen➞clinicalInformation](Pathogen_clinicalInformation.md) - Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
 * [clonedIntoPlasmid](clonedIntoPlasmid.md)
     * [Nucleic Acid➞clonedIntoPlasmid](Nucleic_Acid_clonedIntoPlasmid.md) - The plasmid into which the nucleic acid has been cloned
 * [coInfectingViruses](coInfectingViruses.md)
     * [Virus➞coInfectingViruses](Virus_coInfectingViruses.md) - Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.
 * [collection](collection.md)
     * [ProductOrService➞collection](ProductOrService_collection.md) - The collection(s) to which belongs this item
 * [collectionDataProvider](collectionDataProvider.md)
     * [Collection➞collectionDataProvider](Collection_collectionDataProvider.md) - The provider of the data of the collection
 * [collectionDate](collectionDate.md)
     * [NaturalPartOrigin➞collectionDate](NaturalPartOrigin_collectionDate.md) - The date when the sample was collected in situ. If unknown/private, use a proxy date such as "date received" and indicate this by setting to true the before date property
 * [collectionItem](collectionItem.md)
     * [Collection➞collectionItem](Collection_collectionItem.md) - An item of the collection
 * [complementaryDocument](complementaryDocument.md)
     * [ProductOrService➞complementaryDocument](ProductOrService_complementaryDocument.md) - Any complementary document that can be related to this Item
         * [Bundle➞complementaryDocument](Bundle_complementaryDocument.md) - Links the bundle to any additional documents that provide supplementary information, instructions, or guidelines relevant to the use and assembly of the bundle's products.
 * [contactPoint](contactPoint.md)
     * [PersonOrOrganization➞contactPoint](PersonOrOrganization_contactPoint.md) - An information that allows someone to establish communication
     * [ProductOrService➞contactPoint](ProductOrService_contactPoint.md) - An information that allows someone to establish communication
 * [contaminationWithCoInfectingViruses](contaminationWithCoInfectingViruses.md)
     * [Virus➞contaminationWithCoInfectingViruses](Virus_contaminationWithCoInfectingViruses.md) - A boolean value indicating whether there is contamination with co-infecting viruses
 * [contentType](contentType.md)
     * [DataProvider➞contentType](DataProvider_contentType.md) - The content type of the response to the queries
 * [contentURL](contentURL.md)
     * [File➞contentURL](File_contentURL.md) - The web address or location where the file content is stored and can be accessed or downloaded.
 * [country](country.md)
     * [Organization➞country](Organization_country.md) - The country of the organization
 * [countryOfCollection](countryOfCollection.md)
     * [NaturalPartOrigin➞countryOfCollection](NaturalPartOrigin_countryOfCollection.md) - The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to "country of origin".
 * [cultivability](cultivability.md)
     * [Pathogen➞cultivability](Pathogen_cultivability.md) - The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
 * [description](description.md)
     * [Nameable➞description](Nameable_description.md) - A short explanation of the characteristics, features, or nature of the current item
 * [descriptionOfModificationsMadeFromTheReferenceSequences](descriptionOfModificationsMadeFromTheReferenceSequences.md)
     * [SyntheticPartOrigin➞descriptionOfModificationsMadeFromTheReferenceSequences](SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences.md) - List the modifications mades from the reference sequence if any
 * [disposalConsiderations](disposalConsiderations.md)
     * [MSDS➞disposalConsiderations](MSDS_disposalConsiderations.md) - Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.
 * [domain](domain.md)
     * [Protein➞domain](Protein_domain.md) - A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function
 * [ecologicalInformation](ecologicalInformation.md)
     * [MSDS➞ecologicalInformation](MSDS_ecologicalInformation.md) - Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.
 * [email](email.md)
     * [ContactPoint➞email](ContactPoint_email.md) - Email address
 * [exposureControlsPersonalProtection](exposureControlsPersonalProtection.md)
     * [MSDS➞exposureControlsPersonalProtection](MSDS_exposureControlsPersonalProtection.md) - Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.
 * [expressedAs](expressedAs.md)
     * [Protein➞expressedAs](Protein_expressedAs.md) - Refers to the form in which the protein is produced and manifested in a biological system. Possible values include "Soluble" (proteins that are dissolved in the cellular or extracellular fluid) and "Inclusion bodies" (aggregated proteins that are insoluble and form within the cell)
 * [expressionSystem](expressionSystem.md)
     * [Protein➞expressionSystem](Protein_expressionSystem.md) - The host organism or cellular environment used to produce a protein from a specific gene. Possible values include "E. coli" (bacterial system), "Insect cells" (using baculovirus vectors), and "Mammalian cells" (mammalian cell lines).
 * [externalEquivalentTaxon](externalEquivalentTaxon.md)
     * [Taxon➞externalEquivalentTaxon](Taxon_externalEquivalentTaxon.md) - Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)
 * [externalRelatedReference](externalRelatedReference.md)
     * [ProductOrService➞externalRelatedReference](ProductOrService_externalRelatedReference.md) - A reference that permits to retrieve another related item from an external provider
 * [fireFightingMeasures](fireFightingMeasures.md)
     * [MSDS➞fireFightingMeasures](MSDS_fireFightingMeasures.md) - Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.
 * [firstAidMeasures](firstAidMeasures.md)
     * [MSDS➞firstAidMeasures](MSDS_firstAidMeasures.md) - Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.
 * [format](format.md)
     * [File➞format](File_format.md) - The file type or format that indicates how the data within the file is structured
 * [functionalCharacterization](functionalCharacterization.md)
     * [Protein➞functionalCharacterization](Protein_functionalCharacterization.md) - The process of determining and describing the specific biological activities and roles of a protein. Possible values include "Functionally characterized" (the protein's functions have been identified and described) and "No functional characterization" (the protein's functions have not been identified or described).
 * [functionalTechnicalDescription](functionalTechnicalDescription.md)
     * [Protein➞functionalTechnicalDescription](Protein_functionalTechnicalDescription.md) - Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.
 * [furtherInformation](furtherInformation.md)
     * [MSDS➞furtherInformation](MSDS_furtherInformation.md) - Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.
 * [genotype](genotype.md)
     * [PathogenIdentification➞genotype](PathogenIdentification_genotype.md) - Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes
 * [handlingAndStorage](handlingAndStorage.md)
     * [MSDS➞handlingAndStorage](MSDS_handlingAndStorage.md) - Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.
 * [hasGbFileOfTheConstruct](hasGbFileOfTheConstruct.md)
     * [Nucleic Acid➞hasGbFileOfTheConstruct](Nucleic_Acid_hasGbFileOfTheConstruct.md) - A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct
 * [hasIATAClassification](hasIATAClassification.md)
     * [Product➞hasIATAClassification](Product_hasIATAClassification.md) - The corresponding International Air Transport Association (IATA)'s category for this Product
 * [hasSOPFile](hasSOPFile.md)
     * [Detection Kit➞hasSOPFile](Detection_Kit_hasSOPFile.md) - The related standard operating procedure file
 * [hasTAG](hasTAG.md)
     * [Nucleic Acid➞hasTAG](Nucleic_Acid_hasTAG.md) - TAG sequence used for purposes such as purification, detection, or localization
 * [hazardsIdentification](hazardsIdentification.md)
     * [MSDS➞hazardsIdentification](MSDS_hazardsIdentification.md) - Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.
 * [homePage](homePage.md)
     * [PersonOrOrganization➞homePage](PersonOrOrganization_homePage.md) - Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
 * [hostType](hostType.md)
     * [PathogenIdentification➞hostType](PathogenIdentification_hostType.md) - Indication of the possible host(s) for the identified pathogens among the listed main categories
 * [hybridomaDescription](hybridomaDescription.md)
     * [Hybridoma➞hybridomaDescription](Hybridoma_hybridomaDescription.md) - The description of the hybridoma
 * [identificationTechnique](identificationTechnique.md)
     * [Nucleic Acid➞identificationTechnique](Nucleic_Acid_identificationTechnique.md) - The method used to identify the nucleic acid sequence or its associated constructs, such as PCR, sequencing, or hybridization
     * [Pathogen➞identificationTechnique](Pathogen_identificationTechnique.md) - The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
 * [inVocabulary](inVocabulary.md)
     * [Term➞inVocabulary](Term_inVocabulary.md) - Terms belong to a specific vocabulary
 * [inclusionBodiesType](inclusionBodiesType.md)
     * [Protein➞inclusionBodiesType](Protein_inclusionBodiesType.md) - Refers to the state of aggregated proteins within a cell. Possible values include "Denatured" (proteins are in an unfolded, inactive state) and "Refolded" (proteins have been processed to regain their functional, active conformation).
 * [indigenousPoepleAndLocalCommunityOrigin](indigenousPoepleAndLocalCommunityOrigin.md)
     * [NaturalPartOrigin➞indigenousPoepleAndLocalCommunityOrigin](NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin.md) - The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant
 * [infectivity](infectivity.md)
     * [Pathogen➞infectivity](Pathogen_infectivity.md) - Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
 * [infectivityTest](infectivityTest.md)
     * [Pathogen➞infectivityTest](Pathogen_infectivityTest.md) - The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
 * [internalReference](internalReference.md)
     * [ProductOrService➞internalReference](ProductOrService_internalReference.md) - Any reference or indication to be used for local retrieval purpose
 * [isItAClonedNucleicAcid](isItAClonedNucleicAcid.md)
     * [Nucleic Acid➞isItAClonedNucleicAcid](Nucleic_Acid_isItAClonedNucleicAcid.md) - Indicates that the nucleic acid sequence has been inserted into a plasmid vector for propagation or expression in a host organism
 * [isolate](isolate.md)
     * [PathogenIdentification➞isolate](PathogenIdentification_isolate.md) - Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host
 * [isolationConditions](isolationConditions.md)
     * [Pathogen➞isolationConditions](Pathogen_isolationConditions.md) - The environmental and procedural conditions under which the pathogen was isolated
 * [isolationHost](isolationHost.md)
     * [Pathogen➞isolationHost](Pathogen_isolationHost.md) - The host organism from which the pathogen was originally isolated
 * [isolationTechnique](isolationTechnique.md)
     * [Pathogen➞isolationTechnique](Pathogen_isolationTechnique.md) - The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
 * [journal](journal.md)
     * [Publication➞journal](Publication_journal.md) - The scientific journal in which the publication was published
 * [keywords](keywords.md)
     * [ProductOrService➞keywords](ProductOrService_keywords.md) - List of terms used to tag and categorize this Item
 * [letterOfAuthority](letterOfAuthority.md)
     * [Pathogen➞letterOfAuthority](Pathogen_letterOfAuthority.md) - Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
 * [license](license.md)
     * [DataProvider➞license](DataProvider_license.md) - Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
     * [File➞license](File_license.md) - The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
 * [licensingOrAttribution](licensingOrAttribution.md)
     * [License➞licensingOrAttribution](License_licensingOrAttribution.md) - A text or html code that provides any related data sharing licence and/or attribution
 * [loginRequestMethod](loginRequestMethod.md)
     * [DataProvider➞loginRequestMethod](DataProvider_loginRequestMethod.md) - The http request method used to acces the login request url
 * [loginTokenName](loginTokenName.md)
     * [DataProvider➞loginTokenName](DataProvider_loginTokenName.md) - The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query
 * [loginURL](loginURL.md)
     * [DataProvider➞loginURL](DataProvider_loginURL.md) - The URL template that allows to log in if required
 * [logo](logo.md)
     * [Certification➞logo](Certification_logo.md) - A path or URL to the related logo
     * [License➞logo](License_logo.md) - A path or URL to the related logo
     * [PersonOrOrganization➞logo](PersonOrOrganization_logo.md) - A path or URL to the related logo
 * [materialSafetyDataSheet](materialSafetyDataSheet.md)
     * [Product➞materialSafetyDataSheet](Product_materialSafetyDataSheet.md) - A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
 * [memberOfRI](memberOfRI.md)
     * [Provider➞memberOfRI](Provider_memberOfRI.md) - The research infrastructure of which this organization is a member
 * [modelSpecies](modelSpecies.md)
     * [Service➞modelSpecies](Service_modelSpecies.md) - The species of the infected organism in the experiment
 * [modelType](modelType.md)
     * [Service➞modelType](Service_modelType.md) - The specific name of the infected organism, including its modification if necessary
 * [modificationsFromTheReferenceSequences](modificationsFromTheReferenceSequences.md)
     * [SyntheticPartOrigin➞modificationsFromTheReferenceSequences](SyntheticPartOrigin_modificationsFromTheReferenceSequences.md) - Set to TRUE if there was is any modification made from the reference sequence
 * [msdsContact](msdsContact.md)
     * [MSDS➞msdsContact](MSDS_msdsContact.md) - The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.
 * [mutationObserved](mutationObserved.md)
     * [Nucleic Acid➞mutationObserved](Nucleic_Acid_mutationObserved.md) - Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it
 * [mycoplasmicContent](mycoplasmicContent.md)
     * [Virus➞mycoplasmicContent](Virus_mycoplasmicContent.md) - Indicates the presence of mycoplasma contamination within the sample
 * [name](name.md)
     * [Nameable➞name](Nameable_name.md) - The label that allows humans to identify the current item
 * [note](note.md)
     * [ProductOrService➞note](ProductOrService_note.md) - An aditional information as a textual comment
 * [oRCIDiD](oRCIDiD.md)
     * [ContactPoint➞oRCIDiD](ContactPoint_oRCIDiD.md) - Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
     * [Person➞oRCIDiD](Person_oRCIDiD.md) - Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
 * [observedMutations](observedMutations.md)
     * [Nucleic Acid➞observedMutations](Nucleic_Acid_observedMutations.md) - The specific mutations that have been identified and documented in the nucleic acid sequence
 * [originator](originator.md)
     * [Product➞originator](Product_originator.md) - The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
 * [parentCategory](parentCategory.md)
     * [ProductCategory➞parentCategory](ProductCategory_parentCategory.md) - An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.
 * [parentTaxon](parentTaxon.md)
     * [Taxon➞parentTaxon](Taxon_parentTaxon.md) - The parent taxon of the current taxon
 * [partIdentification](partIdentification.md)
     * [RecombinantPartIdentification➞partIdentification](RecombinantPartIdentification_partIdentification.md) - A short designation of this recombinant part of the related biological material
 * [pasmidSelection](pasmidSelection.md)
     * [Nucleic Acid➞pasmidSelection](Nucleic_Acid_pasmidSelection.md) - Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid
 * [passage](passage.md)
     * [Pathogen➞passage](Pathogen_passage.md) - The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
 * [pathogenIdentification](pathogenIdentification.md)
     * [ProductOrService➞pathogenIdentification](ProductOrService_pathogenIdentification.md) - The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
 * [pathogenName](pathogenName.md)
     * [PathogenIdentification➞pathogenName](PathogenIdentification_pathogenName.md) - A pathogen common name or a name that describes a group of pathogens
 * [pathogenType](pathogenType.md)
     * [PathogenIdentification➞pathogenType](PathogenIdentification_pathogenType.md) - Identification of the specific type of pathogen among the listed categories e.g. "Virus","Viroid","Bacterium"...
 * [permitIdentifierForABS](permitIdentifierForABS.md)
     * [NaturalPartOrigin➞permitIdentifierForABS](NaturalPartOrigin_permitIdentifierForABS.md) - Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
 * [physicalChemicalProperties](physicalChemicalProperties.md)
     * [MSDS➞physicalChemicalProperties](MSDS_physicalChemicalProperties.md) - Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage
 * [postalCode](postalCode.md)
     * [ContactPoint➞postalCode](ContactPoint_postalCode.md) - The postal code
 * [previouslyKnownAs](previouslyKnownAs.md)
     * [Taxon➞previouslyKnownAs](Taxon_previouslyKnownAs.md) - Any historic version of this taxon having a different name
 * [productPicture](productPicture.md)
     * [ProductOrService➞productPicture](ProductOrService_productPicture.md) - A picture that can represent the item
 * [productionCellLine](productionCellLine.md)
     * [Pathogen➞productionCellLine](Pathogen_productionCellLine.md) - The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
 * [productionSystem](productionSystem.md)
     * [Antibody➞productionSystem](Antibody_productionSystem.md) - The biological and technological methods and processes used to produce the antibody
 * [productsOfTheBundle](productsOfTheBundle.md)
     * [Bundle➞productsOfTheBundle](Bundle_productsOfTheBundle.md) - Associates the bundle with the individual products it contains, specifying the components included within the bundle.
 * [propagationHost](propagationHost.md)
     * [Pathogen➞propagationHost](Pathogen_propagationHost.md) - The host organism that propagates the pathogen
 * [proteinPurification](proteinPurification.md)
     * [Protein➞proteinPurification](Protein_proteinPurification.md) - Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
 * [proteinTAG](proteinTAG.md)
     * [Protein➞proteinTAG](Protein_proteinTAG.md) - Peptide sequences genetically grafted onto a recombinant protein
 * [providedEntityType](providedEntityType.md)
     * [DataProvider➞providedEntityType](DataProvider_providedEntityType.md) - The identification of the entity type (Class) described by the response to the query
 * [provider](provider.md)
     * [ProductOrService➞provider](ProductOrService_provider.md) - A provider of this product or service, as a specific organization
 * [qualityGrading](qualityGrading.md)
     * [ProductOrService➞qualityGrading](ProductOrService_qualityGrading.md) - Information that permits to assess the quality level of what will be provided
 * [queryMethod](queryMethod.md)
     * [DataProvider➞queryMethod](DataProvider_queryMethod.md) - The http request method used to access the requested query url
 * [queryURL](queryURL.md)
     * [DataProvider➞queryURL](DataProvider_queryURL.md) - The URL template that allows to get the content
 * [rank](rank.md)
     * [Taxon➞rank](Taxon_rank.md) - Relative level or position of the identified taxon in the taxonomy
     * [Taxonomy➞rank](Taxonomy_rank.md) - Relative level or position of the identified taxon in the taxonomy
 * [rankDataProvider](rankDataProvider.md)
     * [Taxonomy➞rankDataProvider](Taxonomy_rankDataProvider.md) - The data provider for the description of the taxonomic ranks used in this taxonomy
 * [recombinantMaterial](recombinantMaterial.md)
     * [BiologicalMaterialOrigin➞recombinantMaterial](BiologicalMaterialOrigin_recombinantMaterial.md) - Indicates if this biological material is a recombinant biological material.
 * [recombinantPartIdentification](recombinantPartIdentification.md)
     * [BiologicalPartOrigin➞recombinantPartIdentification](BiologicalPartOrigin_recombinantPartIdentification.md) - Identification of a recombinant part
 * [refSKU](refSKU.md)
     * [ProductOrService➞refSKU](ProductOrService_refSKU.md) - The reference or the stock keeping unit of the service or item provided in the provider's catalogue
 * [reference](reference.md)
     * [ExternalRelatedReference➞reference](ExternalRelatedReference_reference.md) - The identifier reference of the connected external item
 * [referenceLabel](referenceLabel.md)
     * [ExternalRelatedReference➞referenceLabel](ExternalRelatedReference_referenceLabel.md) - The label informing what this reference is about
 * [referenceProviderName](referenceProviderName.md)
     * [ExternalRelatedReference➞referenceProviderName](ExternalRelatedReference_referenceProviderName.md) - The name for the reference provider
 * [referenceProviderPrefix](referenceProviderPrefix.md)
     * [ExternalRelatedReference➞referenceProviderPrefix](ExternalRelatedReference_referenceProviderPrefix.md) - The url prefix that once completed with the reference will lead to the linked external resource
 * [regionEncompassedInThisProduct](regionEncompassedInThisProduct.md)
     * [Nucleic Acid➞regionEncompassedInThisProduct](Nucleic_Acid_regionEncompassedInThisProduct.md) - The specific region encompassed in the product
 * [regulatoryInformation](regulatoryInformation.md)
     * [MSDS➞regulatoryInformation](MSDS_regulatoryInformation.md) - Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.
 * [relatedDOI](relatedDOI.md)
     * [ProductOrService➞relatedDOI](ProductOrService_relatedDOI.md) - Any DOI that can be related
     * [Publication➞relatedDOI](Publication_relatedDOI.md) - Any Digital Object Identifier that can be related
 * [relatedPDB](relatedPDB.md)
     * [Protein➞relatedPDB](Protein_relatedPDB.md) - Identifier for 3D structural data as per the PDB (Protein Data Bank) database
 * [resourceURL](resourceURL.md)
     * [Certification➞resourceURL](Certification_resourceURL.md) - The web address or location where the details or content is stored and can be accessed or downloaded.
     * [License➞resourceURL](License_resourceURL.md) - The web address or location where the details or content is stored and can be accessed or downloaded.
 * [riskGroup](riskGroup.md)
     * [ProductOrService➞riskGroup](ProductOrService_riskGroup.md) - The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
 * [sequence](sequence.md)
     * [Nucleic Acid➞sequence](Nucleic_Acid_sequence.md) - The related sequence information from a sequence provider or in fasta format
     * [Pathogen➞sequence](Pathogen_sequence.md) - The related sequence information from a sequence provider or in fasta format
     * [Protein➞sequence](Protein_sequence.md) - The related sequence information from a sequence provider or in fasta format
     * [RecombinantPartIdentification➞sequence](RecombinantPartIdentification_sequence.md) - The related sequence information from a sequence provider or in fasta format
 * [sequenceChecked](sequenceChecked.md)
     * [Nucleic Acid➞sequenceChecked](Nucleic_Acid_sequenceChecked.md) - Tell whether or not the sequence of the product was controlled (compulsory for cloned products)
 * [sequenceFASTA](sequenceFASTA.md)
     * [Sequence➞sequenceFASTA](Sequence_sequenceFASTA.md) - In case no sequence reference exists in public repositories, the corresponding FASTA sequence is required
 * [sequenceProvider](sequenceProvider.md)
     * [SequenceReference➞sequenceProvider](SequenceReference_sequenceProvider.md) - The name of the sequence provider within the list of accepted sequence providers
 * [sequenceReference](sequenceReference.md)
     * [Antibody➞sequenceReference](Antibody_sequenceReference.md) - A reference that permits to retreive the sequence information from a sequence provider
     * [Sequence➞sequenceReference](Sequence_sequenceReference.md) - A reference that permits to retrieve the sequence information from a sequence provider
 * [sequencing](sequencing.md)
     * [Nucleic Acid➞sequencing](Nucleic_Acid_sequencing.md) - Refers to the level of sequencing performed on the nucleic acid. Possible values include "Not sequenced" (no sequencing has been performed), "Partly sequenced" (only a portion of the nucleic acid sequence has been determined), and "Fully sequenced" (the entire nucleic acid sequence has been determined).
     * [Pathogen➞sequencing](Pathogen_sequencing.md) - The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
 * [serotype](serotype.md)
     * [PathogenIdentification➞serotype](PathogenIdentification_serotype.md) - Genetically related pathogens that group together based on serological relationships
 * [shippingConditions](shippingConditions.md)
     * [Product➞shippingConditions](Product_shippingConditions.md) - Specification of the terms and parameters for transporting
 * [sourceOfInformation](sourceOfInformation.md)
     * [AlternateName➞sourceOfInformation](AlternateName_sourceOfInformation.md) - The name of the origin from which knowledge is obtained. This can include any entity that provides information
     * [CommonName➞sourceOfInformation](CommonName_sourceOfInformation.md) - The name of the origin from which knowledge is obtained. This can include any entity that provides information
 * [specialFeature](specialFeature.md)
     * [Protein➞specialFeature](Protein_specialFeature.md) - Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
 * [specificity](specificity.md)
     * [Detection Kit➞specificity](Detection_Kit_specificity.md) - Details on the ability of a detection kit to correctly identify negative results, distinguishing between the target analyte and other substances without cross-reacting
 * [specificityDocumented](specificityDocumented.md)
     * [Antibody➞specificityDocumented](Antibody_specificityDocumented.md) - Tell if the antibody specificity was documented
     * [Detection Kit➞specificityDocumented](Detection_Kit_specificityDocumented.md) - Boolean value indicating whether the specificity of the detection kit has been formally documented.
 * [stabilityAndReactivity](stabilityAndReactivity.md)
     * [MSDS➞stabilityAndReactivity](MSDS_stabilityAndReactivity.md) - Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.
 * [storageConditions](storageConditions.md)
     * [Product➞storageConditions](Product_storageConditions.md) - Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
 * [strain](strain.md)
     * [PathogenIdentification➞strain](PathogenIdentification_strain.md) - Identifier given to a genetic variant within a single species
 * [streetAddress](streetAddress.md)
     * [ContactPoint➞streetAddress](ContactPoint_streetAddress.md) - The building/apartment number and the street name
 * [subspecies](subspecies.md)
     * [PathogenIdentification➞subspecies](PathogenIdentification_subspecies.md) - The subspecies information differentiates closely related pathogens within a single species
 * [suspectedEpidemiologicalOrigin](suspectedEpidemiologicalOrigin.md)
     * [Pathogen➞suspectedEpidemiologicalOrigin](Pathogen_suspectedEpidemiologicalOrigin.md) - The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
 * [targetedAntigen](targetedAntigen.md)
     * [Antibody➞targetedAntigen](Antibody_targetedAntigen.md) - Specific molecular structure or epitope recognized and bound by an antibody
 * [targetedRegion](targetedRegion.md)
     * [Detection Kit➞targetedRegion](Detection_Kit_targetedRegion.md) - The specific area or sequence within the target analyte that the detection kit is designed to identify and interact with, ensuring accurate detection and analysis.
 * [taxon](taxon.md)
     * [PathogenIdentification➞taxon](PathogenIdentification_taxon.md) - Scientifically classified group or entity within the reference taxonomy
     * [Taxonomy➞taxon](Taxonomy_taxon.md) - Scientifically classified group or entity within the reference taxonomy
 * [taxonDataProvider](taxonDataProvider.md)
     * [Taxonomy➞taxonDataProvider](Taxonomy_taxonDataProvider.md) - The data provider for the taxons of the taxonomy
 * [taxonomicID](taxonomicID.md)
     * [Taxon➞taxonomicID](Taxon_taxonomicID.md) - The taxonomic identifier as a persistent identifier accross releases
 * [taxonomicNodeID](taxonomicNodeID.md)
     * [Taxon➞taxonomicNodeID](Taxon_taxonomicNodeID.md) - The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy
 * [taxonomy](taxonomy.md)
     * [Taxon➞taxonomy](Taxon_taxonomy.md) - The taxonomy release(s) in which this entity exists
     * [TaxonomicRank➞taxonomy](TaxonomicRank_taxonomy.md) - The taxonomy release(s) in which this entity exists
 * [technicalRecommendation](technicalRecommendation.md)
     * [ProductOrService➞technicalRecommendation](ProductOrService_technicalRecommendation.md) - Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
 * [telephone](telephone.md)
     * [ContactPoint➞telephone](ContactPoint_telephone.md) - The telephone number
 * [term](term.md)
     * [Vocabulary➞term](Vocabulary_term.md) - The terms related to this vocabulary
 * [termDataProvider](termDataProvider.md)
     * [Vocabulary➞termDataProvider](Vocabulary_termDataProvider.md) - An external API or Endpoint that permits to retrieve the terms of this vocabulary
 * [theTAGStatusOfTheSolubilizedProtein](theTAGStatusOfTheSolubilizedProtein.md)
     * [Protein➞theTAGStatusOfTheSolubilizedProtein](Protein_theTAGStatusOfTheSolubilizedProtein.md) - Indicates the presence and condition of a tag on the protein after solubilization. Possible values include "Uncleaved Tag" (the tag is still attached to the protein), "Cleaved Tag" (the tag has been removed from the protein), and "No Tag" (the protein does not have a tag)
 * [thirdPartyDistributionConsent](thirdPartyDistributionConsent.md)
     * [Product➞thirdPartyDistributionConsent](Product_thirdPartyDistributionConsent.md) - Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
 * [titer](titer.md)
     * [Nucleic Acid➞titer](Nucleic_Acid_titer.md) - The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
     * [Pathogen➞titer](Pathogen_titer.md) - The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
 * [title](title.md)
     * [Publication➞title](Publication_title.md) - The descriptive word or phrase that identifies the current piece of work
 * [toxicologicalInformation](toxicologicalInformation.md)
     * [MSDS➞toxicologicalInformation](MSDS_toxicologicalInformation.md) - Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure
 * [transmissionMethod](transmissionMethod.md)
     * [Pathogen➞transmissionMethod](Pathogen_transmissionMethod.md) - The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
 * [transportInformation](transportInformation.md)
     * [MSDS➞transportInformation](MSDS_transportInformation.md) - Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.
 * [typeOfFunctionalCharacterization](typeOfFunctionalCharacterization.md)
     * [Protein➞typeOfFunctionalCharacterization](Protein_typeOfFunctionalCharacterization.md) - Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include "Enzymatic" (the protein has been characterized for its enzyme activity) and "Antigenic" (the protein has been characterized for its ability to elicit an immune response).
 * [unitCost](unitCost.md)
     * [ProductOrService➞unitCost](ProductOrService_unitCost.md) - The cost per access for one unit as defined by the unit definition
 * [unitDefinition](unitDefinition.md)
     * [ProductOrService➞unitDefinition](ProductOrService_unitDefinition.md) - A short description of what will be delivered by ordering one unit of this item
 * [usageRestrictions](usageRestrictions.md)
     * [Product➞usageRestrictions](Product_usageRestrictions.md) - Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
 * [variant](variant.md)
     * [PathogenIdentification➞variant](PathogenIdentification_variant.md) - An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
 * [version](version.md)
     * [Taxonomy➞version](Taxonomy_version.md) - The version of this instance of entity
 * [versionDataProvider](versionDataProvider.md)
     * [Taxonomy➞versionDataProvider](Taxonomy_versionDataProvider.md) - The data provider for the Version ID of this taxonomy
 * [versionOf](versionOf.md)
     * [Version➞versionOf](Version_versionOf.md) - Identifier of what the version qualifies
 * [weight](weight.md)
     * [DataProvider➞weight](DataProvider_weight.md) - A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
     * [Term➞weight](Term_weight.md) - A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0

### Enums


### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
