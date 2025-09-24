from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "1.0.9907"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'comments': ['EVORAO is an ontology for standardized metadata supporting the '
                  'sharing of pathogens as biological materials, their derived '
                  'products, and associated services, organized into collections. '
                  'While initially focused on virology, it is designed for '
                  'interoperability and is extensible to other pathogens. EVORAO '
                  'is compatible with DCAT, making it well-suited for efficiently '
                  'cataloguing pathogen collections and related resources.'],
     'contributors': ['https://github.com/Angatar',
                      'https://orcid.org/0000-0002-5080-3456',
                      'https://github.com/jamesamcl',
                      'https://orcid.org/0000-0002-8361-2795',
                      'https://orcid.org/0000-0003-3035-4195',
                      'https://orcid.org/0000-0003-4073-7456',
                      'https://orcid.org/0000-0002-2004-4073',
                      'https://orcid.org/0000-0002-6963-8673',
                      'https://orcid.org/0000-0003-3067-827X',
                      'https://orcid.org/0000-0002-1257-6862',
                      'https://orcid.org/0000-0002-2042-2839',
                      'https://orcid.org/0000-0002-2859-7123'],
     'created_by': 'https://github.com/Angatar',
     'default_prefix': 'EVORAO',
     'default_range': 'string',
     'description': 'The EVORAO Ontology provides a structured and harmonized '
                    'vocabulary for describing shareable pathogens as '
                    'characterized biological materials, along with their derived '
                    'products and associated services, organized into collections. '
                    'Developed within the EVORA project, it supports consistent '
                    'metadata annotation across research infrastructures, '
                    'promoting findability, accessibility, interoperability, and '
                    'reusability (FAIR). By aligning with relevant standards and '
                    'ontologies, EVORAO facilitates cross-domain collaboration, '
                    'integration, and sharing of pathogenic resources and services '
                    'to enhance pandemic preparedness and response. While '
                    'initially focused on virology, EVORAO is designed to be '
                    'extensible and also supports metadata harmonization for other '
                    'pathogens. EVORAO is compatible with DCAT, making it '
                    'well-suited for efficiently cataloguing pathogen collections '
                    'and related resources.',
     'generation_date': '2025-09-24T11:32:06',
     'id': 'https://w3id.org/evorao/',
     'imports': ['linkml:types'],
     'in_language': 'en',
     'keywords': ['virus',
                  'pathogen',
                  'viral resources',
                  'pandemic preparedness',
                  'virology',
                  'biological materials',
                  'biological collections',
                  'infectious diseases',
                  'biosample',
                  'diagnostic material',
                  'reference material',
                  'biobank',
                  'pathogen collections',
                  'interoperability'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'EVORAO',
     'prefixes': {'EVORAO': {'prefix_prefix': 'EVORAO',
                             'prefix_reference': 'https://w3id.org/evorao/'},
                  'adms': {'prefix_prefix': 'adms',
                           'prefix_reference': 'http://www.w3.org/ns/adms#'},
                  'afop': {'prefix_prefix': 'afop',
                           'prefix_reference': 'http://purl.allotrope.org/ontologies/property#'},
                  'apollo': {'prefix_prefix': 'apollo',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/APOLLO_SV_'},
                  'bao': {'prefix_prefix': 'bao',
                          'prefix_reference': 'http://www.bioassayontology.org/bao#BAO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'bto': {'prefix_prefix': 'bto',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BTO_'},
                  'chebi': {'prefix_prefix': 'chebi',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'cido': {'prefix_prefix': 'cido',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/CIDO_'},
                  'clo': {'prefix_prefix': 'clo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/CLO_'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcmi': {'prefix_prefix': 'dcmi',
                           'prefix_reference': 'http://purl.org/dc/dcmitype/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'doid': {'prefix_prefix': 'doid',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/DOID_'},
                  'dwc': {'prefix_prefix': 'dwc',
                          'prefix_reference': 'http://rs.tdwg.org/dwc/terms/'},
                  'edam': {'prefix_prefix': 'edam',
                           'prefix_reference': 'http://edamontology.org/data_'},
                  'efo': {'prefix_prefix': 'efo',
                          'prefix_reference': 'http://www.ebi.ac.uk/efo/EFO_'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'genepio': {'prefix_prefix': 'genepio',
                              'prefix_reference': 'http://purl.obolibrary.org/obo/GENEPIO_'},
                  'geno': {'prefix_prefix': 'geno',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/GENO_'},
                  'geo': {'prefix_prefix': 'geo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/GEO_'},
                  'gr': {'prefix_prefix': 'gr',
                         'prefix_reference': 'http://purl.org/goodrelations/v1#'},
                  'hso': {'prefix_prefix': 'hso',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/HSO_'},
                  'iao': {'prefix_prefix': 'iao',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'iceo': {'prefix_prefix': 'iceo',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ICEO_'},
                  'ido': {'prefix_prefix': 'ido',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IDO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mesh': {'prefix_prefix': 'mesh',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'mi': {'prefix_prefix': 'mi',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/MI_'},
                  'mondo': {'prefix_prefix': 'mondo',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'ms': {'prefix_prefix': 'ms',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/MS_'},
                  'ncbitaxon': {'prefix_prefix': 'ncbitaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'ncit': {'prefix_prefix': 'ncit',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'obi': {'prefix_prefix': 'obi',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'obib': {'prefix_prefix': 'obib',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/OBIB_'},
                  'omo': {'prefix_prefix': 'omo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OMO_'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'pav': {'prefix_prefix': 'pav',
                          'prefix_reference': 'http://purl.org/pav/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'reproduceme': {'prefix_prefix': 'reproduceme',
                                  'prefix_reference': 'https://w3id.org/reproduceme#'},
                  'ro': {'prefix_prefix': 'ro',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'rov': {'prefix_prefix': 'rov',
                          'prefix_reference': 'http://www.w3.org/ns/regorg#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sepio': {'prefix_prefix': 'sepio',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/SEPIO_'},
                  'sio': {'prefix_prefix': 'sio',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'snomed': {'prefix_prefix': 'snomed',
                             'prefix_reference': 'http://snomed.info/id/'},
                  'swo': {'prefix_prefix': 'swo',
                          'prefix_reference': 'http://www.ebi.ac.uk/swo/SWO_'},
                  't4fs': {'prefix_prefix': 't4fs',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/T4FS_'},
                  'taxrank': {'prefix_prefix': 'taxrank',
                              'prefix_reference': 'http://purl.obolibrary.org/obo/TAXRANK_'},
                  'uniprotrdfs': {'prefix_prefix': 'uniprotrdfs',
                                  'prefix_reference': 'http://purl.uniprot.org/core/'},
                  'vcard': {'prefix_prefix': 'vcard',
                            'prefix_reference': 'http://www.w3.org/2006/vcard/ns#'},
                  'vo': {'prefix_prefix': 'vo',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/VO_'},
                  'wd': {'prefix_prefix': 'wd',
                         'prefix_reference': 'http://www.wikidata.org/entity/'},
                  'wdp': {'prefix_prefix': 'wdp',
                          'prefix_reference': 'http://www.wikidata.org/prop/'},
                  'xco': {'prefix_prefix': 'xco',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/XCO_'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'models/evora_schema.yaml',
     'title': 'European Viral Outbreak Response Alliance Ontology'} )


class Resource(ConfiguredBaseModel):
    """
    Resource published or curated by a single agent
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:Resource',
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'dateIssued': {'close_mappings': ['schema:datePublished',
                                                          'schema:dateCreated'],
                                       'comments': ['encoded using the relevant ISO '
                                                    '8601 Date and Time compliant '
                                                    'string [DATETIME]'],
                                       'description': 'Date of formal issuance (e.g., '
                                                      'publication) of the resource',
                                       'domain_of': ['Resource'],
                                       'exact_mappings': ['sepio:0000051'],
                                       'multivalued': False,
                                       'name': 'dateIssued',
                                       'range': 'datetime',
                                       'required': False,
                                       'slot_uri': 'dct:issued',
                                       'title': 'date issued'},
                        'dateModified': {'close_mappings': ['schema:dateModified'],
                                         'comments': ['encoded using the relevant ISO '
                                                      '8601 Date and Time compliant '
                                                      'string [DATETIME]'],
                                         'description': 'Most recent date on which the '
                                                        'resource was changed, updated '
                                                        'or modified',
                                         'domain_of': ['Resource'],
                                         'exact_mappings': ['sepio:0000036'],
                                         'multivalued': False,
                                         'name': 'dateModified',
                                         'range': 'datetime',
                                         'required': False,
                                         'slot_uri': 'dct:modified',
                                         'title': 'date modified'},
                        'keyword': {'description': 'A keyword or tag describing the '
                                                   'resource',
                                    'domain_of': ['Resource'],
                                    'multivalued': True,
                                    'name': 'keyword',
                                    'range': 'string',
                                    'required': False,
                                    'slot_uri': 'dcat:keyword',
                                    'title': 'keyword'}},
         'title': 'Resource'})

    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Dataset(Resource):
    """
    A collection of data, published or curated by a single agent, and available for access
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:Dataset',
         'exact_mappings': ['schema:Dataset',
                            'wd:Q1172284',
                            'schema:Dataset',
                            'wd:Q1172284'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'ContactPoint',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['Dataset',
                                                'DataService',
                                                'Publication',
                                                'Term',
                                                'License',
                                                'Certification'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'},
                        'version': {'close_mappings': ['wdp:P393', 'schema:version'],
                                    'description': 'The version indicator (name or '
                                                   'identifier) of a resource',
                                    'domain_of': ['Dataset', 'Version', 'Taxonomy'],
                                    'exact_mappings': ['pav:version'],
                                    'multivalued': False,
                                    'name': 'version',
                                    'range': 'string',
                                    'recommended': True,
                                    'related_mappings': ['schema:identifier'],
                                    'required': False,
                                    'slot_uri': 'dcat:version',
                                    'title': 'version'}},
         'title': 'Dataset'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class DataService(Resource):
    """
    A collection of operations that provides access to one or more datasets or data processing functions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:DataService',
         'close_mappings': ['wd:Q193424',
                            'schema:WebAPI',
                            'wd:Q193424',
                            'schema:WebAPI'],
         'exact_mappings': ['schema:EntryPoint', 'schema:EntryPoint'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['DataService',
                                                      'Dataset',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'ContactPoint',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'endpointUrl': {'close_mappings': ['wdp:P1630'],
                                        'description': 'The URL template that allows '
                                                       'to get the content',
                                        'domain_of': ['DataService'],
                                        'exact_mappings': ['schema:urlTemplate'],
                                        'multivalued': False,
                                        'name': 'endpointUrl',
                                        'range': 'uri',
                                        'required': True,
                                        'slot_uri': 'dcat:endpointURL',
                                        'title': 'endpoint URL'},
                        'servesDataset': {'comments': ['This property rather intends '
                                                       'to point towards Catalogues as '
                                                       'collections of Datasets'],
                                          'description': 'A collection of data that '
                                                         'this data service can '
                                                         'distribute',
                                          'domain_of': ['DataService'],
                                          'multivalued': True,
                                          'name': 'servesDataset',
                                          'range': 'Dataset',
                                          'recommended': True,
                                          'required': False,
                                          'slot_uri': 'dcat:servesDataset',
                                          'title': 'serves dataset'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['DataService',
                                                'Dataset',
                                                'Publication',
                                                'Term',
                                                'License',
                                                'Certification'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'}},
         'title': 'Data Service'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['DataService',
                       'Dataset',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['DataService',
                       'Dataset',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    endpointUrl: str = Field(default=..., title="endpoint URL", description="""The URL template that allows to get the content""", json_schema_extra = { "linkml_meta": {'alias': 'endpointUrl',
         'close_mappings': ['wdp:P1630'],
         'domain_of': ['DataService'],
         'exact_mappings': ['schema:urlTemplate'],
         'slot_uri': 'dcat:endpointURL'} })
    servesDataset: Optional[list[Dataset]] = Field(default=None, title="serves dataset", description="""A collection of data that this data service can distribute""", json_schema_extra = { "linkml_meta": {'alias': 'servesDataset',
         'comments': ['This property rather intends to point towards Catalogues as '
                      'collections of Datasets'],
         'domain_of': ['DataService'],
         'recommended': True,
         'slot_uri': 'dcat:servesDataset'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Version(Resource):
    """
    Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['reproduceme:Version', 'reproduceme:Version'],
         'comments': ['Represents a specific snapshot/release of a resource (e.g., a '
                      'dataset). It enables managing multiple versions as first-class '
                      'nodes and linking each version to its subject via '
                      'evorao:versionOf and to the using resource via evorao:version '
                      '(e.g., as nodes in a graph database).'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['wd:Q114469879', 'wd:Q114469879'],
         'slot_usage': {'resource': {'description': 'Resource published or curated by '
                                                    'a single agent',
                                     'domain_of': ['Version'],
                                     'multivalued': True,
                                     'name': 'resource',
                                     'range': 'Resource',
                                     'recommended': True,
                                     'required': False,
                                     'title': 'resource'},
                        'version': {'close_mappings': ['wdp:P393', 'schema:version'],
                                    'description': 'The version indicator (name or '
                                                   'identifier) of a resource',
                                    'domain_of': ['Version', 'Dataset', 'Taxonomy'],
                                    'exact_mappings': ['pav:version'],
                                    'multivalued': False,
                                    'name': 'version',
                                    'range': 'string',
                                    'related_mappings': ['schema:identifier'],
                                    'required': True,
                                    'slot_uri': 'dcat:version',
                                    'title': 'version'},
                        'versionOf': {'description': 'Identifier of what type of '
                                                     'entities the version qualifies',
                                      'domain_of': ['Version'],
                                      'multivalued': False,
                                      'name': 'versionOf',
                                      'range': 'string',
                                      'related_mappings': ['dct:isVersionOf'],
                                      'required': True,
                                      'title': 'version Of'}},
         'title': 'Version'})

    version: str = Field(default=..., title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Version', 'Dataset', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    versionOf: str = Field(default=..., title="version Of", description="""Identifier of what type of entities the version qualifies""", json_schema_extra = { "linkml_meta": {'alias': 'versionOf',
         'domain_of': ['Version'],
         'related_mappings': ['dct:isVersionOf']} })
    resource: Optional[list[Resource]] = Field(default=None, title="resource", description="""Resource published or curated by a single agent""", json_schema_extra = { "linkml_meta": {'alias': 'resource', 'domain_of': ['Version'], 'recommended': True} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Catalogue(Dataset):
    """
    A curated collection of metadata about resources
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:Catalog',
         'close_mappings': ['wd:Q2352616',
                            'skos:Collection',
                            'wd:Q2352616',
                            'skos:Collection'],
         'exact_mappings': ['schema:DataCatalog', 'schema:DataCatalog'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Catalogue'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Taxonomy(Catalogue):
    """
    A structured representation of data about the classification and naming of biological organisms into groups according to shared characteristics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['skos:Collection', 'skos:Collection'],
         'close_mappings': ['edam:3028', 'ncit:C17469', 'edam:3028', 'ncit:C17469'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['wd:Q8269924', 'wd:Q8269924'],
         'slot_usage': {'rank': {'close_mappings': ['dwc:taxonRank',
                                                    'schema:taxonRank',
                                                    'biolink:has_taxonomic_rank'],
                                 'description': 'Relative level or position of the '
                                                'identified taxon in the taxonomy',
                                 'domain_of': ['Taxonomy', 'Taxon'],
                                 'exact_mappings': ['wdp:P105'],
                                 'multivalued': True,
                                 'name': 'rank',
                                 'range': 'TaxonomicRank',
                                 'related_mappings': ['taxrank:1000000',
                                                      'ncbitaxon:has_rank'],
                                 'required': False,
                                 'title': 'rank'},
                        'rankDataProvider': {'description': 'The data provider for the '
                                                            'description of the '
                                                            'taxonomic ranks used in '
                                                            'this taxonomy',
                                             'domain_of': ['Taxonomy'],
                                             'multivalued': False,
                                             'name': 'rankDataProvider',
                                             'range': 'DataProvider',
                                             'required': False,
                                             'title': 'rank data provider'},
                        'taxon': {'close_mappings': ['schema:taxonomicRange',
                                                     'dwc:taxonID',
                                                     'dwc:toTaxon'],
                                  'description': 'Scientifically classified group or '
                                                 'entity within the reference taxonomy',
                                  'domain_of': ['Taxonomy',
                                                'PathogenIdentification',
                                                'ClinicalGroup'],
                                  'multivalued': True,
                                  'name': 'taxon',
                                  'range': 'Taxon',
                                  'related_mappings': ['dwc:Taxon'],
                                  'required': False,
                                  'title': 'taxon'},
                        'taxonDataProvider': {'description': 'The data provider for '
                                                             'the taxons of the '
                                                             'taxonomy',
                                              'domain_of': ['Taxonomy'],
                                              'multivalued': False,
                                              'name': 'taxonDataProvider',
                                              'range': 'DataProvider',
                                              'required': False,
                                              'title': 'taxon data provider'},
                        'version': {'close_mappings': ['wdp:P393', 'schema:version'],
                                    'description': 'The version indicator (name or '
                                                   'identifier) of a resource',
                                    'domain_of': ['Taxonomy', 'Dataset', 'Version'],
                                    'exact_mappings': ['pav:version'],
                                    'multivalued': False,
                                    'name': 'version',
                                    'range': 'string',
                                    'related_mappings': ['schema:identifier'],
                                    'required': True,
                                    'slot_uri': 'dcat:version',
                                    'title': 'version'},
                        'versionDataProvider': {'description': 'The data provider for '
                                                               'the Version ID of this '
                                                               'taxonomy',
                                                'domain_of': ['Taxonomy'],
                                                'multivalued': False,
                                                'name': 'versionDataProvider',
                                                'range': 'DataProvider',
                                                'required': True,
                                                'title': 'version data provider'}},
         'title': 'Taxonomy'})

    taxon: Optional[list[Taxon]] = Field(default=None, title="taxon", description="""Scientifically classified group or entity within the reference taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'close_mappings': ['schema:taxonomicRange', 'dwc:taxonID', 'dwc:toTaxon'],
         'comments': ['The taxon of the highest rank known that can be used to '
                      'classify a pathogen or group of pathogens (e.g viruses) in the '
                      'reference taxonomy'],
         'domain_of': ['Taxonomy', 'PathogenIdentification', 'ClinicalGroup'],
         'related_mappings': ['dwc:Taxon']} })
    taxonDataProvider: Optional[DataProvider] = Field(default=None, title="taxon data provider", description="""The data provider for the taxons of the taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'taxonDataProvider', 'domain_of': ['Taxonomy']} })
    version: str = Field(default=..., title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Taxonomy', 'Dataset', 'Version'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    versionDataProvider: DataProvider = Field(default=..., title="version data provider", description="""The data provider for the Version ID of this taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'versionDataProvider', 'domain_of': ['Taxonomy']} })
    rank: Optional[list[TaxonomicRank]] = Field(default=None, title="rank", description="""Relative level or position of the identified taxon in the taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'rank',
         'close_mappings': ['dwc:taxonRank',
                            'schema:taxonRank',
                            'biolink:has_taxonomic_rank'],
         'domain_of': ['Taxonomy', 'Taxon'],
         'exact_mappings': ['wdp:P105'],
         'related_mappings': ['taxrank:1000000', 'ncbitaxon:has_rank']} })
    rankDataProvider: Optional[DataProvider] = Field(default=None, title="rank data provider", description="""The data provider for the description of the taxonomic ranks used in this taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'rankDataProvider', 'domain_of': ['Taxonomy']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class DataProvider(DataService):
    """
    An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['schema:EntryPoint', 'schema:EntryPoint'],
         'close_mappings': ['wd:Q122625839',
                            'ncit:C205367',
                            'wd:Q122625839',
                            'ncit:C205367'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'contentType': {'comments': ['This property characterizes how '
                                                     'the content is structured or '
                                                     'encoded, independent of the '
                                                     'entity type it represents. '
                                                     'Values should use MIME types '
                                                     '(e.g. application/json, '
                                                     'text/csv, '
                                                     'text/tab-separated-values, '
                                                     'text/x-fasta, '
                                                     'application/vnd.genbank)'],
                                        'description': 'The content type of the '
                                                       'response to queries. It '
                                                       'specifies the serialization, '
                                                       'file type, or media type used '
                                                       'to convey the resource, '
                                                       'typically expressed as a MIME '
                                                       'type following IANA media type '
                                                       'registrations',
                                        'domain_of': ['DataProvider'],
                                        'exact_mappings': ['schema:contentType',
                                                           'dct:format'],
                                        'ifabsent': 'string(application/json)',
                                        'multivalued': False,
                                        'name': 'contentType',
                                        'range': 'string',
                                        'required': True,
                                        'title': 'content type'},
                        'license': {'close_mappings': ['wdp:P275'],
                                    'description': 'Information about terms and '
                                                   'conditions under which the subject '
                                                   'can be used, shared, or '
                                                   'distributed, indicating any '
                                                   'restrictions or permissions',
                                    'domain_of': ['DataProvider', 'File'],
                                    'exact_mappings': ['schema:license'],
                                    'multivalued': False,
                                    'name': 'license',
                                    'range': 'License',
                                    'required': False,
                                    'slot_uri': 'dct:license',
                                    'title': 'license'},
                        'loginRequestMethod': {'broad_mappings': ['schema:httpMethod'],
                                               'close_mappings': ['dcat:endpointDescription'],
                                               'description': 'The http request method '
                                                              'used to acces the login '
                                                              'request url',
                                               'domain_of': ['DataProvider'],
                                               'ifabsent': 'string(GET)',
                                               'multivalued': False,
                                               'name': 'loginRequestMethod',
                                               'range': 'string',
                                               'required': False,
                                               'title': 'login request method'},
                        'loginTokenName': {'close_mappings': ['dcat:endpointDescription'],
                                           'description': 'The name of the token, '
                                                          'unique identifier of an '
                                                          'interaction session, that '
                                                          'will have to be reused as '
                                                          'credential in the query',
                                           'domain_of': ['DataProvider'],
                                           'multivalued': False,
                                           'name': 'loginTokenName',
                                           'range': 'string',
                                           'required': False,
                                           'title': 'login token name'},
                        'loginUrl': {'broad_mappings': ['schema:urlTemplate'],
                                     'close_mappings': ['wdp:P1630',
                                                        'dcat:endpointDescription'],
                                     'description': 'The URL template that allows to '
                                                    'log in if required',
                                     'domain_of': ['DataProvider'],
                                     'multivalued': False,
                                     'name': 'loginUrl',
                                     'range': 'uri',
                                     'required': False,
                                     'title': 'login URL'},
                        'providedEntityType': {'close_mappings': ['dct:type',
                                                                  'schema:additionalType'],
                                               'comments': ['This property defines '
                                                            'what the response is '
                                                            'about, independent of its '
                                                            'serialization. Values '
                                                            'should be ontology class '
                                                            'IRIs (e.g. '
                                                            'https://w3id.org/evorao/Virus)'],
                                               'description': 'Identifies the type of '
                                                              'entity (ontology class) '
                                                              'described by the '
                                                              'response to a query. '
                                                              'Values should be '
                                                              'expressed as IRIs '
                                                              '(e.g., from an '
                                                              'ontology)',
                                               'domain_of': ['DataProvider'],
                                               'multivalued': True,
                                               'name': 'providedEntityType',
                                               'range': 'uri',
                                               'related_mappings': ['dcat:servesDataset'],
                                               'required': True,
                                               'title': 'provided entity type'},
                        'queryMethod': {'broad_mappings': ['schema:httpMethod'],
                                        'close_mappings': ['dcat:endpointDescription'],
                                        'description': 'The http request method used '
                                                       'to access the requested query '
                                                       'url',
                                        'domain_of': ['DataProvider'],
                                        'multivalued': False,
                                        'name': 'queryMethod',
                                        'range': 'string',
                                        'required': True,
                                        'title': 'query method'},
                        'weight': {'close_mappings': ['adms:status'],
                                   'comments': ['The lowest weighted Data providers '
                                                'are triggered first, this may be '
                                                'usefull to populate at first entities '
                                                'that are referenced by others (e.g. '
                                                'Version ahead of Rank ahead of '
                                                'Taxon)'],
                                   'description': 'A numerical value indicating '
                                                  'relative importance or priority, '
                                                  'generally processed in ascending '
                                                  'order. This weight helps prioritize '
                                                  'content when organizing or '
                                                  'processing data. Its value can be '
                                                  'negative, with a default set to 0',
                                   'domain_of': ['DataProvider', 'Term'],
                                   'multivalued': False,
                                   'name': 'weight',
                                   'range': 'integer',
                                   'required': True,
                                   'title': 'weight'}},
         'title': 'Data provider'})

    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['DataProvider', 'File'],
         'exact_mappings': ['schema:license'],
         'slot_uri': 'dct:license'} })
    loginRequestMethod: Optional[Literal["GET", "POST"]] = Field(default="GET", title="login request method", description="""The http request method used to acces the login request url""", json_schema_extra = { "linkml_meta": {'alias': 'loginRequestMethod',
         'broad_mappings': ['schema:httpMethod'],
         'close_mappings': ['dcat:endpointDescription'],
         'domain_of': ['DataProvider'],
         'equals_string_in': ['GET', 'POST'],
         'ifabsent': 'string(GET)'} })
    loginUrl: Optional[str] = Field(default=None, title="login URL", description="""The URL template that allows to log in if required""", json_schema_extra = { "linkml_meta": {'alias': 'loginUrl',
         'broad_mappings': ['schema:urlTemplate'],
         'close_mappings': ['wdp:P1630', 'dcat:endpointDescription'],
         'domain_of': ['DataProvider']} })
    loginTokenName: Optional[str] = Field(default=None, title="login token name", description="""The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query""", json_schema_extra = { "linkml_meta": {'alias': 'loginTokenName',
         'close_mappings': ['dcat:endpointDescription'],
         'domain_of': ['DataProvider']} })
    queryMethod: Literal["GET", "POST"] = Field(default=..., title="query method", description="""The http request method used to access the requested query url""", json_schema_extra = { "linkml_meta": {'alias': 'queryMethod',
         'broad_mappings': ['schema:httpMethod'],
         'close_mappings': ['dcat:endpointDescription'],
         'domain_of': ['DataProvider'],
         'equals_string_in': ['GET', 'POST']} })
    contentType: str = Field(default="application/json", title="content type", description="""The content type of the response to queries. It specifies the serialization, file type, or media type used to convey the resource, typically expressed as a MIME type following IANA media type registrations""", json_schema_extra = { "linkml_meta": {'alias': 'contentType',
         'comments': ['This property characterizes how the content is structured or '
                      'encoded, independent of the entity type it represents. Values '
                      'should use MIME types (e.g. application/json, text/csv, '
                      'text/tab-separated-values, text/x-fasta, '
                      'application/vnd.genbank)'],
         'domain_of': ['DataProvider'],
         'exact_mappings': ['schema:contentType', 'dct:format'],
         'ifabsent': 'string(application/json)'} })
    providedEntityType: list[str] = Field(default=..., title="provided entity type", description="""Identifies the type of entity (ontology class) described by the response to a query. Values should be expressed as IRIs (e.g., from an ontology)""", json_schema_extra = { "linkml_meta": {'alias': 'providedEntityType',
         'close_mappings': ['dct:type', 'schema:additionalType'],
         'comments': ['This property defines what the response is about, independent '
                      'of its serialization. Values should be ontology class IRIs '
                      '(e.g. https://w3id.org/evorao/Virus)'],
         'domain_of': ['DataProvider'],
         'related_mappings': ['dcat:servesDataset']} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['DataProvider', 'Term'],
         'ifabsent': 'int(0)'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['DataService',
                       'Dataset',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['DataService',
                       'Dataset',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    endpointUrl: str = Field(default=..., title="endpoint URL", description="""The URL template that allows to get the content""", json_schema_extra = { "linkml_meta": {'alias': 'endpointUrl',
         'close_mappings': ['wdp:P1630'],
         'domain_of': ['DataService'],
         'exact_mappings': ['schema:urlTemplate'],
         'slot_uri': 'dcat:endpointURL'} })
    servesDataset: Optional[list[Dataset]] = Field(default=None, title="serves dataset", description="""A collection of data that this data service can distribute""", json_schema_extra = { "linkml_meta": {'alias': 'servesDataset',
         'comments': ['This property rather intends to point towards Catalogues as '
                      'collections of Datasets'],
         'domain_of': ['DataService'],
         'recommended': True,
         'slot_uri': 'dcat:servesDataset'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class PathogenIdentification(Resource):
    """
    A collection of distinguishing information that enables the differentiation of a pathogen from another
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dwc:Identification', 'dwc:Identification'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'genotype': {'close_mappings': ['geno:0000222'],
                                     'description': 'Genotype information that '
                                                    'identifies organisms that cluster '
                                                    'in phylogenetic trees, thus '
                                                    'different clusters are distinct '
                                                    'genotypes',
                                     'domain_of': ['PathogenIdentification'],
                                     'multivalued': False,
                                     'name': 'genotype',
                                     'range': 'string',
                                     'required': False,
                                     'title': 'genotype'},
                        'hostType': {'description': 'Indication of the possible '
                                                    'host(s) for the identified '
                                                    'pathogens among the listed main '
                                                    'categories',
                                     'domain_of': ['PathogenIdentification'],
                                     'multivalued': True,
                                     'name': 'hostType',
                                     'range': 'string',
                                     'recommended': True,
                                     'required': False,
                                     'title': 'host type'},
                        'isolate': {'description': 'Identifier given to a pathogen '
                                                   'that has been isolated from an '
                                                   'infected host and propagated in a '
                                                   'laboratory culture. The isolate '
                                                   'information may include an '
                                                   'internal reference code from the '
                                                   'laboratory that took the sample or '
                                                   'performed the isolation, as well '
                                                   'as details about the specific '
                                                   'conditions of isolation, such as '
                                                   'the name of the town, hospital, '
                                                   'and type of host',
                                    'domain_of': ['PathogenIdentification'],
                                    'multivalued': False,
                                    'name': 'isolate',
                                    'range': 'string',
                                    'required': False,
                                    'title': 'isolate'},
                        'pathogenName': {'description': 'A pathogen common name or a '
                                                        'name that describes a group '
                                                        'of pathogens',
                                         'domain_of': ['PathogenIdentification'],
                                         'exact_mappings': ['dwc:organismName'],
                                         'multivalued': False,
                                         'name': 'pathogenName',
                                         'range': 'CommonName',
                                         'required': True,
                                         'title': 'pathogen name'},
                        'pathogenType': {'close_mappings': ['dwc:organismScope'],
                                         'description': 'Identification of the '
                                                        'specific type of pathogen '
                                                        'among the listed categories '
                                                        'e.g. '
                                                        "'Virus','Viroid','Bacterium'...",
                                         'domain_of': ['PathogenIdentification'],
                                         'exact_mappings': ['schema:infectiousAgentClass'],
                                         'multivalued': False,
                                         'name': 'pathogenType',
                                         'range': 'string',
                                         'required': True,
                                         'title': 'pathogen type'},
                        'serotype': {'description': 'Genetically related pathogens '
                                                    'that group together based on '
                                                    'serological relationships',
                                     'domain_of': ['PathogenIdentification'],
                                     'multivalued': False,
                                     'name': 'serotype',
                                     'range': 'string',
                                     'required': False,
                                     'title': 'serotype'},
                        'strain': {'description': 'Identifier given to a genetic '
                                                  'variant within a single species',
                                   'domain_of': ['PathogenIdentification'],
                                   'multivalued': False,
                                   'name': 'strain',
                                   'range': 'string',
                                   'recommended': True,
                                   'required': False,
                                   'title': 'strain'},
                        'subspecies': {'description': 'The subspecies information '
                                                      'differentiates closely related '
                                                      'pathogens within a single '
                                                      'species',
                                       'domain_of': ['PathogenIdentification'],
                                       'multivalued': False,
                                       'name': 'subspecies',
                                       'range': 'string',
                                       'required': False,
                                       'title': 'subspecies'},
                        'taxon': {'close_mappings': ['schema:taxonomicRange',
                                                     'dwc:taxonID',
                                                     'dwc:toTaxon'],
                                  'comments': ['The taxon of the highest rank known '
                                               'that can be used to classify a '
                                               'pathogen or group of pathogens (e.g '
                                               'viruses) in the reference taxonomy'],
                                  'description': 'Scientifically classified group or '
                                                 'entity within the reference taxonomy',
                                  'domain_of': ['PathogenIdentification',
                                                'Taxonomy',
                                                'ClinicalGroup'],
                                  'multivalued': False,
                                  'name': 'taxon',
                                  'range': 'Taxon',
                                  'related_mappings': ['dwc:Taxon'],
                                  'required': True,
                                  'title': 'taxon'},
                        'variant': {'description': 'An organism with one or more new '
                                                   'mutations is referred to as a '
                                                   '“variant” of the original organism '
                                                   'if not sufficiently different to '
                                                   'be termed a distinct strain',
                                    'domain_of': ['PathogenIdentification'],
                                    'multivalued': False,
                                    'name': 'variant',
                                    'range': 'Variant',
                                    'required': False,
                                    'title': 'variant'}},
         'title': 'Pathogen identification'})

    taxon: Taxon = Field(default=..., title="taxon", description="""Scientifically classified group or entity within the reference taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'close_mappings': ['schema:taxonomicRange', 'dwc:taxonID', 'dwc:toTaxon'],
         'comments': ['The taxon of the highest rank known that can be used to '
                      'classify a pathogen or group of pathogens (e.g viruses) in the '
                      'reference taxonomy'],
         'domain_of': ['PathogenIdentification', 'Taxonomy', 'ClinicalGroup'],
         'related_mappings': ['dwc:Taxon']} })
    pathogenName: CommonName = Field(default=..., title="pathogen name", description="""A pathogen common name or a name that describes a group of pathogens""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenName',
         'domain_of': ['PathogenIdentification'],
         'exact_mappings': ['dwc:organismName']} })
    pathogenType: Literal["Virus", "Bacterium", "Fungus", "Protozoan", "Viroid", "Prion"] = Field(default=..., title="pathogen type", description="""Identification of the specific type of pathogen among the listed categories e.g. 'Virus','Viroid','Bacterium'...""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenType',
         'close_mappings': ['dwc:organismScope'],
         'domain_of': ['PathogenIdentification'],
         'equals_string_in': ['Virus',
                              'Bacterium',
                              'Fungus',
                              'Protozoan',
                              'Viroid',
                              'Prion'],
         'exact_mappings': ['schema:infectiousAgentClass']} })
    hostType: Optional[list[Literal["Animal", "Human", "Plant"]]] = Field(default=None, title="host type", description="""Indication of the possible host(s) for the identified pathogens among the listed main categories""", json_schema_extra = { "linkml_meta": {'alias': 'hostType',
         'domain_of': ['PathogenIdentification'],
         'equals_string_in': ['Animal', 'Human', 'Plant'],
         'recommended': True} })
    subspecies: Optional[str] = Field(default=None, title="subspecies", description="""The subspecies information differentiates closely related pathogens within a single species""", json_schema_extra = { "linkml_meta": {'alias': 'subspecies', 'domain_of': ['PathogenIdentification']} })
    strain: Optional[str] = Field(default=None, title="strain", description="""Identifier given to a genetic variant within a single species""", json_schema_extra = { "linkml_meta": {'alias': 'strain',
         'domain_of': ['PathogenIdentification'],
         'recommended': True} })
    isolate: Optional[str] = Field(default=None, title="isolate", description="""Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host""", json_schema_extra = { "linkml_meta": {'alias': 'isolate', 'domain_of': ['PathogenIdentification']} })
    genotype: Optional[str] = Field(default=None, title="genotype", description="""Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes""", json_schema_extra = { "linkml_meta": {'alias': 'genotype',
         'close_mappings': ['geno:0000222'],
         'domain_of': ['PathogenIdentification']} })
    serotype: Optional[str] = Field(default=None, title="serotype", description="""Genetically related pathogens that group together based on serological relationships""", json_schema_extra = { "linkml_meta": {'alias': 'serotype', 'domain_of': ['PathogenIdentification']} })
    variant: Optional[Variant] = Field(default=None, title="variant", description="""An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain""", json_schema_extra = { "linkml_meta": {'alias': 'variant', 'domain_of': ['PathogenIdentification']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Publication(Resource):
    """
    A scientific publication
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q591041',
                            'reproduceme:Publication',
                            'wd:Q591041',
                            'reproduceme:Publication'],
         'exact_mappings': ['dct:BibliographicResource', 'dct:BibliographicResource'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'abstract': {'close_mappings': ['dct:abstract',
                                                        'schema:abstract'],
                                     'description': 'Concise summary of the '
                                                    'publication',
                                     'domain_of': ['Publication'],
                                     'multivalued': False,
                                     'name': 'abstract',
                                     'range': 'string',
                                     'required': True,
                                     'title': 'abstract'},
                        'authors': {'close_mappings': ['wdp:P2093', 'schema:author'],
                                    'description': 'The list of authors',
                                    'domain_of': ['Publication'],
                                    'multivalued': False,
                                    'name': 'authors',
                                    'range': 'string',
                                    'related_mappings': ['sio:001315', 'iao:0000321'],
                                    'required': True,
                                    'title': 'authors'},
                        'doi': {'broad_mappings': ['dct:bibliographicCitation'],
                                'close_mappings': ['reproduceme:doi'],
                                'description': 'A Digital Object Identifier (DOI) that '
                                               'can be related',
                                'domain_of': ['Publication', 'ProductOrService'],
                                'exact_mappings': ['wdp:P356'],
                                'multivalued': False,
                                'name': 'doi',
                                'range': 'Doi',
                                'required': True,
                                'title': 'DOI'},
                        'journal': {'close_mappings': ['wdp:P1433',
                                                       'biolink:published_in',
                                                       'uniprotrdfs:publishedIn'],
                                    'description': 'The scientific journal in which '
                                                   'the publication was published',
                                    'domain_of': ['Publication'],
                                    'multivalued': False,
                                    'name': 'journal',
                                    'range': 'Journal',
                                    'required': False,
                                    'title': 'journal'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['Publication',
                                                'Dataset',
                                                'DataService',
                                                'Term',
                                                'License',
                                                'Certification'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'}},
         'title': 'Publication'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Publication',
                       'Dataset',
                       'DataService',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    authors: str = Field(default=..., title="authors", description="""The list of authors""", json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'close_mappings': ['wdp:P2093', 'schema:author'],
         'domain_of': ['Publication'],
         'related_mappings': ['sio:001315', 'iao:0000321']} })
    abstract: str = Field(default=..., title="abstract", description="""Concise summary of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'abstract',
         'close_mappings': ['dct:abstract', 'schema:abstract'],
         'domain_of': ['Publication']} })
    doi: Doi = Field(default=..., title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['reproduceme:doi'],
         'domain_of': ['Publication', 'ProductOrService'],
         'exact_mappings': ['wdp:P356']} })
    journal: Optional[Journal] = Field(default=None, title="journal", description="""The scientific journal in which the publication was published""", json_schema_extra = { "linkml_meta": {'alias': 'journal',
         'close_mappings': ['wdp:P1433',
                            'biolink:published_in',
                            'uniprotrdfs:publishedIn'],
         'domain_of': ['Publication']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Vocabulary(Catalogue):
    """
    A subset of words or phrases specific to a particular subject or field
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['skos:Collection', 'skos:Collection'],
         'close_mappings': ['wd:Q1391494',
                            'wd:Q6537693',
                            'wd:Q8380731',
                            'wd:Q1391494',
                            'wd:Q6537693',
                            'wd:Q8380731'],
         'exact_mappings': ['sio:001080', 'sio:001080'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['t4fs:0000335',
                              'wd:Q6499736',
                              't4fs:0000335',
                              'wd:Q6499736'],
         'slot_usage': {'term': {'description': 'The terms related to this vocabulary',
                                 'domain_of': ['Vocabulary'],
                                 'multivalued': True,
                                 'name': 'term',
                                 'range': 'Term',
                                 'recommended': True,
                                 'related_mappings': ['dct:hasPart'],
                                 'required': False,
                                 'title': 'term'},
                        'termDataProvider': {'description': 'An external API or '
                                                            'Endpoint that permits to '
                                                            'retrieve the terms of '
                                                            'this vocabulary',
                                             'domain_of': ['Vocabulary'],
                                             'multivalued': False,
                                             'name': 'termDataProvider',
                                             'range': 'DataProvider',
                                             'required': False,
                                             'title': 'term data provider'}},
         'title': 'Vocabulary'})

    termDataProvider: Optional[DataProvider] = Field(default=None, title="term data provider", description="""An external API or Endpoint that permits to retrieve the terms of this vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'termDataProvider', 'domain_of': ['Vocabulary']} })
    term: Optional[list[Term]] = Field(default=None, title="term", description="""The terms related to this vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Vocabulary'],
         'recommended': True,
         'related_mappings': ['dct:hasPart']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Term(Resource):
    """
    Word or phrase from a specialized area of knowledge
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['sio:000275',
                            'ncit:C45559',
                            'wd:Q1969448',
                            'sio:000275',
                            'ncit:C45559',
                            'wd:Q1969448'],
         'from_schema': 'https://w3id.org/evorao/',
         'narrow_mappings': ['wd:Q12812139', 'wd:Q12812139'],
         'slot_usage': {'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['Term',
                                                      'Dataset',
                                                      'DataService',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'ContactPoint',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'inVocabulary': {'broad_mappings': ['dct:isPartOf'],
                                         'close_mappings': ['wdp:P972'],
                                         'description': 'Terms belong to a specific '
                                                        'vocabulary',
                                         'domain_of': ['Term'],
                                         'multivalued': False,
                                         'name': 'inVocabulary',
                                         'range': 'Vocabulary',
                                         'related_mappings': ['dct:isReferencedBy'],
                                         'required': True,
                                         'title': 'in Vocabulary'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['Term',
                                                'Dataset',
                                                'DataService',
                                                'Publication',
                                                'License',
                                                'Certification'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'},
                        'weight': {'close_mappings': ['adms:status'],
                                   'description': 'A numerical value indicating '
                                                  'relative importance or priority, '
                                                  'generally processed in ascending '
                                                  'order. This weight helps prioritize '
                                                  'content when organizing or '
                                                  'processing data. Its value can be '
                                                  'negative, with a default set to 0',
                                   'domain_of': ['Term', 'DataProvider'],
                                   'ifabsent': 'int(0)',
                                   'multivalued': False,
                                   'name': 'weight',
                                   'range': 'integer',
                                   'required': True,
                                   'title': 'weight'}},
         'title': 'Term'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class CommonName(Term):
    """
    Vernacular name that is the name used in everyday language to refer to something like an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific or technical name
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sio:000118', 'sio:000118'],
         'exact_mappings': ['dwc:vernacularName',
                            'wd:Q502895',
                            'dwc:vernacularName',
                            'wd:Q502895'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'alternateName': {'close_mappings': ['wdp:P4970'],
                                          'comments': ['This includes previous names, '
                                                       'acronyms, former taxonomic '
                                                       'terms, and other variations. '
                                                       'This information can serve as '
                                                       'keywords for search purposes '
                                                       'and as a bridge with other '
                                                       'projects that use different '
                                                       'naming systems or taxonomies'],
                                          'description': 'Any other name under which '
                                                         'the entity can be known',
                                          'domain_of': ['CommonName',
                                                        'AlternateName',
                                                        'ClinicalGroup',
                                                        'Organization'],
                                          'exact_mappings': ['schema:alternateName',
                                                             'dct:alternative',
                                                             'iao:0000118'],
                                          'multivalued': True,
                                          'name': 'alternateName',
                                          'range': 'AlternateName',
                                          'required': False,
                                          'title': 'alternate name'},
                        'sourceOfInformation': {'close_mappings': ['wdp:P248'],
                                                'description': 'The name of the origin '
                                                               'from which knowledge '
                                                               'is obtained. This can '
                                                               'include any entity '
                                                               'that provides '
                                                               'information',
                                                'domain_of': ['CommonName',
                                                              'AlternateName'],
                                                'multivalued': True,
                                                'name': 'sourceOfInformation',
                                                'range': 'string',
                                                'required': False,
                                                'title': 'source of information'}},
         'title': 'Common name'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['CommonName', 'AlternateName', 'ClinicalGroup', 'Organization'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    sourceOfInformation: Optional[list[str]] = Field(default=None, title="source of information", description="""The name of the origin from which knowledge is obtained. This can include any entity that provides information""", json_schema_extra = { "linkml_meta": {'alias': 'sourceOfInformation',
         'close_mappings': ['wdp:P248'],
         'domain_of': ['CommonName', 'AlternateName'],
         'related_mappings': ['sio:000253']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class VirusName(CommonName):
    """
    A virus vernacular name or a name that describes a group of viruses
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dwc:vernacularName', 'dwc:vernacularName'],
         'exact_mappings': ['wd:Q125481078', 'wd:Q125481078'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Virus name'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['CommonName', 'AlternateName', 'ClinicalGroup', 'Organization'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    sourceOfInformation: Optional[list[str]] = Field(default=None, title="source of information", description="""The name of the origin from which knowledge is obtained. This can include any entity that provides information""", json_schema_extra = { "linkml_meta": {'alias': 'sourceOfInformation',
         'close_mappings': ['wdp:P248'],
         'domain_of': ['CommonName', 'AlternateName'],
         'related_mappings': ['sio:000253']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class AlternateName(Term):
    """
    List of other names for things
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q7662595', 'mi:1041', 'wd:Q7662595', 'mi:1041'],
         'exact_mappings': ['ncit:C52469', 'sio:000122', 'ncit:C52469', 'sio:000122'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'alternateName': {'close_mappings': ['wdp:P4970'],
                                          'comments': ['This includes previous names, '
                                                       'acronyms, former taxonomic '
                                                       'terms, and other variations. '
                                                       'This information can serve as '
                                                       'keywords for search purposes '
                                                       'and as a bridge with other '
                                                       'projects that use different '
                                                       'naming systems or taxonomies'],
                                          'description': 'Any other name under which '
                                                         'the entity can be known',
                                          'domain_of': ['AlternateName',
                                                        'CommonName',
                                                        'ClinicalGroup',
                                                        'Organization'],
                                          'exact_mappings': ['schema:alternateName',
                                                             'dct:alternative',
                                                             'iao:0000118'],
                                          'multivalued': True,
                                          'name': 'alternateName',
                                          'range': 'AlternateName',
                                          'required': False,
                                          'title': 'alternate name'},
                        'sourceOfInformation': {'close_mappings': ['wdp:P248'],
                                                'description': 'The name of the origin '
                                                               'from which knowledge '
                                                               'is obtained. This can '
                                                               'include any entity '
                                                               'that provides '
                                                               'information',
                                                'domain_of': ['AlternateName',
                                                              'CommonName'],
                                                'multivalued': True,
                                                'name': 'sourceOfInformation',
                                                'range': 'string',
                                                'related_mappings': ['sio:000253'],
                                                'required': False,
                                                'title': 'source of information'}},
         'title': 'Alternate name'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['AlternateName', 'CommonName', 'ClinicalGroup', 'Organization'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    sourceOfInformation: Optional[list[str]] = Field(default=None, title="source of information", description="""The name of the origin from which knowledge is obtained. This can include any entity that provides information""", json_schema_extra = { "linkml_meta": {'alias': 'sourceOfInformation',
         'close_mappings': ['wdp:P248'],
         'domain_of': ['AlternateName', 'CommonName'],
         'related_mappings': ['sio:000253']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class RiskGroup(Term):
    """
    Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['ncit:C95347', 'ncit:C95347'],
         'comments': ['Use of Data provider if any or manual import of information '
                      'from wd:Q125449389, wd:Q125449412, wd:Q125449429, '
                      'wd:Q125449439'],
         'exact_mappings': ['wd:Q125449255', 'wd:Q125449255'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Risk group'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Doi(Term):
    """
    A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wd:Q25670',
                            'ncit:C71462',
                            't4fs:0000434',
                            'obi:0002110',
                            'wd:Q25670',
                            'ncit:C71462',
                            't4fs:0000434',
                            'obi:0002110'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'DOI'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Journal(Term):
    """
    Periodical journal publishing scientific research
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wd:Q5633421',
                            'sio:000160',
                            'mi:0885',
                            'ncit:C40976',
                            'wd:Q5633421',
                            'sio:000160',
                            'mi:0885',
                            'ncit:C40976'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Journal'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class PdbReference(Term):
    """
    Identifier for 3D structural data as per the PDB (Protein Data Bank) database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['sio:010032', 'sio:010032'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['wdp:P638', 'wd:Q42415644', 'wdp:P638', 'wd:Q42415644'],
         'title': 'PDB reference'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Keyword(Term):
    """
    A term or phrase used to tag and categorize content
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wd:Q1128340',
                            'sio:000147',
                            'edam:0968',
                            'schema:DefinedTerm',
                            'wd:Q1128340',
                            'sio:000147',
                            'edam:0968',
                            'schema:DefinedTerm'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Keyword'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class TagSequence(Term):
    """
    The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q645590', 'wd:Q645590'],
         'comments': ['This class is used for controlled vocabulary terms (e.g., His '
                      'Cterm, His Nterm, MBP, GST, Strep, FLAG-Tag, SUMO ...) and not '
                      'the literal sequences'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Tag sequence'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class SpecialFeature(Term):
    """
    Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['These special features help researchers and professionals in '
                      'the field to select appropriate virus strains for their '
                      'specific research needs and applications.'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C73619', 'ncit:C73619'],
         'title': 'Special feature'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ExpressionVector(Term):
    """
    A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wd:Q5421712', 'obi:0000729', 'wd:Q5421712', 'obi:0000729'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['obi:0600063',
                              'reproduceme:ExpressionSystem',
                              'obi:0600063',
                              'reproduceme:ExpressionSystem'],
         'title': 'Expression vector'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class PlasmidSelection(Term):
    """
    The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['obi:0000729', 'obi:0000729'],
         'title': 'Plasmid selection'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class PropagationHost(Term):
    """
    The organism used to grow and multiply the pathogen under controlled conditions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['sio:010415', 'sio:010415'],
         'title': 'Propagation host'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class TransmissionMethod(Term):
    """
    The process by which the pathogen spreads between hosts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['ncit:C128376', 'ncit:C128376'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C17214', 'ncit:C17214'],
         'title': 'Transmission method'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ProductionCellLine(Term):
    """
    A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q21014462', 'wd:Q21014462'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C16403',
                              'clo:0000031',
                              'ncit:C16403',
                              'clo:0000031'],
         'title': 'Production cell line'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ProductCategory(Term):
    """
    A term used to classify a group of products that share common characteristics or functions, which helps in their organization
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['skos:ConceptScheme', 'skos:ConceptScheme'],
         'close_mappings': ['ncit:C25372', 'ncit:C25372'],
         'exact_mappings': ['wd:Q63981612', 'wd:Q63981612'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['schema:CategoryCode', 'schema:CategoryCode'],
         'slot_usage': {'parentCategory': {'broad_mappings': ['dct:isPartOf'],
                                           'description': 'An overarching category '
                                                          'that encompasses the '
                                                          'current category within a '
                                                          'hierarchical classification '
                                                          'system. It serves as the '
                                                          'top-level classification, '
                                                          'organizing related '
                                                          'subcategories under its '
                                                          'umbrella to create a '
                                                          'structured and logical '
                                                          'order.',
                                           'domain_of': ['ProductCategory'],
                                           'multivalued': False,
                                           'name': 'parentCategory',
                                           'range': 'ProductCategory',
                                           'required': False,
                                           'title': 'parent category'}},
         'title': 'Product category'})

    parentCategory: Optional[ProductCategory] = Field(default=None, title="parent category", description="""An overarching category that encompasses the current category within a hierarchical classification system. It serves as the top-level classification, organizing related subcategories under its umbrella to create a structured and logical order.""", json_schema_extra = { "linkml_meta": {'alias': 'parentCategory',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductCategory']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class IsolationHost(Term):
    """
    Host organism from which the pathogen was isolated
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/', 'title': 'Isolation host'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class GeographicalOrigin(Term):
    """
    The specific location or region where a physical item, originates or is naturally found
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['prov:Location',
                            'dct:Location',
                            'vcard:Location',
                            'prov:Location',
                            'dct:Location',
                            'vcard:Location'],
         'close_mappings': ['wd:Q3885844', 'wd:Q3885844'],
         'comments': ['geonames.org API could be a good service data provider as '
                      'suggested by DCAT-AP'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['schema:countryOfOrigin', 'schema:countryOfOrigin'],
         'title': 'Geographical origin'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class IplcOrigin(GeographicalOrigin):
    """
    The IPLC area (Indigenous People and Local Communities) from which a physical item originates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['ncit:C41152',
                            'mesh:D000081034',
                            'ncit:C41152',
                            'mesh:D000081034'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['dct:Location',
                              'vcard:Location',
                              'dct:Location',
                              'vcard:Location'],
         'title': 'IPLC origin'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Country(Term):
    """
    The country as of ISO3166
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['prov:Location',
                            'dct:Location',
                            'vcard:Location',
                            'prov:Location',
                            'dct:Location',
                            'vcard:Location'],
         'close_mappings': ['wd:Q6256', 'wd:Q6256'],
         'comments': ['Use of Data provider recommended... serve as a local cache for '
                      'ISO3166'],
         'exact_mappings': ['schema:Country',
                            'ncit:C25464',
                            'sio:000664',
                            'schema:Country',
                            'ncit:C25464',
                            'sio:000664'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'alpha2Code': {'close_mappings': ['schema:addressCountry'],
                                       'description': 'Two-letter country codes from '
                                                      'ISO 3166-1 alpha-2',
                                       'domain_of': ['Country'],
                                       'exact_mappings': ['geo:000000023'],
                                       'multivalued': False,
                                       'name': 'alpha2Code',
                                       'range': 'string',
                                       'related_mappings': ['obib:0000620',
                                                            'ncit:C54641'],
                                       'required': True,
                                       'title': 'alpha 2 code'}},
         'title': 'Country'})

    alpha2Code: str = Field(default=..., title="alpha 2 code", description="""Two-letter country codes from ISO 3166-1 alpha-2""", json_schema_extra = { "linkml_meta": {'alias': 'alpha2Code',
         'close_mappings': ['schema:addressCountry'],
         'domain_of': ['Country'],
         'exact_mappings': ['geo:000000023'],
         'related_mappings': ['obib:0000620', 'ncit:C54641']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class IataClassification(Term):
    """
    The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['wd:Q19755', 'wd:Q19755'],
         'title': 'IATA classification'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Variant(CommonName):
    """
    An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q104795308', 'wd:Q104795308'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Variant'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['CommonName', 'AlternateName', 'ClinicalGroup', 'Organization'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    sourceOfInformation: Optional[list[str]] = Field(default=None, title="source of information", description="""The name of the origin from which knowledge is obtained. This can include any entity that provides information""", json_schema_extra = { "linkml_meta": {'alias': 'sourceOfInformation',
         'close_mappings': ['wdp:P248'],
         'domain_of': ['CommonName', 'AlternateName'],
         'related_mappings': ['sio:000253']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class TaxonomicRank(Term):
    """
    The possible taxonomic ranks and their description
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['biolink:TaxonomicRank', 'biolink:TaxonomicRank'],
         'comments': ['Use of Data provider recommended'],
         'exact_mappings': ['taxrank:0000000',
                            'uniprotrdfs:Rank',
                            'wd:Q427626',
                            'taxrank:0000000',
                            'uniprotrdfs:Rank',
                            'wd:Q427626'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['dwc:taxonRank', 'dwc:taxonRank'],
         'slot_usage': {'taxonomy': {'broad_mappings': ['dct:isPartOf'],
                                     'description': 'The taxonomy release(s) in which '
                                                    'this entity exists',
                                     'domain_of': ['TaxonomicRank', 'Taxon'],
                                     'multivalued': True,
                                     'name': 'taxonomy',
                                     'range': 'Taxonomy',
                                     'required': False,
                                     'title': 'taxonomy'}},
         'title': 'Taxonomic rank'})

    taxonomy: Optional[list[Taxonomy]] = Field(default=None, title="taxonomy", description="""The taxonomy release(s) in which this entity exists""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomy',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['TaxonomicRank', 'Taxon'],
         'recommended': True} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Taxon(Term):
    """
    Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q16521',
                            'dwc:Taxon',
                            'uniprotrdfs:Taxon',
                            'wd:Q16521',
                            'dwc:Taxon',
                            'uniprotrdfs:Taxon'],
         'comments': ['The taxonomic taxons connected to their parent so that a full '
                      'lienage can be rebuild. Use of Data provider recommended'],
         'exact_mappings': ['schema:Taxon', 'schema:Taxon'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'externalEquivalentTaxon': {'close_mappings': ['dwc:taxonID'],
                                                    'comments': ['Could serve as a '
                                                                 'bridge between ICTV '
                                                                 'and NCBI as several '
                                                                 'providers currently '
                                                                 'uses NCBI Taxonomy'],
                                                    'description': 'Any equivalent '
                                                                   'taxon in a '
                                                                   'different taxonomy '
                                                                   'if exists/known to '
                                                                   'serve as a bridge '
                                                                   '(e.g, ICTV towards '
                                                                   'NCBI)',
                                                    'domain_of': ['Taxon'],
                                                    'multivalued': True,
                                                    'name': 'externalEquivalentTaxon',
                                                    'range': 'Taxon',
                                                    'related_mappings': ['dct:references'],
                                                    'required': False,
                                                    'title': 'external equivalent '
                                                             'taxon'},
                        'parentTaxon': {'broad_mappings': ['dwc:Taxon'],
                                        'close_mappings': ['wdp:P171'],
                                        'description': 'The parent taxon of the '
                                                       'current taxon',
                                        'domain_of': ['Taxon'],
                                        'exact_mappings': ['schema:parentTaxon'],
                                        'multivalued': False,
                                        'name': 'parentTaxon',
                                        'range': 'Taxon',
                                        'required': True,
                                        'title': 'parent taxon'},
                        'previouslyKnownAs': {'broad_mappings': ['dwc:Taxon'],
                                              'description': 'Any historic version of '
                                                             'this taxon having a '
                                                             'different name',
                                              'domain_of': ['Taxon'],
                                              'multivalued': True,
                                              'name': 'previouslyKnownAs',
                                              'range': 'Taxon',
                                              'related_mappings': ['schema:alternateName'],
                                              'required': False,
                                              'title': 'previously known as'},
                        'rank': {'close_mappings': ['dwc:taxonRank',
                                                    'schema:taxonRank',
                                                    'biolink:has_taxonomic_rank'],
                                 'description': 'Relative level or position of the '
                                                'identified taxon in the taxonomy',
                                 'domain_of': ['Taxon', 'Taxonomy'],
                                 'exact_mappings': ['wdp:P105'],
                                 'multivalued': False,
                                 'name': 'rank',
                                 'range': 'TaxonomicRank',
                                 'related_mappings': ['taxrank:1000000',
                                                      'ncbitaxon:has_rank'],
                                 'required': True,
                                 'title': 'rank'},
                        'taxonomicId': {'broad_mappings': ['schema:identifier',
                                                           'dct:identifier'],
                                        'description': 'The taxonomic identifier as a '
                                                       'persistent identifier accross '
                                                       'releases',
                                        'domain_of': ['Taxon'],
                                        'exact_mappings': ['dwc:taxonID'],
                                        'multivalued': False,
                                        'name': 'taxonomicId',
                                        'narrow_mappings': ['ncit:P331'],
                                        'range': 'string',
                                        'required': True,
                                        'title': 'taxonomic ID'},
                        'taxonomicNodeId': {'broad_mappings': ['dct:identifier'],
                                            'close_mappings': ['dwc:taxonID'],
                                            'comments': ['NCBI does not have a '
                                                         'taxon_node id, only a '
                                                         'taxonomicID. Taxon_node id '
                                                         'is Unique  in ICTV= Key of '
                                                         'the taxon node !! Could be '
                                                         'replaced by a composite key '
                                                         "made of 'taxonomic ID' + "
                                                         "'has version'"],
                                            'description': 'The taxonomic_Node '
                                                           'Identifier as an '
                                                           'identifier specific the '
                                                           'current taxon in the '
                                                           'corresponding '
                                                           'release/version of the '
                                                           'taxonomy',
                                            'domain_of': ['Taxon'],
                                            'multivalued': False,
                                            'name': 'taxonomicNodeId',
                                            'range': 'string',
                                            'recommended': True,
                                            'required': False,
                                            'title': 'taxonomic node ID'},
                        'taxonomy': {'broad_mappings': ['dct:isPartOf'],
                                     'description': 'The taxonomy release(s) in which '
                                                    'this entity exists',
                                     'domain_of': ['Taxon', 'TaxonomicRank'],
                                     'multivalued': True,
                                     'name': 'taxonomy',
                                     'range': 'Taxonomy',
                                     'recommended': True,
                                     'required': False,
                                     'title': 'taxonomy'}},
         'title': 'Taxon'})

    taxonomy: Optional[list[Taxonomy]] = Field(default=None, title="taxonomy", description="""The taxonomy release(s) in which this entity exists""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomy',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['Taxon', 'TaxonomicRank'],
         'recommended': True} })
    parentTaxon: Taxon = Field(default=..., title="parent taxon", description="""The parent taxon of the current taxon""", json_schema_extra = { "linkml_meta": {'alias': 'parentTaxon',
         'broad_mappings': ['dwc:Taxon'],
         'close_mappings': ['wdp:P171'],
         'domain_of': ['Taxon'],
         'exact_mappings': ['schema:parentTaxon']} })
    rank: TaxonomicRank = Field(default=..., title="rank", description="""Relative level or position of the identified taxon in the taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'rank',
         'close_mappings': ['dwc:taxonRank',
                            'schema:taxonRank',
                            'biolink:has_taxonomic_rank'],
         'domain_of': ['Taxon', 'Taxonomy'],
         'exact_mappings': ['wdp:P105'],
         'related_mappings': ['taxrank:1000000', 'ncbitaxon:has_rank']} })
    previouslyKnownAs: Optional[list[Taxon]] = Field(default=None, title="previously known as", description="""Any historic version of this taxon having a different name""", json_schema_extra = { "linkml_meta": {'alias': 'previouslyKnownAs',
         'broad_mappings': ['dwc:Taxon'],
         'domain_of': ['Taxon'],
         'related_mappings': ['schema:alternateName']} })
    externalEquivalentTaxon: Optional[list[Taxon]] = Field(default=None, title="external equivalent taxon", description="""Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)""", json_schema_extra = { "linkml_meta": {'alias': 'externalEquivalentTaxon',
         'close_mappings': ['dwc:taxonID'],
         'comments': ['Could serve as a bridge between ICTV and NCBI as several '
                      'providers currently uses NCBI Taxonomy'],
         'domain_of': ['Taxon'],
         'related_mappings': ['dct:references']} })
    taxonomicId: str = Field(default=..., title="taxonomic ID", description="""The taxonomic identifier as a persistent identifier accross releases""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomicId',
         'broad_mappings': ['schema:identifier', 'dct:identifier'],
         'domain_of': ['Taxon'],
         'exact_mappings': ['dwc:taxonID'],
         'narrow_mappings': ['ncit:P331']} })
    taxonomicNodeId: Optional[str] = Field(default=None, title="taxonomic node ID", description="""The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomicNodeId',
         'broad_mappings': ['dct:identifier'],
         'close_mappings': ['dwc:taxonID'],
         'comments': ['NCBI does not have a taxon_node id, only a taxonomicID. '
                      'Taxon_node id is Unique  in ICTV= Key of the taxon node !! '
                      "Could be replaced by a composite key made of 'taxonomic ID' + "
                      "'has version'"],
         'domain_of': ['Taxon'],
         'recommended': True} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ClinicalGroup(Term):
    """
    A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'alternateName': {'close_mappings': ['wdp:P4970'],
                                          'comments': ['This includes previous names, '
                                                       'acronyms, former taxonomic '
                                                       'terms, and other variations. '
                                                       'This information can serve as '
                                                       'keywords for search purposes '
                                                       'and as a bridge with other '
                                                       'projects that use different '
                                                       'naming systems or taxonomies'],
                                          'description': 'Any other name under which '
                                                         'the entity can be known',
                                          'domain_of': ['ClinicalGroup',
                                                        'CommonName',
                                                        'AlternateName',
                                                        'Organization'],
                                          'exact_mappings': ['schema:alternateName',
                                                             'dct:alternative',
                                                             'iao:0000118'],
                                          'multivalued': True,
                                          'name': 'alternateName',
                                          'range': 'AlternateName',
                                          'required': False,
                                          'title': 'alternate name'},
                        'taxon': {'close_mappings': ['schema:taxonomicRange',
                                                     'dwc:taxonID',
                                                     'dwc:toTaxon'],
                                  'description': 'Scientifically classified group or '
                                                 'entity within the reference taxonomy',
                                  'domain_of': ['ClinicalGroup',
                                                'Taxonomy',
                                                'PathogenIdentification'],
                                  'multivalued': True,
                                  'name': 'taxon',
                                  'range': 'Taxon',
                                  'related_mappings': ['dwc:Taxon'],
                                  'required': False,
                                  'title': 'taxon'}},
         'title': 'Clinical group'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['ClinicalGroup', 'CommonName', 'AlternateName', 'Organization'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    taxon: Optional[list[Taxon]] = Field(default=None, title="taxon", description="""Scientifically classified group or entity within the reference taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'close_mappings': ['schema:taxonomicRange', 'dwc:taxonID', 'dwc:toTaxon'],
         'comments': ['The taxon of the highest rank known that can be used to '
                      'classify a pathogen or group of pathogens (e.g viruses) in the '
                      'reference taxonomy'],
         'domain_of': ['ClinicalGroup', 'Taxonomy', 'PathogenIdentification'],
         'related_mappings': ['dwc:Taxon']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Term',
                       'Dataset',
                       'DataService',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    weight: int = Field(default=0, title="weight", description="""A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0""", json_schema_extra = { "linkml_meta": {'alias': 'weight',
         'close_mappings': ['adms:status'],
         'comments': ['The lowest weighted Data providers are triggered first, this '
                      'may be usefull to populate at first entities that are '
                      'referenced by others (e.g. Version ahead of Rank ahead of '
                      'Taxon)'],
         'domain_of': ['Term', 'DataProvider'],
         'ifabsent': 'int(0)'} })
    inVocabulary: Vocabulary = Field(default=..., title="in Vocabulary", description="""Terms belong to a specific vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'inVocabulary',
         'broad_mappings': ['dct:isPartOf'],
         'close_mappings': ['wdp:P972'],
         'domain_of': ['Term'],
         'related_mappings': ['dct:isReferencedBy']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ExternalRelatedReference(Resource):
    """
    A reference that permits to retrieve an item from an external provider
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['ms:1000878', 'ncit:C43621', 'ms:1000878', 'ncit:C43621'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'reference': {'close_mappings': ['dct:identifier',
                                                         'dct:references'],
                                      'description': 'The identifier reference of the '
                                                     'connected external item',
                                      'domain_of': ['ExternalRelatedReference'],
                                      'multivalued': False,
                                      'name': 'reference',
                                      'range': 'string',
                                      'required': True,
                                      'title': 'reference'},
                        'referenceLabel': {'close_mappings': ['dct:title'],
                                           'comments': ["e.g., 'Infravec2 related "
                                                        "product'"],
                                           'description': 'The label informing what '
                                                          'this reference is about',
                                           'domain_of': ['ExternalRelatedReference'],
                                           'multivalued': False,
                                           'name': 'referenceLabel',
                                           'range': 'string',
                                           'required': True,
                                           'title': 'reference label'},
                        'referenceProviderName': {'close_mappings': ['dct:publisher'],
                                                  'description': 'The name for the '
                                                                 'reference provider',
                                                  'domain_of': ['ExternalRelatedReference'],
                                                  'multivalued': False,
                                                  'name': 'referenceProviderName',
                                                  'range': 'string',
                                                  'required': True,
                                                  'title': 'reference provider name'},
                        'referenceProviderPrefix': {'description': 'The url prefix '
                                                                   'that once '
                                                                   'completed with the '
                                                                   'reference will '
                                                                   'lead to the linked '
                                                                   'external resource',
                                                    'domain_of': ['ExternalRelatedReference'],
                                                    'multivalued': False,
                                                    'name': 'referenceProviderPrefix',
                                                    'range': 'string',
                                                    'related_mappings': ['dcat:landingPage',
                                                                         'iao:0000599'],
                                                    'required': True,
                                                    'title': 'reference provider '
                                                             'prefix'}},
         'title': 'External related reference'})

    reference: str = Field(default=..., title="reference", description="""The identifier reference of the connected external item""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'close_mappings': ['dct:identifier', 'dct:references'],
         'domain_of': ['ExternalRelatedReference']} })
    referenceLabel: str = Field(default=..., title="reference label", description="""The label informing what this reference is about""", json_schema_extra = { "linkml_meta": {'alias': 'referenceLabel',
         'close_mappings': ['dct:title'],
         'comments': ["e.g., 'Infravec2 related product'"],
         'domain_of': ['ExternalRelatedReference']} })
    referenceProviderPrefix: str = Field(default=..., title="reference provider prefix", description="""The url prefix that once completed with the reference will lead to the linked external resource""", json_schema_extra = { "linkml_meta": {'alias': 'referenceProviderPrefix',
         'domain_of': ['ExternalRelatedReference'],
         'related_mappings': ['dcat:landingPage', 'iao:0000599']} })
    referenceProviderName: str = Field(default=..., title="reference provider name", description="""The name for the reference provider""", json_schema_extra = { "linkml_meta": {'alias': 'referenceProviderName',
         'close_mappings': ['dct:publisher'],
         'domain_of': ['ExternalRelatedReference']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Sequence(Resource):
    """
    A nucleic acid or protein sequence information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q3511065', 'wd:Q3511065'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['uniprotrdfs:Sequence', 'uniprotrdfs:Sequence'],
         'slot_usage': {'sequenceFasta': {'comments': ['In cases where no reference '
                                                       'sequence exists in public '
                                                       'repositories, the '
                                                       'corresponding FASTA sequence '
                                                       'is expected; otherwise, the '
                                                       'reference sequence is '
                                                       'sufficient. In FASTA format '
                                                       'the line before the nucleotide '
                                                       'sequence, called the FASTA '
                                                       'definition line, must begin '
                                                       "with a charater ('>'), "
                                                       'followed by a unique SeqID '
                                                       '(sequence identifier). In case '
                                                       'the sequence is made of '
                                                       'multiple parts several fasta '
                                                       'sequences can be provided'],
                                          'description': 'Textual encoding of a '
                                                         'biological sequence '
                                                         'information in FASTA format',
                                          'domain_of': ['Sequence'],
                                          'multivalued': False,
                                          'name': 'sequenceFasta',
                                          'range': 'string',
                                          'required': False,
                                          'title': 'sequence FASTA'},
                        'sequenceReference': {'description': 'A reference that permits '
                                                             'to retrieve the sequence '
                                                             'information from a '
                                                             'sequence provider',
                                              'domain_of': ['Sequence', 'Antibody'],
                                              'multivalued': True,
                                              'name': 'sequenceReference',
                                              'range': 'SequenceReference',
                                              'recommended': True,
                                              'required': False,
                                              'title': 'sequence reference'}},
         'title': 'Sequence'})

    sequenceReference: Optional[list[SequenceReference]] = Field(default=None, title="sequence reference", description="""A reference that permits to retrieve the sequence information from a sequence provider""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceReference',
         'domain_of': ['Sequence', 'Antibody'],
         'recommended': True} })
    sequenceFasta: Optional[str] = Field(default=None, title="sequence FASTA", description="""Textual encoding of a biological sequence information in FASTA format""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceFasta',
         'comments': ['In cases where no reference sequence exists in public '
                      'repositories, the corresponding FASTA sequence is expected; '
                      'otherwise, the reference sequence is sufficient. In FASTA '
                      'format the line before the nucleotide sequence, called the '
                      "FASTA definition line, must begin with a charater ('>'), "
                      'followed by a unique SeqID (sequence identifier). In case the '
                      'sequence is made of multiple parts several fasta sequences can '
                      'be provided'],
         'domain_of': ['Sequence']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class SequenceReference(Resource):
    """
    A reference that permits to retrieve the sequence information from a sequence provider
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A work on making it a subclass of External related reference '
                      'might be consistent and beneficial for data structuration but '
                      'special attention will have to be take to ensure it remains '
                      'consistent with the actual the use cases for users'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'accessionNumber': {'broad_mappings': ['schema:identifier'],
                                            'description': 'The sequence ID that '
                                                           'permits to retrieve the '
                                                           'sequence information from '
                                                           'the sequence provider',
                                            'domain_of': ['SequenceReference'],
                                            'multivalued': False,
                                            'name': 'accessionNumber',
                                            'narrow_mappings': ['ncit:P102'],
                                            'range': 'string',
                                            'related_mappings': ['dct:identifier'],
                                            'required': True,
                                            'title': 'accession number'},
                        'sequenceProvider': {'close_mappings': ['dct:publisher'],
                                             'description': 'The name of the sequence '
                                                            'provider within the list '
                                                            'of accepted sequence '
                                                            'providers',
                                             'domain_of': ['SequenceReference'],
                                             'multivalued': False,
                                             'name': 'sequenceProvider',
                                             'range': 'string',
                                             'required': True,
                                             'title': 'sequence provider'}},
         'title': 'Sequence reference'})

    accessionNumber: str = Field(default=..., title="accession number", description="""The sequence ID that permits to retrieve the sequence information from the sequence provider""", json_schema_extra = { "linkml_meta": {'alias': 'accessionNumber',
         'broad_mappings': ['schema:identifier'],
         'domain_of': ['SequenceReference'],
         'narrow_mappings': ['ncit:P102'],
         'related_mappings': ['dct:identifier']} })
    sequenceProvider: Literal["ENA", "GenBank"] = Field(default=..., title="sequence provider", description="""The name of the sequence provider within the list of accepted sequence providers""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceProvider',
         'close_mappings': ['dct:publisher'],
         'domain_of': ['SequenceReference'],
         'equals_string_in': ['ENA', 'GenBank']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class PersonOrOrganization(Resource):
    """
    A person or an organization
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Agent',
         'close_mappings': ['vcard:Agent', 'vcard:Agent'],
         'exact_mappings': ['dct:Agent', 'prov:Agent', 'dct:Agent', 'prov:Agent'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'contactPoint': {'description': 'An information that allows '
                                                        'someone to establish '
                                                        'communication',
                                         'domain_of': ['PersonOrOrganization',
                                                       'ProductOrService'],
                                         'exact_mappings': ['schema:contactPoint'],
                                         'multivalued': False,
                                         'name': 'contactPoint',
                                         'range': 'ContactPoint',
                                         'recommended': True,
                                         'required': False,
                                         'slot_uri': 'dcat:contactPoint',
                                         'title': 'contact point'},
                        'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['PersonOrOrganization',
                                                      'Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'File',
                                                      'ContactPoint',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'homePage': {'close_mappings': ['swo:0004006'],
                                     'description': 'A web page that serves as the '
                                                    'main or introductory page',
                                     'domain_of': ['PersonOrOrganization'],
                                     'multivalued': False,
                                     'name': 'homePage',
                                     'range': 'uri',
                                     'required': False,
                                     'slot_uri': 'foaf:homepage',
                                     'title': 'home page'},
                        'logo': {'description': 'A path or URL to the related logo',
                                 'domain_of': ['PersonOrOrganization',
                                               'License',
                                               'Certification'],
                                 'exact_mappings': ['schema:logo'],
                                 'multivalued': False,
                                 'name': 'logo',
                                 'range': 'Image',
                                 'required': False,
                                 'title': 'logo'},
                        'name': {'close_mappings': ['rdfs:label', 'dct:title'],
                                 'description': 'A word or set of words used to '
                                                'identify and refer to an entity',
                                 'domain_of': ['PersonOrOrganization',
                                               'File',
                                               'ContactPoint'],
                                 'exact_mappings': ['schema:name', 'vcard:fn'],
                                 'multivalued': False,
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True,
                                 'slot_uri': 'foaf:name',
                                 'title': 'name'}},
         'title': 'Person or organization'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Person(PersonOrOrganization):
    """
    An individual
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Person',
         'close_mappings': ['wd:Q215627',
                            'vcard:Individual',
                            'wd:Q215627',
                            'vcard:Individual'],
         'exact_mappings': ['schema:Person', 'schema:Person'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'orcidId': {'description': 'Unique persistent identifier for a '
                                                   'person, provided by the Open '
                                                   'Researcher and Contributor ID '
                                                   '(ORCID) organisation',
                                    'domain_of': ['Person', 'ContactPoint'],
                                    'exact_mappings': ['wdp:P496', 'reproduceme:ORCID'],
                                    'multivalued': False,
                                    'name': 'orcidId',
                                    'range': 'string',
                                    'recommended': True,
                                    'related_mappings': ['iao:0000708', 'edam:4022'],
                                    'required': False,
                                    'title': 'ORCID id'}},
         'title': 'Person'})

    orcidId: Optional[str] = Field(default=None, title="ORCID id", description="""Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation""", json_schema_extra = { "linkml_meta": {'alias': 'orcidId',
         'domain_of': ['Person', 'ContactPoint'],
         'exact_mappings': ['wdp:P496', 'reproduceme:ORCID'],
         'recommended': True,
         'related_mappings': ['iao:0000708', 'edam:4022']} })
    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Organization(PersonOrOrganization):
    """
    A social entity established to meet needs or pursue specific goals
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Organization',
         'close_mappings': ['wd:Q43229', 'wd:Q43229'],
         'exact_mappings': ['schema:Organization',
                            'vcard:Organization',
                            'schema:Organization',
                            'vcard:Organization'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'alternateName': {'close_mappings': ['wdp:P4970'],
                                          'comments': ['This includes previous names, '
                                                       'acronyms, former taxonomic '
                                                       'terms, and other variations. '
                                                       'This information can serve as '
                                                       'keywords for search purposes '
                                                       'and as a bridge with other '
                                                       'projects that use different '
                                                       'naming systems or taxonomies'],
                                          'description': 'Any other name under which '
                                                         'the entity can be known',
                                          'domain_of': ['Organization',
                                                        'CommonName',
                                                        'AlternateName',
                                                        'ClinicalGroup'],
                                          'exact_mappings': ['schema:alternateName',
                                                             'dct:alternative',
                                                             'iao:0000118'],
                                          'multivalued': True,
                                          'name': 'alternateName',
                                          'range': 'AlternateName',
                                          'required': False,
                                          'title': 'alternate name'},
                        'country': {'description': 'The country of the organization',
                                    'domain_of': ['Organization'],
                                    'multivalued': False,
                                    'name': 'country',
                                    'range': 'Country',
                                    'recommended': True,
                                    'required': False,
                                    'title': 'country'},
                        'rorId': {'description': "The corresponding organization's "
                                                 'persistent identifier from the '
                                                 'Research Organization Registry (ROR)',
                                  'domain_of': ['Organization'],
                                  'exact_mappings': ['wdp:P6782'],
                                  'multivalued': False,
                                  'name': 'rorId',
                                  'range': 'string',
                                  'recommended': True,
                                  'related_mappings': ['dwc:institutionCode'],
                                  'required': False,
                                  'title': 'ROR iD'}},
         'title': 'Organization'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['Organization', 'CommonName', 'AlternateName', 'ClinicalGroup'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    country: Optional[Country] = Field(default=None, title="country", description="""The country of the organization""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Organization'], 'recommended': True} })
    rorId: Optional[str] = Field(default=None, title="ROR iD", description="""The corresponding organization's persistent identifier from the Research Organization Registry (ROR)""", json_schema_extra = { "linkml_meta": {'alias': 'rorId',
         'domain_of': ['Organization'],
         'exact_mappings': ['wdp:P6782'],
         'recommended': True,
         'related_mappings': ['dwc:institutionCode']} })
    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ReasearchInfrastructure(Organization):
    """
    A research infrastructure (RI)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q1438053', 'wd:Q1438053'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['foaf:Organization',
                              'ncit:C19158',
                              'foaf:Organization',
                              'ncit:C19158'],
         'title': 'Reasearch infrastructure'})

    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['Organization', 'CommonName', 'AlternateName', 'ClinicalGroup'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    country: Optional[Country] = Field(default=None, title="country", description="""The country of the organization""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Organization'], 'recommended': True} })
    rorId: Optional[str] = Field(default=None, title="ROR iD", description="""The corresponding organization's persistent identifier from the Research Organization Registry (ROR)""", json_schema_extra = { "linkml_meta": {'alias': 'rorId',
         'domain_of': ['Organization'],
         'exact_mappings': ['wdp:P6782'],
         'recommended': True,
         'related_mappings': ['dwc:institutionCode']} })
    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Provider(Organization):
    """
    A provider of products or services, as a specific organization
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['ncit:C37900', 'ncit:C37900'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['foaf:Organization',
                              'dct:ProvenanceStatement',
                              'foaf:Organization',
                              'dct:ProvenanceStatement'],
         'slot_usage': {'memberOfRi': {'broad_mappings': ['schema:memberOf'],
                                       'description': 'The research infrastructure of '
                                                      'which this organization is a '
                                                      'member',
                                       'domain_of': ['Provider'],
                                       'multivalued': True,
                                       'name': 'memberOfRi',
                                       'range': 'ReasearchInfrastructure',
                                       'required': False,
                                       'title': 'member of RI'}},
         'title': 'Provider'})

    memberOfRi: Optional[list[ReasearchInfrastructure]] = Field(default=None, title="member of RI", description="""The research infrastructure of which this organization is a member""", json_schema_extra = { "linkml_meta": {'alias': 'memberOfRi',
         'broad_mappings': ['schema:memberOf'],
         'domain_of': ['Provider']} })
    alternateName: Optional[list[AlternateName]] = Field(default=None, title="alternate name", description="""Any other name under which the entity can be known""", json_schema_extra = { "linkml_meta": {'alias': 'alternateName',
         'close_mappings': ['wdp:P4970'],
         'comments': ['This includes previous names, acronyms, former taxonomic terms, '
                      'and other variations. This information can serve as keywords '
                      'for search purposes and as a bridge with other projects that '
                      'use different naming systems or taxonomies'],
         'domain_of': ['Organization', 'CommonName', 'AlternateName', 'ClinicalGroup'],
         'exact_mappings': ['schema:alternateName', 'dct:alternative', 'iao:0000118']} })
    country: Optional[Country] = Field(default=None, title="country", description="""The country of the organization""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['Organization'], 'recommended': True} })
    rorId: Optional[str] = Field(default=None, title="ROR iD", description="""The corresponding organization's persistent identifier from the Research Organization Registry (ROR)""", json_schema_extra = { "linkml_meta": {'alias': 'rorId',
         'domain_of': ['Organization'],
         'exact_mappings': ['wdp:P6782'],
         'recommended': True,
         'related_mappings': ['dwc:institutionCode']} })
    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Originator(PersonOrOrganization):
    """
    The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['dct:ProvenanceStatement', 'dct:ProvenanceStatement'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['foaf:Organization',
                              'foaf:Agent',
                              'foaf:Organization',
                              'foaf:Agent'],
         'title': 'Originator'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['PersonOrOrganization', 'File', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['PersonOrOrganization',
                       'Dataset',
                       'DataService',
                       'Term',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    homePage: Optional[str] = Field(default=None, title="home page", description="""A web page that serves as the main or introductory page""", json_schema_extra = { "linkml_meta": {'alias': 'homePage',
         'close_mappings': ['swo:0004006'],
         'domain_of': ['PersonOrOrganization'],
         'slot_uri': 'foaf:homepage'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['PersonOrOrganization', 'ProductOrService'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['PersonOrOrganization', 'License', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class BiologicalMaterialOrigin(Resource):
    """
    Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['sepio:0000058', 'sepio:0000058'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:115668003', 'snomed:115668003'],
         'slot_usage': {'biologicalPartOrigin': {'comments': ['It can be multiple '
                                                              'parts in case of a '
                                                              'recombinant biological '
                                                              'material.'],
                                                 'description': 'Details the origin of '
                                                                'one or more unitary '
                                                                'parts that make up '
                                                                'the biological '
                                                                'material. In the case '
                                                                'of recombinant '
                                                                'biological material, '
                                                                'multiple parts may be '
                                                                'involved.',
                                                 'domain_of': ['BiologicalMaterialOrigin'],
                                                 'multivalued': True,
                                                 'name': 'biologicalPartOrigin',
                                                 'range': 'BiologicalPartOrigin',
                                                 'related_mappings': ['schema:hasBioChemEntityPart'],
                                                 'required': True,
                                                 'title': 'biological part origin'},
                        'biologicalSourceType': {'comments': ['It makes sense that '
                                                              'only recombinant '
                                                              'biological materials '
                                                              'can have a mixed '
                                                              'material origin!'],
                                                 'description': 'Defines if the '
                                                                'current biological '
                                                                'material is natural '
                                                                'and was collected or '
                                                                'if it is a synthetic '
                                                                'biological material. '
                                                                'It makes sense that '
                                                                'only recombinant '
                                                                'biological materials '
                                                                'can have a mixed '
                                                                'material origin!',
                                                 'domain_of': ['BiologicalMaterialOrigin'],
                                                 'multivalued': False,
                                                 'name': 'biologicalSourceType',
                                                 'range': 'boolean',
                                                 'required': True,
                                                 'title': 'biological source type'},
                        'recombinantMaterial': {'description': 'Indicates if this '
                                                               'biological material is '
                                                               'a recombinant '
                                                               'biological material.',
                                                'domain_of': ['BiologicalMaterialOrigin'],
                                                'ifabsent': 'false',
                                                'multivalued': False,
                                                'name': 'recombinantMaterial',
                                                'range': 'boolean',
                                                'required': True,
                                                'title': 'recombinant material'}},
         'title': 'Biological material origin'})

    recombinantMaterial: bool = Field(default=False, title="recombinant material", description="""Indicates if this biological material is a recombinant biological material.""", json_schema_extra = { "linkml_meta": {'alias': 'recombinantMaterial',
         'domain_of': ['BiologicalMaterialOrigin'],
         'ifabsent': 'false'} })
    biologicalSourceType: bool = Field(default=..., title="biological source type", description="""Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalSourceType',
         'comments': ['It makes sense that only recombinant biological materials can '
                      'have a mixed material origin!'],
         'domain_of': ['BiologicalMaterialOrigin']} })
    biologicalPartOrigin: list[BiologicalPartOrigin] = Field(default=..., title="biological part origin", description="""Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalPartOrigin',
         'comments': ['It can be multiple parts in case of a recombinant biological '
                      'material.'],
         'domain_of': ['BiologicalMaterialOrigin'],
         'related_mappings': ['schema:hasBioChemEntityPart']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class BiologicalPartOrigin(Resource):
    """
    Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['sepio:0000058', 'sepio:0000058'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'accessToPhysicalGeneticResource': {'description': 'Indicate '
                                                                           'if the '
                                                                           'biological '
                                                                           'part was '
                                                                           'produced '
                                                                           'with '
                                                                           'access to '
                                                                           'a physical '
                                                                           'genetic '
                                                                           'resource',
                                                            'domain_of': ['BiologicalPartOrigin'],
                                                            'multivalued': False,
                                                            'name': 'accessToPhysicalGeneticResource',
                                                            'range': 'boolean',
                                                            'required': True,
                                                            'title': 'access to '
                                                                     'physical genetic '
                                                                     'resource'},
                        'recombinantPartIdentification': {'comments': ['Information '
                                                                       'not required '
                                                                       'if the current '
                                                                       'biological '
                                                                       'part '
                                                                       'constitutes '
                                                                       'the complete '
                                                                       'biological '
                                                                       'material'],
                                                          'description': 'Identification '
                                                                         'of a '
                                                                         'recombinant '
                                                                         'part',
                                                          'domain_of': ['BiologicalPartOrigin'],
                                                          'multivalued': False,
                                                          'name': 'recombinantPartIdentification',
                                                          'range': 'RecombinantPartIdentification',
                                                          'required': False,
                                                          'title': 'recombinant part '
                                                                   'identification'}},
         'title': 'Biological part origin'})

    recombinantPartIdentification: Optional[RecombinantPartIdentification] = Field(default=None, title="recombinant part identification", description="""Identification of a recombinant part""", json_schema_extra = { "linkml_meta": {'alias': 'recombinantPartIdentification',
         'comments': ['Information not required if the current biological part '
                      'constitutes the complete biological material'],
         'domain_of': ['BiologicalPartOrigin']} })
    accessToPhysicalGeneticResource: bool = Field(default=..., title="access to physical genetic resource", description="""Indicate if the biological part was produced with access to a physical genetic resource""", json_schema_extra = { "linkml_meta": {'alias': 'accessToPhysicalGeneticResource',
         'domain_of': ['BiologicalPartOrigin']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class NaturalPartOrigin(BiologicalPartOrigin):
    """
    Information on the origin of a natural part that composes the biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['sepio:0000058', 'sepio:0000058'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C87913',
                              'ncit:C43581',
                              'ncit:C87913',
                              'ncit:C43581'],
         'slot_usage': {'beforeDate': {'description': 'Set to TRUE if a proxy date for '
                                                      'the collection date is used',
                                       'domain_of': ['NaturalPartOrigin'],
                                       'ifabsent': 'false',
                                       'multivalued': False,
                                       'name': 'beforeDate',
                                       'range': 'boolean',
                                       'related_mappings': ['sepio:0000105',
                                                            'ro:0002089'],
                                       'required': True,
                                       'title': 'before date'},
                        'collectionDate': {'broad_mappings': ['dct:date'],
                                           'description': 'The date when the sample '
                                                          'was collected in situ. If '
                                                          'unknown/private, use a '
                                                          "proxy date such as 'date "
                                                          "received' and indicate this "
                                                          'by setting to true the '
                                                          'before date property',
                                           'domain_of': ['NaturalPartOrigin'],
                                           'multivalued': False,
                                           'name': 'collectionDate',
                                           'range': 'datetime',
                                           'related_mappings': ['obib:0000714'],
                                           'required': True,
                                           'title': 'collection date'},
                        'countryOfCollection': {'broad_mappings': ['dct:spatial'],
                                                'close_mappings': ['wdp:P495',
                                                                   'hso:0000360',
                                                                   'schema:countryOfOrigin'],
                                                'description': 'The geographical '
                                                               'location where the '
                                                               'sample was collected '
                                                               'in situ. Used for '
                                                               'Nagoya/CBD; equivalent '
                                                               "to 'country of "
                                                               "origin'.",
                                                'domain_of': ['NaturalPartOrigin'],
                                                'multivalued': False,
                                                'name': 'countryOfCollection',
                                                'range': 'Country',
                                                'related_mappings': ['dwc:country',
                                                                     'genepio:0000118'],
                                                'required': True,
                                                'title': 'country of collection'},
                        'indigenousPeopleAndLocalCommunityOrigin': {'description': 'The '
                                                                                   'specific '
                                                                                   'IPLC '
                                                                                   'area '
                                                                                   '(Indigenous '
                                                                                   'People '
                                                                                   'and '
                                                                                   'Local '
                                                                                   'Communities) '
                                                                                   'from '
                                                                                   'which '
                                                                                   'this '
                                                                                   'sample/element '
                                                                                   'was '
                                                                                   'sampled, '
                                                                                   'if '
                                                                                   'relevant',
                                                                    'domain_of': ['NaturalPartOrigin'],
                                                                    'multivalued': False,
                                                                    'name': 'indigenousPeopleAndLocalCommunityOrigin',
                                                                    'range': 'IplcOrigin',
                                                                    'related_mappings': ['mesh:D000081034',
                                                                                         'ncit:C41152'],
                                                                    'required': False,
                                                                    'title': 'indigenous '
                                                                             'people '
                                                                             'and '
                                                                             'local '
                                                                             'community '
                                                                             'origin'},
                        'permitIdentifierForAbs': {'description': 'Reference of the '
                                                                  'permit identifiers '
                                                                  'for access to the '
                                                                  'genetic resource, '
                                                                  'applicable if the '
                                                                  'genetic resource '
                                                                  'falls under Access '
                                                                  'and Benefit-Sharing '
                                                                  '(ABS) regulations',
                                                   'domain_of': ['NaturalPartOrigin'],
                                                   'multivalued': False,
                                                   'name': 'permitIdentifierForAbs',
                                                   'required': False,
                                                   'title': 'permit identifier for '
                                                            'ABS'}},
         'title': 'Natural part origin'})

    countryOfCollection: Country = Field(default=..., title="country of collection", description="""The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to 'country of origin'.""", json_schema_extra = { "linkml_meta": {'alias': 'countryOfCollection',
         'broad_mappings': ['dct:spatial'],
         'close_mappings': ['wdp:P495', 'hso:0000360', 'schema:countryOfOrigin'],
         'domain_of': ['NaturalPartOrigin'],
         'related_mappings': ['dwc:country', 'genepio:0000118']} })
    indigenousPeopleAndLocalCommunityOrigin: Optional[IplcOrigin] = Field(default=None, title="indigenous people and local community origin", description="""The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant""", json_schema_extra = { "linkml_meta": {'alias': 'indigenousPeopleAndLocalCommunityOrigin',
         'domain_of': ['NaturalPartOrigin'],
         'related_mappings': ['mesh:D000081034', 'ncit:C41152']} })
    collectionDate: datetime  = Field(default=..., title="collection date", description="""The date when the sample was collected in situ. If unknown/private, use a proxy date such as 'date received' and indicate this by setting to true the before date property""", json_schema_extra = { "linkml_meta": {'alias': 'collectionDate',
         'broad_mappings': ['dct:date'],
         'domain_of': ['NaturalPartOrigin'],
         'related_mappings': ['obib:0000714']} })
    beforeDate: bool = Field(default=False, title="before date", description="""Set to TRUE if a proxy date for the collection date is used""", json_schema_extra = { "linkml_meta": {'alias': 'beforeDate',
         'domain_of': ['NaturalPartOrigin'],
         'ifabsent': 'false',
         'related_mappings': ['sepio:0000105', 'ro:0002089']} })
    permitIdentifierForAbs: Optional[str] = Field(default=None, title="permit identifier for ABS", description="""Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations""", json_schema_extra = { "linkml_meta": {'alias': 'permitIdentifierForAbs', 'domain_of': ['NaturalPartOrigin']} })
    recombinantPartIdentification: Optional[RecombinantPartIdentification] = Field(default=None, title="recombinant part identification", description="""Identification of a recombinant part""", json_schema_extra = { "linkml_meta": {'alias': 'recombinantPartIdentification',
         'comments': ['Information not required if the current biological part '
                      'constitutes the complete biological material'],
         'domain_of': ['BiologicalPartOrigin']} })
    accessToPhysicalGeneticResource: bool = Field(default=..., title="access to physical genetic resource", description="""Indicate if the biological part was produced with access to a physical genetic resource""", json_schema_extra = { "linkml_meta": {'alias': 'accessToPhysicalGeneticResource',
         'domain_of': ['BiologicalPartOrigin']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class SyntheticPartOrigin(BiologicalPartOrigin):
    """
    Information on the origin of a synthetic part that composes the biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'descriptionOfModificationsMadeFromTheReferenceSequences': {'description': 'List '
                                                                                                   'the '
                                                                                                   'modifications '
                                                                                                   'mades '
                                                                                                   'from '
                                                                                                   'the '
                                                                                                   'reference '
                                                                                                   'sequence '
                                                                                                   'if '
                                                                                                   'any',
                                                                                    'domain_of': ['SyntheticPartOrigin'],
                                                                                    'multivalued': False,
                                                                                    'name': 'descriptionOfModificationsMadeFromTheReferenceSequences',
                                                                                    'range': 'string',
                                                                                    'recommended': True,
                                                                                    'related_mappings': ['uniprotrdfs:modification'],
                                                                                    'required': False,
                                                                                    'title': 'description '
                                                                                             'of '
                                                                                             'modification(s) '
                                                                                             'made '
                                                                                             'from '
                                                                                             'the '
                                                                                             'reference '
                                                                                             'sequence(s)'},
                        'modificationsFromTheReferenceSequences': {'description': 'Set '
                                                                                  'to '
                                                                                  'TRUE '
                                                                                  'if '
                                                                                  'there '
                                                                                  'was '
                                                                                  'is '
                                                                                  'any '
                                                                                  'modification '
                                                                                  'made '
                                                                                  'from '
                                                                                  'the '
                                                                                  'reference '
                                                                                  'sequence',
                                                                   'domain_of': ['SyntheticPartOrigin'],
                                                                   'multivalued': False,
                                                                   'name': 'modificationsFromTheReferenceSequences',
                                                                   'range': 'boolean',
                                                                   'related_mappings': ['geno:0000967'],
                                                                   'required': True,
                                                                   'title': 'modifications '
                                                                            'from the '
                                                                            'reference '
                                                                            'sequence(s)'}},
         'title': 'Synthetic part origin'})

    modificationsFromTheReferenceSequences: bool = Field(default=..., title="modifications from the reference sequence(s)", description="""Set to TRUE if there was is any modification made from the reference sequence""", json_schema_extra = { "linkml_meta": {'alias': 'modificationsFromTheReferenceSequences',
         'domain_of': ['SyntheticPartOrigin'],
         'related_mappings': ['geno:0000967']} })
    descriptionOfModificationsMadeFromTheReferenceSequences: Optional[str] = Field(default=None, title="description of modification(s) made from the reference sequence(s)", description="""List the modifications mades from the reference sequence if any""", json_schema_extra = { "linkml_meta": {'alias': 'descriptionOfModificationsMadeFromTheReferenceSequences',
         'domain_of': ['SyntheticPartOrigin'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:modification']} })
    recombinantPartIdentification: Optional[RecombinantPartIdentification] = Field(default=None, title="recombinant part identification", description="""Identification of a recombinant part""", json_schema_extra = { "linkml_meta": {'alias': 'recombinantPartIdentification',
         'comments': ['Information not required if the current biological part '
                      'constitutes the complete biological material'],
         'domain_of': ['BiologicalPartOrigin']} })
    accessToPhysicalGeneticResource: bool = Field(default=..., title="access to physical genetic resource", description="""Indicate if the biological part was produced with access to a physical genetic resource""", json_schema_extra = { "linkml_meta": {'alias': 'accessToPhysicalGeneticResource',
         'domain_of': ['BiologicalPartOrigin']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class RecombinantPartIdentification(Resource):
    """
    Identification of a recombinant part
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'partIdentification': {'description': 'A short designation of '
                                                              'this recombinant part '
                                                              'of the related '
                                                              'biological material',
                                               'domain_of': ['RecombinantPartIdentification'],
                                               'multivalued': False,
                                               'name': 'partIdentification',
                                               'range': 'string',
                                               'required': True,
                                               'title': 'Part identification'},
                        'sequence': {'close_mappings': ['geno:0000239', 'bao:0002817'],
                                     'description': 'The related sequence information '
                                                    'from a sequence provider or in '
                                                    'fasta format',
                                     'domain_of': ['RecombinantPartIdentification',
                                                   'Protein',
                                                   'NucleicAcid',
                                                   'Pathogen'],
                                     'multivalued': True,
                                     'name': 'sequence',
                                     'range': 'Sequence',
                                     'recommended': True,
                                     'related_mappings': ['uniprotrdfs:sequence'],
                                     'required': True,
                                     'title': 'sequence'}},
         'title': 'Recombinant part identification'})

    partIdentification: str = Field(default=..., title="Part identification", description="""A short designation of this recombinant part of the related biological material""", json_schema_extra = { "linkml_meta": {'alias': 'partIdentification', 'domain_of': ['RecombinantPartIdentification']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid',
                       'Pathogen'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Collection(Catalogue):
    """
    Set of products and services with some common characteristics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q2668072', 'wd:Q2668072'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'collectionDataProvider': {'broad_mappings': ['dct:isReferencedBy'],
                                                   'description': 'The provider of the '
                                                                  'data of the '
                                                                  'collection',
                                                   'domain_of': ['Collection'],
                                                   'multivalued': False,
                                                   'name': 'collectionDataProvider',
                                                   'range': 'DataProvider',
                                                   'required': False,
                                                   'title': 'collection data provider'},
                        'collectionItem': {'broad_mappings': ['schema:includesObject',
                                                              'dcat:dataset'],
                                           'description': 'An item of the collection',
                                           'domain_of': ['Collection'],
                                           'multivalued': True,
                                           'name': 'collectionItem',
                                           'range': 'ProductOrService',
                                           'recommended': True,
                                           'related_mappings': ['dcat:resource',
                                                                'dcat:servesDataset'],
                                           'required': False,
                                           'title': 'collection item'}},
         'title': 'Collection'})

    collectionItem: Optional[list[ProductOrService]] = Field(default=None, title="collection item", description="""An item of the collection""", json_schema_extra = { "linkml_meta": {'alias': 'collectionItem',
         'broad_mappings': ['schema:includesObject', 'dcat:dataset'],
         'domain_of': ['Collection'],
         'recommended': True,
         'related_mappings': ['dcat:resource', 'dcat:servesDataset']} })
    collectionDataProvider: Optional[DataProvider] = Field(default=None, title="collection data provider", description="""The provider of the data of the collection""", json_schema_extra = { "linkml_meta": {'alias': 'collectionDataProvider',
         'broad_mappings': ['dct:isReferencedBy'],
         'domain_of': ['Collection']} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ProductOrService(Dataset):
    """
    An offering provided by a provider, which may be tangible (a product) or intangible (a service)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'close_mappings': ['schema:Product',
                            'gr:ProductOrService',
                            'schema:Product',
                            'gr:ProductOrService'],
         'comments': ['part of  wd:Q2897903 (goods and services )'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'accessPointUrl': {'broad_mappings': ['schema:url'],
                                           'description': 'The URL that permits to '
                                                          'access to the '
                                                          'product/service detailed '
                                                          'description page on the '
                                                          "provider's website and/or "
                                                          'allows to place an order '
                                                          'about it or at least '
                                                          'describe the process to '
                                                          'place an order/enquiry',
                                           'domain_of': ['ProductOrService'],
                                           'exact_mappings': ['schema:serviceURL'],
                                           'multivalued': False,
                                           'name': 'accessPointUrl',
                                           'range': 'uri',
                                           'related_mappings': ['dcat:landingPage'],
                                           'required': True,
                                           'title': 'access point URL'},
                        'additionalCategory': {'close_mappings': ['schema:additionalType'],
                                               'description': 'Any category apart from '
                                                              'its main category in '
                                                              'which this product or '
                                                              'service can fit',
                                               'domain_of': ['ProductOrService'],
                                               'is_a': 'category',
                                               'multivalued': True,
                                               'name': 'additionalCategory',
                                               'range': 'ProductCategory',
                                               'recommended': True,
                                               'required': False,
                                               'title': 'additional category'},
                        'availability': {'close_mappings': ['schema:availability',
                                                            'dct:available'],
                                         'comments': ['Possible availabilities may '
                                                      'differ from a project to '
                                                      'another'],
                                         'description': 'The state or condition in '
                                                        'which this item is accessible '
                                                        'and ready for use or can be '
                                                        'obtained',
                                         'domain_of': ['ProductOrService'],
                                         'ifabsent': 'string(on request)',
                                         'multivalued': False,
                                         'name': 'availability',
                                         'range': 'string',
                                         'required': True,
                                         'title': 'availability'},
                        'biosafetyRestrictions': {'description': 'Information about '
                                                                 'guidelines and '
                                                                 'regulations designed '
                                                                 'to prevent the '
                                                                 'exposure to or '
                                                                 'release of '
                                                                 'potentially harmful '
                                                                 'biological agents. '
                                                                 'It thereby '
                                                                 'contributes to '
                                                                 'protecting people '
                                                                 'and the environment '
                                                                 'from biohazards '
                                                                 'while accessing this '
                                                                 'product or service',
                                                  'domain_of': ['ProductOrService'],
                                                  'multivalued': False,
                                                  'name': 'biosafetyRestrictions',
                                                  'range': 'string',
                                                  'related_mappings': ['bao:0002826'],
                                                  'required': False,
                                                  'title': 'biosafety restrictions'},
                        'canBeUsedToProduceGmo': {'broad_mappings': ['schema:potentialUse'],
                                                  'comments': ['Set to TRUE if it can '
                                                               'produce GMO. It is '
                                                               'recommended to have a '
                                                               'value for this field, '
                                                               'no value will be '
                                                               'understood as unknown'],
                                                  'description': 'Indicates if the '
                                                                 'current service or '
                                                                 'product can be used '
                                                                 'to produce GMO',
                                                  'domain_of': ['ProductOrService'],
                                                  'multivalued': False,
                                                  'name': 'canBeUsedToProduceGmo',
                                                  'range': 'boolean',
                                                  'recommended': True,
                                                  'required': True,
                                                  'title': 'can be used to produce '
                                                           'GMO'},
                        'category': {'close_mappings': ['schema:category',
                                                        'gr:category'],
                                     'description': 'The main category of the service '
                                                    'or product',
                                     'domain_of': ['ProductOrService'],
                                     'multivalued': False,
                                     'name': 'category',
                                     'range': 'ProductCategory',
                                     'required': True,
                                     'slot_uri': 'dcat:theme',
                                     'title': 'category'},
                        'certification': {'close_mappings': ['dct:conformsTo'],
                                          'description': 'Any certification related to '
                                                         'the current product or '
                                                         'service; e.g., ISO '
                                                         'certification',
                                          'domain_of': ['ProductOrService'],
                                          'exact_mappings': ['schema:hasCertification'],
                                          'multivalued': True,
                                          'name': 'certification',
                                          'range': 'Certification',
                                          'required': False,
                                          'title': 'certification'},
                        'collection': {'broad_mappings': ['dct:isPartOf'],
                                       'description': 'The collection(s) to which '
                                                      'belongs this item',
                                       'domain_of': ['ProductOrService'],
                                       'multivalued': True,
                                       'name': 'collection',
                                       'range': 'Collection',
                                       'related_mappings': ['afop:AFX_0002720'],
                                       'required': True,
                                       'title': 'collection'},
                        'complementaryDocument': {'close_mappings': ['sepio:0000442'],
                                                  'description': 'Any additional '
                                                                 'documents that '
                                                                 'provide '
                                                                 'supplementary '
                                                                 'information, '
                                                                 'instructions, or '
                                                                 'guidelines relevant '
                                                                 'to the use of this '
                                                                 'item',
                                                  'domain_of': ['ProductOrService'],
                                                  'multivalued': True,
                                                  'name': 'complementaryDocument',
                                                  'range': 'Document',
                                                  'required': False,
                                                  'title': 'complementary document'},
                        'contactPoint': {'description': 'An information that allows '
                                                        'someone to establish '
                                                        'communication',
                                         'domain_of': ['ProductOrService',
                                                       'PersonOrOrganization'],
                                         'exact_mappings': ['schema:contactPoint'],
                                         'multivalued': False,
                                         'name': 'contactPoint',
                                         'range': 'ContactPoint',
                                         'recommended': True,
                                         'required': False,
                                         'slot_uri': 'dcat:contactPoint',
                                         'title': 'contact point'},
                        'doi': {'broad_mappings': ['dct:bibliographicCitation'],
                                'close_mappings': ['wdp:P356', 'reproduceme:doi'],
                                'description': 'A Digital Object Identifier (DOI) that '
                                               'can be related',
                                'domain_of': ['ProductOrService', 'Publication'],
                                'multivalued': True,
                                'name': 'doi',
                                'range': 'Doi',
                                'required': False,
                                'title': 'DOI'},
                        'externalRelatedReference': {'broad_mappings': ['dct:references'],
                                                     'description': 'A reference that '
                                                                    'permits to '
                                                                    'retrieve another '
                                                                    'related item from '
                                                                    'an external '
                                                                    'provider',
                                                     'domain_of': ['ProductOrService'],
                                                     'multivalued': True,
                                                     'name': 'externalRelatedReference',
                                                     'range': 'ExternalRelatedReference',
                                                     'required': False,
                                                     'title': 'external related '
                                                              'reference'},
                        'internalReference': {'broad_mappings': ['dct:references'],
                                              'description': 'Any reference or '
                                                             'indication to be used '
                                                             'for local retrieval '
                                                             'purpose',
                                              'domain_of': ['ProductOrService'],
                                              'multivalued': False,
                                              'name': 'internalReference',
                                              'range': 'string',
                                              'required': False,
                                              'title': 'internal reference'},
                        'keywords': {'close_mappings': ['dcat:keyword'],
                                     'description': 'List of terms used to tag and '
                                                    'categorize this Item',
                                     'domain_of': ['ProductOrService'],
                                     'exact_mappings': ['schema:keywords'],
                                     'multivalued': True,
                                     'name': 'keywords',
                                     'range': 'Keyword',
                                     'recommended': True,
                                     'required': True,
                                     'title': 'keywords'},
                        'note': {'description': 'An aditional information as a textual '
                                                'comment',
                                 'domain_of': ['ProductOrService'],
                                 'multivalued': False,
                                 'name': 'note',
                                 'range': 'string',
                                 'required': False,
                                 'slot_uri': 'skos:note',
                                 'title': 'note'},
                        'pathogenIdentification': {'comments': ['The pathogen '
                                                                'identification '
                                                                'contains information '
                                                                'about name and taxon '
                                                                'but in some '
                                                                'cases(e.g: '
                                                                'FAIRSHARING) there '
                                                                'may have no direct '
                                                                'pathogen related but '
                                                                'simply a taxonomic '
                                                                'information .... the '
                                                                'default value should '
                                                                'be the root of '
                                                                'virology: Viruses'],
                                                   'description': 'The identification '
                                                                  'of the pathogen or '
                                                                  'group of pathogens '
                                                                  '(e.g; name, taxon '
                                                                  'identification, '
                                                                  'etc.) related to '
                                                                  'the current item.',
                                                   'domain_of': ['ProductOrService'],
                                                   'multivalued': True,
                                                   'name': 'pathogenIdentification',
                                                   'range': 'PathogenIdentification',
                                                   'required': True,
                                                   'title': 'pathogen identification'},
                        'productPicture': {'description': 'A picture that can '
                                                          'represent the item',
                                           'domain_of': ['ProductOrService'],
                                           'multivalued': True,
                                           'name': 'productPicture',
                                           'range': 'Image',
                                           'required': False,
                                           'title': 'product picture'},
                        'provider': {'close_mappings': ['schema:provider',
                                                        'dct:publisher'],
                                     'description': 'A provider of this product or '
                                                    'service, as a specific '
                                                    'organization',
                                     'domain_of': ['ProductOrService'],
                                     'exact_mappings': ['sio:000066'],
                                     'multivalued': False,
                                     'name': 'provider',
                                     'range': 'Provider',
                                     'required': True,
                                     'title': 'provider'},
                        'qualityGrading': {'close_mappings': ['bao:0002662',
                                                              'sio:000217'],
                                           'description': 'Information that permits to '
                                                          'assess the quality level of '
                                                          'what will be provided',
                                           'domain_of': ['ProductOrService'],
                                           'multivalued': False,
                                           'name': 'qualityGrading',
                                           'range': 'string',
                                           'required': False,
                                           'title': 'quality grading'},
                        'refSku': {'broad_mappings': ['dct:identifier',
                                                      'schema:identifier'],
                                   'close_mappings': ['dwc:catalogNumber'],
                                   'description': 'The reference or the stock keeping '
                                                  'unit of the service or item '
                                                  "provided in the provider's "
                                                  'catalogue',
                                   'domain_of': ['ProductOrService'],
                                   'exact_mappings': ['schema:sku'],
                                   'multivalued': False,
                                   'name': 'refSku',
                                   'range': 'string',
                                   'required': True,
                                   'title': 'ref SKU'},
                        'riskGroup': {'description': 'The highest risk group related '
                                                     'to this resource. The risk group '
                                                     'of a biological agent guiding '
                                                     'its initial handling in labs '
                                                     'according to the risk group '
                                                     'classification defined by the '
                                                     'WHO laboratory biosafety manual',
                                      'domain_of': ['ProductOrService'],
                                      'exact_mappings': ['wdp:P12663'],
                                      'multivalued': False,
                                      'name': 'riskGroup',
                                      'range': 'RiskGroup',
                                      'recommended': True,
                                      'related_mappings': ['bao:0002826'],
                                      'required': False,
                                      'title': 'risk group'},
                        'technicalRecommendation': {'description': 'Expert advice or '
                                                                   'guidelines '
                                                                   'provided to ensure '
                                                                   'the optimal use, '
                                                                   'performance, and '
                                                                   'maintenance of '
                                                                   'what is provided, '
                                                                   'including best '
                                                                   'practices, '
                                                                   'troubleshooting '
                                                                   'tips, and '
                                                                   'procedural '
                                                                   'instructions',
                                                    'domain_of': ['ProductOrService'],
                                                    'multivalued': False,
                                                    'name': 'technicalRecommendation',
                                                    'range': 'string',
                                                    'required': False,
                                                    'title': 'technical '
                                                             'recommendation'},
                        'unitCost': {'close_mappings': ['schema:price'],
                                     'comments': ['The cost per access may not always '
                                                  'be defined as a fixed numerical '
                                                  'value. In some cases, the price is '
                                                  'conditional or available only upon '
                                                  'request. To accommodate such cases, '
                                                  'descriptive information should be '
                                                  'provided through the property '
                                                  'EVORAO:unitCostNote (xsd:string). '
                                                  'This allows handling of cost '
                                                  'statements such as “on request,” '
                                                  '“depends on volume,” or “free '
                                                  'access for academics,” which cannot '
                                                  'be captured by a simple numeric '
                                                  'value.'],
                                     'description': 'The cost per access for one unit '
                                                    'as defined by the unit definition',
                                     'domain_of': ['ProductOrService'],
                                     'multivalued': False,
                                     'name': 'unitCost',
                                     'range': 'decimal',
                                     'recommended': True,
                                     'required': False,
                                     'title': 'unit cost'},
                        'unitCostCurrency': {'close_mappings': ['schema:priceCurrency'],
                                             'description': 'The currency in which the '
                                                            'unit cost is expressed, '
                                                            'following ISO 4217 '
                                                            'three-letter codes (e.g., '
                                                            'EUR, USD)',
                                             'domain_of': ['ProductOrService'],
                                             'ifabsent': 'string(EUR)',
                                             'multivalued': False,
                                             'name': 'unitCostCurrency',
                                             'range': 'string',
                                             'recommended': True,
                                             'required': False,
                                             'title': 'unit cost currency'},
                        'unitCostNote': {'description': 'A free-text note describing '
                                                        'special conditions or cases '
                                                        'where the cost cannot be '
                                                        'represented by a numerical '
                                                        'value (e.g., on request, free '
                                                        'for academics, depends on '
                                                        'volume)',
                                         'domain_of': ['ProductOrService'],
                                         'multivalued': False,
                                         'name': 'unitCostNote',
                                         'range': 'string',
                                         'required': False,
                                         'title': 'unit cost note'},
                        'unitDefinition': {'comments': ['The description of what will '
                                                        'be delivered to the end-user '
                                                        '(e.g.: packaging, '
                                                        'quantity...)'],
                                           'description': 'A short description of what '
                                                          'will be delivered by '
                                                          'ordering one unit of this '
                                                          'item',
                                           'domain_of': ['ProductOrService'],
                                           'multivalued': False,
                                           'name': 'unitDefinition',
                                           'range': 'string',
                                           'recommended': True,
                                           'related_mappings': ['dct:format'],
                                           'required': False,
                                           'title': 'unit definition'}},
         'title': 'Product or service'})

    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Service(ProductOrService):
    """
    An intangible offering characterized by an activity, performance, or facilitation carried out by a provider to fulfill a user’s need
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q7406919',
                            'dcmi:Service',
                            'schema:Service',
                            'ncit:C88187',
                            'obi:0001173',
                            'wd:Q7406919',
                            'dcmi:Service',
                            'schema:Service',
                            'ncit:C88187',
                            'obi:0001173'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['schema:Product',
                              'ncit:C47920',
                              'schema:Product',
                              'ncit:C47920'],
         'slot_usage': {'modelSpecies': {'description': 'The species of the infected '
                                                        'organism in the experiment',
                                         'domain_of': ['Service'],
                                         'multivalued': False,
                                         'name': 'modelSpecies',
                                         'range': 'string',
                                         'required': False,
                                         'title': 'model species'},
                        'modelType': {'description': 'The specific name of the '
                                                     'infected organism, including its '
                                                     'modification if necessary',
                                      'domain_of': ['Service'],
                                      'multivalued': False,
                                      'name': 'modelType',
                                      'range': 'string',
                                      'required': False,
                                      'title': 'model type'}},
         'title': 'Service'})

    modelSpecies: Optional[str] = Field(default=None, title="model species", description="""The species of the infected organism in the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'modelSpecies', 'domain_of': ['Service']} })
    modelType: Optional[str] = Field(default=None, title="model type", description="""The specific name of the infected organism, including its modification if necessary""", json_schema_extra = { "linkml_meta": {'alias': 'modelType', 'domain_of': ['Service']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Product(ProductOrService):
    """
    A tangible, physical item made available by a provider for use, consumption, or ownership transfer
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:PhysicalResource', 'dct:PhysicalResource'],
         'close_mappings': ['wd:Q2424752', 'wd:Q2424752'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['schema:Product', 'schema:Product'],
         'slot_usage': {'iataClassification': {'close_mappings': ['wdp:P238',
                                                                  'schema:iataCode'],
                                               'description': 'The corresponding '
                                                              'International Air '
                                                              'Transport Association '
                                                              "(IATA)'s category for "
                                                              'this Product',
                                               'domain_of': ['Product'],
                                               'multivalued': False,
                                               'name': 'iataClassification',
                                               'range': 'IataClassification',
                                               'required': True,
                                               'title': 'IATA classification'},
                        'materialSafetyDataSheet': {'comments': ['The MSD  is a '
                                                                 'document that '
                                                                 'provides detailed '
                                                                 'information about '
                                                                 'the properties, '
                                                                 'hazards, handling, '
                                                                 'storage, and '
                                                                 'emergency procedures '
                                                                 'related to the use '
                                                                 'of a chemical or '
                                                                 'substance'],
                                                    'description': 'A Material Safety '
                                                                   'Data Sheet (MSDS) '
                                                                   'or Safety Data '
                                                                   'Sheet (SDS) is a '
                                                                   'standardized '
                                                                   'document that '
                                                                   'contains crucial '
                                                                   'occupational '
                                                                   'safety and health '
                                                                   'information '
                                                                   'related to the '
                                                                   'product',
                                                    'domain_of': ['Product'],
                                                    'multivalued': False,
                                                    'name': 'materialSafetyDataSheet',
                                                    'range': 'ReasearchInfrastructure',
                                                    'required': False,
                                                    'title': 'material safety data '
                                                             'sheet'},
                        'originator': {'close_mappings': ['dct:provenance'],
                                       'description': 'The individual or organization '
                                                      'responsible for the original '
                                                      'discovery, isolation, or '
                                                      'creation of an item, providing '
                                                      'information about the source or '
                                                      'origin of the sample',
                                       'domain_of': ['Product'],
                                       'multivalued': False,
                                       'name': 'originator',
                                       'range': 'Originator',
                                       'required': False,
                                       'title': 'originator'},
                        'shippingConditions': {'close_mappings': ['schema:shippingConditions'],
                                               'description': 'Specification of the '
                                                              'terms and parameters '
                                                              'for transporting',
                                               'domain_of': ['Product'],
                                               'multivalued': False,
                                               'name': 'shippingConditions',
                                               'range': 'string',
                                               'required': True,
                                               'title': 'shipping conditions'},
                        'storageConditions': {'comments': ['e.g, could be a xsd:string '
                                                           "in enumeration ('Freeze "
                                                           "Dried', 'Liquid Nitrogen', "
                                                           "'Viral Storage Medium "
                                                           "-20C', 'Viral Storage "
                                                           "Medium -80C', 'Living "
                                                           "plant material (>= +4°C)', "
                                                           "'Gas Phase', 'Ethanol "
                                                           "-20C', 'Ethanol -80C', "
                                                           "'Dried')"],
                                              'description': 'Specifies the conditions '
                                                             'under which the product '
                                                             'has to be stored to '
                                                             'maintain stability and '
                                                             'integrity, such as '
                                                             'temperature, buffer, and '
                                                             'other environmental '
                                                             'factors.',
                                              'domain_of': ['Product'],
                                              'multivalued': False,
                                              'name': 'storageConditions',
                                              'range': 'string',
                                              'required': True,
                                              'title': 'storage conditions'},
                        'thirdPartyDistributionConsent': {'description': 'Indicates '
                                                                         'whether the '
                                                                         'biological '
                                                                         'material can '
                                                                         'be '
                                                                         'distributed '
                                                                         'without '
                                                                         'restriction '
                                                                         'to third '
                                                                         'parties, as '
                                                                         'indicated by '
                                                                         'the ABS '
                                                                         'permit, in '
                                                                         'case an ABS '
                                                                         'permit is '
                                                                         'required',
                                                          'domain_of': ['Product'],
                                                          'multivalued': False,
                                                          'name': 'thirdPartyDistributionConsent',
                                                          'range': 'boolean',
                                                          'required': False,
                                                          'title': 'third party '
                                                                   'distribution '
                                                                   'consent'},
                        'usageRestrictions': {'description': 'Specifies any '
                                                             'limitations or '
                                                             'conditions on the use of '
                                                             'the biological material, '
                                                             'including restrictions '
                                                             'on research, commercial '
                                                             'use, or distribution, '
                                                             'considering any '
                                                             'potential concerns about '
                                                             'the related genetic '
                                                             'material',
                                              'domain_of': ['Product'],
                                              'multivalued': False,
                                              'name': 'usageRestrictions',
                                              'range': 'string',
                                              'required': False,
                                              'title': 'usage restrictions'}},
         'title': 'Product'})

    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Antibody(Product):
    """
    Protein that can bind to certain types of foreign bodies, such as pathogens
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q79460',
                            'snomed:68498002',
                            'wd:Q79460',
                            'snomed:68498002'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'antibodyPurifiedByAffinity': {'description': 'Indicates '
                                                                      'whether or not '
                                                                      'if the antibody '
                                                                      'was purified by '
                                                                      'affinity',
                                                       'domain_of': ['Antibody'],
                                                       'multivalued': False,
                                                       'name': 'antibodyPurifiedByAffinity',
                                                       'range': 'boolean',
                                                       'required': True,
                                                       'title': 'antibody purified by '
                                                                'affinity'},
                        'productionSystem': {'description': 'The biological and '
                                                            'technological methods and '
                                                            'processes used to produce '
                                                            'the antibody',
                                             'domain_of': ['Antibody'],
                                             'multivalued': False,
                                             'name': 'productionSystem',
                                             'range': 'string',
                                             'recommended': True,
                                             'required': False,
                                             'title': 'production system'},
                        'sequenceReference': {'description': 'A reference that permits '
                                                             'to retrieve the sequence '
                                                             'information from a '
                                                             'sequence provider',
                                              'domain_of': ['Antibody', 'Sequence'],
                                              'multivalued': True,
                                              'name': 'sequenceReference',
                                              'range': 'SequenceReference',
                                              'recommended': True,
                                              'required': False,
                                              'title': 'sequence reference'},
                        'specificityDocumented': {'description': 'Boolean value '
                                                                 'indicating whether '
                                                                 'the specificity of '
                                                                 'the product has been '
                                                                 'formally documented',
                                                  'domain_of': ['Antibody',
                                                                'DetectionKit'],
                                                  'multivalued': False,
                                                  'name': 'specificityDocumented',
                                                  'range': 'boolean',
                                                  'required': True,
                                                  'title': 'specificity documented'},
                        'targetedAntigen': {'description': 'Specific molecular '
                                                           'structure or epitope '
                                                           'recognized and bound by an '
                                                           'antibody',
                                            'domain_of': ['Antibody'],
                                            'multivalued': False,
                                            'name': 'targetedAntigen',
                                            'range': 'string',
                                            'required': True,
                                            'title': 'targeted antigen'}},
         'title': 'Antibody'})

    productionSystem: Optional[str] = Field(default=None, title="production system", description="""The biological and technological methods and processes used to produce the antibody""", json_schema_extra = { "linkml_meta": {'alias': 'productionSystem', 'domain_of': ['Antibody'], 'recommended': True} })
    antibodyPurifiedByAffinity: bool = Field(default=..., title="antibody purified by affinity", description="""Indicates whether or not if the antibody was purified by affinity""", json_schema_extra = { "linkml_meta": {'alias': 'antibodyPurifiedByAffinity', 'domain_of': ['Antibody']} })
    specificityDocumented: bool = Field(default=..., title="specificity documented", description="""Boolean value indicating whether the specificity of the product has been formally documented""", json_schema_extra = { "linkml_meta": {'alias': 'specificityDocumented', 'domain_of': ['Antibody', 'DetectionKit']} })
    targetedAntigen: str = Field(default=..., title="targeted antigen", description="""Specific molecular structure or epitope recognized and bound by an antibody""", json_schema_extra = { "linkml_meta": {'alias': 'targetedAntigen', 'domain_of': ['Antibody']} })
    sequenceReference: Optional[list[SequenceReference]] = Field(default=None, title="sequence reference", description="""A reference that permits to retrieve the sequence information from a sequence provider""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceReference',
         'domain_of': ['Antibody', 'Sequence'],
         'recommended': True} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Hybridoma(Antibody):
    """
    An hybridoma that provides antibodies that can be related to a pathogen
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q27554370',
                            'snomed:25326005',
                            'clo:0036932',
                            'bto:0000610',
                            'ncit:C16700',
                            'wd:Q27554370',
                            'snomed:25326005',
                            'clo:0036932',
                            'bto:0000610',
                            'ncit:C16700'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'hybridomaDescription': {'description': 'The description of '
                                                                'the hybridoma',
                                                 'domain_of': ['Hybridoma'],
                                                 'multivalued': False,
                                                 'name': 'hybridomaDescription',
                                                 'range': 'string',
                                                 'required': True,
                                                 'title': 'hybridoma description'}},
         'title': 'Hybridoma'})

    hybridomaDescription: str = Field(default=..., title="hybridoma description", description="""The description of the hybridoma""", json_schema_extra = { "linkml_meta": {'alias': 'hybridomaDescription', 'domain_of': ['Hybridoma']} })
    productionSystem: Optional[str] = Field(default=None, title="production system", description="""The biological and technological methods and processes used to produce the antibody""", json_schema_extra = { "linkml_meta": {'alias': 'productionSystem', 'domain_of': ['Antibody'], 'recommended': True} })
    antibodyPurifiedByAffinity: bool = Field(default=..., title="antibody purified by affinity", description="""Indicates whether or not if the antibody was purified by affinity""", json_schema_extra = { "linkml_meta": {'alias': 'antibodyPurifiedByAffinity', 'domain_of': ['Antibody']} })
    specificityDocumented: bool = Field(default=..., title="specificity documented", description="""Boolean value indicating whether the specificity of the product has been formally documented""", json_schema_extra = { "linkml_meta": {'alias': 'specificityDocumented', 'domain_of': ['Antibody', 'DetectionKit']} })
    targetedAntigen: str = Field(default=..., title="targeted antigen", description="""Specific molecular structure or epitope recognized and bound by an antibody""", json_schema_extra = { "linkml_meta": {'alias': 'targetedAntigen', 'domain_of': ['Antibody']} })
    sequenceReference: Optional[list[SequenceReference]] = Field(default=None, title="sequence reference", description="""A reference that permits to retrieve the sequence information from a sequence provider""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceReference',
         'domain_of': ['Antibody', 'Sequence'],
         'recommended': True} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Protein(Product):
    """
    A protein as a derived product from a pathogen
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q8054',
                            'snomed:88878007',
                            'sio:010043',
                            'schema:Protein',
                            'wd:Q8054',
                            'snomed:88878007',
                            'sio:010043',
                            'schema:Protein'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'biologicalMaterialOrigin': {'description': 'Information about '
                                                                    'the origin of the '
                                                                    'biological '
                                                                    'material, '
                                                                    'essential for '
                                                                    'access, '
                                                                    'utilization, and '
                                                                    'benefit-sharing '
                                                                    'of genetic '
                                                                    'resources in '
                                                                    'compliance with '
                                                                    'the Nagoya '
                                                                    'Protocol',
                                                     'domain_of': ['Protein',
                                                                   'NucleicAcid',
                                                                   'Pathogen'],
                                                     'multivalued': False,
                                                     'name': 'biologicalMaterialOrigin',
                                                     'range': 'BiologicalMaterialOrigin',
                                                     'related_mappings': ['sepio:0000058'],
                                                     'required': True,
                                                     'title': 'biological material '
                                                              'origin'},
                        'domain': {'close_mappings': ['uniprotrdfs:domain'],
                                   'description': 'A distinct structural and '
                                                  'functional unit within the protein, '
                                                  'often capable of independent '
                                                  'folding and stability, which '
                                                  "contributes to the protein's "
                                                  'overall function',
                                   'domain_of': ['Protein'],
                                   'multivalued': True,
                                   'name': 'domain',
                                   'range': 'string',
                                   'required': False,
                                   'title': 'domain'},
                        'expressedAs': {'close_mappings': ['apollo:00000102'],
                                        'description': 'Refers to the form in which '
                                                       'the protein is produced and '
                                                       'manifested in a biological '
                                                       'system. Possible values '
                                                       "include 'Soluble' (proteins "
                                                       'that are dissolved in the '
                                                       'cellular or extracellular '
                                                       "fluid) and 'Inclusion bodies' "
                                                       '(aggregated proteins that are '
                                                       'insoluble and form within the '
                                                       'cell)',
                                        'domain_of': ['Protein'],
                                        'multivalued': True,
                                        'name': 'expressedAs',
                                        'range': 'string',
                                        'required': False,
                                        'title': 'expressed as'},
                        'expressionSystem': {'close_mappings': ['ro:0002206'],
                                             'description': 'The host organism or '
                                                            'cellular environment used '
                                                            'to produce a protein from '
                                                            'a specific gene. Possible '
                                                            "values include 'E. coli' "
                                                            '(bacterial system), '
                                                            "'Insect cells' (using "
                                                            'baculovirus vectors), and '
                                                            "'Mammalian cells' "
                                                            '(mammalian cell lines).',
                                             'domain_of': ['Protein'],
                                             'multivalued': True,
                                             'name': 'expressionSystem',
                                             'range': 'string',
                                             'required': False,
                                             'title': 'expression system'},
                        'functionalAndTechnicalDescription': {'description': 'Detailed '
                                                                             'information '
                                                                             'about '
                                                                             'the '
                                                                             'specific '
                                                                             'biological '
                                                                             'functions, '
                                                                             'mechanisms '
                                                                             'of '
                                                                             'action, '
                                                                             'and '
                                                                             'technical '
                                                                             'attributes '
                                                                             'of a '
                                                                             'protein. '
                                                                             'This '
                                                                             'includes '
                                                                             'how the '
                                                                             'protein '
                                                                             'interacts '
                                                                             'within '
                                                                             'biological '
                                                                             'systems, '
                                                                             'its role '
                                                                             'in '
                                                                             'cellular '
                                                                             'processes, '
                                                                             'and any '
                                                                             'relevant '
                                                                             'technical '
                                                                             'details '
                                                                             'such as '
                                                                             'structure, '
                                                                             'activity, '
                                                                             'and '
                                                                             'interactions '
                                                                             'with '
                                                                             'other '
                                                                             'molecules.',
                                                              'domain_of': ['Protein'],
                                                              'multivalued': True,
                                                              'name': 'functionalAndTechnicalDescription',
                                                              'range': 'string',
                                                              'required': False,
                                                              'title': 'functional and '
                                                                       'technical '
                                                                       'description'},
                        'functionalCharacterization': {'description': 'The process of '
                                                                      'determining and '
                                                                      'describing the '
                                                                      'specific '
                                                                      'biological '
                                                                      'activities and '
                                                                      'roles of a '
                                                                      'protein. '
                                                                      'Possible values '
                                                                      'include '
                                                                      "'Functionally "
                                                                      "characterized' "
                                                                      "(the protein's "
                                                                      'functions have '
                                                                      'been identified '
                                                                      'and described) '
                                                                      "and 'No "
                                                                      'functional '
                                                                      "characterization' "
                                                                      "(the protein's "
                                                                      'functions have '
                                                                      'not been '
                                                                      'identified or '
                                                                      'described).',
                                                       'domain_of': ['Protein'],
                                                       'multivalued': True,
                                                       'name': 'functionalCharacterization',
                                                       'range': 'string',
                                                       'required': False,
                                                       'title': 'functional '
                                                                'characterization'},
                        'inclusionBodiesType': {'description': 'Refers to the state of '
                                                               'aggregated proteins '
                                                               'within a cell. '
                                                               'Possible values '
                                                               "include 'Denatured' "
                                                               '(proteins are in an '
                                                               'unfolded, inactive '
                                                               "state) and 'Refolded' "
                                                               '(proteins have been '
                                                               'processed to regain '
                                                               'their functional, '
                                                               'active conformation).',
                                                'domain_of': ['Protein'],
                                                'multivalued': True,
                                                'name': 'inclusionBodiesType',
                                                'range': 'string',
                                                'required': False,
                                                'title': 'inclusion bodies type'},
                        'proteinPurification': {'description': 'Refers to the degree '
                                                               'of purity achieved for '
                                                               'a protein sample. '
                                                               'Possible values '
                                                               "include '>95%' (the "
                                                               'protein is highly '
                                                               'purified, with more '
                                                               'than 95% purity) and '
                                                               "'Unpurified expression "
                                                               'host lysate or partly '
                                                               "purified protein' (the "
                                                               'protein is either '
                                                               'unpurified and present '
                                                               'in the host cell '
                                                               'lysate or only '
                                                               'partially purified).',
                                                'domain_of': ['Protein'],
                                                'multivalued': True,
                                                'name': 'proteinPurification',
                                                'range': 'string',
                                                'required': False,
                                                'title': 'protein purification'},
                        'relatedPdb': {'close_mappings': ['wdp:P638'],
                                       'description': 'Identifier for 3D structural '
                                                      'data as per the PDB (Protein '
                                                      'Data Bank) database',
                                       'domain_of': ['Protein'],
                                       'multivalued': True,
                                       'name': 'relatedPdb',
                                       'range': 'PdbReference',
                                       'required': False,
                                       'title': 'related PDB'},
                        'sequence': {'close_mappings': ['geno:0000239', 'bao:0002817'],
                                     'description': 'The related sequence information '
                                                    'from a sequence provider or in '
                                                    'fasta format',
                                     'domain_of': ['Protein',
                                                   'RecombinantPartIdentification',
                                                   'NucleicAcid',
                                                   'Pathogen'],
                                     'multivalued': True,
                                     'name': 'sequence',
                                     'range': 'Sequence',
                                     'related_mappings': ['uniprotrdfs:sequence'],
                                     'required': True,
                                     'title': 'sequence'},
                        'specialFeature': {'description': 'Distinctive attributes of a '
                                                          'product that set it apart '
                                                          'from other similar items '
                                                          'e.g., Reference strain, '
                                                          'Vaccinal strain, Antiviral '
                                                          'resistant strain ...',
                                           'domain_of': ['Protein'],
                                           'multivalued': True,
                                           'name': 'specialFeature',
                                           'range': 'SpecialFeature',
                                           'required': False,
                                           'title': 'special feature'},
                        'tagSequence': {'description': 'The name of the DNA coding '
                                                       'sequence or corresponding '
                                                       'peptide/protein sequence fused '
                                                       'to a sequence of interest, '
                                                       'used to facilitate '
                                                       'experimental operations such '
                                                       'as purification, detection, '
                                                       'localization, tracking, '
                                                       'solubility enhancement, or '
                                                       'selection. Applicable to both '
                                                       'proteins and nucleic acids',
                                        'domain_of': ['Protein', 'NucleicAcid'],
                                        'exact_mappings': ['bao:0002796'],
                                        'multivalued': True,
                                        'name': 'tagSequence',
                                        'range': 'TagSequence',
                                        'required': False,
                                        'title': 'tag sequence'},
                        'tagStatusOfTheSolubilizedProtein': {'description': 'Indicates '
                                                                            'the '
                                                                            'presence '
                                                                            'and '
                                                                            'condition '
                                                                            'of a tag '
                                                                            'on the '
                                                                            'protein '
                                                                            'after '
                                                                            'solubilization. '
                                                                            'Possible '
                                                                            'values '
                                                                            'include '
                                                                            "'Uncleaved "
                                                                            "Tag' (the "
                                                                            'tag is '
                                                                            'still '
                                                                            'attached '
                                                                            'to the '
                                                                            'protein), '
                                                                            "'Cleaved "
                                                                            "Tag' (the "
                                                                            'tag has '
                                                                            'been '
                                                                            'removed '
                                                                            'from the '
                                                                            'protein), '
                                                                            "and 'No "
                                                                            "Tag' (the "
                                                                            'protein '
                                                                            'does not '
                                                                            'have a '
                                                                            'tag)',
                                                             'domain_of': ['Protein'],
                                                             'multivalued': True,
                                                             'name': 'tagStatusOfTheSolubilizedProtein',
                                                             'range': 'string',
                                                             'required': False,
                                                             'title': 'tag status of '
                                                                      'the solubilized '
                                                                      'protein'},
                        'typeOfFunctionalCharacterization': {'description': 'Refers to '
                                                                            'the '
                                                                            'classification '
                                                                            'of a '
                                                                            'protein '
                                                                            'based on '
                                                                            'the '
                                                                            'specific '
                                                                            'type of '
                                                                            'functional '
                                                                            'analysis '
                                                                            'performed '
                                                                            'to '
                                                                            'determine '
                                                                            'its '
                                                                            'biological '
                                                                            'activities '
                                                                            'and '
                                                                            'roles. '
                                                                            'Possible '
                                                                            'values '
                                                                            'include '
                                                                            "'Enzymatic' "
                                                                            '(the '
                                                                            'protein '
                                                                            'has been '
                                                                            'characterized '
                                                                            'for its '
                                                                            'enzyme '
                                                                            'activity) '
                                                                            'and '
                                                                            "'Antigenic' "
                                                                            '(the '
                                                                            'protein '
                                                                            'has been '
                                                                            'characterized '
                                                                            'for its '
                                                                            'ability '
                                                                            'to elicit '
                                                                            'an immune '
                                                                            'response).',
                                                             'domain_of': ['Protein'],
                                                             'multivalued': True,
                                                             'name': 'typeOfFunctionalCharacterization',
                                                             'range': 'string',
                                                             'required': False,
                                                             'title': 'type of '
                                                                      'functional '
                                                                      'Characterization'}},
         'title': 'Protein'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Protein', 'NucleicAcid', 'Pathogen'],
         'related_mappings': ['sepio:0000058']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Protein',
                       'RecombinantPartIdentification',
                       'NucleicAcid',
                       'Pathogen'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence']} })
    relatedPdb: Optional[list[PdbReference]] = Field(default=None, title="related PDB", description="""Identifier for 3D structural data as per the PDB (Protein Data Bank) database""", json_schema_extra = { "linkml_meta": {'alias': 'relatedPdb',
         'close_mappings': ['wdp:P638'],
         'domain_of': ['Protein']} })
    specialFeature: Optional[list[SpecialFeature]] = Field(default=None, title="special feature", description="""Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...""", json_schema_extra = { "linkml_meta": {'alias': 'specialFeature', 'domain_of': ['Protein']} })
    tagSequence: Optional[list[TagSequence]] = Field(default=None, title="tag sequence", description="""The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids""", json_schema_extra = { "linkml_meta": {'alias': 'tagSequence',
         'domain_of': ['Protein', 'NucleicAcid'],
         'exact_mappings': ['bao:0002796']} })
    domain: Optional[list[str]] = Field(default=None, title="domain", description="""A distinct structural and functional unit within the protein, often capable of independent folding and stability, which contributes to the protein's overall function""", json_schema_extra = { "linkml_meta": {'alias': 'domain',
         'close_mappings': ['uniprotrdfs:domain'],
         'domain_of': ['Protein']} })
    expressedAs: Optional[list[Literal["Soluble", "Inclusion bodies"]]] = Field(default=None, title="expressed as", description="""Refers to the form in which the protein is produced and manifested in a biological system. Possible values include 'Soluble' (proteins that are dissolved in the cellular or extracellular fluid) and 'Inclusion bodies' (aggregated proteins that are insoluble and form within the cell)""", json_schema_extra = { "linkml_meta": {'alias': 'expressedAs',
         'close_mappings': ['apollo:00000102'],
         'domain_of': ['Protein'],
         'equals_string_in': ['Soluble', 'Inclusion bodies']} })
    inclusionBodiesType: Optional[list[Literal["Denatured", "Refolded"]]] = Field(default=None, title="inclusion bodies type", description="""Refers to the state of aggregated proteins within a cell. Possible values include 'Denatured' (proteins are in an unfolded, inactive state) and 'Refolded' (proteins have been processed to regain their functional, active conformation).""", json_schema_extra = { "linkml_meta": {'alias': 'inclusionBodiesType',
         'domain_of': ['Protein'],
         'equals_string_in': ['Denatured', 'Refolded']} })
    expressionSystem: Optional[list[Literal["E. coli", "Insect cells", "Mammalian cells"]]] = Field(default=None, title="expression system", description="""The host organism or cellular environment used to produce a protein from a specific gene. Possible values include 'E. coli' (bacterial system), 'Insect cells' (using baculovirus vectors), and 'Mammalian cells' (mammalian cell lines).""", json_schema_extra = { "linkml_meta": {'alias': 'expressionSystem',
         'close_mappings': ['ro:0002206'],
         'domain_of': ['Protein'],
         'equals_string_in': ['E. coli', 'Insect cells', 'Mammalian cells']} })
    functionalCharacterization: Optional[list[Literal["Functionally characterized", "No functional characterization"]]] = Field(default=None, title="functional characterization", description="""The process of determining and describing the specific biological activities and roles of a protein. Possible values include 'Functionally characterized' (the protein's functions have been identified and described) and 'No functional characterization' (the protein's functions have not been identified or described).""", json_schema_extra = { "linkml_meta": {'alias': 'functionalCharacterization',
         'domain_of': ['Protein'],
         'equals_string_in': ['Functionally characterized',
                              'No functional characterization']} })
    functionalAndTechnicalDescription: Optional[list[str]] = Field(default=None, title="functional and technical description", description="""Detailed information about the specific biological functions, mechanisms of action, and technical attributes of a protein. This includes how the protein interacts within biological systems, its role in cellular processes, and any relevant technical details such as structure, activity, and interactions with other molecules.""", json_schema_extra = { "linkml_meta": {'alias': 'functionalAndTechnicalDescription', 'domain_of': ['Protein']} })
    proteinPurification: Optional[list[Literal["Greater than 95 percent", "Unpurified expression host lysate or partly purified protein"]]] = Field(default=None, title="protein purification", description="""Refers to the degree of purity achieved for a protein sample. Possible values include '>95%' (the protein is highly purified, with more than 95% purity) and 'Unpurified expression host lysate or partly purified protein' (the protein is either unpurified and present in the host cell lysate or only partially purified).""", json_schema_extra = { "linkml_meta": {'alias': 'proteinPurification',
         'domain_of': ['Protein'],
         'equals_string_in': ['Greater than 95 percent',
                              'Unpurified expression host lysate or partly purified '
                              'protein']} })
    tagStatusOfTheSolubilizedProtein: Optional[list[str]] = Field(default=None, title="tag status of the solubilized protein", description="""Indicates the presence and condition of a tag on the protein after solubilization. Possible values include 'Uncleaved Tag' (the tag is still attached to the protein), 'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein does not have a tag)""", json_schema_extra = { "linkml_meta": {'alias': 'tagStatusOfTheSolubilizedProtein', 'domain_of': ['Protein']} })
    typeOfFunctionalCharacterization: Optional[list[Literal["Enzymatic", "Antigenic"]]] = Field(default=None, title="type of functional Characterization", description="""Refers to the classification of a protein based on the specific type of functional analysis performed to determine its biological activities and roles. Possible values include 'Enzymatic' (the protein has been characterized for its enzyme activity) and 'Antigenic' (the protein has been characterized for its ability to elicit an immune response).""", json_schema_extra = { "linkml_meta": {'alias': 'typeOfFunctionalCharacterization',
         'domain_of': ['Protein'],
         'equals_string_in': ['Enzymatic', 'Antigenic']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class NucleicAcid(Product):
    """
    Nucleic acid related to a pathogen. It can be extracted or synthetic
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q123619',
                            'ncit:C706',
                            'snomed:27380003',
                            'sio:010008',
                            'chebi:33696',
                            'wd:Q123619',
                            'ncit:C706',
                            'snomed:27380003',
                            'sio:010008',
                            'chebi:33696'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['mi:0318', 'mi:0318'],
         'slot_usage': {'biologicalMaterialOrigin': {'description': 'Information about '
                                                                    'the origin of the '
                                                                    'biological '
                                                                    'material, '
                                                                    'essential for '
                                                                    'access, '
                                                                    'utilization, and '
                                                                    'benefit-sharing '
                                                                    'of genetic '
                                                                    'resources in '
                                                                    'compliance with '
                                                                    'the Nagoya '
                                                                    'Protocol',
                                                     'domain_of': ['NucleicAcid',
                                                                   'Protein',
                                                                   'Pathogen'],
                                                     'multivalued': False,
                                                     'name': 'biologicalMaterialOrigin',
                                                     'range': 'BiologicalMaterialOrigin',
                                                     'related_mappings': ['sepio:0000058'],
                                                     'required': True,
                                                     'title': 'biological material '
                                                              'origin'},
                        'clonedIntoPlasmid': {'description': 'The plasmid into which '
                                                             'the nucleic acid has '
                                                             'been cloned',
                                              'domain_of': ['NucleicAcid'],
                                              'multivalued': False,
                                              'name': 'clonedIntoPlasmid',
                                              'range': 'ExpressionVector',
                                              'recommended': True,
                                              'required': False,
                                              'title': 'cloned into plasmid'},
                        'clonedNucleicAcid': {'description': 'Specification of the '
                                                             'terms and parameters for '
                                                             'transporting',
                                              'domain_of': ['NucleicAcid'],
                                              'multivalued': False,
                                              'name': 'clonedNucleicAcid',
                                              'range': 'boolean',
                                              'required': True,
                                              'title': 'cloned nucleic acid'},
                        'genBankFileOfTheConstruct': {'description': 'A GenBank '
                                                                     'formatted file '
                                                                     'that contains '
                                                                     'detailed '
                                                                     'sequence and '
                                                                     'annotation '
                                                                     'information of a '
                                                                     'nucleic acid '
                                                                     'construct',
                                                      'domain_of': ['NucleicAcid'],
                                                      'multivalued': True,
                                                      'name': 'genBankFileOfTheConstruct',
                                                      'range': 'Data',
                                                      'required': False,
                                                      'title': 'GenBank file of the '
                                                               'construct'},
                        'identificationTechnique': {'description': 'A method or '
                                                                   'procedure used to '
                                                                   'detect, identify, '
                                                                   'and confirm the '
                                                                   'presence of a '
                                                                   'specific nucleic '
                                                                   'acid sequence, '
                                                                   'pathogen, or '
                                                                   'associated '
                                                                   'constructs. This '
                                                                   'may involve '
                                                                   'various techniques '
                                                                   'such as PCR, '
                                                                   'sequencing, '
                                                                   'hybridization, or '
                                                                   'other molecular '
                                                                   'methods, utilizing '
                                                                   'specific tools and '
                                                                   'procedures for '
                                                                   'accurate detection '
                                                                   'and analysis',
                                                    'domain_of': ['NucleicAcid',
                                                                  'Pathogen'],
                                                    'multivalued': False,
                                                    'name': 'identificationTechnique',
                                                    'range': 'string',
                                                    'required': False,
                                                    'title': 'identification '
                                                             'technique'},
                        'mutationObserved': {'description': 'Indicates if the current '
                                                            'nucleic acid has No '
                                                            'mutation compared to the '
                                                            'reference sequence if the '
                                                            'value is set to false or '
                                                            'if it contains mutations '
                                                            '(no frameshift, no '
                                                            'unexpected STOP codon) if '
                                                            'set to true',
                                             'domain_of': ['NucleicAcid'],
                                             'multivalued': False,
                                             'name': 'mutationObserved',
                                             'range': 'boolean',
                                             'required': True,
                                             'title': 'mutation observed'},
                        'observedMutations': {'description': 'The specific mutations '
                                                             'that have been '
                                                             'identified and '
                                                             'documented in the '
                                                             'nucleic acid sequence',
                                              'domain_of': ['NucleicAcid'],
                                              'multivalued': False,
                                              'name': 'observedMutations',
                                              'range': 'string',
                                              'required': False,
                                              'title': 'observed mutations'},
                        'plasmidSelection': {'description': 'Specific selectable '
                                                            'markers in the plasmid, '
                                                            'such as antibiotic '
                                                            'resistance genes, used to '
                                                            'identify and maintain '
                                                            'cells that contain the '
                                                            'plasmid',
                                             'domain_of': ['NucleicAcid'],
                                             'multivalued': True,
                                             'name': 'plasmidSelection',
                                             'range': 'PlasmidSelection',
                                             'recommended': True,
                                             'required': False,
                                             'title': 'plasmid selection'},
                        'regionEncompassedInThisProduct': {'description': 'The '
                                                                          'specific '
                                                                          'region '
                                                                          'encompassed '
                                                                          'in the '
                                                                          'product',
                                                           'domain_of': ['NucleicAcid'],
                                                           'multivalued': False,
                                                           'name': 'regionEncompassedInThisProduct',
                                                           'range': 'string',
                                                           'required': True,
                                                           'title': 'region '
                                                                    'encompassed in '
                                                                    'this Product'},
                        'sequence': {'close_mappings': ['geno:0000239', 'bao:0002817'],
                                     'description': 'The related sequence information '
                                                    'from a sequence provider or in '
                                                    'fasta format',
                                     'domain_of': ['NucleicAcid',
                                                   'RecombinantPartIdentification',
                                                   'Protein',
                                                   'Pathogen'],
                                     'multivalued': True,
                                     'name': 'sequence',
                                     'range': 'Sequence',
                                     'related_mappings': ['uniprotrdfs:sequence'],
                                     'required': True,
                                     'title': 'sequence'},
                        'sequenceChecked': {'comments': ['Sequence check is mandatory '
                                                         'for cloned products'],
                                            'description': 'Tell whether or not the '
                                                           'sequence of the product '
                                                           'was controlled (compulsory '
                                                           'for cloned products)',
                                            'domain_of': ['NucleicAcid'],
                                            'multivalued': False,
                                            'name': 'sequenceChecked',
                                            'range': 'boolean',
                                            'related_mappings': ['iceo:0000336'],
                                            'required': True,
                                            'title': 'sequence checked'},
                        'sequencing': {'comments': ['Cloned products have to be '
                                                    'sequenced'],
                                       'description': 'Refers to the level of '
                                                      'sequencing performed on the '
                                                      'nucleic acid. Possible values '
                                                      "include 'Not sequenced' (no "
                                                      'sequencing has been performed), '
                                                      "'Partly sequenced' (only a "
                                                      'portion of the nucleic acid '
                                                      'sequence has been determined), '
                                                      "and 'Fully sequenced' (the "
                                                      'entire nucleic acid sequence '
                                                      'has been determined).',
                                       'domain_of': ['NucleicAcid'],
                                       'multivalued': False,
                                       'name': 'sequencing',
                                       'range': 'string',
                                       'required': True,
                                       'title': 'sequencing'},
                        'tagSequence': {'description': 'The name of the DNA coding '
                                                       'sequence or corresponding '
                                                       'peptide/protein sequence fused '
                                                       'to a sequence of interest, '
                                                       'used to facilitate '
                                                       'experimental operations such '
                                                       'as purification, detection, '
                                                       'localization, tracking, '
                                                       'solubility enhancement, or '
                                                       'selection. Applicable to both '
                                                       'proteins and nucleic acids',
                                        'domain_of': ['NucleicAcid', 'Protein'],
                                        'exact_mappings': ['bao:0002796'],
                                        'multivalued': False,
                                        'name': 'tagSequence',
                                        'range': 'TagSequence',
                                        'required': True,
                                        'title': 'tag sequence'},
                        'titer': {'description': 'The titer value, its corresponding '
                                                 'unit, and the method of '
                                                 'quantification (e.g., RT-qPCR, '
                                                 'TCID50), representing the '
                                                 'concentration or amount of unit '
                                                 'present in the sample. The titer '
                                                 'corresponds to the highest dilution '
                                                 'factor that still yields a positive '
                                                 'reading',
                                  'domain_of': ['NucleicAcid', 'Pathogen'],
                                  'multivalued': False,
                                  'name': 'titer',
                                  'range': 'string',
                                  'required': False,
                                  'title': 'titer'}},
         'title': 'Nucleic acid'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['NucleicAcid', 'Protein', 'Pathogen'],
         'related_mappings': ['sepio:0000058']} })
    genBankFileOfTheConstruct: Optional[list[Data]] = Field(default=None, title="GenBank file of the construct", description="""A GenBank formatted file that contains detailed sequence and annotation information of a nucleic acid construct""", json_schema_extra = { "linkml_meta": {'alias': 'genBankFileOfTheConstruct', 'domain_of': ['NucleicAcid']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['NucleicAcid',
                       'RecombinantPartIdentification',
                       'Protein',
                       'Pathogen'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence']} })
    clonedNucleicAcid: bool = Field(default=..., title="cloned nucleic acid", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'clonedNucleicAcid', 'domain_of': ['NucleicAcid']} })
    clonedIntoPlasmid: Optional[ExpressionVector] = Field(default=None, title="cloned into plasmid", description="""The plasmid into which the nucleic acid has been cloned""", json_schema_extra = { "linkml_meta": {'alias': 'clonedIntoPlasmid',
         'domain_of': ['NucleicAcid'],
         'recommended': True} })
    plasmidSelection: Optional[list[PlasmidSelection]] = Field(default=None, title="plasmid selection", description="""Specific selectable markers in the plasmid, such as antibiotic resistance genes, used to identify and maintain cells that contain the plasmid""", json_schema_extra = { "linkml_meta": {'alias': 'plasmidSelection', 'domain_of': ['NucleicAcid'], 'recommended': True} })
    tagSequence: TagSequence = Field(default=..., title="tag sequence", description="""The name of the DNA coding sequence or corresponding peptide/protein sequence fused to a sequence of interest, used to facilitate experimental operations such as purification, detection, localization, tracking, solubility enhancement, or selection. Applicable to both proteins and nucleic acids""", json_schema_extra = { "linkml_meta": {'alias': 'tagSequence',
         'domain_of': ['NucleicAcid', 'Protein'],
         'exact_mappings': ['bao:0002796']} })
    regionEncompassedInThisProduct: str = Field(default=..., title="region encompassed in this Product", description="""The specific region encompassed in the product""", json_schema_extra = { "linkml_meta": {'alias': 'regionEncompassedInThisProduct', 'domain_of': ['NucleicAcid']} })
    mutationObserved: bool = Field(default=..., title="mutation observed", description="""Indicates if the current nucleic acid has No mutation compared to the reference sequence if the value is set to false or if it contains mutations (no frameshift, no unexpected STOP codon) if set to true""", json_schema_extra = { "linkml_meta": {'alias': 'mutationObserved', 'domain_of': ['NucleicAcid']} })
    observedMutations: Optional[str] = Field(default=None, title="observed mutations", description="""The specific mutations that have been identified and documented in the nucleic acid sequence""", json_schema_extra = { "linkml_meta": {'alias': 'observedMutations', 'domain_of': ['NucleicAcid']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['NucleicAcid', 'Pathogen']} })
    sequencing: Literal["Not sequenced", "Partly sequenced", "Fully sequenced"] = Field(default=..., title="sequencing", description="""Refers to the level of sequencing performed on the nucleic acid. Possible values include 'Not sequenced' (no sequencing has been performed), 'Partly sequenced' (only a portion of the nucleic acid sequence has been determined), and 'Fully sequenced' (the entire nucleic acid sequence has been determined).""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing',
         'comments': ['Cloned products have to be sequenced'],
         'domain_of': ['NucleicAcid'],
         'equals_string_in': ['Not sequenced', 'Partly sequenced', 'Fully sequenced']} })
    titer: Optional[str] = Field(default=None, title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['NucleicAcid', 'Pathogen'],
         'related_mappings': ['wd:Q2166189']} })
    sequenceChecked: bool = Field(default=..., title="sequence checked", description="""Tell whether or not the sequence of the product was controlled (compulsory for cloned products)""", json_schema_extra = { "linkml_meta": {'alias': 'sequenceChecked',
         'comments': ['Sequence check is mandatory for cloned products'],
         'domain_of': ['NucleicAcid'],
         'related_mappings': ['iceo:0000336']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class DetectionKit(Product):
    """
    A detection kit for specific pathogens
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['mesh:D011933', 'mesh:D011933'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'specificity': {'description': 'Details on the ability of a '
                                                       'detection kit to correctly '
                                                       'identify negative results, '
                                                       'distinguishing between the '
                                                       'target analyte and other '
                                                       'substances without '
                                                       'cross-reacting',
                                        'domain_of': ['DetectionKit'],
                                        'multivalued': False,
                                        'name': 'specificity',
                                        'range': 'string',
                                        'required': False,
                                        'title': 'specificity'},
                        'specificityDocumented': {'description': 'Boolean value '
                                                                 'indicating whether '
                                                                 'the specificity of '
                                                                 'the product has been '
                                                                 'formally documented',
                                                  'domain_of': ['DetectionKit',
                                                                'Antibody'],
                                                  'multivalued': False,
                                                  'name': 'specificityDocumented',
                                                  'range': 'boolean',
                                                  'required': True,
                                                  'title': 'specificity documented'},
                        'standardOperatingProcedureFile': {'description': 'The related '
                                                                          'standard '
                                                                          'operating '
                                                                          'procedure '
                                                                          'file (SOP)',
                                                           'domain_of': ['DetectionKit'],
                                                           'multivalued': True,
                                                           'name': 'standardOperatingProcedureFile',
                                                           'range': 'File',
                                                           'required': False,
                                                           'title': 'standard '
                                                                    'operating '
                                                                    'procedure file'},
                        'targetedRegion': {'description': 'The specific area or '
                                                          'sequence within the target '
                                                          'analyte that the detection '
                                                          'kit is designed to identify '
                                                          'and interact with, ensuring '
                                                          'accurate detection and '
                                                          'analysis.',
                                           'domain_of': ['DetectionKit'],
                                           'multivalued': False,
                                           'name': 'targetedRegion',
                                           'range': 'string',
                                           'required': False,
                                           'title': 'targeted region'}},
         'title': 'Detection Kit'})

    standardOperatingProcedureFile: Optional[list[File]] = Field(default=None, title="standard operating procedure file", description="""The related standard operating procedure file (SOP)""", json_schema_extra = { "linkml_meta": {'alias': 'standardOperatingProcedureFile', 'domain_of': ['DetectionKit']} })
    specificityDocumented: bool = Field(default=..., title="specificity documented", description="""Boolean value indicating whether the specificity of the product has been formally documented""", json_schema_extra = { "linkml_meta": {'alias': 'specificityDocumented', 'domain_of': ['DetectionKit', 'Antibody']} })
    specificity: Optional[str] = Field(default=None, title="specificity", description="""Details on the ability of a detection kit to correctly identify negative results, distinguishing between the target analyte and other substances without cross-reacting""", json_schema_extra = { "linkml_meta": {'alias': 'specificity', 'domain_of': ['DetectionKit']} })
    targetedRegion: Optional[str] = Field(default=None, title="targeted region", description="""The specific area or sequence within the target analyte that the detection kit is designed to identify and interact with, ensuring accurate detection and analysis.""", json_schema_extra = { "linkml_meta": {'alias': 'targetedRegion', 'domain_of': ['DetectionKit']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Bundle(Product):
    """
    A grouping of products and/or services intentionally combined into a single offering, typically to provide added value, convenience, or specific experimental utility
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q1020767', 'wd:Q1020767'],
         'exact_mappings': ['schema:ProductCollection', 'schema:ProductCollection'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C54696', 'ncit:C54696'],
         'slot_usage': {'itemsOfTheBundle': {'close_mappings': ['schema:includesObject'],
                                             'description': 'Specifies the constituent '
                                                            'products and/or services '
                                                            'that are part of the '
                                                            'bundle',
                                             'domain_of': ['Bundle'],
                                             'multivalued': True,
                                             'name': 'itemsOfTheBundle',
                                             'range': 'Product',
                                             'required': True,
                                             'title': 'items of the bundle'}},
         'title': 'Bundle'})

    itemsOfTheBundle: list[Product] = Field(default=..., title="items of the bundle", description="""Specifies the constituent products and/or services that are part of the bundle""", json_schema_extra = { "linkml_meta": {'alias': 'itemsOfTheBundle',
         'close_mappings': ['schema:includesObject'],
         'domain_of': ['Bundle']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Pathogen(Product):
    """
    Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'close_mappings': ['wd:Q170065',
                            'ncit:C80324',
                            'sio:010414',
                            'ido:0000528',
                            'apollo:00000237',
                            'wd:Q170065',
                            'ncit:C80324',
                            'sio:010414',
                            'ido:0000528',
                            'apollo:00000237'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['schema:infectiousAgent',
                              'schema:InfectiousAgentClass',
                              'doid:0050117',
                              'mondo:0005550',
                              'schema:infectiousAgent',
                              'schema:InfectiousAgentClass',
                              'doid:0050117',
                              'mondo:0005550'],
         'slot_usage': {'biologicalMaterialOrigin': {'description': 'Information about '
                                                                    'the origin of the '
                                                                    'biological '
                                                                    'material, '
                                                                    'essential for '
                                                                    'access, '
                                                                    'utilization, and '
                                                                    'benefit-sharing '
                                                                    'of genetic '
                                                                    'resources in '
                                                                    'compliance with '
                                                                    'the Nagoya '
                                                                    'Protocol',
                                                     'domain_of': ['Pathogen',
                                                                   'Protein',
                                                                   'NucleicAcid'],
                                                     'multivalued': False,
                                                     'name': 'biologicalMaterialOrigin',
                                                     'range': 'BiologicalMaterialOrigin',
                                                     'related_mappings': ['sepio:0000058'],
                                                     'required': True,
                                                     'title': 'biological material '
                                                              'origin'},
                        'clinicalInformation': {'description': 'Details about the '
                                                               'clinical aspects of '
                                                               'the pathogen, '
                                                               'including symptoms, '
                                                               'severity, treatment '
                                                               'protocols, and patient '
                                                               'outcomes',
                                                'domain_of': ['Pathogen'],
                                                'multivalued': False,
                                                'name': 'clinicalInformation',
                                                'range': 'string',
                                                'related_mappings': ['ncit:C25398'],
                                                'required': False,
                                                'title': 'clinical information'},
                        'cultivability': {'comments': ['Might also be related to a '
                                                       'product sub-category that '
                                                       'helps filtering'],
                                          'description': 'The ability of the pathogen '
                                                         'to be cultivated or grown in '
                                                         'laboratory conditions. '
                                                         'Possible values are  '
                                                         "'Cultivable pathogen', "
                                                         "'Uncultivable pathogen' or "
                                                         "'Inactivated pathogen'",
                                          'domain_of': ['Pathogen'],
                                          'ifabsent': 'string(Cultivable)',
                                          'multivalued': False,
                                          'name': 'cultivability',
                                          'range': 'string',
                                          'required': True,
                                          'title': 'cultivability'},
                        'genomeSequencing': {'close_mappings': ['bao:0002788'],
                                             'description': 'The extent of the '
                                                            "pathogen's genetic "
                                                            'material that has been '
                                                            'sequenced, with possible '
                                                            'values including '
                                                            "'Complete genome' for the "
                                                            "entire genome, 'Complete "
                                                            "coding sequence' for all "
                                                            'coding regions, and '
                                                            "'Partial sequence' for "
                                                            'only a portion of the '
                                                            'genetic material',
                                             'domain_of': ['Pathogen'],
                                             'multivalued': False,
                                             'name': 'genomeSequencing',
                                             'range': 'string',
                                             'required': True,
                                             'title': 'genome sequencing'},
                        'identificationTechnique': {'description': 'A method or '
                                                                   'procedure used to '
                                                                   'detect, identify, '
                                                                   'and confirm the '
                                                                   'presence of a '
                                                                   'specific nucleic '
                                                                   'acid sequence, '
                                                                   'pathogen, or '
                                                                   'associated '
                                                                   'constructs. This '
                                                                   'may involve '
                                                                   'various techniques '
                                                                   'such as PCR, '
                                                                   'sequencing, '
                                                                   'hybridization, or '
                                                                   'other molecular '
                                                                   'methods, utilizing '
                                                                   'specific tools and '
                                                                   'procedures for '
                                                                   'accurate detection '
                                                                   'and analysis',
                                                    'domain_of': ['Pathogen',
                                                                  'NucleicAcid'],
                                                    'multivalued': False,
                                                    'name': 'identificationTechnique',
                                                    'range': 'string',
                                                    'required': False,
                                                    'title': 'identification '
                                                             'technique'},
                        'infectivity': {'description': 'Indicates the ability of the '
                                                       'pathogen to establish an '
                                                       'infection in a host organism, '
                                                       'with possible values detailing '
                                                       'whether infectivity has been '
                                                       'tested, quantified, or cannot '
                                                       'be tested due to '
                                                       'non-cultivable nature.',
                                        'domain_of': ['Pathogen'],
                                        'multivalued': False,
                                        'name': 'infectivity',
                                        'range': 'string',
                                        'required': True,
                                        'title': 'infectivity'},
                        'infectivityTest': {'description': 'The description of the '
                                                           'completed infectivity '
                                                           'test, providing details on '
                                                           'the methods, conditions, '
                                                           'and results of the test '
                                                           'used to assess the '
                                                           "pathogen's ability to "
                                                           'infect a host organism',
                                            'domain_of': ['Pathogen'],
                                            'multivalued': False,
                                            'name': 'infectivityTest',
                                            'range': 'string',
                                            'related_mappings': ['cido:0001195'],
                                            'required': False,
                                            'title': 'infectivity Test'},
                        'isolationConditions': {'description': 'The environmental and '
                                                               'procedural conditions '
                                                               'under which the '
                                                               'pathogen was isolated',
                                                'domain_of': ['Pathogen'],
                                                'multivalued': False,
                                                'name': 'isolationConditions',
                                                'range': 'string',
                                                'required': False,
                                                'title': 'isolation conditions'},
                        'isolationHost': {'description': 'The host organism from which '
                                                         'the pathogen was originally '
                                                         'isolated',
                                          'domain_of': ['Pathogen'],
                                          'multivalued': True,
                                          'name': 'isolationHost',
                                          'range': 'IsolationHost',
                                          'required': False,
                                          'title': 'isolation host'},
                        'isolationTechnique': {'description': 'The specific method or '
                                                              'procedure used to '
                                                              'isolate the pathogen '
                                                              'from a host organism or '
                                                              'sample, detailing the '
                                                              'techniques and tools '
                                                              'employed in the '
                                                              'isolation process',
                                               'domain_of': ['Pathogen'],
                                               'multivalued': False,
                                               'name': 'isolationTechnique',
                                               'range': 'string',
                                               'required': False,
                                               'title': 'isolation technique'},
                        'letterOfAuthority': {'description': 'Indicate whether a '
                                                             'Letter of Authority is '
                                                             'required, confirming the '
                                                             'necessity of formal '
                                                             'authorization. The '
                                                             'possible values are '
                                                             "'N/A', 'NOT Required', "
                                                             "'Required for customers "
                                                             "in the EU' or 'Required'",
                                              'domain_of': ['Pathogen'],
                                              'ifabsent': 'string(Not applicable)',
                                              'multivalued': False,
                                              'name': 'letterOfAuthority',
                                              'range': 'string',
                                              'required': True,
                                              'title': 'letter of authority'},
                        'passage': {'description': 'The number of times the pathogen '
                                                   'was cultured through serial '
                                                   'passage, a process used to '
                                                   'increase the stock but which can '
                                                   'also lead to the evolution of the '
                                                   'original pathogen.',
                                    'domain_of': ['Pathogen'],
                                    'multivalued': False,
                                    'name': 'passage',
                                    'range': 'string',
                                    'related_mappings': ['ncit:C164572'],
                                    'required': False,
                                    'title': 'passage'},
                        'productionCellLine': {'description': 'The cell line used for '
                                                              'the production or '
                                                              'propagation of the '
                                                              'pathogen, detailing the '
                                                              'cellular environment '
                                                              'employed in its '
                                                              'cultivation and study',
                                               'domain_of': ['Pathogen'],
                                               'multivalued': True,
                                               'name': 'productionCellLine',
                                               'range': 'ProductionCellLine',
                                               'required': False,
                                               'title': 'production cell line'},
                        'propagationHost': {'description': 'The host organism that '
                                                           'propagates the pathogen',
                                            'domain_of': ['Pathogen'],
                                            'multivalued': True,
                                            'name': 'propagationHost',
                                            'range': 'PropagationHost',
                                            'required': False,
                                            'title': 'propagation host'},
                        'sequence': {'close_mappings': ['geno:0000239', 'bao:0002817'],
                                     'description': 'The related sequence information '
                                                    'from a sequence provider or in '
                                                    'fasta format',
                                     'domain_of': ['Pathogen',
                                                   'RecombinantPartIdentification',
                                                   'Protein',
                                                   'NucleicAcid'],
                                     'multivalued': True,
                                     'name': 'sequence',
                                     'range': 'Sequence',
                                     'required': True,
                                     'title': 'sequence'},
                        'suspectedEpidemiologicalOrigin': {'description': 'The '
                                                                          'potential '
                                                                          'geographical '
                                                                          'or '
                                                                          'environmental '
                                                                          'source from '
                                                                          'which the '
                                                                          'pathogen is '
                                                                          'believed to '
                                                                          'have '
                                                                          'originated '
                                                                          'or been '
                                                                          'transmitted',
                                                           'domain_of': ['Pathogen'],
                                                           'multivalued': True,
                                                           'name': 'suspectedEpidemiologicalOrigin',
                                                           'range': 'GeographicalOrigin',
                                                           'related_mappings': ['schema:countryOfOrigin',
                                                                                'dct:spatial'],
                                                           'required': False,
                                                           'title': 'suspected '
                                                                    'epidemiological '
                                                                    'origin'},
                        'titer': {'description': 'The titer value, its corresponding '
                                                 'unit, and the method of '
                                                 'quantification (e.g., RT-qPCR, '
                                                 'TCID50), representing the '
                                                 'concentration or amount of unit '
                                                 'present in the sample. The titer '
                                                 'corresponds to the highest dilution '
                                                 'factor that still yields a positive '
                                                 'reading',
                                  'domain_of': ['Pathogen', 'NucleicAcid'],
                                  'multivalued': False,
                                  'name': 'titer',
                                  'range': 'string',
                                  'related_mappings': ['wd:Q2166189'],
                                  'required': True,
                                  'title': 'titer'},
                        'transmissionMethod': {'close_mappings': ['schema:transmissionMethod'],
                                               'description': 'The method or route '
                                                              'through which the '
                                                              'pathogen is transmitted '
                                                              'from one host to '
                                                              'another, detailing the '
                                                              'mechanisms of infection '
                                                              'spread.',
                                               'domain_of': ['Pathogen'],
                                               'multivalued': True,
                                               'name': 'transmissionMethod',
                                               'range': 'TransmissionMethod',
                                               'required': False,
                                               'title': 'transmission method'}},
         'title': 'Pathogen'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Virus(Pathogen):
    """
    The virus as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q808',
                            'schema:Virus',
                            'biolink:virus',
                            'xco:0000237',
                            'ncit:C14283',
                            'wd:Q808',
                            'schema:Virus',
                            'biolink:virus',
                            'xco:0000237',
                            'ncit:C14283'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncbitaxon:10239',
                              'snomed:49872002',
                              'doid:934',
                              'mondo:0005108',
                              'ncbitaxon:10239',
                              'snomed:49872002',
                              'doid:934',
                              'mondo:0005108'],
         'slot_usage': {'coInfectingViruses': {'close_mappings': ['dwc:associatedTaxa'],
                                               'description': 'Identifies other '
                                                              'viruses that may '
                                                              'co-infect the host '
                                                              'organism along with the '
                                                              'primary virus, '
                                                              'indicating the presence '
                                                              'of multiple viral '
                                                              'infections within the '
                                                              'same host.',
                                               'domain_of': ['Virus'],
                                               'multivalued': True,
                                               'name': 'coInfectingViruses',
                                               'range': 'VirusName',
                                               'related_mappings': ['efo:0010716',
                                                                    'mesh:D060085'],
                                               'required': False,
                                               'title': 'co-infecting viruses'},
                        'contaminationWithCoInfectingViruses': {'description': 'A '
                                                                               'boolean '
                                                                               'value '
                                                                               'indicating '
                                                                               'whether '
                                                                               'there '
                                                                               'is '
                                                                               'contamination '
                                                                               'with '
                                                                               'co-infecting '
                                                                               'viruses',
                                                                'domain_of': ['Virus'],
                                                                'ifabsent': 'false',
                                                                'multivalued': False,
                                                                'name': 'contaminationWithCoInfectingViruses',
                                                                'range': 'boolean',
                                                                'required': True,
                                                                'title': 'contamination '
                                                                         'with '
                                                                         'co-infecting '
                                                                         'viruses'},
                        'mycoplasmicContent': {'description': 'Indicates the presence '
                                                              'of mycoplasma '
                                                              'contamination within '
                                                              'the sample',
                                               'domain_of': ['Virus'],
                                               'multivalued': False,
                                               'name': 'mycoplasmicContent',
                                               'range': 'boolean',
                                               'required': True,
                                               'title': 'mycoplasmic content'}},
         'title': 'Virus'})

    coInfectingViruses: Optional[list[VirusName]] = Field(default=None, title="co-infecting viruses", description="""Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host.""", json_schema_extra = { "linkml_meta": {'alias': 'coInfectingViruses',
         'close_mappings': ['dwc:associatedTaxa'],
         'domain_of': ['Virus'],
         'related_mappings': ['efo:0010716', 'mesh:D060085']} })
    contaminationWithCoInfectingViruses: bool = Field(default=False, title="contamination with co-infecting viruses", description="""A boolean value indicating whether there is contamination with co-infecting viruses""", json_schema_extra = { "linkml_meta": {'alias': 'contaminationWithCoInfectingViruses',
         'domain_of': ['Virus'],
         'ifabsent': 'false'} })
    mycoplasmicContent: bool = Field(default=..., title="mycoplasmic content", description="""Indicates the presence of mycoplasma contamination within the sample""", json_schema_extra = { "linkml_meta": {'alias': 'mycoplasmicContent', 'domain_of': ['Virus']} })
    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Bacterium(Pathogen):
    """
    The bacterium as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q10876',
                            'schema:Bacteria',
                            'ncit:C14187',
                            'xco:0000475',
                            'wd:Q10876',
                            'schema:Bacteria',
                            'ncit:C14187',
                            'xco:0000475'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:41146007',
                              'ncbitaxon:2',
                              'doid:104',
                              'mondo:0005113',
                              'snomed:41146007',
                              'ncbitaxon:2',
                              'doid:104',
                              'mondo:0005113'],
         'title': 'Bacterium'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Fungus(Pathogen):
    """
    The fungus as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q764',
                            'schema:Fungus',
                            'ncit:C14209',
                            'wd:Q764',
                            'schema:Fungus',
                            'ncit:C14209'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:414561005',
                              'ncbitaxon:4751',
                              'doid:1564',
                              'mondo:0002041',
                              'snomed:414561005',
                              'ncbitaxon:4751',
                              'doid:1564',
                              'mondo:0002041'],
         'title': 'Fungus'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Protozoan(Pathogen):
    """
    The protozoan as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q101274',
                            'schema:Protozoa',
                            'vo:0000333',
                            'wd:Q101274',
                            'schema:Protozoa',
                            'vo:0000333'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:95896000',
                              'snomed:417396000',
                              'snomed:95896000',
                              'snomed:417396000'],
         'title': 'Protozoan'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Viroid(Pathogen):
    """
    The viroid as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q209917', 'ncit:C95945', 'wd:Q209917', 'ncit:C95945'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:88117008', 'snomed:88117008'],
         'title': 'Viroid'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Prion(Pathogen):
    """
    The prion as a biological material
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q47051',
                            'schema:Prion',
                            'xco:0000655',
                            'wd:Q47051',
                            'schema:Prion',
                            'xco:0000655'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['snomed:84676004',
                              'doid:649',
                              'snomed:84676004',
                              'doid:649'],
         'title': 'Prion'})

    biologicalMaterialOrigin: BiologicalMaterialOrigin = Field(default=..., title="biological material origin", description="""Information about the origin of the biological material, essential for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol""", json_schema_extra = { "linkml_meta": {'alias': 'biologicalMaterialOrigin',
         'domain_of': ['Pathogen', 'Protein', 'NucleicAcid'],
         'related_mappings': ['sepio:0000058']} })
    suspectedEpidemiologicalOrigin: Optional[list[GeographicalOrigin]] = Field(default=None, title="suspected epidemiological origin", description="""The potential geographical or environmental source from which the pathogen is believed to have originated or been transmitted""", json_schema_extra = { "linkml_meta": {'alias': 'suspectedEpidemiologicalOrigin',
         'domain_of': ['Pathogen'],
         'related_mappings': ['schema:countryOfOrigin', 'dct:spatial']} })
    isolationHost: Optional[list[IsolationHost]] = Field(default=None, title="isolation host", description="""The host organism from which the pathogen was originally isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationHost', 'domain_of': ['Pathogen']} })
    productionCellLine: Optional[list[ProductionCellLine]] = Field(default=None, title="production cell line", description="""The cell line used for the production or propagation of the pathogen, detailing the cellular environment employed in its cultivation and study""", json_schema_extra = { "linkml_meta": {'alias': 'productionCellLine', 'domain_of': ['Pathogen']} })
    propagationHost: Optional[list[PropagationHost]] = Field(default=None, title="propagation host", description="""The host organism that propagates the pathogen""", json_schema_extra = { "linkml_meta": {'alias': 'propagationHost', 'domain_of': ['Pathogen']} })
    transmissionMethod: Optional[list[TransmissionMethod]] = Field(default=None, title="transmission method", description="""The method or route through which the pathogen is transmitted from one host to another, detailing the mechanisms of infection spread.""", json_schema_extra = { "linkml_meta": {'alias': 'transmissionMethod',
         'close_mappings': ['schema:transmissionMethod'],
         'domain_of': ['Pathogen']} })
    sequence: list[Sequence] = Field(default=..., title="sequence", description="""The related sequence information from a sequence provider or in fasta format""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'close_mappings': ['geno:0000239', 'bao:0002817'],
         'domain_of': ['Pathogen',
                       'RecombinantPartIdentification',
                       'Protein',
                       'NucleicAcid'],
         'recommended': True,
         'related_mappings': ['uniprotrdfs:sequence', 'uniprotrdfs:sequence']} })
    cultivability: Literal["Cultivable", "Uncultivable", "Inactivated"] = Field(default="Cultivable", title="cultivability", description="""The ability of the pathogen to be cultivated or grown in laboratory conditions. Possible values are  'Cultivable pathogen', 'Uncultivable pathogen' or 'Inactivated pathogen'""", json_schema_extra = { "linkml_meta": {'alias': 'cultivability',
         'comments': ['Might also be related to a product sub-category that helps '
                      'filtering'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Cultivable', 'Uncultivable', 'Inactivated'],
         'ifabsent': 'string(Cultivable)'} })
    clinicalInformation: Optional[str] = Field(default=None, title="clinical information", description="""Details about the clinical aspects of the pathogen, including symptoms, severity, treatment protocols, and patient outcomes""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalInformation',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C25398']} })
    identificationTechnique: Optional[str] = Field(default=None, title="identification technique", description="""A method or procedure used to detect, identify, and confirm the presence of a specific nucleic acid sequence, pathogen, or associated constructs. This may involve various techniques such as PCR, sequencing, hybridization, or other molecular methods, utilizing specific tools and procedures for accurate detection and analysis""", json_schema_extra = { "linkml_meta": {'alias': 'identificationTechnique', 'domain_of': ['Pathogen', 'NucleicAcid']} })
    infectivity: Literal["Infectivity tested", "Infectivity tested and quantified", "Non cultivable sample, infectivity cannot be tested"] = Field(default=..., title="infectivity", description="""Indicates the ability of the pathogen to establish an infection in a host organism, with possible values detailing whether infectivity has been tested, quantified, or cannot be tested due to non-cultivable nature.""", json_schema_extra = { "linkml_meta": {'alias': 'infectivity',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Infectivity tested',
                              'Infectivity tested and quantified',
                              'Non cultivable sample, infectivity cannot be tested']} })
    infectivityTest: Optional[str] = Field(default=None, title="infectivity Test", description="""The description of the completed infectivity test, providing details on the methods, conditions, and results of the test used to assess the pathogen's ability to infect a host organism""", json_schema_extra = { "linkml_meta": {'alias': 'infectivityTest',
         'domain_of': ['Pathogen'],
         'related_mappings': ['cido:0001195']} })
    isolationTechnique: Optional[str] = Field(default=None, title="isolation technique", description="""The specific method or procedure used to isolate the pathogen from a host organism or sample, detailing the techniques and tools employed in the isolation process""", json_schema_extra = { "linkml_meta": {'alias': 'isolationTechnique', 'domain_of': ['Pathogen']} })
    isolationConditions: Optional[str] = Field(default=None, title="isolation conditions", description="""The environmental and procedural conditions under which the pathogen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'isolationConditions', 'domain_of': ['Pathogen']} })
    letterOfAuthority: Literal["Not applicable", "Not required", "Required for customers in the EU", "Required"] = Field(default="Not applicable", title="letter of authority", description="""Indicate whether a Letter of Authority is required, confirming the necessity of formal authorization. The possible values are 'N/A', 'NOT Required', 'Required for customers in the EU' or 'Required'""", json_schema_extra = { "linkml_meta": {'alias': 'letterOfAuthority',
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Not applicable',
                              'Not required',
                              'Required for customers in the EU',
                              'Required'],
         'ifabsent': 'string(Not applicable)'} })
    passage: Optional[str] = Field(default=None, title="passage", description="""The number of times the pathogen was cultured through serial passage, a process used to increase the stock but which can also lead to the evolution of the original pathogen.""", json_schema_extra = { "linkml_meta": {'alias': 'passage',
         'domain_of': ['Pathogen'],
         'related_mappings': ['ncit:C164572']} })
    genomeSequencing: Literal["Complete genome", "Complete coding sequence", "Partial sequence"] = Field(default=..., title="genome sequencing", description="""The extent of the pathogen's genetic material that has been sequenced, with possible values including 'Complete genome' for the entire genome, 'Complete coding sequence' for all coding regions, and 'Partial sequence' for only a portion of the genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'genomeSequencing',
         'close_mappings': ['bao:0002788'],
         'domain_of': ['Pathogen'],
         'equals_string_in': ['Complete genome',
                              'Complete coding sequence',
                              'Partial sequence']} })
    titer: str = Field(default=..., title="titer", description="""The titer value, its corresponding unit, and the method of quantification (e.g., RT-qPCR, TCID50), representing the concentration or amount of unit present in the sample. The titer corresponds to the highest dilution factor that still yields a positive reading""", json_schema_extra = { "linkml_meta": {'alias': 'titer',
         'domain_of': ['Pathogen', 'NucleicAcid'],
         'related_mappings': ['wd:Q2166189']} })
    iataClassification: IataClassification = Field(default=..., title="IATA classification", description="""The corresponding International Air Transport Association (IATA)'s category for this Product""", json_schema_extra = { "linkml_meta": {'alias': 'iataClassification',
         'close_mappings': ['wdp:P238', 'schema:iataCode'],
         'domain_of': ['Product']} })
    shippingConditions: str = Field(default=..., title="shipping conditions", description="""Specification of the terms and parameters for transporting""", json_schema_extra = { "linkml_meta": {'alias': 'shippingConditions',
         'close_mappings': ['schema:shippingConditions'],
         'domain_of': ['Product']} })
    materialSafetyDataSheet: Optional[ReasearchInfrastructure] = Field(default=None, title="material safety data sheet", description="""A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyDataSheet',
         'comments': ['The MSD  is a document that provides detailed information about '
                      'the properties, hazards, handling, storage, and emergency '
                      'procedures related to the use of a chemical or substance'],
         'domain_of': ['Product']} })
    originator: Optional[Originator] = Field(default=None, title="originator", description="""The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'originator',
         'close_mappings': ['dct:provenance'],
         'domain_of': ['Product']} })
    storageConditions: str = Field(default=..., title="storage conditions", description="""Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors.""", json_schema_extra = { "linkml_meta": {'alias': 'storageConditions',
         'comments': ["e.g, could be a xsd:string in enumeration ('Freeze Dried', "
                      "'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage "
                      "Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', "
                      "'Ethanol -20C', 'Ethanol -80C', 'Dried')"],
         'domain_of': ['Product']} })
    thirdPartyDistributionConsent: Optional[bool] = Field(default=None, title="third party distribution consent", description="""Indicates whether the biological material can be distributed without restriction to third parties, as indicated by the ABS permit, in case an ABS permit is required""", json_schema_extra = { "linkml_meta": {'alias': 'thirdPartyDistributionConsent', 'domain_of': ['Product']} })
    usageRestrictions: Optional[str] = Field(default=None, title="usage restrictions", description="""Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material""", json_schema_extra = { "linkml_meta": {'alias': 'usageRestrictions', 'domain_of': ['Product']} })
    accessPointUrl: str = Field(default=..., title="access point URL", description="""The URL that permits to access to the product/service detailed description page on the provider's website and/or allows to place an order about it or at least describe the process to place an order/enquiry""", json_schema_extra = { "linkml_meta": {'alias': 'accessPointUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:serviceURL'],
         'related_mappings': ['dcat:landingPage']} })
    refSku: str = Field(default=..., title="ref SKU", description="""The reference or the stock keeping unit of the service or item provided in the provider's catalogue""", json_schema_extra = { "linkml_meta": {'alias': 'refSku',
         'broad_mappings': ['dct:identifier', 'schema:identifier'],
         'close_mappings': ['dwc:catalogNumber'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:sku']} })
    unitDefinition: Optional[str] = Field(default=None, title="unit definition", description="""A short description of what will be delivered by ordering one unit of this item""", json_schema_extra = { "linkml_meta": {'alias': 'unitDefinition',
         'comments': ['The description of what will be delivered to the end-user '
                      '(e.g.: packaging, quantity...)'],
         'domain_of': ['ProductOrService'],
         'recommended': True,
         'related_mappings': ['dct:format']} })
    category: ProductCategory = Field(default=..., title="category", description="""The main category of the service or product""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'close_mappings': ['schema:category', 'gr:category'],
         'domain_of': ['ProductOrService'],
         'slot_uri': 'dcat:theme'} })
    additionalCategory: Optional[list[ProductCategory]] = Field(default=None, title="additional category", description="""Any category apart from its main category in which this product or service can fit""", json_schema_extra = { "linkml_meta": {'alias': 'additionalCategory',
         'close_mappings': ['schema:additionalType'],
         'domain_of': ['ProductOrService'],
         'is_a': 'category',
         'recommended': True} })
    unitCost: Optional[Decimal] = Field(default=None, title="unit cost", description="""The cost per access for one unit as defined by the unit definition""", json_schema_extra = { "linkml_meta": {'alias': 'unitCost',
         'close_mappings': ['schema:price'],
         'comments': ['The cost per access may not always be defined as a fixed '
                      'numerical value. In some cases, the price is conditional or '
                      'available only upon request. To accommodate such cases, '
                      'descriptive information should be provided through the property '
                      'EVORAO:unitCostNote (xsd:string). This allows handling of cost '
                      'statements such as “on request,” “depends on volume,” or “free '
                      'access for academics,” which cannot be captured by a simple '
                      'numeric value.'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    unitCostCurrency: Optional[str] = Field(default="EUR", title="unit cost currency", description="""The currency in which the unit cost is expressed, following ISO 4217 three-letter codes (e.g., EUR, USD)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostCurrency',
         'close_mappings': ['schema:priceCurrency'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(EUR)',
         'recommended': True} })
    unitCostNote: Optional[str] = Field(default=None, title="unit cost note", description="""A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)""", json_schema_extra = { "linkml_meta": {'alias': 'unitCostNote', 'domain_of': ['ProductOrService']} })
    qualityGrading: Optional[str] = Field(default=None, title="quality grading", description="""Information that permits to assess the quality level of what will be provided""", json_schema_extra = { "linkml_meta": {'alias': 'qualityGrading',
         'close_mappings': ['bao:0002662', 'sio:000217'],
         'domain_of': ['ProductOrService']} })
    pathogenIdentification: list[PathogenIdentification] = Field(default=..., title="pathogen identification", description="""The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item.""", json_schema_extra = { "linkml_meta": {'alias': 'pathogenIdentification',
         'comments': ['The pathogen identification contains information about name and '
                      'taxon but in some cases(e.g: FAIRSHARING) there may have no '
                      'direct pathogen related but simply a taxonomic information .... '
                      'the default value should be the root of virology: Viruses'],
         'domain_of': ['ProductOrService']} })
    doi: Optional[list[Doi]] = Field(default=None, title="DOI", description="""A Digital Object Identifier (DOI) that can be related""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'broad_mappings': ['dct:bibliographicCitation'],
         'close_mappings': ['wdp:P356', 'reproduceme:doi'],
         'domain_of': ['ProductOrService', 'Publication'],
         'exact_mappings': ['wdp:P356']} })
    riskGroup: Optional[RiskGroup] = Field(default=None, title="risk group", description="""The highest risk group related to this resource. The risk group of a biological agent guiding its initial handling in labs according to the risk group classification defined by the WHO laboratory biosafety manual""", json_schema_extra = { "linkml_meta": {'alias': 'riskGroup',
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['wdp:P12663'],
         'recommended': True,
         'related_mappings': ['bao:0002826']} })
    biosafetyRestrictions: Optional[str] = Field(default=None, title="biosafety restrictions", description="""Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service""", json_schema_extra = { "linkml_meta": {'alias': 'biosafetyRestrictions',
         'domain_of': ['ProductOrService'],
         'related_mappings': ['bao:0002826']} })
    canBeUsedToProduceGmo: bool = Field(default=..., title="can be used to produce GMO", description="""Indicates if the current service or product can be used to produce GMO""", json_schema_extra = { "linkml_meta": {'alias': 'canBeUsedToProduceGmo',
         'broad_mappings': ['schema:potentialUse'],
         'comments': ['Set to TRUE if it can produce GMO. It is recommended to have a '
                      'value for this field, no value will be understood as unknown'],
         'domain_of': ['ProductOrService'],
         'recommended': True} })
    provider: Provider = Field(default=..., title="provider", description="""A provider of this product or service, as a specific organization""", json_schema_extra = { "linkml_meta": {'alias': 'provider',
         'close_mappings': ['schema:provider', 'dct:publisher'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['sio:000066']} })
    collection: list[Collection] = Field(default=..., title="collection", description="""The collection(s) to which belongs this item""", json_schema_extra = { "linkml_meta": {'alias': 'collection',
         'broad_mappings': ['dct:isPartOf'],
         'domain_of': ['ProductOrService'],
         'related_mappings': ['afop:AFX_0002720']} })
    keywords: list[Keyword] = Field(default=..., title="keywords", description="""List of terms used to tag and categorize this Item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'close_mappings': ['dcat:keyword'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:keywords'],
         'recommended': True} })
    availability: str = Field(default="on request", title="availability", description="""The state or condition in which this item is accessible and ready for use or can be obtained""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'close_mappings': ['schema:availability', 'dct:available'],
         'comments': ['Possible availabilities may differ from a project to another'],
         'domain_of': ['ProductOrService'],
         'ifabsent': 'string(on request)'} })
    complementaryDocument: Optional[list[Document]] = Field(default=None, title="complementary document", description="""Any additional documents that provide supplementary information, instructions, or guidelines relevant to the use of this item""", json_schema_extra = { "linkml_meta": {'alias': 'complementaryDocument',
         'close_mappings': ['sepio:0000442'],
         'domain_of': ['ProductOrService']} })
    technicalRecommendation: Optional[str] = Field(default=None, title="technical recommendation", description="""Expert advice or guidelines provided to ensure the optimal use, performance, and maintenance of what is provided, including best practices, troubleshooting tips, and procedural instructions""", json_schema_extra = { "linkml_meta": {'alias': 'technicalRecommendation', 'domain_of': ['ProductOrService']} })
    productPicture: Optional[list[Image]] = Field(default=None, title="product picture", description="""A picture that can represent the item""", json_schema_extra = { "linkml_meta": {'alias': 'productPicture', 'domain_of': ['ProductOrService']} })
    externalRelatedReference: Optional[list[ExternalRelatedReference]] = Field(default=None, title="external related reference", description="""A reference that permits to retrieve another related item from an external provider""", json_schema_extra = { "linkml_meta": {'alias': 'externalRelatedReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    certification: Optional[list[Certification]] = Field(default=None, title="certification", description="""Any certification related to the current product or service; e.g., ISO certification""", json_schema_extra = { "linkml_meta": {'alias': 'certification',
         'close_mappings': ['dct:conformsTo'],
         'domain_of': ['ProductOrService'],
         'exact_mappings': ['schema:hasCertification']} })
    internalReference: Optional[str] = Field(default=None, title="internal reference", description="""Any reference or indication to be used for local retrieval purpose""", json_schema_extra = { "linkml_meta": {'alias': 'internalReference',
         'broad_mappings': ['dct:references'],
         'domain_of': ['ProductOrService']} })
    note: Optional[str] = Field(default=None, title="note", description="""An aditional information as a textual comment""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['ProductOrService'], 'slot_uri': 'skos:note'} })
    contactPoint: Optional[ContactPoint] = Field(default=None, title="contact point", description="""An information that allows someone to establish communication""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['ProductOrService', 'PersonOrOrganization'],
         'exact_mappings': ['schema:contactPoint'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, title="version", description="""The version indicator (name or identifier) of a resource""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'close_mappings': ['wdp:P393', 'schema:version'],
         'domain_of': ['Dataset', 'Version', 'Taxonomy'],
         'exact_mappings': ['pav:version'],
         'recommended': True,
         'related_mappings': ['schema:identifier'],
         'slot_uri': 'dcat:version'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class MaterialSafetyDataSheet(Resource):
    """
    A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q222067', 'wd:Q222067'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'accidentalReleaseMeasures': {'description': 'Guidelines for '
                                                                     'safely managing '
                                                                     'spills or leaks '
                                                                     'of the product, '
                                                                     'including '
                                                                     'containment, '
                                                                     'cleanup '
                                                                     'procedures, and '
                                                                     'precautions to '
                                                                     'prevent harm to '
                                                                     'people, '
                                                                     'property, and '
                                                                     'the environment.',
                                                      'domain_of': ['MaterialSafetyDataSheet'],
                                                      'multivalued': False,
                                                      'name': 'accidentalReleaseMeasures',
                                                      'range': 'string',
                                                      'recommended': True,
                                                      'related_mappings': ['schema:Recommendation'],
                                                      'required': False,
                                                      'title': 'accidental release '
                                                               'measures'},
                        'disposalConsiderations': {'description': 'Guidance on the '
                                                                  'safe and '
                                                                  'environmentally '
                                                                  'responsible '
                                                                  'disposal of the '
                                                                  'product, including '
                                                                  'recommended '
                                                                  'disposal methods, '
                                                                  'regulatory '
                                                                  'requirements, and '
                                                                  'precautions to '
                                                                  'avoid harm to '
                                                                  'people and the '
                                                                  'environment during '
                                                                  'disposal.',
                                                   'domain_of': ['MaterialSafetyDataSheet'],
                                                   'multivalued': False,
                                                   'name': 'disposalConsiderations',
                                                   'range': 'string',
                                                   'recommended': True,
                                                   'required': False,
                                                   'title': 'disposal considerations'},
                        'ecologicalInformation': {'description': 'Details the '
                                                                 'potential '
                                                                 'environmental impact '
                                                                 'of the product, '
                                                                 'including its '
                                                                 'effects on '
                                                                 'ecosystems, '
                                                                 'persistence, '
                                                                 'degradability, '
                                                                 'bioaccumulation '
                                                                 'potential, and '
                                                                 'toxicity to aquatic '
                                                                 'and terrestrial '
                                                                 'organisms.',
                                                  'domain_of': ['MaterialSafetyDataSheet'],
                                                  'multivalued': False,
                                                  'name': 'ecologicalInformation',
                                                  'range': 'string',
                                                  'recommended': True,
                                                  'required': False,
                                                  'title': 'ecological information'},
                        'exposureControlsPersonalProtection': {'description': 'Specifies '
                                                                              'measures '
                                                                              'to '
                                                                              'limit '
                                                                              'exposure '
                                                                              'to the '
                                                                              'product, '
                                                                              'including '
                                                                              'recommended '
                                                                              'engineering '
                                                                              'controls '
                                                                              '(e.g., '
                                                                              'ventilation) '
                                                                              'and '
                                                                              'personal '
                                                                              'protective '
                                                                              'equipment '
                                                                              '(PPE) '
                                                                              'such as '
                                                                              'gloves, '
                                                                              'masks, '
                                                                              'goggles, '
                                                                              'and '
                                                                              'clothing '
                                                                              'to '
                                                                              'ensure '
                                                                              'safe '
                                                                              'handling.',
                                                               'domain_of': ['MaterialSafetyDataSheet'],
                                                               'multivalued': False,
                                                               'name': 'exposureControlsPersonalProtection',
                                                               'range': 'string',
                                                               'recommended': True,
                                                               'required': False,
                                                               'title': 'exposure '
                                                                        'controls/personal '
                                                                        'protection'},
                        'fireFightingMeasures': {'description': 'Guidance on how to '
                                                                'safely extinguish a '
                                                                'fire involving the '
                                                                'product, including '
                                                                'suitable '
                                                                'extinguishing agents, '
                                                                'special protective '
                                                                'equipment for '
                                                                'firefighters, and any '
                                                                'specific hazards from '
                                                                'combustion.',
                                                 'domain_of': ['MaterialSafetyDataSheet'],
                                                 'multivalued': False,
                                                 'name': 'fireFightingMeasures',
                                                 'range': 'string',
                                                 'recommended': True,
                                                 'related_mappings': ['schema:Recommendation'],
                                                 'required': False,
                                                 'title': 'fire fighting measures'},
                        'firstAidMeasures': {'description': 'Instructions on immediate '
                                                            'actions to take in case '
                                                            'of exposure to the '
                                                            'product, including '
                                                            'inhalation, ingestion, '
                                                            'skin, or eye contact. '
                                                            'This section outlines '
                                                            'steps to minimize harm '
                                                            'before medical help is '
                                                            'available.',
                                             'domain_of': ['MaterialSafetyDataSheet'],
                                             'multivalued': False,
                                             'name': 'firstAidMeasures',
                                             'range': 'string',
                                             'recommended': True,
                                             'related_mappings': ['schema:Recommendation'],
                                             'required': False,
                                             'title': 'first aid measures'},
                        'furtherInformation': {'description': 'Provides any additional '
                                                              'details or '
                                                              'clarifications not '
                                                              'covered in other '
                                                              'sections of the MSDS, '
                                                              'such as references, '
                                                              'supporting documents, '
                                                              'or specific '
                                                              'instructions for safe '
                                                              'handling and use of the '
                                                              'product.',
                                               'domain_of': ['MaterialSafetyDataSheet'],
                                               'multivalued': False,
                                               'name': 'furtherInformation',
                                               'range': 'string',
                                               'recommended': True,
                                               'required': False,
                                               'title': 'further information'},
                        'handlingAndStorage': {'description': 'Instructions on the '
                                                              'safe handling practices '
                                                              'and storage conditions '
                                                              'for the product, '
                                                              'including precautions '
                                                              'to prevent accidents, '
                                                              'degradation, or '
                                                              'contamination, as well '
                                                              'as recommended '
                                                              'temperature, humidity, '
                                                              'and container '
                                                              'requirements.',
                                               'domain_of': ['MaterialSafetyDataSheet'],
                                               'multivalued': False,
                                               'name': 'handlingAndStorage',
                                               'range': 'string',
                                               'recommended': True,
                                               'required': False,
                                               'title': 'handling and storage'},
                        'hazardsIdentification': {'description': 'Outlines the '
                                                                 'potential risks and '
                                                                 'dangers associated '
                                                                 'with handling the '
                                                                 'product, including '
                                                                 'its physical, '
                                                                 'chemical, and health '
                                                                 'hazards. This '
                                                                 'section provides '
                                                                 'information on '
                                                                 'toxicity, '
                                                                 'flammability, '
                                                                 'reactivity, and '
                                                                 'other relevant risks '
                                                                 'for safe use.',
                                                  'domain_of': ['MaterialSafetyDataSheet'],
                                                  'multivalued': False,
                                                  'name': 'hazardsIdentification',
                                                  'range': 'string',
                                                  'recommended': True,
                                                  'required': False,
                                                  'title': 'hazards identification'},
                        'materialSafetyContact': {'broad_mappings': ['schema:contactPoint'],
                                                  'description': 'The designated '
                                                                 'contact point '
                                                                 'responsible for '
                                                                 'providing '
                                                                 'information related '
                                                                 'to the safety, '
                                                                 'handling, and '
                                                                 'regulatory '
                                                                 'compliance of the '
                                                                 'biological product.',
                                                  'domain_of': ['MaterialSafetyDataSheet'],
                                                  'is_a': 'contactPoint',
                                                  'multivalued': False,
                                                  'name': 'materialSafetyContact',
                                                  'range': 'ContactPoint',
                                                  'required': True,
                                                  'title': 'material safety contact'},
                        'physicalChemicalProperties': {'description': 'Key '
                                                                      'characteristics '
                                                                      'of the product, '
                                                                      'such as '
                                                                      'physical state, '
                                                                      'appearance, '
                                                                      'solubility, pH, '
                                                                      'chemical '
                                                                      'composition, '
                                                                      'and molecular '
                                                                      'weight, '
                                                                      'essential for '
                                                                      'safe handling '
                                                                      'and storage',
                                                       'domain_of': ['MaterialSafetyDataSheet'],
                                                       'multivalued': False,
                                                       'name': 'physicalChemicalProperties',
                                                       'range': 'string',
                                                       'recommended': True,
                                                       'required': False,
                                                       'title': 'physical and chemical '
                                                                'properties and '
                                                                'information on '
                                                                'ingredients'},
                        'regulatoryInformation': {'description': 'Lists applicable '
                                                                 'laws, regulations, '
                                                                 'and standards '
                                                                 'governing the '
                                                                 'product, including '
                                                                 'local, national, or '
                                                                 'international '
                                                                 'requirements for its '
                                                                 'handling, use, '
                                                                 'transportation, and '
                                                                 'disposal, ensuring '
                                                                 'compliance with '
                                                                 'legal obligations.',
                                                  'domain_of': ['MaterialSafetyDataSheet'],
                                                  'multivalued': False,
                                                  'name': 'regulatoryInformation',
                                                  'range': 'string',
                                                  'recommended': True,
                                                  'related_mappings': ['rdfs:seeAlso'],
                                                  'required': False,
                                                  'title': 'regulatory information'},
                        'stabilityAndReactivity': {'description': 'Describes the '
                                                                  'product’s stability '
                                                                  'under normal '
                                                                  'conditions and its '
                                                                  'potential to react '
                                                                  'with other '
                                                                  'substances. This '
                                                                  'section includes '
                                                                  'information on '
                                                                  'hazardous '
                                                                  'reactions, '
                                                                  'conditions to '
                                                                  'avoid, and '
                                                                  'incompatible '
                                                                  'materials that '
                                                                  'could cause '
                                                                  'degradation or '
                                                                  'dangerous '
                                                                  'reactions.',
                                                   'domain_of': ['MaterialSafetyDataSheet'],
                                                   'multivalued': False,
                                                   'name': 'stabilityAndReactivity',
                                                   'range': 'string',
                                                   'recommended': True,
                                                   'required': False,
                                                   'title': 'stability and reactivity'},
                        'toxicologicalInformation': {'description': 'Details on the '
                                                                    'potential health '
                                                                    'effects of the '
                                                                    'product, '
                                                                    'including routes '
                                                                    'of exposure '
                                                                    '(inhalation, '
                                                                    'ingestion, skin, '
                                                                    'eye contact), '
                                                                    'acute and chronic '
                                                                    'toxicity and '
                                                                    'symptoms of '
                                                                    'exposure',
                                                     'domain_of': ['MaterialSafetyDataSheet'],
                                                     'multivalued': False,
                                                     'name': 'toxicologicalInformation',
                                                     'range': 'string',
                                                     'recommended': True,
                                                     'required': False,
                                                     'title': 'toxicological '
                                                              'information'},
                        'transportInformation': {'description': 'Details the '
                                                                'regulations and '
                                                                'guidelines for safely '
                                                                'transporting the '
                                                                'product, including '
                                                                'classifications for '
                                                                'road, air, sea, or '
                                                                'rail transport, UN '
                                                                'numbers, packaging '
                                                                'requirements, and any '
                                                                'special precautions '
                                                                'to ensure safe '
                                                                'transit.',
                                                 'domain_of': ['MaterialSafetyDataSheet'],
                                                 'multivalued': False,
                                                 'name': 'transportInformation',
                                                 'range': 'string',
                                                 'recommended': True,
                                                 'required': False,
                                                 'title': 'transport information'}},
         'title': 'Material safety data sheet'})

    materialSafetyContact: ContactPoint = Field(default=..., title="material safety contact", description="""The designated contact point responsible for providing information related to the safety, handling, and regulatory compliance of the biological product.""", json_schema_extra = { "linkml_meta": {'alias': 'materialSafetyContact',
         'broad_mappings': ['schema:contactPoint'],
         'domain_of': ['MaterialSafetyDataSheet'],
         'is_a': 'contactPoint',
         'recommended': True} })
    physicalChemicalProperties: Optional[str] = Field(default=None, title="physical and chemical properties and information on ingredients", description="""Key characteristics of the product, such as physical state, appearance, solubility, pH, chemical composition, and molecular weight, essential for safe handling and storage""", json_schema_extra = { "linkml_meta": {'alias': 'physicalChemicalProperties',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    hazardsIdentification: Optional[str] = Field(default=None, title="hazards identification", description="""Outlines the potential risks and dangers associated with handling the product, including its physical, chemical, and health hazards. This section provides information on toxicity, flammability, reactivity, and other relevant risks for safe use.""", json_schema_extra = { "linkml_meta": {'alias': 'hazardsIdentification',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    firstAidMeasures: Optional[str] = Field(default=None, title="first aid measures", description="""Instructions on immediate actions to take in case of exposure to the product, including inhalation, ingestion, skin, or eye contact. This section outlines steps to minimize harm before medical help is available.""", json_schema_extra = { "linkml_meta": {'alias': 'firstAidMeasures',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True,
         'related_mappings': ['schema:Recommendation']} })
    fireFightingMeasures: Optional[str] = Field(default=None, title="fire fighting measures", description="""Guidance on how to safely extinguish a fire involving the product, including suitable extinguishing agents, special protective equipment for firefighters, and any specific hazards from combustion.""", json_schema_extra = { "linkml_meta": {'alias': 'fireFightingMeasures',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True,
         'related_mappings': ['schema:Recommendation']} })
    accidentalReleaseMeasures: Optional[str] = Field(default=None, title="accidental release measures", description="""Guidelines for safely managing spills or leaks of the product, including containment, cleanup procedures, and precautions to prevent harm to people, property, and the environment.""", json_schema_extra = { "linkml_meta": {'alias': 'accidentalReleaseMeasures',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True,
         'related_mappings': ['schema:Recommendation']} })
    handlingAndStorage: Optional[str] = Field(default=None, title="handling and storage", description="""Instructions on the safe handling practices and storage conditions for the product, including precautions to prevent accidents, degradation, or contamination, as well as recommended temperature, humidity, and container requirements.""", json_schema_extra = { "linkml_meta": {'alias': 'handlingAndStorage',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    exposureControlsPersonalProtection: Optional[str] = Field(default=None, title="exposure controls/personal protection", description="""Specifies measures to limit exposure to the product, including recommended engineering controls (e.g., ventilation) and personal protective equipment (PPE) such as gloves, masks, goggles, and clothing to ensure safe handling.""", json_schema_extra = { "linkml_meta": {'alias': 'exposureControlsPersonalProtection',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    stabilityAndReactivity: Optional[str] = Field(default=None, title="stability and reactivity", description="""Describes the product’s stability under normal conditions and its potential to react with other substances. This section includes information on hazardous reactions, conditions to avoid, and incompatible materials that could cause degradation or dangerous reactions.""", json_schema_extra = { "linkml_meta": {'alias': 'stabilityAndReactivity',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    toxicologicalInformation: Optional[str] = Field(default=None, title="toxicological information", description="""Details on the potential health effects of the product, including routes of exposure (inhalation, ingestion, skin, eye contact), acute and chronic toxicity and symptoms of exposure""", json_schema_extra = { "linkml_meta": {'alias': 'toxicologicalInformation',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    ecologicalInformation: Optional[str] = Field(default=None, title="ecological information", description="""Details the potential environmental impact of the product, including its effects on ecosystems, persistence, degradability, bioaccumulation potential, and toxicity to aquatic and terrestrial organisms.""", json_schema_extra = { "linkml_meta": {'alias': 'ecologicalInformation',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    disposalConsiderations: Optional[str] = Field(default=None, title="disposal considerations", description="""Guidance on the safe and environmentally responsible disposal of the product, including recommended disposal methods, regulatory requirements, and precautions to avoid harm to people and the environment during disposal.""", json_schema_extra = { "linkml_meta": {'alias': 'disposalConsiderations',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    transportInformation: Optional[str] = Field(default=None, title="transport information", description="""Details the regulations and guidelines for safely transporting the product, including classifications for road, air, sea, or rail transport, UN numbers, packaging requirements, and any special precautions to ensure safe transit.""", json_schema_extra = { "linkml_meta": {'alias': 'transportInformation',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    regulatoryInformation: Optional[str] = Field(default=None, title="regulatory information", description="""Lists applicable laws, regulations, and standards governing the product, including local, national, or international requirements for its handling, use, transportation, and disposal, ensuring compliance with legal obligations.""", json_schema_extra = { "linkml_meta": {'alias': 'regulatoryInformation',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True,
         'related_mappings': ['rdfs:seeAlso']} })
    furtherInformation: Optional[str] = Field(default=None, title="further information", description="""Provides any additional details or clarifications not covered in other sections of the MSDS, such as references, supporting documents, or specific instructions for safe handling and use of the product.""", json_schema_extra = { "linkml_meta": {'alias': 'furtherInformation',
         'domain_of': ['MaterialSafetyDataSheet'],
         'recommended': True} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class File(Resource):
    """
    Digital document or record stored in a specific format that contains data or information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q82753',
                            'dcat:mediaType',
                            'ncit:C42883',
                            'wd:Q82753',
                            'dcat:mediaType',
                            'ncit:C42883'],
         'exact_mappings': ['schema:MediaObject', 'schema:MediaObject'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'contentUrl': {'description': 'The web address or location '
                                                      'where the file content is '
                                                      'stored and can be accessed or '
                                                      'downloaded.',
                                       'domain_of': ['File'],
                                       'exact_mappings': ['schema:contentUrl'],
                                       'multivalued': False,
                                       'name': 'contentUrl',
                                       'range': 'uri',
                                       'required': True,
                                       'title': 'content URL'},
                        'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the resource'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['File',
                                                      'Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'ContactPoint',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'format': {'close_mappings': ['schema:encodingFormat'],
                                   'description': 'The file type or format that '
                                                  'indicates how the data within the '
                                                  'file is structured',
                                   'domain_of': ['File'],
                                   'exact_mappings': ['schema:fileFormat',
                                                      'dct:format'],
                                   'multivalued': False,
                                   'name': 'format',
                                   'range': 'string',
                                   'required': True,
                                   'title': 'format'},
                        'license': {'close_mappings': ['wdp:P275'],
                                    'description': 'Information about terms and '
                                                   'conditions under which the subject '
                                                   'can be used, shared, or '
                                                   'distributed, indicating any '
                                                   'restrictions or permissions',
                                    'domain_of': ['File', 'DataProvider'],
                                    'exact_mappings': ['dct:license', 'schema:license'],
                                    'multivalued': False,
                                    'name': 'license',
                                    'range': 'License',
                                    'required': False,
                                    'title': 'license'},
                        'name': {'close_mappings': ['rdfs:label', 'dct:title'],
                                 'description': 'A word or set of words used to '
                                                'identify and refer to an entity',
                                 'domain_of': ['File',
                                               'PersonOrOrganization',
                                               'ContactPoint'],
                                 'exact_mappings': ['schema:name', 'vcard:fn'],
                                 'multivalued': False,
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True,
                                 'slot_uri': 'foaf:name',
                                 'title': 'name'}},
         'title': 'File'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Data(File):
    """
    Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q42848',
                            'ncit:C25474',
                            't4fs:0000430',
                            'wd:Q42848',
                            'ncit:C25474',
                            't4fs:0000430'],
         'exact_mappings': ['schema:DataDownload', 'schema:DataDownload'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Data'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Document(File):
    """
    Subclass of File representing textual or written files such as reports, manuals, or forms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q49848',
                            'ncit:C19498',
                            'sio:000148',
                            'iao:0000310',
                            'wd:Q49848',
                            'ncit:C19498',
                            'sio:000148',
                            'iao:0000310'],
         'exact_mappings': ['schema:DigitalDocument', 'schema:DigitalDocument'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Document'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Audio(File):
    """
    Subclass of File representing sound recordings or audio tracks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q26987229',
                            'dcmi:Sound',
                            'ncit:C96977',
                            'wd:Q26987229',
                            'dcmi:Sound',
                            'ncit:C96977'],
         'exact_mappings': ['schema:AudioObject', 'schema:AudioObject'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Audio'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Video(File):
    """
    Subclass of File representing moving visual media, such as recordings, presentations, or movies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q98405806',
                            'ncit:C96985',
                            'wd:Q98405806',
                            'ncit:C96985'],
         'exact_mappings': ['schema:VideoObject', 'schema:VideoObject'],
         'from_schema': 'https://w3id.org/evorao/',
         'title': 'Video'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Image(File):
    """
    Subclass of File representing visual content such as pictures, diagrams, or illustrations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['dct:MediaType', 'dct:MediaType'],
         'close_mappings': ['wd:Q860625',
                            'dcmi:Image',
                            'edam:2968',
                            'reproduceme:Image',
                            'sio:000081',
                            'wd:Q860625',
                            'dcmi:Image',
                            'edam:2968',
                            'reproduceme:Image',
                            'sio:000081'],
         'exact_mappings': ['schema:ImageObject', 'schema:ImageObject'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'altText': {'description': 'An alternate text for the image, '
                                                   'if the image cannot be displayed',
                                    'domain_of': ['Image'],
                                    'exact_mappings': ['schema:caption'],
                                    'multivalued': False,
                                    'name': 'altText',
                                    'range': 'string',
                                    'recommended': True,
                                    'required': False,
                                    'title': 'alt text'}},
         'title': 'Image'})

    altText: Optional[str] = Field(default=None, title="alt text", description="""An alternate text for the image, if the image cannot be displayed""", json_schema_extra = { "linkml_meta": {'alias': 'altText',
         'domain_of': ['Image'],
         'exact_mappings': ['schema:caption'],
         'recommended': True} })
    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['File', 'PersonOrOrganization', 'ContactPoint'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource'],
         'domain_of': ['File',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'ContactPoint',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    contentUrl: str = Field(default=..., title="content URL", description="""The web address or location where the file content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'contentUrl',
         'domain_of': ['File'],
         'exact_mappings': ['schema:contentUrl']} })
    format: str = Field(default=..., title="format", description="""The file type or format that indicates how the data within the file is structured""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'close_mappings': ['schema:encodingFormat'],
         'domain_of': ['File'],
         'exact_mappings': ['schema:fileFormat', 'dct:format']} })
    license: Optional[License] = Field(default=None, title="license", description="""Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'close_mappings': ['wdp:P275'],
         'domain_of': ['File', 'DataProvider'],
         'exact_mappings': ['dct:license', 'schema:license'],
         'slot_uri': 'dct:license'} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class ContactPoint(Resource):
    """
    Entity serving as focal point of information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q30322502', 'wd:Q30322502'],
         'exact_mappings': ['schema:ContactPoint',
                            'vcard:Kind',
                            'schema:ContactPoint',
                            'vcard:Kind'],
         'from_schema': 'https://w3id.org/evorao/',
         'narrow_mappings': ['schema:PostalAddress', 'schema:PostalAddress'],
         'related_mappings': ['vcard:Contact', 'vcard:Contact'],
         'slot_usage': {'addressCountry': {'description': 'The country as of  ISO 3166',
                                           'domain_of': ['ContactPoint'],
                                           'exact_mappings': ['schema:addressCountry',
                                                              'vcard:hasCountryName'],
                                           'multivalued': False,
                                           'name': 'addressCountry',
                                           'range': 'Country',
                                           'required': False,
                                           'title': 'address Country'},
                        'addressLocality': {'close_mappings': ['vcard:hasLocality'],
                                            'description': 'The locality in which the '
                                                           'street address is, and '
                                                           'which is in the region. '
                                                           'e.g, the city',
                                            'domain_of': ['ContactPoint'],
                                            'exact_mappings': ['schema:addressLocality',
                                                               'vcard:locality'],
                                            'multivalued': False,
                                            'name': 'addressLocality',
                                            'range': 'string',
                                            'required': False,
                                            'title': 'locality/city'},
                        'addressRegion': {'close_mappings': ['vcard:hasRegion'],
                                          'description': 'The region in which the '
                                                         'locality is, and which is in '
                                                         'the country. For example, '
                                                         'California or another '
                                                         'appropriate first-level '
                                                         'Administrative division',
                                          'domain_of': ['ContactPoint'],
                                          'exact_mappings': ['schema:addressRegion',
                                                             'vcard:region'],
                                          'multivalued': False,
                                          'name': 'addressRegion',
                                          'range': 'string',
                                          'required': False,
                                          'title': 'region'},
                        'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['ContactPoint',
                                                      'Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'License',
                                                      'Certification'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'email': {'close_mappings': ['vcard:email'],
                                  'description': 'Email address',
                                  'domain_of': ['ContactPoint'],
                                  'exact_mappings': ['schema:email', 'foaf:mbox'],
                                  'multivalued': False,
                                  'name': 'email',
                                  'range': 'string',
                                  'recommended': True,
                                  'required': False,
                                  'title': 'email'},
                        'name': {'close_mappings': ['rdfs:label', 'dct:title'],
                                 'description': 'A word or set of words used to '
                                                'identify and refer to an entity',
                                 'domain_of': ['ContactPoint',
                                               'PersonOrOrganization',
                                               'File'],
                                 'exact_mappings': ['schema:name', 'vcard:fn'],
                                 'multivalued': False,
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True,
                                 'slot_uri': 'foaf:name',
                                 'title': 'name'},
                        'orcidId': {'description': 'Unique persistent identifier for a '
                                                   'person, provided by the Open '
                                                   'Researcher and Contributor ID '
                                                   '(ORCID) organisation',
                                    'domain_of': ['ContactPoint', 'Person'],
                                    'exact_mappings': ['wdp:P496', 'reproduceme:ORCID'],
                                    'multivalued': False,
                                    'name': 'orcidId',
                                    'range': 'string',
                                    'recommended': True,
                                    'related_mappings': ['iao:0000708', 'edam:4022'],
                                    'required': False,
                                    'title': 'ORCID id'},
                        'postalCode': {'close_mappings': ['vcard:hasPostalCode'],
                                       'description': 'The postal code',
                                       'domain_of': ['ContactPoint'],
                                       'exact_mappings': ['schema:postalCode',
                                                          'vcard:postal-code'],
                                       'multivalued': False,
                                       'name': 'postalCode',
                                       'range': 'string',
                                       'required': False,
                                       'title': 'postal code'},
                        'streetAddress': {'close_mappings': ['vcard:hasStreetAddress'],
                                          'description': 'The building/apartment '
                                                         'number and the street name',
                                          'domain_of': ['ContactPoint'],
                                          'exact_mappings': ['schema:streetAddress',
                                                             'vcard:street-address'],
                                          'multivalued': False,
                                          'name': 'streetAddress',
                                          'range': 'string',
                                          'required': False,
                                          'title': 'street address'},
                        'telephone': {'close_mappings': ['vcard:telephone'],
                                      'description': 'The telephone number',
                                      'domain_of': ['ContactPoint'],
                                      'exact_mappings': ['schema:telephone'],
                                      'multivalued': False,
                                      'name': 'telephone',
                                      'range': 'string',
                                      'recommended': True,
                                      'required': False,
                                      'title': 'telephone'}},
         'title': 'Contact Point'})

    name: str = Field(default=..., title="name", description="""A word or set of words used to identify and refer to an entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'close_mappings': ['rdfs:label', 'dct:title'],
         'domain_of': ['ContactPoint', 'PersonOrOrganization', 'File'],
         'exact_mappings': ['schema:name', 'vcard:fn'],
         'slot_uri': 'foaf:name'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['ContactPoint',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'License',
                       'Certification'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    email: Optional[str] = Field(default=None, title="email", description="""Email address""", json_schema_extra = { "linkml_meta": {'alias': 'email',
         'close_mappings': ['vcard:email'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:email', 'foaf:mbox'],
         'recommended': True} })
    telephone: Optional[str] = Field(default=None, title="telephone", description="""The telephone number""", json_schema_extra = { "linkml_meta": {'alias': 'telephone',
         'close_mappings': ['vcard:telephone'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:telephone'],
         'recommended': True} })
    streetAddress: Optional[str] = Field(default=None, title="street address", description="""The building/apartment number and the street name""", json_schema_extra = { "linkml_meta": {'alias': 'streetAddress',
         'close_mappings': ['vcard:hasStreetAddress'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:streetAddress', 'vcard:street-address']} })
    addressLocality: Optional[str] = Field(default=None, title="locality/city", description="""The locality in which the street address is, and which is in the region. e.g, the city""", json_schema_extra = { "linkml_meta": {'alias': 'addressLocality',
         'close_mappings': ['vcard:hasLocality'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:addressLocality', 'vcard:locality']} })
    addressRegion: Optional[str] = Field(default=None, title="region", description="""The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division""", json_schema_extra = { "linkml_meta": {'alias': 'addressRegion',
         'close_mappings': ['vcard:hasRegion'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:addressRegion', 'vcard:region']} })
    postalCode: Optional[str] = Field(default=None, title="postal code", description="""The postal code""", json_schema_extra = { "linkml_meta": {'alias': 'postalCode',
         'close_mappings': ['vcard:hasPostalCode'],
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:postalCode', 'vcard:postal-code']} })
    addressCountry: Optional[Country] = Field(default=None, title="address Country", description="""The country as of  ISO 3166""", json_schema_extra = { "linkml_meta": {'alias': 'addressCountry',
         'domain_of': ['ContactPoint'],
         'exact_mappings': ['schema:addressCountry', 'vcard:hasCountryName']} })
    orcidId: Optional[str] = Field(default=None, title="ORCID id", description="""Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation""", json_schema_extra = { "linkml_meta": {'alias': 'orcidId',
         'domain_of': ['ContactPoint', 'Person'],
         'exact_mappings': ['wdp:P496', 'reproduceme:ORCID'],
         'recommended': True,
         'related_mappings': ['iao:0000708', 'edam:4022']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class License(Resource):
    """
    The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q79719',
                            'dct:LicenseDocument',
                            'reproduceme:LicenseDocument',
                            'wd:Q79719',
                            'dct:LicenseDocument',
                            'reproduceme:LicenseDocument'],
         'exact_mappings': ['dct:RightsStatement', 'dct:RightsStatement'],
         'from_schema': 'https://w3id.org/evorao/',
         'slot_usage': {'description': {'close_mappings': ['schema:description'],
                                        'comments': ['The title of the item should be '
                                                     'as short and descriptive as '
                                                     'possible. E.g. for virus '
                                                     'products it should basically be '
                                                     'based on the following Pattern: '
                                                     "'Virus name', 'virus host type', "
                                                     "'collection year', 'country of "
                                                     "collection' ex 'suspected "
                                                     "epidemiological origin', "
                                                     "'genotype', 'strain', 'variant "
                                                     'name or specific feature'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['License',
                                                      'Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'ContactPoint',
                                                      'Certification'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'licensingOrAttribution': {'close_mappings': ['schema:license'],
                                                   'description': 'A text or html code '
                                                                  'that provides any '
                                                                  'related data '
                                                                  'sharing licence '
                                                                  'and/or attribution',
                                                   'domain_of': ['License'],
                                                   'exact_mappings': ['dct:rights'],
                                                   'multivalued': False,
                                                   'name': 'licensingOrAttribution',
                                                   'range': 'string',
                                                   'required': False,
                                                   'title': 'licensing or attribution'},
                        'logo': {'description': 'A path or URL to the related logo',
                                 'domain_of': ['License',
                                               'PersonOrOrganization',
                                               'Certification'],
                                 'multivalued': False,
                                 'name': 'logo',
                                 'range': 'Image',
                                 'required': False,
                                 'title': 'logo'},
                        'resourceUrl': {'broad_mappings': ['schema:url'],
                                        'description': 'The web address or location '
                                                       'where the details or content '
                                                       'is stored and can be accessed '
                                                       'or downloaded.',
                                        'domain_of': ['License', 'Certification'],
                                        'exact_mappings': ['dct:license'],
                                        'multivalued': False,
                                        'name': 'resourceUrl',
                                        'range': 'uri',
                                        'required': False,
                                        'title': 'resource URL'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['License',
                                                'Dataset',
                                                'DataService',
                                                'Publication',
                                                'Term',
                                                'Certification'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'}},
         'title': 'License'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['License',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'Certification'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['License',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'Certification'],
         'exact_mappings': ['schema:description',
                            'schema:description',
                            'schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    resourceUrl: Optional[str] = Field(default=None, title="resource URL", description="""The web address or location where the details or content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'resourceUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['License', 'Certification'],
         'exact_mappings': ['dct:license']} })
    licensingOrAttribution: Optional[str] = Field(default=None, title="licensing or attribution", description="""A text or html code that provides any related data sharing licence and/or attribution""", json_schema_extra = { "linkml_meta": {'alias': 'licensingOrAttribution',
         'close_mappings': ['schema:license'],
         'domain_of': ['License'],
         'exact_mappings': ['dct:rights']} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['License', 'PersonOrOrganization', 'Certification'],
         'exact_mappings': ['schema:logo']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


class Certification(Resource):
    """
    Assurance given by an independent certification body that a product, service or system meets the requirements of a standard
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wd:Q374814', 'wd:Q374814'],
         'exact_mappings': ['schema:Certification', 'schema:Certification'],
         'from_schema': 'https://w3id.org/evorao/',
         'related_mappings': ['ncit:C43610', 'ncit:C43610'],
         'slot_usage': {'certificationDocument': {'description': 'The document(s) '
                                                                 'issued by an '
                                                                 'authority certifying '
                                                                 'the conformity of '
                                                                 'the subject to the '
                                                                 'applicable scheme, '
                                                                 'including, as the '
                                                                 'case may be, the '
                                                                 'documents attesting '
                                                                 'the equivalence to '
                                                                 'another '
                                                                 'certification '
                                                                 'scheme.',
                                                  'domain_of': ['Certification'],
                                                  'exact_mappings': ['schema:associatedMedia'],
                                                  'multivalued': True,
                                                  'name': 'certificationDocument',
                                                  'range': 'Document',
                                                  'required': False,
                                                  'title': 'certification document'},
                        'description': {'comments': ['Describe this item in few lines. '
                                                     'This description will serve as a '
                                                     'summary to present the '
                                                     'resource.'],
                                        'description': 'A short explanation of the '
                                                       'characteristics, features, or '
                                                       'nature of the current item',
                                        'domain_of': ['Certification',
                                                      'Dataset',
                                                      'DataService',
                                                      'Term',
                                                      'PersonOrOrganization',
                                                      'File',
                                                      'ContactPoint',
                                                      'License'],
                                        'exact_mappings': ['schema:description'],
                                        'multivalued': False,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dct:description',
                                        'title': 'description'},
                        'logo': {'description': 'A path or URL to the related logo',
                                 'domain_of': ['Certification',
                                               'PersonOrOrganization',
                                               'License'],
                                 'exact_mappings': ['schema:logo'],
                                 'multivalued': False,
                                 'name': 'logo',
                                 'range': 'Image',
                                 'required': False,
                                 'title': 'logo'},
                        'resourceUrl': {'broad_mappings': ['schema:url'],
                                        'description': 'The web address or location '
                                                       'where the details or content '
                                                       'is stored and can be accessed '
                                                       'or downloaded.',
                                        'domain_of': ['Certification', 'License'],
                                        'exact_mappings': ['schema:archivedAt'],
                                        'multivalued': False,
                                        'name': 'resourceUrl',
                                        'range': 'uri',
                                        'required': False,
                                        'title': 'resource URL'},
                        'title': {'comments': ['The title of the item should be as '
                                               'short and descriptive as possible. '
                                               'E.g. for virus products it should '
                                               'basically be based on the following '
                                               "Pattern: 'Virus name', 'virus host "
                                               "type', 'collection year', 'country of "
                                               "collection' ex 'suspected "
                                               "epidemiological origin', 'genotype', "
                                               "'strain', 'variant name or specific "
                                               'feature'],
                                  'description': 'A name given to the resource',
                                  'domain_of': ['Certification',
                                                'Dataset',
                                                'DataService',
                                                'Publication',
                                                'Term',
                                                'License'],
                                  'exact_mappings': ['schema:name', 'rdfs:label'],
                                  'multivalued': False,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dct:title',
                                  'title': 'title'}},
         'title': 'Certification'})

    title: str = Field(default=..., title="title", description="""A name given to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'comments': ['The title of the item should be as short and descriptive as '
                      'possible. E.g. for virus products it should basically be based '
                      "on the following Pattern: 'Virus name', 'virus host type', "
                      "'collection year', 'country of collection' ex 'suspected "
                      "epidemiological origin', 'genotype', 'strain', 'variant name or "
                      'specific feature'],
         'domain_of': ['Certification',
                       'Dataset',
                       'DataService',
                       'Publication',
                       'Term',
                       'License'],
         'exact_mappings': ['schema:name', 'rdfs:label'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, title="description", description="""A short explanation of the characteristics, features, or nature of the current item""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'close_mappings': ['schema:description'],
         'comments': ['Describe this item in few lines. This description will serve as '
                      'a summary to present the resource.'],
         'domain_of': ['Certification',
                       'Dataset',
                       'DataService',
                       'Term',
                       'PersonOrOrganization',
                       'File',
                       'ContactPoint',
                       'License'],
         'exact_mappings': ['schema:description'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    logo: Optional[Image] = Field(default=None, title="logo", description="""A path or URL to the related logo""", json_schema_extra = { "linkml_meta": {'alias': 'logo',
         'domain_of': ['Certification', 'PersonOrOrganization', 'License'],
         'exact_mappings': ['schema:logo']} })
    certificationDocument: Optional[list[Document]] = Field(default=None, title="certification document", description="""The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.""", json_schema_extra = { "linkml_meta": {'alias': 'certificationDocument',
         'domain_of': ['Certification'],
         'exact_mappings': ['schema:associatedMedia']} })
    resourceUrl: Optional[str] = Field(default=None, title="resource URL", description="""The web address or location where the details or content is stored and can be accessed or downloaded.""", json_schema_extra = { "linkml_meta": {'alias': 'resourceUrl',
         'broad_mappings': ['schema:url'],
         'domain_of': ['Certification', 'License'],
         'exact_mappings': ['schema:archivedAt']} })
    keyword: Optional[list[str]] = Field(default=None, title="keyword", description="""A keyword or tag describing the resource""", json_schema_extra = { "linkml_meta": {'alias': 'keyword', 'domain_of': ['Resource'], 'slot_uri': 'dcat:keyword'} })
    dateIssued: Optional[datetime ] = Field(default=None, title="date issued", description="""Date of formal issuance (e.g., publication) of the resource""", json_schema_extra = { "linkml_meta": {'alias': 'dateIssued',
         'close_mappings': ['schema:datePublished', 'schema:dateCreated'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000051'],
         'slot_uri': 'dct:issued'} })
    dateModified: Optional[datetime ] = Field(default=None, title="date modified", description="""Most recent date on which the resource was changed, updated or modified""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'close_mappings': ['schema:dateModified'],
         'comments': ['encoded using the relevant ISO 8601 Date and Time compliant '
                      'string [DATETIME]'],
         'domain_of': ['Resource'],
         'exact_mappings': ['sepio:0000036'],
         'slot_uri': 'dct:modified'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Resource.model_rebuild()
Dataset.model_rebuild()
DataService.model_rebuild()
Version.model_rebuild()
Catalogue.model_rebuild()
Taxonomy.model_rebuild()
DataProvider.model_rebuild()
PathogenIdentification.model_rebuild()
Publication.model_rebuild()
Vocabulary.model_rebuild()
Term.model_rebuild()
CommonName.model_rebuild()
VirusName.model_rebuild()
AlternateName.model_rebuild()
RiskGroup.model_rebuild()
Doi.model_rebuild()
Journal.model_rebuild()
PdbReference.model_rebuild()
Keyword.model_rebuild()
TagSequence.model_rebuild()
SpecialFeature.model_rebuild()
ExpressionVector.model_rebuild()
PlasmidSelection.model_rebuild()
PropagationHost.model_rebuild()
TransmissionMethod.model_rebuild()
ProductionCellLine.model_rebuild()
ProductCategory.model_rebuild()
IsolationHost.model_rebuild()
GeographicalOrigin.model_rebuild()
IplcOrigin.model_rebuild()
Country.model_rebuild()
IataClassification.model_rebuild()
Variant.model_rebuild()
TaxonomicRank.model_rebuild()
Taxon.model_rebuild()
ClinicalGroup.model_rebuild()
ExternalRelatedReference.model_rebuild()
Sequence.model_rebuild()
SequenceReference.model_rebuild()
PersonOrOrganization.model_rebuild()
Person.model_rebuild()
Organization.model_rebuild()
ReasearchInfrastructure.model_rebuild()
Provider.model_rebuild()
Originator.model_rebuild()
BiologicalMaterialOrigin.model_rebuild()
BiologicalPartOrigin.model_rebuild()
NaturalPartOrigin.model_rebuild()
SyntheticPartOrigin.model_rebuild()
RecombinantPartIdentification.model_rebuild()
Collection.model_rebuild()
ProductOrService.model_rebuild()
Service.model_rebuild()
Product.model_rebuild()
Antibody.model_rebuild()
Hybridoma.model_rebuild()
Protein.model_rebuild()
NucleicAcid.model_rebuild()
DetectionKit.model_rebuild()
Bundle.model_rebuild()
Pathogen.model_rebuild()
Virus.model_rebuild()
Bacterium.model_rebuild()
Fungus.model_rebuild()
Protozoan.model_rebuild()
Viroid.model_rebuild()
Prion.model_rebuild()
MaterialSafetyDataSheet.model_rebuild()
File.model_rebuild()
Data.model_rebuild()
Document.model_rebuild()
Audio.model_rebuild()
Video.model_rebuild()
Image.model_rebuild()
ContactPoint.model_rebuild()
License.model_rebuild()
Certification.model_rebuild()

