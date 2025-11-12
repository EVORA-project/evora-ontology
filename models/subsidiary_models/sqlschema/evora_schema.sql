-- # Class: "Resource" Description: "Resource published or curated by a single agent."
--     * Slot: id Description: 
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Dataset" Description: "A collection of data, published or curated by a single agent, and available for access."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "DataService" Description: "A collection of operations that provides access to one or more datasets or data processing functions."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: endpointUrl Description: The URL template that allows to get the content.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Version" Description: "Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)."
--     * Slot: id Description: 
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: versionOf Description: Identifier of what type of entities the version qualifies.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Catalogue" Description: "A curated collection of metadata about resources."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Taxonomy" Description: "A structured representation of data about the classification and naming of biological organisms into groups according to shared characteristics."
--     * Slot: id Description: 
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: taxonDataProvider_id Description: The data provider for the taxons of the taxonomy.
--     * Slot: versionDataProvider_id Description: The data provider for the Version ID of this taxonomy.
--     * Slot: rankDataProvider_id Description: The data provider for the description of the taxonomic ranks used in this taxonomy.
-- # Class: "DataProvider" Description: "An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources."
--     * Slot: id Description: 
--     * Slot: loginRequestMethod Description: The http request method used to acces the login request url.
--     * Slot: loginUrl Description: The URL template that allows to log in if required.
--     * Slot: loginTokenName Description: The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query.
--     * Slot: queryMethod Description: The http request method used to access the requested query url.
--     * Slot: contentType Description: The content type of the response to queries. It specifies the serialization, file type, or media type used to convey the resource, typically expressed as a MIME type following IANA media type registrations.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: endpointUrl Description: The URL template that allows to get the content.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "PathogenIdentification" Description: "A collection of distinguishing information that enables the differentiation of a pathogen from another."
--     * Slot: id Description: 
--     * Slot: pathogenType Description: Identification of the specific type of pathogen among the listed categories e.g. 'Virus','Viroid','Bacterium'...
--     * Slot: subspecies Description: The subspecies information differentiates closely related pathogens within a single species.
--     * Slot: strain Description: Identifier given to a genetic variant within a single species.
--     * Slot: isolate Description: Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host.
--     * Slot: genotype Description: Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes.
--     * Slot: serotype Description: Genetically related pathogens that group together based on serological relationships.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: taxon_id Description: Scientifically classified group or entity within the reference taxonomy.
--     * Slot: pathogenName_id Description: A pathogen common name or a name that describes a group of pathogens.
--     * Slot: variant_id Description: An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain.
-- # Class: "Publication" Description: "A scientific publication."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: authors Description: The list of authors.
--     * Slot: abstract Description: Concise summary of the publication.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
--     * Slot: journal_id Description: The scientific journal in which the publication was published.
-- # Class: "Vocabulary" Description: "A subset of words or phrases specific to a particular subject or field."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: termDataProvider_id Description: An external API or Endpoint that permits to retrieve the terms of this vocabulary.
-- # Class: "Term" Description: "Word or phrase from a specialized area of knowledge."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "CommonName" Description: "Vernacular name that is the name used in everyday language to refer to something like an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific or technical name."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "VirusName" Description: "A virus vernacular name or a name that describes a group of viruses."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "AlternateName" Description: "List of other names for things."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "RiskGroup" Description: "Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "BiosafetyLevel" Description: "The level of biocontainment required or applied in the facility where the biological agent is manipulated."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Doi" Description: "A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Journal" Description: "Periodical journal publishing scientific research."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "PdbReference" Description: "Identifier for 3D structural data as per the PDB (Protein Data Bank) database."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Keyword" Description: "A term or phrase used to tag and categorize content."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "TagSequence" Description: "The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "SpecialFeature" Description: "Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ..."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "ExpressionVector" Description: "A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "PlasmidSelection" Description: "The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "PropagationHost" Description: "The organism used to grow and multiply the pathogen under controlled conditions."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "TransmissionMethod" Description: "The process by which the pathogen spreads between hosts."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "ProductionCellLine" Description: "A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "ProductCategory" Description: "A term used to classify a group of products that share common characteristics or functions, which helps in their organization."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: parentCategory_id Description: An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "IsolationHost" Description: "Host organism from which the pathogen was isolated."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "GeographicalOrigin" Description: "The specific location or region where a physical item, originates or is naturally found."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "IplcOrigin" Description: "The IPLC area (Indigenous People and Local Communities) from which a physical item originates."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Country" Description: "The country as of ISO3166."
--     * Slot: id Description: 
--     * Slot: alpha2Code Description: Two-letter country codes from ISO 3166-1 alpha-2.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "IataClassification" Description: "The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Variant" Description: "An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "TaxonomicRank" Description: "The possible taxonomic ranks and their description."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "Taxon" Description: "Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit."
--     * Slot: id Description: 
--     * Slot: taxonomicId Description: The taxonomic identifier as a persistent identifier accross releases.
--     * Slot: taxonomicNodeId Description: The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: parentTaxon_id Description: The parent taxon of the current taxon.
--     * Slot: rank_id Description: Relative level or position of the identified taxon in the taxonomy.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "ClinicalGroup" Description: "A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: weight Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: inVocabulary_id Description: Terms belong to a specific vocabulary.
-- # Class: "ExternalRelatedReference" Description: "A reference that permits to retrieve an item from an external provider."
--     * Slot: id Description: 
--     * Slot: reference Description: The identifier reference of the connected external item.
--     * Slot: referenceLabel Description: The label informing what this reference is about.
--     * Slot: referenceProviderPrefix Description: The url prefix that once completed with the reference will lead to the linked external resource.
--     * Slot: referenceProviderName Description: The name for the reference provider.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Sequence" Description: "A nucleic acid or protein sequence information."
--     * Slot: id Description: 
--     * Slot: sequenceFasta Description: Textual encoding of a biological sequence information in FASTA format.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "SequenceReference" Description: "A reference that permits to retrieve the sequence information from a sequence provider."
--     * Slot: id Description: 
--     * Slot: accessionNumber Description: The sequence ID that permits to retrieve the sequence information from the sequence provider.
--     * Slot: sequenceProvider Description: The name of the sequence provider within the list of accepted sequence providers.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "PersonOrOrganization" Description: "A person or an organization."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Person" Description: "An individual."
--     * Slot: id Description: 
--     * Slot: orcidId Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation.
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Organization" Description: "A social entity established to meet needs or pursue specific goals."
--     * Slot: id Description: 
--     * Slot: rorId Description: The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: country_id Description: The country of the organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "ReasearchInfrastructure" Description: "A research infrastructure (RI)."
--     * Slot: id Description: 
--     * Slot: rorId Description: The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: country_id Description: The country of the organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Provider" Description: "A provider of products or services, as a specific organization."
--     * Slot: id Description: 
--     * Slot: rorId Description: The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: country_id Description: The country of the organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Originator" Description: "The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: homePage Description: A web page that serves as the main or introductory page.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "BiologicalMaterialOrigin" Description: "Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol."
--     * Slot: id Description: 
--     * Slot: recombinantMaterial Description: Indicates if this biological material is a recombinant biological material.
--     * Slot: biologicalSourceType Description: Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "BiologicalPartOrigin" Description: "Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material."
--     * Slot: id Description: 
--     * Slot: accessToPhysicalGeneticResource Description: Indicate if the biological part was produced with access to a physical genetic resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part.
-- # Class: "NaturalPartOrigin" Description: "Information on the origin of a natural part that composes the biological material."
--     * Slot: id Description: 
--     * Slot: collectionDate Description: The date when the sample was collected in situ. If unknown/private, use a proxy date such as 'date received' and indicate this by setting to true the before date property.
--     * Slot: beforeDate Description: Set to TRUE if a proxy date for the collection date is used.
--     * Slot: permitIdentifierForAbs Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations.
--     * Slot: accessToPhysicalGeneticResource Description: Indicate if the biological part was produced with access to a physical genetic resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: countryOfCollection_id Description: The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to 'country of origin'.
--     * Slot: indigenousPeopleAndLocalCommunityOrigin_id Description: The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant.
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part.
-- # Class: "SyntheticPartOrigin" Description: "Information on the origin of a synthetic part that composes the biological material."
--     * Slot: id Description: 
--     * Slot: modificationsFromTheReferenceSequences Description: Set to TRUE if there was is any modification made from the reference sequence.
--     * Slot: descriptionOfModificationsMadeFromTheReferenceSequences Description: List the modifications mades from the reference sequence if any.
--     * Slot: accessToPhysicalGeneticResource Description: Indicate if the biological part was produced with access to a physical genetic resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: recombinantPartIdentification_id Description: Identification of a recombinant part.
-- # Class: "RecombinantPartIdentification" Description: "Identification of a recombinant part."
--     * Slot: id Description: 
--     * Slot: partIdentification Description: A short designation of this recombinant part of the related biological material.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
-- # Class: "Collection" Description: "Set of products and services with some common characteristics."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: collectionDataProvider_id Description: The provider of the data of the collection.
-- # Class: "ProductOrService" Description: "An offering provided by a provider, which may be tangible (a product) or intangible (a service)."
--     * Slot: id Description: 
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Service" Description: "An intangible offering characterized by an activity, performance, or facilitation carried out by a provider to fulfill a user’s need."
--     * Slot: id Description: 
--     * Slot: modelSpecies Description: The species of the infected organism in the experiment.
--     * Slot: modelType Description: The specific name of the infected organism, including its modification if necessary.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Product" Description: "A tangible, physical item made available by a provider for use, consumption, or ownership transfer."
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Antibody" Description: "Protein that can bind to certain types of foreign bodies, such as pathogens."
--     * Slot: id Description: 
--     * Slot: productionSystem Description: The biological and technological methods and processes used to produce the antibody.
--     * Slot: antibodyPurifiedByAffinity Description: Indicates whether or not if the antibody was purified by affinity.
--     * Slot: specificityDocumented Description: Boolean value indicating whether the specificity of the product has been formally documented.
--     * Slot: targetedAntigen Description: Specific molecular structure or epitope recognized and bound by an antibody.
--     * Slot: antibodyType Description: The specification of the class of antibody based on its production method or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"
--     * Slot: antibodyCharacterizationObservation Description: A statement summarizing observed characteristics, behaviors, or findings derived from the antibody characterization process.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Hybridoma" Description: "An hybridoma that provides antibodies that can be related to a pathogen."
--     * Slot: id Description: 
--     * Slot: hybridomaDescription Description: The description of the hybridoma.
--     * Slot: productionSystem Description: The biological and technological methods and processes used to produce the antibody.
--     * Slot: antibodyPurifiedByAffinity Description: Indicates whether or not if the antibody was purified by affinity.
--     * Slot: specificityDocumented Description: Boolean value indicating whether the specificity of the product has been formally documented.
--     * Slot: targetedAntigen Description: Specific molecular structure or epitope recognized and bound by an antibody.
--     * Slot: antibodyType Description: The specification of the class of antibody based on its production method or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"
--     * Slot: antibodyCharacterizationObservation Description: A statement summarizing observed characteristics, behaviors, or findings derived from the antibody characterization process.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Protein" Description: "A protein as a derived product from a pathogen."
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "NucleicAcid" Description: "Nucleic acid related to a pathogen. It can be extracted or synthetic."
--     * Slot: id Description: 
--     * Slot: clonedNucleicAcid Description: Specification of the terms and parameters for transporting.
--     * Slot: regionEncompassedInThisProduct Description: The specific region encompassed in the product.
--     * Slot: mutationObserved Description: Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it contains mutations (no frameshift, no unexpected STOP codon) if set to true.
--     * Slot: observedMutations Description: The specific mutations that have been identified and documented in the nucleic acid sequence.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: sequencing Description: Refers to the level of sequencing performed on the nucleic acid. Possible values include 'Not sequenced' (no sequencing has been performed), 'Partly sequenced' (only a portion of the nucleic acid sequence has been determined), and 'Fully sequenced' (the entire nucleic acid sequence has been determined).
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: sequenceChecked Description: Tell whether or not the sequence of the product was controlled (compulsory for cloned products).
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: clonedIntoPlasmid_id Description: The plasmid into which the nucleic acid has been cloned.
--     * Slot: tagSequence_id Description: The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "DetectionKit" Description: "A detection kit for specific pathogens."
--     * Slot: id Description: 
--     * Slot: specificityDocumented Description: Boolean value indicating whether the specificity of the product has been formally documented.
--     * Slot: specificity Description: Details on the ability of a detection kit to correctly identify negative results, distinguishing between the target analyte and other substances without cross-reacting.
--     * Slot: targetedRegion Description: The specific area or sequence within the target analyte that the detection kit is designed to identify and interact with, ensuring accurate detection and analysis.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Bundle" Description: "A grouping of products and/or services intentionally combined into a single offering, typically to provide added value, convenience, or specific experimental utility."
--     * Slot: id Description: 
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Pathogen" Description: "Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Virus" Description: "The virus as a biological material."
--     * Slot: id Description: 
--     * Slot: contaminationWithCoInfectingViruses Description: A boolean value indicating whether there is contamination with co-infecting viruses.
--     * Slot: mycoplasmicContent Description: Indicates the presence of mycoplasma contamination within the sample.
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Bacterium" Description: "The bacterium as a biological material."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Fungus" Description: "The fungus as a biological material."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Protozoan" Description: "The protozoan as a biological material."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Viroid" Description: "The viroid as a biological material."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "Prion" Description: "The prion as a biological material."
--     * Slot: id Description: 
--     * Slot: cultivability Description: The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
--     * Slot: clinicalInformation Description: Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
--     * Slot: identificationTechnique Description: A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
--     * Slot: infectivity Description: Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
--     * Slot: infectivityTest Description: The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
--     * Slot: isolationTechnique Description: The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
--     * Slot: isolationConditions Description: The environmental and procedural conditions under which the pathogen was isolated.
--     * Slot: letterOfAuthority Description: Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
--     * Slot: passage Description: The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
--     * Slot: genomeSequencing Description: The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
--     * Slot: titer Description: The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
--     * Slot: shippingConditions Description: Specification of the terms and parameters for transporting.
--     * Slot: storageConditions Description: Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
--     * Slot: thirdPartyDistributionConsent Description: Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
--     * Slot: usageRestrictions Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
--     * Slot: preparationTechnique Description: The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
--     * Slot: accessPointUrl Description: The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
--     * Slot: refSku Description: The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
--     * Slot: unitDefinition Description: A short description of what will be delivered by ordering one unit of this item.
--     * Slot: unitCost Description: The cost per access for one unit as defined by the unit definition.
--     * Slot: unitCostCurrency Description: The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
--     * Slot: unitCostNote Description: A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
--     * Slot: qualityGrading Description: Information that permits to assess the quality level of what will be provided.
--     * Slot: biosafetyRestrictions Description: Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
--     * Slot: canBeUsedToProduceGmo Description: Indicates if the current service or product can be used to produce GMO.
--     * Slot: availability Description: The state or condition in which this item is accessible and ready for use or can be obtained.
--     * Slot: technicalRecommendation Description: Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
--     * Slot: internalReference Description: Any reference or indication to be used for local retrieval purpose.
--     * Slot: note Description: An aditional information as a textual comment.
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: biologicalMaterialOrigin_id Description: Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
--     * Slot: iataClassification_id Description: The corresponding International Air Transport Association (IATA)'s category for this Product.
--     * Slot: materialSafetyDataSheet_id Description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
--     * Slot: originator_id Description: The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
--     * Slot: category_id Description: The main category of the service or product.
--     * Slot: riskGroup_id Description: The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
--     * Slot: biosafetyLevel_id Description: The level of biocontainment required or applied in the facility where the biological agent is manipulated.
--     * Slot: provider_id Description: A provider of this product or service, as a specific organization.
--     * Slot: contactPoint_id Description: An information that allows someone to establish communication.
-- # Class: "MaterialSafetyDataSheet" Description: "A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product."
--     * Slot: id Description: 
--     * Slot: physicalChemicalProperties Description: Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage.
--     * Slot: hazardsIdentification Description: Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.
--     * Slot: firstAidMeasures Description: Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.
--     * Slot: fireFightingMeasures Description: Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.
--     * Slot: accidentalReleaseMeasures Description: Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.
--     * Slot: handlingAndStorage Description: Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.
--     * Slot: exposureControlsPersonalProtection Description: Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.
--     * Slot: stabilityAndReactivity Description: Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.
--     * Slot: toxicologicalInformation Description: Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure.
--     * Slot: ecologicalInformation Description: Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.
--     * Slot: disposalConsiderations Description: Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.
--     * Slot: transportInformation Description: Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.
--     * Slot: regulatoryInformation Description: Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.
--     * Slot: furtherInformation Description: Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: materialSafetyContact_id Description: The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.
-- # Class: "File" Description: "Digital document or record stored in a specific format that contains data or information."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Data" Description: "Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Document" Description: "Subclass of File representing textual or written files such as reports, manuals, or forms."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Audio" Description: "Subclass of File representing sound recordings or audio tracks."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Video" Description: "Subclass of File representing moving visual media, such as recordings, presentations, or movies."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "Image" Description: "Subclass of File representing visual content such as pictures, diagrams, or illustrations."
--     * Slot: id Description: 
--     * Slot: altText Description: An alternate text for the image, if the image cannot be displayed.
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: contentUrl Description: The web address or location where the file content is stored and can be accessed or downloaded.
--     * Slot: format Description: The file type or format that indicates how the data within the file is structured.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: license_id Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
-- # Class: "ContactPoint" Description: "Entity serving as focal point of information."
--     * Slot: id Description: 
--     * Slot: name Description: A word or set of words used to identify and refer to an entity.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: email Description: The email address.
--     * Slot: telephone Description: The telephone number.
--     * Slot: streetAddress Description: The building/apartment number and the street name.
--     * Slot: addressLocality Description: The locality in which the street address is, and which is in the region. e.g, the city.
--     * Slot: addressRegion Description: The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division.
--     * Slot: postalCode Description: The postal code.
--     * Slot: orcidId Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: addressCountry_id Description: The country as of  ISO 3166.
-- # Class: "License" Description: "The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: resourceUrl Description: The web address or location where the details or content is stored and can be accessed or downloaded.
--     * Slot: licensingOrAttribution Description: A text or html code that provides any related data sharing licence and/or attribution.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Certification" Description: "Assurance given by an independent certification body that a product, service or system meets the requirements of a standard."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: resourceUrl Description: The web address or location where the details or content is stored and can be accessed or downloaded.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "FundingSource" Description: "A program, grant, or project providing financial support for the access or use of a product or service, either fully or partially."
--     * Slot: id Description: 
--     * Slot: title Description: A name given to the resource.
--     * Slot: description Description: A short explanation of the characteristics, features, or nature of the current item.
--     * Slot: fundingProgram Description: Identifies the overarching financial framework, research initiative, or support mechanism that enables or contributes to the provision of a product or service. The value may correspond to a European funding framework (e.g. Horizon Europe), a specific research initiative (e.g. an EU project), or another public or private funding mechanism.
--     * Slot: grantNumber Description: A formal reference or agreement number assigned by the funding body.
--     * Slot: fundingPeriodStart Description: The date from which the financial mechanism is active or applicable to the supported product or service.
--     * Slot: fundingPeriodEnd Description: The date on which the financial mechanism ceases to apply to the supported product or service.
--     * Slot: eligibilityCriteria Description: Conditions under which individuals or organisations may benefit from the financial mechanism, including access rules, eligibility requirements, or geographical/institutional restrictions. May be expressed as text or as a link to a formal eligibility statement.
--     * Slot: dateIssued Description: Date of formal issuance (e.g., publication) of the resource.
--     * Slot: dateModified Description: Most recent date on which the resource was changed, updated or modified.
--     * Slot: funder_id Description: The organization providing the financial support.
--     * Slot: logo_id Description: A path or URL to the related logo.
-- # Class: "Resource_keyword" Description: ""
--     * Slot: Resource_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Resource_identifier" Description: ""
--     * Slot: Resource_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Resource_iri" Description: ""
--     * Slot: Resource_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Dataset_keyword" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Dataset_identifier" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Dataset_iri" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "DataService_servesDataset" Description: ""
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: servesDataset_id Description: A collection of data that this data service can distribute.
-- # Class: "DataService_keyword" Description: ""
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "DataService_identifier" Description: ""
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "DataService_iri" Description: ""
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Version_resource" Description: ""
--     * Slot: Version_id Description: Autocreated FK slot
--     * Slot: resource_id Description: Resource published or curated by a single agent.
-- # Class: "Version_keyword" Description: ""
--     * Slot: Version_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Version_identifier" Description: ""
--     * Slot: Version_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Version_iri" Description: ""
--     * Slot: Version_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Catalogue_keyword" Description: ""
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Catalogue_identifier" Description: ""
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Catalogue_iri" Description: ""
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Taxonomy_taxon" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: taxon_id Description: Scientifically classified group or entity within the reference taxonomy.
-- # Class: "Taxonomy_rank" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: rank_id Description: Relative level or position of the identified taxon in the taxonomy.
-- # Class: "Taxonomy_keyword" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Taxonomy_identifier" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Taxonomy_iri" Description: ""
--     * Slot: Taxonomy_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "DataProvider_providedEntityType" Description: ""
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: providedEntityType Description: Identifies the type of entity (ontology class) described by the response to a query. Values should be expressed as IRIs (e.g., from an ontology).
-- # Class: "DataProvider_servesDataset" Description: ""
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: servesDataset_id Description: A collection of data that this data service can distribute.
-- # Class: "DataProvider_keyword" Description: ""
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "DataProvider_identifier" Description: ""
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "DataProvider_iri" Description: ""
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "PathogenIdentification_hostType" Description: ""
--     * Slot: PathogenIdentification_id Description: Autocreated FK slot
--     * Slot: hostType Description: Indication of the possible host(s) for the identified pathogens among the listed main categories.
-- # Class: "PathogenIdentification_keyword" Description: ""
--     * Slot: PathogenIdentification_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "PathogenIdentification_identifier" Description: ""
--     * Slot: PathogenIdentification_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "PathogenIdentification_iri" Description: ""
--     * Slot: PathogenIdentification_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Publication_keyword" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Publication_identifier" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Publication_iri" Description: ""
--     * Slot: Publication_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Vocabulary_term" Description: ""
--     * Slot: Vocabulary_id Description: Autocreated FK slot
--     * Slot: term_id Description: The terms related to this vocabulary.
-- # Class: "Vocabulary_keyword" Description: ""
--     * Slot: Vocabulary_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Vocabulary_identifier" Description: ""
--     * Slot: Vocabulary_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Vocabulary_iri" Description: ""
--     * Slot: Vocabulary_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Term_keyword" Description: ""
--     * Slot: Term_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Term_identifier" Description: ""
--     * Slot: Term_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Term_iri" Description: ""
--     * Slot: Term_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "CommonName_alternateName" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "CommonName_sourceOfInformation" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information.
-- # Class: "CommonName_keyword" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "CommonName_identifier" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "CommonName_iri" Description: ""
--     * Slot: CommonName_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "VirusName_alternateName" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "VirusName_sourceOfInformation" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information.
-- # Class: "VirusName_keyword" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "VirusName_identifier" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "VirusName_iri" Description: ""
--     * Slot: VirusName_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "AlternateName_alternateName" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "AlternateName_sourceOfInformation" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information.
-- # Class: "AlternateName_keyword" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "AlternateName_identifier" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "AlternateName_iri" Description: ""
--     * Slot: AlternateName_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "RiskGroup_keyword" Description: ""
--     * Slot: RiskGroup_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "RiskGroup_identifier" Description: ""
--     * Slot: RiskGroup_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "RiskGroup_iri" Description: ""
--     * Slot: RiskGroup_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "BiosafetyLevel_keyword" Description: ""
--     * Slot: BiosafetyLevel_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "BiosafetyLevel_identifier" Description: ""
--     * Slot: BiosafetyLevel_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "BiosafetyLevel_iri" Description: ""
--     * Slot: BiosafetyLevel_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Doi_keyword" Description: ""
--     * Slot: Doi_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Doi_identifier" Description: ""
--     * Slot: Doi_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Doi_iri" Description: ""
--     * Slot: Doi_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Journal_keyword" Description: ""
--     * Slot: Journal_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Journal_identifier" Description: ""
--     * Slot: Journal_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Journal_iri" Description: ""
--     * Slot: Journal_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "PdbReference_keyword" Description: ""
--     * Slot: PdbReference_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "PdbReference_identifier" Description: ""
--     * Slot: PdbReference_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "PdbReference_iri" Description: ""
--     * Slot: PdbReference_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Keyword_keyword" Description: ""
--     * Slot: Keyword_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Keyword_identifier" Description: ""
--     * Slot: Keyword_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Keyword_iri" Description: ""
--     * Slot: Keyword_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "TagSequence_keyword" Description: ""
--     * Slot: TagSequence_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "TagSequence_identifier" Description: ""
--     * Slot: TagSequence_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "TagSequence_iri" Description: ""
--     * Slot: TagSequence_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "SpecialFeature_keyword" Description: ""
--     * Slot: SpecialFeature_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "SpecialFeature_identifier" Description: ""
--     * Slot: SpecialFeature_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "SpecialFeature_iri" Description: ""
--     * Slot: SpecialFeature_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ExpressionVector_keyword" Description: ""
--     * Slot: ExpressionVector_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ExpressionVector_identifier" Description: ""
--     * Slot: ExpressionVector_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ExpressionVector_iri" Description: ""
--     * Slot: ExpressionVector_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "PlasmidSelection_keyword" Description: ""
--     * Slot: PlasmidSelection_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "PlasmidSelection_identifier" Description: ""
--     * Slot: PlasmidSelection_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "PlasmidSelection_iri" Description: ""
--     * Slot: PlasmidSelection_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "PropagationHost_keyword" Description: ""
--     * Slot: PropagationHost_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "PropagationHost_identifier" Description: ""
--     * Slot: PropagationHost_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "PropagationHost_iri" Description: ""
--     * Slot: PropagationHost_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "TransmissionMethod_keyword" Description: ""
--     * Slot: TransmissionMethod_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "TransmissionMethod_identifier" Description: ""
--     * Slot: TransmissionMethod_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "TransmissionMethod_iri" Description: ""
--     * Slot: TransmissionMethod_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ProductionCellLine_keyword" Description: ""
--     * Slot: ProductionCellLine_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ProductionCellLine_identifier" Description: ""
--     * Slot: ProductionCellLine_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ProductionCellLine_iri" Description: ""
--     * Slot: ProductionCellLine_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ProductCategory_keyword" Description: ""
--     * Slot: ProductCategory_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ProductCategory_identifier" Description: ""
--     * Slot: ProductCategory_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ProductCategory_iri" Description: ""
--     * Slot: ProductCategory_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "IsolationHost_keyword" Description: ""
--     * Slot: IsolationHost_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "IsolationHost_identifier" Description: ""
--     * Slot: IsolationHost_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "IsolationHost_iri" Description: ""
--     * Slot: IsolationHost_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "GeographicalOrigin_keyword" Description: ""
--     * Slot: GeographicalOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "GeographicalOrigin_identifier" Description: ""
--     * Slot: GeographicalOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "GeographicalOrigin_iri" Description: ""
--     * Slot: GeographicalOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "IplcOrigin_keyword" Description: ""
--     * Slot: IplcOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "IplcOrigin_identifier" Description: ""
--     * Slot: IplcOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "IplcOrigin_iri" Description: ""
--     * Slot: IplcOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Country_keyword" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Country_identifier" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Country_iri" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "IataClassification_keyword" Description: ""
--     * Slot: IataClassification_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "IataClassification_identifier" Description: ""
--     * Slot: IataClassification_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "IataClassification_iri" Description: ""
--     * Slot: IataClassification_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Variant_alternateName" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "Variant_sourceOfInformation" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: sourceOfInformation Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information.
-- # Class: "Variant_keyword" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Variant_identifier" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Variant_iri" Description: ""
--     * Slot: Variant_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "TaxonomicRank_taxonomy" Description: ""
--     * Slot: TaxonomicRank_id Description: Autocreated FK slot
--     * Slot: taxonomy_id Description: The taxonomy release(s) in which this entity exists.
-- # Class: "TaxonomicRank_keyword" Description: ""
--     * Slot: TaxonomicRank_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "TaxonomicRank_identifier" Description: ""
--     * Slot: TaxonomicRank_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "TaxonomicRank_iri" Description: ""
--     * Slot: TaxonomicRank_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Taxon_taxonomy" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: taxonomy_id Description: The taxonomy release(s) in which this entity exists.
-- # Class: "Taxon_externalEquivalentTaxon" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: externalEquivalentTaxon_id Description: Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI).
-- # Class: "Taxon_alternateName" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "Taxon_previouslyKnownAs" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: previouslyKnownAs_id Description: Any historic version of this taxon having a different name.
-- # Class: "Taxon_keyword" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Taxon_identifier" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Taxon_iri" Description: ""
--     * Slot: Taxon_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ClinicalGroup_alternateName" Description: ""
--     * Slot: ClinicalGroup_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "ClinicalGroup_taxon" Description: ""
--     * Slot: ClinicalGroup_id Description: Autocreated FK slot
--     * Slot: taxon_id Description: Scientifically classified group or entity within the reference taxonomy.
-- # Class: "ClinicalGroup_keyword" Description: ""
--     * Slot: ClinicalGroup_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ClinicalGroup_identifier" Description: ""
--     * Slot: ClinicalGroup_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ClinicalGroup_iri" Description: ""
--     * Slot: ClinicalGroup_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ExternalRelatedReference_keyword" Description: ""
--     * Slot: ExternalRelatedReference_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ExternalRelatedReference_identifier" Description: ""
--     * Slot: ExternalRelatedReference_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ExternalRelatedReference_iri" Description: ""
--     * Slot: ExternalRelatedReference_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Sequence_sequenceReference" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retrieve the sequence information from a sequence provider.
-- # Class: "Sequence_keyword" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Sequence_identifier" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Sequence_iri" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "SequenceReference_keyword" Description: ""
--     * Slot: SequenceReference_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "SequenceReference_identifier" Description: ""
--     * Slot: SequenceReference_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "SequenceReference_iri" Description: ""
--     * Slot: SequenceReference_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "PersonOrOrganization_keyword" Description: ""
--     * Slot: PersonOrOrganization_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "PersonOrOrganization_identifier" Description: ""
--     * Slot: PersonOrOrganization_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "PersonOrOrganization_iri" Description: ""
--     * Slot: PersonOrOrganization_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Person_keyword" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Person_identifier" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Person_iri" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Organization_alternateName" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "Organization_keyword" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Organization_identifier" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Organization_iri" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ReasearchInfrastructure_alternateName" Description: ""
--     * Slot: ReasearchInfrastructure_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "ReasearchInfrastructure_keyword" Description: ""
--     * Slot: ReasearchInfrastructure_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ReasearchInfrastructure_identifier" Description: ""
--     * Slot: ReasearchInfrastructure_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ReasearchInfrastructure_iri" Description: ""
--     * Slot: ReasearchInfrastructure_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Provider_memberOfRi" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: memberOfRi_id Description: The research infrastructure of which this organization is a member.
-- # Class: "Provider_alternateName" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: alternateName_id Description: Any other name under which the entity can be known.
-- # Class: "Provider_keyword" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Provider_identifier" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Provider_iri" Description: ""
--     * Slot: Provider_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Originator_keyword" Description: ""
--     * Slot: Originator_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Originator_identifier" Description: ""
--     * Slot: Originator_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Originator_iri" Description: ""
--     * Slot: Originator_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "BiologicalMaterialOrigin_biologicalPartOrigin" Description: ""
--     * Slot: BiologicalMaterialOrigin_id Description: Autocreated FK slot
--     * Slot: biologicalPartOrigin_id Description: Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.
-- # Class: "BiologicalMaterialOrigin_keyword" Description: ""
--     * Slot: BiologicalMaterialOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "BiologicalMaterialOrigin_identifier" Description: ""
--     * Slot: BiologicalMaterialOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "BiologicalMaterialOrigin_iri" Description: ""
--     * Slot: BiologicalMaterialOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "BiologicalPartOrigin_keyword" Description: ""
--     * Slot: BiologicalPartOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "BiologicalPartOrigin_identifier" Description: ""
--     * Slot: BiologicalPartOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "BiologicalPartOrigin_iri" Description: ""
--     * Slot: BiologicalPartOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "NaturalPartOrigin_keyword" Description: ""
--     * Slot: NaturalPartOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "NaturalPartOrigin_identifier" Description: ""
--     * Slot: NaturalPartOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "NaturalPartOrigin_iri" Description: ""
--     * Slot: NaturalPartOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "SyntheticPartOrigin_keyword" Description: ""
--     * Slot: SyntheticPartOrigin_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "SyntheticPartOrigin_identifier" Description: ""
--     * Slot: SyntheticPartOrigin_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "SyntheticPartOrigin_iri" Description: ""
--     * Slot: SyntheticPartOrigin_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "RecombinantPartIdentification_sequence" Description: ""
--     * Slot: RecombinantPartIdentification_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "RecombinantPartIdentification_keyword" Description: ""
--     * Slot: RecombinantPartIdentification_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "RecombinantPartIdentification_identifier" Description: ""
--     * Slot: RecombinantPartIdentification_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "RecombinantPartIdentification_iri" Description: ""
--     * Slot: RecombinantPartIdentification_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Collection_collectionItem" Description: ""
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: collectionItem_id Description: An item of the collection.
-- # Class: "Collection_keyword" Description: ""
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Collection_identifier" Description: ""
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Collection_iri" Description: ""
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ProductOrService_additionalCategory" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "ProductOrService_pathogenIdentification" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "ProductOrService_doi" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "ProductOrService_collection" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "ProductOrService_keywords" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "ProductOrService_complementaryDocument" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "ProductOrService_productPicture" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "ProductOrService_externalRelatedReference" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "ProductOrService_certification" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "ProductOrService_fundingSource" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "ProductOrService_keyword" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ProductOrService_identifier" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ProductOrService_iri" Description: ""
--     * Slot: ProductOrService_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Service_additionalCategory" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Service_pathogenIdentification" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Service_doi" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Service_collection" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Service_keywords" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Service_complementaryDocument" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Service_productPicture" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Service_externalRelatedReference" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Service_certification" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Service_fundingSource" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Service_keyword" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Service_identifier" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Service_iri" Description: ""
--     * Slot: Service_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Product_additionalCategory" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Product_pathogenIdentification" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Product_doi" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Product_collection" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Product_keywords" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Product_complementaryDocument" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Product_productPicture" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Product_externalRelatedReference" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Product_certification" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Product_fundingSource" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Product_keyword" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Product_identifier" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Product_iri" Description: ""
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Antibody_sequenceReference" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retrieve the sequence information from a sequence provider.
-- # Class: "Antibody_antibodyCharacterizationMethod" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: antibodyCharacterizationMethod Description: A method used to determine the specificity, affinity, or functionality of an antibody or antiserum.
-- # Class: "Antibody_additionalCategory" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Antibody_pathogenIdentification" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Antibody_doi" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Antibody_collection" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Antibody_keywords" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Antibody_complementaryDocument" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Antibody_productPicture" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Antibody_externalRelatedReference" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Antibody_certification" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Antibody_fundingSource" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Antibody_keyword" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Antibody_identifier" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Antibody_iri" Description: ""
--     * Slot: Antibody_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Hybridoma_sequenceReference" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: sequenceReference_id Description: A reference that permits to retrieve the sequence information from a sequence provider.
-- # Class: "Hybridoma_antibodyCharacterizationMethod" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: antibodyCharacterizationMethod Description: A method used to determine the specificity, affinity, or functionality of an antibody or antiserum.
-- # Class: "Hybridoma_additionalCategory" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Hybridoma_pathogenIdentification" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Hybridoma_doi" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Hybridoma_collection" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Hybridoma_keywords" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Hybridoma_complementaryDocument" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Hybridoma_productPicture" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Hybridoma_externalRelatedReference" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Hybridoma_certification" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Hybridoma_fundingSource" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Hybridoma_keyword" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Hybridoma_identifier" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Hybridoma_iri" Description: ""
--     * Slot: Hybridoma_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Protein_sequence" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Protein_relatedPdb" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: relatedPdb_id Description: Identifier for 3D structural data as per the PDB (Protein Data Bank) database.
-- # Class: "Protein_specialFeature" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: specialFeature_id Description: Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
-- # Class: "Protein_tagSequence" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: tagSequence_id Description: The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids.
-- # Class: "Protein_domain" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: domain Description: A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function.
-- # Class: "Protein_expressedAs" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: expressedAs Description: Refers to the form in which the protein is produced and manifested in a biological system. Possible values include 'Soluble' (proteins that are dissolved in the cellular or extracellular fluid) and 'Inclusion bodies' (aggregated proteins that are insoluble and form within the cell).
-- # Class: "Protein_inclusionBodiesType" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: inclusionBodiesType Description: Refers to the state of aggregated proteins within a cell. Possible values include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded' (proteins have been processed to regain their functional, active conformation).
-- # Class: "Protein_expressionSystem" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: expressionSystem Description: The host organism or cellular environment used to produce a protein from a specific gene. Possible values include 'E. coli' (bacterial system), 'Insect cells' (using baculovirus vectors), and 'Mammalian cells' (mammalian cell lines).
-- # Class: "Protein_functionalCharacterization" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: functionalCharacterization Description: The process of determining and describing the specific biological activities and roles of a protein. Possible values include 'Functionally characterized' (the protein's functions have been identified and described) and 'No functional characterization' (the protein's functions have not been identified or described).
-- # Class: "Protein_functionalAndTechnicalDescription" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: functionalAndTechnicalDescription Description: Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.
-- # Class: "Protein_proteinPurification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: proteinPurification Description: Refers to the degree of purity achieved for a protein sample. Possible values include '>95%' (the protein is highly purified, with more than 95% purity) and 'Unpurified expression host lysate or partly purified protein' (the protein is either unpurified and present in the host cell lysate or only partially purified).
-- # Class: "Protein_tagStatusOfTheSolubilizedProtein" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: tagStatusOfTheSolubilizedProtein Description: Indicates the presence and condition of a tag on the protein after solubilization. Possible values include 'Uncleaved Tag' (the tag is still attached to the protein), 'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein does not have a tag).
-- # Class: "Protein_typeOfFunctionalCharacterization" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: typeOfFunctionalCharacterization Description: Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include 'Enzymatic' (the protein has been characterized for its enzyme activity) and 'Antigenic' (the protein has been characterized for its ability to elicit an immune response).
-- # Class: "Protein_additionalCategory" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Protein_pathogenIdentification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Protein_doi" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Protein_collection" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Protein_keywords" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Protein_complementaryDocument" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Protein_productPicture" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Protein_externalRelatedReference" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Protein_certification" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Protein_fundingSource" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Protein_keyword" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Protein_identifier" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Protein_iri" Description: ""
--     * Slot: Protein_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "NucleicAcid_genBankFileOfTheConstruct" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: genBankFileOfTheConstruct_id Description: A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct.
-- # Class: "NucleicAcid_sequence" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "NucleicAcid_plasmidSelection" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: plasmidSelection_id Description: Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid.
-- # Class: "NucleicAcid_additionalCategory" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "NucleicAcid_pathogenIdentification" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "NucleicAcid_doi" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "NucleicAcid_collection" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "NucleicAcid_keywords" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "NucleicAcid_complementaryDocument" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "NucleicAcid_productPicture" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "NucleicAcid_externalRelatedReference" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "NucleicAcid_certification" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "NucleicAcid_fundingSource" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "NucleicAcid_keyword" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "NucleicAcid_identifier" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "NucleicAcid_iri" Description: ""
--     * Slot: NucleicAcid_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "DetectionKit_standardOperatingProcedureFile" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: standardOperatingProcedureFile_id Description: The related standard operating procedure file (SOP).
-- # Class: "DetectionKit_additionalCategory" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "DetectionKit_pathogenIdentification" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "DetectionKit_doi" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "DetectionKit_collection" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "DetectionKit_keywords" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "DetectionKit_complementaryDocument" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "DetectionKit_productPicture" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "DetectionKit_externalRelatedReference" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "DetectionKit_certification" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "DetectionKit_fundingSource" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "DetectionKit_keyword" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "DetectionKit_identifier" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "DetectionKit_iri" Description: ""
--     * Slot: DetectionKit_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Bundle_itemsOfTheBundle" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: itemsOfTheBundle_id Description: Specifies the constituent products and/or services that are part of the bundle.
-- # Class: "Bundle_additionalCategory" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Bundle_pathogenIdentification" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Bundle_doi" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Bundle_collection" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Bundle_keywords" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Bundle_complementaryDocument" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Bundle_productPicture" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Bundle_externalRelatedReference" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Bundle_certification" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Bundle_fundingSource" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Bundle_keyword" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Bundle_identifier" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Bundle_iri" Description: ""
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Pathogen_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Pathogen_isolationHost" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Pathogen_productionCellLine" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Pathogen_propagationHost" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Pathogen_transmissionMethod" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Pathogen_sequence" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Pathogen_additionalCategory" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Pathogen_pathogenIdentification" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Pathogen_doi" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Pathogen_collection" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Pathogen_keywords" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Pathogen_complementaryDocument" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Pathogen_productPicture" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Pathogen_externalRelatedReference" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Pathogen_certification" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Pathogen_fundingSource" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Pathogen_keyword" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Pathogen_identifier" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Pathogen_iri" Description: ""
--     * Slot: Pathogen_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Virus_coInfectingViruses" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: coInfectingViruses_id Description: Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.
-- # Class: "Virus_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Virus_isolationHost" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Virus_productionCellLine" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Virus_propagationHost" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Virus_transmissionMethod" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Virus_sequence" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Virus_additionalCategory" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Virus_pathogenIdentification" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Virus_doi" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Virus_collection" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Virus_keywords" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Virus_complementaryDocument" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Virus_productPicture" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Virus_externalRelatedReference" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Virus_certification" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Virus_fundingSource" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Virus_keyword" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Virus_identifier" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Virus_iri" Description: ""
--     * Slot: Virus_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Bacterium_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Bacterium_isolationHost" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Bacterium_productionCellLine" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Bacterium_propagationHost" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Bacterium_transmissionMethod" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Bacterium_sequence" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Bacterium_additionalCategory" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Bacterium_pathogenIdentification" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Bacterium_doi" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Bacterium_collection" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Bacterium_keywords" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Bacterium_complementaryDocument" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Bacterium_productPicture" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Bacterium_externalRelatedReference" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Bacterium_certification" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Bacterium_fundingSource" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Bacterium_keyword" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Bacterium_identifier" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Bacterium_iri" Description: ""
--     * Slot: Bacterium_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Fungus_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Fungus_isolationHost" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Fungus_productionCellLine" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Fungus_propagationHost" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Fungus_transmissionMethod" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Fungus_sequence" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Fungus_additionalCategory" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Fungus_pathogenIdentification" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Fungus_doi" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Fungus_collection" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Fungus_keywords" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Fungus_complementaryDocument" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Fungus_productPicture" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Fungus_externalRelatedReference" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Fungus_certification" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Fungus_fundingSource" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Fungus_keyword" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Fungus_identifier" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Fungus_iri" Description: ""
--     * Slot: Fungus_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Protozoan_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Protozoan_isolationHost" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Protozoan_productionCellLine" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Protozoan_propagationHost" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Protozoan_transmissionMethod" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Protozoan_sequence" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Protozoan_additionalCategory" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Protozoan_pathogenIdentification" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Protozoan_doi" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Protozoan_collection" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Protozoan_keywords" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Protozoan_complementaryDocument" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Protozoan_productPicture" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Protozoan_externalRelatedReference" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Protozoan_certification" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Protozoan_fundingSource" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Protozoan_keyword" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Protozoan_identifier" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Protozoan_iri" Description: ""
--     * Slot: Protozoan_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Viroid_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Viroid_isolationHost" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Viroid_productionCellLine" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Viroid_propagationHost" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Viroid_transmissionMethod" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Viroid_sequence" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Viroid_additionalCategory" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Viroid_pathogenIdentification" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Viroid_doi" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Viroid_collection" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Viroid_keywords" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Viroid_complementaryDocument" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Viroid_productPicture" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Viroid_externalRelatedReference" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Viroid_certification" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Viroid_fundingSource" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Viroid_keyword" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Viroid_identifier" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Viroid_iri" Description: ""
--     * Slot: Viroid_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Prion_suspectedEpidemiologicalOrigin" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: suspectedEpidemiologicalOrigin_id Description: The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
-- # Class: "Prion_isolationHost" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: isolationHost_id Description: The host organism from which the pathogen was originally isolated.
-- # Class: "Prion_productionCellLine" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: productionCellLine_id Description: The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
-- # Class: "Prion_propagationHost" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: propagationHost_id Description: The host organism that propagates the pathogen.
-- # Class: "Prion_transmissionMethod" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: transmissionMethod_id Description: The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
-- # Class: "Prion_sequence" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The related sequence information from a sequence provider or in fasta format.
-- # Class: "Prion_additionalCategory" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: additionalCategory_id Description: Any category apart from its main category in which this product or service can fit.
-- # Class: "Prion_pathogenIdentification" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: pathogenIdentification_id Description: The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
-- # Class: "Prion_doi" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: doi_id Description: A Digital Object Identifier (DOI) that can be related.
-- # Class: "Prion_collection" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: collection_id Description: The collection(s) to which belongs this item.
-- # Class: "Prion_keywords" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: keywords_id Description: List of terms used to tag and categorize this Item.
-- # Class: "Prion_complementaryDocument" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: complementaryDocument_id Description: Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
-- # Class: "Prion_productPicture" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: productPicture_id Description: A picture that can represent the item.
-- # Class: "Prion_externalRelatedReference" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: externalRelatedReference_id Description: A reference that permits to retrieve another related item from an external provider.
-- # Class: "Prion_certification" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: certification_id Description: Any certification related to the current product or service; e.g., ISO certification.
-- # Class: "Prion_fundingSource" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: fundingSource_id Description: A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
-- # Class: "Prion_keyword" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Prion_identifier" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Prion_iri" Description: ""
--     * Slot: Prion_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "MaterialSafetyDataSheet_keyword" Description: ""
--     * Slot: MaterialSafetyDataSheet_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "MaterialSafetyDataSheet_identifier" Description: ""
--     * Slot: MaterialSafetyDataSheet_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "MaterialSafetyDataSheet_iri" Description: ""
--     * Slot: MaterialSafetyDataSheet_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "File_keyword" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "File_identifier" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "File_iri" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Data_keyword" Description: ""
--     * Slot: Data_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Data_identifier" Description: ""
--     * Slot: Data_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Data_iri" Description: ""
--     * Slot: Data_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Document_keyword" Description: ""
--     * Slot: Document_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Document_identifier" Description: ""
--     * Slot: Document_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Document_iri" Description: ""
--     * Slot: Document_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Audio_keyword" Description: ""
--     * Slot: Audio_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Audio_identifier" Description: ""
--     * Slot: Audio_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Audio_iri" Description: ""
--     * Slot: Audio_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Video_keyword" Description: ""
--     * Slot: Video_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Video_identifier" Description: ""
--     * Slot: Video_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Video_iri" Description: ""
--     * Slot: Video_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Image_keyword" Description: ""
--     * Slot: Image_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Image_identifier" Description: ""
--     * Slot: Image_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Image_iri" Description: ""
--     * Slot: Image_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "ContactPoint_keyword" Description: ""
--     * Slot: ContactPoint_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "ContactPoint_identifier" Description: ""
--     * Slot: ContactPoint_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "ContactPoint_iri" Description: ""
--     * Slot: ContactPoint_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "License_keyword" Description: ""
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "License_identifier" Description: ""
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "License_iri" Description: ""
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "Certification_certificationDocument" Description: ""
--     * Slot: Certification_id Description: Autocreated FK slot
--     * Slot: certificationDocument_id Description: The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.
-- # Class: "Certification_keyword" Description: ""
--     * Slot: Certification_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "Certification_identifier" Description: ""
--     * Slot: Certification_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "Certification_iri" Description: ""
--     * Slot: Certification_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
-- # Class: "FundingSource_keyword" Description: ""
--     * Slot: FundingSource_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: "FundingSource_identifier" Description: ""
--     * Slot: FundingSource_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource being described or cataloged.
-- # Class: "FundingSource_iri" Description: ""
--     * Slot: FundingSource_id Description: Autocreated FK slot
--     * Slot: iri Description: International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.

CREATE TABLE "Resource" (
	id INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataService" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	"endpointUrl" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "Version" (
	id INTEGER NOT NULL, 
	version TEXT NOT NULL, 
	"versionOf" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "Catalogue" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "ExternalRelatedReference" (
	id INTEGER NOT NULL, 
	reference TEXT NOT NULL, 
	"referenceLabel" TEXT NOT NULL, 
	"referenceProviderPrefix" TEXT NOT NULL, 
	"referenceProviderName" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL, 
	"sequenceFasta" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceReference" (
	id INTEGER NOT NULL, 
	"accessionNumber" TEXT NOT NULL, 
	"sequenceProvider" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "BiologicalMaterialOrigin" (
	id INTEGER NOT NULL, 
	"recombinantMaterial" BOOLEAN NOT NULL, 
	"biologicalSourceType" BOOLEAN NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "RecombinantPartIdentification" (
	id INTEGER NOT NULL, 
	"partIdentification" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "Image" (
	id INTEGER NOT NULL, 
	"altText" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "License" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	"resourceUrl" TEXT, 
	"licensingOrAttribution" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "DataProvider" (
	id INTEGER NOT NULL, 
	"loginRequestMethod" TEXT, 
	"loginUrl" TEXT, 
	"loginTokenName" TEXT, 
	"queryMethod" TEXT NOT NULL, 
	"contentType" TEXT NOT NULL, 
	weight INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	"endpointUrl" TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "BiologicalPartOrigin" (
	id INTEGER NOT NULL, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "SyntheticPartOrigin" (
	id INTEGER NOT NULL, 
	"modificationsFromTheReferenceSequences" BOOLEAN NOT NULL, 
	"descriptionOfModificationsMadeFromTheReferenceSequences" TEXT, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "File" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Data" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Document" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Audio" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Video" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"contentUrl" TEXT NOT NULL, 
	format TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	license_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(license_id) REFERENCES "License" (id)
);
CREATE TABLE "Certification" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	"resourceUrl" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Resource_keyword" (
	"Resource_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Resource_id", keyword), 
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE TABLE "Resource_identifier" (
	"Resource_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Resource_id", identifier), 
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE TABLE "Resource_iri" (
	"Resource_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Resource_id", iri), 
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE TABLE "Dataset_keyword" (
	"Dataset_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Dataset_id", keyword), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_identifier" (
	"Dataset_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Dataset_id", identifier), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_iri" (
	"Dataset_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Dataset_id", iri), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "DataService_servesDataset" (
	"DataService_id" INTEGER, 
	"servesDataset_id" INTEGER, 
	PRIMARY KEY ("DataService_id", "servesDataset_id"), 
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id), 
	FOREIGN KEY("servesDataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "DataService_keyword" (
	"DataService_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("DataService_id", keyword), 
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE TABLE "DataService_identifier" (
	"DataService_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("DataService_id", identifier), 
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE TABLE "DataService_iri" (
	"DataService_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("DataService_id", iri), 
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE TABLE "Version_resource" (
	"Version_id" INTEGER, 
	resource_id INTEGER, 
	PRIMARY KEY ("Version_id", resource_id), 
	FOREIGN KEY("Version_id") REFERENCES "Version" (id), 
	FOREIGN KEY(resource_id) REFERENCES "Resource" (id)
);
CREATE TABLE "Version_keyword" (
	"Version_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Version_id", keyword), 
	FOREIGN KEY("Version_id") REFERENCES "Version" (id)
);
CREATE TABLE "Version_identifier" (
	"Version_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Version_id", identifier), 
	FOREIGN KEY("Version_id") REFERENCES "Version" (id)
);
CREATE TABLE "Version_iri" (
	"Version_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Version_id", iri), 
	FOREIGN KEY("Version_id") REFERENCES "Version" (id)
);
CREATE TABLE "Catalogue_keyword" (
	"Catalogue_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Catalogue_id", keyword), 
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);
CREATE TABLE "Catalogue_identifier" (
	"Catalogue_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Catalogue_id", identifier), 
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);
CREATE TABLE "Catalogue_iri" (
	"Catalogue_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Catalogue_id", iri), 
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);
CREATE TABLE "ExternalRelatedReference_keyword" (
	"ExternalRelatedReference_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ExternalRelatedReference_id", keyword), 
	FOREIGN KEY("ExternalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "ExternalRelatedReference_identifier" (
	"ExternalRelatedReference_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ExternalRelatedReference_id", identifier), 
	FOREIGN KEY("ExternalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "ExternalRelatedReference_iri" (
	"ExternalRelatedReference_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ExternalRelatedReference_id", iri), 
	FOREIGN KEY("ExternalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "Sequence_sequenceReference" (
	"Sequence_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Sequence_id", "sequenceReference_id"), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "Sequence_keyword" (
	"Sequence_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Sequence_id", keyword), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id)
);
CREATE TABLE "Sequence_identifier" (
	"Sequence_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Sequence_id", identifier), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id)
);
CREATE TABLE "Sequence_iri" (
	"Sequence_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Sequence_id", iri), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id)
);
CREATE TABLE "SequenceReference_keyword" (
	"SequenceReference_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("SequenceReference_id", keyword), 
	FOREIGN KEY("SequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "SequenceReference_identifier" (
	"SequenceReference_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("SequenceReference_id", identifier), 
	FOREIGN KEY("SequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "SequenceReference_iri" (
	"SequenceReference_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("SequenceReference_id", iri), 
	FOREIGN KEY("SequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "BiologicalMaterialOrigin_keyword" (
	"BiologicalMaterialOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("BiologicalMaterialOrigin_id", keyword), 
	FOREIGN KEY("BiologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id)
);
CREATE TABLE "BiologicalMaterialOrigin_identifier" (
	"BiologicalMaterialOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("BiologicalMaterialOrigin_id", identifier), 
	FOREIGN KEY("BiologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id)
);
CREATE TABLE "BiologicalMaterialOrigin_iri" (
	"BiologicalMaterialOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("BiologicalMaterialOrigin_id", iri), 
	FOREIGN KEY("BiologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id)
);
CREATE TABLE "RecombinantPartIdentification_sequence" (
	"RecombinantPartIdentification_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("RecombinantPartIdentification_id", sequence_id), 
	FOREIGN KEY("RecombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RecombinantPartIdentification_keyword" (
	"RecombinantPartIdentification_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("RecombinantPartIdentification_id", keyword), 
	FOREIGN KEY("RecombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "RecombinantPartIdentification_identifier" (
	"RecombinantPartIdentification_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("RecombinantPartIdentification_id", identifier), 
	FOREIGN KEY("RecombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "RecombinantPartIdentification_iri" (
	"RecombinantPartIdentification_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("RecombinantPartIdentification_id", iri), 
	FOREIGN KEY("RecombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "Image_keyword" (
	"Image_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Image_id", keyword), 
	FOREIGN KEY("Image_id") REFERENCES "Image" (id)
);
CREATE TABLE "Image_identifier" (
	"Image_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Image_id", identifier), 
	FOREIGN KEY("Image_id") REFERENCES "Image" (id)
);
CREATE TABLE "Image_iri" (
	"Image_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Image_id", iri), 
	FOREIGN KEY("Image_id") REFERENCES "Image" (id)
);
CREATE TABLE "License_keyword" (
	"License_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("License_id", keyword), 
	FOREIGN KEY("License_id") REFERENCES "License" (id)
);
CREATE TABLE "License_identifier" (
	"License_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("License_id", identifier), 
	FOREIGN KEY("License_id") REFERENCES "License" (id)
);
CREATE TABLE "License_iri" (
	"License_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("License_id", iri), 
	FOREIGN KEY("License_id") REFERENCES "License" (id)
);
CREATE TABLE "Taxonomy" (
	id INTEGER NOT NULL, 
	version TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"taxonDataProvider_id" INTEGER, 
	"versionDataProvider_id" INTEGER NOT NULL, 
	"rankDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("taxonDataProvider_id") REFERENCES "DataProvider" (id), 
	FOREIGN KEY("versionDataProvider_id") REFERENCES "DataProvider" (id), 
	FOREIGN KEY("rankDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "Vocabulary" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"termDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("termDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "Collection" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"collectionDataProvider_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("collectionDataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "DataProvider_providedEntityType" (
	"DataProvider_id" INTEGER, 
	"providedEntityType" TEXT NOT NULL, 
	PRIMARY KEY ("DataProvider_id", "providedEntityType"), 
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "DataProvider_servesDataset" (
	"DataProvider_id" INTEGER, 
	"servesDataset_id" INTEGER, 
	PRIMARY KEY ("DataProvider_id", "servesDataset_id"), 
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id), 
	FOREIGN KEY("servesDataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "DataProvider_keyword" (
	"DataProvider_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("DataProvider_id", keyword), 
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "DataProvider_identifier" (
	"DataProvider_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("DataProvider_id", identifier), 
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "DataProvider_iri" (
	"DataProvider_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("DataProvider_id", iri), 
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE TABLE "BiologicalMaterialOrigin_biologicalPartOrigin" (
	"BiologicalMaterialOrigin_id" INTEGER, 
	"biologicalPartOrigin_id" INTEGER NOT NULL, 
	PRIMARY KEY ("BiologicalMaterialOrigin_id", "biologicalPartOrigin_id"), 
	FOREIGN KEY("BiologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("biologicalPartOrigin_id") REFERENCES "BiologicalPartOrigin" (id)
);
CREATE TABLE "BiologicalPartOrigin_keyword" (
	"BiologicalPartOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("BiologicalPartOrigin_id", keyword), 
	FOREIGN KEY("BiologicalPartOrigin_id") REFERENCES "BiologicalPartOrigin" (id)
);
CREATE TABLE "BiologicalPartOrigin_identifier" (
	"BiologicalPartOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("BiologicalPartOrigin_id", identifier), 
	FOREIGN KEY("BiologicalPartOrigin_id") REFERENCES "BiologicalPartOrigin" (id)
);
CREATE TABLE "BiologicalPartOrigin_iri" (
	"BiologicalPartOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("BiologicalPartOrigin_id", iri), 
	FOREIGN KEY("BiologicalPartOrigin_id") REFERENCES "BiologicalPartOrigin" (id)
);
CREATE TABLE "SyntheticPartOrigin_keyword" (
	"SyntheticPartOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("SyntheticPartOrigin_id", keyword), 
	FOREIGN KEY("SyntheticPartOrigin_id") REFERENCES "SyntheticPartOrigin" (id)
);
CREATE TABLE "SyntheticPartOrigin_identifier" (
	"SyntheticPartOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("SyntheticPartOrigin_id", identifier), 
	FOREIGN KEY("SyntheticPartOrigin_id") REFERENCES "SyntheticPartOrigin" (id)
);
CREATE TABLE "SyntheticPartOrigin_iri" (
	"SyntheticPartOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("SyntheticPartOrigin_id", iri), 
	FOREIGN KEY("SyntheticPartOrigin_id") REFERENCES "SyntheticPartOrigin" (id)
);
CREATE TABLE "File_keyword" (
	"File_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("File_id", keyword), 
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE TABLE "File_identifier" (
	"File_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("File_id", identifier), 
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE TABLE "File_iri" (
	"File_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("File_id", iri), 
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE TABLE "Data_keyword" (
	"Data_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Data_id", keyword), 
	FOREIGN KEY("Data_id") REFERENCES "Data" (id)
);
CREATE TABLE "Data_identifier" (
	"Data_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Data_id", identifier), 
	FOREIGN KEY("Data_id") REFERENCES "Data" (id)
);
CREATE TABLE "Data_iri" (
	"Data_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Data_id", iri), 
	FOREIGN KEY("Data_id") REFERENCES "Data" (id)
);
CREATE TABLE "Document_keyword" (
	"Document_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Document_id", keyword), 
	FOREIGN KEY("Document_id") REFERENCES "Document" (id)
);
CREATE TABLE "Document_identifier" (
	"Document_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Document_id", identifier), 
	FOREIGN KEY("Document_id") REFERENCES "Document" (id)
);
CREATE TABLE "Document_iri" (
	"Document_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Document_id", iri), 
	FOREIGN KEY("Document_id") REFERENCES "Document" (id)
);
CREATE TABLE "Audio_keyword" (
	"Audio_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Audio_id", keyword), 
	FOREIGN KEY("Audio_id") REFERENCES "Audio" (id)
);
CREATE TABLE "Audio_identifier" (
	"Audio_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Audio_id", identifier), 
	FOREIGN KEY("Audio_id") REFERENCES "Audio" (id)
);
CREATE TABLE "Audio_iri" (
	"Audio_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Audio_id", iri), 
	FOREIGN KEY("Audio_id") REFERENCES "Audio" (id)
);
CREATE TABLE "Video_keyword" (
	"Video_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Video_id", keyword), 
	FOREIGN KEY("Video_id") REFERENCES "Video" (id)
);
CREATE TABLE "Video_identifier" (
	"Video_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Video_id", identifier), 
	FOREIGN KEY("Video_id") REFERENCES "Video" (id)
);
CREATE TABLE "Video_iri" (
	"Video_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Video_id", iri), 
	FOREIGN KEY("Video_id") REFERENCES "Video" (id)
);
CREATE TABLE "Certification_certificationDocument" (
	"Certification_id" INTEGER, 
	"certificationDocument_id" INTEGER, 
	PRIMARY KEY ("Certification_id", "certificationDocument_id"), 
	FOREIGN KEY("Certification_id") REFERENCES "Certification" (id), 
	FOREIGN KEY("certificationDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "Certification_keyword" (
	"Certification_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Certification_id", keyword), 
	FOREIGN KEY("Certification_id") REFERENCES "Certification" (id)
);
CREATE TABLE "Certification_identifier" (
	"Certification_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Certification_id", identifier), 
	FOREIGN KEY("Certification_id") REFERENCES "Certification" (id)
);
CREATE TABLE "Certification_iri" (
	"Certification_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Certification_id", iri), 
	FOREIGN KEY("Certification_id") REFERENCES "Certification" (id)
);
CREATE TABLE "Term" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "CommonName" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "VirusName" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "AlternateName" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "RiskGroup" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "BiosafetyLevel" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Doi" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Journal" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PdbReference" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Keyword" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "TagSequence" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "SpecialFeature" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ExpressionVector" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PlasmidSelection" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "PropagationHost" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "TransmissionMethod" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ProductionCellLine" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ProductCategory" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"parentCategory_id" INTEGER, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("parentCategory_id") REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IsolationHost" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "GeographicalOrigin" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IplcOrigin" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Country" (
	id INTEGER NOT NULL, 
	"alpha2Code" TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "IataClassification" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Variant" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "TaxonomicRank" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "ClinicalGroup" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"inVocabulary_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inVocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Taxonomy_keyword" (
	"Taxonomy_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Taxonomy_id", keyword), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id)
);
CREATE TABLE "Taxonomy_identifier" (
	"Taxonomy_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Taxonomy_id", identifier), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id)
);
CREATE TABLE "Taxonomy_iri" (
	"Taxonomy_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Taxonomy_id", iri), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id)
);
CREATE TABLE "Vocabulary_keyword" (
	"Vocabulary_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Vocabulary_id", keyword), 
	FOREIGN KEY("Vocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Vocabulary_identifier" (
	"Vocabulary_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Vocabulary_id", identifier), 
	FOREIGN KEY("Vocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Vocabulary_iri" (
	"Vocabulary_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Vocabulary_id", iri), 
	FOREIGN KEY("Vocabulary_id") REFERENCES "Vocabulary" (id)
);
CREATE TABLE "Collection_keyword" (
	"Collection_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Collection_id", keyword), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id)
);
CREATE TABLE "Collection_identifier" (
	"Collection_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Collection_id", identifier), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id)
);
CREATE TABLE "Collection_iri" (
	"Collection_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Collection_id", iri), 
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id)
);
CREATE TABLE "Publication" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	authors TEXT NOT NULL, 
	abstract TEXT NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	doi_id INTEGER NOT NULL, 
	journal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id), 
	FOREIGN KEY(journal_id) REFERENCES "Journal" (id)
);
CREATE TABLE "Taxon" (
	id INTEGER NOT NULL, 
	"taxonomicId" TEXT NOT NULL, 
	"taxonomicNodeId" TEXT, 
	title TEXT NOT NULL, 
	description TEXT, 
	weight INTEGER NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"parentTaxon_id" INTEGER, 
	rank_id INTEGER, 
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
	"permitIdentifierForAbs" TEXT, 
	"accessToPhysicalGeneticResource" BOOLEAN NOT NULL, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"countryOfCollection_id" INTEGER NOT NULL, 
	"indigenousPeopleAndLocalCommunityOrigin_id" INTEGER, 
	"recombinantPartIdentification_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("countryOfCollection_id") REFERENCES "Country" (id), 
	FOREIGN KEY("indigenousPeopleAndLocalCommunityOrigin_id") REFERENCES "IplcOrigin" (id), 
	FOREIGN KEY("recombinantPartIdentification_id") REFERENCES "RecombinantPartIdentification" (id)
);
CREATE TABLE "ContactPoint" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	email TEXT, 
	telephone TEXT, 
	"streetAddress" TEXT, 
	"addressLocality" TEXT, 
	"addressRegion" TEXT, 
	"postalCode" TEXT, 
	"orcidId" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
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
CREATE TABLE "Term_keyword" (
	"Term_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Term_id", keyword), 
	FOREIGN KEY("Term_id") REFERENCES "Term" (id)
);
CREATE TABLE "Term_identifier" (
	"Term_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Term_id", identifier), 
	FOREIGN KEY("Term_id") REFERENCES "Term" (id)
);
CREATE TABLE "Term_iri" (
	"Term_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Term_id", iri), 
	FOREIGN KEY("Term_id") REFERENCES "Term" (id)
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
CREATE TABLE "CommonName_keyword" (
	"CommonName_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("CommonName_id", keyword), 
	FOREIGN KEY("CommonName_id") REFERENCES "CommonName" (id)
);
CREATE TABLE "CommonName_identifier" (
	"CommonName_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("CommonName_id", identifier), 
	FOREIGN KEY("CommonName_id") REFERENCES "CommonName" (id)
);
CREATE TABLE "CommonName_iri" (
	"CommonName_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("CommonName_id", iri), 
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
CREATE TABLE "VirusName_keyword" (
	"VirusName_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("VirusName_id", keyword), 
	FOREIGN KEY("VirusName_id") REFERENCES "VirusName" (id)
);
CREATE TABLE "VirusName_identifier" (
	"VirusName_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("VirusName_id", identifier), 
	FOREIGN KEY("VirusName_id") REFERENCES "VirusName" (id)
);
CREATE TABLE "VirusName_iri" (
	"VirusName_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("VirusName_id", iri), 
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
CREATE TABLE "AlternateName_keyword" (
	"AlternateName_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("AlternateName_id", keyword), 
	FOREIGN KEY("AlternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "AlternateName_identifier" (
	"AlternateName_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("AlternateName_id", identifier), 
	FOREIGN KEY("AlternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "AlternateName_iri" (
	"AlternateName_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("AlternateName_id", iri), 
	FOREIGN KEY("AlternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "RiskGroup_keyword" (
	"RiskGroup_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("RiskGroup_id", keyword), 
	FOREIGN KEY("RiskGroup_id") REFERENCES "RiskGroup" (id)
);
CREATE TABLE "RiskGroup_identifier" (
	"RiskGroup_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("RiskGroup_id", identifier), 
	FOREIGN KEY("RiskGroup_id") REFERENCES "RiskGroup" (id)
);
CREATE TABLE "RiskGroup_iri" (
	"RiskGroup_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("RiskGroup_id", iri), 
	FOREIGN KEY("RiskGroup_id") REFERENCES "RiskGroup" (id)
);
CREATE TABLE "BiosafetyLevel_keyword" (
	"BiosafetyLevel_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("BiosafetyLevel_id", keyword), 
	FOREIGN KEY("BiosafetyLevel_id") REFERENCES "BiosafetyLevel" (id)
);
CREATE TABLE "BiosafetyLevel_identifier" (
	"BiosafetyLevel_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("BiosafetyLevel_id", identifier), 
	FOREIGN KEY("BiosafetyLevel_id") REFERENCES "BiosafetyLevel" (id)
);
CREATE TABLE "BiosafetyLevel_iri" (
	"BiosafetyLevel_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("BiosafetyLevel_id", iri), 
	FOREIGN KEY("BiosafetyLevel_id") REFERENCES "BiosafetyLevel" (id)
);
CREATE TABLE "Doi_keyword" (
	"Doi_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Doi_id", keyword), 
	FOREIGN KEY("Doi_id") REFERENCES "Doi" (id)
);
CREATE TABLE "Doi_identifier" (
	"Doi_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Doi_id", identifier), 
	FOREIGN KEY("Doi_id") REFERENCES "Doi" (id)
);
CREATE TABLE "Doi_iri" (
	"Doi_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Doi_id", iri), 
	FOREIGN KEY("Doi_id") REFERENCES "Doi" (id)
);
CREATE TABLE "Journal_keyword" (
	"Journal_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Journal_id", keyword), 
	FOREIGN KEY("Journal_id") REFERENCES "Journal" (id)
);
CREATE TABLE "Journal_identifier" (
	"Journal_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Journal_id", identifier), 
	FOREIGN KEY("Journal_id") REFERENCES "Journal" (id)
);
CREATE TABLE "Journal_iri" (
	"Journal_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Journal_id", iri), 
	FOREIGN KEY("Journal_id") REFERENCES "Journal" (id)
);
CREATE TABLE "PdbReference_keyword" (
	"PdbReference_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("PdbReference_id", keyword), 
	FOREIGN KEY("PdbReference_id") REFERENCES "PdbReference" (id)
);
CREATE TABLE "PdbReference_identifier" (
	"PdbReference_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("PdbReference_id", identifier), 
	FOREIGN KEY("PdbReference_id") REFERENCES "PdbReference" (id)
);
CREATE TABLE "PdbReference_iri" (
	"PdbReference_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("PdbReference_id", iri), 
	FOREIGN KEY("PdbReference_id") REFERENCES "PdbReference" (id)
);
CREATE TABLE "Keyword_keyword" (
	"Keyword_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Keyword_id", keyword), 
	FOREIGN KEY("Keyword_id") REFERENCES "Keyword" (id)
);
CREATE TABLE "Keyword_identifier" (
	"Keyword_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Keyword_id", identifier), 
	FOREIGN KEY("Keyword_id") REFERENCES "Keyword" (id)
);
CREATE TABLE "Keyword_iri" (
	"Keyword_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Keyword_id", iri), 
	FOREIGN KEY("Keyword_id") REFERENCES "Keyword" (id)
);
CREATE TABLE "TagSequence_keyword" (
	"TagSequence_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("TagSequence_id", keyword), 
	FOREIGN KEY("TagSequence_id") REFERENCES "TagSequence" (id)
);
CREATE TABLE "TagSequence_identifier" (
	"TagSequence_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("TagSequence_id", identifier), 
	FOREIGN KEY("TagSequence_id") REFERENCES "TagSequence" (id)
);
CREATE TABLE "TagSequence_iri" (
	"TagSequence_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("TagSequence_id", iri), 
	FOREIGN KEY("TagSequence_id") REFERENCES "TagSequence" (id)
);
CREATE TABLE "SpecialFeature_keyword" (
	"SpecialFeature_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("SpecialFeature_id", keyword), 
	FOREIGN KEY("SpecialFeature_id") REFERENCES "SpecialFeature" (id)
);
CREATE TABLE "SpecialFeature_identifier" (
	"SpecialFeature_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("SpecialFeature_id", identifier), 
	FOREIGN KEY("SpecialFeature_id") REFERENCES "SpecialFeature" (id)
);
CREATE TABLE "SpecialFeature_iri" (
	"SpecialFeature_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("SpecialFeature_id", iri), 
	FOREIGN KEY("SpecialFeature_id") REFERENCES "SpecialFeature" (id)
);
CREATE TABLE "ExpressionVector_keyword" (
	"ExpressionVector_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ExpressionVector_id", keyword), 
	FOREIGN KEY("ExpressionVector_id") REFERENCES "ExpressionVector" (id)
);
CREATE TABLE "ExpressionVector_identifier" (
	"ExpressionVector_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ExpressionVector_id", identifier), 
	FOREIGN KEY("ExpressionVector_id") REFERENCES "ExpressionVector" (id)
);
CREATE TABLE "ExpressionVector_iri" (
	"ExpressionVector_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ExpressionVector_id", iri), 
	FOREIGN KEY("ExpressionVector_id") REFERENCES "ExpressionVector" (id)
);
CREATE TABLE "PlasmidSelection_keyword" (
	"PlasmidSelection_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("PlasmidSelection_id", keyword), 
	FOREIGN KEY("PlasmidSelection_id") REFERENCES "PlasmidSelection" (id)
);
CREATE TABLE "PlasmidSelection_identifier" (
	"PlasmidSelection_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("PlasmidSelection_id", identifier), 
	FOREIGN KEY("PlasmidSelection_id") REFERENCES "PlasmidSelection" (id)
);
CREATE TABLE "PlasmidSelection_iri" (
	"PlasmidSelection_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("PlasmidSelection_id", iri), 
	FOREIGN KEY("PlasmidSelection_id") REFERENCES "PlasmidSelection" (id)
);
CREATE TABLE "PropagationHost_keyword" (
	"PropagationHost_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("PropagationHost_id", keyword), 
	FOREIGN KEY("PropagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "PropagationHost_identifier" (
	"PropagationHost_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("PropagationHost_id", identifier), 
	FOREIGN KEY("PropagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "PropagationHost_iri" (
	"PropagationHost_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("PropagationHost_id", iri), 
	FOREIGN KEY("PropagationHost_id") REFERENCES "PropagationHost" (id)
);
CREATE TABLE "TransmissionMethod_keyword" (
	"TransmissionMethod_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("TransmissionMethod_id", keyword), 
	FOREIGN KEY("TransmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "TransmissionMethod_identifier" (
	"TransmissionMethod_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("TransmissionMethod_id", identifier), 
	FOREIGN KEY("TransmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "TransmissionMethod_iri" (
	"TransmissionMethod_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("TransmissionMethod_id", iri), 
	FOREIGN KEY("TransmissionMethod_id") REFERENCES "TransmissionMethod" (id)
);
CREATE TABLE "ProductionCellLine_keyword" (
	"ProductionCellLine_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ProductionCellLine_id", keyword), 
	FOREIGN KEY("ProductionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "ProductionCellLine_identifier" (
	"ProductionCellLine_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ProductionCellLine_id", identifier), 
	FOREIGN KEY("ProductionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "ProductionCellLine_iri" (
	"ProductionCellLine_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ProductionCellLine_id", iri), 
	FOREIGN KEY("ProductionCellLine_id") REFERENCES "ProductionCellLine" (id)
);
CREATE TABLE "ProductCategory_keyword" (
	"ProductCategory_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ProductCategory_id", keyword), 
	FOREIGN KEY("ProductCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "ProductCategory_identifier" (
	"ProductCategory_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ProductCategory_id", identifier), 
	FOREIGN KEY("ProductCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "ProductCategory_iri" (
	"ProductCategory_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ProductCategory_id", iri), 
	FOREIGN KEY("ProductCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "IsolationHost_keyword" (
	"IsolationHost_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("IsolationHost_id", keyword), 
	FOREIGN KEY("IsolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "IsolationHost_identifier" (
	"IsolationHost_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("IsolationHost_id", identifier), 
	FOREIGN KEY("IsolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "IsolationHost_iri" (
	"IsolationHost_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("IsolationHost_id", iri), 
	FOREIGN KEY("IsolationHost_id") REFERENCES "IsolationHost" (id)
);
CREATE TABLE "GeographicalOrigin_keyword" (
	"GeographicalOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("GeographicalOrigin_id", keyword), 
	FOREIGN KEY("GeographicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "GeographicalOrigin_identifier" (
	"GeographicalOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("GeographicalOrigin_id", identifier), 
	FOREIGN KEY("GeographicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "GeographicalOrigin_iri" (
	"GeographicalOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("GeographicalOrigin_id", iri), 
	FOREIGN KEY("GeographicalOrigin_id") REFERENCES "GeographicalOrigin" (id)
);
CREATE TABLE "IplcOrigin_keyword" (
	"IplcOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("IplcOrigin_id", keyword), 
	FOREIGN KEY("IplcOrigin_id") REFERENCES "IplcOrigin" (id)
);
CREATE TABLE "IplcOrigin_identifier" (
	"IplcOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("IplcOrigin_id", identifier), 
	FOREIGN KEY("IplcOrigin_id") REFERENCES "IplcOrigin" (id)
);
CREATE TABLE "IplcOrigin_iri" (
	"IplcOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("IplcOrigin_id", iri), 
	FOREIGN KEY("IplcOrigin_id") REFERENCES "IplcOrigin" (id)
);
CREATE TABLE "Country_keyword" (
	"Country_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Country_id", keyword), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "Country_identifier" (
	"Country_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Country_id", identifier), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "Country_iri" (
	"Country_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Country_id", iri), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "IataClassification_keyword" (
	"IataClassification_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("IataClassification_id", keyword), 
	FOREIGN KEY("IataClassification_id") REFERENCES "IataClassification" (id)
);
CREATE TABLE "IataClassification_identifier" (
	"IataClassification_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("IataClassification_id", identifier), 
	FOREIGN KEY("IataClassification_id") REFERENCES "IataClassification" (id)
);
CREATE TABLE "IataClassification_iri" (
	"IataClassification_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("IataClassification_id", iri), 
	FOREIGN KEY("IataClassification_id") REFERENCES "IataClassification" (id)
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
CREATE TABLE "Variant_keyword" (
	"Variant_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Variant_id", keyword), 
	FOREIGN KEY("Variant_id") REFERENCES "Variant" (id)
);
CREATE TABLE "Variant_identifier" (
	"Variant_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Variant_id", identifier), 
	FOREIGN KEY("Variant_id") REFERENCES "Variant" (id)
);
CREATE TABLE "Variant_iri" (
	"Variant_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Variant_id", iri), 
	FOREIGN KEY("Variant_id") REFERENCES "Variant" (id)
);
CREATE TABLE "TaxonomicRank_taxonomy" (
	"TaxonomicRank_id" INTEGER, 
	taxonomy_id INTEGER, 
	PRIMARY KEY ("TaxonomicRank_id", taxonomy_id), 
	FOREIGN KEY("TaxonomicRank_id") REFERENCES "TaxonomicRank" (id), 
	FOREIGN KEY(taxonomy_id) REFERENCES "Taxonomy" (id)
);
CREATE TABLE "TaxonomicRank_keyword" (
	"TaxonomicRank_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("TaxonomicRank_id", keyword), 
	FOREIGN KEY("TaxonomicRank_id") REFERENCES "TaxonomicRank" (id)
);
CREATE TABLE "TaxonomicRank_identifier" (
	"TaxonomicRank_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("TaxonomicRank_id", identifier), 
	FOREIGN KEY("TaxonomicRank_id") REFERENCES "TaxonomicRank" (id)
);
CREATE TABLE "TaxonomicRank_iri" (
	"TaxonomicRank_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("TaxonomicRank_id", iri), 
	FOREIGN KEY("TaxonomicRank_id") REFERENCES "TaxonomicRank" (id)
);
CREATE TABLE "ClinicalGroup_alternateName" (
	"ClinicalGroup_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("ClinicalGroup_id", "alternateName_id"), 
	FOREIGN KEY("ClinicalGroup_id") REFERENCES "ClinicalGroup" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "ClinicalGroup_keyword" (
	"ClinicalGroup_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ClinicalGroup_id", keyword), 
	FOREIGN KEY("ClinicalGroup_id") REFERENCES "ClinicalGroup" (id)
);
CREATE TABLE "ClinicalGroup_identifier" (
	"ClinicalGroup_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ClinicalGroup_id", identifier), 
	FOREIGN KEY("ClinicalGroup_id") REFERENCES "ClinicalGroup" (id)
);
CREATE TABLE "ClinicalGroup_iri" (
	"ClinicalGroup_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ClinicalGroup_id", iri), 
	FOREIGN KEY("ClinicalGroup_id") REFERENCES "ClinicalGroup" (id)
);
CREATE TABLE "PathogenIdentification" (
	id INTEGER NOT NULL, 
	"pathogenType" TEXT NOT NULL, 
	subspecies TEXT, 
	strain TEXT, 
	isolate TEXT, 
	genotype TEXT, 
	serotype TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
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
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	"orcidId" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Organization" (
	id INTEGER NOT NULL, 
	"rorId" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "ReasearchInfrastructure" (
	id INTEGER NOT NULL, 
	"rorId" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Provider" (
	id INTEGER NOT NULL, 
	"rorId" TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	country_id INTEGER, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "Originator" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"homePage" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"contactPoint_id" INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "MaterialSafetyDataSheet" (
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
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"materialSafetyContact_id" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("materialSafetyContact_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Taxonomy_taxon" (
	"Taxonomy_id" INTEGER, 
	taxon_id INTEGER, 
	PRIMARY KEY ("Taxonomy_id", taxon_id), 
	FOREIGN KEY("Taxonomy_id") REFERENCES "Taxonomy" (id), 
	FOREIGN KEY(taxon_id) REFERENCES "Taxon" (id)
);
CREATE TABLE "Publication_keyword" (
	"Publication_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Publication_id", keyword), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id)
);
CREATE TABLE "Publication_identifier" (
	"Publication_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Publication_id", identifier), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id)
);
CREATE TABLE "Publication_iri" (
	"Publication_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Publication_id", iri), 
	FOREIGN KEY("Publication_id") REFERENCES "Publication" (id)
);
CREATE TABLE "Taxon_taxonomy" (
	"Taxon_id" INTEGER, 
	taxonomy_id INTEGER, 
	PRIMARY KEY ("Taxon_id", taxonomy_id), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY(taxonomy_id) REFERENCES "Taxonomy" (id)
);
CREATE TABLE "Taxon_externalEquivalentTaxon" (
	"Taxon_id" INTEGER, 
	"externalEquivalentTaxon_id" INTEGER, 
	PRIMARY KEY ("Taxon_id", "externalEquivalentTaxon_id"), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY("externalEquivalentTaxon_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_alternateName" (
	"Taxon_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("Taxon_id", "alternateName_id"), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "Taxon_previouslyKnownAs" (
	"Taxon_id" INTEGER, 
	"previouslyKnownAs_id" INTEGER, 
	PRIMARY KEY ("Taxon_id", "previouslyKnownAs_id"), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id), 
	FOREIGN KEY("previouslyKnownAs_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_keyword" (
	"Taxon_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Taxon_id", keyword), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_identifier" (
	"Taxon_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Taxon_id", identifier), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "Taxon_iri" (
	"Taxon_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Taxon_id", iri), 
	FOREIGN KEY("Taxon_id") REFERENCES "Taxon" (id)
);
CREATE TABLE "ClinicalGroup_taxon" (
	"ClinicalGroup_id" INTEGER, 
	taxon_id INTEGER, 
	PRIMARY KEY ("ClinicalGroup_id", taxon_id), 
	FOREIGN KEY("ClinicalGroup_id") REFERENCES "ClinicalGroup" (id), 
	FOREIGN KEY(taxon_id) REFERENCES "Taxon" (id)
);
CREATE TABLE "NaturalPartOrigin_keyword" (
	"NaturalPartOrigin_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("NaturalPartOrigin_id", keyword), 
	FOREIGN KEY("NaturalPartOrigin_id") REFERENCES "NaturalPartOrigin" (id)
);
CREATE TABLE "NaturalPartOrigin_identifier" (
	"NaturalPartOrigin_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("NaturalPartOrigin_id", identifier), 
	FOREIGN KEY("NaturalPartOrigin_id") REFERENCES "NaturalPartOrigin" (id)
);
CREATE TABLE "NaturalPartOrigin_iri" (
	"NaturalPartOrigin_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("NaturalPartOrigin_id", iri), 
	FOREIGN KEY("NaturalPartOrigin_id") REFERENCES "NaturalPartOrigin" (id)
);
CREATE TABLE "ContactPoint_keyword" (
	"ContactPoint_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ContactPoint_id", keyword), 
	FOREIGN KEY("ContactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "ContactPoint_identifier" (
	"ContactPoint_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ContactPoint_id", identifier), 
	FOREIGN KEY("ContactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "ContactPoint_iri" (
	"ContactPoint_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ContactPoint_id", iri), 
	FOREIGN KEY("ContactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "ProductOrService" (
	id INTEGER NOT NULL, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Service" (
	id INTEGER NOT NULL, 
	"modelSpecies" TEXT, 
	"modelType" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Product" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Antibody" (
	id INTEGER NOT NULL, 
	"productionSystem" TEXT, 
	"antibodyPurifiedByAffinity" BOOLEAN, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	"targetedAntigen" TEXT NOT NULL, 
	"antibodyType" TEXT, 
	"antibodyCharacterizationObservation" TEXT, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Hybridoma" (
	id INTEGER NOT NULL, 
	"hybridomaDescription" TEXT NOT NULL, 
	"productionSystem" TEXT, 
	"antibodyPurifiedByAffinity" BOOLEAN, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	"targetedAntigen" TEXT NOT NULL, 
	"antibodyType" TEXT, 
	"antibodyCharacterizationObservation" TEXT, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Protein" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "NucleicAcid" (
	id INTEGER NOT NULL, 
	"clonedNucleicAcid" BOOLEAN NOT NULL, 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"clonedIntoPlasmid_id" INTEGER, 
	"tagSequence_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("clonedIntoPlasmid_id") REFERENCES "ExpressionVector" (id), 
	FOREIGN KEY("tagSequence_id") REFERENCES "TagSequence" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "DetectionKit" (
	id INTEGER NOT NULL, 
	"specificityDocumented" BOOLEAN NOT NULL, 
	specificity TEXT, 
	"targetedRegion" TEXT, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "Bundle" (
	id INTEGER NOT NULL, 
	"shippingConditions" TEXT NOT NULL, 
	"storageConditions" TEXT NOT NULL, 
	"thirdPartyDistributionConsent" BOOLEAN, 
	"usageRestrictions" TEXT, 
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
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
	"preparationTechnique" TEXT, 
	"accessPointUrl" TEXT NOT NULL, 
	"refSku" TEXT NOT NULL, 
	"unitDefinition" TEXT, 
	"unitCost" INTEGER, 
	"unitCostCurrency" TEXT, 
	"unitCostNote" TEXT, 
	"qualityGrading" TEXT, 
	"biosafetyRestrictions" TEXT, 
	"canBeUsedToProduceGmo" BOOLEAN NOT NULL, 
	availability TEXT NOT NULL, 
	"technicalRecommendation" TEXT, 
	"internalReference" TEXT, 
	note TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	"biologicalMaterialOrigin_id" INTEGER NOT NULL, 
	"iataClassification_id" INTEGER NOT NULL, 
	"materialSafetyDataSheet_id" INTEGER, 
	originator_id INTEGER, 
	category_id INTEGER NOT NULL, 
	"riskGroup_id" INTEGER, 
	"biosafetyLevel_id" INTEGER, 
	provider_id INTEGER NOT NULL, 
	"contactPoint_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("biologicalMaterialOrigin_id") REFERENCES "BiologicalMaterialOrigin" (id), 
	FOREIGN KEY("iataClassification_id") REFERENCES "IataClassification" (id), 
	FOREIGN KEY("materialSafetyDataSheet_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY(originator_id) REFERENCES "Originator" (id), 
	FOREIGN KEY(category_id) REFERENCES "ProductCategory" (id), 
	FOREIGN KEY("riskGroup_id") REFERENCES "RiskGroup" (id), 
	FOREIGN KEY("biosafetyLevel_id") REFERENCES "BiosafetyLevel" (id), 
	FOREIGN KEY(provider_id) REFERENCES "Provider" (id), 
	FOREIGN KEY("contactPoint_id") REFERENCES "ContactPoint" (id)
);
CREATE TABLE "FundingSource" (
	id INTEGER NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	"fundingProgram" TEXT, 
	"grantNumber" TEXT, 
	"fundingPeriodStart" DATE, 
	"fundingPeriodEnd" DATE, 
	"eligibilityCriteria" TEXT, 
	"dateIssued" DATETIME, 
	"dateModified" DATETIME, 
	funder_id INTEGER, 
	logo_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(funder_id) REFERENCES "Organization" (id), 
	FOREIGN KEY(logo_id) REFERENCES "Image" (id)
);
CREATE TABLE "PathogenIdentification_hostType" (
	"PathogenIdentification_id" INTEGER, 
	"hostType" TEXT, 
	PRIMARY KEY ("PathogenIdentification_id", "hostType"), 
	FOREIGN KEY("PathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "PathogenIdentification_keyword" (
	"PathogenIdentification_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("PathogenIdentification_id", keyword), 
	FOREIGN KEY("PathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "PathogenIdentification_identifier" (
	"PathogenIdentification_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("PathogenIdentification_id", identifier), 
	FOREIGN KEY("PathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "PathogenIdentification_iri" (
	"PathogenIdentification_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("PathogenIdentification_id", iri), 
	FOREIGN KEY("PathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "PersonOrOrganization_keyword" (
	"PersonOrOrganization_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("PersonOrOrganization_id", keyword), 
	FOREIGN KEY("PersonOrOrganization_id") REFERENCES "PersonOrOrganization" (id)
);
CREATE TABLE "PersonOrOrganization_identifier" (
	"PersonOrOrganization_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("PersonOrOrganization_id", identifier), 
	FOREIGN KEY("PersonOrOrganization_id") REFERENCES "PersonOrOrganization" (id)
);
CREATE TABLE "PersonOrOrganization_iri" (
	"PersonOrOrganization_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("PersonOrOrganization_id", iri), 
	FOREIGN KEY("PersonOrOrganization_id") REFERENCES "PersonOrOrganization" (id)
);
CREATE TABLE "Person_keyword" (
	"Person_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Person_id", keyword), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Person_identifier" (
	"Person_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Person_id", identifier), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Person_iri" (
	"Person_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Person_id", iri), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Organization_alternateName" (
	"Organization_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("Organization_id", "alternateName_id"), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "Organization_keyword" (
	"Organization_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Organization_id", keyword), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "Organization_identifier" (
	"Organization_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Organization_id", identifier), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "Organization_iri" (
	"Organization_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Organization_id", iri), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "ReasearchInfrastructure_alternateName" (
	"ReasearchInfrastructure_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("ReasearchInfrastructure_id", "alternateName_id"), 
	FOREIGN KEY("ReasearchInfrastructure_id") REFERENCES "ReasearchInfrastructure" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "ReasearchInfrastructure_keyword" (
	"ReasearchInfrastructure_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ReasearchInfrastructure_id", keyword), 
	FOREIGN KEY("ReasearchInfrastructure_id") REFERENCES "ReasearchInfrastructure" (id)
);
CREATE TABLE "ReasearchInfrastructure_identifier" (
	"ReasearchInfrastructure_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ReasearchInfrastructure_id", identifier), 
	FOREIGN KEY("ReasearchInfrastructure_id") REFERENCES "ReasearchInfrastructure" (id)
);
CREATE TABLE "ReasearchInfrastructure_iri" (
	"ReasearchInfrastructure_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ReasearchInfrastructure_id", iri), 
	FOREIGN KEY("ReasearchInfrastructure_id") REFERENCES "ReasearchInfrastructure" (id)
);
CREATE TABLE "Provider_memberOfRi" (
	"Provider_id" INTEGER, 
	"memberOfRi_id" INTEGER, 
	PRIMARY KEY ("Provider_id", "memberOfRi_id"), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id), 
	FOREIGN KEY("memberOfRi_id") REFERENCES "ReasearchInfrastructure" (id)
);
CREATE TABLE "Provider_alternateName" (
	"Provider_id" INTEGER, 
	"alternateName_id" INTEGER, 
	PRIMARY KEY ("Provider_id", "alternateName_id"), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id), 
	FOREIGN KEY("alternateName_id") REFERENCES "AlternateName" (id)
);
CREATE TABLE "Provider_keyword" (
	"Provider_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Provider_id", keyword), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id)
);
CREATE TABLE "Provider_identifier" (
	"Provider_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Provider_id", identifier), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id)
);
CREATE TABLE "Provider_iri" (
	"Provider_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Provider_id", iri), 
	FOREIGN KEY("Provider_id") REFERENCES "Provider" (id)
);
CREATE TABLE "Originator_keyword" (
	"Originator_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Originator_id", keyword), 
	FOREIGN KEY("Originator_id") REFERENCES "Originator" (id)
);
CREATE TABLE "Originator_identifier" (
	"Originator_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Originator_id", identifier), 
	FOREIGN KEY("Originator_id") REFERENCES "Originator" (id)
);
CREATE TABLE "Originator_iri" (
	"Originator_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Originator_id", iri), 
	FOREIGN KEY("Originator_id") REFERENCES "Originator" (id)
);
CREATE TABLE "MaterialSafetyDataSheet_keyword" (
	"MaterialSafetyDataSheet_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("MaterialSafetyDataSheet_id", keyword), 
	FOREIGN KEY("MaterialSafetyDataSheet_id") REFERENCES "MaterialSafetyDataSheet" (id)
);
CREATE TABLE "MaterialSafetyDataSheet_identifier" (
	"MaterialSafetyDataSheet_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("MaterialSafetyDataSheet_id", identifier), 
	FOREIGN KEY("MaterialSafetyDataSheet_id") REFERENCES "MaterialSafetyDataSheet" (id)
);
CREATE TABLE "MaterialSafetyDataSheet_iri" (
	"MaterialSafetyDataSheet_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("MaterialSafetyDataSheet_id", iri), 
	FOREIGN KEY("MaterialSafetyDataSheet_id") REFERENCES "MaterialSafetyDataSheet" (id)
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
CREATE TABLE "ProductOrService_doi" (
	"ProductOrService_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("ProductOrService_id", doi_id), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "ProductOrService_fundingSource" (
	"ProductOrService_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("ProductOrService_id", "fundingSource_id"), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "ProductOrService_keyword" (
	"ProductOrService_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("ProductOrService_id", keyword), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id)
);
CREATE TABLE "ProductOrService_identifier" (
	"ProductOrService_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("ProductOrService_id", identifier), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id)
);
CREATE TABLE "ProductOrService_iri" (
	"ProductOrService_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("ProductOrService_id", iri), 
	FOREIGN KEY("ProductOrService_id") REFERENCES "ProductOrService" (id)
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
CREATE TABLE "Service_doi" (
	"Service_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Service_id", doi_id), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Service_fundingSource" (
	"Service_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Service_id", "fundingSource_id"), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Service_keyword" (
	"Service_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Service_id", keyword), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id)
);
CREATE TABLE "Service_identifier" (
	"Service_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Service_id", identifier), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id)
);
CREATE TABLE "Service_iri" (
	"Service_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Service_id", iri), 
	FOREIGN KEY("Service_id") REFERENCES "Service" (id)
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
CREATE TABLE "Product_doi" (
	"Product_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Product_id", doi_id), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Product_fundingSource" (
	"Product_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Product_id", "fundingSource_id"), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Product_keyword" (
	"Product_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Product_id", keyword), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id)
);
CREATE TABLE "Product_identifier" (
	"Product_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Product_id", identifier), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id)
);
CREATE TABLE "Product_iri" (
	"Product_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Product_id", iri), 
	FOREIGN KEY("Product_id") REFERENCES "Product" (id)
);
CREATE TABLE "Antibody_sequenceReference" (
	"Antibody_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "sequenceReference_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "Antibody_antibodyCharacterizationMethod" (
	"Antibody_id" INTEGER, 
	"antibodyCharacterizationMethod" TEXT, 
	PRIMARY KEY ("Antibody_id", "antibodyCharacterizationMethod"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id)
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
CREATE TABLE "Antibody_doi" (
	"Antibody_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Antibody_id", doi_id), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Antibody_fundingSource" (
	"Antibody_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Antibody_id", "fundingSource_id"), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Antibody_keyword" (
	"Antibody_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Antibody_id", keyword), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id)
);
CREATE TABLE "Antibody_identifier" (
	"Antibody_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Antibody_id", identifier), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id)
);
CREATE TABLE "Antibody_iri" (
	"Antibody_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Antibody_id", iri), 
	FOREIGN KEY("Antibody_id") REFERENCES "Antibody" (id)
);
CREATE TABLE "Hybridoma_sequenceReference" (
	"Hybridoma_id" INTEGER, 
	"sequenceReference_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "sequenceReference_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("sequenceReference_id") REFERENCES "SequenceReference" (id)
);
CREATE TABLE "Hybridoma_antibodyCharacterizationMethod" (
	"Hybridoma_id" INTEGER, 
	"antibodyCharacterizationMethod" TEXT, 
	PRIMARY KEY ("Hybridoma_id", "antibodyCharacterizationMethod"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id)
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
CREATE TABLE "Hybridoma_doi" (
	"Hybridoma_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Hybridoma_id", doi_id), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Hybridoma_fundingSource" (
	"Hybridoma_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Hybridoma_id", "fundingSource_id"), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Hybridoma_keyword" (
	"Hybridoma_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Hybridoma_id", keyword), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id)
);
CREATE TABLE "Hybridoma_identifier" (
	"Hybridoma_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Hybridoma_id", identifier), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id)
);
CREATE TABLE "Hybridoma_iri" (
	"Hybridoma_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Hybridoma_id", iri), 
	FOREIGN KEY("Hybridoma_id") REFERENCES "Hybridoma" (id)
);
CREATE TABLE "Protein_sequence" (
	"Protein_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("Protein_id", sequence_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "Protein_relatedPdb" (
	"Protein_id" INTEGER, 
	"relatedPdb_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "relatedPdb_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("relatedPdb_id") REFERENCES "PdbReference" (id)
);
CREATE TABLE "Protein_specialFeature" (
	"Protein_id" INTEGER, 
	"specialFeature_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "specialFeature_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("specialFeature_id") REFERENCES "SpecialFeature" (id)
);
CREATE TABLE "Protein_tagSequence" (
	"Protein_id" INTEGER, 
	"tagSequence_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "tagSequence_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("tagSequence_id") REFERENCES "TagSequence" (id)
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
CREATE TABLE "Protein_functionalAndTechnicalDescription" (
	"Protein_id" INTEGER, 
	"functionalAndTechnicalDescription" TEXT, 
	PRIMARY KEY ("Protein_id", "functionalAndTechnicalDescription"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_proteinPurification" (
	"Protein_id" INTEGER, 
	"proteinPurification" TEXT, 
	PRIMARY KEY ("Protein_id", "proteinPurification"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_tagStatusOfTheSolubilizedProtein" (
	"Protein_id" INTEGER, 
	"tagStatusOfTheSolubilizedProtein" TEXT, 
	PRIMARY KEY ("Protein_id", "tagStatusOfTheSolubilizedProtein"), 
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
CREATE TABLE "Protein_doi" (
	"Protein_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Protein_id", doi_id), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Protein_fundingSource" (
	"Protein_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Protein_id", "fundingSource_id"), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Protein_keyword" (
	"Protein_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Protein_id", keyword), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_identifier" (
	"Protein_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Protein_id", identifier), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "Protein_iri" (
	"Protein_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Protein_id", iri), 
	FOREIGN KEY("Protein_id") REFERENCES "Protein" (id)
);
CREATE TABLE "NucleicAcid_genBankFileOfTheConstruct" (
	"NucleicAcid_id" INTEGER, 
	"genBankFileOfTheConstruct_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "genBankFileOfTheConstruct_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("genBankFileOfTheConstruct_id") REFERENCES "Data" (id)
);
CREATE TABLE "NucleicAcid_sequence" (
	"NucleicAcid_id" INTEGER, 
	sequence_id INTEGER NOT NULL, 
	PRIMARY KEY ("NucleicAcid_id", sequence_id), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "NucleicAcid_plasmidSelection" (
	"NucleicAcid_id" INTEGER, 
	"plasmidSelection_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "plasmidSelection_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("plasmidSelection_id") REFERENCES "PlasmidSelection" (id)
);
CREATE TABLE "NucleicAcid_additionalCategory" (
	"NucleicAcid_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "additionalCategory_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "NucleicAcid_pathogenIdentification" (
	"NucleicAcid_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("NucleicAcid_id", "pathogenIdentification_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "NucleicAcid_doi" (
	"NucleicAcid_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", doi_id), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
);
CREATE TABLE "NucleicAcid_collection" (
	"NucleicAcid_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("NucleicAcid_id", collection_id), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "NucleicAcid_keywords" (
	"NucleicAcid_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("NucleicAcid_id", keywords_id), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "NucleicAcid_complementaryDocument" (
	"NucleicAcid_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "complementaryDocument_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "NucleicAcid_productPicture" (
	"NucleicAcid_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "productPicture_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "NucleicAcid_externalRelatedReference" (
	"NucleicAcid_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "externalRelatedReference_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "NucleicAcid_certification" (
	"NucleicAcid_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", certification_id), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "NucleicAcid_fundingSource" (
	"NucleicAcid_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("NucleicAcid_id", "fundingSource_id"), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "NucleicAcid_keyword" (
	"NucleicAcid_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("NucleicAcid_id", keyword), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id)
);
CREATE TABLE "NucleicAcid_identifier" (
	"NucleicAcid_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("NucleicAcid_id", identifier), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id)
);
CREATE TABLE "NucleicAcid_iri" (
	"NucleicAcid_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("NucleicAcid_id", iri), 
	FOREIGN KEY("NucleicAcid_id") REFERENCES "NucleicAcid" (id)
);
CREATE TABLE "DetectionKit_standardOperatingProcedureFile" (
	"DetectionKit_id" INTEGER, 
	"standardOperatingProcedureFile_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "standardOperatingProcedureFile_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("standardOperatingProcedureFile_id") REFERENCES "File" (id)
);
CREATE TABLE "DetectionKit_additionalCategory" (
	"DetectionKit_id" INTEGER, 
	"additionalCategory_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "additionalCategory_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("additionalCategory_id") REFERENCES "ProductCategory" (id)
);
CREATE TABLE "DetectionKit_pathogenIdentification" (
	"DetectionKit_id" INTEGER, 
	"pathogenIdentification_id" INTEGER NOT NULL, 
	PRIMARY KEY ("DetectionKit_id", "pathogenIdentification_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("pathogenIdentification_id") REFERENCES "PathogenIdentification" (id)
);
CREATE TABLE "DetectionKit_doi" (
	"DetectionKit_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("DetectionKit_id", doi_id), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
);
CREATE TABLE "DetectionKit_collection" (
	"DetectionKit_id" INTEGER, 
	collection_id INTEGER NOT NULL, 
	PRIMARY KEY ("DetectionKit_id", collection_id), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY(collection_id) REFERENCES "Collection" (id)
);
CREATE TABLE "DetectionKit_keywords" (
	"DetectionKit_id" INTEGER, 
	keywords_id INTEGER NOT NULL, 
	PRIMARY KEY ("DetectionKit_id", keywords_id), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY(keywords_id) REFERENCES "Keyword" (id)
);
CREATE TABLE "DetectionKit_complementaryDocument" (
	"DetectionKit_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "complementaryDocument_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
);
CREATE TABLE "DetectionKit_productPicture" (
	"DetectionKit_id" INTEGER, 
	"productPicture_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "productPicture_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("productPicture_id") REFERENCES "Image" (id)
);
CREATE TABLE "DetectionKit_externalRelatedReference" (
	"DetectionKit_id" INTEGER, 
	"externalRelatedReference_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "externalRelatedReference_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("externalRelatedReference_id") REFERENCES "ExternalRelatedReference" (id)
);
CREATE TABLE "DetectionKit_certification" (
	"DetectionKit_id" INTEGER, 
	certification_id INTEGER, 
	PRIMARY KEY ("DetectionKit_id", certification_id), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY(certification_id) REFERENCES "Certification" (id)
);
CREATE TABLE "DetectionKit_fundingSource" (
	"DetectionKit_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("DetectionKit_id", "fundingSource_id"), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "DetectionKit_keyword" (
	"DetectionKit_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("DetectionKit_id", keyword), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id)
);
CREATE TABLE "DetectionKit_identifier" (
	"DetectionKit_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("DetectionKit_id", identifier), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id)
);
CREATE TABLE "DetectionKit_iri" (
	"DetectionKit_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("DetectionKit_id", iri), 
	FOREIGN KEY("DetectionKit_id") REFERENCES "DetectionKit" (id)
);
CREATE TABLE "Bundle_itemsOfTheBundle" (
	"Bundle_id" INTEGER, 
	"itemsOfTheBundle_id" INTEGER NOT NULL, 
	PRIMARY KEY ("Bundle_id", "itemsOfTheBundle_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("itemsOfTheBundle_id") REFERENCES "Product" (id)
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
CREATE TABLE "Bundle_doi" (
	"Bundle_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Bundle_id", doi_id), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Bundle_complementaryDocument" (
	"Bundle_id" INTEGER, 
	"complementaryDocument_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "complementaryDocument_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("complementaryDocument_id") REFERENCES "Document" (id)
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
CREATE TABLE "Bundle_fundingSource" (
	"Bundle_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Bundle_id", "fundingSource_id"), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Bundle_keyword" (
	"Bundle_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Bundle_id", keyword), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id)
);
CREATE TABLE "Bundle_identifier" (
	"Bundle_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Bundle_id", identifier), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id)
);
CREATE TABLE "Bundle_iri" (
	"Bundle_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Bundle_id", iri), 
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id)
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
CREATE TABLE "Pathogen_doi" (
	"Pathogen_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Pathogen_id", doi_id), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Pathogen_fundingSource" (
	"Pathogen_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Pathogen_id", "fundingSource_id"), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Pathogen_keyword" (
	"Pathogen_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Pathogen_id", keyword), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id)
);
CREATE TABLE "Pathogen_identifier" (
	"Pathogen_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Pathogen_id", identifier), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id)
);
CREATE TABLE "Pathogen_iri" (
	"Pathogen_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Pathogen_id", iri), 
	FOREIGN KEY("Pathogen_id") REFERENCES "Pathogen" (id)
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
CREATE TABLE "Virus_doi" (
	"Virus_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Virus_id", doi_id), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Virus_fundingSource" (
	"Virus_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Virus_id", "fundingSource_id"), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Virus_keyword" (
	"Virus_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Virus_id", keyword), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id)
);
CREATE TABLE "Virus_identifier" (
	"Virus_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Virus_id", identifier), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id)
);
CREATE TABLE "Virus_iri" (
	"Virus_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Virus_id", iri), 
	FOREIGN KEY("Virus_id") REFERENCES "Virus" (id)
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
CREATE TABLE "Bacterium_doi" (
	"Bacterium_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Bacterium_id", doi_id), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Bacterium_fundingSource" (
	"Bacterium_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Bacterium_id", "fundingSource_id"), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Bacterium_keyword" (
	"Bacterium_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Bacterium_id", keyword), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id)
);
CREATE TABLE "Bacterium_identifier" (
	"Bacterium_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Bacterium_id", identifier), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id)
);
CREATE TABLE "Bacterium_iri" (
	"Bacterium_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Bacterium_id", iri), 
	FOREIGN KEY("Bacterium_id") REFERENCES "Bacterium" (id)
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
CREATE TABLE "Fungus_doi" (
	"Fungus_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Fungus_id", doi_id), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Fungus_fundingSource" (
	"Fungus_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Fungus_id", "fundingSource_id"), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Fungus_keyword" (
	"Fungus_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Fungus_id", keyword), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id)
);
CREATE TABLE "Fungus_identifier" (
	"Fungus_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Fungus_id", identifier), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id)
);
CREATE TABLE "Fungus_iri" (
	"Fungus_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Fungus_id", iri), 
	FOREIGN KEY("Fungus_id") REFERENCES "Fungus" (id)
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
CREATE TABLE "Protozoan_doi" (
	"Protozoan_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Protozoan_id", doi_id), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Protozoan_fundingSource" (
	"Protozoan_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Protozoan_id", "fundingSource_id"), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Protozoan_keyword" (
	"Protozoan_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Protozoan_id", keyword), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id)
);
CREATE TABLE "Protozoan_identifier" (
	"Protozoan_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Protozoan_id", identifier), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id)
);
CREATE TABLE "Protozoan_iri" (
	"Protozoan_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Protozoan_id", iri), 
	FOREIGN KEY("Protozoan_id") REFERENCES "Protozoan" (id)
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
CREATE TABLE "Viroid_doi" (
	"Viroid_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Viroid_id", doi_id), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Viroid_fundingSource" (
	"Viroid_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Viroid_id", "fundingSource_id"), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Viroid_keyword" (
	"Viroid_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Viroid_id", keyword), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id)
);
CREATE TABLE "Viroid_identifier" (
	"Viroid_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Viroid_id", identifier), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id)
);
CREATE TABLE "Viroid_iri" (
	"Viroid_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Viroid_id", iri), 
	FOREIGN KEY("Viroid_id") REFERENCES "Viroid" (id)
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
CREATE TABLE "Prion_doi" (
	"Prion_id" INTEGER, 
	doi_id INTEGER, 
	PRIMARY KEY ("Prion_id", doi_id), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY(doi_id) REFERENCES "Doi" (id)
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
CREATE TABLE "Prion_fundingSource" (
	"Prion_id" INTEGER, 
	"fundingSource_id" INTEGER, 
	PRIMARY KEY ("Prion_id", "fundingSource_id"), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id), 
	FOREIGN KEY("fundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "Prion_keyword" (
	"Prion_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("Prion_id", keyword), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id)
);
CREATE TABLE "Prion_identifier" (
	"Prion_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("Prion_id", identifier), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id)
);
CREATE TABLE "Prion_iri" (
	"Prion_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("Prion_id", iri), 
	FOREIGN KEY("Prion_id") REFERENCES "Prion" (id)
);
CREATE TABLE "FundingSource_keyword" (
	"FundingSource_id" INTEGER, 
	keyword TEXT, 
	PRIMARY KEY ("FundingSource_id", keyword), 
	FOREIGN KEY("FundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "FundingSource_identifier" (
	"FundingSource_id" INTEGER, 
	identifier TEXT, 
	PRIMARY KEY ("FundingSource_id", identifier), 
	FOREIGN KEY("FundingSource_id") REFERENCES "FundingSource" (id)
);
CREATE TABLE "FundingSource_iri" (
	"FundingSource_id" INTEGER, 
	iri TEXT, 
	PRIMARY KEY ("FundingSource_id", iri), 
	FOREIGN KEY("FundingSource_id") REFERENCES "FundingSource" (id)
);
