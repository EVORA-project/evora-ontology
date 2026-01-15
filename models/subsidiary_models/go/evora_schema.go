package EVORAO

/*
 * Resource published or curated by a single agent.
 */
type Resource struct {
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A collection of data, published or curated by a single agent, and available for access.
 */
type Dataset struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A collection of operations that provides access to one or more datasets or data processing functions.
 */
type DataService struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The URL template that allows to get the content.
	 */
	EndpointUrl string `json:"endpointUrl"`
	/*
	 * A collection of data that this data service can distribute.
	 */
	ServesDataset []Dataset `json:"servesDataset"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards).
 */
type Version struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * Identifier of what type of entities the version qualifies.
	 */
	VersionOf string `json:"versionOf"`
	/*
	 * Resource published or curated by a single agent.
	 */
	Resource []Resource `json:"resource"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A curated collection of metadata about resources.
 */
type Catalogue struct {
	/*
	 * parent types
	 */
	Dataset
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A structured representation of data about the classification and naming of biological organisms into groups according to shared characteristics.
 */
type Taxonomy struct {
	/*
	 * parent types
	 */
	Catalogue
	/*
	 * Scientifically classified group or entity within the reference taxonomy.
	 */
	Taxon []Taxon `json:"taxon"`
	/*
	 * The data provider for the taxons of the taxonomy.
	 */
	TaxonDataProvider DataProvider `json:"taxonDataProvider"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * The data provider for the Version ID of this taxonomy.
	 */
	VersionDataProvider DataProvider `json:"versionDataProvider"`
	/*
	 * Relative level or position of the identified taxon in the taxonomy.
	 */
	Rank []TaxonomicRank `json:"rank"`
	/*
	 * The data provider for the description of the taxonomic ranks used in this taxonomy.
	 */
	RankDataProvider DataProvider `json:"rankDataProvider"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources.
 */
type DataProvider struct {
	/*
	 * parent types
	 */
	DataService
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * The http request method used to acces the login request url.
	 */
	LoginRequestMethod string `json:"loginRequestMethod"`
	/*
	 * The URL template that allows to log in if required.
	 */
	LoginUrl string `json:"loginUrl"`
	/*
	 * The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query.
	 */
	LoginTokenName string `json:"loginTokenName"`
	/*
	 * The http request method used to access the requested query url.
	 */
	QueryMethod string `json:"queryMethod"`
	/*
	 * The content type of the response to queries. It specifies the serialization, file type, or media type used to convey the resource, typically expressed as a MIME type following IANA media type registrations.
	 */
	ContentType string `json:"contentType"`
	/*
	 * Identifies the type of entity (ontology class) described by the response to a query. Values should be expressed as IRIs (e.g., from an ontology).
	 */
	ProvidedEntityType string `json:"providedEntityType"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The URL template that allows to get the content.
	 */
	EndpointUrl string `json:"endpointUrl"`
	/*
	 * A collection of data that this data service can distribute.
	 */
	ServesDataset []Dataset `json:"servesDataset"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A collection of distinguishing information that enables the differentiation of a pathogen from another.
 */
type PathogenIdentification struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * Scientifically classified group or entity within the reference taxonomy.
	 */
	Taxon Taxon `json:"taxon"`
	/*
	 * A pathogen common name or a name that describes a group of pathogens.
	 */
	PathogenName CommonName `json:"pathogenName"`
	/*
	 * Identification of the specific type of pathogen among the listed categories e.g. 'Virus','Viroid','Bacterium'...
	 */
	PathogenType string `json:"pathogenType"`
	/*
	 * Indication of the possible host(s) for the identified pathogens among the listed main categories.
	 */
	HostType string `json:"hostType"`
	/*
	 * The subspecies information differentiates closely related pathogens within a single species.
	 */
	Subspecies string `json:"subspecies"`
	/*
	 * Identifier given to a genetic variant within a single species.
	 */
	Strain string `json:"strain"`
	/*
	 * Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host.
	 */
	Isolate string `json:"isolate"`
	/*
	 * Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes.
	 */
	Genotype string `json:"genotype"`
	/*
	 * Genetically related pathogens that group together based on serological relationships.
	 */
	Serotype string `json:"serotype"`
	/*
	 * An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain.
	 */
	Variant Variant `json:"variant"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A scientific publication.
 */
type Publication struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * The list of authors.
	 */
	Authors string `json:"authors"`
	/*
	 * Concise summary of the publication.
	 */
	Abstract string `json:"abstract"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi Doi `json:"doi"`
	/*
	 * The scientific journal in which the publication was published.
	 */
	Journal Journal `json:"journal"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A subset of words or phrases specific to a particular subject or field.
 */
type Vocabulary struct {
	/*
	 * parent types
	 */
	Catalogue
	/*
	 * An external API or Endpoint that permits to retrieve the terms of this vocabulary.
	 */
	TermDataProvider DataProvider `json:"termDataProvider"`
	/*
	 * The terms related to this vocabulary.
	 */
	Term []Term `json:"term"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Word or phrase from a specialized area of knowledge.
 */
type Term struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Vernacular name that is the name used in everyday language to refer to something like an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific or technical name.
 */
type CommonName struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The name of the origin from which knowledge is obtained. This can include any entity that provides information.
	 */
	SourceOfInformation string `json:"sourceOfInformation"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A virus vernacular name or a name that describes a group of viruses.
 */
type VirusName struct {
	/*
	 * parent types
	 */
	CommonName
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The name of the origin from which knowledge is obtained. This can include any entity that provides information.
	 */
	SourceOfInformation string `json:"sourceOfInformation"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * List of other names for things.
 */
type AlternateName struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The name of the origin from which knowledge is obtained. This can include any entity that provides information.
	 */
	SourceOfInformation string `json:"sourceOfInformation"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence.
 */
type RiskGroup struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
 */
type BiosafetyLevel struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard.
 */
type Doi struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Periodical journal publishing scientific research.
 */
type Journal struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Identifier for 3D structural data as per the PDB (Protein Data Bank) database.
 */
type PdbReference struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A term or phrase used to tag and categorize content.
 */
type Keyword struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids.
 */
type TagSequence struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
 */
type SpecialFeature struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression.
 */
type ExpressionVector struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers.
 */
type PlasmidSelection struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The organism used to grow and multiply the pathogen under controlled conditions.
 */
type PropagationHost struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The process by which the pathogen spreads between hosts.
 */
type TransmissionMethod struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances.
 */
type ProductionCellLine struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A term used to classify a group of products that share common characteristics or functions, which helps in their organization.
 */
type ProductCategory struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.
	 */
	ParentCategory ProductCategory `json:"parentCategory"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Host organism from which the pathogen was isolated.
 */
type IsolationHost struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The specific location or region where a physical item, originates or is naturally found.
 */
type GeographicalOrigin struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The IPLC area (Indigenous People and Local Communities) from which a physical item originates.
 */
type IplcOrigin struct {
	/*
	 * parent types
	 */
	GeographicalOrigin
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The country as of ISO3166.
 */
type Country struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * Two-letter country codes from ISO 3166-1 alpha-2.
	 */
	Alpha2Code string `json:"alpha2Code"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air.
 */
type IataClassification struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain.
 */
type Variant struct {
	/*
	 * parent types
	 */
	CommonName
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The name of the origin from which knowledge is obtained. This can include any entity that provides information.
	 */
	SourceOfInformation string `json:"sourceOfInformation"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The possible taxonomic ranks and their description.
 */
type TaxonomicRank struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * The taxonomy release(s) in which this entity exists.
	 */
	Taxonomy []Taxonomy `json:"taxonomy"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit.
 */
type Taxon struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * The taxonomy release(s) in which this entity exists.
	 */
	Taxonomy []Taxonomy `json:"taxonomy"`
	/*
	 * The parent taxon of the current taxon.
	 */
	ParentTaxon Taxon `json:"parentTaxon"`
	/*
	 * Relative level or position of the identified taxon in the taxonomy.
	 */
	Rank TaxonomicRank `json:"rank"`
	/*
	 * Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI).
	 */
	ExternalEquivalentTaxon []Taxon `json:"externalEquivalentTaxon"`
	/*
	 * The taxonomic identifier as a persistent identifier accross releases.
	 */
	TaxonomicId string `json:"taxonomicId"`
	/*
	 * The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy.
	 */
	TaxonomicNodeId string `json:"taxonomicNodeId"`
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * Any historic version of this taxon having a different name.
	 */
	PreviouslyKnownAs []Taxon `json:"previouslyKnownAs"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health.
 */
type ClinicalGroup struct {
	/*
	 * parent types
	 */
	Term
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * Scientifically classified group or entity within the reference taxonomy.
	 */
	Taxon []Taxon `json:"taxon"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0.
	 */
	Weight int `json:"weight"`
	/*
	 * Terms belong to a specific vocabulary.
	 */
	InVocabulary Vocabulary `json:"inVocabulary"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A reference that permits to retrieve an item from an external provider.
 */
type ExternalRelatedReference struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * The identifier reference of the connected external item.
	 */
	Reference string `json:"reference"`
	/*
	 * The label informing what this reference is about.
	 */
	ReferenceLabel string `json:"referenceLabel"`
	/*
	 * The url prefix that once completed with the reference will lead to the linked external resource.
	 */
	ReferenceProviderPrefix string `json:"referenceProviderPrefix"`
	/*
	 * The name for the reference provider.
	 */
	ReferenceProviderName string `json:"referenceProviderName"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A nucleic acid or protein sequence information.
 */
type Sequence struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A reference that permits to retrieve the sequence information from a sequence provider.
	 */
	SequenceReference []SequenceReference `json:"sequenceReference"`
	/*
	 * Textual encoding of a biological sequence information in FASTA format.
	 */
	SequenceFasta string `json:"sequenceFasta"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A reference that permits to retrieve the sequence information from a sequence provider.
 */
type SequenceReference struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * The sequence ID that permits to retrieve the sequence information from the sequence provider.
	 */
	AccessionNumber string `json:"accessionNumber"`
	/*
	 * The name of the sequence provider within the list of accepted sequence providers.
	 */
	SequenceProvider string `json:"sequenceProvider"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A person or an organization.
 */
type PersonOrOrganization struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An individual.
 */
type Person struct {
	/*
	 * parent types
	 */
	PersonOrOrganization
	/*
	 * Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation.
	 */
	OrcidId string `json:"orcidId"`
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A social entity established to meet needs or pursue specific goals.
 */
type Organization struct {
	/*
	 * parent types
	 */
	PersonOrOrganization
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The country of the organization.
	 */
	Country Country `json:"country"`
	/*
	 * The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
	 */
	RorId string `json:"rorId"`
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A research infrastructure (RI).
 */
type ResearchInfrastructure struct {
	/*
	 * parent types
	 */
	Organization
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The country of the organization.
	 */
	Country Country `json:"country"`
	/*
	 * The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
	 */
	RorId string `json:"rorId"`
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A provider of products or services, as a specific organization.
 */
type Provider struct {
	/*
	 * parent types
	 */
	Organization
	/*
	 * The research infrastructure of which this organization is a member.
	 */
	MemberOfRi []ResearchInfrastructure `json:"memberOfRi"`
	/*
	 * Any other name under which the entity can be known.
	 */
	AlternateName []AlternateName `json:"alternateName"`
	/*
	 * The country of the organization.
	 */
	Country Country `json:"country"`
	/*
	 * The corresponding organization's persistent identifier from the Research Organization Registry (ROR).
	 */
	RorId string `json:"rorId"`
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
 */
type Originator struct {
	/*
	 * parent types
	 */
	PersonOrOrganization
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A web page that serves as the main or introductory page.
	 */
	HomePage string `json:"homePage"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
 */
type BiologicalMaterialOrigin struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * Indicates if this biological material is a recombinant biological material.
	 */
	RecombinantMaterial bool `json:"recombinantMaterial"`
	/*
	 * Indicates whether the biological material includes any part originally collected from a natural source (true) or is composed exclusively of synthetic parts (false).
	 */
	BiologicalSourceType bool `json:"biologicalSourceType"`
	/*
	 * Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.
	 */
	BiologicalPartOrigin []BiologicalPartOrigin `json:"biologicalPartOrigin"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material.
 */
type BiologicalPartOrigin struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * Identification of a recombinant part.
	 */
	RecombinantPartIdentification RecombinantPartIdentification `json:"recombinantPartIdentification"`
	/*
	 * Indicate if the biological part was produced with access to a physical genetic resource.
	 */
	AccessToPhysicalGeneticResource bool `json:"accessToPhysicalGeneticResource"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Information on the origin of a natural part that composes the biological material.
 */
type NaturalPartOrigin struct {
	/*
	 * parent types
	 */
	BiologicalPartOrigin
	/*
	 * The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to 'country of origin'.
	 */
	CountryOfCollection Country `json:"countryOfCollection"`
	/*
	 * The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant.
	 */
	IndigenousPeopleAndLocalCommunityOrigin IplcOrigin `json:"indigenousPeopleAndLocalCommunityOrigin"`
	/*
	 * The date when the sample was collected in situ. If unknown/private, use a proxy date such as 'date received' and indicate this by setting to true the before date property.
	 */
	CollectionDate string `json:"collectionDate"`
	/*
	 * Set to TRUE if a proxy date for the collection date is used.
	 */
	CollectedBeforeDate bool `json:"collectedBeforeDate"`
	/*
	 * Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations.
	 */
	PermitIdentifierForAbs string `json:"permitIdentifierForAbs"`
	/*
	 * Identification of a recombinant part.
	 */
	RecombinantPartIdentification RecombinantPartIdentification `json:"recombinantPartIdentification"`
	/*
	 * Indicate if the biological part was produced with access to a physical genetic resource.
	 */
	AccessToPhysicalGeneticResource bool `json:"accessToPhysicalGeneticResource"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Information on the origin of a synthetic part that composes the biological material.
 */
type SyntheticPartOrigin struct {
	/*
	 * parent types
	 */
	BiologicalPartOrigin
	/*
	 * Set to TRUE if there was is any modification made from the reference sequence.
	 */
	ModificationsFromTheReferenceSequences bool `json:"modificationsFromTheReferenceSequences"`
	/*
	 * List the modifications mades from the reference sequence if any.
	 */
	DescriptionOfModificationsMadeFromTheReferenceSequences string `json:"descriptionOfModificationsMadeFromTheReferenceSequences"`
	/*
	 * Identification of a recombinant part.
	 */
	RecombinantPartIdentification RecombinantPartIdentification `json:"recombinantPartIdentification"`
	/*
	 * Indicate if the biological part was produced with access to a physical genetic resource.
	 */
	AccessToPhysicalGeneticResource bool `json:"accessToPhysicalGeneticResource"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Identification of a recombinant part.
 */
type RecombinantPartIdentification struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A short designation of this recombinant part of the related biological material.
	 */
	PartIdentification string `json:"partIdentification"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Set of products and services with some common characteristics.
 */
type Collection struct {
	/*
	 * parent types
	 */
	Catalogue
	/*
	 * An item of the collection.
	 */
	CollectionItem []ProductOrService `json:"collectionItem"`
	/*
	 * The provider of the data of the collection.
	 */
	CollectionDataProvider DataProvider `json:"collectionDataProvider"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An offering provided by a provider, which may be tangible (a product) or intangible (a service).
 */
type ProductOrService struct {
	/*
	 * parent types
	 */
	Dataset
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An intangible offering characterized by an activity, performance, or facilitation carried out by a provider to fulfill a user’s need.
 */
type Service struct {
	/*
	 * parent types
	 */
	ProductOrService
	/*
	 * The species of the infected organism in the experiment.
	 */
	ModelSpecies string `json:"modelSpecies"`
	/*
	 * The specific name of the infected organism, including its modification if necessary.
	 */
	ModelType string `json:"modelType"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A tangible, physical item made available by a provider for use, consumption, or ownership transfer.
 */
type Product struct {
	/*
	 * parent types
	 */
	ProductOrService
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Protein that can bind to certain types of foreign bodies, such as pathogens.
 */
type Antibody struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * The biological and technological methods and processes used to produce the antibody.
	 */
	ProductionSystem string `json:"productionSystem"`
	/*
	 * Indicates whether or not if the antibody was purified by affinity.
	 */
	AntibodyPurifiedByAffinity bool `json:"antibodyPurifiedByAffinity"`
	/*
	 * Boolean value indicating whether the specificity of the product has been formally documented.
	 */
	SpecificityDocumented bool `json:"specificityDocumented"`
	/*
	 * Information describing the molecular or antigenic specificity of the antibody, including its recognized target(s), cross-reactivity with related antigens, and any contextual information supporting its selectivity.
	 */
	AntibodySpecificity string `json:"antibodySpecificity"`
	/*
	 * Specific molecular structure or epitope recognized and bound by an antibody.
	 */
	TargetedAntigen string `json:"targetedAntigen"`
	/*
	 * A reference that permits to retrieve the sequence information from a sequence provider.
	 */
	SequenceReference []SequenceReference `json:"sequenceReference"`
	/*
	 * The specification of the class of antibody based on its production method or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"
	 */
	AntibodyType string `json:"antibodyType"`
	/*
	 * A method used to determine the specificity, affinity, or functionality of an antibody or antiserum.
	 */
	AntibodyCharacterizationMethod string `json:"antibodyCharacterizationMethod"`
	/*
	 * A statement summarizing observed characteristics, behaviors, or findings derived from the antibody characterization process.
	 */
	AntibodyCharacterizationObservation string `json:"antibodyCharacterizationObservation"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * An hybridoma that provides antibodies that can be related to a pathogen.
 */
type Hybridoma struct {
	/*
	 * parent types
	 */
	Antibody
	/*
	 * The description of the hybridoma.
	 */
	HybridomaDescription string `json:"hybridomaDescription"`
	/*
	 * The biological and technological methods and processes used to produce the antibody.
	 */
	ProductionSystem string `json:"productionSystem"`
	/*
	 * Indicates whether or not if the antibody was purified by affinity.
	 */
	AntibodyPurifiedByAffinity bool `json:"antibodyPurifiedByAffinity"`
	/*
	 * Boolean value indicating whether the specificity of the product has been formally documented.
	 */
	SpecificityDocumented bool `json:"specificityDocumented"`
	/*
	 * Information describing the molecular or antigenic specificity of the antibody, including its recognized target(s), cross-reactivity with related antigens, and any contextual information supporting its selectivity.
	 */
	AntibodySpecificity string `json:"antibodySpecificity"`
	/*
	 * Specific molecular structure or epitope recognized and bound by an antibody.
	 */
	TargetedAntigen string `json:"targetedAntigen"`
	/*
	 * A reference that permits to retrieve the sequence information from a sequence provider.
	 */
	SequenceReference []SequenceReference `json:"sequenceReference"`
	/*
	 * The specification of the class of antibody based on its production method or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"
	 */
	AntibodyType string `json:"antibodyType"`
	/*
	 * A method used to determine the specificity, affinity, or functionality of an antibody or antiserum.
	 */
	AntibodyCharacterizationMethod string `json:"antibodyCharacterizationMethod"`
	/*
	 * A statement summarizing observed characteristics, behaviors, or findings derived from the antibody characterization process.
	 */
	AntibodyCharacterizationObservation string `json:"antibodyCharacterizationObservation"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A protein as a derived product from a pathogen.
 */
type Protein struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * Identifier for 3D structural data as per the PDB (Protein Data Bank) database.
	 */
	RelatedPdb []PdbReference `json:"relatedPdb"`
	/*
	 * Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
	 */
	SpecialFeature []SpecialFeature `json:"specialFeature"`
	/*
	 * The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids.
	 */
	TagSequence TagSequence `json:"tagSequence"`
	/*
	 * A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function.
	 */
	Domain string `json:"domain"`
	/*
	 * Refers to the form in which the protein is produced and manifested in a biological system. Possible values include 'Soluble' (proteins that are dissolved in the cellular or extracellular fluid) and 'Inclusion bodies' (aggregated proteins that are insoluble and form within the cell).
	 */
	ExpressedAs string `json:"expressedAs"`
	/*
	 * Refers to the state of aggregated proteins within a cell. Possible values include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded' (proteins have been processed to regain their functional, active conformation).
	 */
	InclusionBodiesType string `json:"inclusionBodiesType"`
	/*
	 * The host organism or cellular environment used to produce a protein from a specific gene. Possible values include 'E. coli' (bacterial system), 'Insect cells' (using baculovirus vectors), and 'Mammalian cells' (mammalian cell lines).
	 */
	ExpressionSystem string `json:"expressionSystem"`
	/*
	 * The process of determining and describing the specific biological activities and roles of a protein. Possible values include 'Functionally characterized' (the protein's functions have been identified and described) and 'No functional characterization' (the protein's functions have not been identified or described).
	 */
	FunctionalCharacterization string `json:"functionalCharacterization"`
	/*
	 * Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.
	 */
	FunctionalAndTechnicalDescription string `json:"functionalAndTechnicalDescription"`
	/*
	 * Refers to the degree of purity achieved for a protein sample. Possible values include '>95%' (the protein is highly purified, with more than 95% purity) and 'Unpurified expression host lysate or partly purified protein' (the protein is either unpurified and present in the host cell lysate or only partially purified).
	 */
	ProteinPurification string `json:"proteinPurification"`
	/*
	 * Indicates the presence and condition of a tag on the protein after solubilization. Possible values include 'Uncleaved Tag' (the tag is still attached to the protein), 'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein does not have a tag).
	 */
	TagStatusOfTheSolubilizedProtein string `json:"tagStatusOfTheSolubilizedProtein"`
	/*
	 * Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include 'Enzymatic' (the protein has been characterized for its enzyme activity) and 'Antigenic' (the protein has been characterized for its ability to elicit an immune response).
	 */
	TypeOfFunctionalCharacterization string `json:"typeOfFunctionalCharacterization"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Nucleic acid related to a pathogen. It can be extracted or synthetic.
 */
type NucleicAcid struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct.
	 */
	GenBankFileOfTheConstruct []Data `json:"genBankFileOfTheConstruct"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ClonedNucleicAcid bool `json:"clonedNucleicAcid"`
	/*
	 * The plasmid into which the nucleic acid has been cloned.
	 */
	ClonedIntoPlasmid ExpressionVector `json:"clonedIntoPlasmid"`
	/*
	 * Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid.
	 */
	PlasmidSelection []PlasmidSelection `json:"plasmidSelection"`
	/*
	 * The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids.
	 */
	TagSequence TagSequence `json:"tagSequence"`
	/*
	 * The specific region encompassed in the product.
	 */
	RegionEncompassedInThisProduct string `json:"regionEncompassedInThisProduct"`
	/*
	 * Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it contains mutations (no frameshift, no unexpected STOP codon) if set to true.
	 */
	MutationObserved bool `json:"mutationObserved"`
	/*
	 * The specific mutations that have been identified and documented in the nucleic acid sequence.
	 */
	ObservedMutations string `json:"observedMutations"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Refers to the level of sequencing performed on the nucleic acid. Possible values include 'Not sequenced' (no sequencing has been performed), 'Partly sequenced' (only a portion of the nucleic acid sequence has been determined), and 'Fully sequenced' (the entire nucleic acid sequence has been determined).
	 */
	Sequencing string `json:"sequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * Tell whether or not the sequence of the product was controlled, which is expected for sequenced nucleic acids and especially important for cloned ones.
	 */
	SequenceChecked bool `json:"sequenceChecked"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A detection kit for specific pathogens.
 */
type DetectionKit struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * The related standard operating procedure file (SOP).
	 */
	StandardOperatingProcedureFile []File `json:"standardOperatingProcedureFile"`
	/*
	 * Boolean value indicating whether the specificity of the product has been formally documented.
	 */
	SpecificityDocumented bool `json:"specificityDocumented"`
	/*
	 * Details on the ability of a detection kit to correctly identify negative results, distinguishing between the target analyte and other substances without cross-reacting.
	 */
	Specificity string `json:"specificity"`
	/*
	 * The specific area or sequence within the target analyte that the detection kit is designed to identify and interact with, ensuring accurate detection and analysis.
	 */
	TargetedRegion string `json:"targetedRegion"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A grouping of products and/or services intentionally combined into a single offering, typically to provide added value, convenience, or specific experimental utility.
 */
type Bundle struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * Specifies the constituent products and/or services that are part of the bundle.
	 */
	ItemsOfTheBundle []Product `json:"itemsOfTheBundle"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus.
 */
type Pathogen struct {
	/*
	 * parent types
	 */
	Product
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The virus as a biological material.
 */
type Virus struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.
	 */
	CoInfectingViruses []VirusName `json:"coInfectingViruses"`
	/*
	 * A boolean value indicating whether there is contamination with co-infecting viruses.
	 */
	ContaminationWithCoInfectingViruses bool `json:"contaminationWithCoInfectingViruses"`
	/*
	 * Indicates the presence of mycoplasma contamination within the sample.
	 */
	MycoplasmicContent bool `json:"mycoplasmicContent"`
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The bacterium as a biological material.
 */
type Bacterium struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The fungus as a biological material.
 */
type Fungus struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The protozoan as a biological material.
 */
type Protozoan struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The viroid as a biological material.
 */
type Viroid struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The prion as a biological material.
 */
type Prion struct {
	/*
	 * parent types
	 */
	Pathogen
	/*
	 * Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol.
	 */
	BiologicalMaterialOrigin BiologicalMaterialOrigin `json:"biologicalMaterialOrigin"`
	/*
	 * The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted.
	 */
	SuspectedEpidemiologicalOrigin []GeographicalOrigin `json:"suspectedEpidemiologicalOrigin"`
	/*
	 * The host organism from which the pathogen was originally isolated.
	 */
	IsolationHost []IsolationHost `json:"isolationHost"`
	/*
	 * The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study.
	 */
	ProductionCellLine []ProductionCellLine `json:"productionCellLine"`
	/*
	 * The host organism that propagates the pathogen.
	 */
	PropagationHost []PropagationHost `json:"propagationHost"`
	/*
	 * The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.
	 */
	TransmissionMethod []TransmissionMethod `json:"transmissionMethod"`
	/*
	 * The related sequence information from a sequence provider or in fasta format.
	 */
	Sequence []Sequence `json:"sequence"`
	/*
	 * The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'.
	 */
	Cultivability string `json:"cultivability"`
	/*
	 * Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes.
	 */
	ClinicalInformation string `json:"clinicalInformation"`
	/*
	 * A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis.
	 */
	IdentificationTechnique string `json:"identificationTechnique"`
	/*
	 * Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.
	 */
	Infectivity string `json:"infectivity"`
	/*
	 * The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism.
	 */
	InfectivityTest string `json:"infectivityTest"`
	/*
	 * The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process.
	 */
	IsolationTechnique string `json:"isolationTechnique"`
	/*
	 * The environmental and procedural conditions under which the pathogen was isolated.
	 */
	IsolationConditions string `json:"isolationConditions"`
	/*
	 * Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'.
	 */
	LetterOfAuthority string `json:"letterOfAuthority"`
	/*
	 * The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.
	 */
	Passage string `json:"passage"`
	/*
	 * The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material.
	 */
	GenomeSequencing string `json:"genomeSequencing"`
	/*
	 * The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading.
	 */
	Titer string `json:"titer"`
	/*
	 * The corresponding International Air Transport Association (IATA)'s category for this Product.
	 */
	IataClassification IataClassification `json:"iataClassification"`
	/*
	 * Specification of the terms and parameters for transporting.
	 */
	ShippingConditions string `json:"shippingConditions"`
	/*
	 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
	 */
	MaterialSafetyDataSheet MaterialSafetyDataSheet `json:"materialSafetyDataSheet"`
	/*
	 * The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample.
	 */
	Originator Originator `json:"originator"`
	/*
	 * Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.
	 */
	StorageConditions string `json:"storageConditions"`
	/*
	 * Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required.
	 */
	ThirdPartyDistributionConsent bool `json:"thirdPartyDistributionConsent"`
	/*
	 * Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material.
	 */
	UsageRestrictions string `json:"usageRestrictions"`
	/*
	 * The technique, method, or procedure employed to obtain or prepare the material prior to its use or storage.
	 */
	PreparationTechnique string `json:"preparationTechnique"`
	/*
	 * The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry.
	 */
	AccessPointUrl string `json:"accessPointUrl"`
	/*
	 * The reference or the stock keeping unit of the service or item provided in the provider's catalogue.
	 */
	RefSku string `json:"refSku"`
	/*
	 * A short description of what will be delivered by ordering one unit of this item.
	 */
	UnitDefinition string `json:"unitDefinition"`
	/*
	 * The main category of the service or product.
	 */
	Category ProductCategory `json:"category"`
	/*
	 * Any category apart from its main category in which this product or service can fit.
	 */
	AdditionalCategory []ProductCategory `json:"additionalCategory"`
	/*
	 * The cost per access for one unit as defined by the unit definition.
	 */
	UnitCost string `json:"unitCost"`
	/*
	 * The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD).
	 */
	UnitCostCurrency string `json:"unitCostCurrency"`
	/*
	 * A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume).
	 */
	UnitCostNote string `json:"unitCostNote"`
	/*
	 * Information that permits to assess the quality level of what will be provided.
	 */
	QualityGrading string `json:"qualityGrading"`
	/*
	 * The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.
	 */
	PathogenIdentification []PathogenIdentification `json:"pathogenIdentification"`
	/*
	 * A Digital Object Identifier (DOI) that can be related.
	 */
	Doi []Doi `json:"doi"`
	/*
	 * The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual.
	 */
	RiskGroup RiskGroup `json:"riskGroup"`
	/*
	 * The level of biocontainment required or applied in the facility where the biological agent is manipulated.
	 */
	BiosafetyLevel BiosafetyLevel `json:"biosafetyLevel"`
	/*
	 * Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service.
	 */
	BiosafetyRestrictions string `json:"biosafetyRestrictions"`
	/*
	 * Indicates if the current service or product can be used to produce GMO.
	 */
	CanBeUsedToProduceGmo bool `json:"canBeUsedToProduceGmo"`
	/*
	 * A provider of this product or service, as a specific organization.
	 */
	Provider Provider `json:"provider"`
	/*
	 * The collection(s) to which belongs this item.
	 */
	Collection []Collection `json:"collection"`
	/*
	 * List of terms used to tag and categorize this Item.
	 */
	Keywords []Keyword `json:"keywords"`
	/*
	 * The state or condition in which this item is accessible and ready for use or can be obtained.
	 */
	Availability string `json:"availability"`
	/*
	 * Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item.
	 */
	ComplementaryDocument []Document `json:"complementaryDocument"`
	/*
	 * Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions.
	 */
	TechnicalRecommendation string `json:"technicalRecommendation"`
	/*
	 * A picture that can represent the item.
	 */
	ProductPicture []Image `json:"productPicture"`
	/*
	 * A reference that permits to retrieve another related item from an external provider.
	 */
	ExternalRelatedReference []ExternalRelatedReference `json:"externalRelatedReference"`
	/*
	 * Any certification related to the current product or service; e.g., ISO certification.
	 */
	Certification []Certification `json:"certification"`
	/*
	 * Any reference or indication to be used for local retrieval purpose.
	 */
	InternalReference string `json:"internalReference"`
	/*
	 * An aditional information as a textual comment.
	 */
	Note string `json:"note"`
	/*
	 * An information that allows someone to establish communication.
	 */
	ContactPoint ContactPoint `json:"contactPoint"`
	/*
	 * A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially.
	 */
	FundingSource []FundingSource `json:"fundingSource"`
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The version indicator (name or identifier) of a resource.
	 */
	Version string `json:"version"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product.
 */
type MaterialSafetyDataSheet struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.
	 */
	MaterialSafetyContact ContactPoint `json:"materialSafetyContact"`
	/*
	 * Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage.
	 */
	PhysicalChemicalProperties string `json:"physicalChemicalProperties"`
	/*
	 * Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.
	 */
	HazardsIdentification string `json:"hazardsIdentification"`
	/*
	 * Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.
	 */
	FirstAidMeasures string `json:"firstAidMeasures"`
	/*
	 * Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.
	 */
	FireFightingMeasures string `json:"fireFightingMeasures"`
	/*
	 * Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.
	 */
	AccidentalReleaseMeasures string `json:"accidentalReleaseMeasures"`
	/*
	 * Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.
	 */
	HandlingAndStorage string `json:"handlingAndStorage"`
	/*
	 * Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.
	 */
	ExposureControlsPersonalProtection string `json:"exposureControlsPersonalProtection"`
	/*
	 * Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.
	 */
	StabilityAndReactivity string `json:"stabilityAndReactivity"`
	/*
	 * Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure.
	 */
	ToxicologicalInformation string `json:"toxicologicalInformation"`
	/*
	 * Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.
	 */
	EcologicalInformation string `json:"ecologicalInformation"`
	/*
	 * Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.
	 */
	DisposalConsiderations string `json:"disposalConsiderations"`
	/*
	 * Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.
	 */
	TransportInformation string `json:"transportInformation"`
	/*
	 * Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.
	 */
	RegulatoryInformation string `json:"regulatoryInformation"`
	/*
	 * Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.
	 */
	FurtherInformation string `json:"furtherInformation"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Digital document or record stored in a specific format that contains data or information.
 */
type File struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information.
 */
type Data struct {
	/*
	 * parent types
	 */
	File
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Subclass of File representing textual or written files such as reports, manuals, or forms.
 */
type Document struct {
	/*
	 * parent types
	 */
	File
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Subclass of File representing sound recordings or audio tracks.
 */
type Audio struct {
	/*
	 * parent types
	 */
	File
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Subclass of File representing moving visual media, such as recordings, presentations, or movies.
 */
type Video struct {
	/*
	 * parent types
	 */
	File
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Subclass of File representing visual content such as pictures, diagrams, or illustrations.
 */
type Image struct {
	/*
	 * parent types
	 */
	File
	/*
	 * An alternate text for the image, if the image cannot be displayed.
	 */
	AltText string `json:"altText"`
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the file content is stored and can be accessed or downloaded.
	 */
	ContentUrl string `json:"contentUrl"`
	/*
	 * The file type or format that indicates how the data within the file is structured.
	 */
	Format string `json:"format"`
	/*
	 * Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
	 */
	License License `json:"license"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Entity serving as focal point of information.
 */
type ContactPoint struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A word or set of words used to identify and refer to an entity.
	 */
	Name string `json:"name"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The email address.
	 */
	Email string `json:"email"`
	/*
	 * The telephone number.
	 */
	Telephone string `json:"telephone"`
	/*
	 * The building/apartment number and the street name.
	 */
	StreetAddress string `json:"streetAddress"`
	/*
	 * The locality in which the street address is, and which is in the region. e.g, the city.
	 */
	AddressLocality string `json:"addressLocality"`
	/*
	 * The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division.
	 */
	AddressRegion string `json:"addressRegion"`
	/*
	 * The postal code.
	 */
	PostalCode string `json:"postalCode"`
	/*
	 * The country as of  ISO 3166.
	 */
	AddressCountry Country `json:"addressCountry"`
	/*
	 * Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation.
	 */
	OrcidId string `json:"orcidId"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
 */
type License struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * The web address or location where the details or content is stored and can be accessed or downloaded.
	 */
	ResourceUrl string `json:"resourceUrl"`
	/*
	 * A text or html code that provides any related data sharing licence and/or attribution.
	 */
	LicensingOrAttribution string `json:"licensingOrAttribution"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * Assurance given by an independent certification body that a product, service or system meets the requirements of a standard.
 */
type Certification struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.
	 */
	CertificationDocument []Document `json:"certificationDocument"`
	/*
	 * The web address or location where the details or content is stored and can be accessed or downloaded.
	 */
	ResourceUrl string `json:"resourceUrl"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}

/*
 * A program, grant, or project providing financial support for the access or use of a product or service, either fully or partially.
 */
type FundingSource struct {
	/*
	 * parent types
	 */
	Resource
	/*
	 * A name given to the resource.
	 */
	Title string `json:"title"`
	/*
	 * A short explanation of the characteristics, features, or nature of the current item.
	 */
	Description string `json:"description"`
	/*
	 * Identifies the overarching financial framework, research initiative, or support mechanism that enables or contributes to the provision of a product or service. The value may correspond to a European funding framework (e.g. Horizon Europe), a specific research initiative (e.g. an EU project), or another public or private funding mechanism.
	 */
	FundingProgram string `json:"fundingProgram"`
	/*
	 * A formal reference or agreement number assigned by the funding body.
	 */
	GrantNumber string `json:"grantNumber"`
	/*
	 * The organization providing the financial support.
	 */
	Funder Organization `json:"funder"`
	/*
	 * The date from which the financial mechanism is active or applicable to the supported product or service.
	 */
	FundingPeriodStart time.Date `json:"fundingPeriodStart"`
	/*
	 * The date on which the financial mechanism ceases to apply to the supported product or service.
	 */
	FundingPeriodEnd time.Date `json:"fundingPeriodEnd"`
	/*
	 * Conditions under which individuals or organisations may benefit from the financial mechanism, including access rules, eligibility requirements, or geographical/institutional restrictions. May be expressed as text or as a link to a formal eligibility statement.
	 */
	EligibilityCriteria string `json:"eligibilityCriteria"`
	/*
	 * A path or URL to the related logo.
	 */
	Logo Image `json:"logo"`
	/*
	 * A keyword or tag describing the resource.
	 */
	Keyword string `json:"keyword"`
	/*
	 * Date of formal issuance (e.g., publication) of the resource.
	 */
	DateIssued string `json:"dateIssued"`
	/*
	 * Most recent date on which the resource was changed, updated or modified.
	 */
	DateModified string `json:"dateModified"`
	/*
	 * A unique identifier of the resource being described or cataloged.
	 */
	Identifier string `json:"identifier"`
	/*
	 * International Resource Identifier (IRI) that uniquely identifies or refers to the resource. IRIs include URIs, and URIs include URLs.
	 */
	Iri string `json:"iri"`
	/*
	 * The entity responsible for making the resource available.
	 */
	Publisher PersonOrOrganization `json:"publisher"`
}


