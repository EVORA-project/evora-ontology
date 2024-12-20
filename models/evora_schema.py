# Auto generated from evora_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-20T16:19:56
# Schema: EVORA
#
# id: EVORA
# description:
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
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
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
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EVORA = CurieNamespace('EVORA', 'https://evora-project.eu/')
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
DEFAULT_ = EVORA


# Types

# Class references



@dataclass(repr=False)
class Nameable(YAMLRoot):
    """
    Any entity that has a name and can have a textual description
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Nameable"]
    class_class_curie: ClassVar[str] = "EVORA:Nameable"
    class_name: ClassVar[str] = "Nameable"
    class_model_uri: ClassVar[URIRef] = EVORA.Nameable

    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalogue(Nameable):
    """
    A curated collection of metadata about resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Catalogue"]
    class_class_curie: ClassVar[str] = "EVORA:Catalogue"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = EVORA.Catalogue

    name: str = None

class Dataset(YAMLRoot):
    """
    A collection of data, published or curated by a single agent, and available for access
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Dataset"]
    class_class_curie: ClassVar[str] = "EVORA:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = EVORA.Dataset


@dataclass(repr=False)
class Version(Dataset):
    """
    Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Version"]
    class_class_curie: ClassVar[str] = "EVORA:Version"
    class_name: ClassVar[str] = "Version"
    class_model_uri: ClassVar[URIRef] = EVORA.Version

    ID: str = None
    versionOf: Union[str, URI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, str):
            self.ID = str(self.ID)

        if self._is_empty(self.versionOf):
            self.MissingRequiredField("versionOf")
        if not isinstance(self.versionOf, URI):
            self.versionOf = URI(self.versionOf)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedDataset(Nameable):
    """
    A collection of data, that has a name and can have a description, published or curated by a single agent, and
    available for access
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["NamedDataset"]
    class_class_curie: ClassVar[str] = "EVORA:NamedDataset"
    class_name: ClassVar[str] = "NamedDataset"
    class_model_uri: ClassVar[URIRef] = EVORA.NamedDataset

    name: str = None

@dataclass(repr=False)
class DataService(Nameable):
    """
    A collection of operations that provides access to one or more datasets or data processing functions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["DataService"]
    class_class_curie: ClassVar[str] = "EVORA:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = EVORA.DataService

    name: str = None

@dataclass(repr=False)
class Taxonomy(Catalogue):
    """
    Science of naming, defining and classifying organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Taxonomy"]
    class_class_curie: ClassVar[str] = "EVORA:Taxonomy"
    class_name: ClassVar[str] = "Taxonomy"
    class_model_uri: ClassVar[URIRef] = EVORA.Taxonomy

    name: str = None
    version: Union[dict, Version] = None
    versionDataProvider: Union[dict, "DataProvider"] = None
    taxon: Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]] = empty_list()
    taxonDataProvider: Optional[Union[dict, "DataProvider"]] = None
    rank: Optional[Union[Union[dict, "TaxonomicRank"], List[Union[dict, "TaxonomicRank"]]]] = empty_list()
    rankDataProvider: Optional[Union[dict, "DataProvider"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, Version):
            self.version = Version(**as_dict(self.version))

        if self._is_empty(self.versionDataProvider):
            self.MissingRequiredField("versionDataProvider")
        if not isinstance(self.versionDataProvider, DataProvider):
            self.versionDataProvider = DataProvider(**as_dict(self.versionDataProvider))

        self._normalize_inlined_as_dict(slot_name="taxon", slot_type=Taxon, key_name="name", keyed=False)

        if self.taxonDataProvider is not None and not isinstance(self.taxonDataProvider, DataProvider):
            self.taxonDataProvider = DataProvider(**as_dict(self.taxonDataProvider))

        self._normalize_inlined_as_dict(slot_name="rank", slot_type=TaxonomicRank, key_name="name", keyed=False)

        if self.rankDataProvider is not None and not isinstance(self.rankDataProvider, DataProvider):
            self.rankDataProvider = DataProvider(**as_dict(self.rankDataProvider))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProvider(DataService):
    """
    An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["DataProvider"]
    class_class_curie: ClassVar[str] = "EVORA:DataProvider"
    class_name: ClassVar[str] = "DataProvider"
    class_model_uri: ClassVar[URIRef] = EVORA.DataProvider

    name: str = None
    queryURL: Union[str, URI] = None
    queryMethod: str = None
    providedEntityType: str = None
    weight: int = None
    contentType: str = "JSON"
    license: Optional[Union[dict, "License"]] = None
    loginRequestMethod: Optional[str] = "GET"
    loginURL: Optional[Union[str, URI]] = None
    loginTokenName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.queryURL):
            self.MissingRequiredField("queryURL")
        if not isinstance(self.queryURL, URI):
            self.queryURL = URI(self.queryURL)

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
        if not isinstance(self.providedEntityType, str):
            self.providedEntityType = str(self.providedEntityType)

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
class PathogenIdentification(Dataset):
    """
    A collection of distinguishing information that enables the differentiation of a pathogen from another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["PathogenIdentification"]
    class_class_curie: ClassVar[str] = "EVORA:PathogenIdentification"
    class_name: ClassVar[str] = "PathogenIdentification"
    class_model_uri: ClassVar[URIRef] = EVORA.PathogenIdentification

    taxon: Union[dict, "Taxon"] = None
    pathogenName: Union[dict, "CommonName"] = None
    pathogenType: str = None
    hostType: Optional[Union[str, List[str]]] = empty_list()
    subspecies: Optional[str] = None
    strain: Optional[str] = None
    isolate: Optional[str] = None
    genotype: Optional[str] = None
    serotype: Optional[str] = None
    variant: Optional[Union[dict, "Variant"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class Publication(Dataset):
    """
    A scientific publication
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Publication"]
    class_class_curie: ClassVar[str] = "EVORA:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = EVORA.Publication

    title: str = None
    authors: str = None
    abstract: str = None
    relatedDOI: Union[dict, "DOI"] = None
    journal: Optional[Union[dict, "Journal"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
        if not isinstance(self.relatedDOI, DOI):
            self.relatedDOI = DOI(**as_dict(self.relatedDOI))

        if self.journal is not None and not isinstance(self.journal, Journal):
            self.journal = Journal(**as_dict(self.journal))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vocabulary(Catalogue):
    """
    A subset of words or phrases specific to a particular subject or field
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Vocabulary"]
    class_class_curie: ClassVar[str] = "EVORA:Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = EVORA.Vocabulary

    name: str = None
    termDataProvider: Optional[Union[dict, DataProvider]] = None
    term: Optional[Union[Union[dict, "Term"], List[Union[dict, "Term"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.termDataProvider is not None and not isinstance(self.termDataProvider, DataProvider):
            self.termDataProvider = DataProvider(**as_dict(self.termDataProvider))

        self._normalize_inlined_as_dict(slot_name="term", slot_type=Term, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(NamedDataset):
    """
    Word or phrase from a specialized area of knowledge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Term"]
    class_class_curie: ClassVar[str] = "EVORA:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = EVORA.Term

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.weight):
            self.MissingRequiredField("weight")
        if not isinstance(self.weight, int):
            self.weight = int(self.weight)

        if self._is_empty(self.inVocabulary):
            self.MissingRequiredField("inVocabulary")
        if not isinstance(self.inVocabulary, Vocabulary):
            self.inVocabulary = Vocabulary(**as_dict(self.inVocabulary))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonName(Term):
    """
    Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This
    name is typically easier to remember and pronounce compared to the scientific name
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["CommonName"]
    class_class_curie: ClassVar[str] = "EVORA:CommonName"
    class_name: ClassVar[str] = "CommonName"
    class_model_uri: ClassVar[URIRef] = EVORA.CommonName

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    alternateName: Optional[Union[Union[dict, "AlternateName"], List[Union[dict, "AlternateName"]]]] = empty_list()
    sourceOfInformation: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="alternateName", slot_type=AlternateName, key_name="name", keyed=False)

        if not isinstance(self.sourceOfInformation, list):
            self.sourceOfInformation = [self.sourceOfInformation] if self.sourceOfInformation is not None else []
        self.sourceOfInformation = [v if isinstance(v, str) else str(v) for v in self.sourceOfInformation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirusName(CommonName):
    """
    A virus vernacular name or a name that describes a group of viruses
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["VirusName"]
    class_class_curie: ClassVar[str] = "EVORA:VirusName"
    class_name: ClassVar[str] = "VirusName"
    class_model_uri: ClassVar[URIRef] = EVORA.VirusName

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class AlternateName(Term):
    """
    List of alternate names for things
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["AlternateName"]
    class_class_curie: ClassVar[str] = "EVORA:AlternateName"
    class_name: ClassVar[str] = "AlternateName"
    class_model_uri: ClassVar[URIRef] = EVORA.AlternateName

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    alternateName: Optional[Union[Union[dict, "AlternateName"], List[Union[dict, "AlternateName"]]]] = empty_list()
    sourceOfInformation: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="alternateName", slot_type=AlternateName, key_name="name", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["RiskGroup"]
    class_class_curie: ClassVar[str] = "EVORA:RiskGroup"
    class_name: ClassVar[str] = "RiskGroup"
    class_model_uri: ClassVar[URIRef] = EVORA.RiskGroup

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class DOI(Term):
    """
    A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and
    access. The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["DOI"]
    class_class_curie: ClassVar[str] = "EVORA:DOI"
    class_name: ClassVar[str] = "DOI"
    class_model_uri: ClassVar[URIRef] = EVORA.DOI

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Journal(Term):
    """
    Periodical journal publishing scientific research
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Journal"]
    class_class_curie: ClassVar[str] = "EVORA:Journal"
    class_name: ClassVar[str] = "Journal"
    class_model_uri: ClassVar[URIRef] = EVORA.Journal

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PDBReference(Term):
    """
    Identifier for 3D structural data as per the PDB (Protein Data Bank) database
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["PDBReference"]
    class_class_curie: ClassVar[str] = "EVORA:PDBReference"
    class_name: ClassVar[str] = "PDBReference"
    class_model_uri: ClassVar[URIRef] = EVORA.PDBReference

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Keyword(Term):
    """
    A term or phrase used to tag and categorize content
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Keyword"]
    class_class_curie: ClassVar[str] = "EVORA:Keyword"
    class_name: ClassVar[str] = "Keyword"
    class_model_uri: ClassVar[URIRef] = EVORA.Keyword

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProteinTag(Term):
    """
    Peptide sequence genetically grafted onto a recombinant protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ProteinTag"]
    class_class_curie: ClassVar[str] = "EVORA:ProteinTag"
    class_name: ClassVar[str] = "ProteinTag"
    class_model_uri: ClassVar[URIRef] = EVORA.ProteinTag

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class SpecialFeature(Term):
    """
    Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal
    strain, Antiviral resistant strain ...
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["SpecialFeature"]
    class_class_curie: ClassVar[str] = "EVORA:SpecialFeature"
    class_name: ClassVar[str] = "SpecialFeature"
    class_model_uri: ClassVar[URIRef] = EVORA.SpecialFeature

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ExpressionVector(Term):
    """
    A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein
    expression
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ExpressionVector"]
    class_class_curie: ClassVar[str] = "EVORA:ExpressionVector"
    class_name: ClassVar[str] = "ExpressionVector"
    class_model_uri: ClassVar[URIRef] = EVORA.ExpressionVector

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PlasmidSelection(Term):
    """
    The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic
    resistance markers
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["PlasmidSelection"]
    class_class_curie: ClassVar[str] = "EVORA:PlasmidSelection"
    class_name: ClassVar[str] = "PlasmidSelection"
    class_model_uri: ClassVar[URIRef] = EVORA.PlasmidSelection

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class PropagationHost(Term):
    """
    The organism used to grow and multiply the pathogen under controlled conditions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["PropagationHost"]
    class_class_curie: ClassVar[str] = "EVORA:PropagationHost"
    class_name: ClassVar[str] = "PropagationHost"
    class_model_uri: ClassVar[URIRef] = EVORA.PropagationHost

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class TransmissionMethod(Term):
    """
    The process by which the pathogen spreads between hosts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["TransmissionMethod"]
    class_class_curie: ClassVar[str] = "EVORA:TransmissionMethod"
    class_name: ClassVar[str] = "TransmissionMethod"
    class_model_uri: ClassVar[URIRef] = EVORA.TransmissionMethod

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProductionCellLine(Term):
    """
    A population of cells that originates from a primary culture, adapted to grow and divide under laboratory
    conditions. Used in biotechnology to consistently produce biological substances
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ProductionCellLine"]
    class_class_curie: ClassVar[str] = "EVORA:ProductionCellLine"
    class_name: ClassVar[str] = "ProductionCellLine"
    class_model_uri: ClassVar[URIRef] = EVORA.ProductionCellLine

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class ProductCategory(Term):
    """
    A term used to classify a group of products that share common characteristics or functions, which helps in their
    organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ProductCategory"]
    class_class_curie: ClassVar[str] = "EVORA:ProductCategory"
    class_name: ClassVar[str] = "ProductCategory"
    class_model_uri: ClassVar[URIRef] = EVORA.ProductCategory

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    parentCategory: Optional[Union[dict, "ProductCategory"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.parentCategory is not None and not isinstance(self.parentCategory, ProductCategory):
            self.parentCategory = ProductCategory(**as_dict(self.parentCategory))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsolationHost(Term):
    """
    Host organism from which the pathogen was isolated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["IsolationHost"]
    class_class_curie: ClassVar[str] = "EVORA:IsolationHost"
    class_name: ClassVar[str] = "IsolationHost"
    class_model_uri: ClassVar[URIRef] = EVORA.IsolationHost

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class GeographicalOrigin(Term):
    """
    The specific location or region where a physical item, originates or is naturally found
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["GeographicalOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:GeographicalOrigin"
    class_name: ClassVar[str] = "GeographicalOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.GeographicalOrigin

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class IPLCOrigin(GeographicalOrigin):
    """
    The IPLC area (Indigenous People and Local Communities) from which a physical item originates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["IPLCOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:IPLCOrigin"
    class_name: ClassVar[str] = "IPLCOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.IPLCOrigin

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Country(Term):
    """
    The country as of ISO3166
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Country"]
    class_class_curie: ClassVar[str] = "EVORA:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = EVORA.Country

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    alpha2Code: str = None
    weight: int = 0

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["IATAClassification"]
    class_class_curie: ClassVar[str] = "EVORA:IATAClassification"
    class_name: ClassVar[str] = "IATAClassification"
    class_model_uri: ClassVar[URIRef] = EVORA.IATAClassification

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class Variant(CommonName):
    """
    An organism with one or more new mutations is referred to as a “variant” of the original organism if not
    sufficiently different to be termed a distinct strain
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Variant"]
    class_class_curie: ClassVar[str] = "EVORA:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = EVORA.Variant

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0

@dataclass(repr=False)
class TaxonomicRank(Term):
    """
    The possible taxonomic ranks and their description
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["TaxonomicRank"]
    class_class_curie: ClassVar[str] = "EVORA:TaxonomicRank"
    class_name: ClassVar[str] = "TaxonomicRank"
    class_model_uri: ClassVar[URIRef] = EVORA.TaxonomicRank

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    weight: int = 0
    taxonomy: Optional[Union[Union[dict, Taxonomy], List[Union[dict, Taxonomy]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=Taxonomy, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Taxon(Term):
    """
    Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form
    a unit
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Taxon"]
    class_class_curie: ClassVar[str] = "EVORA:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = EVORA.Taxon

    name: str = None
    inVocabulary: Union[dict, Vocabulary] = None
    parentTaxon: Union[dict, "Taxon"] = None
    rank: Union[dict, TaxonomicRank] = None
    taxonomicID: str = None
    weight: int = 0
    taxonomy: Optional[Union[Union[dict, Taxonomy], List[Union[dict, Taxonomy]]]] = empty_list()
    previouslyKnownAs: Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]] = empty_list()
    externalEquivalentTaxon: Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]] = empty_list()
    taxonomicNodeID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="taxonomy", slot_type=Taxonomy, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="previouslyKnownAs", slot_type=Taxon, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="externalEquivalentTaxon", slot_type=Taxon, key_name="name", keyed=False)

        if self.taxonomicNodeID is not None and not isinstance(self.taxonomicNodeID, str):
            self.taxonomicNodeID = str(self.taxonomicNodeID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalRelatedReference(Dataset):
    """
    A reference that permits to retrieve an item from an external provider
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ExternalRelatedReference"]
    class_class_curie: ClassVar[str] = "EVORA:ExternalRelatedReference"
    class_name: ClassVar[str] = "ExternalRelatedReference"
    class_model_uri: ClassVar[URIRef] = EVORA.ExternalRelatedReference

    reference: str = None
    referenceLabel: str = None
    referenceProviderPrefix: str = None
    referenceProviderName: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class Sequence(Dataset):
    """
    A nucleic acid or protein sequence information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Sequence"]
    class_class_curie: ClassVar[str] = "EVORA:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = EVORA.Sequence

    sequenceReference: Optional[Union[Union[dict, "SequenceReference"], List[Union[dict, "SequenceReference"]]]] = empty_list()
    sequenceFASTA: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="sequenceReference", slot_type=SequenceReference, key_name="accessionNumber", keyed=False)

        if self.sequenceFASTA is not None and not isinstance(self.sequenceFASTA, str):
            self.sequenceFASTA = str(self.sequenceFASTA)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceReference(Dataset):
    """
    A reference that permits to retrieve the sequence information from a sequence provider
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["SequenceReference"]
    class_class_curie: ClassVar[str] = "EVORA:SequenceReference"
    class_name: ClassVar[str] = "SequenceReference"
    class_model_uri: ClassVar[URIRef] = EVORA.SequenceReference

    accessionNumber: str = None
    sequenceProvider: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class PersonOrOrganization(Nameable):
    """
    A person or an organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["PersonOrOrganization"]
    class_class_curie: ClassVar[str] = "EVORA:PersonOrOrganization"
    class_name: ClassVar[str] = "PersonOrOrganization"
    class_model_uri: ClassVar[URIRef] = EVORA.PersonOrOrganization

    name: str = None
    homePage: Optional[str] = None
    contactPoint: Optional[Union[dict, "ContactPoint"]] = None
    logo: Optional[Union[dict, "Image"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.homePage is not None and not isinstance(self.homePage, str):
            self.homePage = str(self.homePage)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Person"]
    class_class_curie: ClassVar[str] = "EVORA:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EVORA.Person

    name: str = None
    oRCIDiD: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.oRCIDiD is not None and not isinstance(self.oRCIDiD, str):
            self.oRCIDiD = str(self.oRCIDiD)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(PersonOrOrganization):
    """
    A social entity established to meet needs or pursue specific goals
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Organization"]
    class_class_curie: ClassVar[str] = "EVORA:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = EVORA.Organization

    name: str = None
    alternateName: Optional[Union[dict, AlternateName]] = None
    country: Optional[Union[dict, Country]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alternateName is not None and not isinstance(self.alternateName, AlternateName):
            self.alternateName = AlternateName(**as_dict(self.alternateName))

        if self.country is not None and not isinstance(self.country, Country):
            self.country = Country(**as_dict(self.country))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RI(Organization):
    """
    A research infrastructure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["RI"]
    class_class_curie: ClassVar[str] = "EVORA:RI"
    class_name: ClassVar[str] = "RI"
    class_model_uri: ClassVar[URIRef] = EVORA.RI

    name: str = None

@dataclass(repr=False)
class Provider(Organization):
    """
    A provider of products or services, as a specific organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Provider"]
    class_class_curie: ClassVar[str] = "EVORA:Provider"
    class_name: ClassVar[str] = "Provider"
    class_model_uri: ClassVar[URIRef] = EVORA.Provider

    name: str = None
    memberOfRI: Optional[Union[Union[dict, RI], List[Union[dict, RI]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="memberOfRI", slot_type=RI, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Originator(PersonOrOrganization):
    """
    The individual or organization responsible for the original discovery, isolation, or creation of an item,
    providing information about the source or origin of the sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Originator"]
    class_class_curie: ClassVar[str] = "EVORA:Originator"
    class_name: ClassVar[str] = "Originator"
    class_model_uri: ClassVar[URIRef] = EVORA.Originator

    name: str = None

@dataclass(repr=False)
class BiologicalMaterialOrigin(Dataset):
    """
    Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing
    of genetic resources in compliance with the Nagoya Protocol
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["BiologicalMaterialOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:BiologicalMaterialOrigin"
    class_name: ClassVar[str] = "BiologicalMaterialOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.BiologicalMaterialOrigin

    biologicalSourceType: Union[bool, Bool] = None
    biologicalPartOrigin: Union[Union[dict, "BiologicalPartOrigin"], List[Union[dict, "BiologicalPartOrigin"]]] = None
    recombinantMaterial: Union[bool, Bool] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class BiologicalPartOrigin(Dataset):
    """
    Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It
    can be multiple parts in case of a recombinant biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["BiologicalPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:BiologicalPartOrigin"
    class_name: ClassVar[str] = "BiologicalPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.BiologicalPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    recombinantPartIdentification: Optional[Union[dict, "RecombinantPartIdentification"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["NaturalPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:NaturalPartOrigin"
    class_name: ClassVar[str] = "NaturalPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.NaturalPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    countryOfCollection: Union[dict, Country] = None
    collectionDate: Union[str, XSDDateTime] = None
    beforeDate: Union[bool, Bool] = False
    indigenousPoepleAndLocalCommunityOrigin: Optional[Union[dict, IPLCOrigin]] = None
    permitIdentifierForABS: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["SyntheticPartOrigin"]
    class_class_curie: ClassVar[str] = "EVORA:SyntheticPartOrigin"
    class_name: ClassVar[str] = "SyntheticPartOrigin"
    class_model_uri: ClassVar[URIRef] = EVORA.SyntheticPartOrigin

    accessToPhysicalGeneticResource: Union[bool, Bool] = None
    modificationsFromTheReferenceSequences: Union[bool, Bool] = None
    descriptionOfModificationsMadeFromTheReferenceSequences: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.modificationsFromTheReferenceSequences):
            self.MissingRequiredField("modificationsFromTheReferenceSequences")
        if not isinstance(self.modificationsFromTheReferenceSequences, Bool):
            self.modificationsFromTheReferenceSequences = Bool(self.modificationsFromTheReferenceSequences)

        if self.descriptionOfModificationsMadeFromTheReferenceSequences is not None and not isinstance(self.descriptionOfModificationsMadeFromTheReferenceSequences, str):
            self.descriptionOfModificationsMadeFromTheReferenceSequences = str(self.descriptionOfModificationsMadeFromTheReferenceSequences)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecombinantPartIdentification(YAMLRoot):
    """
    Identification of a recombinant part
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["RecombinantPartIdentification"]
    class_class_curie: ClassVar[str] = "EVORA:RecombinantPartIdentification"
    class_name: ClassVar[str] = "RecombinantPartIdentification"
    class_model_uri: ClassVar[URIRef] = EVORA.RecombinantPartIdentification

    partIdentification: str = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Collection"]
    class_class_curie: ClassVar[str] = "EVORA:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = EVORA.Collection

    name: str = None
    collectionItem: Optional[Union[Union[dict, "ProductOrService"], List[Union[dict, "ProductOrService"]]]] = empty_list()
    collectionDataProvider: Optional[Union[dict, DataProvider]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="collectionItem", slot_type=ProductOrService, key_name="name", keyed=False)

        if self.collectionDataProvider is not None and not isinstance(self.collectionDataProvider, DataProvider):
            self.collectionDataProvider = DataProvider(**as_dict(self.collectionDataProvider))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProductOrService(NamedDataset):
    """
    A product or a service
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ProductOrService"]
    class_class_curie: ClassVar[str] = "EVORA:ProductOrService"
    class_name: ClassVar[str] = "ProductOrService"
    class_model_uri: ClassVar[URIRef] = EVORA.ProductOrService

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    unitDefinition: Optional[str] = None
    additionalCategory: Optional[Union[Union[dict, ProductCategory], List[Union[dict, ProductCategory]]]] = empty_list()
    qualityGrading: Optional[str] = None
    relatedDOI: Optional[Union[Union[dict, DOI], List[Union[dict, DOI]]]] = empty_list()
    riskGroup: Optional[Union[dict, RiskGroup]] = None
    biosafetyRestrictions: Optional[str] = None
    canItBeUsedToProduceGMO: Optional[Union[bool, Bool]] = None
    complementaryDocument: Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]] = empty_list()
    technicalRecommendation: Optional[str] = None
    productPicture: Optional[Union[Union[dict, "Image"], List[Union[dict, "Image"]]]] = empty_list()
    externalRelatedReference: Optional[Union[Union[dict, ExternalRelatedReference], List[Union[dict, ExternalRelatedReference]]]] = empty_list()
    certification: Optional[Union[Union[dict, "Certification"], List[Union[dict, "Certification"]]]] = empty_list()
    internalReference: Optional[str] = None
    note: Optional[str] = None
    contactPoint: Optional[Union[dict, "ContactPoint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self._is_empty(self.provider):
            self.MissingRequiredField("provider")
        if not isinstance(self.provider, Provider):
            self.provider = Provider(**as_dict(self.provider))

        if self._is_empty(self.collection):
            self.MissingRequiredField("collection")
        self._normalize_inlined_as_dict(slot_name="collection", slot_type=Collection, key_name="name", keyed=False)

        if self._is_empty(self.keywords):
            self.MissingRequiredField("keywords")
        self._normalize_inlined_as_dict(slot_name="keywords", slot_type=Keyword, key_name="name", keyed=False)

        if self._is_empty(self.availability):
            self.MissingRequiredField("availability")
        if not isinstance(self.availability, str):
            self.availability = str(self.availability)

        if self.unitDefinition is not None and not isinstance(self.unitDefinition, str):
            self.unitDefinition = str(self.unitDefinition)

        self._normalize_inlined_as_dict(slot_name="additionalCategory", slot_type=ProductCategory, key_name="name", keyed=False)

        if self.qualityGrading is not None and not isinstance(self.qualityGrading, str):
            self.qualityGrading = str(self.qualityGrading)

        self._normalize_inlined_as_dict(slot_name="relatedDOI", slot_type=DOI, key_name="name", keyed=False)

        if self.riskGroup is not None and not isinstance(self.riskGroup, RiskGroup):
            self.riskGroup = RiskGroup(**as_dict(self.riskGroup))

        if self.biosafetyRestrictions is not None and not isinstance(self.biosafetyRestrictions, str):
            self.biosafetyRestrictions = str(self.biosafetyRestrictions)

        if self.canItBeUsedToProduceGMO is not None and not isinstance(self.canItBeUsedToProduceGMO, Bool):
            self.canItBeUsedToProduceGMO = Bool(self.canItBeUsedToProduceGMO)

        self._normalize_inlined_as_dict(slot_name="complementaryDocument", slot_type=Document, key_name="name", keyed=False)

        if self.technicalRecommendation is not None and not isinstance(self.technicalRecommendation, str):
            self.technicalRecommendation = str(self.technicalRecommendation)

        self._normalize_inlined_as_dict(slot_name="productPicture", slot_type=Image, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="externalRelatedReference", slot_type=ExternalRelatedReference, key_name="reference", keyed=False)

        self._normalize_inlined_as_dict(slot_name="certification", slot_type=Certification, key_name="name", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Service"]
    class_class_curie: ClassVar[str] = "EVORA:Service"
    class_name: ClassVar[str] = "Service"
    class_model_uri: ClassVar[URIRef] = EVORA.Service

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    modelSpecies: Optional[str] = None
    modelType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Product"]
    class_class_curie: ClassVar[str] = "EVORA:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = EVORA.Product

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    materialSafetyDataSheet: Optional[Union[dict, "MSDS"]] = None
    originator: Optional[Union[dict, Originator]] = None
    thirdPartyDistributionConsent: Optional[Union[bool, Bool]] = None
    usageRestrictions: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Antibody"]
    class_class_curie: ClassVar[str] = "EVORA:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = EVORA.Antibody

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    antibodyPurifiedByAffinity: Union[bool, Bool] = None
    specificityDocumented: Union[bool, Bool] = None
    targetedAntigen: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    productionSystem: Optional[str] = None
    sequenceReference: Optional[Union[Union[dict, SequenceReference], List[Union[dict, SequenceReference]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Hybridoma"]
    class_class_curie: ClassVar[str] = "EVORA:Hybridoma"
    class_name: ClassVar[str] = "Hybridoma"
    class_model_uri: ClassVar[URIRef] = EVORA.Hybridoma

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    antibodyPurifiedByAffinity: Union[bool, Bool] = None
    specificityDocumented: Union[bool, Bool] = None
    targetedAntigen: str = None
    hybridomaDescription: str = None
    unitCost: str = "on request"
    availability: str = "on request"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Protein"]
    class_class_curie: ClassVar[str] = "EVORA:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = EVORA.Protein

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    relatedPDB: Optional[Union[Union[dict, PDBReference], List[Union[dict, PDBReference]]]] = empty_list()
    specialFeature: Optional[Union[Union[dict, SpecialFeature], List[Union[dict, SpecialFeature]]]] = empty_list()
    proteinTAG: Optional[Union[Union[dict, ProteinTag], List[Union[dict, ProteinTag]]]] = empty_list()
    domain: Optional[Union[str, List[str]]] = empty_list()
    expressedAs: Optional[Union[str, List[str]]] = empty_list()
    inclusionBodiesType: Optional[Union[str, List[str]]] = empty_list()
    expressionSystem: Optional[Union[str, List[str]]] = empty_list()
    functionalCharacterization: Optional[Union[str, List[str]]] = empty_list()
    functionalTechnicalDescription: Optional[Union[str, List[str]]] = empty_list()
    proteinPurification: Optional[Union[str, List[str]]] = empty_list()
    theTAGStatusOfTheSolubilizedProtein: Optional[Union[str, List[str]]] = empty_list()
    typeOfFunctionalCharacterization: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biologicalMaterialOrigin):
            self.MissingRequiredField("biologicalMaterialOrigin")
        if not isinstance(self.biologicalMaterialOrigin, BiologicalMaterialOrigin):
            self.biologicalMaterialOrigin = BiologicalMaterialOrigin(**as_dict(self.biologicalMaterialOrigin))

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, Sequence) else Sequence(**as_dict(v)) for v in self.sequence]

        self._normalize_inlined_as_dict(slot_name="relatedPDB", slot_type=PDBReference, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="specialFeature", slot_type=SpecialFeature, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="proteinTAG", slot_type=ProteinTag, key_name="name", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["NucleicAcid"]
    class_class_curie: ClassVar[str] = "EVORA:NucleicAcid"
    class_name: ClassVar[str] = "Nucleic Acid"
    class_model_uri: ClassVar[URIRef] = EVORA.NucleicAcid

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    isItAClonedNucleicAcid: Union[bool, Bool] = None
    hasTAG: Union[dict, ProteinTag] = None
    regionEncompassedInThisProduct: str = None
    mutationObserved: Union[bool, Bool] = None
    sequencing: str = None
    sequenceChecked: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    hasGbFileOfTheConstruct: Optional[Union[Union[dict, "Data"], List[Union[dict, "Data"]]]] = empty_list()
    clonedIntoPlasmid: Optional[Union[dict, ExpressionVector]] = None
    pasmidSelection: Optional[Union[Union[dict, PlasmidSelection], List[Union[dict, PlasmidSelection]]]] = empty_list()
    observedMutations: Optional[str] = None
    identificationTechnique: Optional[str] = None
    titer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self._is_empty(self.sequenceChecked):
            self.MissingRequiredField("sequenceChecked")
        if not isinstance(self.sequenceChecked, Bool):
            self.sequenceChecked = Bool(self.sequenceChecked)

        self._normalize_inlined_as_dict(slot_name="hasGbFileOfTheConstruct", slot_type=Data, key_name="name", keyed=False)

        if self.clonedIntoPlasmid is not None and not isinstance(self.clonedIntoPlasmid, ExpressionVector):
            self.clonedIntoPlasmid = ExpressionVector(**as_dict(self.clonedIntoPlasmid))

        self._normalize_inlined_as_dict(slot_name="pasmidSelection", slot_type=PlasmidSelection, key_name="name", keyed=False)

        if self.observedMutations is not None and not isinstance(self.observedMutations, str):
            self.observedMutations = str(self.observedMutations)

        if self.identificationTechnique is not None and not isinstance(self.identificationTechnique, str):
            self.identificationTechnique = str(self.identificationTechnique)

        if self.titer is not None and not isinstance(self.titer, str):
            self.titer = str(self.titer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DetectionKit(Product):
    """
    A detection kit for specific pathogens
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["DetectionKit"]
    class_class_curie: ClassVar[str] = "EVORA:DetectionKit"
    class_name: ClassVar[str] = "Detection Kit"
    class_model_uri: ClassVar[URIRef] = EVORA.DetectionKit

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    specificityDocumented: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    hasSOPFile: Optional[Union[Union[dict, "File"], List[Union[dict, "File"]]]] = empty_list()
    specificity: Optional[str] = None
    targetedRegion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Bundle"]
    class_class_curie: ClassVar[str] = "EVORA:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = EVORA.Bundle

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    productsOfTheBundle: Union[Union[dict, Product], List[Union[dict, Product]]] = None
    unitCost: str = "on request"
    availability: str = "on request"
    complementaryDocument: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.productsOfTheBundle):
            self.MissingRequiredField("productsOfTheBundle")
        self._normalize_inlined_as_dict(slot_name="productsOfTheBundle", slot_type=Product, key_name="name", keyed=False)

        if self.complementaryDocument is not None and not isinstance(self.complementaryDocument, str):
            self.complementaryDocument = str(self.complementaryDocument)

        self._normalize_inlined_as_dict(slot_name="complementaryDocument", slot_type=File, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pathogen(Product):
    """
    Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such
    as a virus, bacterium, protozoan, prion, viroid, or fungus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Pathogen"]
    class_class_curie: ClassVar[str] = "EVORA:Pathogen"
    class_name: ClassVar[str] = "Pathogen"
    class_model_uri: ClassVar[URIRef] = EVORA.Pathogen

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"
    suspectedEpidemiologicalOrigin: Optional[Union[Union[dict, GeographicalOrigin], List[Union[dict, GeographicalOrigin]]]] = empty_list()
    isolationHost: Optional[Union[Union[dict, IsolationHost], List[Union[dict, IsolationHost]]]] = empty_list()
    productionCellLine: Optional[Union[Union[dict, ProductionCellLine], List[Union[dict, ProductionCellLine]]]] = empty_list()
    propagationHost: Optional[Union[Union[dict, PropagationHost], List[Union[dict, PropagationHost]]]] = empty_list()
    transmissionMethod: Optional[Union[Union[dict, TransmissionMethod], List[Union[dict, TransmissionMethod]]]] = empty_list()
    clinicalInformation: Optional[str] = None
    identificationTechnique: Optional[str] = None
    infectivityTest: Optional[str] = None
    isolationTechnique: Optional[str] = None
    isolationConditions: Optional[str] = None
    passage: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self._is_empty(self.sequencing):
            self.MissingRequiredField("sequencing")
        if not isinstance(self.sequencing, str):
            self.sequencing = str(self.sequencing)

        if self._is_empty(self.titer):
            self.MissingRequiredField("titer")
        if not isinstance(self.titer, str):
            self.titer = str(self.titer)

        self._normalize_inlined_as_dict(slot_name="suspectedEpidemiologicalOrigin", slot_type=GeographicalOrigin, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="isolationHost", slot_type=IsolationHost, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="productionCellLine", slot_type=ProductionCellLine, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="propagationHost", slot_type=PropagationHost, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="transmissionMethod", slot_type=TransmissionMethod, key_name="name", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Virus"]
    class_class_curie: ClassVar[str] = "EVORA:Virus"
    class_name: ClassVar[str] = "Virus"
    class_model_uri: ClassVar[URIRef] = EVORA.Virus

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    mycoplasmicContent: Union[bool, Bool] = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"
    contaminationWithCoInfectingViruses: Union[bool, Bool] = False
    coInfectingViruses: Optional[Union[Union[dict, VirusName], List[Union[dict, VirusName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contaminationWithCoInfectingViruses):
            self.MissingRequiredField("contaminationWithCoInfectingViruses")
        if not isinstance(self.contaminationWithCoInfectingViruses, Bool):
            self.contaminationWithCoInfectingViruses = Bool(self.contaminationWithCoInfectingViruses)

        if self._is_empty(self.mycoplasmicContent):
            self.MissingRequiredField("mycoplasmicContent")
        if not isinstance(self.mycoplasmicContent, Bool):
            self.mycoplasmicContent = Bool(self.mycoplasmicContent)

        self._normalize_inlined_as_dict(slot_name="coInfectingViruses", slot_type=VirusName, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bacterium(Pathogen):
    """
    The bacterium as a biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Bacterium"]
    class_class_curie: ClassVar[str] = "EVORA:Bacterium"
    class_name: ClassVar[str] = "Bacterium"
    class_model_uri: ClassVar[URIRef] = EVORA.Bacterium

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"

@dataclass(repr=False)
class Fungus(Pathogen):
    """
    The fungus as a biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Fungus"]
    class_class_curie: ClassVar[str] = "EVORA:Fungus"
    class_name: ClassVar[str] = "Fungus"
    class_model_uri: ClassVar[URIRef] = EVORA.Fungus

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"

@dataclass(repr=False)
class Protozoan(Pathogen):
    """
    The protozoan as a biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Protozoan"]
    class_class_curie: ClassVar[str] = "EVORA:Protozoan"
    class_name: ClassVar[str] = "Protozoan"
    class_model_uri: ClassVar[URIRef] = EVORA.Protozoan

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"

@dataclass(repr=False)
class Viroid(Pathogen):
    """
    The viroid as a biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Viroid"]
    class_class_curie: ClassVar[str] = "EVORA:Viroid"
    class_name: ClassVar[str] = "Viroid"
    class_model_uri: ClassVar[URIRef] = EVORA.Viroid

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"

@dataclass(repr=False)
class Prion(Pathogen):
    """
    The prion as a biological material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Prion"]
    class_class_curie: ClassVar[str] = "EVORA:Prion"
    class_name: ClassVar[str] = "Prion"
    class_model_uri: ClassVar[URIRef] = EVORA.Prion

    name: str = None
    accessPointURL: Union[str, URI] = None
    refSKU: str = None
    category: Union[dict, ProductCategory] = None
    pathogenIdentification: Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]] = None
    provider: Union[dict, Provider] = None
    collection: Union[Union[dict, Collection], List[Union[dict, Collection]]] = None
    keywords: Union[Union[dict, Keyword], List[Union[dict, Keyword]]] = None
    hasIATAClassification: Union[dict, IATAClassification] = None
    shippingConditions: str = None
    storageConditions: str = None
    biologicalMaterialOrigin: Union[dict, BiologicalMaterialOrigin] = None
    sequence: Union[Union[dict, Sequence], List[Union[dict, Sequence]]] = None
    infectivity: str = None
    sequencing: str = None
    titer: str = None
    unitCost: str = "on request"
    availability: str = "on request"
    cultivability: str = "Cultivable pathogen"
    letterOfAuthority: str = "N/A"

@dataclass(repr=False)
class MSDS(Dataset):
    """
    A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial
    occupational safety and health information related to the product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["MSDS"]
    class_class_curie: ClassVar[str] = "EVORA:MSDS"
    class_name: ClassVar[str] = "MSDS"
    class_model_uri: ClassVar[URIRef] = EVORA.MSDS

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class File(Nameable):
    """
    Digital document or record stored in a specific format that contains data or information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["File"]
    class_class_curie: ClassVar[str] = "EVORA:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = EVORA.File

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None
    license: Optional[Union[dict, "License"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contentURL):
            self.MissingRequiredField("contentURL")
        if not isinstance(self.contentURL, URI):
            self.contentURL = URI(self.contentURL)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Data(File):
    """
    Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer
    of information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Data"]
    class_class_curie: ClassVar[str] = "EVORA:Data"
    class_name: ClassVar[str] = "Data"
    class_model_uri: ClassVar[URIRef] = EVORA.Data

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Document(File):
    """
    Subclass of File representing textual or written files such as reports, manuals, or forms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Document"]
    class_class_curie: ClassVar[str] = "EVORA:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = EVORA.Document

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Audio(File):
    """
    Subclass of File representing sound recordings or audio tracks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Audio"]
    class_class_curie: ClassVar[str] = "EVORA:Audio"
    class_name: ClassVar[str] = "Audio"
    class_model_uri: ClassVar[URIRef] = EVORA.Audio

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Video(File):
    """
    Subclass of File representing moving visual media, such as recordings, presentations, or movies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Video"]
    class_class_curie: ClassVar[str] = "EVORA:Video"
    class_name: ClassVar[str] = "Video"
    class_model_uri: ClassVar[URIRef] = EVORA.Video

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None

@dataclass(repr=False)
class Image(File):
    """
    Subclass of File representing visual content such as pictures, diagrams, or illustrations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Image"]
    class_class_curie: ClassVar[str] = "EVORA:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = EVORA.Image

    name: str = None
    contentURL: Union[str, URI] = None
    format: str = None
    altText: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.altText is not None and not isinstance(self.altText, str):
            self.altText = str(self.altText)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContactPoint(Nameable):
    """
    Entity serving as focal point of information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["ContactPoint"]
    class_class_curie: ClassVar[str] = "EVORA:ContactPoint"
    class_name: ClassVar[str] = "ContactPoint"
    class_model_uri: ClassVar[URIRef] = EVORA.ContactPoint

    name: str = None
    email: Optional[str] = None
    telephone: Optional[str] = None
    streetAddress: Optional[str] = None
    addressLocality: Optional[str] = None
    addressRegion: Optional[str] = None
    postalCode: Optional[str] = None
    addressCountry: Optional[Union[dict, Country]] = None
    oRCIDiD: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class License(Nameable):
    """
    The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any
    restrictions or permissions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["License"]
    class_class_curie: ClassVar[str] = "EVORA:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = EVORA.License

    name: str = None
    resourceURL: Optional[Union[str, URI]] = None
    licensingOrAttribution: Optional[str] = None
    logo: Optional[Union[dict, Image]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resourceURL is not None and not isinstance(self.resourceURL, URI):
            self.resourceURL = URI(self.resourceURL)

        if self.licensingOrAttribution is not None and not isinstance(self.licensingOrAttribution, str):
            self.licensingOrAttribution = str(self.licensingOrAttribution)

        if self.logo is not None and not isinstance(self.logo, Image):
            self.logo = Image(**as_dict(self.logo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Certification(Nameable):
    """
    Assurance given by an independent certification body that a product, service or system meets the requirements of a
    standard
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EVORA["Certification"]
    class_class_curie: ClassVar[str] = "EVORA:Certification"
    class_name: ClassVar[str] = "Certification"
    class_model_uri: ClassVar[URIRef] = EVORA.Certification

    name: str = None
    logo: Optional[Union[dict, Image]] = None
    certificationDocument: Optional[Union[Union[dict, Document], List[Union[dict, Document]]]] = empty_list()
    resourceURL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

slots.ID = Slot(uri=EVORA.ID, name="ID", curie=EVORA.curie('ID'),
                   model_uri=EVORA.ID, domain=None, range=Optional[str])

slots.versionOf = Slot(uri=EVORA.versionOf, name="versionOf", curie=EVORA.curie('versionOf'),
                   model_uri=EVORA.versionOf, domain=None, range=Optional[str])

slots.name = Slot(uri=EVORA.name, name="name", curie=EVORA.curie('name'),
                   model_uri=EVORA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=EVORA.description, name="description", curie=EVORA.curie('description'),
                   model_uri=EVORA.description, domain=None, range=Optional[str])

slots.taxon = Slot(uri=EVORA.taxon, name="taxon", curie=EVORA.curie('taxon'),
                   model_uri=EVORA.taxon, domain=None, range=Optional[str])

slots.taxonDataProvider = Slot(uri=EVORA.taxonDataProvider, name="taxonDataProvider", curie=EVORA.curie('taxonDataProvider'),
                   model_uri=EVORA.taxonDataProvider, domain=None, range=Optional[str])

slots.version = Slot(uri=EVORA.version, name="version", curie=EVORA.curie('version'),
                   model_uri=EVORA.version, domain=None, range=Optional[str])

slots.versionDataProvider = Slot(uri=EVORA.versionDataProvider, name="versionDataProvider", curie=EVORA.curie('versionDataProvider'),
                   model_uri=EVORA.versionDataProvider, domain=None, range=Optional[str])

slots.rank = Slot(uri=EVORA.rank, name="rank", curie=EVORA.curie('rank'),
                   model_uri=EVORA.rank, domain=None, range=Optional[str])

slots.rankDataProvider = Slot(uri=EVORA.rankDataProvider, name="rankDataProvider", curie=EVORA.curie('rankDataProvider'),
                   model_uri=EVORA.rankDataProvider, domain=None, range=Optional[str])

slots.license = Slot(uri=EVORA.license, name="license", curie=EVORA.curie('license'),
                   model_uri=EVORA.license, domain=None, range=Optional[str])

slots.loginRequestMethod = Slot(uri=EVORA.loginRequestMethod, name="loginRequestMethod", curie=EVORA.curie('loginRequestMethod'),
                   model_uri=EVORA.loginRequestMethod, domain=None, range=Optional[str])

slots.loginURL = Slot(uri=EVORA.loginURL, name="loginURL", curie=EVORA.curie('loginURL'),
                   model_uri=EVORA.loginURL, domain=None, range=Optional[str])

slots.loginTokenName = Slot(uri=EVORA.loginTokenName, name="loginTokenName", curie=EVORA.curie('loginTokenName'),
                   model_uri=EVORA.loginTokenName, domain=None, range=Optional[str])

slots.queryURL = Slot(uri=EVORA.queryURL, name="queryURL", curie=EVORA.curie('queryURL'),
                   model_uri=EVORA.queryURL, domain=None, range=Optional[str])

slots.queryMethod = Slot(uri=EVORA.queryMethod, name="queryMethod", curie=EVORA.curie('queryMethod'),
                   model_uri=EVORA.queryMethod, domain=None, range=Optional[str])

slots.contentType = Slot(uri=EVORA.contentType, name="contentType", curie=EVORA.curie('contentType'),
                   model_uri=EVORA.contentType, domain=None, range=Optional[str])

slots.providedEntityType = Slot(uri=EVORA.providedEntityType, name="providedEntityType", curie=EVORA.curie('providedEntityType'),
                   model_uri=EVORA.providedEntityType, domain=None, range=Optional[str])

slots.weight = Slot(uri=EVORA.weight, name="weight", curie=EVORA.curie('weight'),
                   model_uri=EVORA.weight, domain=None, range=Optional[str])

slots.pathogenName = Slot(uri=EVORA.pathogenName, name="pathogenName", curie=EVORA.curie('pathogenName'),
                   model_uri=EVORA.pathogenName, domain=None, range=Optional[str])

slots.pathogenType = Slot(uri=EVORA.pathogenType, name="pathogenType", curie=EVORA.curie('pathogenType'),
                   model_uri=EVORA.pathogenType, domain=None, range=Optional[str])

slots.hostType = Slot(uri=EVORA.hostType, name="hostType", curie=EVORA.curie('hostType'),
                   model_uri=EVORA.hostType, domain=None, range=Optional[str])

slots.subspecies = Slot(uri=EVORA.subspecies, name="subspecies", curie=EVORA.curie('subspecies'),
                   model_uri=EVORA.subspecies, domain=None, range=Optional[str])

slots.strain = Slot(uri=EVORA.strain, name="strain", curie=EVORA.curie('strain'),
                   model_uri=EVORA.strain, domain=None, range=Optional[str])

slots.isolate = Slot(uri=EVORA.isolate, name="isolate", curie=EVORA.curie('isolate'),
                   model_uri=EVORA.isolate, domain=None, range=Optional[str])

slots.genotype = Slot(uri=EVORA.genotype, name="genotype", curie=EVORA.curie('genotype'),
                   model_uri=EVORA.genotype, domain=None, range=Optional[str])

slots.serotype = Slot(uri=EVORA.serotype, name="serotype", curie=EVORA.curie('serotype'),
                   model_uri=EVORA.serotype, domain=None, range=Optional[str])

slots.variant = Slot(uri=EVORA.variant, name="variant", curie=EVORA.curie('variant'),
                   model_uri=EVORA.variant, domain=None, range=Optional[str])

slots.title = Slot(uri=EVORA.title, name="title", curie=EVORA.curie('title'),
                   model_uri=EVORA.title, domain=None, range=Optional[str])

slots.authors = Slot(uri=EVORA.authors, name="authors", curie=EVORA.curie('authors'),
                   model_uri=EVORA.authors, domain=None, range=Optional[str])

slots.abstract = Slot(uri=EVORA.abstract, name="abstract", curie=EVORA.curie('abstract'),
                   model_uri=EVORA.abstract, domain=None, range=Optional[str])

slots.relatedDOI = Slot(uri=EVORA.relatedDOI, name="relatedDOI", curie=EVORA.curie('relatedDOI'),
                   model_uri=EVORA.relatedDOI, domain=None, range=Optional[str])

slots.journal = Slot(uri=EVORA.journal, name="journal", curie=EVORA.curie('journal'),
                   model_uri=EVORA.journal, domain=None, range=Optional[str])

slots.termDataProvider = Slot(uri=EVORA.termDataProvider, name="termDataProvider", curie=EVORA.curie('termDataProvider'),
                   model_uri=EVORA.termDataProvider, domain=None, range=Optional[str])

slots.term = Slot(uri=EVORA.term, name="term", curie=EVORA.curie('term'),
                   model_uri=EVORA.term, domain=None, range=Optional[str])

slots.inVocabulary = Slot(uri=EVORA.inVocabulary, name="inVocabulary", curie=EVORA.curie('inVocabulary'),
                   model_uri=EVORA.inVocabulary, domain=None, range=Optional[str])

slots.alternateName = Slot(uri=EVORA.alternateName, name="alternateName", curie=EVORA.curie('alternateName'),
                   model_uri=EVORA.alternateName, domain=None, range=Optional[str])

slots.sourceOfInformation = Slot(uri=EVORA.sourceOfInformation, name="sourceOfInformation", curie=EVORA.curie('sourceOfInformation'),
                   model_uri=EVORA.sourceOfInformation, domain=None, range=Optional[str])

slots.parentCategory = Slot(uri=EVORA.parentCategory, name="parentCategory", curie=EVORA.curie('parentCategory'),
                   model_uri=EVORA.parentCategory, domain=None, range=Optional[str])

slots.alpha2Code = Slot(uri=EVORA.alpha2Code, name="alpha2Code", curie=EVORA.curie('alpha2Code'),
                   model_uri=EVORA.alpha2Code, domain=None, range=Optional[str])

slots.taxonomy = Slot(uri=EVORA.taxonomy, name="taxonomy", curie=EVORA.curie('taxonomy'),
                   model_uri=EVORA.taxonomy, domain=None, range=Optional[str])

slots.parentTaxon = Slot(uri=EVORA.parentTaxon, name="parentTaxon", curie=EVORA.curie('parentTaxon'),
                   model_uri=EVORA.parentTaxon, domain=None, range=Optional[str])

slots.previouslyKnownAs = Slot(uri=EVORA.previouslyKnownAs, name="previouslyKnownAs", curie=EVORA.curie('previouslyKnownAs'),
                   model_uri=EVORA.previouslyKnownAs, domain=None, range=Optional[str])

slots.externalEquivalentTaxon = Slot(uri=EVORA.externalEquivalentTaxon, name="externalEquivalentTaxon", curie=EVORA.curie('externalEquivalentTaxon'),
                   model_uri=EVORA.externalEquivalentTaxon, domain=None, range=Optional[str])

slots.taxonomicID = Slot(uri=EVORA.taxonomicID, name="taxonomicID", curie=EVORA.curie('taxonomicID'),
                   model_uri=EVORA.taxonomicID, domain=None, range=Optional[str])

slots.taxonomicNodeID = Slot(uri=EVORA.taxonomicNodeID, name="taxonomicNodeID", curie=EVORA.curie('taxonomicNodeID'),
                   model_uri=EVORA.taxonomicNodeID, domain=None, range=Optional[str])

slots.reference = Slot(uri=EVORA.reference, name="reference", curie=EVORA.curie('reference'),
                   model_uri=EVORA.reference, domain=None, range=Optional[str])

slots.referenceLabel = Slot(uri=EVORA.referenceLabel, name="referenceLabel", curie=EVORA.curie('referenceLabel'),
                   model_uri=EVORA.referenceLabel, domain=None, range=Optional[str])

slots.referenceProviderPrefix = Slot(uri=EVORA.referenceProviderPrefix, name="referenceProviderPrefix", curie=EVORA.curie('referenceProviderPrefix'),
                   model_uri=EVORA.referenceProviderPrefix, domain=None, range=Optional[str])

slots.referenceProviderName = Slot(uri=EVORA.referenceProviderName, name="referenceProviderName", curie=EVORA.curie('referenceProviderName'),
                   model_uri=EVORA.referenceProviderName, domain=None, range=Optional[str])

slots.sequenceReference = Slot(uri=EVORA.sequenceReference, name="sequenceReference", curie=EVORA.curie('sequenceReference'),
                   model_uri=EVORA.sequenceReference, domain=None, range=Optional[str])

slots.sequenceFASTA = Slot(uri=EVORA.sequenceFASTA, name="sequenceFASTA", curie=EVORA.curie('sequenceFASTA'),
                   model_uri=EVORA.sequenceFASTA, domain=None, range=Optional[str])

slots.accessionNumber = Slot(uri=EVORA.accessionNumber, name="accessionNumber", curie=EVORA.curie('accessionNumber'),
                   model_uri=EVORA.accessionNumber, domain=None, range=Optional[str])

slots.sequenceProvider = Slot(uri=EVORA.sequenceProvider, name="sequenceProvider", curie=EVORA.curie('sequenceProvider'),
                   model_uri=EVORA.sequenceProvider, domain=None, range=Optional[str])

slots.homePage = Slot(uri=EVORA.homePage, name="homePage", curie=EVORA.curie('homePage'),
                   model_uri=EVORA.homePage, domain=None, range=Optional[str])

slots.contactPoint = Slot(uri=EVORA.contactPoint, name="contactPoint", curie=EVORA.curie('contactPoint'),
                   model_uri=EVORA.contactPoint, domain=None, range=Optional[str])

slots.logo = Slot(uri=EVORA.logo, name="logo", curie=EVORA.curie('logo'),
                   model_uri=EVORA.logo, domain=None, range=Optional[str])

slots.oRCIDiD = Slot(uri=EVORA.oRCIDiD, name="oRCIDiD", curie=EVORA.curie('oRCIDiD'),
                   model_uri=EVORA.oRCIDiD, domain=None, range=Optional[str])

slots.country = Slot(uri=EVORA.country, name="country", curie=EVORA.curie('country'),
                   model_uri=EVORA.country, domain=None, range=Optional[str])

slots.memberOfRI = Slot(uri=EVORA.memberOfRI, name="memberOfRI", curie=EVORA.curie('memberOfRI'),
                   model_uri=EVORA.memberOfRI, domain=None, range=Optional[str])

slots.recombinantMaterial = Slot(uri=EVORA.recombinantMaterial, name="recombinantMaterial", curie=EVORA.curie('recombinantMaterial'),
                   model_uri=EVORA.recombinantMaterial, domain=None, range=Optional[str])

slots.biologicalSourceType = Slot(uri=EVORA.biologicalSourceType, name="biologicalSourceType", curie=EVORA.curie('biologicalSourceType'),
                   model_uri=EVORA.biologicalSourceType, domain=None, range=Optional[str])

slots.biologicalPartOrigin = Slot(uri=EVORA.biologicalPartOrigin, name="biologicalPartOrigin", curie=EVORA.curie('biologicalPartOrigin'),
                   model_uri=EVORA.biologicalPartOrigin, domain=None, range=Optional[str])

slots.recombinantPartIdentification = Slot(uri=EVORA.recombinantPartIdentification, name="recombinantPartIdentification", curie=EVORA.curie('recombinantPartIdentification'),
                   model_uri=EVORA.recombinantPartIdentification, domain=None, range=Optional[str])

slots.accessToPhysicalGeneticResource = Slot(uri=EVORA.accessToPhysicalGeneticResource, name="accessToPhysicalGeneticResource", curie=EVORA.curie('accessToPhysicalGeneticResource'),
                   model_uri=EVORA.accessToPhysicalGeneticResource, domain=None, range=Optional[str])

slots.countryOfCollection = Slot(uri=EVORA.countryOfCollection, name="countryOfCollection", curie=EVORA.curie('countryOfCollection'),
                   model_uri=EVORA.countryOfCollection, domain=None, range=Optional[str])

slots.indigenousPoepleAndLocalCommunityOrigin = Slot(uri=EVORA.indigenousPoepleAndLocalCommunityOrigin, name="indigenousPoepleAndLocalCommunityOrigin", curie=EVORA.curie('indigenousPoepleAndLocalCommunityOrigin'),
                   model_uri=EVORA.indigenousPoepleAndLocalCommunityOrigin, domain=None, range=Optional[str])

slots.collectionDate = Slot(uri=EVORA.collectionDate, name="collectionDate", curie=EVORA.curie('collectionDate'),
                   model_uri=EVORA.collectionDate, domain=None, range=Optional[str])

slots.beforeDate = Slot(uri=EVORA.beforeDate, name="beforeDate", curie=EVORA.curie('beforeDate'),
                   model_uri=EVORA.beforeDate, domain=None, range=Optional[str])

slots.permitIdentifierForABS = Slot(uri=EVORA.permitIdentifierForABS, name="permitIdentifierForABS", curie=EVORA.curie('permitIdentifierForABS'),
                   model_uri=EVORA.permitIdentifierForABS, domain=None, range=Optional[str])

slots.modificationsFromTheReferenceSequences = Slot(uri=EVORA.modificationsFromTheReferenceSequences, name="modificationsFromTheReferenceSequences", curie=EVORA.curie('modificationsFromTheReferenceSequences'),
                   model_uri=EVORA.modificationsFromTheReferenceSequences, domain=None, range=Optional[str])

slots.descriptionOfModificationsMadeFromTheReferenceSequences = Slot(uri=EVORA.descriptionOfModificationsMadeFromTheReferenceSequences, name="descriptionOfModificationsMadeFromTheReferenceSequences", curie=EVORA.curie('descriptionOfModificationsMadeFromTheReferenceSequences'),
                   model_uri=EVORA.descriptionOfModificationsMadeFromTheReferenceSequences, domain=None, range=Optional[str])

slots.partIdentification = Slot(uri=EVORA.partIdentification, name="partIdentification", curie=EVORA.curie('partIdentification'),
                   model_uri=EVORA.partIdentification, domain=None, range=Optional[str])

slots.sequence = Slot(uri=EVORA.sequence, name="sequence", curie=EVORA.curie('sequence'),
                   model_uri=EVORA.sequence, domain=None, range=Optional[str])

slots.collectionItem = Slot(uri=EVORA.collectionItem, name="collectionItem", curie=EVORA.curie('collectionItem'),
                   model_uri=EVORA.collectionItem, domain=None, range=Optional[str])

slots.collectionDataProvider = Slot(uri=EVORA.collectionDataProvider, name="collectionDataProvider", curie=EVORA.curie('collectionDataProvider'),
                   model_uri=EVORA.collectionDataProvider, domain=None, range=Optional[str])

slots.accessPointURL = Slot(uri=EVORA.accessPointURL, name="accessPointURL", curie=EVORA.curie('accessPointURL'),
                   model_uri=EVORA.accessPointURL, domain=None, range=Optional[str])

slots.refSKU = Slot(uri=EVORA.refSKU, name="refSKU", curie=EVORA.curie('refSKU'),
                   model_uri=EVORA.refSKU, domain=None, range=Optional[str])

slots.unitDefinition = Slot(uri=EVORA.unitDefinition, name="unitDefinition", curie=EVORA.curie('unitDefinition'),
                   model_uri=EVORA.unitDefinition, domain=None, range=Optional[str])

slots.category = Slot(uri=EVORA.category, name="category", curie=EVORA.curie('category'),
                   model_uri=EVORA.category, domain=None, range=Optional[str])

slots.additionalCategory = Slot(uri=EVORA.additionalCategory, name="additionalCategory", curie=EVORA.curie('additionalCategory'),
                   model_uri=EVORA.additionalCategory, domain=None, range=Optional[str])

slots.unitCost = Slot(uri=EVORA.unitCost, name="unitCost", curie=EVORA.curie('unitCost'),
                   model_uri=EVORA.unitCost, domain=None, range=Optional[str])

slots.qualityGrading = Slot(uri=EVORA.qualityGrading, name="qualityGrading", curie=EVORA.curie('qualityGrading'),
                   model_uri=EVORA.qualityGrading, domain=None, range=Optional[str])

slots.pathogenIdentification = Slot(uri=EVORA.pathogenIdentification, name="pathogenIdentification", curie=EVORA.curie('pathogenIdentification'),
                   model_uri=EVORA.pathogenIdentification, domain=None, range=Optional[str])

slots.riskGroup = Slot(uri=EVORA.riskGroup, name="riskGroup", curie=EVORA.curie('riskGroup'),
                   model_uri=EVORA.riskGroup, domain=None, range=Optional[str])

slots.biosafetyRestrictions = Slot(uri=EVORA.biosafetyRestrictions, name="biosafetyRestrictions", curie=EVORA.curie('biosafetyRestrictions'),
                   model_uri=EVORA.biosafetyRestrictions, domain=None, range=Optional[str])

slots.canItBeUsedToProduceGMO = Slot(uri=EVORA.canItBeUsedToProduceGMO, name="canItBeUsedToProduceGMO", curie=EVORA.curie('canItBeUsedToProduceGMO'),
                   model_uri=EVORA.canItBeUsedToProduceGMO, domain=None, range=Optional[str])

slots.provider = Slot(uri=EVORA.provider, name="provider", curie=EVORA.curie('provider'),
                   model_uri=EVORA.provider, domain=None, range=Optional[str])

slots.collection = Slot(uri=EVORA.collection, name="collection", curie=EVORA.curie('collection'),
                   model_uri=EVORA.collection, domain=None, range=Optional[str])

slots.keywords = Slot(uri=EVORA.keywords, name="keywords", curie=EVORA.curie('keywords'),
                   model_uri=EVORA.keywords, domain=None, range=Optional[str])

slots.availability = Slot(uri=EVORA.availability, name="availability", curie=EVORA.curie('availability'),
                   model_uri=EVORA.availability, domain=None, range=Optional[str])

slots.complementaryDocument = Slot(uri=EVORA.complementaryDocument, name="complementaryDocument", curie=EVORA.curie('complementaryDocument'),
                   model_uri=EVORA.complementaryDocument, domain=None, range=Optional[str])

slots.technicalRecommendation = Slot(uri=EVORA.technicalRecommendation, name="technicalRecommendation", curie=EVORA.curie('technicalRecommendation'),
                   model_uri=EVORA.technicalRecommendation, domain=None, range=Optional[str])

slots.productPicture = Slot(uri=EVORA.productPicture, name="productPicture", curie=EVORA.curie('productPicture'),
                   model_uri=EVORA.productPicture, domain=None, range=Optional[str])

slots.externalRelatedReference = Slot(uri=EVORA.externalRelatedReference, name="externalRelatedReference", curie=EVORA.curie('externalRelatedReference'),
                   model_uri=EVORA.externalRelatedReference, domain=None, range=Optional[str])

slots.certification = Slot(uri=EVORA.certification, name="certification", curie=EVORA.curie('certification'),
                   model_uri=EVORA.certification, domain=None, range=Optional[str])

slots.internalReference = Slot(uri=EVORA.internalReference, name="internalReference", curie=EVORA.curie('internalReference'),
                   model_uri=EVORA.internalReference, domain=None, range=Optional[str])

slots.note = Slot(uri=EVORA.note, name="note", curie=EVORA.curie('note'),
                   model_uri=EVORA.note, domain=None, range=Optional[str])

slots.modelSpecies = Slot(uri=EVORA.modelSpecies, name="modelSpecies", curie=EVORA.curie('modelSpecies'),
                   model_uri=EVORA.modelSpecies, domain=None, range=Optional[str])

slots.modelType = Slot(uri=EVORA.modelType, name="modelType", curie=EVORA.curie('modelType'),
                   model_uri=EVORA.modelType, domain=None, range=Optional[str])

slots.hasIATAClassification = Slot(uri=EVORA.hasIATAClassification, name="hasIATAClassification", curie=EVORA.curie('hasIATAClassification'),
                   model_uri=EVORA.hasIATAClassification, domain=None, range=Optional[str])

slots.shippingConditions = Slot(uri=EVORA.shippingConditions, name="shippingConditions", curie=EVORA.curie('shippingConditions'),
                   model_uri=EVORA.shippingConditions, domain=None, range=Optional[str])

slots.materialSafetyDataSheet = Slot(uri=EVORA.materialSafetyDataSheet, name="materialSafetyDataSheet", curie=EVORA.curie('materialSafetyDataSheet'),
                   model_uri=EVORA.materialSafetyDataSheet, domain=None, range=Optional[str])

slots.originator = Slot(uri=EVORA.originator, name="originator", curie=EVORA.curie('originator'),
                   model_uri=EVORA.originator, domain=None, range=Optional[str])

slots.storageConditions = Slot(uri=EVORA.storageConditions, name="storageConditions", curie=EVORA.curie('storageConditions'),
                   model_uri=EVORA.storageConditions, domain=None, range=Optional[str])

slots.thirdPartyDistributionConsent = Slot(uri=EVORA.thirdPartyDistributionConsent, name="thirdPartyDistributionConsent", curie=EVORA.curie('thirdPartyDistributionConsent'),
                   model_uri=EVORA.thirdPartyDistributionConsent, domain=None, range=Optional[str])

slots.usageRestrictions = Slot(uri=EVORA.usageRestrictions, name="usageRestrictions", curie=EVORA.curie('usageRestrictions'),
                   model_uri=EVORA.usageRestrictions, domain=None, range=Optional[str])

slots.productionSystem = Slot(uri=EVORA.productionSystem, name="productionSystem", curie=EVORA.curie('productionSystem'),
                   model_uri=EVORA.productionSystem, domain=None, range=Optional[str])

slots.antibodyPurifiedByAffinity = Slot(uri=EVORA.antibodyPurifiedByAffinity, name="antibodyPurifiedByAffinity", curie=EVORA.curie('antibodyPurifiedByAffinity'),
                   model_uri=EVORA.antibodyPurifiedByAffinity, domain=None, range=Optional[str])

slots.specificityDocumented = Slot(uri=EVORA.specificityDocumented, name="specificityDocumented", curie=EVORA.curie('specificityDocumented'),
                   model_uri=EVORA.specificityDocumented, domain=None, range=Optional[str])

slots.targetedAntigen = Slot(uri=EVORA.targetedAntigen, name="targetedAntigen", curie=EVORA.curie('targetedAntigen'),
                   model_uri=EVORA.targetedAntigen, domain=None, range=Optional[str])

slots.hybridomaDescription = Slot(uri=EVORA.hybridomaDescription, name="hybridomaDescription", curie=EVORA.curie('hybridomaDescription'),
                   model_uri=EVORA.hybridomaDescription, domain=None, range=Optional[str])

slots.biologicalMaterialOrigin = Slot(uri=EVORA.biologicalMaterialOrigin, name="biologicalMaterialOrigin", curie=EVORA.curie('biologicalMaterialOrigin'),
                   model_uri=EVORA.biologicalMaterialOrigin, domain=None, range=Optional[str])

slots.relatedPDB = Slot(uri=EVORA.relatedPDB, name="relatedPDB", curie=EVORA.curie('relatedPDB'),
                   model_uri=EVORA.relatedPDB, domain=None, range=Optional[str])

slots.specialFeature = Slot(uri=EVORA.specialFeature, name="specialFeature", curie=EVORA.curie('specialFeature'),
                   model_uri=EVORA.specialFeature, domain=None, range=Optional[str])

slots.proteinTAG = Slot(uri=EVORA.proteinTAG, name="proteinTAG", curie=EVORA.curie('proteinTAG'),
                   model_uri=EVORA.proteinTAG, domain=None, range=Optional[str])

slots.domain = Slot(uri=EVORA.domain, name="domain", curie=EVORA.curie('domain'),
                   model_uri=EVORA.domain, domain=None, range=Optional[str])

slots.expressedAs = Slot(uri=EVORA.expressedAs, name="expressedAs", curie=EVORA.curie('expressedAs'),
                   model_uri=EVORA.expressedAs, domain=None, range=Optional[str])

slots.inclusionBodiesType = Slot(uri=EVORA.inclusionBodiesType, name="inclusionBodiesType", curie=EVORA.curie('inclusionBodiesType'),
                   model_uri=EVORA.inclusionBodiesType, domain=None, range=Optional[str])

slots.expressionSystem = Slot(uri=EVORA.expressionSystem, name="expressionSystem", curie=EVORA.curie('expressionSystem'),
                   model_uri=EVORA.expressionSystem, domain=None, range=Optional[str])

slots.functionalCharacterization = Slot(uri=EVORA.functionalCharacterization, name="functionalCharacterization", curie=EVORA.curie('functionalCharacterization'),
                   model_uri=EVORA.functionalCharacterization, domain=None, range=Optional[str])

slots.functionalTechnicalDescription = Slot(uri=EVORA.functionalTechnicalDescription, name="functionalTechnicalDescription", curie=EVORA.curie('functionalTechnicalDescription'),
                   model_uri=EVORA.functionalTechnicalDescription, domain=None, range=Optional[str])

slots.proteinPurification = Slot(uri=EVORA.proteinPurification, name="proteinPurification", curie=EVORA.curie('proteinPurification'),
                   model_uri=EVORA.proteinPurification, domain=None, range=Optional[str])

slots.theTAGStatusOfTheSolubilizedProtein = Slot(uri=EVORA.theTAGStatusOfTheSolubilizedProtein, name="theTAGStatusOfTheSolubilizedProtein", curie=EVORA.curie('theTAGStatusOfTheSolubilizedProtein'),
                   model_uri=EVORA.theTAGStatusOfTheSolubilizedProtein, domain=None, range=Optional[str])

slots.typeOfFunctionalCharacterization = Slot(uri=EVORA.typeOfFunctionalCharacterization, name="typeOfFunctionalCharacterization", curie=EVORA.curie('typeOfFunctionalCharacterization'),
                   model_uri=EVORA.typeOfFunctionalCharacterization, domain=None, range=Optional[str])

slots.hasGbFileOfTheConstruct = Slot(uri=EVORA.hasGbFileOfTheConstruct, name="hasGbFileOfTheConstruct", curie=EVORA.curie('hasGbFileOfTheConstruct'),
                   model_uri=EVORA.hasGbFileOfTheConstruct, domain=None, range=Optional[str])

slots.isItAClonedNucleicAcid = Slot(uri=EVORA.isItAClonedNucleicAcid, name="isItAClonedNucleicAcid", curie=EVORA.curie('isItAClonedNucleicAcid'),
                   model_uri=EVORA.isItAClonedNucleicAcid, domain=None, range=Optional[str])

slots.clonedIntoPlasmid = Slot(uri=EVORA.clonedIntoPlasmid, name="clonedIntoPlasmid", curie=EVORA.curie('clonedIntoPlasmid'),
                   model_uri=EVORA.clonedIntoPlasmid, domain=None, range=Optional[str])

slots.pasmidSelection = Slot(uri=EVORA.pasmidSelection, name="pasmidSelection", curie=EVORA.curie('pasmidSelection'),
                   model_uri=EVORA.pasmidSelection, domain=None, range=Optional[str])

slots.hasTAG = Slot(uri=EVORA.hasTAG, name="hasTAG", curie=EVORA.curie('hasTAG'),
                   model_uri=EVORA.hasTAG, domain=None, range=Optional[str])

slots.regionEncompassedInThisProduct = Slot(uri=EVORA.regionEncompassedInThisProduct, name="regionEncompassedInThisProduct", curie=EVORA.curie('regionEncompassedInThisProduct'),
                   model_uri=EVORA.regionEncompassedInThisProduct, domain=None, range=Optional[str])

slots.mutationObserved = Slot(uri=EVORA.mutationObserved, name="mutationObserved", curie=EVORA.curie('mutationObserved'),
                   model_uri=EVORA.mutationObserved, domain=None, range=Optional[str])

slots.observedMutations = Slot(uri=EVORA.observedMutations, name="observedMutations", curie=EVORA.curie('observedMutations'),
                   model_uri=EVORA.observedMutations, domain=None, range=Optional[str])

slots.identificationTechnique = Slot(uri=EVORA.identificationTechnique, name="identificationTechnique", curie=EVORA.curie('identificationTechnique'),
                   model_uri=EVORA.identificationTechnique, domain=None, range=Optional[str])

slots.sequencing = Slot(uri=EVORA.sequencing, name="sequencing", curie=EVORA.curie('sequencing'),
                   model_uri=EVORA.sequencing, domain=None, range=Optional[str])

slots.titer = Slot(uri=EVORA.titer, name="titer", curie=EVORA.curie('titer'),
                   model_uri=EVORA.titer, domain=None, range=Optional[str])

slots.sequenceChecked = Slot(uri=EVORA.sequenceChecked, name="sequenceChecked", curie=EVORA.curie('sequenceChecked'),
                   model_uri=EVORA.sequenceChecked, domain=None, range=Optional[str])

slots.hasSOPFile = Slot(uri=EVORA.hasSOPFile, name="hasSOPFile", curie=EVORA.curie('hasSOPFile'),
                   model_uri=EVORA.hasSOPFile, domain=None, range=Optional[str])

slots.specificity = Slot(uri=EVORA.specificity, name="specificity", curie=EVORA.curie('specificity'),
                   model_uri=EVORA.specificity, domain=None, range=Optional[str])

slots.targetedRegion = Slot(uri=EVORA.targetedRegion, name="targetedRegion", curie=EVORA.curie('targetedRegion'),
                   model_uri=EVORA.targetedRegion, domain=None, range=Optional[str])

slots.productsOfTheBundle = Slot(uri=EVORA.productsOfTheBundle, name="productsOfTheBundle", curie=EVORA.curie('productsOfTheBundle'),
                   model_uri=EVORA.productsOfTheBundle, domain=None, range=Optional[str])

slots.suspectedEpidemiologicalOrigin = Slot(uri=EVORA.suspectedEpidemiologicalOrigin, name="suspectedEpidemiologicalOrigin", curie=EVORA.curie('suspectedEpidemiologicalOrigin'),
                   model_uri=EVORA.suspectedEpidemiologicalOrigin, domain=None, range=Optional[str])

slots.isolationHost = Slot(uri=EVORA.isolationHost, name="isolationHost", curie=EVORA.curie('isolationHost'),
                   model_uri=EVORA.isolationHost, domain=None, range=Optional[str])

slots.productionCellLine = Slot(uri=EVORA.productionCellLine, name="productionCellLine", curie=EVORA.curie('productionCellLine'),
                   model_uri=EVORA.productionCellLine, domain=None, range=Optional[str])

slots.propagationHost = Slot(uri=EVORA.propagationHost, name="propagationHost", curie=EVORA.curie('propagationHost'),
                   model_uri=EVORA.propagationHost, domain=None, range=Optional[str])

slots.transmissionMethod = Slot(uri=EVORA.transmissionMethod, name="transmissionMethod", curie=EVORA.curie('transmissionMethod'),
                   model_uri=EVORA.transmissionMethod, domain=None, range=Optional[str])

slots.cultivability = Slot(uri=EVORA.cultivability, name="cultivability", curie=EVORA.curie('cultivability'),
                   model_uri=EVORA.cultivability, domain=None, range=Optional[str])

slots.clinicalInformation = Slot(uri=EVORA.clinicalInformation, name="clinicalInformation", curie=EVORA.curie('clinicalInformation'),
                   model_uri=EVORA.clinicalInformation, domain=None, range=Optional[str])

slots.infectivity = Slot(uri=EVORA.infectivity, name="infectivity", curie=EVORA.curie('infectivity'),
                   model_uri=EVORA.infectivity, domain=None, range=Optional[str])

slots.infectivityTest = Slot(uri=EVORA.infectivityTest, name="infectivityTest", curie=EVORA.curie('infectivityTest'),
                   model_uri=EVORA.infectivityTest, domain=None, range=Optional[str])

slots.isolationTechnique = Slot(uri=EVORA.isolationTechnique, name="isolationTechnique", curie=EVORA.curie('isolationTechnique'),
                   model_uri=EVORA.isolationTechnique, domain=None, range=Optional[str])

slots.isolationConditions = Slot(uri=EVORA.isolationConditions, name="isolationConditions", curie=EVORA.curie('isolationConditions'),
                   model_uri=EVORA.isolationConditions, domain=None, range=Optional[str])

slots.letterOfAuthority = Slot(uri=EVORA.letterOfAuthority, name="letterOfAuthority", curie=EVORA.curie('letterOfAuthority'),
                   model_uri=EVORA.letterOfAuthority, domain=None, range=Optional[str])

slots.passage = Slot(uri=EVORA.passage, name="passage", curie=EVORA.curie('passage'),
                   model_uri=EVORA.passage, domain=None, range=Optional[str])

slots.coInfectingViruses = Slot(uri=EVORA.coInfectingViruses, name="coInfectingViruses", curie=EVORA.curie('coInfectingViruses'),
                   model_uri=EVORA.coInfectingViruses, domain=None, range=Optional[str])

slots.contaminationWithCoInfectingViruses = Slot(uri=EVORA.contaminationWithCoInfectingViruses, name="contaminationWithCoInfectingViruses", curie=EVORA.curie('contaminationWithCoInfectingViruses'),
                   model_uri=EVORA.contaminationWithCoInfectingViruses, domain=None, range=Optional[str])

slots.mycoplasmicContent = Slot(uri=EVORA.mycoplasmicContent, name="mycoplasmicContent", curie=EVORA.curie('mycoplasmicContent'),
                   model_uri=EVORA.mycoplasmicContent, domain=None, range=Optional[str])

slots.msdsContact = Slot(uri=EVORA.msdsContact, name="msdsContact", curie=EVORA.curie('msdsContact'),
                   model_uri=EVORA.msdsContact, domain=None, range=Optional[str])

slots.physicalChemicalProperties = Slot(uri=EVORA.physicalChemicalProperties, name="physicalChemicalProperties", curie=EVORA.curie('physicalChemicalProperties'),
                   model_uri=EVORA.physicalChemicalProperties, domain=None, range=Optional[str])

slots.hazardsIdentification = Slot(uri=EVORA.hazardsIdentification, name="hazardsIdentification", curie=EVORA.curie('hazardsIdentification'),
                   model_uri=EVORA.hazardsIdentification, domain=None, range=Optional[str])

slots.firstAidMeasures = Slot(uri=EVORA.firstAidMeasures, name="firstAidMeasures", curie=EVORA.curie('firstAidMeasures'),
                   model_uri=EVORA.firstAidMeasures, domain=None, range=Optional[str])

slots.fireFightingMeasures = Slot(uri=EVORA.fireFightingMeasures, name="fireFightingMeasures", curie=EVORA.curie('fireFightingMeasures'),
                   model_uri=EVORA.fireFightingMeasures, domain=None, range=Optional[str])

slots.accidentalReleaseMeasures = Slot(uri=EVORA.accidentalReleaseMeasures, name="accidentalReleaseMeasures", curie=EVORA.curie('accidentalReleaseMeasures'),
                   model_uri=EVORA.accidentalReleaseMeasures, domain=None, range=Optional[str])

slots.handlingAndStorage = Slot(uri=EVORA.handlingAndStorage, name="handlingAndStorage", curie=EVORA.curie('handlingAndStorage'),
                   model_uri=EVORA.handlingAndStorage, domain=None, range=Optional[str])

slots.exposureControlsPersonalProtection = Slot(uri=EVORA.exposureControlsPersonalProtection, name="exposureControlsPersonalProtection", curie=EVORA.curie('exposureControlsPersonalProtection'),
                   model_uri=EVORA.exposureControlsPersonalProtection, domain=None, range=Optional[str])

slots.stabilityAndReactivity = Slot(uri=EVORA.stabilityAndReactivity, name="stabilityAndReactivity", curie=EVORA.curie('stabilityAndReactivity'),
                   model_uri=EVORA.stabilityAndReactivity, domain=None, range=Optional[str])

slots.toxicologicalInformation = Slot(uri=EVORA.toxicologicalInformation, name="toxicologicalInformation", curie=EVORA.curie('toxicologicalInformation'),
                   model_uri=EVORA.toxicologicalInformation, domain=None, range=Optional[str])

slots.ecologicalInformation = Slot(uri=EVORA.ecologicalInformation, name="ecologicalInformation", curie=EVORA.curie('ecologicalInformation'),
                   model_uri=EVORA.ecologicalInformation, domain=None, range=Optional[str])

slots.disposalConsiderations = Slot(uri=EVORA.disposalConsiderations, name="disposalConsiderations", curie=EVORA.curie('disposalConsiderations'),
                   model_uri=EVORA.disposalConsiderations, domain=None, range=Optional[str])

slots.transportInformation = Slot(uri=EVORA.transportInformation, name="transportInformation", curie=EVORA.curie('transportInformation'),
                   model_uri=EVORA.transportInformation, domain=None, range=Optional[str])

slots.regulatoryInformation = Slot(uri=EVORA.regulatoryInformation, name="regulatoryInformation", curie=EVORA.curie('regulatoryInformation'),
                   model_uri=EVORA.regulatoryInformation, domain=None, range=Optional[str])

slots.furtherInformation = Slot(uri=EVORA.furtherInformation, name="furtherInformation", curie=EVORA.curie('furtherInformation'),
                   model_uri=EVORA.furtherInformation, domain=None, range=Optional[str])

slots.contentURL = Slot(uri=EVORA.contentURL, name="contentURL", curie=EVORA.curie('contentURL'),
                   model_uri=EVORA.contentURL, domain=None, range=Optional[str])

slots.format = Slot(uri=EVORA.format, name="format", curie=EVORA.curie('format'),
                   model_uri=EVORA.format, domain=None, range=Optional[str])

slots.altText = Slot(uri=EVORA.altText, name="altText", curie=EVORA.curie('altText'),
                   model_uri=EVORA.altText, domain=None, range=Optional[str])

slots.email = Slot(uri=EVORA.email, name="email", curie=EVORA.curie('email'),
                   model_uri=EVORA.email, domain=None, range=Optional[str])

slots.telephone = Slot(uri=EVORA.telephone, name="telephone", curie=EVORA.curie('telephone'),
                   model_uri=EVORA.telephone, domain=None, range=Optional[str])

slots.streetAddress = Slot(uri=EVORA.streetAddress, name="streetAddress", curie=EVORA.curie('streetAddress'),
                   model_uri=EVORA.streetAddress, domain=None, range=Optional[str])

slots.addressLocality = Slot(uri=EVORA.addressLocality, name="addressLocality", curie=EVORA.curie('addressLocality'),
                   model_uri=EVORA.addressLocality, domain=None, range=Optional[str])

slots.addressRegion = Slot(uri=EVORA.addressRegion, name="addressRegion", curie=EVORA.curie('addressRegion'),
                   model_uri=EVORA.addressRegion, domain=None, range=Optional[str])

slots.postalCode = Slot(uri=EVORA.postalCode, name="postalCode", curie=EVORA.curie('postalCode'),
                   model_uri=EVORA.postalCode, domain=None, range=Optional[str])

slots.addressCountry = Slot(uri=EVORA.addressCountry, name="addressCountry", curie=EVORA.curie('addressCountry'),
                   model_uri=EVORA.addressCountry, domain=None, range=Optional[str])

slots.resourceURL = Slot(uri=EVORA.resourceURL, name="resourceURL", curie=EVORA.curie('resourceURL'),
                   model_uri=EVORA.resourceURL, domain=None, range=Optional[str])

slots.licensingOrAttribution = Slot(uri=EVORA.licensingOrAttribution, name="licensingOrAttribution", curie=EVORA.curie('licensingOrAttribution'),
                   model_uri=EVORA.licensingOrAttribution, domain=None, range=Optional[str])

slots.certificationDocument = Slot(uri=EVORA.certificationDocument, name="certificationDocument", curie=EVORA.curie('certificationDocument'),
                   model_uri=EVORA.certificationDocument, domain=None, range=Optional[str])

slots.Version_ID = Slot(uri=EVORA.ID, name="Version_ID", curie=EVORA.curie('ID'),
                   model_uri=EVORA.Version_ID, domain=Version, range=str)

slots.Version_versionOf = Slot(uri=EVORA.versionOf, name="Version_versionOf", curie=EVORA.curie('versionOf'),
                   model_uri=EVORA.Version_versionOf, domain=Version, range=Union[str, URI])

slots.Nameable_name = Slot(uri=EVORA.name, name="Nameable_name", curie=EVORA.curie('name'),
                   model_uri=EVORA.Nameable_name, domain=Nameable, range=str)

slots.Nameable_description = Slot(uri=EVORA.description, name="Nameable_description", curie=EVORA.curie('description'),
                   model_uri=EVORA.Nameable_description, domain=Nameable, range=Optional[str])

slots.Taxonomy_taxon = Slot(uri=EVORA.taxon, name="Taxonomy_taxon", curie=EVORA.curie('taxon'),
                   model_uri=EVORA.Taxonomy_taxon, domain=Taxonomy, range=Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]])

slots.Taxonomy_taxonDataProvider = Slot(uri=EVORA.taxonDataProvider, name="Taxonomy_taxonDataProvider", curie=EVORA.curie('taxonDataProvider'),
                   model_uri=EVORA.Taxonomy_taxonDataProvider, domain=Taxonomy, range=Optional[Union[dict, "DataProvider"]])

slots.Taxonomy_version = Slot(uri=EVORA.version, name="Taxonomy_version", curie=EVORA.curie('version'),
                   model_uri=EVORA.Taxonomy_version, domain=Taxonomy, range=Union[dict, Version])

slots.Taxonomy_versionDataProvider = Slot(uri=EVORA.versionDataProvider, name="Taxonomy_versionDataProvider", curie=EVORA.curie('versionDataProvider'),
                   model_uri=EVORA.Taxonomy_versionDataProvider, domain=Taxonomy, range=Union[dict, "DataProvider"])

slots.Taxonomy_rank = Slot(uri=EVORA.rank, name="Taxonomy_rank", curie=EVORA.curie('rank'),
                   model_uri=EVORA.Taxonomy_rank, domain=Taxonomy, range=Optional[Union[Union[dict, "TaxonomicRank"], List[Union[dict, "TaxonomicRank"]]]])

slots.Taxonomy_rankDataProvider = Slot(uri=EVORA.rankDataProvider, name="Taxonomy_rankDataProvider", curie=EVORA.curie('rankDataProvider'),
                   model_uri=EVORA.Taxonomy_rankDataProvider, domain=Taxonomy, range=Optional[Union[dict, "DataProvider"]])

slots.DataProvider_license = Slot(uri=EVORA.license, name="DataProvider_license", curie=EVORA.curie('license'),
                   model_uri=EVORA.DataProvider_license, domain=DataProvider, range=Optional[Union[dict, "License"]])

slots.DataProvider_loginRequestMethod = Slot(uri=EVORA.loginRequestMethod, name="DataProvider_loginRequestMethod", curie=EVORA.curie('loginRequestMethod'),
                   model_uri=EVORA.DataProvider_loginRequestMethod, domain=DataProvider, range=Optional[str])

slots.DataProvider_loginURL = Slot(uri=EVORA.loginURL, name="DataProvider_loginURL", curie=EVORA.curie('loginURL'),
                   model_uri=EVORA.DataProvider_loginURL, domain=DataProvider, range=Optional[Union[str, URI]])

slots.DataProvider_loginTokenName = Slot(uri=EVORA.loginTokenName, name="DataProvider_loginTokenName", curie=EVORA.curie('loginTokenName'),
                   model_uri=EVORA.DataProvider_loginTokenName, domain=DataProvider, range=Optional[str])

slots.DataProvider_queryURL = Slot(uri=EVORA.queryURL, name="DataProvider_queryURL", curie=EVORA.curie('queryURL'),
                   model_uri=EVORA.DataProvider_queryURL, domain=DataProvider, range=Union[str, URI])

slots.DataProvider_queryMethod = Slot(uri=EVORA.queryMethod, name="DataProvider_queryMethod", curie=EVORA.curie('queryMethod'),
                   model_uri=EVORA.DataProvider_queryMethod, domain=DataProvider, range=str)

slots.DataProvider_contentType = Slot(uri=EVORA.contentType, name="DataProvider_contentType", curie=EVORA.curie('contentType'),
                   model_uri=EVORA.DataProvider_contentType, domain=DataProvider, range=str)

slots.DataProvider_providedEntityType = Slot(uri=EVORA.providedEntityType, name="DataProvider_providedEntityType", curie=EVORA.curie('providedEntityType'),
                   model_uri=EVORA.DataProvider_providedEntityType, domain=DataProvider, range=str)

slots.DataProvider_weight = Slot(uri=EVORA.weight, name="DataProvider_weight", curie=EVORA.curie('weight'),
                   model_uri=EVORA.DataProvider_weight, domain=DataProvider, range=int)

slots.PathogenIdentification_taxon = Slot(uri=EVORA.taxon, name="PathogenIdentification_taxon", curie=EVORA.curie('taxon'),
                   model_uri=EVORA.PathogenIdentification_taxon, domain=PathogenIdentification, range=Union[dict, "Taxon"])

slots.PathogenIdentification_pathogenName = Slot(uri=EVORA.pathogenName, name="PathogenIdentification_pathogenName", curie=EVORA.curie('pathogenName'),
                   model_uri=EVORA.PathogenIdentification_pathogenName, domain=PathogenIdentification, range=Union[dict, "CommonName"])

slots.PathogenIdentification_pathogenType = Slot(uri=EVORA.pathogenType, name="PathogenIdentification_pathogenType", curie=EVORA.curie('pathogenType'),
                   model_uri=EVORA.PathogenIdentification_pathogenType, domain=PathogenIdentification, range=str)

slots.PathogenIdentification_hostType = Slot(uri=EVORA.hostType, name="PathogenIdentification_hostType", curie=EVORA.curie('hostType'),
                   model_uri=EVORA.PathogenIdentification_hostType, domain=PathogenIdentification, range=Optional[Union[str, List[str]]])

slots.PathogenIdentification_subspecies = Slot(uri=EVORA.subspecies, name="PathogenIdentification_subspecies", curie=EVORA.curie('subspecies'),
                   model_uri=EVORA.PathogenIdentification_subspecies, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_strain = Slot(uri=EVORA.strain, name="PathogenIdentification_strain", curie=EVORA.curie('strain'),
                   model_uri=EVORA.PathogenIdentification_strain, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_isolate = Slot(uri=EVORA.isolate, name="PathogenIdentification_isolate", curie=EVORA.curie('isolate'),
                   model_uri=EVORA.PathogenIdentification_isolate, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_genotype = Slot(uri=EVORA.genotype, name="PathogenIdentification_genotype", curie=EVORA.curie('genotype'),
                   model_uri=EVORA.PathogenIdentification_genotype, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_serotype = Slot(uri=EVORA.serotype, name="PathogenIdentification_serotype", curie=EVORA.curie('serotype'),
                   model_uri=EVORA.PathogenIdentification_serotype, domain=PathogenIdentification, range=Optional[str])

slots.PathogenIdentification_variant = Slot(uri=EVORA.variant, name="PathogenIdentification_variant", curie=EVORA.curie('variant'),
                   model_uri=EVORA.PathogenIdentification_variant, domain=PathogenIdentification, range=Optional[Union[dict, "Variant"]])

slots.Publication_title = Slot(uri=EVORA.title, name="Publication_title", curie=EVORA.curie('title'),
                   model_uri=EVORA.Publication_title, domain=Publication, range=str)

slots.Publication_authors = Slot(uri=EVORA.authors, name="Publication_authors", curie=EVORA.curie('authors'),
                   model_uri=EVORA.Publication_authors, domain=Publication, range=str)

slots.Publication_abstract = Slot(uri=EVORA.abstract, name="Publication_abstract", curie=EVORA.curie('abstract'),
                   model_uri=EVORA.Publication_abstract, domain=Publication, range=str)

slots.Publication_relatedDOI = Slot(uri=EVORA.relatedDOI, name="Publication_relatedDOI", curie=EVORA.curie('relatedDOI'),
                   model_uri=EVORA.Publication_relatedDOI, domain=Publication, range=Union[dict, "DOI"])

slots.Publication_journal = Slot(uri=EVORA.journal, name="Publication_journal", curie=EVORA.curie('journal'),
                   model_uri=EVORA.Publication_journal, domain=Publication, range=Optional[Union[dict, "Journal"]])

slots.Vocabulary_termDataProvider = Slot(uri=EVORA.termDataProvider, name="Vocabulary_termDataProvider", curie=EVORA.curie('termDataProvider'),
                   model_uri=EVORA.Vocabulary_termDataProvider, domain=Vocabulary, range=Optional[Union[dict, DataProvider]])

slots.Vocabulary_term = Slot(uri=EVORA.term, name="Vocabulary_term", curie=EVORA.curie('term'),
                   model_uri=EVORA.Vocabulary_term, domain=Vocabulary, range=Optional[Union[Union[dict, "Term"], List[Union[dict, "Term"]]]])

slots.Term_weight = Slot(uri=EVORA.weight, name="Term_weight", curie=EVORA.curie('weight'),
                   model_uri=EVORA.Term_weight, domain=Term, range=int)

slots.Term_inVocabulary = Slot(uri=EVORA.inVocabulary, name="Term_inVocabulary", curie=EVORA.curie('inVocabulary'),
                   model_uri=EVORA.Term_inVocabulary, domain=Term, range=Union[dict, Vocabulary])

slots.CommonName_alternateName = Slot(uri=EVORA.alternateName, name="CommonName_alternateName", curie=EVORA.curie('alternateName'),
                   model_uri=EVORA.CommonName_alternateName, domain=CommonName, range=Optional[Union[Union[dict, "AlternateName"], List[Union[dict, "AlternateName"]]]])

slots.CommonName_sourceOfInformation = Slot(uri=EVORA.sourceOfInformation, name="CommonName_sourceOfInformation", curie=EVORA.curie('sourceOfInformation'),
                   model_uri=EVORA.CommonName_sourceOfInformation, domain=CommonName, range=Optional[Union[str, List[str]]])

slots.AlternateName_alternateName = Slot(uri=EVORA.alternateName, name="AlternateName_alternateName", curie=EVORA.curie('alternateName'),
                   model_uri=EVORA.AlternateName_alternateName, domain=AlternateName, range=Optional[Union[Union[dict, "AlternateName"], List[Union[dict, "AlternateName"]]]])

slots.AlternateName_sourceOfInformation = Slot(uri=EVORA.sourceOfInformation, name="AlternateName_sourceOfInformation", curie=EVORA.curie('sourceOfInformation'),
                   model_uri=EVORA.AlternateName_sourceOfInformation, domain=AlternateName, range=Optional[Union[str, List[str]]])

slots.ProductCategory_parentCategory = Slot(uri=EVORA.parentCategory, name="ProductCategory_parentCategory", curie=EVORA.curie('parentCategory'),
                   model_uri=EVORA.ProductCategory_parentCategory, domain=ProductCategory, range=Optional[Union[dict, "ProductCategory"]])

slots.Country_alpha2Code = Slot(uri=EVORA.alpha2Code, name="Country_alpha2Code", curie=EVORA.curie('alpha2Code'),
                   model_uri=EVORA.Country_alpha2Code, domain=Country, range=str)

slots.TaxonomicRank_taxonomy = Slot(uri=EVORA.taxonomy, name="TaxonomicRank_taxonomy", curie=EVORA.curie('taxonomy'),
                   model_uri=EVORA.TaxonomicRank_taxonomy, domain=TaxonomicRank, range=Optional[Union[Union[dict, Taxonomy], List[Union[dict, Taxonomy]]]])

slots.Taxon_taxonomy = Slot(uri=EVORA.taxonomy, name="Taxon_taxonomy", curie=EVORA.curie('taxonomy'),
                   model_uri=EVORA.Taxon_taxonomy, domain=Taxon, range=Optional[Union[Union[dict, Taxonomy], List[Union[dict, Taxonomy]]]])

slots.Taxon_parentTaxon = Slot(uri=EVORA.parentTaxon, name="Taxon_parentTaxon", curie=EVORA.curie('parentTaxon'),
                   model_uri=EVORA.Taxon_parentTaxon, domain=Taxon, range=Union[dict, "Taxon"])

slots.Taxon_rank = Slot(uri=EVORA.rank, name="Taxon_rank", curie=EVORA.curie('rank'),
                   model_uri=EVORA.Taxon_rank, domain=Taxon, range=Union[dict, TaxonomicRank])

slots.Taxon_previouslyKnownAs = Slot(uri=EVORA.previouslyKnownAs, name="Taxon_previouslyKnownAs", curie=EVORA.curie('previouslyKnownAs'),
                   model_uri=EVORA.Taxon_previouslyKnownAs, domain=Taxon, range=Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]])

slots.Taxon_externalEquivalentTaxon = Slot(uri=EVORA.externalEquivalentTaxon, name="Taxon_externalEquivalentTaxon", curie=EVORA.curie('externalEquivalentTaxon'),
                   model_uri=EVORA.Taxon_externalEquivalentTaxon, domain=Taxon, range=Optional[Union[Union[dict, "Taxon"], List[Union[dict, "Taxon"]]]])

slots.Taxon_taxonomicID = Slot(uri=EVORA.taxonomicID, name="Taxon_taxonomicID", curie=EVORA.curie('taxonomicID'),
                   model_uri=EVORA.Taxon_taxonomicID, domain=Taxon, range=str)

slots.Taxon_taxonomicNodeID = Slot(uri=EVORA.taxonomicNodeID, name="Taxon_taxonomicNodeID", curie=EVORA.curie('taxonomicNodeID'),
                   model_uri=EVORA.Taxon_taxonomicNodeID, domain=Taxon, range=Optional[str])

slots.ExternalRelatedReference_reference = Slot(uri=EVORA.reference, name="ExternalRelatedReference_reference", curie=EVORA.curie('reference'),
                   model_uri=EVORA.ExternalRelatedReference_reference, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceLabel = Slot(uri=EVORA.referenceLabel, name="ExternalRelatedReference_referenceLabel", curie=EVORA.curie('referenceLabel'),
                   model_uri=EVORA.ExternalRelatedReference_referenceLabel, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceProviderPrefix = Slot(uri=EVORA.referenceProviderPrefix, name="ExternalRelatedReference_referenceProviderPrefix", curie=EVORA.curie('referenceProviderPrefix'),
                   model_uri=EVORA.ExternalRelatedReference_referenceProviderPrefix, domain=ExternalRelatedReference, range=str)

slots.ExternalRelatedReference_referenceProviderName = Slot(uri=EVORA.referenceProviderName, name="ExternalRelatedReference_referenceProviderName", curie=EVORA.curie('referenceProviderName'),
                   model_uri=EVORA.ExternalRelatedReference_referenceProviderName, domain=ExternalRelatedReference, range=str)

slots.Sequence_sequenceReference = Slot(uri=EVORA.sequenceReference, name="Sequence_sequenceReference", curie=EVORA.curie('sequenceReference'),
                   model_uri=EVORA.Sequence_sequenceReference, domain=Sequence, range=Optional[Union[Union[dict, "SequenceReference"], List[Union[dict, "SequenceReference"]]]])

slots.Sequence_sequenceFASTA = Slot(uri=EVORA.sequenceFASTA, name="Sequence_sequenceFASTA", curie=EVORA.curie('sequenceFASTA'),
                   model_uri=EVORA.Sequence_sequenceFASTA, domain=Sequence, range=Optional[str])

slots.SequenceReference_accessionNumber = Slot(uri=EVORA.accessionNumber, name="SequenceReference_accessionNumber", curie=EVORA.curie('accessionNumber'),
                   model_uri=EVORA.SequenceReference_accessionNumber, domain=SequenceReference, range=str)

slots.SequenceReference_sequenceProvider = Slot(uri=EVORA.sequenceProvider, name="SequenceReference_sequenceProvider", curie=EVORA.curie('sequenceProvider'),
                   model_uri=EVORA.SequenceReference_sequenceProvider, domain=SequenceReference, range=str)

slots.PersonOrOrganization_homePage = Slot(uri=EVORA.homePage, name="PersonOrOrganization_homePage", curie=EVORA.curie('homePage'),
                   model_uri=EVORA.PersonOrOrganization_homePage, domain=PersonOrOrganization, range=Optional[str])

slots.PersonOrOrganization_contactPoint = Slot(uri=EVORA.contactPoint, name="PersonOrOrganization_contactPoint", curie=EVORA.curie('contactPoint'),
                   model_uri=EVORA.PersonOrOrganization_contactPoint, domain=PersonOrOrganization, range=Optional[Union[dict, "ContactPoint"]])

slots.PersonOrOrganization_logo = Slot(uri=EVORA.logo, name="PersonOrOrganization_logo", curie=EVORA.curie('logo'),
                   model_uri=EVORA.PersonOrOrganization_logo, domain=PersonOrOrganization, range=Optional[Union[dict, "Image"]])

slots.Person_oRCIDiD = Slot(uri=EVORA.oRCIDiD, name="Person_oRCIDiD", curie=EVORA.curie('oRCIDiD'),
                   model_uri=EVORA.Person_oRCIDiD, domain=Person, range=Optional[str])

slots.Organization_alternateName = Slot(uri=EVORA.alternateName, name="Organization_alternateName", curie=EVORA.curie('alternateName'),
                   model_uri=EVORA.Organization_alternateName, domain=Organization, range=Optional[Union[dict, AlternateName]])

slots.Organization_country = Slot(uri=EVORA.country, name="Organization_country", curie=EVORA.curie('country'),
                   model_uri=EVORA.Organization_country, domain=Organization, range=Optional[Union[dict, Country]])

slots.Provider_memberOfRI = Slot(uri=EVORA.memberOfRI, name="Provider_memberOfRI", curie=EVORA.curie('memberOfRI'),
                   model_uri=EVORA.Provider_memberOfRI, domain=Provider, range=Optional[Union[Union[dict, RI], List[Union[dict, RI]]]])

slots.BiologicalMaterialOrigin_recombinantMaterial = Slot(uri=EVORA.recombinantMaterial, name="BiologicalMaterialOrigin_recombinantMaterial", curie=EVORA.curie('recombinantMaterial'),
                   model_uri=EVORA.BiologicalMaterialOrigin_recombinantMaterial, domain=BiologicalMaterialOrigin, range=Union[bool, Bool])

slots.BiologicalMaterialOrigin_biologicalSourceType = Slot(uri=EVORA.biologicalSourceType, name="BiologicalMaterialOrigin_biologicalSourceType", curie=EVORA.curie('biologicalSourceType'),
                   model_uri=EVORA.BiologicalMaterialOrigin_biologicalSourceType, domain=BiologicalMaterialOrigin, range=Union[bool, Bool])

slots.BiologicalMaterialOrigin_biologicalPartOrigin = Slot(uri=EVORA.biologicalPartOrigin, name="BiologicalMaterialOrigin_biologicalPartOrigin", curie=EVORA.curie('biologicalPartOrigin'),
                   model_uri=EVORA.BiologicalMaterialOrigin_biologicalPartOrigin, domain=BiologicalMaterialOrigin, range=Union[Union[dict, "BiologicalPartOrigin"], List[Union[dict, "BiologicalPartOrigin"]]])

slots.BiologicalPartOrigin_recombinantPartIdentification = Slot(uri=EVORA.recombinantPartIdentification, name="BiologicalPartOrigin_recombinantPartIdentification", curie=EVORA.curie('recombinantPartIdentification'),
                   model_uri=EVORA.BiologicalPartOrigin_recombinantPartIdentification, domain=BiologicalPartOrigin, range=Optional[Union[dict, "RecombinantPartIdentification"]])

slots.BiologicalPartOrigin_accessToPhysicalGeneticResource = Slot(uri=EVORA.accessToPhysicalGeneticResource, name="BiologicalPartOrigin_accessToPhysicalGeneticResource", curie=EVORA.curie('accessToPhysicalGeneticResource'),
                   model_uri=EVORA.BiologicalPartOrigin_accessToPhysicalGeneticResource, domain=BiologicalPartOrigin, range=Union[bool, Bool])

slots.NaturalPartOrigin_countryOfCollection = Slot(uri=EVORA.countryOfCollection, name="NaturalPartOrigin_countryOfCollection", curie=EVORA.curie('countryOfCollection'),
                   model_uri=EVORA.NaturalPartOrigin_countryOfCollection, domain=NaturalPartOrigin, range=Union[dict, Country])

slots.NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin = Slot(uri=EVORA.indigenousPoepleAndLocalCommunityOrigin, name="NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin", curie=EVORA.curie('indigenousPoepleAndLocalCommunityOrigin'),
                   model_uri=EVORA.NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin, domain=NaturalPartOrigin, range=Optional[Union[dict, IPLCOrigin]])

slots.NaturalPartOrigin_collectionDate = Slot(uri=EVORA.collectionDate, name="NaturalPartOrigin_collectionDate", curie=EVORA.curie('collectionDate'),
                   model_uri=EVORA.NaturalPartOrigin_collectionDate, domain=NaturalPartOrigin, range=Union[str, XSDDateTime])

slots.NaturalPartOrigin_beforeDate = Slot(uri=EVORA.beforeDate, name="NaturalPartOrigin_beforeDate", curie=EVORA.curie('beforeDate'),
                   model_uri=EVORA.NaturalPartOrigin_beforeDate, domain=NaturalPartOrigin, range=Union[bool, Bool])

slots.NaturalPartOrigin_permitIdentifierForABS = Slot(uri=EVORA.permitIdentifierForABS, name="NaturalPartOrigin_permitIdentifierForABS", curie=EVORA.curie('permitIdentifierForABS'),
                   model_uri=EVORA.NaturalPartOrigin_permitIdentifierForABS, domain=NaturalPartOrigin, range=Optional[str])

slots.SyntheticPartOrigin_modificationsFromTheReferenceSequences = Slot(uri=EVORA.modificationsFromTheReferenceSequences, name="SyntheticPartOrigin_modificationsFromTheReferenceSequences", curie=EVORA.curie('modificationsFromTheReferenceSequences'),
                   model_uri=EVORA.SyntheticPartOrigin_modificationsFromTheReferenceSequences, domain=SyntheticPartOrigin, range=Union[bool, Bool])

slots.SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences = Slot(uri=EVORA.descriptionOfModificationsMadeFromTheReferenceSequences, name="SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences", curie=EVORA.curie('descriptionOfModificationsMadeFromTheReferenceSequences'),
                   model_uri=EVORA.SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences, domain=SyntheticPartOrigin, range=Optional[str])

slots.RecombinantPartIdentification_partIdentification = Slot(uri=EVORA.partIdentification, name="RecombinantPartIdentification_partIdentification", curie=EVORA.curie('partIdentification'),
                   model_uri=EVORA.RecombinantPartIdentification_partIdentification, domain=RecombinantPartIdentification, range=str)

slots.RecombinantPartIdentification_sequence = Slot(uri=EVORA.sequence, name="RecombinantPartIdentification_sequence", curie=EVORA.curie('sequence'),
                   model_uri=EVORA.RecombinantPartIdentification_sequence, domain=RecombinantPartIdentification, range=Union[Union[dict, Sequence], List[Union[dict, Sequence]]])

slots.Collection_collectionItem = Slot(uri=EVORA.collectionItem, name="Collection_collectionItem", curie=EVORA.curie('collectionItem'),
                   model_uri=EVORA.Collection_collectionItem, domain=Collection, range=Optional[Union[Union[dict, "ProductOrService"], List[Union[dict, "ProductOrService"]]]])

slots.Collection_collectionDataProvider = Slot(uri=EVORA.collectionDataProvider, name="Collection_collectionDataProvider", curie=EVORA.curie('collectionDataProvider'),
                   model_uri=EVORA.Collection_collectionDataProvider, domain=Collection, range=Optional[Union[dict, DataProvider]])

slots.ProductOrService_accessPointURL = Slot(uri=EVORA.accessPointURL, name="ProductOrService_accessPointURL", curie=EVORA.curie('accessPointURL'),
                   model_uri=EVORA.ProductOrService_accessPointURL, domain=ProductOrService, range=Union[str, URI])

slots.ProductOrService_refSKU = Slot(uri=EVORA.refSKU, name="ProductOrService_refSKU", curie=EVORA.curie('refSKU'),
                   model_uri=EVORA.ProductOrService_refSKU, domain=ProductOrService, range=str)

slots.ProductOrService_unitDefinition = Slot(uri=EVORA.unitDefinition, name="ProductOrService_unitDefinition", curie=EVORA.curie('unitDefinition'),
                   model_uri=EVORA.ProductOrService_unitDefinition, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_category = Slot(uri=EVORA.category, name="ProductOrService_category", curie=EVORA.curie('category'),
                   model_uri=EVORA.ProductOrService_category, domain=ProductOrService, range=Union[dict, ProductCategory])

slots.ProductOrService_additionalCategory = Slot(uri=EVORA.additionalCategory, name="ProductOrService_additionalCategory", curie=EVORA.curie('additionalCategory'),
                   model_uri=EVORA.ProductOrService_additionalCategory, domain=ProductOrService, range=Optional[Union[Union[dict, ProductCategory], List[Union[dict, ProductCategory]]]])

slots.ProductOrService_unitCost = Slot(uri=EVORA.unitCost, name="ProductOrService_unitCost", curie=EVORA.curie('unitCost'),
                   model_uri=EVORA.ProductOrService_unitCost, domain=ProductOrService, range=str)

slots.ProductOrService_qualityGrading = Slot(uri=EVORA.qualityGrading, name="ProductOrService_qualityGrading", curie=EVORA.curie('qualityGrading'),
                   model_uri=EVORA.ProductOrService_qualityGrading, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_pathogenIdentification = Slot(uri=EVORA.pathogenIdentification, name="ProductOrService_pathogenIdentification", curie=EVORA.curie('pathogenIdentification'),
                   model_uri=EVORA.ProductOrService_pathogenIdentification, domain=ProductOrService, range=Union[Union[dict, PathogenIdentification], List[Union[dict, PathogenIdentification]]])

slots.ProductOrService_relatedDOI = Slot(uri=EVORA.relatedDOI, name="ProductOrService_relatedDOI", curie=EVORA.curie('relatedDOI'),
                   model_uri=EVORA.ProductOrService_relatedDOI, domain=ProductOrService, range=Optional[Union[Union[dict, DOI], List[Union[dict, DOI]]]])

slots.ProductOrService_riskGroup = Slot(uri=EVORA.riskGroup, name="ProductOrService_riskGroup", curie=EVORA.curie('riskGroup'),
                   model_uri=EVORA.ProductOrService_riskGroup, domain=ProductOrService, range=Optional[Union[dict, RiskGroup]])

slots.ProductOrService_biosafetyRestrictions = Slot(uri=EVORA.biosafetyRestrictions, name="ProductOrService_biosafetyRestrictions", curie=EVORA.curie('biosafetyRestrictions'),
                   model_uri=EVORA.ProductOrService_biosafetyRestrictions, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_canItBeUsedToProduceGMO = Slot(uri=EVORA.canItBeUsedToProduceGMO, name="ProductOrService_canItBeUsedToProduceGMO", curie=EVORA.curie('canItBeUsedToProduceGMO'),
                   model_uri=EVORA.ProductOrService_canItBeUsedToProduceGMO, domain=ProductOrService, range=Optional[Union[bool, Bool]])

slots.ProductOrService_provider = Slot(uri=EVORA.provider, name="ProductOrService_provider", curie=EVORA.curie('provider'),
                   model_uri=EVORA.ProductOrService_provider, domain=ProductOrService, range=Union[dict, Provider])

slots.ProductOrService_collection = Slot(uri=EVORA.collection, name="ProductOrService_collection", curie=EVORA.curie('collection'),
                   model_uri=EVORA.ProductOrService_collection, domain=ProductOrService, range=Union[Union[dict, Collection], List[Union[dict, Collection]]])

slots.ProductOrService_keywords = Slot(uri=EVORA.keywords, name="ProductOrService_keywords", curie=EVORA.curie('keywords'),
                   model_uri=EVORA.ProductOrService_keywords, domain=ProductOrService, range=Union[Union[dict, Keyword], List[Union[dict, Keyword]]])

slots.ProductOrService_availability = Slot(uri=EVORA.availability, name="ProductOrService_availability", curie=EVORA.curie('availability'),
                   model_uri=EVORA.ProductOrService_availability, domain=ProductOrService, range=str)

slots.ProductOrService_complementaryDocument = Slot(uri=EVORA.complementaryDocument, name="ProductOrService_complementaryDocument", curie=EVORA.curie('complementaryDocument'),
                   model_uri=EVORA.ProductOrService_complementaryDocument, domain=ProductOrService, range=Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]])

slots.ProductOrService_technicalRecommendation = Slot(uri=EVORA.technicalRecommendation, name="ProductOrService_technicalRecommendation", curie=EVORA.curie('technicalRecommendation'),
                   model_uri=EVORA.ProductOrService_technicalRecommendation, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_productPicture = Slot(uri=EVORA.productPicture, name="ProductOrService_productPicture", curie=EVORA.curie('productPicture'),
                   model_uri=EVORA.ProductOrService_productPicture, domain=ProductOrService, range=Optional[Union[Union[dict, "Image"], List[Union[dict, "Image"]]]])

slots.ProductOrService_externalRelatedReference = Slot(uri=EVORA.externalRelatedReference, name="ProductOrService_externalRelatedReference", curie=EVORA.curie('externalRelatedReference'),
                   model_uri=EVORA.ProductOrService_externalRelatedReference, domain=ProductOrService, range=Optional[Union[Union[dict, ExternalRelatedReference], List[Union[dict, ExternalRelatedReference]]]])

slots.ProductOrService_certification = Slot(uri=EVORA.certification, name="ProductOrService_certification", curie=EVORA.curie('certification'),
                   model_uri=EVORA.ProductOrService_certification, domain=ProductOrService, range=Optional[Union[Union[dict, "Certification"], List[Union[dict, "Certification"]]]])

slots.ProductOrService_internalReference = Slot(uri=EVORA.internalReference, name="ProductOrService_internalReference", curie=EVORA.curie('internalReference'),
                   model_uri=EVORA.ProductOrService_internalReference, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_note = Slot(uri=EVORA.note, name="ProductOrService_note", curie=EVORA.curie('note'),
                   model_uri=EVORA.ProductOrService_note, domain=ProductOrService, range=Optional[str])

slots.ProductOrService_contactPoint = Slot(uri=EVORA.contactPoint, name="ProductOrService_contactPoint", curie=EVORA.curie('contactPoint'),
                   model_uri=EVORA.ProductOrService_contactPoint, domain=ProductOrService, range=Optional[Union[dict, "ContactPoint"]])

slots.Service_modelSpecies = Slot(uri=EVORA.modelSpecies, name="Service_modelSpecies", curie=EVORA.curie('modelSpecies'),
                   model_uri=EVORA.Service_modelSpecies, domain=Service, range=Optional[str])

slots.Service_modelType = Slot(uri=EVORA.modelType, name="Service_modelType", curie=EVORA.curie('modelType'),
                   model_uri=EVORA.Service_modelType, domain=Service, range=Optional[str])

slots.Product_hasIATAClassification = Slot(uri=EVORA.hasIATAClassification, name="Product_hasIATAClassification", curie=EVORA.curie('hasIATAClassification'),
                   model_uri=EVORA.Product_hasIATAClassification, domain=Product, range=Union[dict, IATAClassification])

slots.Product_shippingConditions = Slot(uri=EVORA.shippingConditions, name="Product_shippingConditions", curie=EVORA.curie('shippingConditions'),
                   model_uri=EVORA.Product_shippingConditions, domain=Product, range=str)

slots.Product_materialSafetyDataSheet = Slot(uri=EVORA.materialSafetyDataSheet, name="Product_materialSafetyDataSheet", curie=EVORA.curie('materialSafetyDataSheet'),
                   model_uri=EVORA.Product_materialSafetyDataSheet, domain=Product, range=Optional[Union[dict, "MSDS"]])

slots.Product_originator = Slot(uri=EVORA.originator, name="Product_originator", curie=EVORA.curie('originator'),
                   model_uri=EVORA.Product_originator, domain=Product, range=Optional[Union[dict, Originator]])

slots.Product_storageConditions = Slot(uri=EVORA.storageConditions, name="Product_storageConditions", curie=EVORA.curie('storageConditions'),
                   model_uri=EVORA.Product_storageConditions, domain=Product, range=str)

slots.Product_thirdPartyDistributionConsent = Slot(uri=EVORA.thirdPartyDistributionConsent, name="Product_thirdPartyDistributionConsent", curie=EVORA.curie('thirdPartyDistributionConsent'),
                   model_uri=EVORA.Product_thirdPartyDistributionConsent, domain=Product, range=Optional[Union[bool, Bool]])

slots.Product_usageRestrictions = Slot(uri=EVORA.usageRestrictions, name="Product_usageRestrictions", curie=EVORA.curie('usageRestrictions'),
                   model_uri=EVORA.Product_usageRestrictions, domain=Product, range=Optional[str])

slots.Antibody_productionSystem = Slot(uri=EVORA.productionSystem, name="Antibody_productionSystem", curie=EVORA.curie('productionSystem'),
                   model_uri=EVORA.Antibody_productionSystem, domain=Antibody, range=Optional[str])

slots.Antibody_antibodyPurifiedByAffinity = Slot(uri=EVORA.antibodyPurifiedByAffinity, name="Antibody_antibodyPurifiedByAffinity", curie=EVORA.curie('antibodyPurifiedByAffinity'),
                   model_uri=EVORA.Antibody_antibodyPurifiedByAffinity, domain=Antibody, range=Union[bool, Bool])

slots.Antibody_specificityDocumented = Slot(uri=EVORA.specificityDocumented, name="Antibody_specificityDocumented", curie=EVORA.curie('specificityDocumented'),
                   model_uri=EVORA.Antibody_specificityDocumented, domain=Antibody, range=Union[bool, Bool])

slots.Antibody_targetedAntigen = Slot(uri=EVORA.targetedAntigen, name="Antibody_targetedAntigen", curie=EVORA.curie('targetedAntigen'),
                   model_uri=EVORA.Antibody_targetedAntigen, domain=Antibody, range=str)

slots.Antibody_sequenceReference = Slot(uri=EVORA.sequenceReference, name="Antibody_sequenceReference", curie=EVORA.curie('sequenceReference'),
                   model_uri=EVORA.Antibody_sequenceReference, domain=Antibody, range=Optional[Union[Union[dict, SequenceReference], List[Union[dict, SequenceReference]]]])

slots.Hybridoma_hybridomaDescription = Slot(uri=EVORA.hybridomaDescription, name="Hybridoma_hybridomaDescription", curie=EVORA.curie('hybridomaDescription'),
                   model_uri=EVORA.Hybridoma_hybridomaDescription, domain=Hybridoma, range=str)

slots.Protein_biologicalMaterialOrigin = Slot(uri=EVORA.biologicalMaterialOrigin, name="Protein_biologicalMaterialOrigin", curie=EVORA.curie('biologicalMaterialOrigin'),
                   model_uri=EVORA.Protein_biologicalMaterialOrigin, domain=Protein, range=Union[dict, BiologicalMaterialOrigin])

slots.Protein_sequence = Slot(uri=EVORA.sequence, name="Protein_sequence", curie=EVORA.curie('sequence'),
                   model_uri=EVORA.Protein_sequence, domain=Protein, range=Union[Union[dict, Sequence], List[Union[dict, Sequence]]])

slots.Protein_relatedPDB = Slot(uri=EVORA.relatedPDB, name="Protein_relatedPDB", curie=EVORA.curie('relatedPDB'),
                   model_uri=EVORA.Protein_relatedPDB, domain=Protein, range=Optional[Union[Union[dict, PDBReference], List[Union[dict, PDBReference]]]])

slots.Protein_specialFeature = Slot(uri=EVORA.specialFeature, name="Protein_specialFeature", curie=EVORA.curie('specialFeature'),
                   model_uri=EVORA.Protein_specialFeature, domain=Protein, range=Optional[Union[Union[dict, SpecialFeature], List[Union[dict, SpecialFeature]]]])

slots.Protein_proteinTAG = Slot(uri=EVORA.proteinTAG, name="Protein_proteinTAG", curie=EVORA.curie('proteinTAG'),
                   model_uri=EVORA.Protein_proteinTAG, domain=Protein, range=Optional[Union[Union[dict, ProteinTag], List[Union[dict, ProteinTag]]]])

slots.Protein_domain = Slot(uri=EVORA.domain, name="Protein_domain", curie=EVORA.curie('domain'),
                   model_uri=EVORA.Protein_domain, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_expressedAs = Slot(uri=EVORA.expressedAs, name="Protein_expressedAs", curie=EVORA.curie('expressedAs'),
                   model_uri=EVORA.Protein_expressedAs, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_inclusionBodiesType = Slot(uri=EVORA.inclusionBodiesType, name="Protein_inclusionBodiesType", curie=EVORA.curie('inclusionBodiesType'),
                   model_uri=EVORA.Protein_inclusionBodiesType, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_expressionSystem = Slot(uri=EVORA.expressionSystem, name="Protein_expressionSystem", curie=EVORA.curie('expressionSystem'),
                   model_uri=EVORA.Protein_expressionSystem, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_functionalCharacterization = Slot(uri=EVORA.functionalCharacterization, name="Protein_functionalCharacterization", curie=EVORA.curie('functionalCharacterization'),
                   model_uri=EVORA.Protein_functionalCharacterization, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_functionalTechnicalDescription = Slot(uri=EVORA.functionalTechnicalDescription, name="Protein_functionalTechnicalDescription", curie=EVORA.curie('functionalTechnicalDescription'),
                   model_uri=EVORA.Protein_functionalTechnicalDescription, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_proteinPurification = Slot(uri=EVORA.proteinPurification, name="Protein_proteinPurification", curie=EVORA.curie('proteinPurification'),
                   model_uri=EVORA.Protein_proteinPurification, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_theTAGStatusOfTheSolubilizedProtein = Slot(uri=EVORA.theTAGStatusOfTheSolubilizedProtein, name="Protein_theTAGStatusOfTheSolubilizedProtein", curie=EVORA.curie('theTAGStatusOfTheSolubilizedProtein'),
                   model_uri=EVORA.Protein_theTAGStatusOfTheSolubilizedProtein, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Protein_typeOfFunctionalCharacterization = Slot(uri=EVORA.typeOfFunctionalCharacterization, name="Protein_typeOfFunctionalCharacterization", curie=EVORA.curie('typeOfFunctionalCharacterization'),
                   model_uri=EVORA.Protein_typeOfFunctionalCharacterization, domain=Protein, range=Optional[Union[str, List[str]]])

slots.Nucleic_Acid_biologicalMaterialOrigin = Slot(uri=EVORA.biologicalMaterialOrigin, name="Nucleic Acid_biologicalMaterialOrigin", curie=EVORA.curie('biologicalMaterialOrigin'),
                   model_uri=EVORA.Nucleic_Acid_biologicalMaterialOrigin, domain=NucleicAcid, range=Union[dict, BiologicalMaterialOrigin])

slots.Nucleic_Acid_hasGbFileOfTheConstruct = Slot(uri=EVORA.hasGbFileOfTheConstruct, name="Nucleic Acid_hasGbFileOfTheConstruct", curie=EVORA.curie('hasGbFileOfTheConstruct'),
                   model_uri=EVORA.Nucleic_Acid_hasGbFileOfTheConstruct, domain=NucleicAcid, range=Optional[Union[Union[dict, "Data"], List[Union[dict, "Data"]]]])

slots.Nucleic_Acid_sequence = Slot(uri=EVORA.sequence, name="Nucleic Acid_sequence", curie=EVORA.curie('sequence'),
                   model_uri=EVORA.Nucleic_Acid_sequence, domain=NucleicAcid, range=Union[Union[dict, Sequence], List[Union[dict, Sequence]]])

slots.Nucleic_Acid_isItAClonedNucleicAcid = Slot(uri=EVORA.isItAClonedNucleicAcid, name="Nucleic Acid_isItAClonedNucleicAcid", curie=EVORA.curie('isItAClonedNucleicAcid'),
                   model_uri=EVORA.Nucleic_Acid_isItAClonedNucleicAcid, domain=NucleicAcid, range=Union[bool, Bool])

slots.Nucleic_Acid_clonedIntoPlasmid = Slot(uri=EVORA.clonedIntoPlasmid, name="Nucleic Acid_clonedIntoPlasmid", curie=EVORA.curie('clonedIntoPlasmid'),
                   model_uri=EVORA.Nucleic_Acid_clonedIntoPlasmid, domain=NucleicAcid, range=Optional[Union[dict, ExpressionVector]])

slots.Nucleic_Acid_pasmidSelection = Slot(uri=EVORA.pasmidSelection, name="Nucleic Acid_pasmidSelection", curie=EVORA.curie('pasmidSelection'),
                   model_uri=EVORA.Nucleic_Acid_pasmidSelection, domain=NucleicAcid, range=Optional[Union[Union[dict, PlasmidSelection], List[Union[dict, PlasmidSelection]]]])

slots.Nucleic_Acid_hasTAG = Slot(uri=EVORA.hasTAG, name="Nucleic Acid_hasTAG", curie=EVORA.curie('hasTAG'),
                   model_uri=EVORA.Nucleic_Acid_hasTAG, domain=NucleicAcid, range=Union[dict, ProteinTag])

slots.Nucleic_Acid_regionEncompassedInThisProduct = Slot(uri=EVORA.regionEncompassedInThisProduct, name="Nucleic Acid_regionEncompassedInThisProduct", curie=EVORA.curie('regionEncompassedInThisProduct'),
                   model_uri=EVORA.Nucleic_Acid_regionEncompassedInThisProduct, domain=NucleicAcid, range=str)

slots.Nucleic_Acid_mutationObserved = Slot(uri=EVORA.mutationObserved, name="Nucleic Acid_mutationObserved", curie=EVORA.curie('mutationObserved'),
                   model_uri=EVORA.Nucleic_Acid_mutationObserved, domain=NucleicAcid, range=Union[bool, Bool])

slots.Nucleic_Acid_observedMutations = Slot(uri=EVORA.observedMutations, name="Nucleic Acid_observedMutations", curie=EVORA.curie('observedMutations'),
                   model_uri=EVORA.Nucleic_Acid_observedMutations, domain=NucleicAcid, range=Optional[str])

slots.Nucleic_Acid_identificationTechnique = Slot(uri=EVORA.identificationTechnique, name="Nucleic Acid_identificationTechnique", curie=EVORA.curie('identificationTechnique'),
                   model_uri=EVORA.Nucleic_Acid_identificationTechnique, domain=NucleicAcid, range=Optional[str])

slots.Nucleic_Acid_sequencing = Slot(uri=EVORA.sequencing, name="Nucleic Acid_sequencing", curie=EVORA.curie('sequencing'),
                   model_uri=EVORA.Nucleic_Acid_sequencing, domain=NucleicAcid, range=str)

slots.Nucleic_Acid_titer = Slot(uri=EVORA.titer, name="Nucleic Acid_titer", curie=EVORA.curie('titer'),
                   model_uri=EVORA.Nucleic_Acid_titer, domain=NucleicAcid, range=Optional[str])

slots.Nucleic_Acid_sequenceChecked = Slot(uri=EVORA.sequenceChecked, name="Nucleic Acid_sequenceChecked", curie=EVORA.curie('sequenceChecked'),
                   model_uri=EVORA.Nucleic_Acid_sequenceChecked, domain=NucleicAcid, range=Union[bool, Bool])

slots.Detection_Kit_hasSOPFile = Slot(uri=EVORA.hasSOPFile, name="Detection Kit_hasSOPFile", curie=EVORA.curie('hasSOPFile'),
                   model_uri=EVORA.Detection_Kit_hasSOPFile, domain=DetectionKit, range=Optional[Union[Union[dict, "File"], List[Union[dict, "File"]]]])

slots.Detection_Kit_specificityDocumented = Slot(uri=EVORA.specificityDocumented, name="Detection Kit_specificityDocumented", curie=EVORA.curie('specificityDocumented'),
                   model_uri=EVORA.Detection_Kit_specificityDocumented, domain=DetectionKit, range=Union[bool, Bool])

slots.Detection_Kit_specificity = Slot(uri=EVORA.specificity, name="Detection Kit_specificity", curie=EVORA.curie('specificity'),
                   model_uri=EVORA.Detection_Kit_specificity, domain=DetectionKit, range=Optional[str])

slots.Detection_Kit_targetedRegion = Slot(uri=EVORA.targetedRegion, name="Detection Kit_targetedRegion", curie=EVORA.curie('targetedRegion'),
                   model_uri=EVORA.Detection_Kit_targetedRegion, domain=DetectionKit, range=Optional[str])

slots.Bundle_productsOfTheBundle = Slot(uri=EVORA.productsOfTheBundle, name="Bundle_productsOfTheBundle", curie=EVORA.curie('productsOfTheBundle'),
                   model_uri=EVORA.Bundle_productsOfTheBundle, domain=Bundle, range=Union[Union[dict, Product], List[Union[dict, Product]]])

slots.Bundle_complementaryDocument = Slot(uri=EVORA.complementaryDocument, name="Bundle_complementaryDocument", curie=EVORA.curie('complementaryDocument'),
                   model_uri=EVORA.Bundle_complementaryDocument, domain=Bundle, range=Optional[Union[Union[dict, "File"], List[Union[dict, "File"]]]])

slots.Pathogen_biologicalMaterialOrigin = Slot(uri=EVORA.biologicalMaterialOrigin, name="Pathogen_biologicalMaterialOrigin", curie=EVORA.curie('biologicalMaterialOrigin'),
                   model_uri=EVORA.Pathogen_biologicalMaterialOrigin, domain=Pathogen, range=Union[dict, BiologicalMaterialOrigin])

slots.Pathogen_suspectedEpidemiologicalOrigin = Slot(uri=EVORA.suspectedEpidemiologicalOrigin, name="Pathogen_suspectedEpidemiologicalOrigin", curie=EVORA.curie('suspectedEpidemiologicalOrigin'),
                   model_uri=EVORA.Pathogen_suspectedEpidemiologicalOrigin, domain=Pathogen, range=Optional[Union[Union[dict, GeographicalOrigin], List[Union[dict, GeographicalOrigin]]]])

slots.Pathogen_isolationHost = Slot(uri=EVORA.isolationHost, name="Pathogen_isolationHost", curie=EVORA.curie('isolationHost'),
                   model_uri=EVORA.Pathogen_isolationHost, domain=Pathogen, range=Optional[Union[Union[dict, IsolationHost], List[Union[dict, IsolationHost]]]])

slots.Pathogen_productionCellLine = Slot(uri=EVORA.productionCellLine, name="Pathogen_productionCellLine", curie=EVORA.curie('productionCellLine'),
                   model_uri=EVORA.Pathogen_productionCellLine, domain=Pathogen, range=Optional[Union[Union[dict, ProductionCellLine], List[Union[dict, ProductionCellLine]]]])

slots.Pathogen_propagationHost = Slot(uri=EVORA.propagationHost, name="Pathogen_propagationHost", curie=EVORA.curie('propagationHost'),
                   model_uri=EVORA.Pathogen_propagationHost, domain=Pathogen, range=Optional[Union[Union[dict, PropagationHost], List[Union[dict, PropagationHost]]]])

slots.Pathogen_transmissionMethod = Slot(uri=EVORA.transmissionMethod, name="Pathogen_transmissionMethod", curie=EVORA.curie('transmissionMethod'),
                   model_uri=EVORA.Pathogen_transmissionMethod, domain=Pathogen, range=Optional[Union[Union[dict, TransmissionMethod], List[Union[dict, TransmissionMethod]]]])

slots.Pathogen_sequence = Slot(uri=EVORA.sequence, name="Pathogen_sequence", curie=EVORA.curie('sequence'),
                   model_uri=EVORA.Pathogen_sequence, domain=Pathogen, range=Union[Union[dict, Sequence], List[Union[dict, Sequence]]])

slots.Pathogen_cultivability = Slot(uri=EVORA.cultivability, name="Pathogen_cultivability", curie=EVORA.curie('cultivability'),
                   model_uri=EVORA.Pathogen_cultivability, domain=Pathogen, range=str)

slots.Pathogen_clinicalInformation = Slot(uri=EVORA.clinicalInformation, name="Pathogen_clinicalInformation", curie=EVORA.curie('clinicalInformation'),
                   model_uri=EVORA.Pathogen_clinicalInformation, domain=Pathogen, range=Optional[str])

slots.Pathogen_identificationTechnique = Slot(uri=EVORA.identificationTechnique, name="Pathogen_identificationTechnique", curie=EVORA.curie('identificationTechnique'),
                   model_uri=EVORA.Pathogen_identificationTechnique, domain=Pathogen, range=Optional[str])

slots.Pathogen_infectivity = Slot(uri=EVORA.infectivity, name="Pathogen_infectivity", curie=EVORA.curie('infectivity'),
                   model_uri=EVORA.Pathogen_infectivity, domain=Pathogen, range=str)

slots.Pathogen_infectivityTest = Slot(uri=EVORA.infectivityTest, name="Pathogen_infectivityTest", curie=EVORA.curie('infectivityTest'),
                   model_uri=EVORA.Pathogen_infectivityTest, domain=Pathogen, range=Optional[str])

slots.Pathogen_isolationTechnique = Slot(uri=EVORA.isolationTechnique, name="Pathogen_isolationTechnique", curie=EVORA.curie('isolationTechnique'),
                   model_uri=EVORA.Pathogen_isolationTechnique, domain=Pathogen, range=Optional[str])

slots.Pathogen_isolationConditions = Slot(uri=EVORA.isolationConditions, name="Pathogen_isolationConditions", curie=EVORA.curie('isolationConditions'),
                   model_uri=EVORA.Pathogen_isolationConditions, domain=Pathogen, range=Optional[str])

slots.Pathogen_letterOfAuthority = Slot(uri=EVORA.letterOfAuthority, name="Pathogen_letterOfAuthority", curie=EVORA.curie('letterOfAuthority'),
                   model_uri=EVORA.Pathogen_letterOfAuthority, domain=Pathogen, range=str)

slots.Pathogen_passage = Slot(uri=EVORA.passage, name="Pathogen_passage", curie=EVORA.curie('passage'),
                   model_uri=EVORA.Pathogen_passage, domain=Pathogen, range=Optional[str])

slots.Pathogen_sequencing = Slot(uri=EVORA.sequencing, name="Pathogen_sequencing", curie=EVORA.curie('sequencing'),
                   model_uri=EVORA.Pathogen_sequencing, domain=Pathogen, range=str)

slots.Pathogen_titer = Slot(uri=EVORA.titer, name="Pathogen_titer", curie=EVORA.curie('titer'),
                   model_uri=EVORA.Pathogen_titer, domain=Pathogen, range=str)

slots.Virus_coInfectingViruses = Slot(uri=EVORA.coInfectingViruses, name="Virus_coInfectingViruses", curie=EVORA.curie('coInfectingViruses'),
                   model_uri=EVORA.Virus_coInfectingViruses, domain=Virus, range=Optional[Union[Union[dict, VirusName], List[Union[dict, VirusName]]]])

slots.Virus_contaminationWithCoInfectingViruses = Slot(uri=EVORA.contaminationWithCoInfectingViruses, name="Virus_contaminationWithCoInfectingViruses", curie=EVORA.curie('contaminationWithCoInfectingViruses'),
                   model_uri=EVORA.Virus_contaminationWithCoInfectingViruses, domain=Virus, range=Union[bool, Bool])

slots.Virus_mycoplasmicContent = Slot(uri=EVORA.mycoplasmicContent, name="Virus_mycoplasmicContent", curie=EVORA.curie('mycoplasmicContent'),
                   model_uri=EVORA.Virus_mycoplasmicContent, domain=Virus, range=Union[bool, Bool])

slots.MSDS_msdsContact = Slot(uri=EVORA.msdsContact, name="MSDS_msdsContact", curie=EVORA.curie('msdsContact'),
                   model_uri=EVORA.MSDS_msdsContact, domain=MSDS, range=Union[dict, "ContactPoint"])

slots.MSDS_physicalChemicalProperties = Slot(uri=EVORA.physicalChemicalProperties, name="MSDS_physicalChemicalProperties", curie=EVORA.curie('physicalChemicalProperties'),
                   model_uri=EVORA.MSDS_physicalChemicalProperties, domain=MSDS, range=Optional[str])

slots.MSDS_hazardsIdentification = Slot(uri=EVORA.hazardsIdentification, name="MSDS_hazardsIdentification", curie=EVORA.curie('hazardsIdentification'),
                   model_uri=EVORA.MSDS_hazardsIdentification, domain=MSDS, range=Optional[str])

slots.MSDS_firstAidMeasures = Slot(uri=EVORA.firstAidMeasures, name="MSDS_firstAidMeasures", curie=EVORA.curie('firstAidMeasures'),
                   model_uri=EVORA.MSDS_firstAidMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_fireFightingMeasures = Slot(uri=EVORA.fireFightingMeasures, name="MSDS_fireFightingMeasures", curie=EVORA.curie('fireFightingMeasures'),
                   model_uri=EVORA.MSDS_fireFightingMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_accidentalReleaseMeasures = Slot(uri=EVORA.accidentalReleaseMeasures, name="MSDS_accidentalReleaseMeasures", curie=EVORA.curie('accidentalReleaseMeasures'),
                   model_uri=EVORA.MSDS_accidentalReleaseMeasures, domain=MSDS, range=Optional[str])

slots.MSDS_handlingAndStorage = Slot(uri=EVORA.handlingAndStorage, name="MSDS_handlingAndStorage", curie=EVORA.curie('handlingAndStorage'),
                   model_uri=EVORA.MSDS_handlingAndStorage, domain=MSDS, range=Optional[str])

slots.MSDS_exposureControlsPersonalProtection = Slot(uri=EVORA.exposureControlsPersonalProtection, name="MSDS_exposureControlsPersonalProtection", curie=EVORA.curie('exposureControlsPersonalProtection'),
                   model_uri=EVORA.MSDS_exposureControlsPersonalProtection, domain=MSDS, range=Optional[str])

slots.MSDS_stabilityAndReactivity = Slot(uri=EVORA.stabilityAndReactivity, name="MSDS_stabilityAndReactivity", curie=EVORA.curie('stabilityAndReactivity'),
                   model_uri=EVORA.MSDS_stabilityAndReactivity, domain=MSDS, range=Optional[str])

slots.MSDS_toxicologicalInformation = Slot(uri=EVORA.toxicologicalInformation, name="MSDS_toxicologicalInformation", curie=EVORA.curie('toxicologicalInformation'),
                   model_uri=EVORA.MSDS_toxicologicalInformation, domain=MSDS, range=Optional[str])

slots.MSDS_ecologicalInformation = Slot(uri=EVORA.ecologicalInformation, name="MSDS_ecologicalInformation", curie=EVORA.curie('ecologicalInformation'),
                   model_uri=EVORA.MSDS_ecologicalInformation, domain=MSDS, range=Optional[str])

slots.MSDS_disposalConsiderations = Slot(uri=EVORA.disposalConsiderations, name="MSDS_disposalConsiderations", curie=EVORA.curie('disposalConsiderations'),
                   model_uri=EVORA.MSDS_disposalConsiderations, domain=MSDS, range=Optional[str])

slots.MSDS_transportInformation = Slot(uri=EVORA.transportInformation, name="MSDS_transportInformation", curie=EVORA.curie('transportInformation'),
                   model_uri=EVORA.MSDS_transportInformation, domain=MSDS, range=Optional[str])

slots.MSDS_regulatoryInformation = Slot(uri=EVORA.regulatoryInformation, name="MSDS_regulatoryInformation", curie=EVORA.curie('regulatoryInformation'),
                   model_uri=EVORA.MSDS_regulatoryInformation, domain=MSDS, range=Optional[str])

slots.MSDS_furtherInformation = Slot(uri=EVORA.furtherInformation, name="MSDS_furtherInformation", curie=EVORA.curie('furtherInformation'),
                   model_uri=EVORA.MSDS_furtherInformation, domain=MSDS, range=Optional[str])

slots.File_contentURL = Slot(uri=EVORA.contentURL, name="File_contentURL", curie=EVORA.curie('contentURL'),
                   model_uri=EVORA.File_contentURL, domain=File, range=Union[str, URI])

slots.File_format = Slot(uri=EVORA.format, name="File_format", curie=EVORA.curie('format'),
                   model_uri=EVORA.File_format, domain=File, range=str)

slots.File_license = Slot(uri=EVORA.license, name="File_license", curie=EVORA.curie('license'),
                   model_uri=EVORA.File_license, domain=File, range=Optional[Union[dict, "License"]])

slots.Image_altText = Slot(uri=EVORA.altText, name="Image_altText", curie=EVORA.curie('altText'),
                   model_uri=EVORA.Image_altText, domain=Image, range=Optional[str])

slots.ContactPoint_email = Slot(uri=EVORA.email, name="ContactPoint_email", curie=EVORA.curie('email'),
                   model_uri=EVORA.ContactPoint_email, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_telephone = Slot(uri=EVORA.telephone, name="ContactPoint_telephone", curie=EVORA.curie('telephone'),
                   model_uri=EVORA.ContactPoint_telephone, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_streetAddress = Slot(uri=EVORA.streetAddress, name="ContactPoint_streetAddress", curie=EVORA.curie('streetAddress'),
                   model_uri=EVORA.ContactPoint_streetAddress, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressLocality = Slot(uri=EVORA.addressLocality, name="ContactPoint_addressLocality", curie=EVORA.curie('addressLocality'),
                   model_uri=EVORA.ContactPoint_addressLocality, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressRegion = Slot(uri=EVORA.addressRegion, name="ContactPoint_addressRegion", curie=EVORA.curie('addressRegion'),
                   model_uri=EVORA.ContactPoint_addressRegion, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_postalCode = Slot(uri=EVORA.postalCode, name="ContactPoint_postalCode", curie=EVORA.curie('postalCode'),
                   model_uri=EVORA.ContactPoint_postalCode, domain=ContactPoint, range=Optional[str])

slots.ContactPoint_addressCountry = Slot(uri=EVORA.addressCountry, name="ContactPoint_addressCountry", curie=EVORA.curie('addressCountry'),
                   model_uri=EVORA.ContactPoint_addressCountry, domain=ContactPoint, range=Optional[Union[dict, Country]])

slots.ContactPoint_oRCIDiD = Slot(uri=EVORA.oRCIDiD, name="ContactPoint_oRCIDiD", curie=EVORA.curie('oRCIDiD'),
                   model_uri=EVORA.ContactPoint_oRCIDiD, domain=ContactPoint, range=Optional[str])

slots.License_resourceURL = Slot(uri=EVORA.resourceURL, name="License_resourceURL", curie=EVORA.curie('resourceURL'),
                   model_uri=EVORA.License_resourceURL, domain=License, range=Optional[Union[str, URI]])

slots.License_licensingOrAttribution = Slot(uri=EVORA.licensingOrAttribution, name="License_licensingOrAttribution", curie=EVORA.curie('licensingOrAttribution'),
                   model_uri=EVORA.License_licensingOrAttribution, domain=License, range=Optional[str])

slots.License_logo = Slot(uri=EVORA.logo, name="License_logo", curie=EVORA.curie('logo'),
                   model_uri=EVORA.License_logo, domain=License, range=Optional[Union[dict, Image]])

slots.Certification_logo = Slot(uri=EVORA.logo, name="Certification_logo", curie=EVORA.curie('logo'),
                   model_uri=EVORA.Certification_logo, domain=Certification, range=Optional[Union[dict, Image]])

slots.Certification_certificationDocument = Slot(uri=EVORA.certificationDocument, name="Certification_certificationDocument", curie=EVORA.curie('certificationDocument'),
                   model_uri=EVORA.Certification_certificationDocument, domain=Certification, range=Optional[Union[Union[dict, Document], List[Union[dict, Document]]]])

slots.Certification_resourceURL = Slot(uri=EVORA.resourceURL, name="Certification_resourceURL", curie=EVORA.curie('resourceURL'),
                   model_uri=EVORA.Certification_resourceURL, domain=Certification, range=Optional[Union[str, URI]])