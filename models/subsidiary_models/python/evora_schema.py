# Auto generated from evora_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-13T11:30:26
# Schema: EVORAO
#
# id: https://w3id.org/evorao/
# description: The EVORAO Ontology provides a structured and harmonized vocabulary for describing shareable pathogens as characterized biological materials, along with their derived products and associated services, organized into collections. Developed within the EVORA project, it supports consistent metadata annotation across research infrastructures, promoting findability, accessibility, interoperability, and reusability (FAIR). By aligning with relevant standards and ontologies, EVORAO facilitates cross-domain collaboration, integration, and sharing of pathogenic resources and services to enhance pandemic preparedness and response. While initially focused on virology, EVORAO is designed to be extensible and also supports metadata harmonization for other pathogens.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDateTime

metamodel_version = "1.7.0"
version = "1.0.8687"

# Namespaces
EVORAO = CurieNamespace('EVORAO', 'https://w3id.org/evorao/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCMI = CurieNamespace('dcmi', 'http://purl.org/dc/dcmitype/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DWC = CurieNamespace('dwc', 'http://rs.tdwg.org/dwc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
ROV = CurieNamespace('rov', 'http://www.w3.org/ns/regorg#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
WDP = CurieNamespace('wdp', 'http://www.wikidata.org/prop/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EVORAO


# Types

# Class references



class Resource(YAMLRoot):
    """
    Resource published or curated by a single agent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = EVORAO.Resource


@dataclass(repr=False)
class Dataset(Resource):
    """
    A collection of data, published or curated by a single agent, and available for access
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = EVORAO.Dataset

    title: str = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataService(Resource):
    """
    A collection of operations that provides access to one or more datasets or data processing functions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = EVORAO.DataService

    title: str = None
    endpointURL: Union[str, URI] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.endpointURL):
            self.MissingRequiredField("endpointURL")
        if not isinstance(self.endpointURL, URI):
            self.endpointURL = URI(self.endpointURL)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Version(Resource):
    """
    Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Version"]
    class_class_curie: ClassVar[str] = "EVORAO:Version"
    class_name: ClassVar[str] = "Version"
    class_model_uri: ClassVar[URIRef] = EVORAO.Version

    ID: str = None
    versionOf: Union[dict, Dataset] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, str):
            self.ID = str(self.ID)

        if self._is_empty(self.versionOf):
            self.MissingRequiredField("versionOf")
        if not isinstance(self.versionOf, Dataset):
            self.versionOf = Dataset(**as_dict(self.versionOf))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalogue(Dataset):
    """
    A curated collection of metadata about resources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = EVORAO.Catalogue

    title: str = None
    description: str = None

@dataclass(repr=False)
class Taxonomy(Catalogue):
    """
    Science of naming, defining and classifying organisms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Taxonomy"]
    class_class_curie: ClassVar[str] = "EVORAO:Taxonomy"
    class_name: ClassVar[str] = "Taxonomy"
    class_model_uri: ClassVar[URIRef] = EVORAO.Taxonomy

    title: str = None
    description: str = None
    taxon: Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]] = None
    version: Union[dict, Version] = None
    versionDataProvider: Union[dict, "DataProvider"] = None
    rank: Union[Union[dict, "TaxonomicRank"], list[Union[dict, "TaxonomicRank"]]] = None
    taxonDataProvider: Optional[Union[dict, "DataProvider"]] = None
    rankDataProvider: Optional[Union[dict, "DataProvider"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        self._normalize_inlined_as_dict(slot_name="taxon", slot_type=Taxon, key_name="title", keyed=False)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, Version):
            self.version = Version(**as_dict(self.version))

        if self._is_empty(self.versionDataProvider):
            self.MissingRequiredField("versionDataProvider")
        if not isinstance(self.versionDataProvider, DataProvider):
            self.versionDataProvider = DataProvider(**as_dict(self.versionDataProvider))

        if self._is_empty(self.rank):
            self.MissingRequiredField("rank")
        self._normalize_inlined_as_dict(slot_name="rank", slot_type=TaxonomicRank, key_name="title", keyed=False)

        if self.taxonDataProvider is not None and not isinstance(self.taxonDataProvider, DataProvider):
            self.taxonDataProvider = DataProvider(**as_dict(self.taxonDataProvider))

        if self.rankDataProvider is not None and not isinstance(self.rankDataProvider, DataProvider):
            self.rankDataProvider = DataProvider(**as_dict(self.rankDataProvider))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProvider(DataService):
    """
    An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["DataProvider"]
    class_class_curie: ClassVar[str] = "EVORAO:DataProvider"
    class_name: ClassVar[str] = "DataProvider"
    class_model_uri: ClassVar[URIRef] = EVORAO.DataProvider

    title: str = None
    endpointURL: Union[str, URI] = None
    queryMethod: str = None
    providedEntityType: Union[dict, Dataset] = None
    contentType: str = "JSON"
    weight: int = 0
    license: Optional[Union[dict, "License"]] = None
    loginRequestMethod: Optional[str] = "GET"
    loginURL: Optional[Union[str, URI]] = None
    loginTokenName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.queryMethod):
            self.MissingRequiredField("queryMethod")
        if not isinstance(self.queryMethod, str):
            self.queryMethod = str(self.queryMethod)

        if self._is_empty(self.contentType):
            self.MissingRequiredField("contentType")
        if not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        if self._is_empty(self.providedEntityType):
            self.MissingRequiredField("providedEntityType")
        if not isinstance(self.providedEntityType, Dataset):
            self.providedEntityType = Dataset(**as_dict(self.providedEntityType))

        if self._is_empty(self.weight):
            self.MissingRequiredField("weight")
        if not isinstance(self.weight, int):
            self.weight = int(self.weight)

        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self.loginRequestMethod is not None and not isinstance(self.loginRequestMethod, str):
            self.loginRequestMethod = str(self.loginRequestMethod)

        if self.loginURL is not None and not isinstance(self.loginURL, URI):
            self.loginURL = URI(self.loginURL)

        if self.loginTokenName is not None and not isinstance(self.loginTokenName, str):
            self.loginTokenName = str(self.loginTokenName)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathogenIdentification(Resource):
    """
    A collection of distinguishing information that enables the differentiation of a pathogen from another
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["PathogenIdentification"]
    class_class_curie: ClassVar[str] = "EVORAO:PathogenIdentification"
    class_name: ClassVar[str] = "PathogenIdentification"
    class_model_uri: ClassVar[URIRef] = EVORAO.PathogenIdentification

    taxon: Union[dict, "Taxon"] = None
    pathogenName: Union[dict, "CommonName"] = None
    pathogenType: str = None
    hostType: Optional[Union[str, list[str]]] = empty_list()
    subspecies: Optional[str] = None
    strain: Optional[str] = None
    isolate: Optional[str] = None
    genotype: Optional[str] = None
    serotype: Optional[str] = None
    variant: Optional[Union[dict, "Variant"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, Taxon):
            self.taxon = Taxon(**as_dict(self.taxon))

        if self._is_empty(self.pathogenName):
            self.MissingRequiredField("pathogenName")
        if not isinstance(self.pathogenName, CommonName):
            self.pathogenName = CommonName(**as_dict(self.pathogenName))

        if self._is_empty(self.pathogenType):
            self.MissingRequiredField("pathogenType")
        if not isinstance(self.pathogenType, str):
            self.pathogenType = str(self.pathogenType)

        if not isinstance(self.hostType, list):
            self.hostType = [self.hostType] if self.hostType is not None else []
        self.hostType = [v if isinstance(v, str) else str(v) for v in self.hostType]

        if self.subspecies is not None and not isinstance(self.subspecies, str):
            self.subspecies = str(self.subspecies)

        if self.strain is not None and not isinstance(self.strain, str):
            self.strain = str(self.strain)

        if self.isolate is not None and not isinstance(self.isolate, str):
            self.isolate = str(self.isolate)

        if self.genotype is not None and not isinstance(self.genotype, str):
            self.genotype = str(self.genotype)

        if self.serotype is not None and not isinstance(self.serotype, str):
            self.serotype = str(self.serotype)

        if self.variant is not None and not isinstance(self.variant, Variant):
            self.variant = Variant(**as_dict(self.variant))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(Resource):
    """
    A scientific publication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Publication"]
    class_class_curie: ClassVar[str] = "EVORAO:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = EVORAO.Publication

    title: str = None
    authors: str = None
    abstract: str = None
    relatedDOI: Union[Union[dict, "DOI"], list[Union[dict, "DOI"]]] = None
    journal: Optional[Union[dict, "Journal"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.authors):
            self.MissingRequiredField("authors")
        if not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self._is_empty(self.abstract):
            self.MissingRequiredField("abstract")
        if not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self._is_empty(self.relatedDOI):
            self.MissingRequiredField("relatedDOI")
        self._normalize_inlined_as_dict(slot_name="relatedDOI", slot_type=DOI, key_name="title", keyed=False)

        if self.journal is not None and not isinstance(self.journal, Journal):
            self.journal = Journal(**as_dict(self.journal))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vocabulary(Catalogue):
    """
    A subset of words or phrases specific to a particular subject or field
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Vocabulary"]
    class_class_curie: ClassVar[str] = "EVORAO:Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = EVORAO.Vocabulary

    title: str = None
    description: str = None
    termDataProvider: Optional[Union[dict, DataProvider]] = None
    term: Optional[Union[Union[dict, "Term"], list[Union[dict, "Term"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.termDataProvider is not None and not isinstance(self.termDataProvider, DataProvider):
            self.termDataProvider = DataProvider(**as_dict(self.termDataProvider))

        self._normalize_inlined_as_dict(slot_name="term", slot_type=Term, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(Resource):
    """
    Word or phrase from a specialized area of knowledge
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Term"]
    class_class_curie: ClassVar[str] = "EVORAO:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = EVORAO.Term

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.weight):
            self.MissingRequiredField("weight")
        if not isinstance(self.weight, int):
            self.weight = int(self.weight)

        if self._is_empty(self.inVocabulary):
            self.MissingRequiredField("inVocabulary")
        if not isinstance(self.inVocabulary, Vocabulary):
            self.inVocabulary = Vocabulary(**as_dict(self.inVocabulary))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonName(Term):
    """
    Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This
    name is typically easier to remember and pronounce compared to the scientific name
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["CommonName"]
    class_class_curie: ClassVar[str] = "EVORAO:CommonName"
    class_name: ClassVar[str] = "CommonName"
    class_model_uri: ClassVar[URIRef] = EVORAO.CommonName

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    alternateName: Optional[Union[Union[dict, "AlternateName"], list[Union[dict, "AlternateName"]]]] = empty_list()
    sourceOfInformation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="alternateName", slot_type=AlternateName, key_name="title", keyed=False)

        if not isinstance(self.sourceOfInformation, list):
            self.sourceOfInformation = [self.sourceOfInformation] if self.sourceOfInformation is not None else []
        self.sourceOfInformation = [v if isinstance(v, str) else str(v) for v in self.sourceOfInformation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirusName(CommonName):
    """
    A virus vernacular name or a name that describes a group of viruses
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["VirusName"]
    class_class_curie: ClassVar[str] = "EVORAO:VirusName"
    class_name: ClassVar[str] = "VirusName"
    class_model_uri: ClassVar[URIRef] = EVORAO.VirusName

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class AlternateName(Term):
    """
    List of other names for things
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["AlternateName"]
    class_class_curie: ClassVar[str] = "EVORAO:AlternateName"
    class_name: ClassVar[str] = "AlternateName"
    class_model_uri: ClassVar[URIRef] = EVORAO.AlternateName

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    alternateName: Optional[Union[Union[dict, "AlternateName"], list[Union[dict, "AlternateName"]]]] = empty_list()
    sourceOfInformation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="alternateName", slot_type=AlternateName, key_name="title", keyed=False)

        if not isinstance(self.sourceOfInformation, list):
            self.sourceOfInformation = [self.sourceOfInformation] if self.sourceOfInformation is not None else []
        self.sourceOfInformation = [v if isinstance(v, str) else str(v) for v in self.sourceOfInformation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskGroup(Term):
    """
    Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate
    to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["RiskGroup"]
    class_class_curie: ClassVar[str] = "EVORAO:RiskGroup"
    class_name: ClassVar[str] = "RiskGroup"
    class_model_uri: ClassVar[URIRef] = EVORAO.RiskGroup

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class DOI(Term):
    """
    A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and
    access. The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["DOI"]
    class_class_curie: ClassVar[str] = "EVORAO:DOI"
    class_name: ClassVar[str] = "DOI"
    class_model_uri: ClassVar[URIRef] = EVORAO.DOI

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Journal(Term):
    """
    Periodical journal publishing scientific research
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Journal"]
    class_class_curie: ClassVar[str] = "EVORAO:Journal"
    class_name: ClassVar[str] = "Journal"
    class_model_uri: ClassVar[URIRef] = EVORAO.Journal

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PDBReference(Term):
    """
    Identifier for 3D structural data as per the PDB (Protein Data Bank) database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["PDBReference"]
    class_class_curie: ClassVar[str] = "EVORAO:PDBReference"
    class_name: ClassVar[str] = "PDBReference"
    class_model_uri: ClassVar[URIRef] = EVORAO.PDBReference

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Keyword(Term):
    """
    A term or phrase used to tag and categorize content
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Keyword"]
    class_class_curie: ClassVar[str] = "EVORAO:Keyword"
    class_name: ClassVar[str] = "Keyword"
    class_model_uri: ClassVar[URIRef] = EVORAO.Keyword

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProteinTag(Term):
    """
    Peptide sequence genetically grafted onto a recombinant protein
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ProteinTag"]
    class_class_curie: ClassVar[str] = "EVORAO:ProteinTag"
    class_name: ClassVar[str] = "ProteinTag"
    class_model_uri: ClassVar[URIRef] = EVORAO.ProteinTag

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class SpecialFeature(Term):
    """
    Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal
    strain, Antiviral resistant strain ...
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["SpecialFeature"]
    class_class_curie: ClassVar[str] = "EVORAO:SpecialFeature"
    class_name: ClassVar[str] = "SpecialFeature"
    class_model_uri: ClassVar[URIRef] = EVORAO.SpecialFeature

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ExpressionVector(Term):
    """
    A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein
    expression
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ExpressionVector"]
    class_class_curie: ClassVar[str] = "EVORAO:ExpressionVector"
    class_name: ClassVar[str] = "ExpressionVector"
    class_model_uri: ClassVar[URIRef] = EVORAO.ExpressionVector

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PlasmidSelection(Term):
    """
    The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic
    resistance markers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["PlasmidSelection"]
    class_class_curie: ClassVar[str] = "EVORAO:PlasmidSelection"
    class_name: ClassVar[str] = "PlasmidSelection"
    class_model_uri: ClassVar[URIRef] = EVORAO.PlasmidSelection

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PropagationHost(Term):
    """
    The organism used to grow and multiply the pathogen under controlled conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["PropagationHost"]
    class_class_curie: ClassVar[str] = "EVORAO:PropagationHost"
    class_name: ClassVar[str] = "PropagationHost"
    class_model_uri: ClassVar[URIRef] = EVORAO.PropagationHost

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class TransmissionMethod(Term):
    """
    The process by which the pathogen spreads between hosts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["TransmissionMethod"]
    class_class_curie: ClassVar[str] = "EVORAO:TransmissionMethod"
    class_name: ClassVar[str] = "TransmissionMethod"
    class_model_uri: ClassVar[URIRef] = EVORAO.TransmissionMethod

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProductionCellLine(Term):
    """
    A population of cells that originates from a primary culture, adapted to grow and divide under laboratory
    conditions. Used in biotechnology to consistently produce biological substances
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ProductionCellLine"]
    class_class_curie: ClassVar[str] = "EVORAO:ProductionCellLine"
    class_name: ClassVar[str] = "ProductionCellLine"
    class_model_uri: ClassVar[URIRef] = EVORAO.ProductionCellLine

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProductCategory(Term):
    """
    A term used to classify a group of products that share common characteristics or functions, which helps in their
    organization
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ProductCategory"]
    class_class_curie: ClassVar[str] = "EVORAO:ProductCategory"
    class_name: ClassVar[str] = "ProductCategory"
    class_model_uri: ClassVar[URIRef] = EVORAO.ProductCategory

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    parentCategory: Optional[Union[dict, "ProductCategory"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.parentCategory is not None and not isinstance(self.parentCategory, ProductCategory):
            self.parentCategory = ProductCategory(**as_dict(self.parentCategory))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsolationHost(Term):
    """
    Host organism from which the pathogen was isolated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["IsolationHost"]
    class_class_curie: ClassVar[str] = "EVORAO:IsolationHost"
    class_name: ClassVar[str] = "IsolationHost"
    class_model_uri: ClassVar[URIRef] = EVORAO.IsolationHost

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class GeographicalOrigin(Term):
    """
    The specific location or region where a physical item, originates or is naturally found
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["GeographicalOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:GeographicalOrigin"
    class_name: ClassVar[str] = "GeographicalOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.GeographicalOrigin

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class IPLCOrigin(GeographicalOrigin):
    """
    The IPLC area (Indigenous People and Local Communities) from which a physical item originates
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["IPLCOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:IPLCOrigin"
    class_name: ClassVar[str] = "IPLCOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.IPLCOrigin

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Country(Term):
    """
    The country as of ISO3166
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Country"]
    class_class_curie: ClassVar[str] = "EVORAO:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = EVORAO.Country

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    alpha2Code: str = None
    weight: int = 0

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.alpha2Code):
            self.MissingRequiredField("alpha2Code")
        if not isinstance(self.alpha2Code, str):
            self.alpha2Code = str(self.alpha2Code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IATAClassification(Term):
    """
    The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are
    transported by air
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["IATAClassification"]
    class_class_curie: ClassVar[str] = "EVORAO:IATAClassification"
    class_name: ClassVar[str] = "IATAClassification"
    class_model_uri: ClassVar[URIRef] = EVORAO.IATAClassification

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Variant(CommonName):
    """
    An organism with one or more new mutations is referred to as a “variant” of the original organism if not
    sufficiently different to be termed a distinct strain
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Variant"]
    class_class_curie: ClassVar[str] = "EVORAO:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = EVORAO.Variant

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class TaxonomicRank(Term):
    """
    The possible taxonomic ranks and their description
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["TaxonomicRank"]
    class_class_curie: ClassVar[str] = "EVORAO:TaxonomicRank"
    class_name: ClassVar[str] = "TaxonomicRank"
    class_model_uri: ClassVar[URIRef] = EVORAO.TaxonomicRank

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    taxonomy: Optional[Union[Union[dict, Taxonomy], list[Union[dict, Taxonomy]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=Taxonomy, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Taxon(Term):
    """
    Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form
    a unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Taxon"]
    class_class_curie: ClassVar[str] = "EVORAO:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = EVORAO.Taxon

    title: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    parentTaxon: Union[dict, "Taxon"] = None
    rank: Union[dict, TaxonomicRank] = None
    taxonomicID: str = None
    weight: int = 0
    taxonomy: Optional[Union[Union[dict, Taxonomy], list[Union[dict, Taxonomy]]]] = empty_list()
    previouslyKnownAs: Optional[Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]]] = empty_list()
    externalEquivalentTaxon: Optional[Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]]] = empty_list()
    taxonomicNodeID: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.parentTaxon):
            self.MissingRequiredField("parentTaxon")
        if not isinstance(self.parentTaxon, Taxon):
            self.parentTaxon = Taxon(**as_dict(self.parentTaxon))

        if self._is_empty(self.rank):
            self.MissingRequiredField("rank")
        if not isinstance(self.rank, TaxonomicRank):
            self.rank = TaxonomicRank(**as_dict(self.rank))

        if self._is_empty(self.taxonomicID):
            self.MissingRequiredField("taxonomicID")
        if not isinstance(self.taxonomicID, str):
            self.taxonomicID = str(self.taxonomicID)

        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=Taxonomy, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="previouslyKnownAs", slot_type=Taxon, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="externalEquivalentTaxon", slot_type=Taxon, key_name="title", keyed=False)

        if self.taxonomicNodeID is not None and not isinstance(self.taxonomicNodeID, str):
            self.taxonomicNodeID = str(self.taxonomicNodeID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalRelatedReference(Resource):
    """
    A reference that permits to retrieve an item from an external provider
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ExternalRelatedReference"]
    class_class_curie: ClassVar[str] = "EVORAO:ExternalRelatedReference"
    class_name: ClassVar[str] = "ExternalRelatedReference"
    class_model_uri: ClassVar[URIRef] = EVORAO.ExternalRelatedReference

    reference: str = None
    referenceLabel: str = None
    referenceProviderPrefix: str = None
    referenceProviderName: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.referenceLabel):
            self.MissingRequiredField("referenceLabel")
        if not isinstance(self.referenceLabel, str):
            self.referenceLabel = str(self.referenceLabel)

        if self._is_empty(self.referenceProviderPrefix):
            self.MissingRequiredField("referenceProviderPrefix")
        if not isinstance(self.referenceProviderPrefix, str):
            self.referenceProviderPrefix = str(self.referenceProviderPrefix)

        if self._is_empty(self.referenceProviderName):
            self.MissingRequiredField("referenceProviderName")
        if not isinstance(self.referenceProviderName, str):
            self.referenceProviderName = str(self.referenceProviderName)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sequence(Resource):
    """
    A nucleic acid or protein sequence information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Sequence"]
    class_class_curie: ClassVar[str] = "EVORAO:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = EVORAO.Sequence

    sequenceReference: Optional[Union[Union[dict, "SequenceReference"], list[Union[dict, "SequenceReference"]]]] = empty_list()
    sequenceFASTA: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="sequenceReference", slot_type=SequenceReference, key_name="accessionNumber", keyed=False)

        if self.sequenceFASTA is not None and not isinstance(self.sequenceFASTA, str):
            self.sequenceFASTA = str(self.sequenceFASTA)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceReference(Resource):
    """
    A reference that permits to retrieve the sequence information from a sequence provider
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["SequenceReference"]
    class_class_curie: ClassVar[str] = "EVORAO:SequenceReference"
    class_name: ClassVar[str] = "SequenceReference"
    class_model_uri: ClassVar[URIRef] = EVORAO.SequenceReference

    accessionNumber: str = None
    sequenceProvider: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accessionNumber):
            self.MissingRequiredField("accessionNumber")
        if not isinstance(self.accessionNumber, str):
            self.accessionNumber = str(self.accessionNumber)

        if self._is_empty(self.sequenceProvider):
            self.MissingRequiredField("sequenceProvider")
        if not isinstance(self.sequenceProvider, str):
            self.sequenceProvider = str(self.sequenceProvider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonOrOrganization(Resource):
    """
    A person or an organization
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "PersonOrOrganization"
    class_model_uri: ClassVar[URIRef] = EVORAO.PersonOrOrganization

    name: str = None
    description: Optional[str] = None
    homePage: Optional[Union[str, URI]] = None
    contactPoint: Optional[Union[dict, "ContactPoint"]] = None
    logo: Optional[Union[dict, "Image"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.homePage is not None and not isinstance(self.homePage, URI):
            self.homePage = URI(self.homePage)

        if self.contactPoint is not None and not isinstance(self.contactPoint, ContactPoint):
            self.contactPoint = ContactPoint(**as_dict(self.contactPoint))

        if self.logo is not None and not isinstance(self.logo, Image):
            self.logo = Image(**as_dict(self.logo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(PersonOrOrganization):
    """
    An individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Person"]
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EVORAO.Person

    name: str = None
    oRCIDiD: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.oRCIDiD is not None and not isinstance(self.oRCIDiD, str):
            self.oRCIDiD = str(self.oRCIDiD)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(PersonOrOrganization):
    """
    A social entity established to meet needs or pursue specific goals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Organization"]
    class_class_curie: ClassVar[str] = "foaf:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = EVORAO.Organization

    name: str = None
    alternateName: Optional[Union[Union[dict, AlternateName], list[Union[dict, AlternateName]]]] = empty_list()
    country: Optional[Union[dict, Country]] = None
    rORiD: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="alternateName", slot_type=AlternateName, key_name="title", keyed=False)

        if self.country is not None and not isinstance(self.country, Country):
            self.country = Country(**as_dict(self.country))

        if self.rORiD is not None and not isinstance(self.rORiD, str):
            self.rORiD = str(self.rORiD)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RI(Organization):
    """
    A research infrastructure
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["RI"]
    class_class_curie: ClassVar[str] = "EVORAO:RI"
    class_name: ClassVar[str] = "RI"
    class_model_uri: ClassVar[URIRef] = EVORAO.RI

    name: str = None

@dataclass(repr=False)
class Provider(Organization):
    """
    A provider of products or services, as a specific organization
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Provider"]
    class_class_curie: ClassVar[str] = "EVORAO:Provider"
    class_name: ClassVar[str] = "Provider"
    class_model_uri: ClassVar[URIRef] = EVORAO.Provider

    name: str = None
    memberOfRI: Optional[Union[Union[dict, RI], list[Union[dict, RI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="memberOfRI", slot_type=RI, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Originator(PersonOrOrganization):
    """
    The individual or organization responsible for the original discovery, isolation, or creation of an item,
    providing information about the source or origin of the sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Originator"]
    class_class_curie: ClassVar[str] = "EVORAO:Originator"
    class_name: ClassVar[str] = "Originator"
    class_model_uri: ClassVar[URIRef] = EVORAO.Originator

    name: str = None

@dataclass(repr=False)
class BiologicalMaterialOrigin(Resource):
    """
    Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing
    of genetic resources in compliance with the Nagoya Protocol
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["BiologicalMaterialOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:BiologicalMaterialOrigin"
    class_name: ClassVar[str] = "BiologicalMaterialOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.BiologicalMaterialOrigin

    biologicalSourceType: Union[bool, Bool] = None
    biologicalPartOrigin: Union[Union[dict, "BiologicalPartOrigin"], list[Union[dict, "BiologicalPartOrigin"]]] = None
    recombinantMaterial: Union[bool, Bool] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recombinantMaterial):
            self.MissingRequiredField("recombinantMaterial")
        if not isinstance(self.recombinantMaterial, Bool):
            self.recombinantMaterial = Bool(self.recombinantMaterial)

        if self._is_empty(self.biologicalSourceType):
            self.MissingRequiredField("biologicalSourceType")
        if not isinstance(self.biologicalSourceType, Bool):
            self.biologicalSourceType = Bool(self.biologicalSourceType)

        if self._is_empty(self.biologicalPartOrigin):
            self.MissingRequiredField("biologicalPartOrigin")
        self._normalize_inlined_as_dict(slot_name="biologicalPartOrigin", slot_type=BiologicalPartOrigin, key_name="accessToPhysicalGeneticResource", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalPartOrigin(Resource):
    """
    Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It
    can be multiple parts in case of a recombinant biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["BiologicalPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:BiologicalPartOrigin"
    class_name: ClassVar[str] = "BiologicalPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.BiologicalPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    recombinantPartIdentification: Optional[Union[dict, "RecombinantPartIdentification"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accessToPhysicalGeneticResource):
            self.MissingRequiredField("accessToPhysicalGeneticResource")
        if not isinstance(self.accessToPhysicalGeneticResource, Bool):
            self.accessToPhysicalGeneticResource = Bool(self.accessToPhysicalGeneticResource)

        if self.recombinantPartIdentification is not None and not isinstance(self.recombinantPartIdentification, RecombinantPartIdentification):
            self.recombinantPartIdentification = RecombinantPartIdentification(**as_dict(self.recombinantPartIdentification))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaturalPartOrigin(BiologicalPartOrigin):
    """
    Information on the origin of a natural part that composes the biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["NaturalPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:NaturalPartOrigin"
    class_name: ClassVar[str] = "NaturalPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.NaturalPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    countryOfCollection: Union[dict, Country] = None
    collectionDate: Union[str, XSDDateTime] = None
    beforeDate: Union[bool, Bool] = False
    indigenousPoepleAndLocalCommunityOrigin: Optional[Union[dict, IPLCOrigin]] = None
    permitIdentifierForABS: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.countryOfCollection):
            self.MissingRequiredField("countryOfCollection")
        if not isinstance(self.countryOfCollection, Country):
            self.countryOfCollection = Country(**as_dict(self.countryOfCollection))

        if self._is_empty(self.collectionDate):
            self.MissingRequiredField("collectionDate")
        if not isinstance(self.collectionDate, XSDDateTime):
            self.collectionDate = XSDDateTime(self.collectionDate)

        if self._is_empty(self.beforeDate):
            self.MissingRequiredField("beforeDate")
        if not isinstance(self.beforeDate, Bool):
            self.beforeDate = Bool(self.beforeDate)

        if self.indigenousPoepleAndLocalCommunityOrigin is not None and not isinstance(self.indigenousPoepleAndLocalCommunityOrigin, IPLCOrigin):
            self.indigenousPoepleAndLocalCommunityOrigin = IPLCOrigin(**as_dict(self.indigenousPoepleAndLocalCommunityOrigin))

        if self.permitIdentifierForABS is not None and not isinstance(self.permitIdentifierForABS, str):
            self.permitIdentifierForABS = str(self.permitIdentifierForABS)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SyntheticPartOrigin(BiologicalPartOrigin):
    """
    Information on the origin of a synthetic part that composes the biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["SyntheticPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORAO:SyntheticPartOrigin"
    class_name: ClassVar[str] = "SyntheticPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORAO.SyntheticPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    modificationsFromTheReferenceSequences: Union[bool, Bool] = None
    descriptionOfModificationsMadeFromTheReferenceSequences: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modificationsFromTheReferenceSequences):
            self.MissingRequiredField("modificationsFromTheReferenceSequences")
        if not isinstance(self.modificationsFromTheReferenceSequences, Bool):
            self.modificationsFromTheReferenceSequences = Bool(self.modificationsFromTheReferenceSequences)

        if self.descriptionOfModificationsMadeFromTheReferenceSequences is not None and not isinstance(self.descriptionOfModificationsMadeFromTheReferenceSequences, str):
            self.descriptionOfModificationsMadeFromTheReferenceSequences = str(self.descriptionOfModificationsMadeFromTheReferenceSequences)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecombinantPartIdentification(Resource):
    """
    Identification of a recombinant part
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["RecombinantPartIdentification"]
    class_class_curie: ClassVar[str] = "EVORAO:RecombinantPartIdentification"
    class_name: ClassVar[str] = "RecombinantPartIdentification"
    class_model_uri: ClassVar[URIRef] = EVORAO.RecombinantPartIdentification

    partIdentification: str = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.partIdentification):
            self.MissingRequiredField("partIdentification")
        if not isinstance(self.partIdentification, str):
            self.partIdentification = str(self.partIdentification)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Collection(Catalogue):
    """
    Set of products and services with some common characteristics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Collection"]
    class_class_curie: ClassVar[str] = "EVORAO:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = EVORAO.Collection

    title: str = None
    description: str = None
    collectionItem: Optional[Union[Union[dict, "ProductOrService"], list[Union[dict, "ProductOrService"]]]] = empty_list()
    collectionDataProvider: Optional[Union[dict, DataProvider]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="collectionItem", slot_type=ProductOrService, key_name="title", keyed=False)

        if self.collectionDataProvider is not None and not isinstance(self.collectionDataProvider, DataProvider):
            self.collectionDataProvider = DataProvider(**as_dict(self.collectionDataProvider))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProductOrService(Dataset):
    """
    A product or a service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ProductOrService"]
    class_class_curie: ClassVar[str] = "EVORAO:ProductOrService"
    class_name: ClassVar[str] = "ProductOrService"
    class_model_uri: ClassVar[URIRef] = EVORAO.ProductOrService

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    unitDefinition: Optional[str] = None
    additionalCategory: Optional[Union[Union[dict, ProductCategory], list[Union[dict, ProductCategory]]]] = empty_list()
    qualityGrading: Optional[str] = None
    relatedDOI: Optional[Union[Union[dict, DOI], list[Union[dict, DOI]]]] = empty_list()
    riskGroup: Optional[Union[dict, RiskGroup]] = None
    biosafetyRestrictions: Optional[str] = None
    complementaryDocument: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    technicalRecommendation: Optional[str] = None
    productPicture: Optional[Union[Union[dict, "Image"], list[Union[dict, "Image"]]]] = empty_list()
    externalRelatedReference: Optional[Union[Union[dict, ExternalRelatedReference], list[Union[dict, ExternalRelatedReference]]]] = empty_list()
    certification: Optional[Union[Union[dict, "Certification"], list[Union[dict, "Certification"]]]] = empty_list()
    internalReference: Optional[str] = None
    note: Optional[str] = None
    contactPoint: Optional[Union[dict, "ContactPoint"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accessPointURL):
            self.MissingRequiredField("accessPointURL")
        if not isinstance(self.accessPointURL, URI):
            self.accessPointURL = URI(self.accessPointURL)

        if self._is_empty(self.refSKU):
            self.MissingRequiredField("refSKU")
        if not isinstance(self.refSKU, str):
            self.refSKU = str(self.refSKU)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, ProductCategory):
            self.category = ProductCategory(**as_dict(self.category))

        if self._is_empty(self.unitCost):
            self.MissingRequiredField("unitCost")
        if not isinstance(self.unitCost, str):
            self.unitCost = str(self.unitCost)

        if self._is_empty(self.pathogenIdentification):
            self.MissingRequiredField("pathogenIdentification")
        self._normalize_inlined_as_dict(slot_name="pathogenIdentification", slot_type=PathogenIdentification, key_name="taxon", keyed=False)

        if self._is_empty(self.canItBeUsedToProduceGMO):
            self.MissingRequiredField("canItBeUsedToProduceGMO")
        if not isinstance(self.canItBeUsedToProduceGMO, Bool):
            self.canItBeUsedToProduceGMO = Bool(self.canItBeUsedToProduceGMO)

        if self._is_empty(self.provider):
            self.MissingRequiredField("provider")
        if not isinstance(self.provider, Provider):
            self.provider = Provider(**as_dict(self.provider))

        if self._is_empty(self.collection):
            self.MissingRequiredField("collection")
        self._normalize_inlined_as_dict(slot_name="collection", slot_type=Collection, key_name="title", keyed=False)

        if self._is_empty(self.keywords):
            self.MissingRequiredField("keywords")
        self._normalize_inlined_as_dict(slot_name="keywords", slot_type=Keyword, key_name="title", keyed=False)

        if self._is_empty(self.availability):
            self.MissingRequiredField("availability")
        if not isinstance(self.availability, str):
            self.availability = str(self.availability)

        if self.unitDefinition is not None and not isinstance(self.unitDefinition, str):
            self.unitDefinition = str(self.unitDefinition)

        self._normalize_inlined_as_dict(slot_name="additionalCategory", slot_type=ProductCategory, key_name="title", keyed=False)

        if self.qualityGrading is not None and not isinstance(self.qualityGrading, str):
            self.qualityGrading = str(self.qualityGrading)

        self._normalize_inlined_as_dict(slot_name="relatedDOI", slot_type=DOI, key_name="title", keyed=False)

        if self.riskGroup is not None and not isinstance(self.riskGroup, RiskGroup):
            self.riskGroup = RiskGroup(**as_dict(self.riskGroup))

        if self.biosafetyRestrictions is not None and not isinstance(self.biosafetyRestrictions, str):
            self.biosafetyRestrictions = str(self.biosafetyRestrictions)

        self._normalize_inlined_as_dict(slot_name="complementaryDocument", slot_type=Document, key_name="name", keyed=False)

        if self.technicalRecommendation is not None and not isinstance(self.technicalRecommendation, str):
            self.technicalRecommendation = str(self.technicalRecommendation)

        self._normalize_inlined_as_dict(slot_name="productPicture", slot_type=Image, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="externalRelatedReference", slot_type=ExternalRelatedReference, key_name="reference", keyed=False)

        self._normalize_inlined_as_dict(slot_name="certification", slot_type=Certification, key_name="title", keyed=False)

        if self.internalReference is not None and not isinstance(self.internalReference, str):
            self.internalReference = str(self.internalReference)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        if self.contactPoint is not None and not isinstance(self.contactPoint, ContactPoint):
            self.contactPoint = ContactPoint(**as_dict(self.contactPoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Service(ProductOrService):
    """
    A service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Service"]
    class_class_curie: ClassVar[str] = "EVORAO:Service"
    class_name: ClassVar[str] = "Service"
    class_model_uri: ClassVar[URIRef] = EVORAO.Service

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    modelSpecies: Optional[str] = None
    modelType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.modelSpecies is not None and not isinstance(self.modelSpecies, str):
            self.modelSpecies = str(self.modelSpecies)

        if self.modelType is not None and not isinstance(self.modelType, str):
            self.modelType = str(self.modelType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Product(ProductOrService):
    """
    A product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Product"]
    class_class_curie: ClassVar[str] = "EVORAO:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = EVORAO.Product

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    materialSafetyDataSheet: Optional[Union[dict, "MSDS"]] = None
    originator: Optional[Union[dict, Originator]] = None
    thirdPartyDistributionConsent: Optional[Union[bool, Bool]] = None
    usageRestrictions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hasIATAClassification):
            self.MissingRequiredField("hasIATAClassification")
        if not isinstance(self.hasIATAClassification, IATAClassification):
            self.hasIATAClassification = IATAClassification(**as_dict(self.hasIATAClassification))

        if self._is_empty(self.shippingConditions):
            self.MissingRequiredField("shippingConditions")
        if not isinstance(self.shippingConditions, str):
            self.shippingConditions = str(self.shippingConditions)

        if self._is_empty(self.storageConditions):
            self.MissingRequiredField("storageConditions")
        if not isinstance(self.storageConditions, str):
            self.storageConditions = str(self.storageConditions)

        if self.materialSafetyDataSheet is not None and not isinstance(self.materialSafetyDataSheet, MSDS):
            self.materialSafetyDataSheet = MSDS(**as_dict(self.materialSafetyDataSheet))

        if self.originator is not None and not isinstance(self.originator, Originator):
            self.originator = Originator(**as_dict(self.originator))

        if self.thirdPartyDistributionConsent is not None and not isinstance(self.thirdPartyDistributionConsent, Bool):
            self.thirdPartyDistributionConsent = Bool(self.thirdPartyDistributionConsent)

        if self.usageRestrictions is not None and not isinstance(self.usageRestrictions, str):
            self.usageRestrictions = str(self.usageRestrictions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Antibody(Product):
    """
    Protein that can bind to certain types of foreign bodies, such as pathogens
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Antibody"]
    class_class_curie: ClassVar[str] = "EVORAO:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = EVORAO.Antibody

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    antibodyPurifiedByAffinity: Union[bool, Bool] = None
    specificityDocumented: Union[bool, Bool] = None
    targetedAntigen: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    productionSystem: Optional[str] = None
    sequenceReference: Optional[Union[Union[dict, SequenceReference], list[Union[dict, SequenceReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.antibodyPurifiedByAffinity):
            self.MissingRequiredField("antibodyPurifiedByAffinity")
        if not isinstance(self.antibodyPurifiedByAffinity, Bool):
            self.antibodyPurifiedByAffinity = Bool(self.antibodyPurifiedByAffinity)

        if self._is_empty(self.specificityDocumented):
            self.MissingRequiredField("specificityDocumented")
        if not isinstance(self.specificityDocumented, Bool):
            self.specificityDocumented = Bool(self.specificityDocumented)

        if self._is_empty(self.targetedAntigen):
            self.MissingRequiredField("targetedAntigen")
        if not isinstance(self.targetedAntigen, str):
            self.targetedAntigen = str(self.targetedAntigen)

        if self.productionSystem is not None and not isinstance(self.productionSystem, str):
            self.productionSystem = str(self.productionSystem)

        self._normalize_inlined_as_dict(slot_name="sequenceReference", slot_type=SequenceReference, key_name="accessionNumber", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hybridoma(Antibody):
    """
    An hybridoma that provides antibodies that can be related to a pathogen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Hybridoma"]
    class_class_curie: ClassVar[str] = "EVORAO:Hybridoma"
    class_name: ClassVar[str] = "Hybridoma"
    class_model_uri: ClassVar[URIRef] = EVORAO.Hybridoma

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    antibodyPurifiedByAffinity: Union[bool, Bool] = None
    specificityDocumented: Union[bool, Bool] = None
    targetedAntigen: str = None
    hybridomaDescription: str = None
    unitCost: str = "on request"
    availability: str = "on request"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hybridomaDescription):
            self.MissingRequiredField("hybridomaDescription")
        if not isinstance(self.hybridomaDescription, str):
            self.hybridomaDescription = str(self.hybridomaDescription)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protein(Product):
    """
    A protein as a derived product from a pathogen
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Protein"]
    class_class_curie: ClassVar[str] = "EVORAO:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = EVORAO.Protein

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    relatedPDB: Optional[Union[Union[dict, PDBReference], list[Union[dict, PDBReference]]]] = empty_list()
    specialFeature: Optional[Union[Union[dict, SpecialFeature], list[Union[dict, SpecialFeature]]]] = empty_list()
    proteinTAG: Optional[Union[Union[dict, ProteinTag], list[Union[dict, ProteinTag]]]] = empty_list()
    domain: Optional[Union[str, list[str]]] = empty_list()
    expressedAs: Optional[Union[str, list[str]]] = empty_list()
    inclusionBodiesType: Optional[Union[str, list[str]]] = empty_list()
    expressionSystem: Optional[Union[str, list[str]]] = empty_list()
    functionalCharacterization: Optional[Union[str, list[str]]] = empty_list()
    functionalTechnicalDescription: Optional[Union[str, list[str]]] = empty_list()
    proteinPurification: Optional[Union[str, list[str]]] = empty_list()
    theTAGStatusOfTheSolubilizedProtein: Optional[Union[str, list[str]]] = empty_list()
    typeOfFunctionalCharacterization: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biologicalMaterialOrigin):
            self.MissingRequiredField("biologicalMaterialOrigin")
        if not isinstance(self.biologicalMaterialOrigin, BiologicalMaterialOrigin):
            self.biologicalMaterialOrigin = BiologicalMaterialOrigin(**as_dict(self.biologicalMaterialOrigin))

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequence]

        self._normalize_inlined_as_dict(slot_name="relatedPDB", slot_type=PDBReference, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="specialFeature", slot_type=SpecialFeature, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="proteinTAG", slot_type=ProteinTag, key_name="title", keyed=False)

        if not isinstance(self.domain, list):
            self.domain = [self.domain] if self.domain is not None else []
        self.domain = [v if isinstance(v, str) else str(v) for v in self.domain]

        if not isinstance(self.expressedAs, list):
            self.expressedAs = [self.expressedAs] if self.expressedAs is not None else []
        self.expressedAs = [v if isinstance(v, str) else str(v) for v in self.expressedAs]

        if not isinstance(self.inclusionBodiesType, list):
            self.inclusionBodiesType = [self.inclusionBodiesType] if self.inclusionBodiesType is not None else []
        self.inclusionBodiesType = [v if isinstance(v, str) else str(v) for v in self.inclusionBodiesType]

        if not isinstance(self.expressionSystem, list):
            self.expressionSystem = [self.expressionSystem] if self.expressionSystem is not None else []
        self.expressionSystem = [v if isinstance(v, str) else str(v) for v in self.expressionSystem]

        if not isinstance(self.functionalCharacterization, list):
            self.functionalCharacterization = [self.functionalCharacterization] if self.functionalCharacterization is not None else []
        self.functionalCharacterization = [v if isinstance(v, str) else str(v) for v in self.functionalCharacterization]

        if not isinstance(self.functionalTechnicalDescription, list):
            self.functionalTechnicalDescription = [self.functionalTechnicalDescription] if self.functionalTechnicalDescription is not None else []
        self.functionalTechnicalDescription = [v if isinstance(v, str) else str(v) for v in self.functionalTechnicalDescription]

        if not isinstance(self.proteinPurification, list):
            self.proteinPurification = [self.proteinPurification] if self.proteinPurification is not None else []
        self.proteinPurification = [v if isinstance(v, str) else str(v) for v in self.proteinPurification]

        if not isinstance(self.theTAGStatusOfTheSolubilizedProtein, list):
            self.theTAGStatusOfTheSolubilizedProtein = [self.theTAGStatusOfTheSolubilizedProtein] if self.theTAGStatusOfTheSolubilizedProtein is not None else []
        self.theTAGStatusOfTheSolubilizedProtein = [v if isinstance(v, str) else str(v) for v in self.theTAGStatusOfTheSolubilizedProtein]

        if not isinstance(self.typeOfFunctionalCharacterization, list):
            self.typeOfFunctionalCharacterization = [self.typeOfFunctionalCharacterization] if self.typeOfFunctionalCharacterization is not None else []
        self.typeOfFunctionalCharacterization = [v if isinstance(v, str) else str(v) for v in self.typeOfFunctionalCharacterization]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleicAcid(Product):
    """
    Nucleic acid related to a pathogen. It can be extracted or synthetic
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["NucleicAcid"]
    class_class_curie: ClassVar[str] = "EVORAO:NucleicAcid"
    class_name: ClassVar[str] = "Nucleic Acid"
    class_model_uri: ClassVar[URIRef] = EVORAO.NucleicAcid

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    isItAClonedNucleicAcid: Union[bool, Bool] = None
    hasTAG: Union[dict, ProteinTag] = None
    regionEncompassedInThisProduct: str = None
    mutationObserved: Union[bool, Bool] = None
    sequencing: str = None
    titer: str = None
    sequenceChecked: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    hasGbFileOfTheConstruct: Optional[Union[Union[dict, "Data"], list[Union[dict, "Data"]]]] = empty_list()
    clonedIntoPlasmid: Optional[Union[dict, ExpressionVector]] = None
    pasmidSelection: Optional[Union[Union[dict, PlasmidSelection], list[Union[dict, PlasmidSelection]]]] = empty_list()
    observedMutations: Optional[str] = None
    identificationTechnique: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biologicalMaterialOrigin):
            self.MissingRequiredField("biologicalMaterialOrigin")
        if not isinstance(self.biologicalMaterialOrigin, BiologicalMaterialOrigin):
            self.biologicalMaterialOrigin = BiologicalMaterialOrigin(**as_dict(self.biologicalMaterialOrigin))

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequence]

        if self._is_empty(self.isItAClonedNucleicAcid):
            self.MissingRequiredField("isItAClonedNucleicAcid")
        if not isinstance(self.isItAClonedNucleicAcid, Bool):
            self.isItAClonedNucleicAcid = Bool(self.isItAClonedNucleicAcid)

        if self._is_empty(self.hasTAG):
            self.MissingRequiredField("hasTAG")
        if not isinstance(self.hasTAG, ProteinTag):
            self.hasTAG = ProteinTag(**as_dict(self.hasTAG))

        if self._is_empty(self.regionEncompassedInThisProduct):
            self.MissingRequiredField("regionEncompassedInThisProduct")
        if not isinstance(self.regionEncompassedInThisProduct, str):
            self.regionEncompassedInThisProduct = str(self.regionEncompassedInThisProduct)

        if self._is_empty(self.mutationObserved):
            self.MissingRequiredField("mutationObserved")
        if not isinstance(self.mutationObserved, Bool):
            self.mutationObserved = Bool(self.mutationObserved)

        if self._is_empty(self.sequencing):
            self.MissingRequiredField("sequencing")
        if not isinstance(self.sequencing, str):
            self.sequencing = str(self.sequencing)

        if self._is_empty(self.titer):
            self.MissingRequiredField("titer")
        if not isinstance(self.titer, str):
            self.titer = str(self.titer)

        if self._is_empty(self.sequenceChecked):
            self.MissingRequiredField("sequenceChecked")
        if not isinstance(self.sequenceChecked, Bool):
            self.sequenceChecked = Bool(self.sequenceChecked)

        self._normalize_inlined_as_dict(slot_name="hasGbFileOfTheConstruct", slot_type=Data, key_name="name", keyed=False)

        if self.clonedIntoPlasmid is not None and not isinstance(self.clonedIntoPlasmid, ExpressionVector):
            self.clonedIntoPlasmid = ExpressionVector(**as_dict(self.clonedIntoPlasmid))

        self._normalize_inlined_as_dict(slot_name="pasmidSelection", slot_type=PlasmidSelection, key_name="title", keyed=False)

        if self.observedMutations is not None and not isinstance(self.observedMutations, str):
            self.observedMutations = str(self.observedMutations)

        if self.identificationTechnique is not None and not isinstance(self.identificationTechnique, str):
            self.identificationTechnique = str(self.identificationTechnique)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DetectionKit(Product):
    """
    A detection kit for specific pathogens
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["DetectionKit"]
    class_class_curie: ClassVar[str] = "EVORAO:DetectionKit"
    class_name: ClassVar[str] = "Detection Kit"
    class_model_uri: ClassVar[URIRef] = EVORAO.DetectionKit

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    specificityDocumented: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    hasSOPFile: Optional[Union[Union[dict, "File"], list[Union[dict, "File"]]]] = empty_list()
    specificity: Optional[str] = None
    targetedRegion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.specificityDocumented):
            self.MissingRequiredField("specificityDocumented")
        if not isinstance(self.specificityDocumented, Bool):
            self.specificityDocumented = Bool(self.specificityDocumented)

        self._normalize_inlined_as_dict(slot_name="hasSOPFile", slot_type=File, key_name="name", keyed=False)

        if self.specificity is not None and not isinstance(self.specificity, str):
            self.specificity = str(self.specificity)

        if self.targetedRegion is not None and not isinstance(self.targetedRegion, str):
            self.targetedRegion = str(self.targetedRegion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bundle(Product):
    """
    A group of products
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Bundle"]
    class_class_curie: ClassVar[str] = "EVORAO:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = EVORAO.Bundle

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    productsOfTheBundle: Union[Union[dict, Product], list[Union[dict, Product]]] = None
    unitCost: str = "on request"
    availability: str = "on request"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.productsOfTheBundle):
            self.MissingRequiredField("productsOfTheBundle")
        self._normalize_inlined_as_dict(slot_name="productsOfTheBundle", slot_type=Product, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pathogen(Product):
    """
    Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such
    as a virus, bacterium, protozoan, prion, viroid, or fungus
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Pathogen"]
    class_class_curie: ClassVar[str] = "EVORAO:Pathogen"
    class_name: ClassVar[str] = "Pathogen"
    class_model_uri: ClassVar[URIRef] = EVORAO.Pathogen

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"
    suspectedEpidemiologicalOrigin: Optional[Union[Union[dict, GeographicalOrigin], list[Union[dict, GeographicalOrigin]]]] = empty_list()
    isolationHost: Optional[Union[Union[dict, IsolationHost], list[Union[dict, IsolationHost]]]] = empty_list()
    productionCellLine: Optional[Union[Union[dict, ProductionCellLine], list[Union[dict, ProductionCellLine]]]] = empty_list()
    propagationHost: Optional[Union[Union[dict, PropagationHost], list[Union[dict, PropagationHost]]]] = empty_list()
    transmissionMethod: Optional[Union[Union[dict, TransmissionMethod], list[Union[dict, TransmissionMethod]]]] = empty_list()
    clinicalInformation: Optional[str] = None
    identificationTechnique: Optional[str] = None
    infectivityTest: Optional[str] = None
    isolationTechnique: Optional[str] = None
    isolationConditions: Optional[str] = None
    passage: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biologicalMaterialOrigin):
            self.MissingRequiredField("biologicalMaterialOrigin")
        if not isinstance(self.biologicalMaterialOrigin, BiologicalMaterialOrigin):
            self.biologicalMaterialOrigin = BiologicalMaterialOrigin(**as_dict(self.biologicalMaterialOrigin))

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequence]

        if self._is_empty(self.cultivability):
            self.MissingRequiredField("cultivability")
        if not isinstance(self.cultivability, str):
            self.cultivability = str(self.cultivability)

        if self._is_empty(self.infectivity):
            self.MissingRequiredField("infectivity")
        if not isinstance(self.infectivity, str):
            self.infectivity = str(self.infectivity)

        if self._is_empty(self.letterOfAuthority):
            self.MissingRequiredField("letterOfAuthority")
        if not isinstance(self.letterOfAuthority, str):
            self.letterOfAuthority = str(self.letterOfAuthority)

        if self._is_empty(self.genomeSequencing):
            self.MissingRequiredField("genomeSequencing")
        if not isinstance(self.genomeSequencing, str):
            self.genomeSequencing = str(self.genomeSequencing)

        if self._is_empty(self.titer):
            self.MissingRequiredField("titer")
        if not isinstance(self.titer, str):
            self.titer = str(self.titer)

        self._normalize_inlined_as_dict(slot_name="suspectedEpidemiologicalOrigin", slot_type=GeographicalOrigin, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="isolationHost", slot_type=IsolationHost, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="productionCellLine", slot_type=ProductionCellLine, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="propagationHost", slot_type=PropagationHost, key_name="title", keyed=False)

        self._normalize_inlined_as_dict(slot_name="transmissionMethod", slot_type=TransmissionMethod, key_name="title", keyed=False)

        if self.clinicalInformation is not None and not isinstance(self.clinicalInformation, str):
            self.clinicalInformation = str(self.clinicalInformation)

        if self.identificationTechnique is not None and not isinstance(self.identificationTechnique, str):
            self.identificationTechnique = str(self.identificationTechnique)

        if self.infectivityTest is not None and not isinstance(self.infectivityTest, str):
            self.infectivityTest = str(self.infectivityTest)

        if self.isolationTechnique is not None and not isinstance(self.isolationTechnique, str):
            self.isolationTechnique = str(self.isolationTechnique)

        if self.isolationConditions is not None and not isinstance(self.isolationConditions, str):
            self.isolationConditions = str(self.isolationConditions)

        if self.passage is not None and not isinstance(self.passage, str):
            self.passage = str(self.passage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Virus(Pathogen):
    """
    The virus as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Virus"]
    class_class_curie: ClassVar[str] = "EVORAO:Virus"
    class_name: ClassVar[str] = "Virus"
    class_model_uri: ClassVar[URIRef] = EVORAO.Virus

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    mycoplasmicContent: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"
    contaminationWithCoInfectingViruses: Union[bool, Bool] = False
    coInfectingViruses: Optional[Union[Union[dict, VirusName], list[Union[dict, VirusName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.contaminationWithCoInfectingViruses):
            self.MissingRequiredField("contaminationWithCoInfectingViruses")
        if not isinstance(self.contaminationWithCoInfectingViruses, Bool):
            self.contaminationWithCoInfectingViruses = Bool(self.contaminationWithCoInfectingViruses)

        if self._is_empty(self.mycoplasmicContent):
            self.MissingRequiredField("mycoplasmicContent")
        if not isinstance(self.mycoplasmicContent, Bool):
            self.mycoplasmicContent = Bool(self.mycoplasmicContent)

        self._normalize_inlined_as_dict(slot_name="coInfectingViruses", slot_type=VirusName, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bacterium(Pathogen):
    """
    The bacterium as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Bacterium"]
    class_class_curie: ClassVar[str] = "EVORAO:Bacterium"
    class_name: ClassVar[str] = "Bacterium"
    class_model_uri: ClassVar[URIRef] = EVORAO.Bacterium

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"

@dataclass(repr=False)
class Fungus(Pathogen):
    """
    The fungus as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Fungus"]
    class_class_curie: ClassVar[str] = "EVORAO:Fungus"
    class_name: ClassVar[str] = "Fungus"
    class_model_uri: ClassVar[URIRef] = EVORAO.Fungus

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"

@dataclass(repr=False)
class Protozoan(Pathogen):
    """
    The protozoan as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Protozoan"]
    class_class_curie: ClassVar[str] = "EVORAO:Protozoan"
    class_name: ClassVar[str] = "Protozoan"
    class_model_uri: ClassVar[URIRef] = EVORAO.Protozoan

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"

@dataclass(repr=False)
class Viroid(Pathogen):
    """
    The viroid as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Viroid"]
    class_class_curie: ClassVar[str] = "EVORAO:Viroid"
    class_name: ClassVar[str] = "Viroid"
    class_model_uri: ClassVar[URIRef] = EVORAO.Viroid

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"

@dataclass(repr=False)
class Prion(Pathogen):
    """
    The prion as a biological material
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Prion"]
    class_class_curie: ClassVar[str] = "EVORAO:Prion"
    class_name: ClassVar[str] = "Prion"
    class_model_uri: ClassVar[URIRef] = EVORAO.Prion

    title: str = None
    description: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]] = None
    canItBeUsedToProduceGMO: Union[bool, Bool] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], list[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], list[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], list[Union[dict, Sequence]]] = None
    infectivity: str = None
    genomeSequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable"
    letterOfAuthority: str = "Not applicable"

@dataclass(repr=False)
class MSDS(Resource):
    """
    A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial
    occupational safety and health information related to the product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["MSDS"]
    class_class_curie: ClassVar[str] = "EVORAO:MSDS"
    class_name: ClassVar[str] = "MSDS"
    class_model_uri: ClassVar[URIRef] = EVORAO.MSDS

    msdsContact: Union[dict, "ContactPoint"] = None
    physicalChemicalProperties: Optional[str] = None
    hazardsIdentification: Optional[str] = None
    firstAidMeasures: Optional[str] = None
    fireFightingMeasures: Optional[str] = None
    accidentalReleaseMeasures: Optional[str] = None
    handlingAndStorage: Optional[str] = None
    exposureControlsPersonalProtection: Optional[str] = None
    stabilityAndReactivity: Optional[str] = None
    toxicologicalInformation: Optional[str] = None
    ecologicalInformation: Optional[str] = None
    disposalConsiderations: Optional[str] = None
    transportInformation: Optional[str] = None
    regulatoryInformation: Optional[str] = None
    furtherInformation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msdsContact):
            self.MissingRequiredField("msdsContact")
        if not isinstance(self.msdsContact, ContactPoint):
            self.msdsContact = ContactPoint(**as_dict(self.msdsContact))

        if self.physicalChemicalProperties is not None and not isinstance(self.physicalChemicalProperties, str):
            self.physicalChemicalProperties = str(self.physicalChemicalProperties)

        if self.hazardsIdentification is not None and not isinstance(self.hazardsIdentification, str):
            self.hazardsIdentification = str(self.hazardsIdentification)

        if self.firstAidMeasures is not None and not isinstance(self.firstAidMeasures, str):
            self.firstAidMeasures = str(self.firstAidMeasures)

        if self.fireFightingMeasures is not None and not isinstance(self.fireFightingMeasures, str):
            self.fireFightingMeasures = str(self.fireFightingMeasures)

        if self.accidentalReleaseMeasures is not None and not isinstance(self.accidentalReleaseMeasures, str):
            self.accidentalReleaseMeasures = str(self.accidentalReleaseMeasures)

        if self.handlingAndStorage is not None and not isinstance(self.handlingAndStorage, str):
            self.handlingAndStorage = str(self.handlingAndStorage)

        if self.exposureControlsPersonalProtection is not None and not isinstance(self.exposureControlsPersonalProtection, str):
            self.exposureControlsPersonalProtection = str(self.exposureControlsPersonalProtection)

        if self.stabilityAndReactivity is not None and not isinstance(self.stabilityAndReactivity, str):
            self.stabilityAndReactivity = str(self.stabilityAndReactivity)

        if self.toxicologicalInformation is not None and not isinstance(self.toxicologicalInformation, str):
            self.toxicologicalInformation = str(self.toxicologicalInformation)

        if self.ecologicalInformation is not None and not isinstance(self.ecologicalInformation, str):
            self.ecologicalInformation = str(self.ecologicalInformation)

        if self.disposalConsiderations is not None and not isinstance(self.disposalConsiderations, str):
            self.disposalConsiderations = str(self.disposalConsiderations)

        if self.transportInformation is not None and not isinstance(self.transportInformation, str):
            self.transportInformation = str(self.transportInformation)

        if self.regulatoryInformation is not None and not isinstance(self.regulatoryInformation, str):
            self.regulatoryInformation = str(self.regulatoryInformation)

        if self.furtherInformation is not None and not isinstance(self.furtherInformation, str):
            self.furtherInformation = str(self.furtherInformation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(Resource):
    """
    Digital document or record stored in a specific format that contains data or information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["File"]
    class_class_curie: ClassVar[str] = "EVORAO:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = EVORAO.File

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None
    description: Optional[str] = None
    license: Optional[Union[dict, "License"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.contentURL):
            self.MissingRequiredField("contentURL")
        if not isinstance(self.contentURL, URI):
            self.contentURL = URI(self.contentURL)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Data(File):
    """
    Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer
    of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Data"]
    class_class_curie: ClassVar[str] = "EVORAO:Data"
    class_name: ClassVar[str] = "Data"
    class_model_uri: ClassVar[URIRef] = EVORAO.Data

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Document(File):
    """
    Subclass of File representing textual or written files such as reports, manuals, or forms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Document"]
    class_class_curie: ClassVar[str] = "EVORAO:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = EVORAO.Document

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Audio(File):
    """
    Subclass of File representing sound recordings or audio tracks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Audio"]
    class_class_curie: ClassVar[str] = "EVORAO:Audio"
    class_name: ClassVar[str] = "Audio"
    class_model_uri: ClassVar[URIRef] = EVORAO.Audio

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Video(File):
    """
    Subclass of File representing moving visual media, such as recordings, presentations, or movies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Video"]
    class_class_curie: ClassVar[str] = "EVORAO:Video"
    class_name: ClassVar[str] = "Video"
    class_model_uri: ClassVar[URIRef] = EVORAO.Video

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Image(File):
    """
    Subclass of File representing visual content such as pictures, diagrams, or illustrations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Image"]
    class_class_curie: ClassVar[str] = "EVORAO:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = EVORAO.Image

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None
    altText: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.altText is not None and not isinstance(self.altText, str):
            self.altText = str(self.altText)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContactPoint(Resource):
    """
    Entity serving as focal point of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["ContactPoint"]
    class_class_curie: ClassVar[str] = "EVORAO:ContactPoint"
    class_name: ClassVar[str] = "ContactPoint"
    class_model_uri: ClassVar[URIRef] = EVORAO.ContactPoint

    name: str = None
    description: Optional[str] = None
    email: Optional[str] = None
    telephone: Optional[str] = None
    streetAddress: Optional[str] = None
    addressLocality: Optional[str] = None
    addressRegion: Optional[str] = None
    postalCode: Optional[str] = None
    addressCountry: Optional[Union[dict, Country]] = None
    oRCIDiD: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.telephone is not None and not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        if self.streetAddress is not None and not isinstance(self.streetAddress, str):
            self.streetAddress = str(self.streetAddress)

        if self.addressLocality is not None and not isinstance(self.addressLocality, str):
            self.addressLocality = str(self.addressLocality)

        if self.addressRegion is not None and not isinstance(self.addressRegion, str):
            self.addressRegion = str(self.addressRegion)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.addressCountry is not None and not isinstance(self.addressCountry, Country):
            self.addressCountry = Country(**as_dict(self.addressCountry))

        if self.oRCIDiD is not None and not isinstance(self.oRCIDiD, str):
            self.oRCIDiD = str(self.oRCIDiD)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class License(Resource):
    """
    The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any
    restrictions or permissions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["License"]
    class_class_curie: ClassVar[str] = "EVORAO:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = EVORAO.License

    title: str = None
    description: Optional[str] = None
    resourceURL: Optional[Union[str, URI]] = None
    licensingOrAttribution: Optional[str] = None
    logo: Optional[Union[dict, Image]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resourceURL is not None and not isinstance(self.resourceURL, URI):
            self.resourceURL = URI(self.resourceURL)

        if self.licensingOrAttribution is not None and not isinstance(self.licensingOrAttribution, str):
            self.licensingOrAttribution = str(self.licensingOrAttribution)

        if self.logo is not None and not isinstance(self.logo, Image):
            self.logo = Image(**as_dict(self.logo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Certification(Resource):
    """
    Assurance given by an independent certification body that a product, service or system meets the requirements of a
    standard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORAO["Certification"]
    class_class_curie: ClassVar[str] = "EVORAO:Certification"
    class_name: ClassVar[str] = "Certification"
    class_model_uri: ClassVar[URIRef] = EVORAO.Certification

    title: str = None
    description: Optional[str] = None
    logo: Optional[Union[dict, Image]] = None
    certificationDocument: Optional[Union[Union[dict, Document], list[Union[dict, Document]]]] = empty_list()
    resourceURL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.logo is not None and not isinstance(self.logo, Image):
            self.logo = Image(**as_dict(self.logo))

        self._normalize_inlined_as_dict(slot_name="certificationDocument", slot_type=Document, key_name="name", keyed=False)

        if self.resourceURL is not None and not isinstance(self.resourceURL, URI):
            self.resourceURL = URI(self.resourceURL)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=EVORAO.title, domain=None, range=str)

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=EVORAO.description, domain=None, range=Optional[str])

slots.endpointURL = Slot(uri=DCAT.endpointURL, name="endpointURL", curie=DCAT.curie('endpointURL'),
                   model_uri=EVORAO.endpointURL, domain=None, range=Union[str, URI])

slots.ID = Slot(uri=EVORAO.ID, name="ID", curie=EVORAO.curie('ID'),
                   model_uri=EVORAO.ID, domain=None, range=str)

slots.versionOf = Slot(uri=EVORAO.versionOf, name="versionOf", curie=EVORAO.curie('versionOf'),
                   model_uri=EVORAO.versionOf, domain=None, range=Union[dict, Dataset])

slots.taxon = Slot(uri=EVORAO.taxon, name="taxon", curie=EVORAO.curie('taxon'),
                   model_uri=EVORAO.taxon, domain=None, range=Union[dict, Taxon])

slots.taxonDataProvider = Slot(uri=EVORAO.taxonDataProvider, name="taxonDataProvider", curie=EVORAO.curie('taxonDataProvider'),
                   model_uri=EVORAO.taxonDataProvider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.version = Slot(uri=EVORAO.version, name="version", curie=EVORAO.curie('version'),
                   model_uri=EVORAO.version, domain=None, range=Union[dict, Version])

slots.versionDataProvider = Slot(uri=EVORAO.versionDataProvider, name="versionDataProvider", curie=EVORAO.curie('versionDataProvider'),
                   model_uri=EVORAO.versionDataProvider, domain=None, range=Union[dict, DataProvider])

slots.rank = Slot(uri=EVORAO.rank, name="rank", curie=EVORAO.curie('rank'),
                   model_uri=EVORAO.rank, domain=None, range=Union[dict, TaxonomicRank])

slots.rankDataProvider = Slot(uri=EVORAO.rankDataProvider, name="rankDataProvider", curie=EVORAO.curie('rankDataProvider'),
                   model_uri=EVORAO.rankDataProvider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.license = Slot(uri=EVORAO.license, name="license", curie=EVORAO.curie('license'),
                   model_uri=EVORAO.license, domain=None, range=Optional[Union[dict, License]])

slots.loginRequestMethod = Slot(uri=EVORAO.loginRequestMethod, name="loginRequestMethod", curie=EVORAO.curie('loginRequestMethod'),
                   model_uri=EVORAO.loginRequestMethod, domain=None, range=Optional[str])

slots.loginURL = Slot(uri=EVORAO.loginURL, name="loginURL", curie=EVORAO.curie('loginURL'),
                   model_uri=EVORAO.loginURL, domain=None, range=Optional[Union[str, URI]])

slots.loginTokenName = Slot(uri=EVORAO.loginTokenName, name="loginTokenName", curie=EVORAO.curie('loginTokenName'),
                   model_uri=EVORAO.loginTokenName, domain=None, range=Optional[str])

slots.queryMethod = Slot(uri=EVORAO.queryMethod, name="queryMethod", curie=EVORAO.curie('queryMethod'),
                   model_uri=EVORAO.queryMethod, domain=None, range=str)

slots.contentType = Slot(uri=EVORAO.contentType, name="contentType", curie=EVORAO.curie('contentType'),
                   model_uri=EVORAO.contentType, domain=None, range=str)

slots.providedEntityType = Slot(uri=EVORAO.providedEntityType, name="providedEntityType", curie=EVORAO.curie('providedEntityType'),
                   model_uri=EVORAO.providedEntityType, domain=None, range=Union[dict, Dataset])

slots.weight = Slot(uri=EVORAO.weight, name="weight", curie=EVORAO.curie('weight'),
                   model_uri=EVORAO.weight, domain=None, range=int)

slots.pathogenName = Slot(uri=EVORAO.pathogenName, name="pathogenName", curie=EVORAO.curie('pathogenName'),
                   model_uri=EVORAO.pathogenName, domain=None, range=Union[dict, CommonName])

slots.pathogenType = Slot(uri=EVORAO.pathogenType, name="pathogenType", curie=EVORAO.curie('pathogenType'),
                   model_uri=EVORAO.pathogenType, domain=None, range=str)

slots.hostType = Slot(uri=EVORAO.hostType, name="hostType", curie=EVORAO.curie('hostType'),
                   model_uri=EVORAO.hostType, domain=None, range=Optional[Union[str, list[str]]])

slots.subspecies = Slot(uri=EVORAO.subspecies, name="subspecies", curie=EVORAO.curie('subspecies'),
                   model_uri=EVORAO.subspecies, domain=None, range=Optional[str])

slots.strain = Slot(uri=EVORAO.strain, name="strain", curie=EVORAO.curie('strain'),
                   model_uri=EVORAO.strain, domain=None, range=Optional[str])

slots.isolate = Slot(uri=EVORAO.isolate, name="isolate", curie=EVORAO.curie('isolate'),
                   model_uri=EVORAO.isolate, domain=None, range=Optional[str])

slots.genotype = Slot(uri=EVORAO.genotype, name="genotype", curie=EVORAO.curie('genotype'),
                   model_uri=EVORAO.genotype, domain=None, range=Optional[str])

slots.serotype = Slot(uri=EVORAO.serotype, name="serotype", curie=EVORAO.curie('serotype'),
                   model_uri=EVORAO.serotype, domain=None, range=Optional[str])

slots.variant = Slot(uri=EVORAO.variant, name="variant", curie=EVORAO.curie('variant'),
                   model_uri=EVORAO.variant, domain=None, range=Optional[Union[dict, Variant]])

slots.authors = Slot(uri=EVORAO.authors, name="authors", curie=EVORAO.curie('authors'),
                   model_uri=EVORAO.authors, domain=None, range=str)

slots.abstract = Slot(uri=EVORAO.abstract, name="abstract", curie=EVORAO.curie('abstract'),
                   model_uri=EVORAO.abstract, domain=None, range=str)

slots.relatedDOI = Slot(uri=EVORAO.relatedDOI, name="relatedDOI", curie=EVORAO.curie('relatedDOI'),
                   model_uri=EVORAO.relatedDOI, domain=None, range=Optional[Union[Union[dict, DOI], list[Union[dict, DOI]]]])

slots.journal = Slot(uri=EVORAO.journal, name="journal", curie=EVORAO.curie('journal'),
                   model_uri=EVORAO.journal, domain=None, range=Optional[Union[dict, Journal]])

slots.termDataProvider = Slot(uri=EVORAO.termDataProvider, name="termDataProvider", curie=EVORAO.curie('termDataProvider'),
                   model_uri=EVORAO.termDataProvider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.term = Slot(uri=EVORAO.term, name="term", curie=EVORAO.curie('term'),
                   model_uri=EVORAO.term, domain=None, range=Optional[Union[Union[dict, Term], list[Union[dict, Term]]]])

slots.inVocabulary = Slot(uri=EVORAO.inVocabulary, name="inVocabulary", curie=EVORAO.curie('inVocabulary'),
                   model_uri=EVORAO.inVocabulary, domain=None, range=Union[dict, Vocabulary])

slots.alternateName = Slot(uri=EVORAO.alternateName, name="alternateName", curie=EVORAO.curie('alternateName'),
                   model_uri=EVORAO.alternateName, domain=None, range=Optional[Union[Union[dict, AlternateName], list[Union[dict, AlternateName]]]])

slots.sourceOfInformation = Slot(uri=EVORAO.sourceOfInformation, name="sourceOfInformation", curie=EVORAO.curie('sourceOfInformation'),
                   model_uri=EVORAO.sourceOfInformation, domain=None, range=Optional[Union[str, list[str]]])

slots.parentCategory = Slot(uri=EVORAO.parentCategory, name="parentCategory", curie=EVORAO.curie('parentCategory'),
                   model_uri=EVORAO.parentCategory, domain=None, range=Optional[Union[dict, ProductCategory]])

slots.alpha2Code = Slot(uri=EVORAO.alpha2Code, name="alpha2Code", curie=EVORAO.curie('alpha2Code'),
                   model_uri=EVORAO.alpha2Code, domain=None, range=str)

slots.taxonomy = Slot(uri=EVORAO.taxonomy, name="taxonomy", curie=EVORAO.curie('taxonomy'),
                   model_uri=EVORAO.taxonomy, domain=None, range=Optional[Union[Union[dict, Taxonomy], list[Union[dict, Taxonomy]]]])

slots.parentTaxon = Slot(uri=EVORAO.parentTaxon, name="parentTaxon", curie=EVORAO.curie('parentTaxon'),
                   model_uri=EVORAO.parentTaxon, domain=None, range=Union[dict, Taxon])

slots.previouslyKnownAs = Slot(uri=EVORAO.previouslyKnownAs, name="previouslyKnownAs", curie=EVORAO.curie('previouslyKnownAs'),
                   model_uri=EVORAO.previouslyKnownAs, domain=None, range=Optional[Union[Union[dict, Taxon], list[Union[dict, Taxon]]]])

slots.externalEquivalentTaxon = Slot(uri=EVORAO.externalEquivalentTaxon, name="externalEquivalentTaxon", curie=EVORAO.curie('externalEquivalentTaxon'),
                   model_uri=EVORAO.externalEquivalentTaxon, domain=None, range=Optional[Union[Union[dict, Taxon], list[Union[dict, Taxon]]]])

slots.taxonomicID = Slot(uri=EVORAO.taxonomicID, name="taxonomicID", curie=EVORAO.curie('taxonomicID'),
                   model_uri=EVORAO.taxonomicID, domain=None, range=str)

slots.taxonomicNodeID = Slot(uri=EVORAO.taxonomicNodeID, name="taxonomicNodeID", curie=EVORAO.curie('taxonomicNodeID'),
                   model_uri=EVORAO.taxonomicNodeID, domain=None, range=Optional[str])

slots.reference = Slot(uri=EVORAO.reference, name="reference", curie=EVORAO.curie('reference'),
                   model_uri=EVORAO.reference, domain=None, range=str)

slots.referenceLabel = Slot(uri=EVORAO.referenceLabel, name="referenceLabel", curie=EVORAO.curie('referenceLabel'),
                   model_uri=EVORAO.referenceLabel, domain=None, range=str)

slots.referenceProviderPrefix = Slot(uri=EVORAO.referenceProviderPrefix, name="referenceProviderPrefix", curie=EVORAO.curie('referenceProviderPrefix'),
                   model_uri=EVORAO.referenceProviderPrefix, domain=None, range=str)

slots.referenceProviderName = Slot(uri=EVORAO.referenceProviderName, name="referenceProviderName", curie=EVORAO.curie('referenceProviderName'),
                   model_uri=EVORAO.referenceProviderName, domain=None, range=str)

slots.sequenceReference = Slot(uri=EVORAO.sequenceReference, name="sequenceReference", curie=EVORAO.curie('sequenceReference'),
                   model_uri=EVORAO.sequenceReference, domain=None, range=Optional[Union[Union[dict, SequenceReference], list[Union[dict, SequenceReference]]]])

slots.sequenceFASTA = Slot(uri=EVORAO.sequenceFASTA, name="sequenceFASTA", curie=EVORAO.curie('sequenceFASTA'),
                   model_uri=EVORAO.sequenceFASTA, domain=None, range=Optional[str])

slots.accessionNumber = Slot(uri=EVORAO.accessionNumber, name="accessionNumber", curie=EVORAO.curie('accessionNumber'),
                   model_uri=EVORAO.accessionNumber, domain=None, range=str)

slots.sequenceProvider = Slot(uri=EVORAO.sequenceProvider, name="sequenceProvider", curie=EVORAO.curie('sequenceProvider'),
                   model_uri=EVORAO.sequenceProvider, domain=None, range=str)

slots.name = Slot(uri=EVORAO.name, name="name", curie=EVORAO.curie('name'),
                   model_uri=EVORAO.name, domain=None, range=str)

slots.homePage = Slot(uri=EVORAO.homePage, name="homePage", curie=EVORAO.curie('homePage'),
                   model_uri=EVORAO.homePage, domain=None, range=Optional[Union[str, URI]])

slots.contactPoint = Slot(uri=EVORAO.contactPoint, name="contactPoint", curie=EVORAO.curie('contactPoint'),
                   model_uri=EVORAO.contactPoint, domain=None, range=Optional[Union[dict, ContactPoint]])

slots.logo = Slot(uri=EVORAO.logo, name="logo", curie=EVORAO.curie('logo'),
                   model_uri=EVORAO.logo, domain=None, range=Optional[Union[dict, Image]])

slots.oRCIDiD = Slot(uri=EVORAO.oRCIDiD, name="oRCIDiD", curie=EVORAO.curie('oRCIDiD'),
                   model_uri=EVORAO.oRCIDiD, domain=None, range=Optional[str])

slots.country = Slot(uri=EVORAO.country, name="country", curie=EVORAO.curie('country'),
                   model_uri=EVORAO.country, domain=None, range=Optional[Union[dict, Country]])

slots.rORiD = Slot(uri=EVORAO.rORiD, name="rORiD", curie=EVORAO.curie('rORiD'),
                   model_uri=EVORAO.rORiD, domain=None, range=Optional[str])

slots.memberOfRI = Slot(uri=EVORAO.memberOfRI, name="memberOfRI", curie=EVORAO.curie('memberOfRI'),
                   model_uri=EVORAO.memberOfRI, domain=None, range=Optional[Union[Union[dict, RI], list[Union[dict, RI]]]])

slots.recombinantMaterial = Slot(uri=EVORAO.recombinantMaterial, name="recombinantMaterial", curie=EVORAO.curie('recombinantMaterial'),
                   model_uri=EVORAO.recombinantMaterial, domain=None, range=Union[bool, Bool])

slots.biologicalSourceType = Slot(uri=EVORAO.biologicalSourceType, name="biologicalSourceType", curie=EVORAO.curie('biologicalSourceType'),
                   model_uri=EVORAO.biologicalSourceType, domain=None, range=Union[bool, Bool])

slots.biologicalPartOrigin = Slot(uri=EVORAO.biologicalPartOrigin, name="biologicalPartOrigin", curie=EVORAO.curie('biologicalPartOrigin'),
                   model_uri=EVORAO.biologicalPartOrigin, domain=None, range=Union[Union[dict, BiologicalPartOrigin], list[Union[dict, BiologicalPartOrigin]]])

slots.recombinantPartIdentification = Slot(uri=EVORAO.recombinantPartIdentification, name="recombinantPartIdentification", curie=EVORAO.curie('recombinantPartIdentification'),
                   model_uri=EVORAO.recombinantPartIdentification, domain=None, range=Optional[Union[dict, RecombinantPartIdentification]])

slots.accessToPhysicalGeneticResource = Slot(uri=EVORAO.accessToPhysicalGeneticResource, name="accessToPhysicalGeneticResource", curie=EVORAO.curie('accessToPhysicalGeneticResource'),
                   model_uri=EVORAO.accessToPhysicalGeneticResource, domain=None, range=Union[bool, Bool])

slots.countryOfCollection = Slot(uri=EVORAO.countryOfCollection, name="countryOfCollection", curie=EVORAO.curie('countryOfCollection'),
                   model_uri=EVORAO.countryOfCollection, domain=None, range=Union[dict, Country])

slots.indigenousPoepleAndLocalCommunityOrigin = Slot(uri=EVORAO.indigenousPoepleAndLocalCommunityOrigin, name="indigenousPoepleAndLocalCommunityOrigin", curie=EVORAO.curie('indigenousPoepleAndLocalCommunityOrigin'),
                   model_uri=EVORAO.indigenousPoepleAndLocalCommunityOrigin, domain=None, range=Optional[Union[dict, IPLCOrigin]])

slots.collectionDate = Slot(uri=EVORAO.collectionDate, name="collectionDate", curie=EVORAO.curie('collectionDate'),
                   model_uri=EVORAO.collectionDate, domain=None, range=Union[str, XSDDateTime])

slots.beforeDate = Slot(uri=EVORAO.beforeDate, name="beforeDate", curie=EVORAO.curie('beforeDate'),
                   model_uri=EVORAO.beforeDate, domain=None, range=Union[bool, Bool])

slots.permitIdentifierForABS = Slot(uri=EVORAO.permitIdentifierForABS, name="permitIdentifierForABS", curie=EVORAO.curie('permitIdentifierForABS'),
                   model_uri=EVORAO.permitIdentifierForABS, domain=None, range=Optional[str])

slots.modificationsFromTheReferenceSequences = Slot(uri=EVORAO.modificationsFromTheReferenceSequences, name="modificationsFromTheReferenceSequences", curie=EVORAO.curie('modificationsFromTheReferenceSequences'),
                   model_uri=EVORAO.modificationsFromTheReferenceSequences, domain=None, range=Union[bool, Bool])

slots.descriptionOfModificationsMadeFromTheReferenceSequences = Slot(uri=EVORAO.descriptionOfModificationsMadeFromTheReferenceSequences, name="descriptionOfModificationsMadeFromTheReferenceSequences", curie=EVORAO.curie('descriptionOfModificationsMadeFromTheReferenceSequences'),
                   model_uri=EVORAO.descriptionOfModificationsMadeFromTheReferenceSequences, domain=None, range=Optional[str])

slots.partIdentification = Slot(uri=EVORAO.partIdentification, name="partIdentification", curie=EVORAO.curie('partIdentification'),
                   model_uri=EVORAO.partIdentification, domain=None, range=str)

slots.sequence = Slot(uri=EVORAO.sequence, name="sequence", curie=EVORAO.curie('sequence'),
                   model_uri=EVORAO.sequence, domain=None, range=Union[Union[dict, Sequence], list[Union[dict, Sequence]]])

slots.collectionItem = Slot(uri=EVORAO.collectionItem, name="collectionItem", curie=EVORAO.curie('collectionItem'),
                   model_uri=EVORAO.collectionItem, domain=None, range=Optional[Union[Union[dict, ProductOrService], list[Union[dict, ProductOrService]]]])

slots.collectionDataProvider = Slot(uri=EVORAO.collectionDataProvider, name="collectionDataProvider", curie=EVORAO.curie('collectionDataProvider'),
                   model_uri=EVORAO.collectionDataProvider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.accessPointURL = Slot(uri=EVORAO.accessPointURL, name="accessPointURL", curie=EVORAO.curie('accessPointURL'),
                   model_uri=EVORAO.accessPointURL, domain=None, range=Union[str, URI])

slots.refSKU = Slot(uri=EVORAO.refSKU, name="refSKU", curie=EVORAO.curie('refSKU'),
                   model_uri=EVORAO.refSKU, domain=None, range=str)

slots.unitDefinition = Slot(uri=EVORAO.unitDefinition, name="unitDefinition", curie=EVORAO.curie('unitDefinition'),
                   model_uri=EVORAO.unitDefinition, domain=None, range=Optional[str])

slots.category = Slot(uri=EVORAO.category, name="category", curie=EVORAO.curie('category'),
                   model_uri=EVORAO.category, domain=None, range=Union[dict, ProductCategory])

slots.additionalCategory = Slot(uri=EVORAO.additionalCategory, name="additionalCategory", curie=EVORAO.curie('additionalCategory'),
                   model_uri=EVORAO.additionalCategory, domain=None, range=Optional[Union[Union[dict, ProductCategory], list[Union[dict, ProductCategory]]]])

slots.unitCost = Slot(uri=EVORAO.unitCost, name="unitCost", curie=EVORAO.curie('unitCost'),
                   model_uri=EVORAO.unitCost, domain=None, range=str)

slots.qualityGrading = Slot(uri=EVORAO.qualityGrading, name="qualityGrading", curie=EVORAO.curie('qualityGrading'),
                   model_uri=EVORAO.qualityGrading, domain=None, range=Optional[str])

slots.pathogenIdentification = Slot(uri=EVORAO.pathogenIdentification, name="pathogenIdentification", curie=EVORAO.curie('pathogenIdentification'),
                   model_uri=EVORAO.pathogenIdentification, domain=None, range=Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]])

slots.riskGroup = Slot(uri=EVORAO.riskGroup, name="riskGroup", curie=EVORAO.curie('riskGroup'),
                   model_uri=EVORAO.riskGroup, domain=None, range=Optional[Union[dict, RiskGroup]])

slots.biosafetyRestrictions = Slot(uri=EVORAO.biosafetyRestrictions, name="biosafetyRestrictions", curie=EVORAO.curie('biosafetyRestrictions'),
                   model_uri=EVORAO.biosafetyRestrictions, domain=None, range=Optional[str])

slots.canItBeUsedToProduceGMO = Slot(uri=EVORAO.canItBeUsedToProduceGMO, name="canItBeUsedToProduceGMO", curie=EVORAO.curie('canItBeUsedToProduceGMO'),
                   model_uri=EVORAO.canItBeUsedToProduceGMO, domain=None, range=Union[bool, Bool])

slots.provider = Slot(uri=EVORAO.provider, name="provider", curie=EVORAO.curie('provider'),
                   model_uri=EVORAO.provider, domain=None, range=Union[dict, Provider])

slots.collection = Slot(uri=EVORAO.collection, name="collection", curie=EVORAO.curie('collection'),
                   model_uri=EVORAO.collection, domain=None, range=Union[Union[dict, Collection], list[Union[dict, Collection]]])

slots.keywords = Slot(uri=EVORAO.keywords, name="keywords", curie=EVORAO.curie('keywords'),
                   model_uri=EVORAO.keywords, domain=None, range=Union[Union[dict, Keyword], list[Union[dict, Keyword]]])

slots.availability = Slot(uri=EVORAO.availability, name="availability", curie=EVORAO.curie('availability'),
                   model_uri=EVORAO.availability, domain=None, range=str)

slots.complementaryDocument = Slot(uri=EVORAO.complementaryDocument, name="complementaryDocument", curie=EVORAO.curie('complementaryDocument'),
                   model_uri=EVORAO.complementaryDocument, domain=None, range=Optional[Union[Union[dict, Document], list[Union[dict, Document]]]])

slots.technicalRecommendation = Slot(uri=EVORAO.technicalRecommendation, name="technicalRecommendation", curie=EVORAO.curie('technicalRecommendation'),
                   model_uri=EVORAO.technicalRecommendation, domain=None, range=Optional[str])

slots.productPicture = Slot(uri=EVORAO.productPicture, name="productPicture", curie=EVORAO.curie('productPicture'),
                   model_uri=EVORAO.productPicture, domain=None, range=Optional[Union[Union[dict, Image], list[Union[dict, Image]]]])

slots.externalRelatedReference = Slot(uri=EVORAO.externalRelatedReference, name="externalRelatedReference", curie=EVORAO.curie('externalRelatedReference'),
                   model_uri=EVORAO.externalRelatedReference, domain=None, range=Optional[Union[Union[dict, ExternalRelatedReference], list[Union[dict, ExternalRelatedReference]]]])

slots.certification = Slot(uri=EVORAO.certification, name="certification", curie=EVORAO.curie('certification'),
                   model_uri=EVORAO.certification, domain=None, range=Optional[Union[Union[dict, Certification], list[Union[dict, Certification]]]])

slots.internalReference = Slot(uri=EVORAO.internalReference, name="internalReference", curie=EVORAO.curie('internalReference'),
                   model_uri=EVORAO.internalReference, domain=None, range=Optional[str])

slots.note = Slot(uri=EVORAO.note, name="note", curie=EVORAO.curie('note'),
                   model_uri=EVORAO.note, domain=None, range=Optional[str])

slots.modelSpecies = Slot(uri=EVORAO.modelSpecies, name="modelSpecies", curie=EVORAO.curie('modelSpecies'),
                   model_uri=EVORAO.modelSpecies, domain=None, range=Optional[str])

slots.modelType = Slot(uri=EVORAO.modelType, name="modelType", curie=EVORAO.curie('modelType'),
                   model_uri=EVORAO.modelType, domain=None, range=Optional[str])

slots.hasIATAClassification = Slot(uri=EVORAO.hasIATAClassification, name="hasIATAClassification", curie=EVORAO.curie('hasIATAClassification'),
                   model_uri=EVORAO.hasIATAClassification, domain=None, range=Union[dict, IATAClassification])

slots.shippingConditions = Slot(uri=EVORAO.shippingConditions, name="shippingConditions", curie=EVORAO.curie('shippingConditions'),
                   model_uri=EVORAO.shippingConditions, domain=None, range=str)

slots.materialSafetyDataSheet = Slot(uri=EVORAO.materialSafetyDataSheet, name="materialSafetyDataSheet", curie=EVORAO.curie('materialSafetyDataSheet'),
                   model_uri=EVORAO.materialSafetyDataSheet, domain=None, range=Optional[Union[dict, MSDS]])

slots.originator = Slot(uri=EVORAO.originator, name="originator", curie=EVORAO.curie('originator'),
                   model_uri=EVORAO.originator, domain=None, range=Optional[Union[dict, Originator]])

slots.storageConditions = Slot(uri=EVORAO.storageConditions, name="storageConditions", curie=EVORAO.curie('storageConditions'),
                   model_uri=EVORAO.storageConditions, domain=None, range=str)

slots.thirdPartyDistributionConsent = Slot(uri=EVORAO.thirdPartyDistributionConsent, name="thirdPartyDistributionConsent", curie=EVORAO.curie('thirdPartyDistributionConsent'),
                   model_uri=EVORAO.thirdPartyDistributionConsent, domain=None, range=Optional[Union[bool, Bool]])

slots.usageRestrictions = Slot(uri=EVORAO.usageRestrictions, name="usageRestrictions", curie=EVORAO.curie('usageRestrictions'),
                   model_uri=EVORAO.usageRestrictions, domain=None, range=Optional[str])

slots.productionSystem = Slot(uri=EVORAO.productionSystem, name="productionSystem", curie=EVORAO.curie('productionSystem'),
                   model_uri=EVORAO.productionSystem, domain=None, range=Optional[str])

slots.antibodyPurifiedByAffinity = Slot(uri=EVORAO.antibodyPurifiedByAffinity, name="antibodyPurifiedByAffinity", curie=EVORAO.curie('antibodyPurifiedByAffinity'),
                   model_uri=EVORAO.antibodyPurifiedByAffinity, domain=None, range=Union[bool, Bool])

slots.specificityDocumented = Slot(uri=EVORAO.specificityDocumented, name="specificityDocumented", curie=EVORAO.curie('specificityDocumented'),
                   model_uri=EVORAO.specificityDocumented, domain=None, range=Union[bool, Bool])

slots.targetedAntigen = Slot(uri=EVORAO.targetedAntigen, name="targetedAntigen", curie=EVORAO.curie('targetedAntigen'),
                   model_uri=EVORAO.targetedAntigen, domain=None, range=str)

slots.hybridomaDescription = Slot(uri=EVORAO.hybridomaDescription, name="hybridomaDescription", curie=EVORAO.curie('hybridomaDescription'),
                   model_uri=EVORAO.hybridomaDescription, domain=None, range=str)

slots.biologicalMaterialOrigin = Slot(uri=EVORAO.biologicalMaterialOrigin, name="biologicalMaterialOrigin", curie=EVORAO.curie('biologicalMaterialOrigin'),
                   model_uri=EVORAO.biologicalMaterialOrigin, domain=None, range=Union[dict, BiologicalMaterialOrigin])

slots.relatedPDB = Slot(uri=EVORAO.relatedPDB, name="relatedPDB", curie=EVORAO.curie('relatedPDB'),
                   model_uri=EVORAO.relatedPDB, domain=None, range=Optional[Union[Union[dict, PDBReference], list[Union[dict, PDBReference]]]])

slots.specialFeature = Slot(uri=EVORAO.specialFeature, name="specialFeature", curie=EVORAO.curie('specialFeature'),
                   model_uri=EVORAO.specialFeature, domain=None, range=Optional[Union[Union[dict, SpecialFeature], list[Union[dict, SpecialFeature]]]])

slots.proteinTAG = Slot(uri=EVORAO.proteinTAG, name="proteinTAG", curie=EVORAO.curie('proteinTAG'),
                   model_uri=EVORAO.proteinTAG, domain=None, range=Optional[Union[Union[dict, ProteinTag], list[Union[dict, ProteinTag]]]])

slots.domain = Slot(uri=EVORAO.domain, name="domain", curie=EVORAO.curie('domain'),
                   model_uri=EVORAO.domain, domain=None, range=Optional[Union[str, list[str]]])

slots.expressedAs = Slot(uri=EVORAO.expressedAs, name="expressedAs", curie=EVORAO.curie('expressedAs'),
                   model_uri=EVORAO.expressedAs, domain=None, range=Optional[Union[str, list[str]]])

slots.inclusionBodiesType = Slot(uri=EVORAO.inclusionBodiesType, name="inclusionBodiesType", curie=EVORAO.curie('inclusionBodiesType'),
                   model_uri=EVORAO.inclusionBodiesType, domain=None, range=Optional[Union[str, list[str]]])

slots.expressionSystem = Slot(uri=EVORAO.expressionSystem, name="expressionSystem", curie=EVORAO.curie('expressionSystem'),
                   model_uri=EVORAO.expressionSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalCharacterization = Slot(uri=EVORAO.functionalCharacterization, name="functionalCharacterization", curie=EVORAO.curie('functionalCharacterization'),
                   model_uri=EVORAO.functionalCharacterization, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalTechnicalDescription = Slot(uri=EVORAO.functionalTechnicalDescription, name="functionalTechnicalDescription", curie=EVORAO.curie('functionalTechnicalDescription'),
                   model_uri=EVORAO.functionalTechnicalDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.proteinPurification = Slot(uri=EVORAO.proteinPurification, name="proteinPurification", curie=EVORAO.curie('proteinPurification'),
                   model_uri=EVORAO.proteinPurification, domain=None, range=Optional[Union[str, list[str]]])

slots.theTAGStatusOfTheSolubilizedProtein = Slot(uri=EVORAO.theTAGStatusOfTheSolubilizedProtein, name="theTAGStatusOfTheSolubilizedProtein", curie=EVORAO.curie('theTAGStatusOfTheSolubilizedProtein'),
                   model_uri=EVORAO.theTAGStatusOfTheSolubilizedProtein, domain=None, range=Optional[Union[str, list[str]]])

slots.typeOfFunctionalCharacterization = Slot(uri=EVORAO.typeOfFunctionalCharacterization, name="typeOfFunctionalCharacterization", curie=EVORAO.curie('typeOfFunctionalCharacterization'),
                   model_uri=EVORAO.typeOfFunctionalCharacterization, domain=None, range=Optional[Union[str, list[str]]])

slots.hasGbFileOfTheConstruct = Slot(uri=EVORAO.hasGbFileOfTheConstruct, name="hasGbFileOfTheConstruct", curie=EVORAO.curie('hasGbFileOfTheConstruct'),
                   model_uri=EVORAO.hasGbFileOfTheConstruct, domain=None, range=Optional[Union[Union[dict, Data], list[Union[dict, Data]]]])

slots.isItAClonedNucleicAcid = Slot(uri=EVORAO.isItAClonedNucleicAcid, name="isItAClonedNucleicAcid", curie=EVORAO.curie('isItAClonedNucleicAcid'),
                   model_uri=EVORAO.isItAClonedNucleicAcid, domain=None, range=Union[bool, Bool])

slots.clonedIntoPlasmid = Slot(uri=EVORAO.clonedIntoPlasmid, name="clonedIntoPlasmid", curie=EVORAO.curie('clonedIntoPlasmid'),
                   model_uri=EVORAO.clonedIntoPlasmid, domain=None, range=Optional[Union[dict, ExpressionVector]])

slots.pasmidSelection = Slot(uri=EVORAO.pasmidSelection, name="pasmidSelection", curie=EVORAO.curie('pasmidSelection'),
                   model_uri=EVORAO.pasmidSelection, domain=None, range=Optional[Union[Union[dict, PlasmidSelection], list[Union[dict, PlasmidSelection]]]])

slots.hasTAG = Slot(uri=EVORAO.hasTAG, name="hasTAG", curie=EVORAO.curie('hasTAG'),
                   model_uri=EVORAO.hasTAG, domain=None, range=Union[dict, ProteinTag])

slots.regionEncompassedInThisProduct = Slot(uri=EVORAO.regionEncompassedInThisProduct, name="regionEncompassedInThisProduct", curie=EVORAO.curie('regionEncompassedInThisProduct'),
                   model_uri=EVORAO.regionEncompassedInThisProduct, domain=None, range=str)

slots.mutationObserved = Slot(uri=EVORAO.mutationObserved, name="mutationObserved", curie=EVORAO.curie('mutationObserved'),
                   model_uri=EVORAO.mutationObserved, domain=None, range=Union[bool, Bool])

slots.observedMutations = Slot(uri=EVORAO.observedMutations, name="observedMutations", curie=EVORAO.curie('observedMutations'),
                   model_uri=EVORAO.observedMutations, domain=None, range=Optional[str])

slots.identificationTechnique = Slot(uri=EVORAO.identificationTechnique, name="identificationTechnique", curie=EVORAO.curie('identificationTechnique'),
                   model_uri=EVORAO.identificationTechnique, domain=None, range=Optional[str])

slots.sequencing = Slot(uri=EVORAO.sequencing, name="sequencing", curie=EVORAO.curie('sequencing'),
                   model_uri=EVORAO.sequencing, domain=None, range=str)

slots.titer = Slot(uri=EVORAO.titer, name="titer", curie=EVORAO.curie('titer'),
                   model_uri=EVORAO.titer, domain=None, range=str)

slots.sequenceChecked = Slot(uri=EVORAO.sequenceChecked, name="sequenceChecked", curie=EVORAO.curie('sequenceChecked'),
                   model_uri=EVORAO.sequenceChecked, domain=None, range=Union[bool, Bool])

slots.hasSOPFile = Slot(uri=EVORAO.hasSOPFile, name="hasSOPFile", curie=EVORAO.curie('hasSOPFile'),
                   model_uri=EVORAO.hasSOPFile, domain=None, range=Optional[Union[Union[dict, File], list[Union[dict, File]]]])

slots.specificity = Slot(uri=EVORAO.specificity, name="specificity", curie=EVORAO.curie('specificity'),
                   model_uri=EVORAO.specificity, domain=None, range=Optional[str])

slots.targetedRegion = Slot(uri=EVORAO.targetedRegion, name="targetedRegion", curie=EVORAO.curie('targetedRegion'),
                   model_uri=EVORAO.targetedRegion, domain=None, range=Optional[str])

slots.productsOfTheBundle = Slot(uri=EVORAO.productsOfTheBundle, name="productsOfTheBundle", curie=EVORAO.curie('productsOfTheBundle'),
                   model_uri=EVORAO.productsOfTheBundle, domain=None, range=Union[Union[dict, Product], list[Union[dict, Product]]])

slots.suspectedEpidemiologicalOrigin = Slot(uri=EVORAO.suspectedEpidemiologicalOrigin, name="suspectedEpidemiologicalOrigin", curie=EVORAO.curie('suspectedEpidemiologicalOrigin'),
                   model_uri=EVORAO.suspectedEpidemiologicalOrigin, domain=None, range=Optional[Union[Union[dict, GeographicalOrigin], list[Union[dict, GeographicalOrigin]]]])

slots.isolationHost = Slot(uri=EVORAO.isolationHost, name="isolationHost", curie=EVORAO.curie('isolationHost'),
                   model_uri=EVORAO.isolationHost, domain=None, range=Optional[Union[Union[dict, IsolationHost], list[Union[dict, IsolationHost]]]])

slots.productionCellLine = Slot(uri=EVORAO.productionCellLine, name="productionCellLine", curie=EVORAO.curie('productionCellLine'),
                   model_uri=EVORAO.productionCellLine, domain=None, range=Optional[Union[Union[dict, ProductionCellLine], list[Union[dict, ProductionCellLine]]]])

slots.propagationHost = Slot(uri=EVORAO.propagationHost, name="propagationHost", curie=EVORAO.curie('propagationHost'),
                   model_uri=EVORAO.propagationHost, domain=None, range=Optional[Union[Union[dict, PropagationHost], list[Union[dict, PropagationHost]]]])

slots.transmissionMethod = Slot(uri=EVORAO.transmissionMethod, name="transmissionMethod", curie=EVORAO.curie('transmissionMethod'),
                   model_uri=EVORAO.transmissionMethod, domain=None, range=Optional[Union[Union[dict, TransmissionMethod], list[Union[dict, TransmissionMethod]]]])

slots.cultivability = Slot(uri=EVORAO.cultivability, name="cultivability", curie=EVORAO.curie('cultivability'),
                   model_uri=EVORAO.cultivability, domain=None, range=str)

slots.clinicalInformation = Slot(uri=EVORAO.clinicalInformation, name="clinicalInformation", curie=EVORAO.curie('clinicalInformation'),
                   model_uri=EVORAO.clinicalInformation, domain=None, range=Optional[str])

slots.infectivity = Slot(uri=EVORAO.infectivity, name="infectivity", curie=EVORAO.curie('infectivity'),
                   model_uri=EVORAO.infectivity, domain=None, range=str)

slots.infectivityTest = Slot(uri=EVORAO.infectivityTest, name="infectivityTest", curie=EVORAO.curie('infectivityTest'),
                   model_uri=EVORAO.infectivityTest, domain=None, range=Optional[str])

slots.isolationTechnique = Slot(uri=EVORAO.isolationTechnique, name="isolationTechnique", curie=EVORAO.curie('isolationTechnique'),
                   model_uri=EVORAO.isolationTechnique, domain=None, range=Optional[str])

slots.isolationConditions = Slot(uri=EVORAO.isolationConditions, name="isolationConditions", curie=EVORAO.curie('isolationConditions'),
                   model_uri=EVORAO.isolationConditions, domain=None, range=Optional[str])

slots.letterOfAuthority = Slot(uri=EVORAO.letterOfAuthority, name="letterOfAuthority", curie=EVORAO.curie('letterOfAuthority'),
                   model_uri=EVORAO.letterOfAuthority, domain=None, range=str)

slots.passage = Slot(uri=EVORAO.passage, name="passage", curie=EVORAO.curie('passage'),
                   model_uri=EVORAO.passage, domain=None, range=Optional[str])

slots.genomeSequencing = Slot(uri=EVORAO.genomeSequencing, name="genomeSequencing", curie=EVORAO.curie('genomeSequencing'),
                   model_uri=EVORAO.genomeSequencing, domain=None, range=str)

slots.coInfectingViruses = Slot(uri=EVORAO.coInfectingViruses, name="coInfectingViruses", curie=EVORAO.curie('coInfectingViruses'),
                   model_uri=EVORAO.coInfectingViruses, domain=None, range=Optional[Union[Union[dict, VirusName], list[Union[dict, VirusName]]]])

slots.contaminationWithCoInfectingViruses = Slot(uri=EVORAO.contaminationWithCoInfectingViruses, name="contaminationWithCoInfectingViruses", curie=EVORAO.curie('contaminationWithCoInfectingViruses'),
                   model_uri=EVORAO.contaminationWithCoInfectingViruses, domain=None, range=Union[bool, Bool])

slots.mycoplasmicContent = Slot(uri=EVORAO.mycoplasmicContent, name="mycoplasmicContent", curie=EVORAO.curie('mycoplasmicContent'),
                   model_uri=EVORAO.mycoplasmicContent, domain=None, range=Union[bool, Bool])

slots.msdsContact = Slot(uri=EVORAO.msdsContact, name="msdsContact", curie=EVORAO.curie('msdsContact'),
                   model_uri=EVORAO.msdsContact, domain=None, range=Union[dict, ContactPoint])

slots.physicalChemicalProperties = Slot(uri=EVORAO.physicalChemicalProperties, name="physicalChemicalProperties", curie=EVORAO.curie('physicalChemicalProperties'),
                   model_uri=EVORAO.physicalChemicalProperties, domain=None, range=Optional[str])

slots.hazardsIdentification = Slot(uri=EVORAO.hazardsIdentification, name="hazardsIdentification", curie=EVORAO.curie('hazardsIdentification'),
                   model_uri=EVORAO.hazardsIdentification, domain=None, range=Optional[str])

slots.firstAidMeasures = Slot(uri=EVORAO.firstAidMeasures, name="firstAidMeasures", curie=EVORAO.curie('firstAidMeasures'),
                   model_uri=EVORAO.firstAidMeasures, domain=None, range=Optional[str])

slots.fireFightingMeasures = Slot(uri=EVORAO.fireFightingMeasures, name="fireFightingMeasures", curie=EVORAO.curie('fireFightingMeasures'),
                   model_uri=EVORAO.fireFightingMeasures, domain=None, range=Optional[str])

slots.accidentalReleaseMeasures = Slot(uri=EVORAO.accidentalReleaseMeasures, name="accidentalReleaseMeasures", curie=EVORAO.curie('accidentalReleaseMeasures'),
                   model_uri=EVORAO.accidentalReleaseMeasures, domain=None, range=Optional[str])

slots.handlingAndStorage = Slot(uri=EVORAO.handlingAndStorage, name="handlingAndStorage", curie=EVORAO.curie('handlingAndStorage'),
                   model_uri=EVORAO.handlingAndStorage, domain=None, range=Optional[str])

slots.exposureControlsPersonalProtection = Slot(uri=EVORAO.exposureControlsPersonalProtection, name="exposureControlsPersonalProtection", curie=EVORAO.curie('exposureControlsPersonalProtection'),
                   model_uri=EVORAO.exposureControlsPersonalProtection, domain=None, range=Optional[str])

slots.stabilityAndReactivity = Slot(uri=EVORAO.stabilityAndReactivity, name="stabilityAndReactivity", curie=EVORAO.curie('stabilityAndReactivity'),
                   model_uri=EVORAO.stabilityAndReactivity, domain=None, range=Optional[str])

slots.toxicologicalInformation = Slot(uri=EVORAO.toxicologicalInformation, name="toxicologicalInformation", curie=EVORAO.curie('toxicologicalInformation'),
                   model_uri=EVORAO.toxicologicalInformation, domain=None, range=Optional[str])

slots.ecologicalInformation = Slot(uri=EVORAO.ecologicalInformation, name="ecologicalInformation", curie=EVORAO.curie('ecologicalInformation'),
                   model_uri=EVORAO.ecologicalInformation, domain=None, range=Optional[str])

slots.disposalConsiderations = Slot(uri=EVORAO.disposalConsiderations, name="disposalConsiderations", curie=EVORAO.curie('disposalConsiderations'),
                   model_uri=EVORAO.disposalConsiderations, domain=None, range=Optional[str])

slots.transportInformation = Slot(uri=EVORAO.transportInformation, name="transportInformation", curie=EVORAO.curie('transportInformation'),
                   model_uri=EVORAO.transportInformation, domain=None, range=Optional[str])

slots.regulatoryInformation = Slot(uri=EVORAO.regulatoryInformation, name="regulatoryInformation", curie=EVORAO.curie('regulatoryInformation'),
                   model_uri=EVORAO.regulatoryInformation, domain=None, range=Optional[str])

slots.furtherInformation = Slot(uri=EVORAO.furtherInformation, name="furtherInformation", curie=EVORAO.curie('furtherInformation'),
                   model_uri=EVORAO.furtherInformation, domain=None, range=Optional[str])

slots.contentURL = Slot(uri=EVORAO.contentURL, name="contentURL", curie=EVORAO.curie('contentURL'),
                   model_uri=EVORAO.contentURL, domain=None, range=Union[str, URI])

slots.format = Slot(uri=EVORAO.format, name="format", curie=EVORAO.curie('format'),
                   model_uri=EVORAO.format, domain=None, range=str)

slots.altText = Slot(uri=EVORAO.altText, name="altText", curie=EVORAO.curie('altText'),
                   model_uri=EVORAO.altText, domain=None, range=Optional[str])

slots.email = Slot(uri=EVORAO.email, name="email", curie=EVORAO.curie('email'),
                   model_uri=EVORAO.email, domain=None, range=Optional[str])

slots.telephone = Slot(uri=EVORAO.telephone, name="telephone", curie=EVORAO.curie('telephone'),
                   model_uri=EVORAO.telephone, domain=None, range=Optional[str])

slots.streetAddress = Slot(uri=EVORAO.streetAddress, name="streetAddress", curie=EVORAO.curie('streetAddress'),
                   model_uri=EVORAO.streetAddress, domain=None, range=Optional[str])

slots.addressLocality = Slot(uri=EVORAO.addressLocality, name="addressLocality", curie=EVORAO.curie('addressLocality'),
                   model_uri=EVORAO.addressLocality, domain=None, range=Optional[str])

slots.addressRegion = Slot(uri=EVORAO.addressRegion, name="addressRegion", curie=EVORAO.curie('addressRegion'),
                   model_uri=EVORAO.addressRegion, domain=None, range=Optional[str])

slots.postalCode = Slot(uri=EVORAO.postalCode, name="postalCode", curie=EVORAO.curie('postalCode'),
                   model_uri=EVORAO.postalCode, domain=None, range=Optional[str])

slots.addressCountry = Slot(uri=EVORAO.addressCountry, name="addressCountry", curie=EVORAO.curie('addressCountry'),
                   model_uri=EVORAO.addressCountry, domain=None, range=Optional[Union[dict, Country]])

slots.resourceURL = Slot(uri=EVORAO.resourceURL, name="resourceURL", curie=EVORAO.curie('resourceURL'),
                   model_uri=EVORAO.resourceURL, domain=None, range=Optional[Union[str, URI]])

slots.licensingOrAttribution = Slot(uri=EVORAO.licensingOrAttribution, name="licensingOrAttribution", curie=EVORAO.curie('licensingOrAttribution'),
                   model_uri=EVORAO.licensingOrAttribution, domain=None, range=Optional[str])

slots.certificationDocument = Slot(uri=EVORAO.certificationDocument, name="certificationDocument", curie=EVORAO.curie('certificationDocument'),
                   model_uri=EVORAO.certificationDocument, domain=None, range=Optional[Union[Union[dict, Document], list[Union[dict, Document]]]])

slots.Dataset_title = Slot(uri=DCT.title, name="Dataset_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.Dataset_title, domain=Dataset, range=str)

slots.Dataset_description = Slot(uri=DCT.description, name="Dataset_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.Dataset_description, domain=Dataset, range=str)

slots.DataService_title = Slot(uri=DCT.title, name="DataService_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.DataService_title, domain=DataService, range=str)

slots.DataService_description = Slot(uri=DCT.description, name="DataService_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.DataService_description, domain=DataService, range=Optional[str])

slots.DataService_endpointURL = Slot(uri=DCAT.endpointURL, name="DataService_endpointURL", curie=DCAT.curie('endpointURL'),
                   model_uri=EVORAO.DataService_endpointURL, domain=DataService, range=Union[str, URI])

slots.Version_ID = Slot(uri=EVORAO.ID, name="Version_ID", curie=EVORAO.curie('ID'),
                   model_uri=EVORAO.Version_ID, domain=Version, range=str)

slots.Version_versionOf = Slot(uri=EVORAO.versionOf, name="Version_versionOf", curie=EVORAO.curie('versionOf'),
                   model_uri=EVORAO.Version_versionOf, domain=Version, range=Union[dict, Dataset])

slots.Taxonomy_taxon = Slot(uri=EVORAO.taxon, name="Taxonomy_taxon", curie=EVORAO.curie('taxon'),
                   model_uri=EVORAO.Taxonomy_taxon, domain=Taxonomy, range=Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]])

slots.Taxonomy_taxonDataProvider = Slot(uri=EVORAO.taxonDataProvider, name="Taxonomy_taxonDataProvider", curie=EVORAO.curie('taxonDataProvider'),
                   model_uri=EVORAO.Taxonomy_taxonDataProvider, domain=Taxonomy, range=Optional[Union[dict, "DataProvider"]])

slots.Taxonomy_version = Slot(uri=EVORAO.version, name="Taxonomy_version", curie=EVORAO.curie('version'),
                   model_uri=EVORAO.Taxonomy_version, domain=Taxonomy, range=Union[dict, Version])

slots.Taxonomy_versionDataProvider = Slot(uri=EVORAO.versionDataProvider, name="Taxonomy_versionDataProvider", curie=EVORAO.curie('versionDataProvider'),
                   model_uri=EVORAO.Taxonomy_versionDataProvider, domain=Taxonomy, range=Union[dict, "DataProvider"])

slots.Taxonomy_rank = Slot(uri=EVORAO.rank, name="Taxonomy_rank", curie=EVORAO.curie('rank'),
                   model_uri=EVORAO.Taxonomy_rank, domain=Taxonomy, range=Union[Union[dict, "TaxonomicRank"], list[Union[dict, "TaxonomicRank"]]])

slots.Taxonomy_rankDataProvider = Slot(uri=EVORAO.rankDataProvider, name="Taxonomy_rankDataProvider", curie=EVORAO.curie('rankDataProvider'),
                   model_uri=EVORAO.Taxonomy_rankDataProvider, domain=Taxonomy, range=Optional[Union[dict, "DataProvider"]])

slots.DataProvider_license = Slot(uri=EVORAO.license, name="DataProvider_license", curie=EVORAO.curie('license'),
                   model_uri=EVORAO.DataProvider_license, domain=DataProvider, range=Optional[Union[dict, "License"]])

slots.DataProvider_loginRequestMethod = Slot(uri=EVORAO.loginRequestMethod, name="DataProvider_loginRequestMethod", curie=EVORAO.curie('loginRequestMethod'),
                   model_uri=EVORAO.DataProvider_loginRequestMethod, domain=DataProvider, range=Optional[str])

slots.DataProvider_loginURL = Slot(uri=EVORAO.loginURL, name="DataProvider_loginURL", curie=EVORAO.curie('loginURL'),
                   model_uri=EVORAO.DataProvider_loginURL, domain=DataProvider, range=Optional[Union[str, URI]])

slots.DataProvider_loginTokenName = Slot(uri=EVORAO.loginTokenName, name="DataProvider_loginTokenName", curie=EVORAO.curie('loginTokenName'),
                   model_uri=EVORAO.DataProvider_loginTokenName, domain=DataProvider, range=Optional[str])

slots.DataProvider_queryMethod = Slot(uri=EVORAO.queryMethod, name="DataProvider_queryMethod", curie=EVORAO.curie('queryMethod'),
                   model_uri=EVORAO.DataProvider_queryMethod, domain=DataProvider, range=str)

slots.DataProvider_contentType = Slot(uri=EVORAO.contentType, name="DataProvider_contentType", curie=EVORAO.curie('contentType'),
                   model_uri=EVORAO.DataProvider_contentType, domain=DataProvider, range=str)

slots.DataProvider_providedEntityType = Slot(uri=EVORAO.providedEntityType, name="DataProvider_providedEntityType", curie=EVORAO.curie('providedEntityType'),
                   model_uri=EVORAO.DataProvider_providedEntityType, domain=DataProvider, range=Union[dict, Dataset])

slots.DataProvider_weight = Slot(uri=EVORAO.weight, name="DataProvider_weight", curie=EVORAO.curie('weight'),
                   model_uri=EVORAO.DataProvider_weight, domain=DataProvider, range=int)

slots.PathogenIdentification_taxon = Slot(uri=EVORAO.taxon, name="PathogenIdentification_taxon", curie=EVORAO.curie('taxon'),
                   model_uri=EVORAO.PathogenIdentification_taxon, domain=PathogenIdentification, range=Union[dict, "Taxon"])

slots.PathogenIdentification_pathogenName = Slot(uri=EVORAO.pathogenName, name="PathogenIdentification_pathogenName", curie=EVORAO.curie('pathogenName'),
                   model_uri=EVORAO.PathogenIdentification_pathogenName, domain=PathogenIdentification, range=Union[dict, "CommonName"])

slots.PathogenIdentification_pathogenType = Slot(uri=EVORAO.pathogenType, name="PathogenIdentification_pathogenType", curie=EVORAO.curie('pathogenType'),
                   model_uri=EVORAO.PathogenIdentification_pathogenType, domain=PathogenIdentification, range=str)

slots.PathogenIdentification_hostType = Slot(uri=EVORAO.hostType, name="PathogenIdentification_hostType", curie=EVORAO.curie('hostType'),
                   model_uri=EVORAO.PathogenIdentification_hostType, domain=PathogenIdentification, range=Optional[Union[str, list[str]]])

slots.PathogenIdentification_subspecies = Slot(uri=EVORAO.subspecies, name="PathogenIdentification_subspecies", curie=EVORAO.curie('subspecies'),
                   model_uri=EVORAO.PathogenIdentification_subspecies, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_strain = Slot(uri=EVORAO.strain, name="PathogenIdentification_strain", curie=EVORAO.curie('strain'),
                   model_uri=EVORAO.PathogenIdentification_strain, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_isolate = Slot(uri=EVORAO.isolate, name="PathogenIdentification_isolate", curie=EVORAO.curie('isolate'),
                   model_uri=EVORAO.PathogenIdentification_isolate, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_genotype = Slot(uri=EVORAO.genotype, name="PathogenIdentification_genotype", curie=EVORAO.curie('genotype'),
                   model_uri=EVORAO.PathogenIdentification_genotype, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_serotype = Slot(uri=EVORAO.serotype, name="PathogenIdentification_serotype", curie=EVORAO.curie('serotype'),
                   model_uri=EVORAO.PathogenIdentification_serotype, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_variant = Slot(uri=EVORAO.variant, name="PathogenIdentification_variant", curie=EVORAO.curie('variant'),
                   model_uri=EVORAO.PathogenIdentification_variant, domain=PathogenIdentification, range=Optional[Union[dict, "Variant"]])

slots.Publication_title = Slot(uri=DCT.title, name="Publication_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.Publication_title, domain=Publication, range=str)

slots.Publication_authors = Slot(uri=EVORAO.authors, name="Publication_authors", curie=EVORAO.curie('authors'),
                   model_uri=EVORAO.Publication_authors, domain=Publication, range=str)

slots.Publication_abstract = Slot(uri=EVORAO.abstract, name="Publication_abstract", curie=EVORAO.curie('abstract'),
                   model_uri=EVORAO.Publication_abstract, domain=Publication, range=str)

slots.Publication_relatedDOI = Slot(uri=EVORAO.relatedDOI, name="Publication_relatedDOI", curie=EVORAO.curie('relatedDOI'),
                   model_uri=EVORAO.Publication_relatedDOI, domain=Publication, range=Union[Union[dict, "DOI"], list[Union[dict, "DOI"]]])

slots.Publication_journal = Slot(uri=EVORAO.journal, name="Publication_journal", curie=EVORAO.curie('journal'),
                   model_uri=EVORAO.Publication_journal, domain=Publication, range=Optional[Union[dict, "Journal"]])

slots.Vocabulary_termDataProvider = Slot(uri=EVORAO.termDataProvider, name="Vocabulary_termDataProvider", curie=EVORAO.curie('termDataProvider'),
                   model_uri=EVORAO.Vocabulary_termDataProvider, domain=Vocabulary, range=Optional[Union[dict, DataProvider]])

slots.Vocabulary_term = Slot(uri=EVORAO.term, name="Vocabulary_term", curie=EVORAO.curie('term'),
                   model_uri=EVORAO.Vocabulary_term, domain=Vocabulary, range=Optional[Union[Union[dict, "Term"], list[Union[dict, "Term"]]]])

slots.Term_title = Slot(uri=DCT.title, name="Term_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.Term_title, domain=Term, range=str)

slots.Term_description = Slot(uri=DCT.description, name="Term_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.Term_description, domain=Term, range=Optional[str])

slots.Term_weight = Slot(uri=EVORAO.weight, name="Term_weight", curie=EVORAO.curie('weight'),
                   model_uri=EVORAO.Term_weight, domain=Term, range=int)

slots.Term_inVocabulary = Slot(uri=EVORAO.inVocabulary, name="Term_inVocabulary", curie=EVORAO.curie('inVocabulary'),
                   model_uri=EVORAO.Term_inVocabulary, domain=Term, range=Union[dict, Vocabulary])

slots.CommonName_alternateName = Slot(uri=EVORAO.alternateName, name="CommonName_alternateName", curie=EVORAO.curie('alternateName'),
                   model_uri=EVORAO.CommonName_alternateName, domain=CommonName, range=Optional[Union[Union[dict, "AlternateName"], list[Union[dict, "AlternateName"]]]])

slots.CommonName_sourceOfInformation = Slot(uri=EVORAO.sourceOfInformation, name="CommonName_sourceOfInformation", curie=EVORAO.curie('sourceOfInformation'),
                   model_uri=EVORAO.CommonName_sourceOfInformation, domain=CommonName, range=Optional[Union[str, list[str]]])

slots.AlternateName_alternateName = Slot(uri=EVORAO.alternateName, name="AlternateName_alternateName", curie=EVORAO.curie('alternateName'),
                   model_uri=EVORAO.AlternateName_alternateName, domain=AlternateName, range=Optional[Union[Union[dict, "AlternateName"], list[Union[dict, "AlternateName"]]]])

slots.AlternateName_sourceOfInformation = Slot(uri=EVORAO.sourceOfInformation, name="AlternateName_sourceOfInformation", curie=EVORAO.curie('sourceOfInformation'),
                   model_uri=EVORAO.AlternateName_sourceOfInformation, domain=AlternateName, range=Optional[Union[str, list[str]]])

slots.ProductCategory_parentCategory = Slot(uri=EVORAO.parentCategory, name="ProductCategory_parentCategory", curie=EVORAO.curie('parentCategory'),
                   model_uri=EVORAO.ProductCategory_parentCategory, domain=ProductCategory, range=Optional[Union[dict, "ProductCategory"]])

slots.Country_alpha2Code = Slot(uri=EVORAO.alpha2Code, name="Country_alpha2Code", curie=EVORAO.curie('alpha2Code'),
                   model_uri=EVORAO.Country_alpha2Code, domain=Country, range=str)

slots.TaxonomicRank_taxonomy = Slot(uri=EVORAO.taxonomy, name="TaxonomicRank_taxonomy", curie=EVORAO.curie('taxonomy'),
                   model_uri=EVORAO.TaxonomicRank_taxonomy, domain=TaxonomicRank, range=Optional[Union[Union[dict, Taxonomy], list[Union[dict, Taxonomy]]]])

slots.Taxon_taxonomy = Slot(uri=EVORAO.taxonomy, name="Taxon_taxonomy", curie=EVORAO.curie('taxonomy'),
                   model_uri=EVORAO.Taxon_taxonomy, domain=Taxon, range=Optional[Union[Union[dict, Taxonomy], list[Union[dict, Taxonomy]]]])

slots.Taxon_parentTaxon = Slot(uri=EVORAO.parentTaxon, name="Taxon_parentTaxon", curie=EVORAO.curie('parentTaxon'),
                   model_uri=EVORAO.Taxon_parentTaxon, domain=Taxon, range=Union[dict, "Taxon"])

slots.Taxon_rank = Slot(uri=EVORAO.rank, name="Taxon_rank", curie=EVORAO.curie('rank'),
                   model_uri=EVORAO.Taxon_rank, domain=Taxon, range=Union[dict, TaxonomicRank])

slots.Taxon_previouslyKnownAs = Slot(uri=EVORAO.previouslyKnownAs, name="Taxon_previouslyKnownAs", curie=EVORAO.curie('previouslyKnownAs'),
                   model_uri=EVORAO.Taxon_previouslyKnownAs, domain=Taxon, range=Optional[Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]]])

slots.Taxon_externalEquivalentTaxon = Slot(uri=EVORAO.externalEquivalentTaxon, name="Taxon_externalEquivalentTaxon", curie=EVORAO.curie('externalEquivalentTaxon'),
                   model_uri=EVORAO.Taxon_externalEquivalentTaxon, domain=Taxon, range=Optional[Union[Union[dict, "Taxon"], list[Union[dict, "Taxon"]]]])

slots.Taxon_taxonomicID = Slot(uri=EVORAO.taxonomicID, name="Taxon_taxonomicID", curie=EVORAO.curie('taxonomicID'),
                   model_uri=EVORAO.Taxon_taxonomicID, domain=Taxon, range=str)

slots.Taxon_taxonomicNodeID = Slot(uri=EVORAO.taxonomicNodeID, name="Taxon_taxonomicNodeID", curie=EVORAO.curie('taxonomicNodeID'),
                   model_uri=EVORAO.Taxon_taxonomicNodeID, domain=Taxon, range=Optional[str])

slots.ExternalRelatedReference_reference = Slot(uri=EVORAO.reference, name="ExternalRelatedReference_reference", curie=EVORAO.curie('reference'),
                   model_uri=EVORAO.ExternalRelatedReference_reference, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceLabel = Slot(uri=EVORAO.referenceLabel, name="ExternalRelatedReference_referenceLabel", curie=EVORAO.curie('referenceLabel'),
                   model_uri=EVORAO.ExternalRelatedReference_referenceLabel, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceProviderPrefix = Slot(uri=EVORAO.referenceProviderPrefix, name="ExternalRelatedReference_referenceProviderPrefix", curie=EVORAO.curie('referenceProviderPrefix'),
                   model_uri=EVORAO.ExternalRelatedReference_referenceProviderPrefix, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceProviderName = Slot(uri=EVORAO.referenceProviderName, name="ExternalRelatedReference_referenceProviderName", curie=EVORAO.curie('referenceProviderName'),
                   model_uri=EVORAO.ExternalRelatedReference_referenceProviderName, domain=ExternalRelatedReference, range=str)

slots.Sequence_sequenceReference = Slot(uri=EVORAO.sequenceReference, name="Sequence_sequenceReference", curie=EVORAO.curie('sequenceReference'),
                   model_uri=EVORAO.Sequence_sequenceReference, domain=Sequence, range=Optional[Union[Union[dict, "SequenceReference"], list[Union[dict, "SequenceReference"]]]])

slots.Sequence_sequenceFASTA = Slot(uri=EVORAO.sequenceFASTA, name="Sequence_sequenceFASTA", curie=EVORAO.curie('sequenceFASTA'),
                   model_uri=EVORAO.Sequence_sequenceFASTA, domain=Sequence, range=Optional[str])

slots.SequenceReference_accessionNumber = Slot(uri=EVORAO.accessionNumber, name="SequenceReference_accessionNumber", curie=EVORAO.curie('accessionNumber'),
                   model_uri=EVORAO.SequenceReference_accessionNumber, domain=SequenceReference, range=str)

slots.SequenceReference_sequenceProvider = Slot(uri=EVORAO.sequenceProvider, name="SequenceReference_sequenceProvider", curie=EVORAO.curie('sequenceProvider'),
                   model_uri=EVORAO.SequenceReference_sequenceProvider, domain=SequenceReference, range=str)

slots.PersonOrOrganization_name = Slot(uri=EVORAO.name, name="PersonOrOrganization_name", curie=EVORAO.curie('name'),
                   model_uri=EVORAO.PersonOrOrganization_name, domain=PersonOrOrganization, range=str)

slots.PersonOrOrganization_description = Slot(uri=DCT.description, name="PersonOrOrganization_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.PersonOrOrganization_description, domain=PersonOrOrganization, range=Optional[str])

slots.PersonOrOrganization_homePage = Slot(uri=EVORAO.homePage, name="PersonOrOrganization_homePage", curie=EVORAO.curie('homePage'),
                   model_uri=EVORAO.PersonOrOrganization_homePage, domain=PersonOrOrganization, range=Optional[Union[str, URI]])

slots.PersonOrOrganization_contactPoint = Slot(uri=EVORAO.contactPoint, name="PersonOrOrganization_contactPoint", curie=EVORAO.curie('contactPoint'),
                   model_uri=EVORAO.PersonOrOrganization_contactPoint, domain=PersonOrOrganization, range=Optional[Union[dict, "ContactPoint"]])

slots.PersonOrOrganization_logo = Slot(uri=EVORAO.logo, name="PersonOrOrganization_logo", curie=EVORAO.curie('logo'),
                   model_uri=EVORAO.PersonOrOrganization_logo, domain=PersonOrOrganization, range=Optional[Union[dict, "Image"]])

slots.Person_oRCIDiD = Slot(uri=EVORAO.oRCIDiD, name="Person_oRCIDiD", curie=EVORAO.curie('oRCIDiD'),
                   model_uri=EVORAO.Person_oRCIDiD, domain=Person, range=Optional[str])

slots.Organization_alternateName = Slot(uri=EVORAO.alternateName, name="Organization_alternateName", curie=EVORAO.curie('alternateName'),
                   model_uri=EVORAO.Organization_alternateName, domain=Organization, range=Optional[Union[Union[dict, AlternateName], list[Union[dict, AlternateName]]]])

slots.Organization_country = Slot(uri=EVORAO.country, name="Organization_country", curie=EVORAO.curie('country'),
                   model_uri=EVORAO.Organization_country, domain=Organization, range=Optional[Union[dict, Country]])

slots.Organization_rORiD = Slot(uri=EVORAO.rORiD, name="Organization_rORiD", curie=EVORAO.curie('rORiD'),
                   model_uri=EVORAO.Organization_rORiD, domain=Organization, range=Optional[str])

slots.Provider_memberOfRI = Slot(uri=EVORAO.memberOfRI, name="Provider_memberOfRI", curie=EVORAO.curie('memberOfRI'),
                   model_uri=EVORAO.Provider_memberOfRI, domain=Provider, range=Optional[Union[Union[dict, RI], list[Union[dict, RI]]]])

slots.BiologicalMaterialOrigin_recombinantMaterial = Slot(uri=EVORAO.recombinantMaterial, name="BiologicalMaterialOrigin_recombinantMaterial", curie=EVORAO.curie('recombinantMaterial'),
                   model_uri=EVORAO.BiologicalMaterialOrigin_recombinantMaterial, domain=BiologicalMaterialOrigin, range=Union[bool, Bool])

slots.BiologicalMaterialOrigin_biologicalSourceType = Slot(uri=EVORAO.biologicalSourceType, name="BiologicalMaterialOrigin_biologicalSourceType", curie=EVORAO.curie('biologicalSourceType'),
                   model_uri=EVORAO.BiologicalMaterialOrigin_biologicalSourceType, domain=BiologicalMaterialOrigin, range=Union[bool, Bool])

slots.BiologicalMaterialOrigin_biologicalPartOrigin = Slot(uri=EVORAO.biologicalPartOrigin, name="BiologicalMaterialOrigin_biologicalPartOrigin", curie=EVORAO.curie('biologicalPartOrigin'),
                   model_uri=EVORAO.BiologicalMaterialOrigin_biologicalPartOrigin, domain=BiologicalMaterialOrigin, range=Union[Union[dict, "BiologicalPartOrigin"], list[Union[dict, "BiologicalPartOrigin"]]])

slots.BiologicalPartOrigin_recombinantPartIdentification = Slot(uri=EVORAO.recombinantPartIdentification, name="BiologicalPartOrigin_recombinantPartIdentification", curie=EVORAO.curie('recombinantPartIdentification'),
                   model_uri=EVORAO.BiologicalPartOrigin_recombinantPartIdentification, domain=BiologicalPartOrigin, range=Optional[Union[dict, "RecombinantPartIdentification"]])

slots.BiologicalPartOrigin_accessToPhysicalGeneticResource = Slot(uri=EVORAO.accessToPhysicalGeneticResource, name="BiologicalPartOrigin_accessToPhysicalGeneticResource", curie=EVORAO.curie('accessToPhysicalGeneticResource'),
                   model_uri=EVORAO.BiologicalPartOrigin_accessToPhysicalGeneticResource, domain=BiologicalPartOrigin, range=Union[bool, Bool])

slots.NaturalPartOrigin_countryOfCollection = Slot(uri=EVORAO.countryOfCollection, name="NaturalPartOrigin_countryOfCollection", curie=EVORAO.curie('countryOfCollection'),
                   model_uri=EVORAO.NaturalPartOrigin_countryOfCollection, domain=NaturalPartOrigin, range=Union[dict, Country])

slots.NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin = Slot(uri=EVORAO.indigenousPoepleAndLocalCommunityOrigin, name="NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin", curie=EVORAO.curie('indigenousPoepleAndLocalCommunityOrigin'),
                   model_uri=EVORAO.NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin, domain=NaturalPartOrigin, range=Optional[Union[dict, IPLCOrigin]])

slots.NaturalPartOrigin_collectionDate = Slot(uri=EVORAO.collectionDate, name="NaturalPartOrigin_collectionDate", curie=EVORAO.curie('collectionDate'),
                   model_uri=EVORAO.NaturalPartOrigin_collectionDate, domain=NaturalPartOrigin, range=Union[str, XSDDateTime])

slots.NaturalPartOrigin_beforeDate = Slot(uri=EVORAO.beforeDate, name="NaturalPartOrigin_beforeDate", curie=EVORAO.curie('beforeDate'),
                   model_uri=EVORAO.NaturalPartOrigin_beforeDate, domain=NaturalPartOrigin, range=Union[bool, Bool])

slots.NaturalPartOrigin_permitIdentifierForABS = Slot(uri=EVORAO.permitIdentifierForABS, name="NaturalPartOrigin_permitIdentifierForABS", curie=EVORAO.curie('permitIdentifierForABS'),
                   model_uri=EVORAO.NaturalPartOrigin_permitIdentifierForABS, domain=NaturalPartOrigin, range=Optional[str])

slots.SyntheticPartOrigin_modificationsFromTheReferenceSequences = Slot(uri=EVORAO.modificationsFromTheReferenceSequences, name="SyntheticPartOrigin_modificationsFromTheReferenceSequences", curie=EVORAO.curie('modificationsFromTheReferenceSequences'),
                   model_uri=EVORAO.SyntheticPartOrigin_modificationsFromTheReferenceSequences, domain=SyntheticPartOrigin, range=Union[bool, Bool])

slots.SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences = Slot(uri=EVORAO.descriptionOfModificationsMadeFromTheReferenceSequences, name="SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences", curie=EVORAO.curie('descriptionOfModificationsMadeFromTheReferenceSequences'),
                   model_uri=EVORAO.SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences, domain=SyntheticPartOrigin, range=Optional[str])

slots.RecombinantPartIdentification_partIdentification = Slot(uri=EVORAO.partIdentification, name="RecombinantPartIdentification_partIdentification", curie=EVORAO.curie('partIdentification'),
                   model_uri=EVORAO.RecombinantPartIdentification_partIdentification, domain=RecombinantPartIdentification, range=str)

slots.RecombinantPartIdentification_sequence = Slot(uri=EVORAO.sequence, name="RecombinantPartIdentification_sequence", curie=EVORAO.curie('sequence'),
                   model_uri=EVORAO.RecombinantPartIdentification_sequence, domain=RecombinantPartIdentification, range=Union[Union[dict, Sequence], list[Union[dict, Sequence]]])

slots.Collection_collectionItem = Slot(uri=EVORAO.collectionItem, name="Collection_collectionItem", curie=EVORAO.curie('collectionItem'),
                   model_uri=EVORAO.Collection_collectionItem, domain=Collection, range=Optional[Union[Union[dict, "ProductOrService"], list[Union[dict, "ProductOrService"]]]])

slots.Collection_collectionDataProvider = Slot(uri=EVORAO.collectionDataProvider, name="Collection_collectionDataProvider", curie=EVORAO.curie('collectionDataProvider'),
                   model_uri=EVORAO.Collection_collectionDataProvider, domain=Collection, range=Optional[Union[dict, DataProvider]])

slots.ProductOrService_accessPointURL = Slot(uri=EVORAO.accessPointURL, name="ProductOrService_accessPointURL", curie=EVORAO.curie('accessPointURL'),
                   model_uri=EVORAO.ProductOrService_accessPointURL, domain=ProductOrService, range=Union[str, URI])

slots.ProductOrService_refSKU = Slot(uri=EVORAO.refSKU, name="ProductOrService_refSKU", curie=EVORAO.curie('refSKU'),
                   model_uri=EVORAO.ProductOrService_refSKU, domain=ProductOrService, range=str)

slots.ProductOrService_unitDefinition = Slot(uri=EVORAO.unitDefinition, name="ProductOrService_unitDefinition", curie=EVORAO.curie('unitDefinition'),
                   model_uri=EVORAO.ProductOrService_unitDefinition, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_category = Slot(uri=EVORAO.category, name="ProductOrService_category", curie=EVORAO.curie('category'),
                   model_uri=EVORAO.ProductOrService_category, domain=ProductOrService, range=Union[dict, ProductCategory])

slots.ProductOrService_additionalCategory = Slot(uri=EVORAO.additionalCategory, name="ProductOrService_additionalCategory", curie=EVORAO.curie('additionalCategory'),
                   model_uri=EVORAO.ProductOrService_additionalCategory, domain=ProductOrService, range=Optional[Union[Union[dict, ProductCategory], list[Union[dict, ProductCategory]]]])

slots.ProductOrService_unitCost = Slot(uri=EVORAO.unitCost, name="ProductOrService_unitCost", curie=EVORAO.curie('unitCost'),
                   model_uri=EVORAO.ProductOrService_unitCost, domain=ProductOrService, range=str)

slots.ProductOrService_qualityGrading = Slot(uri=EVORAO.qualityGrading, name="ProductOrService_qualityGrading", curie=EVORAO.curie('qualityGrading'),
                   model_uri=EVORAO.ProductOrService_qualityGrading, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_pathogenIdentification = Slot(uri=EVORAO.pathogenIdentification, name="ProductOrService_pathogenIdentification", curie=EVORAO.curie('pathogenIdentification'),
                   model_uri=EVORAO.ProductOrService_pathogenIdentification, domain=ProductOrService, range=Union[Union[dict, PathogenIdentification], list[Union[dict, PathogenIdentification]]])

slots.ProductOrService_relatedDOI = Slot(uri=EVORAO.relatedDOI, name="ProductOrService_relatedDOI", curie=EVORAO.curie('relatedDOI'),
                   model_uri=EVORAO.ProductOrService_relatedDOI, domain=ProductOrService, range=Optional[Union[Union[dict, DOI], list[Union[dict, DOI]]]])

slots.ProductOrService_riskGroup = Slot(uri=EVORAO.riskGroup, name="ProductOrService_riskGroup", curie=EVORAO.curie('riskGroup'),
                   model_uri=EVORAO.ProductOrService_riskGroup, domain=ProductOrService, range=Optional[Union[dict, RiskGroup]])

slots.ProductOrService_biosafetyRestrictions = Slot(uri=EVORAO.biosafetyRestrictions, name="ProductOrService_biosafetyRestrictions", curie=EVORAO.curie('biosafetyRestrictions'),
                   model_uri=EVORAO.ProductOrService_biosafetyRestrictions, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_canItBeUsedToProduceGMO = Slot(uri=EVORAO.canItBeUsedToProduceGMO, name="ProductOrService_canItBeUsedToProduceGMO", curie=EVORAO.curie('canItBeUsedToProduceGMO'),
                   model_uri=EVORAO.ProductOrService_canItBeUsedToProduceGMO, domain=ProductOrService, range=Union[bool, Bool])

slots.ProductOrService_provider = Slot(uri=EVORAO.provider, name="ProductOrService_provider", curie=EVORAO.curie('provider'),
                   model_uri=EVORAO.ProductOrService_provider, domain=ProductOrService, range=Union[dict, Provider])

slots.ProductOrService_collection = Slot(uri=EVORAO.collection, name="ProductOrService_collection", curie=EVORAO.curie('collection'),
                   model_uri=EVORAO.ProductOrService_collection, domain=ProductOrService, range=Union[Union[dict, Collection], list[Union[dict, Collection]]])

slots.ProductOrService_keywords = Slot(uri=EVORAO.keywords, name="ProductOrService_keywords", curie=EVORAO.curie('keywords'),
                   model_uri=EVORAO.ProductOrService_keywords, domain=ProductOrService, range=Union[Union[dict, Keyword], list[Union[dict, Keyword]]])

slots.ProductOrService_availability = Slot(uri=EVORAO.availability, name="ProductOrService_availability", curie=EVORAO.curie('availability'),
                   model_uri=EVORAO.ProductOrService_availability, domain=ProductOrService, range=str)

slots.ProductOrService_complementaryDocument = Slot(uri=EVORAO.complementaryDocument, name="ProductOrService_complementaryDocument", curie=EVORAO.curie('complementaryDocument'),
                   model_uri=EVORAO.ProductOrService_complementaryDocument, domain=ProductOrService, range=Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]])

slots.ProductOrService_technicalRecommendation = Slot(uri=EVORAO.technicalRecommendation, name="ProductOrService_technicalRecommendation", curie=EVORAO.curie('technicalRecommendation'),
                   model_uri=EVORAO.ProductOrService_technicalRecommendation, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_productPicture = Slot(uri=EVORAO.productPicture, name="ProductOrService_productPicture", curie=EVORAO.curie('productPicture'),
                   model_uri=EVORAO.ProductOrService_productPicture, domain=ProductOrService, range=Optional[Union[Union[dict, "Image"], list[Union[dict, "Image"]]]])

slots.ProductOrService_externalRelatedReference = Slot(uri=EVORAO.externalRelatedReference, name="ProductOrService_externalRelatedReference", curie=EVORAO.curie('externalRelatedReference'),
                   model_uri=EVORAO.ProductOrService_externalRelatedReference, domain=ProductOrService, range=Optional[Union[Union[dict, ExternalRelatedReference], list[Union[dict, ExternalRelatedReference]]]])

slots.ProductOrService_certification = Slot(uri=EVORAO.certification, name="ProductOrService_certification", curie=EVORAO.curie('certification'),
                   model_uri=EVORAO.ProductOrService_certification, domain=ProductOrService, range=Optional[Union[Union[dict, "Certification"], list[Union[dict, "Certification"]]]])

slots.ProductOrService_internalReference = Slot(uri=EVORAO.internalReference, name="ProductOrService_internalReference", curie=EVORAO.curie('internalReference'),
                   model_uri=EVORAO.ProductOrService_internalReference, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_note = Slot(uri=EVORAO.note, name="ProductOrService_note", curie=EVORAO.curie('note'),
                   model_uri=EVORAO.ProductOrService_note, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_contactPoint = Slot(uri=EVORAO.contactPoint, name="ProductOrService_contactPoint", curie=EVORAO.curie('contactPoint'),
                   model_uri=EVORAO.ProductOrService_contactPoint, domain=ProductOrService, range=Optional[Union[dict, "ContactPoint"]])

slots.Service_modelSpecies = Slot(uri=EVORAO.modelSpecies, name="Service_modelSpecies", curie=EVORAO.curie('modelSpecies'),
                   model_uri=EVORAO.Service_modelSpecies, domain=Service, range=Optional[str])

slots.Service_modelType = Slot(uri=EVORAO.modelType, name="Service_modelType", curie=EVORAO.curie('modelType'),
                   model_uri=EVORAO.Service_modelType, domain=Service, range=Optional[str])

slots.Product_hasIATAClassification = Slot(uri=EVORAO.hasIATAClassification, name="Product_hasIATAClassification", curie=EVORAO.curie('hasIATAClassification'),
                   model_uri=EVORAO.Product_hasIATAClassification, domain=Product, range=Union[dict, IATAClassification])

slots.Product_shippingConditions = Slot(uri=EVORAO.shippingConditions, name="Product_shippingConditions", curie=EVORAO.curie('shippingConditions'),
                   model_uri=EVORAO.Product_shippingConditions, domain=Product, range=str)

slots.Product_materialSafetyDataSheet = Slot(uri=EVORAO.materialSafetyDataSheet, name="Product_materialSafetyDataSheet", curie=EVORAO.curie('materialSafetyDataSheet'),
                   model_uri=EVORAO.Product_materialSafetyDataSheet, domain=Product, range=Optional[Union[dict, "MSDS"]])

slots.Product_originator = Slot(uri=EVORAO.originator, name="Product_originator", curie=EVORAO.curie('originator'),
                   model_uri=EVORAO.Product_originator, domain=Product, range=Optional[Union[dict, Originator]])

slots.Product_storageConditions = Slot(uri=EVORAO.storageConditions, name="Product_storageConditions", curie=EVORAO.curie('storageConditions'),
                   model_uri=EVORAO.Product_storageConditions, domain=Product, range=str)

slots.Product_thirdPartyDistributionConsent = Slot(uri=EVORAO.thirdPartyDistributionConsent, name="Product_thirdPartyDistributionConsent", curie=EVORAO.curie('thirdPartyDistributionConsent'),
                   model_uri=EVORAO.Product_thirdPartyDistributionConsent, domain=Product, range=Optional[Union[bool, Bool]])

slots.Product_usageRestrictions = Slot(uri=EVORAO.usageRestrictions, name="Product_usageRestrictions", curie=EVORAO.curie('usageRestrictions'),
                   model_uri=EVORAO.Product_usageRestrictions, domain=Product, range=Optional[str])

slots.Antibody_productionSystem = Slot(uri=EVORAO.productionSystem, name="Antibody_productionSystem", curie=EVORAO.curie('productionSystem'),
                   model_uri=EVORAO.Antibody_productionSystem, domain=Antibody, range=Optional[str])

slots.Antibody_antibodyPurifiedByAffinity = Slot(uri=EVORAO.antibodyPurifiedByAffinity, name="Antibody_antibodyPurifiedByAffinity", curie=EVORAO.curie('antibodyPurifiedByAffinity'),
                   model_uri=EVORAO.Antibody_antibodyPurifiedByAffinity, domain=Antibody, range=Union[bool, Bool])

slots.Antibody_specificityDocumented = Slot(uri=EVORAO.specificityDocumented, name="Antibody_specificityDocumented", curie=EVORAO.curie('specificityDocumented'),
                   model_uri=EVORAO.Antibody_specificityDocumented, domain=Antibody, range=Union[bool, Bool])

slots.Antibody_targetedAntigen = Slot(uri=EVORAO.targetedAntigen, name="Antibody_targetedAntigen", curie=EVORAO.curie('targetedAntigen'),
                   model_uri=EVORAO.Antibody_targetedAntigen, domain=Antibody, range=str)

slots.Antibody_sequenceReference = Slot(uri=EVORAO.sequenceReference, name="Antibody_sequenceReference", curie=EVORAO.curie('sequenceReference'),
                   model_uri=EVORAO.Antibody_sequenceReference, domain=Antibody, range=Optional[Union[Union[dict, SequenceReference], list[Union[dict, SequenceReference]]]])

slots.Hybridoma_hybridomaDescription = Slot(uri=EVORAO.hybridomaDescription, name="Hybridoma_hybridomaDescription", curie=EVORAO.curie('hybridomaDescription'),
                   model_uri=EVORAO.Hybridoma_hybridomaDescription, domain=Hybridoma, range=str)

slots.Protein_biologicalMaterialOrigin = Slot(uri=EVORAO.biologicalMaterialOrigin, name="Protein_biologicalMaterialOrigin", curie=EVORAO.curie('biologicalMaterialOrigin'),
                   model_uri=EVORAO.Protein_biologicalMaterialOrigin, domain=Protein, range=Union[dict, BiologicalMaterialOrigin])

slots.Protein_sequence = Slot(uri=EVORAO.sequence, name="Protein_sequence", curie=EVORAO.curie('sequence'),
                   model_uri=EVORAO.Protein_sequence, domain=Protein, range=Union[Union[dict, Sequence], list[Union[dict, Sequence]]])

slots.Protein_relatedPDB = Slot(uri=EVORAO.relatedPDB, name="Protein_relatedPDB", curie=EVORAO.curie('relatedPDB'),
                   model_uri=EVORAO.Protein_relatedPDB, domain=Protein, range=Optional[Union[Union[dict, PDBReference], list[Union[dict, PDBReference]]]])

slots.Protein_specialFeature = Slot(uri=EVORAO.specialFeature, name="Protein_specialFeature", curie=EVORAO.curie('specialFeature'),
                   model_uri=EVORAO.Protein_specialFeature, domain=Protein, range=Optional[Union[Union[dict, SpecialFeature], list[Union[dict, SpecialFeature]]]])

slots.Protein_proteinTAG = Slot(uri=EVORAO.proteinTAG, name="Protein_proteinTAG", curie=EVORAO.curie('proteinTAG'),
                   model_uri=EVORAO.Protein_proteinTAG, domain=Protein, range=Optional[Union[Union[dict, ProteinTag], list[Union[dict, ProteinTag]]]])

slots.Protein_domain = Slot(uri=EVORAO.domain, name="Protein_domain", curie=EVORAO.curie('domain'),
                   model_uri=EVORAO.Protein_domain, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_expressedAs = Slot(uri=EVORAO.expressedAs, name="Protein_expressedAs", curie=EVORAO.curie('expressedAs'),
                   model_uri=EVORAO.Protein_expressedAs, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_inclusionBodiesType = Slot(uri=EVORAO.inclusionBodiesType, name="Protein_inclusionBodiesType", curie=EVORAO.curie('inclusionBodiesType'),
                   model_uri=EVORAO.Protein_inclusionBodiesType, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_expressionSystem = Slot(uri=EVORAO.expressionSystem, name="Protein_expressionSystem", curie=EVORAO.curie('expressionSystem'),
                   model_uri=EVORAO.Protein_expressionSystem, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_functionalCharacterization = Slot(uri=EVORAO.functionalCharacterization, name="Protein_functionalCharacterization", curie=EVORAO.curie('functionalCharacterization'),
                   model_uri=EVORAO.Protein_functionalCharacterization, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_functionalTechnicalDescription = Slot(uri=EVORAO.functionalTechnicalDescription, name="Protein_functionalTechnicalDescription", curie=EVORAO.curie('functionalTechnicalDescription'),
                   model_uri=EVORAO.Protein_functionalTechnicalDescription, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_proteinPurification = Slot(uri=EVORAO.proteinPurification, name="Protein_proteinPurification", curie=EVORAO.curie('proteinPurification'),
                   model_uri=EVORAO.Protein_proteinPurification, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_theTAGStatusOfTheSolubilizedProtein = Slot(uri=EVORAO.theTAGStatusOfTheSolubilizedProtein, name="Protein_theTAGStatusOfTheSolubilizedProtein", curie=EVORAO.curie('theTAGStatusOfTheSolubilizedProtein'),
                   model_uri=EVORAO.Protein_theTAGStatusOfTheSolubilizedProtein, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Protein_typeOfFunctionalCharacterization = Slot(uri=EVORAO.typeOfFunctionalCharacterization, name="Protein_typeOfFunctionalCharacterization", curie=EVORAO.curie('typeOfFunctionalCharacterization'),
                   model_uri=EVORAO.Protein_typeOfFunctionalCharacterization, domain=Protein, range=Optional[Union[str, list[str]]])

slots.Nucleic_Acid_biologicalMaterialOrigin = Slot(uri=EVORAO.biologicalMaterialOrigin, name="Nucleic Acid_biologicalMaterialOrigin", curie=EVORAO.curie('biologicalMaterialOrigin'),
                   model_uri=EVORAO.Nucleic_Acid_biologicalMaterialOrigin, domain=NucleicAcid, range=Union[dict, BiologicalMaterialOrigin])

slots.Nucleic_Acid_hasGbFileOfTheConstruct = Slot(uri=EVORAO.hasGbFileOfTheConstruct, name="Nucleic Acid_hasGbFileOfTheConstruct", curie=EVORAO.curie('hasGbFileOfTheConstruct'),
                   model_uri=EVORAO.Nucleic_Acid_hasGbFileOfTheConstruct, domain=NucleicAcid, range=Optional[Union[Union[dict, "Data"], list[Union[dict, "Data"]]]])

slots.Nucleic_Acid_sequence = Slot(uri=EVORAO.sequence, name="Nucleic Acid_sequence", curie=EVORAO.curie('sequence'),
                   model_uri=EVORAO.Nucleic_Acid_sequence, domain=NucleicAcid, range=Union[Union[dict, Sequence], list[Union[dict, Sequence]]])

slots.Nucleic_Acid_isItAClonedNucleicAcid = Slot(uri=EVORAO.isItAClonedNucleicAcid, name="Nucleic Acid_isItAClonedNucleicAcid", curie=EVORAO.curie('isItAClonedNucleicAcid'),
                   model_uri=EVORAO.Nucleic_Acid_isItAClonedNucleicAcid, domain=NucleicAcid, range=Union[bool, Bool])

slots.Nucleic_Acid_clonedIntoPlasmid = Slot(uri=EVORAO.clonedIntoPlasmid, name="Nucleic Acid_clonedIntoPlasmid", curie=EVORAO.curie('clonedIntoPlasmid'),
                   model_uri=EVORAO.Nucleic_Acid_clonedIntoPlasmid, domain=NucleicAcid, range=Optional[Union[dict, ExpressionVector]])

slots.Nucleic_Acid_pasmidSelection = Slot(uri=EVORAO.pasmidSelection, name="Nucleic Acid_pasmidSelection", curie=EVORAO.curie('pasmidSelection'),
                   model_uri=EVORAO.Nucleic_Acid_pasmidSelection, domain=NucleicAcid, range=Optional[Union[Union[dict, PlasmidSelection], list[Union[dict, PlasmidSelection]]]])

slots.Nucleic_Acid_hasTAG = Slot(uri=EVORAO.hasTAG, name="Nucleic Acid_hasTAG", curie=EVORAO.curie('hasTAG'),
                   model_uri=EVORAO.Nucleic_Acid_hasTAG, domain=NucleicAcid, range=Union[dict, ProteinTag])

slots.Nucleic_Acid_regionEncompassedInThisProduct = Slot(uri=EVORAO.regionEncompassedInThisProduct, name="Nucleic Acid_regionEncompassedInThisProduct", curie=EVORAO.curie('regionEncompassedInThisProduct'),
                   model_uri=EVORAO.Nucleic_Acid_regionEncompassedInThisProduct, domain=NucleicAcid, range=str)

slots.Nucleic_Acid_mutationObserved = Slot(uri=EVORAO.mutationObserved, name="Nucleic Acid_mutationObserved", curie=EVORAO.curie('mutationObserved'),
                   model_uri=EVORAO.Nucleic_Acid_mutationObserved, domain=NucleicAcid, range=Union[bool, Bool])

slots.Nucleic_Acid_observedMutations = Slot(uri=EVORAO.observedMutations, name="Nucleic Acid_observedMutations", curie=EVORAO.curie('observedMutations'),
                   model_uri=EVORAO.Nucleic_Acid_observedMutations, domain=NucleicAcid, range=Optional[str])

slots.Nucleic_Acid_identificationTechnique = Slot(uri=EVORAO.identificationTechnique, name="Nucleic Acid_identificationTechnique", curie=EVORAO.curie('identificationTechnique'),
                   model_uri=EVORAO.Nucleic_Acid_identificationTechnique, domain=NucleicAcid, range=Optional[str])

slots.Nucleic_Acid_sequencing = Slot(uri=EVORAO.sequencing, name="Nucleic Acid_sequencing", curie=EVORAO.curie('sequencing'),
                   model_uri=EVORAO.Nucleic_Acid_sequencing, domain=NucleicAcid, range=str)

slots.Nucleic_Acid_titer = Slot(uri=EVORAO.titer, name="Nucleic Acid_titer", curie=EVORAO.curie('titer'),
                   model_uri=EVORAO.Nucleic_Acid_titer, domain=NucleicAcid, range=str)

slots.Nucleic_Acid_sequenceChecked = Slot(uri=EVORAO.sequenceChecked, name="Nucleic Acid_sequenceChecked", curie=EVORAO.curie('sequenceChecked'),
                   model_uri=EVORAO.Nucleic_Acid_sequenceChecked, domain=NucleicAcid, range=Union[bool, Bool])

slots.Detection_Kit_hasSOPFile = Slot(uri=EVORAO.hasSOPFile, name="Detection Kit_hasSOPFile", curie=EVORAO.curie('hasSOPFile'),
                   model_uri=EVORAO.Detection_Kit_hasSOPFile, domain=DetectionKit, range=Optional[Union[Union[dict, "File"], list[Union[dict, "File"]]]])

slots.Detection_Kit_specificityDocumented = Slot(uri=EVORAO.specificityDocumented, name="Detection Kit_specificityDocumented", curie=EVORAO.curie('specificityDocumented'),
                   model_uri=EVORAO.Detection_Kit_specificityDocumented, domain=DetectionKit, range=Union[bool, Bool])

slots.Detection_Kit_specificity = Slot(uri=EVORAO.specificity, name="Detection Kit_specificity", curie=EVORAO.curie('specificity'),
                   model_uri=EVORAO.Detection_Kit_specificity, domain=DetectionKit, range=Optional[str])

slots.Detection_Kit_targetedRegion = Slot(uri=EVORAO.targetedRegion, name="Detection Kit_targetedRegion", curie=EVORAO.curie('targetedRegion'),
                   model_uri=EVORAO.Detection_Kit_targetedRegion, domain=DetectionKit, range=Optional[str])

slots.Bundle_productsOfTheBundle = Slot(uri=EVORAO.productsOfTheBundle, name="Bundle_productsOfTheBundle", curie=EVORAO.curie('productsOfTheBundle'),
                   model_uri=EVORAO.Bundle_productsOfTheBundle, domain=Bundle, range=Union[Union[dict, Product], list[Union[dict, Product]]])

slots.Pathogen_biologicalMaterialOrigin = Slot(uri=EVORAO.biologicalMaterialOrigin, name="Pathogen_biologicalMaterialOrigin", curie=EVORAO.curie('biologicalMaterialOrigin'),
                   model_uri=EVORAO.Pathogen_biologicalMaterialOrigin, domain=Pathogen, range=Union[dict, BiologicalMaterialOrigin])

slots.Pathogen_suspectedEpidemiologicalOrigin = Slot(uri=EVORAO.suspectedEpidemiologicalOrigin, name="Pathogen_suspectedEpidemiologicalOrigin", curie=EVORAO.curie('suspectedEpidemiologicalOrigin'),
                   model_uri=EVORAO.Pathogen_suspectedEpidemiologicalOrigin, domain=Pathogen, range=Optional[Union[Union[dict, GeographicalOrigin], list[Union[dict, GeographicalOrigin]]]])

slots.Pathogen_isolationHost = Slot(uri=EVORAO.isolationHost, name="Pathogen_isolationHost", curie=EVORAO.curie('isolationHost'),
                   model_uri=EVORAO.Pathogen_isolationHost, domain=Pathogen, range=Optional[Union[Union[dict, IsolationHost], list[Union[dict, IsolationHost]]]])

slots.Pathogen_productionCellLine = Slot(uri=EVORAO.productionCellLine, name="Pathogen_productionCellLine", curie=EVORAO.curie('productionCellLine'),
                   model_uri=EVORAO.Pathogen_productionCellLine, domain=Pathogen, range=Optional[Union[Union[dict, ProductionCellLine], list[Union[dict, ProductionCellLine]]]])

slots.Pathogen_propagationHost = Slot(uri=EVORAO.propagationHost, name="Pathogen_propagationHost", curie=EVORAO.curie('propagationHost'),
                   model_uri=EVORAO.Pathogen_propagationHost, domain=Pathogen, range=Optional[Union[Union[dict, PropagationHost], list[Union[dict, PropagationHost]]]])

slots.Pathogen_transmissionMethod = Slot(uri=EVORAO.transmissionMethod, name="Pathogen_transmissionMethod", curie=EVORAO.curie('transmissionMethod'),
                   model_uri=EVORAO.Pathogen_transmissionMethod, domain=Pathogen, range=Optional[Union[Union[dict, TransmissionMethod], list[Union[dict, TransmissionMethod]]]])

slots.Pathogen_sequence = Slot(uri=EVORAO.sequence, name="Pathogen_sequence", curie=EVORAO.curie('sequence'),
                   model_uri=EVORAO.Pathogen_sequence, domain=Pathogen, range=Union[Union[dict, Sequence], list[Union[dict, Sequence]]])

slots.Pathogen_cultivability = Slot(uri=EVORAO.cultivability, name="Pathogen_cultivability", curie=EVORAO.curie('cultivability'),
                   model_uri=EVORAO.Pathogen_cultivability, domain=Pathogen, range=str)

slots.Pathogen_clinicalInformation = Slot(uri=EVORAO.clinicalInformation, name="Pathogen_clinicalInformation", curie=EVORAO.curie('clinicalInformation'),
                   model_uri=EVORAO.Pathogen_clinicalInformation, domain=Pathogen, range=Optional[str])

slots.Pathogen_identificationTechnique = Slot(uri=EVORAO.identificationTechnique, name="Pathogen_identificationTechnique", curie=EVORAO.curie('identificationTechnique'),
                   model_uri=EVORAO.Pathogen_identificationTechnique, domain=Pathogen, range=Optional[str])

slots.Pathogen_infectivity = Slot(uri=EVORAO.infectivity, name="Pathogen_infectivity", curie=EVORAO.curie('infectivity'),
                   model_uri=EVORAO.Pathogen_infectivity, domain=Pathogen, range=str)

slots.Pathogen_infectivityTest = Slot(uri=EVORAO.infectivityTest, name="Pathogen_infectivityTest", curie=EVORAO.curie('infectivityTest'),
                   model_uri=EVORAO.Pathogen_infectivityTest, domain=Pathogen, range=Optional[str])

slots.Pathogen_isolationTechnique = Slot(uri=EVORAO.isolationTechnique, name="Pathogen_isolationTechnique", curie=EVORAO.curie('isolationTechnique'),
                   model_uri=EVORAO.Pathogen_isolationTechnique, domain=Pathogen, range=Optional[str])

slots.Pathogen_isolationConditions = Slot(uri=EVORAO.isolationConditions, name="Pathogen_isolationConditions", curie=EVORAO.curie('isolationConditions'),
                   model_uri=EVORAO.Pathogen_isolationConditions, domain=Pathogen, range=Optional[str])

slots.Pathogen_letterOfAuthority = Slot(uri=EVORAO.letterOfAuthority, name="Pathogen_letterOfAuthority", curie=EVORAO.curie('letterOfAuthority'),
                   model_uri=EVORAO.Pathogen_letterOfAuthority, domain=Pathogen, range=str)

slots.Pathogen_passage = Slot(uri=EVORAO.passage, name="Pathogen_passage", curie=EVORAO.curie('passage'),
                   model_uri=EVORAO.Pathogen_passage, domain=Pathogen, range=Optional[str])

slots.Pathogen_genomeSequencing = Slot(uri=EVORAO.genomeSequencing, name="Pathogen_genomeSequencing", curie=EVORAO.curie('genomeSequencing'),
                   model_uri=EVORAO.Pathogen_genomeSequencing, domain=Pathogen, range=str)

slots.Pathogen_titer = Slot(uri=EVORAO.titer, name="Pathogen_titer", curie=EVORAO.curie('titer'),
                   model_uri=EVORAO.Pathogen_titer, domain=Pathogen, range=str)

slots.Virus_coInfectingViruses = Slot(uri=EVORAO.coInfectingViruses, name="Virus_coInfectingViruses", curie=EVORAO.curie('coInfectingViruses'),
                   model_uri=EVORAO.Virus_coInfectingViruses, domain=Virus, range=Optional[Union[Union[dict, VirusName], list[Union[dict, VirusName]]]])

slots.Virus_contaminationWithCoInfectingViruses = Slot(uri=EVORAO.contaminationWithCoInfectingViruses, name="Virus_contaminationWithCoInfectingViruses", curie=EVORAO.curie('contaminationWithCoInfectingViruses'),
                   model_uri=EVORAO.Virus_contaminationWithCoInfectingViruses, domain=Virus, range=Union[bool, Bool])

slots.Virus_mycoplasmicContent = Slot(uri=EVORAO.mycoplasmicContent, name="Virus_mycoplasmicContent", curie=EVORAO.curie('mycoplasmicContent'),
                   model_uri=EVORAO.Virus_mycoplasmicContent, domain=Virus, range=Union[bool, Bool])

slots.MSDS_msdsContact = Slot(uri=EVORAO.msdsContact, name="MSDS_msdsContact", curie=EVORAO.curie('msdsContact'),
                   model_uri=EVORAO.MSDS_msdsContact, domain=MSDS, range=Union[dict, "ContactPoint"])

slots.MSDS_physicalChemicalProperties = Slot(uri=EVORAO.physicalChemicalProperties, name="MSDS_physicalChemicalProperties", curie=EVORAO.curie('physicalChemicalProperties'),
                   model_uri=EVORAO.MSDS_physicalChemicalProperties, domain=MSDS, range=Optional[str])

slots.MSDS_hazardsIdentification = Slot(uri=EVORAO.hazardsIdentification, name="MSDS_hazardsIdentification", curie=EVORAO.curie('hazardsIdentification'),
                   model_uri=EVORAO.MSDS_hazardsIdentification, domain=MSDS, range=Optional[str])

slots.MSDS_firstAidMeasures = Slot(uri=EVORAO.firstAidMeasures, name="MSDS_firstAidMeasures", curie=EVORAO.curie('firstAidMeasures'),
                   model_uri=EVORAO.MSDS_firstAidMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_fireFightingMeasures = Slot(uri=EVORAO.fireFightingMeasures, name="MSDS_fireFightingMeasures", curie=EVORAO.curie('fireFightingMeasures'),
                   model_uri=EVORAO.MSDS_fireFightingMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_accidentalReleaseMeasures = Slot(uri=EVORAO.accidentalReleaseMeasures, name="MSDS_accidentalReleaseMeasures", curie=EVORAO.curie('accidentalReleaseMeasures'),
                   model_uri=EVORAO.MSDS_accidentalReleaseMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_handlingAndStorage = Slot(uri=EVORAO.handlingAndStorage, name="MSDS_handlingAndStorage", curie=EVORAO.curie('handlingAndStorage'),
                   model_uri=EVORAO.MSDS_handlingAndStorage, domain=MSDS, range=Optional[str])

slots.MSDS_exposureControlsPersonalProtection = Slot(uri=EVORAO.exposureControlsPersonalProtection, name="MSDS_exposureControlsPersonalProtection", curie=EVORAO.curie('exposureControlsPersonalProtection'),
                   model_uri=EVORAO.MSDS_exposureControlsPersonalProtection, domain=MSDS, range=Optional[str])

slots.MSDS_stabilityAndReactivity = Slot(uri=EVORAO.stabilityAndReactivity, name="MSDS_stabilityAndReactivity", curie=EVORAO.curie('stabilityAndReactivity'),
                   model_uri=EVORAO.MSDS_stabilityAndReactivity, domain=MSDS, range=Optional[str])

slots.MSDS_toxicologicalInformation = Slot(uri=EVORAO.toxicologicalInformation, name="MSDS_toxicologicalInformation", curie=EVORAO.curie('toxicologicalInformation'),
                   model_uri=EVORAO.MSDS_toxicologicalInformation, domain=MSDS, range=Optional[str])

slots.MSDS_ecologicalInformation = Slot(uri=EVORAO.ecologicalInformation, name="MSDS_ecologicalInformation", curie=EVORAO.curie('ecologicalInformation'),
                   model_uri=EVORAO.MSDS_ecologicalInformation, domain=MSDS, range=Optional[str])

slots.MSDS_disposalConsiderations = Slot(uri=EVORAO.disposalConsiderations, name="MSDS_disposalConsiderations", curie=EVORAO.curie('disposalConsiderations'),
                   model_uri=EVORAO.MSDS_disposalConsiderations, domain=MSDS, range=Optional[str])

slots.MSDS_transportInformation = Slot(uri=EVORAO.transportInformation, name="MSDS_transportInformation", curie=EVORAO.curie('transportInformation'),
                   model_uri=EVORAO.MSDS_transportInformation, domain=MSDS, range=Optional[str])

slots.MSDS_regulatoryInformation = Slot(uri=EVORAO.regulatoryInformation, name="MSDS_regulatoryInformation", curie=EVORAO.curie('regulatoryInformation'),
                   model_uri=EVORAO.MSDS_regulatoryInformation, domain=MSDS, range=Optional[str])

slots.MSDS_furtherInformation = Slot(uri=EVORAO.furtherInformation, name="MSDS_furtherInformation", curie=EVORAO.curie('furtherInformation'),
                   model_uri=EVORAO.MSDS_furtherInformation, domain=MSDS, range=Optional[str])

slots.File_name = Slot(uri=EVORAO.name, name="File_name", curie=EVORAO.curie('name'),
                   model_uri=EVORAO.File_name, domain=File, range=str)

slots.File_description = Slot(uri=DCT.description, name="File_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.File_description, domain=File, range=Optional[str])

slots.File_contentURL = Slot(uri=EVORAO.contentURL, name="File_contentURL", curie=EVORAO.curie('contentURL'),
                   model_uri=EVORAO.File_contentURL, domain=File, range=Union[str, URI])

slots.File_format = Slot(uri=EVORAO.format, name="File_format", curie=EVORAO.curie('format'),
                   model_uri=EVORAO.File_format, domain=File, range=str)

slots.File_license = Slot(uri=EVORAO.license, name="File_license", curie=EVORAO.curie('license'),
                   model_uri=EVORAO.File_license, domain=File, range=Optional[Union[dict, "License"]])

slots.Image_altText = Slot(uri=EVORAO.altText, name="Image_altText", curie=EVORAO.curie('altText'),
                   model_uri=EVORAO.Image_altText, domain=Image, range=Optional[str])

slots.ContactPoint_name = Slot(uri=EVORAO.name, name="ContactPoint_name", curie=EVORAO.curie('name'),
                   model_uri=EVORAO.ContactPoint_name, domain=ContactPoint, range=str)

slots.ContactPoint_description = Slot(uri=DCT.description, name="ContactPoint_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.ContactPoint_description, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_email = Slot(uri=EVORAO.email, name="ContactPoint_email", curie=EVORAO.curie('email'),
                   model_uri=EVORAO.ContactPoint_email, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_telephone = Slot(uri=EVORAO.telephone, name="ContactPoint_telephone", curie=EVORAO.curie('telephone'),
                   model_uri=EVORAO.ContactPoint_telephone, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_streetAddress = Slot(uri=EVORAO.streetAddress, name="ContactPoint_streetAddress", curie=EVORAO.curie('streetAddress'),
                   model_uri=EVORAO.ContactPoint_streetAddress, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressLocality = Slot(uri=EVORAO.addressLocality, name="ContactPoint_addressLocality", curie=EVORAO.curie('addressLocality'),
                   model_uri=EVORAO.ContactPoint_addressLocality, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressRegion = Slot(uri=EVORAO.addressRegion, name="ContactPoint_addressRegion", curie=EVORAO.curie('addressRegion'),
                   model_uri=EVORAO.ContactPoint_addressRegion, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_postalCode = Slot(uri=EVORAO.postalCode, name="ContactPoint_postalCode", curie=EVORAO.curie('postalCode'),
                   model_uri=EVORAO.ContactPoint_postalCode, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressCountry = Slot(uri=EVORAO.addressCountry, name="ContactPoint_addressCountry", curie=EVORAO.curie('addressCountry'),
                   model_uri=EVORAO.ContactPoint_addressCountry, domain=ContactPoint, range=Optional[Union[dict, Country]])

slots.ContactPoint_oRCIDiD = Slot(uri=EVORAO.oRCIDiD, name="ContactPoint_oRCIDiD", curie=EVORAO.curie('oRCIDiD'),
                   model_uri=EVORAO.ContactPoint_oRCIDiD, domain=ContactPoint, range=Optional[str])

slots.License_title = Slot(uri=DCT.title, name="License_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.License_title, domain=License, range=str)

slots.License_description = Slot(uri=DCT.description, name="License_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.License_description, domain=License, range=Optional[str])

slots.License_resourceURL = Slot(uri=EVORAO.resourceURL, name="License_resourceURL", curie=EVORAO.curie('resourceURL'),
                   model_uri=EVORAO.License_resourceURL, domain=License, range=Optional[Union[str, URI]])

slots.License_licensingOrAttribution = Slot(uri=EVORAO.licensingOrAttribution, name="License_licensingOrAttribution", curie=EVORAO.curie('licensingOrAttribution'),
                   model_uri=EVORAO.License_licensingOrAttribution, domain=License, range=Optional[str])

slots.License_logo = Slot(uri=EVORAO.logo, name="License_logo", curie=EVORAO.curie('logo'),
                   model_uri=EVORAO.License_logo, domain=License, range=Optional[Union[dict, Image]])

slots.Certification_title = Slot(uri=DCT.title, name="Certification_title", curie=DCT.curie('title'),
                   model_uri=EVORAO.Certification_title, domain=Certification, range=str)

slots.Certification_description = Slot(uri=DCT.description, name="Certification_description", curie=DCT.curie('description'),
                   model_uri=EVORAO.Certification_description, domain=Certification, range=Optional[str])

slots.Certification_logo = Slot(uri=EVORAO.logo, name="Certification_logo", curie=EVORAO.curie('logo'),
                   model_uri=EVORAO.Certification_logo, domain=Certification, range=Optional[Union[dict, Image]])

slots.Certification_certificationDocument = Slot(uri=EVORAO.certificationDocument, name="Certification_certificationDocument", curie=EVORAO.curie('certificationDocument'),
                   model_uri=EVORAO.Certification_certificationDocument, domain=Certification, range=Optional[Union[Union[dict, Document], list[Union[dict, Document]]]])

slots.Certification_resourceURL = Slot(uri=EVORAO.resourceURL, name="Certification_resourceURL", curie=EVORAO.curie('resourceURL'),
                   model_uri=EVORAO.Certification_resourceURL, domain=Certification, range=Optional[Union[str, URI]])
