-- # Class: "Version" Description: "Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)"
--     * Slot: id Description: 
--     * Slot: ID Description: The version identifier
--     * Slot: versionOf Description: Identifier of what the version qualifies
-- # Class: "Nameable" Description: "Any entity that has a name and can have a textual description"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
-- # Class: "Catalogue" Description: "A curated collection of metadata about resources"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
-- # Class: "Dataset" Description: "A collection of data, published or curated by a single agent, and available for access"
--     * Slot: id Description: 
-- # Class: "NamedDataset" Description: "A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
-- # Class: "DataService" Description: "A collection of operations that provides access to one or more datasets or data processing functions"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
-- # Class: "Taxonomy" Description: "Science of naming, defining and classifying organisms"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: taxonDataProvider_id Description: The data provider for the taxons of the taxonomy
--     * Slot: version_id Description: The version of this instance of entity
--     * Slot: versionDataProvider_id Description: The data provider for the Version ID of this taxonomy
--     * Slot: rankDataProvider_id Description: The data provider for the description of the taxonomic ranks used in this taxonomy
-- # Class: "DataProvider" Description: "An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources"
--     * Slot: id Description: 
--     * Slot: loginRequestMethod Description: The http request method used to acces the login request url
--     * Slot: loginURL Description: The URL template that allows to log in if required
--     * Slot: loginTokenName Description: The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query
--     * Slot: queryURL Description: The URL template that allows to get the content
--     * Slot: queryMethod Description: The http request method used to access the requested query url
--     * Slot: contentType Description: The content type of the response to the queries
--     * Slot: providedEntityType Description: The identification of the entity type (Class) described by the response to the query
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
-- # Class: "PathogenIdentification" Description: "A collection of distinguishing information that enables the differentiation of a pathogen from another"
--     * Slot: id Description: 
--     * Slot: pathogenType Description: Identification of the specific type of pathogen among the listed categories e.g. "Virus","Viroid","Bacterium"...
--     * Slot: subspecies Description: The subspecies information differentiates closely related pathogens within a single species
--     * Slot: strain Description: Identifier given to a genetic variant within a single species
--     * Slot: isolate Description: Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host
--     * Slot: genotype Description: Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes
--     * Slot: serotype Description: Genetically related pathogens that group together based on serological relationships
--     * Slot: taxon_id Description: Scientifically classified group or entity within the reference taxonomy
--     * Slot: pathogenName_id Description: A pathogen common name or a name that describes a group of pathogens
--     * Slot: variant_id Description: An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
-- # Class: "Publication" Description: "A scientific publication"
--     * Slot: id Description: 
--     * Slot: title Description: The descriptive word or phrase that identifies the current piece of work
--     * Slot: authors Description: The list of authors
--     * Slot: abstract Description: Concise summary of the publication
--     * Slot: relatedDOI_id Description: Any Digital Object Identifier that can be related
--     * Slot: journal_id Description: The scientific journal in which the publication was published
-- # Class: "Vocabulary" Description: "A subset of words or phrases specific to a particular subject or field"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: termDataProvider_id Description: An external API or Endpoint that permits to retrieve the terms of this vocabulary
-- # Class: "Term" Description: "Word or phrase from a specialized area of knowledge"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "CommonName" Description: "Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "VirusName" Description: "A virus vernacular name or a name that describes a group of viruses"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "AlternateName" Description: "List of alternate names for things"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "RiskGroup" Description: "Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "DOI" Description: "A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "Journal" Description: "Periodical journal publishing scientific research"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "PDBReference" Description: "Identifier for 3D structural data as per the PDB (Protein Data Bank) database"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "Keyword" Description: "A term or phrase used to tag and categorize content"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "ProteinTag" Description: "Peptide sequence genetically grafted onto a recombinant protein"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "SpecialFeature" Description: "Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ..."
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "ExpressionVector" Description: "A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "PlasmidSelection" Description: "The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "PropagationHost" Description: "The organism used to grow and multiply the pathogen under controlled conditions"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "TransmissionMethod" Description: "The process by which the pathogen spreads between hosts"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "ProductionCellLine" Description: "A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "ProductCategory" Description: "A term used to classify a group of products that share common characteristics or functions, which helps in their organization"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: parentCategory_id Description: An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "IsolationHost" Description: "Host organism from which the pathogen was isolated"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "GeographicalOrigin" Description: "The specific location or region where a physical item, originates or is naturally found"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "IPLCOrigin" Description: "The IPLC area (Indigenous People and Local Communities) from which a physical item originates"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "Country" Description: "The country as of ISO3166"
--     * Slot: id Description: 
--     * Slot: alpha2Code Description: Two-letter country codes from ISO 3166-1 alpha-2
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "IATAClassification" Description: "The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "Variant" Description: "An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "TaxonomicRank" Description: "The possible taxonomic ranks and their description"
--     * Slot: id Description: 
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "Taxon" Description: "Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit"
--     * Slot: id Description: 
--     * Slot: taxonomicID Description: The taxonomic identifier as a persistent identifier accross releases
--     * Slot: taxonomicNodeID Description: The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: parentTaxon_id Description: The parent taxon of the current taxon
--     * Slot: rank_id Description: Relative level or position of the identified taxon in the taxonomy
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary
-- # Class: "ExternalRelatedReference" Description: "A reference that permits to retrieve an item from an external provider"
--     * Slot: id Description: 
--     * Slot: reference Description: The identifier reference of the connected external item
--     * Slot: referenceLabel Description: The label informing what this reference is about
--     * Slot: referenceProviderPrefix Description: The url prefix that once completed with the reference will lead to the linked external resource
--     * Slot: referenceProviderName Description: The name for the reference provider
-- # Class: "Sequence" Description: "A nucleic acid or protein sequence information"
--     * Slot: id Description: 
--     * Slot: sequenceFASTA Description: In case no sequence reference exists in public repositories, the corresponding FASTA sequence is required
-- # Class: "SequenceReference" Description: "A reference that permits to retrieve the sequence information from a sequence provider"
--     * Slot: id Description: 
--     * Slot: accessionNumber Description: The sequence ID that permits to retrieve the sequence information from the sequence provider
--     * Slot: sequenceProvider Description: The name of the sequence provider within the list of accepted sequence providers
-- # Class: "PersonOrOrganization" Description: "A person or an organization"
--     * Slot: id Description: 
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Person" Description: "An individual"
--     * Slot: id Description: 
--     * Slot: oRCIDiD Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Organization" Description: "A social entity established to meet needs or pursue specific goals"
--     * Slot: id Description: 
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: alternateName_id Description: An alternate name or acronym
--     * Slot: country_id Description: The country of the organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "RI" Description: "A research infrastructure"
--     * Slot: id Description: 
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: alternateName_id Description: An alternate name or acronym
--     * Slot: country_id Description: The country of the organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Provider" Description: "A provider of products or services, as a specific organization"
--     * Slot: id Description: 
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: alternateName_id Description: An alternate name or acronym
--     * Slot: country_id Description: The country of the organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Originator" Description: "The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample"
--     * Slot: id Description: 
--     * Slot: homePage Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "BiologicalMaterialOrigin" Description: "Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol"
--     * Slot: id Description: 
--     * Slot: recombinantMaterial Description: Indicates if this biological material is a recombinant biological material.
--     * Slot: biologicalSourceType Description: Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!
-- # Class: "BiologicalPartOrigin" Description: "Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material"
--     * Slot: id Description: 
--     * Slot: accessToPhysicalGeneticResource Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part
-- # Class: "NaturalPartOrigin" Description: "Information on the origin of a natural part that composes the biological material"
--     * Slot: id Description: 
--     * Slot: collectionDate Description: The date when the sample was collected in situ. If unknown/private, use a proxy date such as "date received" and indicate this by setting to true the before date property
--     * Slot: beforeDate Description: Set to TRUE if a proxy date for the collection date is used
--     * Slot: permitIdentifierForABS Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
--     * Slot: accessToPhysicalGeneticResource Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
--     * Slot: countryOfCollection_id Description: The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to "country of origin".
--     * Slot: indigenousPoepleAndLocalCommunityOrigin_id Description: The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part
-- # Class: "SyntheticPartOrigin" Description: "Information on the origin of a synthetic part that composes the biological material"
--     * Slot: id Description: 
--     * Slot: modificationsFromTheReferenceSequences Description: Set to TRUE if there was is any modification made from the reference sequence
--     * Slot: descriptionOfModificationsMadeFromTheReferenceSequences Description: List the modifications mades from the reference sequence if any
--     * Slot: accessToPhysicalGeneticResource Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part
-- # Class: "RecombinantPartIdentification" Description: "Identification of a recombinant part"
--     * Slot: id Description: 
--     * Slot: partIdentification Description: A short designation of this recombinant part of the related biological material
-- # Class: "Collection" Description: "Set of products and services with some common characteristics"
--     * Slot: id Description: 
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: collectionDataProvider_id Description: The provider of the data of the collection
-- # Class: "ProductOrService" Description: "A product or a service"
--     * Slot: id Description: 
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Service" Description: "A service"
--     * Slot: id Description: 
--     * Slot: modelSpecies Description: The species of the infected organism in the experiment
--     * Slot: modelType Description: The specific name of the infected organism, including its modification if necessary
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Product" Description: "A product"
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Antibody" Description: "Protein that can bind to certain types of foreign bodies, such as pathogens"
--     * Slot: id Description: 
--     * Slot: productionSystem Description: The biological and technological methods and processes used to produce the antibody
--     * Slot: antibodyPurifiedByAffinity Description: Indicates whether or not if the antibody was purified by affinity
--     * Slot: specificityDocumented Description: Tell if the antibody specificity was documented
--     * Slot: targetedAntigen Description: Specific molecular structure or epitope recognized and bound by an antibody
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Hybridoma" Description: "An hybridoma that provides antibodies that can be related to a pathogen"
--     * Slot: id Description: 
--     * Slot: hybridomaDescription Description: The description of the hybridoma
--     * Slot: productionSystem Description: The biological and technological methods and processes used to produce the antibody
--     * Slot: antibodyPurifiedByAffinity Description: Indicates whether or not if the antibody was purified by affinity
--     * Slot: specificityDocumented Description: Tell if the antibody specificity was documented
--     * Slot: targetedAntigen Description: Specific molecular structure or epitope recognized and bound by an antibody
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Protein" Description: "A protein as a derived product from a pathogen"
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Nucleic Acid" Description: "Nucleic acid related to a pathogen. It can be extracted or synthetic"
--     * Slot: id Description: 
--     * Slot: isItAClonedNucleicAcid Description: Indicates that the nucleic acid sequence has been inserted into a plasmid vector for propagation or expression in a host organism
--     * Slot: regionEncompassedInThisProduct Description: The specific region encompassed in the product
--     * Slot: mutationObserved Description: Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it contains mutations (no frameshift, no unexpected STOP codon) if set to true
--     * Slot: observedMutations Description: The specific mutations that have been identified and documented in the nucleic acid sequence
--     * Slot: identificationTechnique Description: The method used to identify the nucleic acid sequence or its associated constructs, such as PCR, sequencing, or hybridization
--     * Slot: sequencing Description: Refers to the level of sequencing performed on the nucleic acid. Possible values include "Not sequenced" (no sequencing has been performed), "Partly sequenced" (only a portion of the nucleic acid sequence has been determined), and "Fully sequenced" (the entire nucleic acid sequence has been determined).
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: sequenceChecked Description: Tell whether or not the sequence of the product was controlled (compulsory for cloned products)
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
--     * Slot: clonedIntoPlasmid_id Description: The plasmid into which the nucleic acid has been cloned
--     * Slot: hasTAG_id Description: TAG sequence used for purposes such as purification, detection, or localization
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Detection Kit" Description: "A detection kit for specific pathogens"
--     * Slot: id Description: 
--     * Slot: specificityDocumented Description: Boolean value indicating whether the specificity of the detection kit has been formally documented.
--     * Slot: specificity Description: Details on the ability of a detection kit to correctly identify negative results, distinguishing between the target analyte and other substances without cross-reacting
--     * Slot: targetedRegion Description: The specific area or sequence within the target analyte that the detection kit is designed to identify and interact with, ensuring accurate detection and analysis.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Bundle" Description: "A group of products"
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Pathogen" Description: "Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Virus" Description: "The virus as a biological material"
--     * Slot: id Description: 
--     * Slot: contaminationWithCoInfectingViruses Description: A boolean value indicating whether there is contamination with co-infecting viruses
--     * Slot: mycoplasmicContent Description: Indicates the presence of mycoplasma contamination within the sample
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Bacterium" Description: "The bacterium as a biological material"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Fungus" Description: "The fungus as a biological material"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Protozoan" Description: "The protozoan as a biological material"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Viroid" Description: "The viroid as a biological material"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "Prion" Description: "The prion as a biological material"
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are " Cultivable pathogen", "Uncultivable pathogen" or "Inactivated pathogen"
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes
--     * Slot: identificationTechnique Description: The method or technique used to identify and confirm the presence of the pathogen, detailing the specific procedures and tools employed in the detection process
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are "N/A", "NOT Required", "Required for customers in the EU" or "Required"
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including "Complete genome" for the entire genome, "Complete coding sequence" for all coding regions, and "Partial sequence" for only a portion of the genetic material
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
--     * Slot: accessPointURL Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry
--     * Slot: refSKU Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service
--     * Slot: canItBeUsedToProduceGMO Description: Indicates if the current service or product can be used to produce GMO
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose
--     * Slot: note Description: An aditional information as a textual comment
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: hasIATAClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
--     * Slot: category_id Description: The main category of the service or product
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication
-- # Class: "MSDS" Description: "A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product"
--     * Slot: id Description: 
--     * Slot: physicalChemicalProperties Description: Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage
--     * Slot: hazardsIdentification Description: Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.
--     * Slot: firstAidMeasures Description: Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.
--     * Slot: fireFightingMeasures Description: Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.
--     * Slot: accidentalReleaseMeasures Description: Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.
--     * Slot: handlingAndStorage Description: Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.
--     * Slot: exposureControlsPersonalProtection Description: Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.
--     * Slot: stabilityAndReactivity Description: Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.
--     * Slot: toxicologicalInformation Description: Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure
--     * Slot: ecologicalInformation Description: Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.
--     * Slot: disposalConsiderations Description: Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.
--     * Slot: transportInformation Description: Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.
--     * Slot: regulatoryInformation Description: Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.
--     * Slot: furtherInformation Description: Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.
--     * Slot: msdsContact_id Description: The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.
-- # Class: "File" Description: "Digital document or record stored in a specific format that contains data or information"
--     * Slot: id Description: 
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Data" Description: "Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information"
--     * Slot: id Description: 
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Document" Description: "Subclass of File representing textual or written files such as reports, manuals, or forms"
--     * Slot: id Description: 
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Audio" Description: "Subclass of File representing sound recordings or audio tracks"
--     * Slot: id Description: 
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Video" Description: "Subclass of File representing moving visual media, such as recordings, presentations, or movies"
--     * Slot: id Description: 
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Image" Description: "Subclass of File representing visual content such as pictures, diagrams, or illustrations"
--     * Slot: id Description: 
--     * Slot: altText Description: An alternate text for the image, if the image cannot be displayed
--     * Slot: contentURL Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: license_id Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "ContactPoint" Description: "Entity serving as focal point of information"
--     * Slot: id Description: 
--     * Slot: email Description: Email address
--     * Slot: telephone Description: The telephone number
--     * Slot: streetAddress Description: The building/apartment number and the street name
--     * Slot: addressLocality Description: The locality in which the street address is, and which is in the region. e.g, the city
--     * Slot: addressRegion Description: The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division
--     * Slot: postalCode Description: The postal code
--     * Slot: oRCIDiD Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: addressCountry_id Description: The country as of  ISO 3166
-- # Class: "License" Description: "The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions"
--     * Slot: id Description: 
--     * Slot: resourceURL Description: The web address or location where the details or content is stored and can be accessed or downloaded.
--     * Slot: licensingOrAttribution Description: A text or html code that provides any related data sharing licence and/or attribution
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Certification" Description: "Assurance given by an independent certification body that a product, service or system meets the requirements of a standard"
--     * Slot: id Description: 
--     * Slot: resourceURL Description: The web address or location where the details or content is stored and can be accessed or downloaded.
--     * Slot: name Description: The label that allows humans to identify the current item
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item
--     * Slot: logo_id Description: A path or URL to the related logo
-- # Class: "Taxonomy_taxon" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: taxon_id Description: Scientifically classified group or entity within the reference taxonomy
-- # Class: "Taxonomy_rank" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: rank_id Description: Relative level or position of the identified taxon in the taxonomy
-- # Class: "PathogenIdentification_hostType" Description: ""
--     * Slot: PathogenIdentification_id Description: Autocreated FK slot
--     * Slot: hostType Description: Indication of the possible host(s) for the identified pathogens among the listed main categories
-- # Class: "Vocabulary_term" Description: ""
--     * Slot: Vocabulary_id Description: Autocreated FK slot
--     * Slot: term_id Description: The terms related to this vocabulary
-- # Class: "CommonName_alternateName" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any known alternate name related to this name
-- # Class: "CommonName_sourceOfInformation" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
-- # Class: "VirusName_alternateName" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any known alternate name related to this name
-- # Class: "VirusName_sourceOfInformation" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
-- # Class: "AlternateName_alternateName" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any known alternate name related to this name
-- # Class: "AlternateName_sourceOfInformation" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
-- # Class: "Variant_alternateName" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any known alternate name related to this name
-- # Class: "Variant_sourceOfInformation" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
-- # Class: "TaxonomicRank_taxonomy" Description: ""
--     * Slot: TaxonomicRank_id Description: Autocreated FK slot
--     * Slot: taxonomy_id Description: The taxonomy release(s) in which this entity exists
-- # Class: "Taxon_taxonomy" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: taxonomy_id Description: The taxonomy release(s) in which this entity exists
-- # Class: "Taxon_previouslyKnownAs" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: previouslyKnownAs_id Description: Any historic version of this taxon having a different name
-- # Class: "Taxon_externalEquivalentTaxon" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: externalEquivalentTaxon_id Description: Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)
-- # Class: "Sequence_sequenceReference" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retrieve the sequence information from a sequence provider
-- # Class: "Provider_memberOfRI" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: memberOfRI_id Description: The research infrastructure of which this organization is a member
-- # Class: "BiologicalMaterialOrigin_biologicalPartOrigin" Description: ""
--     * Slot: BiologicalMaterialOrigin_id Description: Autocreated FK slot
--     * Slot: biologicalPartOrigin_id Description: Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.
-- # Class: "RecombinantPartIdentification_sequence" Description: ""
--     * Slot: RecombinantPartIdentification_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Collection_collectionItem" Description: ""
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: collectionItem_id Description: An item of the collection
-- # Class: "ProductOrService_additionalCategory" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "ProductOrService_pathogenIdentification" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "ProductOrService_relatedDOI" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "ProductOrService_collection" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "ProductOrService_keywords" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "ProductOrService_complementaryDocument" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "ProductOrService_productPicture" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "ProductOrService_externalRelatedReference" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "ProductOrService_certification" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Service_additionalCategory" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Service_pathogenIdentification" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Service_relatedDOI" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Service_collection" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Service_keywords" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Service_complementaryDocument" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Service_productPicture" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Service_externalRelatedReference" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Service_certification" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Product_additionalCategory" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Product_pathogenIdentification" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Product_relatedDOI" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Product_collection" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Product_keywords" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Product_complementaryDocument" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Product_productPicture" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Product_externalRelatedReference" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Product_certification" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Antibody_sequenceReference" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retreive the sequence information from a sequence provider
-- # Class: "Antibody_additionalCategory" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Antibody_pathogenIdentification" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Antibody_relatedDOI" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Antibody_collection" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Antibody_keywords" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Antibody_complementaryDocument" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Antibody_productPicture" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Antibody_externalRelatedReference" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Antibody_certification" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Hybridoma_sequenceReference" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retreive the sequence information from a sequence provider
-- # Class: "Hybridoma_additionalCategory" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Hybridoma_pathogenIdentification" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Hybridoma_relatedDOI" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Hybridoma_collection" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Hybridoma_keywords" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Hybridoma_complementaryDocument" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Hybridoma_productPicture" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Hybridoma_externalRelatedReference" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Hybridoma_certification" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Protein_sequence" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Protein_relatedPDB" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: relatedPDB_id Description: Identifier for 3D structural data as per the PDB (Protein Data Bank) database
-- # Class: "Protein_specialFeature" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: specialFeature_id Description: Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
-- # Class: "Protein_proteinTAG" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: proteinTAG_id Description: Peptide sequences genetically grafted onto a recombinant protein
-- # Class: "Protein_domain" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: domain Description: A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function
-- # Class: "Protein_expressedAs" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: expressedAs Description: Refers to the form in which the protein is produced and manifested in a biological system. Possible values include "Soluble" (proteins that are dissolved in the cellular or extracellular fluid) and "Inclusion bodies" (aggregated proteins that are insoluble and form within the cell)
-- # Class: "Protein_inclusionBodiesType" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: inclusionBodiesType Description: Refers to the state of aggregated proteins within a cell. Possible values include "Denatured" (proteins are in an unfolded, inactive state) and "Refolded" (proteins have been processed to regain their functional, active conformation).
-- # Class: "Protein_expressionSystem" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: expressionSystem Description: The host organism or cellular environment used to produce a protein from a specific gene. Possible values include "E. coli" (bacterial system), "Insect cells" (using baculovirus vectors), and "Mammalian cells" (mammalian cell lines).
-- # Class: "Protein_functionalCharacterization" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: functionalCharacterization Description: The process of determining and describing the specific biological activities and roles of a protein. Possible values include "Functionally characterized" (the protein's functions have been identified and described) and "No functional characterization" (the protein's functions have not been identified or described).
-- # Class: "Protein_functionalTechnicalDescription" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: functionalTechnicalDescription Description: Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.
-- # Class: "Protein_proteinPurification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: proteinPurification Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
-- # Class: "Protein_theTAGStatusOfTheSolubilizedProtein" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: theTAGStatusOfTheSolubilizedProtein Description: Indicates the presence and condition of a tag on the protein after solubilization. Possible values include "Uncleaved Tag" (the tag is still attached to the protein), "Cleaved Tag" (the tag has been removed from the protein), and "No Tag" (the protein does not have a tag)
-- # Class: "Protein_typeOfFunctionalCharacterization" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: typeOfFunctionalCharacterization Description: Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include "Enzymatic" (the protein has been characterized for its enzyme activity) and "Antigenic" (the protein has been characterized for its ability to elicit an immune response).
-- # Class: "Protein_additionalCategory" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Protein_pathogenIdentification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Protein_relatedDOI" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Protein_collection" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Protein_keywords" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Protein_complementaryDocument" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Protein_productPicture" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Protein_externalRelatedReference" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Protein_certification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Nucleic Acid_hasGbFileOfTheConstruct" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: hasGbFileOfTheConstruct_id Description: A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct
-- # Class: "Nucleic Acid_sequence" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Nucleic Acid_pasmidSelection" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: pasmidSelection_id Description: Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid
-- # Class: "Nucleic Acid_additionalCategory" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Nucleic Acid_pathogenIdentification" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Nucleic Acid_relatedDOI" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Nucleic Acid_collection" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Nucleic Acid_keywords" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Nucleic Acid_complementaryDocument" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Nucleic Acid_productPicture" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Nucleic Acid_externalRelatedReference" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Nucleic Acid_certification" Description: ""
--     * Slot: Nucleic Acid_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Detection Kit_hasSOPFile" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: hasSOPFile_id Description: The related standard operating procedure file
-- # Class: "Detection Kit_additionalCategory" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Detection Kit_pathogenIdentification" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Detection Kit_relatedDOI" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Detection Kit_collection" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Detection Kit_keywords" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Detection Kit_complementaryDocument" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Detection Kit_productPicture" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Detection Kit_externalRelatedReference" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Detection Kit_certification" Description: ""
--     * Slot: Detection Kit_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Bundle_productsOfTheBundle" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: productsOfTheBundle_id Description: Associates the bundle with the individual products it contains, specifying the components included within the bundle.
-- # Class: "Bundle_complementaryDocument" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Links the bundle to any additional documents that provide supplementary information, instructions, or guidelines relevant to the use and assembly of the bundle's products.
-- # Class: "Bundle_additionalCategory" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Bundle_pathogenIdentification" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Bundle_relatedDOI" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Bundle_collection" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Bundle_keywords" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Bundle_productPicture" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Bundle_externalRelatedReference" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Bundle_certification" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Pathogen_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Pathogen_isolationHost" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Pathogen_productionCellLine" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Pathogen_propagationHost" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Pathogen_transmissionMethod" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Pathogen_sequence" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Pathogen_additionalCategory" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Pathogen_pathogenIdentification" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Pathogen_relatedDOI" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Pathogen_collection" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Pathogen_keywords" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Pathogen_complementaryDocument" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Pathogen_productPicture" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Pathogen_externalRelatedReference" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Pathogen_certification" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Virus_coInfectingViruses" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: coInfectingViruses_id Description: Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.
-- # Class: "Virus_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Virus_isolationHost" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Virus_productionCellLine" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Virus_propagationHost" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Virus_transmissionMethod" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Virus_sequence" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Virus_additionalCategory" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Virus_pathogenIdentification" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Virus_relatedDOI" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Virus_collection" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Virus_keywords" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Virus_complementaryDocument" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Virus_productPicture" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Virus_externalRelatedReference" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Virus_certification" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Bacterium_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Bacterium_isolationHost" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Bacterium_productionCellLine" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Bacterium_propagationHost" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Bacterium_transmissionMethod" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Bacterium_sequence" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Bacterium_additionalCategory" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Bacterium_pathogenIdentification" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Bacterium_relatedDOI" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Bacterium_collection" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Bacterium_keywords" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Bacterium_complementaryDocument" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Bacterium_productPicture" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Bacterium_externalRelatedReference" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Bacterium_certification" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Fungus_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Fungus_isolationHost" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Fungus_productionCellLine" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Fungus_propagationHost" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Fungus_transmissionMethod" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Fungus_sequence" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Fungus_additionalCategory" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Fungus_pathogenIdentification" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Fungus_relatedDOI" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Fungus_collection" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Fungus_keywords" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Fungus_complementaryDocument" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Fungus_productPicture" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Fungus_externalRelatedReference" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Fungus_certification" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Protozoan_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Protozoan_isolationHost" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Protozoan_productionCellLine" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Protozoan_propagationHost" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Protozoan_transmissionMethod" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Protozoan_sequence" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Protozoan_additionalCategory" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Protozoan_pathogenIdentification" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Protozoan_relatedDOI" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Protozoan_collection" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Protozoan_keywords" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Protozoan_complementaryDocument" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Protozoan_productPicture" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Protozoan_externalRelatedReference" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Protozoan_certification" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Viroid_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Viroid_isolationHost" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Viroid_productionCellLine" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Viroid_propagationHost" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Viroid_transmissionMethod" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Viroid_sequence" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Viroid_additionalCategory" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Viroid_pathogenIdentification" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Viroid_relatedDOI" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Viroid_collection" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Viroid_keywords" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Viroid_complementaryDocument" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Viroid_productPicture" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Viroid_externalRelatedReference" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Viroid_certification" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Prion_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted
-- # Class: "Prion_isolationHost" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated
-- # Class: "Prion_productionCellLine" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study
-- # Class: "Prion_propagationHost" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen
-- # Class: "Prion_transmissionMethod" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Prion_sequence" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format
-- # Class: "Prion_additionalCategory" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit
-- # Class: "Prion_pathogenIdentification" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Prion_relatedDOI" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: relatedDOI_id Description: Any DOI that can be related
-- # Class: "Prion_collection" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item
-- # Class: "Prion_keywords" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item
-- # Class: "Prion_complementaryDocument" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any complementary document that can be related to this Item
-- # Class: "Prion_productPicture" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item
-- # Class: "Prion_externalRelatedReference" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider
-- # Class: "Prion_certification" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification
-- # Class: "Certification_certificationDocument" Description: ""
--     * Slot: Certification_id Description: Autocreated FK slot
--     * Slot: certificationDocument_id Description: The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.

CREATE TABLE "Version" (
	id INTEGER NOT NULL, 
	"ID" TEXT NOT NULL, 
	"versionOf" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Nameable" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Catalogue" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedDataset" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataService" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ExternalRelatedReference" (
	id INTEGER NOT NULL, 
	reference TEXT NOT NULL, 
	"referenceLabel" TEXT NOT NULL, 
	"referenceProviderPrefix" TEXT NOT NULL, 
	"referenceProviderName" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL, 
	"sequenceFASTA" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceReference" (
	id INTEGER NOT NULL, 
	"accessionNumber" TEXT NOT NULL, 
	"sequenceProvider" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "BiologicalMaterialOrigin" (
	id INTEGER NOT NULL, 
	"recombinantMaterial" BOOLEAN NOT NULL, 
	"biologicalSourceType" BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RecombinantPartIdentification" (
	id INTEGER NOT NULL, 
	"partIdentification" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Image" (
	id INTEGER NOT NULL, 
	"altText" TEXT, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "License" (
	id INTEGER NOT NULL, 
	"resourceURL" TEXT, 
	"licensingOrAttribution" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "DataProvider" (
	id INTEGER NOT NULL, 
	"loginRequestMethod" TEXT, 
	"loginURL" TEXT, 
	"loginTokenName" TEXT, 
	"queryURL" TEXT NOT NULL, 
	"queryMethod" TEXT NOT NULL, 
	"contentType" TEXT NOT NULL, 
	"providedEntityType" TEXT NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "BiologicalPartOrigin" (
	id INTEGER NOT NULL, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "SyntheticPartOrigin" (
	id INTEGER NOT NULL, 
	"modificationsFromTheReferenceSequences" BOOLEAN NOT NULL, 
	"descriptionOfModificationsMadeFromTheReferenceSequences" TEXT, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "File" (
	id INTEGER NOT NULL, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Data" (
	id INTEGER NOT NULL, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Document" (
	id INTEGER NOT NULL, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Audio" (
	id INTEGER NOT NULL, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Video" (
	id INTEGER NOT NULL, 
	"contentURL" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Certification" (
	id INTEGER NOT NULL, 
	"resourceURL" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Sequence_sequenceReference" (
	"Sequence_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Sequence_id", "sequenceReference_id"), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "RecombinantPartIdentification_sequence" (
	"RecombinantPartIdentification_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("RecombinantPartIdentification_id", sequence_id), 
	FOREIGN KEY("RecombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Taxonomy" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"taxonDataProvider_id" INTEGER, 
	version_id INTEGER NOT NULL, 
	"versionDataProvider_id" INTEGER NOT NULL, 
	"rankDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("taxonDataProvider_id") REFERENCES "DataProvider" (id), 
	FOREIGN KEY(version_id) REFERENCES "Version" (id), 
	FOREIGN KEY("versionDataProvider_id") REFERENCES "DataProvider" (id), 
	FOREIGN KEY("rankDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "Vocabulary" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"termDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("termDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "Collection" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"collectionDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("collectionDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "BiologicalMaterialOrigin_biologicalPartOrigin" (
	"BiologicalMaterialOrigin_id" INTEGER, 
	"biologicalPartOrigin_id" INTEGER NOT NULL, 
	PRIMARY KEY ("BiologicalMaterialOrigin_id", "biologicalPartOrigin_id"), 
	FOREIGN KEY("BiologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("biologicalPartOrigin_id") REFERENCES "BiologicalPartOrigin" (id)
);
CREATE TABLE "Certification_certificationDocument" (
	"Certification_id" INTEGER, 
	"certificationDocument_id" INTEGER, 
	PRIMARY KEY ("Certification_id", "certificationDocument_id"), 
	FOREIGN KEY("Certification_id") REFERENCES "Certification" (id), 
	FOREIGN KEY("certificationDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Term" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "CommonName" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "VirusName" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "AlternateName" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "RiskGroup" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "DOI" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Journal" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PDBReference" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Keyword" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ProteinTag" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "SpecialFeature" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ExpressionVector" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PlasmidSelection" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PropagationHost" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "TransmissionMethod" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ProductionCellLine" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ProductCategory" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"parentCategory_id" INTEGER, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("parentCategory_id") REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IsolationHost" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "GeographicalOrigin" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IPLCOrigin" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Country" (
	id INTEGER NOT NULL, 
	"alpha2Code" TEXT NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IATAClassification" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Variant" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "TaxonomicRank" (
	id INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Publication" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	authors TEXT NOT NULL, 
	abstract TEXT NOT NULL, 
	"relatedDOI_id" INTEGER NOT NULL, 
	journal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id), 
	FOREIGN KEY(journal_id) REFERENCES "Journal" (id)
);
CREATE TABLE "Taxon" (
	id INTEGER NOT NULL, 
	"taxonomicID" TEXT NOT NULL, 
	"taxonomicNodeID" TEXT, 
	weight INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"parentTaxon_id" INTEGER NOT NULL, 
	rank_id INTEGER NOT NULL, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("parentTaxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY(rank_id) REFERENCES "TaxonomicRank" (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "NaturalPartOrigin" (
	id INTEGER NOT NULL, 
	"collectionDate" DATETIME NOT NULL, 
	"beforeDate" BOOLEAN NOT NULL, 
	"permitIdentifierForABS" TEXT, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"countryOfCollection_id" INTEGER NOT NULL, 
	"indigenousPoepleAndLocalCommunityOrigin_id" INTEGER, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("countryOfCollection_id") REFERENCES "Country" (id), 
	FOREIGN KEY("indigenousPoepleAndLocalCommunityOrigin_id") REFERENCES "IPLCOrigin" (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "ContactPoint" (
	id INTEGER NOT NULL, 
	email TEXT, 
	telephone TEXT, 
	"streetAddress" TEXT, 
	"addressLocality" TEXT, 
	"addressRegion" TEXT, 
	"postalCode" TEXT, 
	"oRCIDiD" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"addressCountry_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("addressCountry_id") REFERENCES "Country" (id)
);
CREATE TABLE "Taxonomy_rank" (
	"Taxonomy_id" INTEGER, 
	rank_id INTEGER, 
	PRIMARY KEY ("Taxonomy_id", rank_id), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id), 
	FOREIGN KEY(rank_id) REFERENCES "TaxonomicRank" (id)
);
CREATE TABLE "Vocabulary_term" (
	"Vocabulary_id" INTEGER, 
	term_id INTEGER, 
	PRIMARY KEY ("Vocabulary_id", term_id), 
	FOREIGN KEY("Vocabulary_id") REFERENCES "Vocabulary" (id), 
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);
CREATE TABLE "CommonName_alternateName" (
	"CommonName_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("CommonName_id", "alternateName_id"), 
	FOREIGN KEY("CommonName_id") REFERENCES "CommonName" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "CommonName_sourceOfInformation" (
	"CommonName_id" INTEGER, 
	"sourceOfInformation" TEXT, 
	PRIMARY KEY ("CommonName_id", "sourceOfInformation"), 
	FOREIGN KEY("CommonName_id") REFERENCES "CommonName" (id)
);
CREATE TABLE "VirusName_alternateName" (
	"VirusName_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("VirusName_id", "alternateName_id"), 
	FOREIGN KEY("VirusName_id") REFERENCES "VirusName" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "VirusName_sourceOfInformation" (
	"VirusName_id" INTEGER, 
	"sourceOfInformation" TEXT, 
	PRIMARY KEY ("VirusName_id", "sourceOfInformation"), 
	FOREIGN KEY("VirusName_id") REFERENCES "VirusName" (id)
);
CREATE TABLE "AlternateName_alternateName" (
	"AlternateName_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("AlternateName_id", "alternateName_id"), 
	FOREIGN KEY("AlternateName_id") REFERENCES "AlternateName" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "AlternateName_sourceOfInformation" (
	"AlternateName_id" INTEGER, 
	"sourceOfInformation" TEXT, 
	PRIMARY KEY ("AlternateName_id", "sourceOfInformation"), 
	FOREIGN KEY("AlternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "Variant_alternateName" (
	"Variant_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("Variant_id", "alternateName_id"), 
	FOREIGN KEY("Variant_id") REFERENCES "Variant" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "Variant_sourceOfInformation" (
	"Variant_id" INTEGER, 
	"sourceOfInformation" TEXT, 
	PRIMARY KEY ("Variant_id", "sourceOfInformation"), 
	FOREIGN KEY("Variant_id") REFERENCES "Variant" (id)
);
CREATE TABLE "TaxonomicRank_taxonomy" (
	"TaxonomicRank_id" INTEGER, 
	taxonomy_id INTEGER, 
	PRIMARY KEY ("TaxonomicRank_id", taxonomy_id), 
	FOREIGN KEY("TaxonomicRank_id") REFERENCES "TaxonomicRank" (id), 
	FOREIGN KEY(taxonomy_id) REFERENCES "Taxonomy" (id)
);
CREATE TABLE "PathogenIdentification" (
	id INTEGER NOT NULL, 
	"pathogenType" TEXT NOT NULL, 
	subspecies TEXT, 
	strain TEXT, 
	isolate TEXT, 
	genotype TEXT, 
	serotype TEXT, 
	taxon_id INTEGER NOT NULL, 
	"pathogenName_id" INTEGER NOT NULL, 
	variant_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(taxon_id) REFERENCES "Taxon" (id), 
	FOREIGN KEY("pathogenName_id") REFERENCES "CommonName" (id), 
	FOREIGN KEY(variant_id) REFERENCES "Variant" (id)
);
CREATE TABLE "PersonOrOrganization" (
	id INTEGER NOT NULL, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	"oRCIDiD" TEXT, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Organization" (
	id INTEGER NOT NULL, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"alternateName_id" INTEGER, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "RI" (
	id INTEGER NOT NULL, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"alternateName_id" INTEGER, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Provider" (
	id INTEGER NOT NULL, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"alternateName_id" INTEGER, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Originator" (
	id INTEGER NOT NULL, 
	"homePage" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "MSDS" (
	id INTEGER NOT NULL, 
	"physicalChemicalProperties" TEXT, 
	"hazardsIdentification" TEXT, 
	"firstAidMeasures" TEXT, 
	"fireFightingMeasures" TEXT, 
	"accidentalReleaseMeasures" TEXT, 
	"handlingAndStorage" TEXT, 
	"exposureControlsPersonalProtection" TEXT, 
	"stabilityAndReactivity" TEXT, 
	"toxicologicalInformation" TEXT, 
	"ecologicalInformation" TEXT, 
	"disposalConsiderations" TEXT, 
	"transportInformation" TEXT, 
	"regulatoryInformation" TEXT, 
	"furtherInformation" TEXT, 
	"msdsContact_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("msdsContact_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Taxonomy_taxon" (
	"Taxonomy_id" INTEGER, 
	taxon_id INTEGER, 
	PRIMARY KEY ("Taxonomy_id", taxon_id), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id), 
	FOREIGN KEY(taxon_id) REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_taxonomy" (
	"Taxon_id" INTEGER, 
	taxonomy_id INTEGER, 
	PRIMARY KEY ("Taxon_id", taxonomy_id), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY(taxonomy_id) REFERENCES "Taxonomy" (id)
);
CREATE TABLE "Taxon_previouslyKnownAs" (
	"Taxon_id" INTEGER, 
	"previouslyKnownAs_id" INTEGER, 
	PRIMARY KEY ("Taxon_id", "previouslyKnownAs_id"), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY("previouslyKnownAs_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_externalEquivalentTaxon" (
	"Taxon_id" INTEGER, 
	"externalEquivalentTaxon_id" INTEGER, 
	PRIMARY KEY ("Taxon_id", "externalEquivalentTaxon_id"), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY("externalEquivalentTaxon_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "ProductOrService" (
	id INTEGER NOT NULL, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Service" (
	id INTEGER NOT NULL, 
	"modelSpecies" TEXT, 
	"modelType" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Product" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Antibody" (
	id INTEGER NOT NULL, 
	"productionSystem" TEXT, 
	"antibodyPurifiedByAffinity" BOOLEAN NOT NULL, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	"targetedAntigen" TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Hybridoma" (
	id INTEGER NOT NULL, 
	"hybridomaDescription" TEXT NOT NULL, 
	"productionSystem" TEXT, 
	"antibodyPurifiedByAffinity" BOOLEAN NOT NULL, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	"targetedAntigen" TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Protein" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Nucleic Acid" (
	id INTEGER NOT NULL, 
	"isItAClonedNucleicAcid" BOOLEAN NOT NULL, 
	"regionEncompassedInThisProduct" TEXT NOT NULL, 
	"mutationObserved" BOOLEAN NOT NULL, 
	"observedMutations" TEXT, 
	"identificationTechnique" TEXT, 
	sequencing TEXT NOT NULL, 
	titer TEXT, 
	"sequenceChecked" BOOLEAN NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"clonedIntoPlasmid_id" INTEGER, 
	"hasTAG_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("clonedIntoPlasmid_id") REFERENCES "ExpressionVector" (id), 
	FOREIGN KEY("hasTAG_id") REFERENCES "ProteinTag" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Detection Kit" (
	id INTEGER NOT NULL, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	specificity TEXT, 
	"targetedRegion" TEXT, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Bundle" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Pathogen" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Virus" (
	id INTEGER NOT NULL, 
	"contaminationWithCoInfectingViruses" BOOLEAN NOT NULL, 
	"mycoplasmicContent" BOOLEAN NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Bacterium" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Fungus" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Protozoan" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Viroid" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Prion" (
	id INTEGER NOT NULL, 
	cultivability TEXT NOT NULL, 
	"clinicalInformation" TEXT, 
	"identificationTechnique" TEXT, 
	infectivity TEXT NOT NULL, 
	"infectivityTest" TEXT, 
	"isolationTechnique" TEXT, 
	"isolationConditions" TEXT, 
	"letterOfAuthority" TEXT NOT NULL, 
	passage TEXT, 
	"genomeSequencing" TEXT NOT NULL, 
	titer TEXT NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"accessPointURL" TEXT NOT NULL, 
	"refSKU" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" TEXT NOT NULL, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canItBeUsedToProduceGMO" BOOLEAN, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"hasIATAClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("hasIATAClassification_id") REFERENCES "IATAClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "MSDS" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "PathogenIdentification_hostType" (
	"PathogenIdentification_id" INTEGER, 
	"hostType" TEXT, 
	PRIMARY KEY ("PathogenIdentification_id", "hostType"), 
	FOREIGN KEY("PathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Provider_memberOfRI" (
	"Provider_id" INTEGER, 
	"memberOfRI_id" INTEGER, 
	PRIMARY KEY ("Provider_id", "memberOfRI_id"), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id), 
	FOREIGN KEY("memberOfRI_id") REFERENCES "RI" (id)
);
CREATE TABLE "Collection_collectionItem" (
	"Collection_id" INTEGER, 
	"collectionItem_id" INTEGER, 
	PRIMARY KEY ("Collection_id", "collectionItem_id"), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id), 
	FOREIGN KEY("collectionItem_id") REFERENCES "ProductOrService" (id)
);
CREATE TABLE "ProductOrService_additionalCategory" (
	"ProductOrService_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "additionalCategory_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "ProductOrService_pathogenIdentification" (
	"ProductOrService_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("ProductOrService_id", "pathogenIdentification_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "ProductOrService_relatedDOI" (
	"ProductOrService_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "relatedDOI_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "ProductOrService_collection" (
	"ProductOrService_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("ProductOrService_id", collection_id), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "ProductOrService_keywords" (
	"ProductOrService_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("ProductOrService_id", keywords_id), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "ProductOrService_complementaryDocument" (
	"ProductOrService_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "complementaryDocument_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "ProductOrService_productPicture" (
	"ProductOrService_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "productPicture_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "ProductOrService_externalRelatedReference" (
	"ProductOrService_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "externalRelatedReference_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "ProductOrService_certification" (
	"ProductOrService_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("ProductOrService_id", certification_id), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Service_additionalCategory" (
	"Service_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Service_id", "additionalCategory_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Service_pathogenIdentification" (
	"Service_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Service_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Service_relatedDOI" (
	"Service_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Service_id", "relatedDOI_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Service_collection" (
	"Service_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Service_id", collection_id), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Service_keywords" (
	"Service_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Service_id", keywords_id), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Service_complementaryDocument" (
	"Service_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Service_id", "complementaryDocument_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Service_productPicture" (
	"Service_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Service_id", "productPicture_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Service_externalRelatedReference" (
	"Service_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Service_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Service_certification" (
	"Service_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Service_id", certification_id), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Product_additionalCategory" (
	"Product_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Product_id", "additionalCategory_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Product_pathogenIdentification" (
	"Product_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Product_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Product_relatedDOI" (
	"Product_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Product_id", "relatedDOI_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Product_collection" (
	"Product_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Product_id", collection_id), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Product_keywords" (
	"Product_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Product_id", keywords_id), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Product_complementaryDocument" (
	"Product_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Product_id", "complementaryDocument_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Product_productPicture" (
	"Product_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Product_id", "productPicture_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Product_externalRelatedReference" (
	"Product_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Product_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Product_certification" (
	"Product_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Product_id", certification_id), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Antibody_sequenceReference" (
	"Antibody_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "sequenceReference_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "Antibody_additionalCategory" (
	"Antibody_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "additionalCategory_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Antibody_pathogenIdentification" (
	"Antibody_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Antibody_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Antibody_relatedDOI" (
	"Antibody_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "relatedDOI_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Antibody_collection" (
	"Antibody_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Antibody_id", collection_id), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Antibody_keywords" (
	"Antibody_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Antibody_id", keywords_id), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Antibody_complementaryDocument" (
	"Antibody_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "complementaryDocument_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Antibody_productPicture" (
	"Antibody_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "productPicture_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Antibody_externalRelatedReference" (
	"Antibody_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Antibody_certification" (
	"Antibody_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Antibody_id", certification_id), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Hybridoma_sequenceReference" (
	"Hybridoma_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "sequenceReference_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "Hybridoma_additionalCategory" (
	"Hybridoma_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "additionalCategory_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Hybridoma_pathogenIdentification" (
	"Hybridoma_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Hybridoma_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Hybridoma_relatedDOI" (
	"Hybridoma_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "relatedDOI_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Hybridoma_collection" (
	"Hybridoma_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Hybridoma_id", collection_id), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Hybridoma_keywords" (
	"Hybridoma_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Hybridoma_id", keywords_id), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Hybridoma_complementaryDocument" (
	"Hybridoma_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "complementaryDocument_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Hybridoma_productPicture" (
	"Hybridoma_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "productPicture_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Hybridoma_externalRelatedReference" (
	"Hybridoma_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Hybridoma_certification" (
	"Hybridoma_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Hybridoma_id", certification_id), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Protein_sequence" (
	"Protein_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protein_id", sequence_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Protein_relatedPDB" (
	"Protein_id" INTEGER, 
	"relatedPDB_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "relatedPDB_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("relatedPDB_id") REFERENCES "PDBReference" (id)
);
CREATE TABLE "Protein_specialFeature" (
	"Protein_id" INTEGER, 
	"specialFeature_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "specialFeature_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("specialFeature_id") REFERENCES "SpecialFeature" (id)
);
CREATE TABLE "Protein_proteinTAG" (
	"Protein_id" INTEGER, 
	"proteinTAG_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "proteinTAG_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("proteinTAG_id") REFERENCES "ProteinTag" (id)
);
CREATE TABLE "Protein_domain" (
	"Protein_id" INTEGER, 
	domain TEXT, 
	PRIMARY KEY ("Protein_id", domain), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_expressedAs" (
	"Protein_id" INTEGER, 
	"expressedAs" TEXT, 
	PRIMARY KEY ("Protein_id", "expressedAs"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_inclusionBodiesType" (
	"Protein_id" INTEGER, 
	"inclusionBodiesType" TEXT, 
	PRIMARY KEY ("Protein_id", "inclusionBodiesType"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_expressionSystem" (
	"Protein_id" INTEGER, 
	"expressionSystem" TEXT, 
	PRIMARY KEY ("Protein_id", "expressionSystem"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_functionalCharacterization" (
	"Protein_id" INTEGER, 
	"functionalCharacterization" TEXT, 
	PRIMARY KEY ("Protein_id", "functionalCharacterization"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_functionalTechnicalDescription" (
	"Protein_id" INTEGER, 
	"functionalTechnicalDescription" TEXT, 
	PRIMARY KEY ("Protein_id", "functionalTechnicalDescription"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_proteinPurification" (
	"Protein_id" INTEGER, 
	"proteinPurification" TEXT, 
	PRIMARY KEY ("Protein_id", "proteinPurification"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_theTAGStatusOfTheSolubilizedProtein" (
	"Protein_id" INTEGER, 
	"theTAGStatusOfTheSolubilizedProtein" TEXT, 
	PRIMARY KEY ("Protein_id", "theTAGStatusOfTheSolubilizedProtein"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_typeOfFunctionalCharacterization" (
	"Protein_id" INTEGER, 
	"typeOfFunctionalCharacterization" TEXT, 
	PRIMARY KEY ("Protein_id", "typeOfFunctionalCharacterization"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_additionalCategory" (
	"Protein_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "additionalCategory_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Protein_pathogenIdentification" (
	"Protein_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Protein_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Protein_relatedDOI" (
	"Protein_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "relatedDOI_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Protein_collection" (
	"Protein_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protein_id", collection_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Protein_keywords" (
	"Protein_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protein_id", keywords_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Protein_complementaryDocument" (
	"Protein_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "complementaryDocument_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Protein_productPicture" (
	"Protein_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "productPicture_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Protein_externalRelatedReference" (
	"Protein_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Protein_certification" (
	"Protein_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Protein_id", certification_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Nucleic Acid_hasGbFileOfTheConstruct" (
	"Nucleic Acid_id" INTEGER, 
	"hasGbFileOfTheConstruct_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "hasGbFileOfTheConstruct_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("hasGbFileOfTheConstruct_id") REFERENCES "Data" (id)
);
CREATE TABLE "Nucleic Acid_sequence" (
	"Nucleic Acid_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Nucleic Acid_id", sequence_id), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Nucleic Acid_pasmidSelection" (
	"Nucleic Acid_id" INTEGER, 
	"pasmidSelection_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "pasmidSelection_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("pasmidSelection_id") REFERENCES "PlasmidSelection" (id)
);
CREATE TABLE "Nucleic Acid_additionalCategory" (
	"Nucleic Acid_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "additionalCategory_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Nucleic Acid_pathogenIdentification" (
	"Nucleic Acid_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Nucleic Acid_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Nucleic Acid_relatedDOI" (
	"Nucleic Acid_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "relatedDOI_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Nucleic Acid_collection" (
	"Nucleic Acid_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Nucleic Acid_id", collection_id), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Nucleic Acid_keywords" (
	"Nucleic Acid_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Nucleic Acid_id", keywords_id), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Nucleic Acid_complementaryDocument" (
	"Nucleic Acid_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "complementaryDocument_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Nucleic Acid_productPicture" (
	"Nucleic Acid_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "productPicture_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Nucleic Acid_externalRelatedReference" (
	"Nucleic Acid_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Nucleic Acid_certification" (
	"Nucleic Acid_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Nucleic Acid_id", certification_id), 
	FOREIGN KEY("Nucleic Acid_id") REFERENCES "Nucleic Acid" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Detection Kit_hasSOPFile" (
	"Detection Kit_id" INTEGER, 
	"hasSOPFile_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "hasSOPFile_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("hasSOPFile_id") REFERENCES "File" (id)
);
CREATE TABLE "Detection Kit_additionalCategory" (
	"Detection Kit_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "additionalCategory_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Detection Kit_pathogenIdentification" (
	"Detection Kit_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Detection Kit_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Detection Kit_relatedDOI" (
	"Detection Kit_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "relatedDOI_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Detection Kit_collection" (
	"Detection Kit_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Detection Kit_id", collection_id), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Detection Kit_keywords" (
	"Detection Kit_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Detection Kit_id", keywords_id), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Detection Kit_complementaryDocument" (
	"Detection Kit_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "complementaryDocument_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Detection Kit_productPicture" (
	"Detection Kit_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "productPicture_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Detection Kit_externalRelatedReference" (
	"Detection Kit_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Detection Kit_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Detection Kit_certification" (
	"Detection Kit_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Detection Kit_id", certification_id), 
	FOREIGN KEY("Detection Kit_id") REFERENCES "Detection Kit" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Bundle_productsOfTheBundle" (
	"Bundle_id" INTEGER, 
	"productsOfTheBundle_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Bundle_id", "productsOfTheBundle_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("productsOfTheBundle_id") REFERENCES "Product" (id)
);
CREATE TABLE "Bundle_complementaryDocument" (
	"Bundle_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "complementaryDocument_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "File" (id)
);
CREATE TABLE "Bundle_additionalCategory" (
	"Bundle_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "additionalCategory_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Bundle_pathogenIdentification" (
	"Bundle_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Bundle_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Bundle_relatedDOI" (
	"Bundle_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "relatedDOI_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Bundle_collection" (
	"Bundle_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Bundle_id", collection_id), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Bundle_keywords" (
	"Bundle_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Bundle_id", keywords_id), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Bundle_productPicture" (
	"Bundle_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "productPicture_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Bundle_externalRelatedReference" (
	"Bundle_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Bundle_certification" (
	"Bundle_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Bundle_id", certification_id), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Pathogen_suspectedEpidemiologicalOrigin" (
	"Pathogen_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Pathogen_isolationHost" (
	"Pathogen_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "isolationHost_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Pathogen_productionCellLine" (
	"Pathogen_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "productionCellLine_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Pathogen_propagationHost" (
	"Pathogen_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "propagationHost_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Pathogen_transmissionMethod" (
	"Pathogen_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "transmissionMethod_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Pathogen_sequence" (
	"Pathogen_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Pathogen_id", sequence_id), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Pathogen_additionalCategory" (
	"Pathogen_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "additionalCategory_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Pathogen_pathogenIdentification" (
	"Pathogen_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Pathogen_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Pathogen_relatedDOI" (
	"Pathogen_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "relatedDOI_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Pathogen_collection" (
	"Pathogen_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Pathogen_id", collection_id), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Pathogen_keywords" (
	"Pathogen_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Pathogen_id", keywords_id), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Pathogen_complementaryDocument" (
	"Pathogen_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "complementaryDocument_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Pathogen_productPicture" (
	"Pathogen_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "productPicture_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Pathogen_externalRelatedReference" (
	"Pathogen_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Pathogen_certification" (
	"Pathogen_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Pathogen_id", certification_id), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Virus_coInfectingViruses" (
	"Virus_id" INTEGER, 
	"coInfectingViruses_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "coInfectingViruses_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("coInfectingViruses_id") REFERENCES "VirusName" (id)
);
CREATE TABLE "Virus_suspectedEpidemiologicalOrigin" (
	"Virus_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Virus_isolationHost" (
	"Virus_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "isolationHost_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Virus_productionCellLine" (
	"Virus_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "productionCellLine_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Virus_propagationHost" (
	"Virus_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "propagationHost_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Virus_transmissionMethod" (
	"Virus_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "transmissionMethod_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Virus_sequence" (
	"Virus_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Virus_id", sequence_id), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Virus_additionalCategory" (
	"Virus_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "additionalCategory_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Virus_pathogenIdentification" (
	"Virus_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Virus_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Virus_relatedDOI" (
	"Virus_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "relatedDOI_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Virus_collection" (
	"Virus_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Virus_id", collection_id), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Virus_keywords" (
	"Virus_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Virus_id", keywords_id), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Virus_complementaryDocument" (
	"Virus_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "complementaryDocument_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Virus_productPicture" (
	"Virus_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "productPicture_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Virus_externalRelatedReference" (
	"Virus_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Virus_certification" (
	"Virus_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Virus_id", certification_id), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Bacterium_suspectedEpidemiologicalOrigin" (
	"Bacterium_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Bacterium_isolationHost" (
	"Bacterium_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "isolationHost_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Bacterium_productionCellLine" (
	"Bacterium_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "productionCellLine_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Bacterium_propagationHost" (
	"Bacterium_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "propagationHost_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Bacterium_transmissionMethod" (
	"Bacterium_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "transmissionMethod_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Bacterium_sequence" (
	"Bacterium_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Bacterium_id", sequence_id), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Bacterium_additionalCategory" (
	"Bacterium_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "additionalCategory_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Bacterium_pathogenIdentification" (
	"Bacterium_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Bacterium_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Bacterium_relatedDOI" (
	"Bacterium_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "relatedDOI_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Bacterium_collection" (
	"Bacterium_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Bacterium_id", collection_id), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Bacterium_keywords" (
	"Bacterium_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Bacterium_id", keywords_id), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Bacterium_complementaryDocument" (
	"Bacterium_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "complementaryDocument_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Bacterium_productPicture" (
	"Bacterium_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "productPicture_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Bacterium_externalRelatedReference" (
	"Bacterium_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Bacterium_certification" (
	"Bacterium_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Bacterium_id", certification_id), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Fungus_suspectedEpidemiologicalOrigin" (
	"Fungus_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Fungus_isolationHost" (
	"Fungus_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "isolationHost_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Fungus_productionCellLine" (
	"Fungus_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "productionCellLine_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Fungus_propagationHost" (
	"Fungus_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "propagationHost_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Fungus_transmissionMethod" (
	"Fungus_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "transmissionMethod_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Fungus_sequence" (
	"Fungus_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Fungus_id", sequence_id), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Fungus_additionalCategory" (
	"Fungus_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "additionalCategory_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Fungus_pathogenIdentification" (
	"Fungus_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Fungus_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Fungus_relatedDOI" (
	"Fungus_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "relatedDOI_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Fungus_collection" (
	"Fungus_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Fungus_id", collection_id), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Fungus_keywords" (
	"Fungus_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Fungus_id", keywords_id), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Fungus_complementaryDocument" (
	"Fungus_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "complementaryDocument_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Fungus_productPicture" (
	"Fungus_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "productPicture_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Fungus_externalRelatedReference" (
	"Fungus_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Fungus_certification" (
	"Fungus_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Fungus_id", certification_id), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Protozoan_suspectedEpidemiologicalOrigin" (
	"Protozoan_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Protozoan_isolationHost" (
	"Protozoan_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "isolationHost_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Protozoan_productionCellLine" (
	"Protozoan_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "productionCellLine_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Protozoan_propagationHost" (
	"Protozoan_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "propagationHost_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Protozoan_transmissionMethod" (
	"Protozoan_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "transmissionMethod_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Protozoan_sequence" (
	"Protozoan_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protozoan_id", sequence_id), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Protozoan_additionalCategory" (
	"Protozoan_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "additionalCategory_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Protozoan_pathogenIdentification" (
	"Protozoan_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Protozoan_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Protozoan_relatedDOI" (
	"Protozoan_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "relatedDOI_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Protozoan_collection" (
	"Protozoan_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protozoan_id", collection_id), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Protozoan_keywords" (
	"Protozoan_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protozoan_id", keywords_id), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Protozoan_complementaryDocument" (
	"Protozoan_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "complementaryDocument_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Protozoan_productPicture" (
	"Protozoan_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "productPicture_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Protozoan_externalRelatedReference" (
	"Protozoan_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Protozoan_certification" (
	"Protozoan_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Protozoan_id", certification_id), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Viroid_suspectedEpidemiologicalOrigin" (
	"Viroid_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Viroid_isolationHost" (
	"Viroid_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "isolationHost_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Viroid_productionCellLine" (
	"Viroid_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "productionCellLine_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Viroid_propagationHost" (
	"Viroid_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "propagationHost_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Viroid_transmissionMethod" (
	"Viroid_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "transmissionMethod_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Viroid_sequence" (
	"Viroid_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Viroid_id", sequence_id), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Viroid_additionalCategory" (
	"Viroid_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "additionalCategory_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Viroid_pathogenIdentification" (
	"Viroid_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Viroid_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Viroid_relatedDOI" (
	"Viroid_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "relatedDOI_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Viroid_collection" (
	"Viroid_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Viroid_id", collection_id), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Viroid_keywords" (
	"Viroid_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Viroid_id", keywords_id), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Viroid_complementaryDocument" (
	"Viroid_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "complementaryDocument_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Viroid_productPicture" (
	"Viroid_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "productPicture_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Viroid_externalRelatedReference" (
	"Viroid_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Viroid_certification" (
	"Viroid_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Viroid_id", certification_id), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "Prion_suspectedEpidemiologicalOrigin" (
	"Prion_id" INTEGER, 
	"suspectedEpidemiologicalOrigin_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "suspectedEpidemiologicalOrigin_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("suspectedEpidemiologicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "Prion_isolationHost" (
	"Prion_id" INTEGER, 
	"isolationHost_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "isolationHost_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("isolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "Prion_productionCellLine" (
	"Prion_id" INTEGER, 
	"productionCellLine_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "productionCellLine_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("productionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "Prion_propagationHost" (
	"Prion_id" INTEGER, 
	"propagationHost_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "propagationHost_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("propagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "Prion_transmissionMethod" (
	"Prion_id" INTEGER, 
	"transmissionMethod_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "transmissionMethod_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("transmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "Prion_sequence" (
	"Prion_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Prion_id", sequence_id), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Prion_additionalCategory" (
	"Prion_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "additionalCategory_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "Prion_pathogenIdentification" (
	"Prion_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Prion_id", "pathogenIdentification_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "Prion_relatedDOI" (
	"Prion_id" INTEGER, 
	"relatedDOI_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "relatedDOI_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("relatedDOI_id") REFERENCES "DOI" (id)
);
CREATE TABLE "Prion_collection" (
	"Prion_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("Prion_id", collection_id), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "Prion_keywords" (
	"Prion_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("Prion_id", keywords_id), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "Prion_complementaryDocument" (
	"Prion_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "complementaryDocument_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Prion_productPicture" (
	"Prion_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "productPicture_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "Prion_externalRelatedReference" (
	"Prion_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "externalRelatedReference_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Prion_certification" (
	"Prion_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("Prion_id", certification_id), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
