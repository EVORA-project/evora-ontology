# European Viral Outbreak Response Alliance Ontology

The EVORAO Ontology provides a structured and harmonized vocabulary for describing shareable pathogens as characterized biological materials, along with their derived products and associated services, organized into collections. Developed within the EVORA project, it supports consistent metadata annotation across research infrastructures, promoting findability, accessibility, interoperability, and reusability (FAIR). By aligning with relevant standards and ontologies, EVORAO facilitates cross-domain collaboration, integration, and sharing of pathogenic resources and services to enhance pandemic preparedness and response. While initially focused on virology, EVORAO is designed to be extensible and also supports metadata harmonization for other pathogens. EVORAO is compatible with DCAT, making it well-suited for efficiently cataloguing pathogen collections and related resources.

URI: https://w3id.org/evorao/

Name: EVORAO



## Classes

| Class | Description |
| --- | --- |
| [Resource](Resource.md) | Resource published or curated by a single agent. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalPartOrigin](BiologicalPartOrigin.md) | Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SyntheticPartOrigin](SyntheticPartOrigin.md) | Information on the origin of a synthetic part that composes the biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Certification](Certification.md) | Assurance given by an independent certification body that a product, service or system meets the requirements of a standard. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContactPoint](ContactPoint.md) | Entity serving as focal point of information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataService](DataService.md) | A collection of operations that provides access to one or more datasets or data processing functions. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | A collection of data, published or curated by a single agent, and available for access. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Catalogue](Catalogue.md) | A curated collection of metadata about resources. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Collection](Collection.md) | Set of products and services with some common characteristics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Taxonomy](Taxonomy.md) | A structured representation of data about the classification and naming of biological organisms into groups according to shared characteristics. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or intangible (a service). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, or ownership transfer. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single offering, typically to provide added value, convenience, or specific experimental utility. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DetectionKit](DetectionKit.md) | A detection kit for specific pathogens. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen. It can be extracted or synthetic. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bacterium](Bacterium.md) | The bacterium as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fungus](Fungus.md) | The fungus as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prion](Prion.md) | The prion as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protozoan](Protozoan.md) | The protozoan as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Viroid](Viroid.md) | The viroid as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virus](Virus.md) | The virus as a biological material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protein](Protein.md) | A protein as a derived product from a pathogen. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Service](Service.md) | An intangible offering characterized by an activity, performance, or facilitation carried out by a provider to fulfill a user’s need. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve an item from an external provider. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[File](File.md) | Digital document or record stored in a specific format that contains data or information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Document](Document.md) | Subclass of File representing textual or written files such as reports, manuals, or forms. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or illustrations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presentations, or movies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FundingSource](FundingSource.md) | A program, grant, or project providing financial support for the access or use of a product or service, either fully or partially. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](License.md) | The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSafetyDataSheet](MaterialSafetyDataSheet.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation of a pathogen from another. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PersonOrOrganization](PersonOrOrganization.md) | A person or an organization. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.md) | A social entity established to meet needs or pursue specific goals. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Provider](Provider.md) | A provider of products or services, as a specific organization. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Originator](Originator.md) | The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | An individual. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.md) | A scientific publication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RecombinantPartIdentification](RecombinantPartIdentification.md) | Identification of a recombinant part. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sequence](Sequence.md) | A nucleic acid or protein sequence information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceReference](SequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence provider. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Term](Term.md) | Word or phrase from a specialized area of knowledge. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AlternateName](AlternateName.md) | List of other names for things. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiosafetyLevel](BiosafetyLevel.md) | The level of biocontainment required or applied in the facility where the biological agent is manipulated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalGroup](ClinicalGroup.md) | A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to something like an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific or technical name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Country](Country.md) | The country as of ISO3166. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Doi](Doi.md) | A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is naturally found. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IplcOrigin](IplcOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical item originates. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IataClassification](IataClassification.md) | The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Journal](Journal.md) | Periodical journal publishing scientific research. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Keyword](Keyword.md) | A term or phrase used to tag and categorize content. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PdbReference](PdbReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics or functions, which helps in their organization. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditions. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TagSequence](TagSequence.md) | The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Version](Version.md) | Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards). |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | Concise summary of the publication |
| [accessionNumber](accessionNumber.md) | The sequence ID that permits to retrieve the sequence information from the se... |
| [accessPointUrl](accessPointUrl.md) | The URL that permits to access to the product/service detailed description pa... |
| [accessToPhysicalGeneticResource](accessToPhysicalGeneticResource.md) | Indicate if the biological part was produced with access to a physical geneti... |
| [accidentalReleaseMeasures](accidentalReleaseMeasures.md) | Guidelines for safely managing spills or leaks of the product, including cont... |
| [additionalCategory](additionalCategory.md) | Any category apart from its main category in which this product or service ca... |
| [addressCountry](addressCountry.md) | The country as of  ISO 3166 |
| [addressLocality](addressLocality.md) | The locality in which the street address is, and which is in the region |
| [addressRegion](addressRegion.md) | The region in which the locality is, and which is in the country |
| [alpha2Code](alpha2Code.md) | Two-letter country codes from ISO 3166-1 alpha-2 |
| [alternateName](alternateName.md) | Any other name under which the entity can be known |
| [altText](altText.md) | An alternate text for the image, if the image cannot be displayed |
| [antibodyPurifiedByAffinity](antibodyPurifiedByAffinity.md) | Indicates whether or not if the antibody was purified by affinity |
| [authors](authors.md) | The list of authors |
| [availability](availability.md) | The state or condition in which this item is accessible and ready for use or ... |
| [beforeDate](beforeDate.md) | Set to TRUE if a proxy date for the collection date is used |
| [biologicalMaterialOrigin](biologicalMaterialOrigin.md) | Information about the origin of the biological material, essential for access... |
| [biologicalPartOrigin](biologicalPartOrigin.md) | Details the origin of one or more unitary parts that make up the biological m... |
| [biologicalSourceType](biologicalSourceType.md) | Defines if the current biological material is natural and was collected or if... |
| [biosafetyLevel](biosafetyLevel.md) | The level of biocontainment required or applied in the facility where the bio... |
| [biosafetyRestrictions](biosafetyRestrictions.md) | Information about guidelines and regulations designed to prevent the exposure... |
| [canBeUsedToProduceGmo](canBeUsedToProduceGmo.md) | Indicates if the current service or product can be used to produce GMO |
| [category](category.md) | The main category of the service or product |
| [certification](certification.md) | Any certification related to the current product or service; e |
| [certificationDocument](certificationDocument.md) | The document(s) issued by an authority certifying the conformity of the subje... |
| [clinicalInformation](clinicalInformation.md) | Details about the clinical aspects of the pathogen, including symptoms, sever... |
| [clonedIntoPlasmid](clonedIntoPlasmid.md) | The plasmid into which the nucleic acid has been cloned |
| [clonedNucleicAcid](clonedNucleicAcid.md) | Specification of the terms and parameters for transporting |
| [coInfectingViruses](coInfectingViruses.md) | Identifies other viruses that may co-infect the host organism along with the ... |
| [collection](collection.md) | The collection(s) to which belongs this item |
| [collectionDataProvider](collectionDataProvider.md) | The provider of the data of the collection |
| [collectionDate](collectionDate.md) | The date when the sample was collected in situ |
| [collectionItem](collectionItem.md) | An item of the collection |
| [complementaryDocument](complementaryDocument.md) | Any additional documents that provide supplementary information, instructions... |
| [contactPoint](contactPoint.md) | An information that allows someone to establish communication |
| [contaminationWithCoInfectingViruses](contaminationWithCoInfectingViruses.md) | A boolean value indicating whether there is contamination with co-infecting v... |
| [contentType](contentType.md) | The content type of the response to queries |
| [contentUrl](contentUrl.md) | The web address or location where the file content is stored and can be acces... |
| [country](country.md) | The country of the organization |
| [countryOfCollection](countryOfCollection.md) | The geographical location where the sample was collected in situ |
| [cultivability](cultivability.md) | The ability of the pathogen to be cultivated or grown in laboratory condition... |
| [dateIssued](dateIssued.md) | Date of formal issuance (e |
| [dateModified](dateModified.md) | Most recent date on which the resource was changed, updated or modified |
| [description](description.md) | A short explanation of the characteristics, features, or nature of the curren... |
| [descriptionOfModificationsMadeFromTheReferenceSequences](descriptionOfModificationsMadeFromTheReferenceSequences.md) | List the modifications mades from the reference sequence if any |
| [disposalConsiderations](disposalConsiderations.md) | Guidance on the safe and environmentally responsible disposal of the product,... |
| [doi](doi.md) | A Digital Object Identifier (DOI) that can be related |
| [domain](domain.md) | A distinct structural and functional unit within the protein, often capable o... |
| [ecologicalInformation](ecologicalInformation.md) | Details the potential environmental impact of the product, including its effe... |
| [eligibilityCriteria](eligibilityCriteria.md) | Conditions under which individuals or organisations may benefit from the fina... |
| [email](email.md) | The email address |
| [endpointUrl](endpointUrl.md) | The URL template that allows to get the content |
| [exposureControlsPersonalProtection](exposureControlsPersonalProtection.md) | Specifies measures to limit exposure to the product, including recommended en... |
| [expressedAs](expressedAs.md) | Refers to the form in which the protein is produced and manifested in a biolo... |
| [expressionSystem](expressionSystem.md) | The host organism or cellular environment used to produce a protein from a sp... |
| [externalEquivalentTaxon](externalEquivalentTaxon.md) | Any equivalent taxon in a different taxonomy if exists/known to serve as a br... |
| [externalRelatedReference](externalRelatedReference.md) | A reference that permits to retrieve another related item from an external pr... |
| [fireFightingMeasures](fireFightingMeasures.md) | Guidance on how to safely extinguish a fire involving the product, including ... |
| [firstAidMeasures](firstAidMeasures.md) | Instructions on immediate actions to take in case of exposure to the product,... |
| [format](format.md) | The file type or format that indicates how the data within the file is struct... |
| [functionalAndTechnicalDescription](functionalAndTechnicalDescription.md) | Detailed information about the specific biological functions, mechanisms of a... |
| [functionalCharacterization](functionalCharacterization.md) | The process of determining and describing the specific biological activities ... |
| [funder](funder.md) | The organization providing the financial support |
| [fundingPeriodEnd](fundingPeriodEnd.md) | The date on which the financial mechanism ceases to apply to the supported pr... |
| [fundingPeriodStart](fundingPeriodStart.md) | The date from which the financial mechanism is active or applicable to the su... |
| [fundingProgram](fundingProgram.md) | Identifies the overarching financial framework, research initiative, or suppo... |
| [fundingSource](fundingSource.md) | A program, grant, or project providing financial support for the access or us... |
| [furtherInformation](furtherInformation.md) | Provides any additional details or clarifications not covered in other sectio... |
| [genBankFileOfTheConstruct](genBankFileOfTheConstruct.md) | A GenBank formatted file that contains detailed sequence and annotation infor... |
| [genomeSequencing](genomeSequencing.md) | The extent of the pathogen's genetic material that has been sequenced, with p... |
| [genotype](genotype.md) | Genotype information that identifies organisms that cluster in phylogenetic t... |
| [grantNumber](grantNumber.md) | A formal reference or agreement number assigned by the funding body |
| [handlingAndStorage](handlingAndStorage.md) | Instructions on the safe handling practices and storage conditions for the pr... |
| [hazardsIdentification](hazardsIdentification.md) | Outlines the potential risks and dangers associated with handling the product... |
| [homePage](homePage.md) | A web page that serves as the main or introductory page |
| [hostType](hostType.md) | Indication of the possible host(s) for the identified pathogens among the lis... |
| [hybridomaDescription](hybridomaDescription.md) | The description of the hybridoma |
| [iataClassification](iataClassification.md) | The corresponding International Air Transport Association (IATA)'s category f... |
| [identificationTechnique](identificationTechnique.md) | A method or procedure used to detect, identify, and confirm the presence of a... |
| [identifier](identifier.md) | A unique identifier of the resource being described or cataloged |
| [inclusionBodiesType](inclusionBodiesType.md) | Refers to the state of aggregated proteins within a cell |
| [indigenousPeopleAndLocalCommunityOrigin](indigenousPeopleAndLocalCommunityOrigin.md) | The specific IPLC area (Indigenous People and Local Communities) from which t... |
| [infectivity](infectivity.md) | Indicates the ability of the pathogen to establish an infection in a host org... |
| [infectivityTest](infectivityTest.md) | The description of the completed infectivity test, providing details on the m... |
| [internalReference](internalReference.md) | Any reference or indication to be used for local retrieval purpose |
| [inVocabulary](inVocabulary.md) | Terms belong to a specific vocabulary |
| [iri](iri.md) | International Resource Identifier (IRI) that uniquely identifies or refers to... |
| [isolate](isolate.md) | Identifier given to a pathogen that has been isolated from an infected host a... |
| [isolationConditions](isolationConditions.md) | The environmental and procedural conditions under which the pathogen was isol... |
| [isolationHost](isolationHost.md) | The host organism from which the pathogen was originally isolated |
| [isolationTechnique](isolationTechnique.md) | The specific method or procedure used to isolate the pathogen from a host org... |
| [itemsOfTheBundle](itemsOfTheBundle.md) | Specifies the constituent products and/or services that are part of the bundl... |
| [journal](journal.md) | The scientific journal in which the publication was published |
| [keyword](keyword.md) | A keyword or tag describing the resource |
| [keywords](keywords.md) | List of terms used to tag and categorize this Item |
| [letterOfAuthority](letterOfAuthority.md) | Indicate whether a Letter of Authority is required, confirming the necessity ... |
| [license](license.md) | Information about terms and conditions under which the subject can be used, s... |
| [licensingOrAttribution](licensingOrAttribution.md) | A text or html code that provides any related data sharing licence and/or att... |
| [loginRequestMethod](loginRequestMethod.md) | The http request method used to acces the login request url |
| [loginTokenName](loginTokenName.md) | The name of the token, unique identifier of an interaction session, that will... |
| [loginUrl](loginUrl.md) | The URL template that allows to log in if required |
| [logo](logo.md) | A path or URL to the related logo |
| [materialSafetyContact](materialSafetyContact.md) | The designated contact point responsible for providing information related to... |
| [materialSafetyDataSheet](materialSafetyDataSheet.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardi... |
| [memberOfRi](memberOfRi.md) | The research infrastructure of which this organization is a member |
| [modelSpecies](modelSpecies.md) | The species of the infected organism in the experiment |
| [modelType](modelType.md) | The specific name of the infected organism, including its modification if nec... |
| [modificationsFromTheReferenceSequences](modificationsFromTheReferenceSequences.md) | Set to TRUE if there was is any modification made from the reference sequence |
| [mutationObserved](mutationObserved.md) | Indicates if the current nucleic acid has No mutation compared to the referen... |
| [mycoplasmicContent](mycoplasmicContent.md) | Indicates the presence of mycoplasma contamination within the sample |
| [name](name.md) | A word or set of words used to identify and refer to an entity |
| [note](note.md) | An aditional information as a textual comment |
| [observedMutations](observedMutations.md) | The specific mutations that have been identified and documented in the nuclei... |
| [orcidId](orcidId.md) | Unique persistent identifier for a person, provided by the Open Researcher an... |
| [originator](originator.md) | The individual or organization responsible for the original discovery, isolat... |
| [parentCategory](parentCategory.md) | An overarching category that encompasses the current category within a hierar... |
| [parentTaxon](parentTaxon.md) | The parent taxon of the current taxon |
| [partIdentification](partIdentification.md) | A short designation of this recombinant part of the related biological materi... |
| [passage](passage.md) | The number of times the pathogen was cultured through serial passage, a proce... |
| [pathogenIdentification](pathogenIdentification.md) | The identification of the pathogen or group of pathogens (e |
| [pathogenName](pathogenName.md) | A pathogen common name or a name that describes a group of pathogens |
| [pathogenType](pathogenType.md) | Identification of the specific type of pathogen among the listed categories e |
| [permitIdentifierForAbs](permitIdentifierForAbs.md) | Reference of the permit identifiers for access to the genetic resource, appli... |
| [physicalChemicalProperties](physicalChemicalProperties.md) | Key characteristics of the product, such as physical state, appearance, solub... |
| [plasmidSelection](plasmidSelection.md) | Specific selectable markers in the plasmid, such as antibiotic resistance gen... |
| [postalCode](postalCode.md) | The postal code |
| [preparationTechnique](preparationTechnique.md) | The technique, method, or procedure employed to obtain or prepare the materia... |
| [previouslyKnownAs](previouslyKnownAs.md) | Any historic version of this taxon having a different name |
| [productionCellLine](productionCellLine.md) | The cell line used for the production or propagation of the pathogen, detaili... |
| [productionSystem](productionSystem.md) | The biological and technological methods and processes used to produce the an... |
| [productPicture](productPicture.md) | A picture that can represent the item |
| [propagationHost](propagationHost.md) | The host organism that propagates the pathogen |
| [proteinPurification](proteinPurification.md) | Refers to the degree of purity achieved for a protein sample |
| [providedEntityType](providedEntityType.md) | Identifies the type of entity (ontology class) described by the response to a... |
| [provider](provider.md) | A provider of this product or service, as a specific organization |
| [qualityGrading](qualityGrading.md) | Information that permits to assess the quality level of what will be provided |
| [queryMethod](queryMethod.md) | The http request method used to access the requested query url |
| [rank](rank.md) | Relative level or position of the identified taxon in the taxonomy |
| [rankDataProvider](rankDataProvider.md) | The data provider for the description of the taxonomic ranks used in this tax... |
| [recombinantMaterial](recombinantMaterial.md) | Indicates if this biological material is a recombinant biological material |
| [recombinantPartIdentification](recombinantPartIdentification.md) | Identification of a recombinant part |
| [reference](reference.md) | The identifier reference of the connected external item |
| [referenceLabel](referenceLabel.md) | The label informing what this reference is about |
| [referenceProviderName](referenceProviderName.md) | The name for the reference provider |
| [referenceProviderPrefix](referenceProviderPrefix.md) | The url prefix that once completed with the reference will lead to the linked... |
| [refSku](refSku.md) | The reference or the stock keeping unit of the service or item provided in th... |
| [regionEncompassedInThisProduct](regionEncompassedInThisProduct.md) | The specific region encompassed in the product |
| [regulatoryInformation](regulatoryInformation.md) | Lists applicable laws, regulations, and standards governing the product, incl... |
| [relatedPdb](relatedPdb.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |
| [resource](resource.md) | Resource published or curated by a single agent |
| [resourceUrl](resourceUrl.md) | The web address or location where the details or content is stored and can be... |
| [riskGroup](riskGroup.md) | The highest risk group related to this resource |
| [rorId](rorId.md) | The corresponding organization's persistent identifier from the Research Orga... |
| [sequence](sequence.md) | The related sequence information from a sequence provider or in fasta format |
| [sequenceChecked](sequenceChecked.md) | Tell whether or not the sequence of the product was controlled (compulsory fo... |
| [sequenceFasta](sequenceFasta.md) | Textual encoding of a biological sequence information in FASTA format |
| [sequenceProvider](sequenceProvider.md) | The name of the sequence provider within the list of accepted sequence provid... |
| [sequenceReference](sequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence... |
| [sequencing](sequencing.md) | Refers to the level of sequencing performed on the nucleic acid |
| [serotype](serotype.md) | Genetically related pathogens that group together based on serological relati... |
| [servesDataset](servesDataset.md) | A collection of data that this data service can distribute |
| [shippingConditions](shippingConditions.md) | Specification of the terms and parameters for transporting |
| [sourceOfInformation](sourceOfInformation.md) | The name of the origin from which knowledge is obtained |
| [specialFeature](specialFeature.md) | Distinctive attributes of a product that set it apart from other similar item... |
| [specificity](specificity.md) | Details on the ability of a detection kit to correctly identify negative resu... |
| [specificityDocumented](specificityDocumented.md) | Boolean value indicating whether the specificity of the product has been form... |
| [stabilityAndReactivity](stabilityAndReactivity.md) | Describes the product’s stability under normal conditions and its potential t... |
| [standardOperatingProcedureFile](standardOperatingProcedureFile.md) | The related standard operating procedure file (SOP) |
| [storageConditions](storageConditions.md) | Specifies the conditions under which the product has to be stored to maintain... |
| [strain](strain.md) | Identifier given to a genetic variant within a single species |
| [streetAddress](streetAddress.md) | The building/apartment number and the street name |
| [subspecies](subspecies.md) | The subspecies information differentiates closely related pathogens within a ... |
| [suspectedEpidemiologicalOrigin](suspectedEpidemiologicalOrigin.md) | The potential geographical or environmental source from which the pathogen is... |
| [tagSequence](tagSequence.md) | The name of the DNA coding sequence or corresponding peptide/protein sequence... |
| [tagStatusOfTheSolubilizedProtein](tagStatusOfTheSolubilizedProtein.md) | Indicates the presence and condition of a tag on the protein after solubiliza... |
| [targetedAntigen](targetedAntigen.md) | Specific molecular structure or epitope recognized and bound by an antibody |
| [targetedRegion](targetedRegion.md) | The specific area or sequence within the target analyte that the detection ki... |
| [taxon](taxon.md) | Scientifically classified group or entity within the reference taxonomy |
| [taxonDataProvider](taxonDataProvider.md) | The data provider for the taxons of the taxonomy |
| [taxonomicId](taxonomicId.md) | The taxonomic identifier as a persistent identifier accross releases |
| [taxonomicNodeId](taxonomicNodeId.md) | The taxonomic_Node Identifier as an identifier specific the current taxon in ... |
| [taxonomy](taxonomy.md) | The taxonomy release(s) in which this entity exists |
| [technicalRecommendation](technicalRecommendation.md) | Expert advice or guidelines provided to ensure the optimal use, performance, ... |
| [telephone](telephone.md) | The telephone number |
| [term](term.md) | The terms related to this vocabulary |
| [termDataProvider](termDataProvider.md) | An external API or Endpoint that permits to retrieve the terms of this vocabu... |
| [thirdPartyDistributionConsent](thirdPartyDistributionConsent.md) | Indicates whether the biological material can be distributed without restrict... |
| [titer](titer.md) | The titer value, its corresponding unit, and the method of quantification (e |
| [title](title.md) | A name given to the resource |
| [toxicologicalInformation](toxicologicalInformation.md) | Details on the potential health effects of the product, including routes of e... |
| [transmissionMethod](transmissionMethod.md) | The method or route through which the pathogen is transmitted from one host t... |
| [transportInformation](transportInformation.md) | Details the regulations and guidelines for safely transporting the product, i... |
| [typeOfFunctionalCharacterization](typeOfFunctionalCharacterization.md) | Refers to the classification of a protein based on the specific type of funct... |
| [unitCost](unitCost.md) | The cost per access for one unit as defined by the unit definition |
| [unitCostCurrency](unitCostCurrency.md) | The currency in which the unit cost is expressed, following ISO 4217 three-le... |
| [unitCostNote](unitCostNote.md) | A free-text note describing special conditions or cases where the cost cannot... |
| [unitDefinition](unitDefinition.md) | A short description of what will be delivered by ordering one unit of this it... |
| [usageRestrictions](usageRestrictions.md) | Specifies any limitations or conditions on the use of the biological material... |
| [variant](variant.md) | An organism with one or more new mutations is referred to as a “variant” of t... |
| [version](version.md) | The version indicator (name or identifier) of a resource |
| [versionDataProvider](versionDataProvider.md) | The data provider for the Version ID of this taxonomy |
| [versionOf](versionOf.md) | Identifier of what type of entities the version qualifies |
| [weight](weight.md) | A numerical value indicating relative importance or priority, generally proce... |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
