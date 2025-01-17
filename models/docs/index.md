# European Viral Outbreak Response Alliance Ontology

The EVORA Ontology harmonizes metadata in virology to describe viral resources, their derived products, and services. It aligns with FAIR principles to ensure interoperability, accessibility, and reusability across various projects. The EVORA Ontology aims to support preparedness and response to pandemics.

URI: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#

Name: EVORAO



## Classes

| Class | Description |
| --- | --- |
| [Dataset](Dataset.md) | A collection of data, published or curated by a single agent, and available for access |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md) | Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalPartOrigin](BiologicalPartOrigin.md) | Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaturalPartOrigin](NaturalPartOrigin.md) | Information on the origin of a natural part that composes the biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SyntheticPartOrigin](SyntheticPartOrigin.md) | Information on the origin of a synthetic part that composes the biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExternalRelatedReference](ExternalRelatedReference.md) | A reference that permits to retrieve an item from an external provider |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MSDS](MSDS.md) | A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation of a pathogen from another |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.md) | A scientific publication |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sequence](Sequence.md) | A nucleic acid or protein sequence information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceReference](SequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence provider |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Version](Version.md) | Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards) |
| [Nameable](Nameable.md) | Any entity that has a name and can have a textual description |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Catalogue](Catalogue.md) | A curated collection of metadata about resources |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Collection](Collection.md) | Set of products and services with some common characteristics |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Taxonomy](Taxonomy.md) | Science of naming, defining and classifying organisms |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vocabulary](Vocabulary.md) | A subset of words or phrases specific to a particular subject or field |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Certification](Certification.md) | Assurance given by an independent certification body that a product, service or system meets the requirements of a standard |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContactPoint](ContactPoint.md) | Entity serving as focal point of information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataService](DataService.md) | A collection of operations that provides access to one or more datasets or data processing functions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataProvider](DataProvider.md) | An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[File](File.md) | Digital document or record stored in a specific format that contains data or information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Audio](Audio.md) | Subclass of File representing sound recordings or audio tracks |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Data](Data.md) | Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Document](Document.md) | Subclass of File representing textual or written files such as reports, manuals, or forms |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | Subclass of File representing visual content such as pictures, diagrams, or illustrations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Video](Video.md) | Subclass of File representing moving visual media, such as recordings, presentations, or movies |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[License](License.md) | The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NamedDataset](NamedDataset.md) | A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductOrService](ProductOrService.md) | A product or a service |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Product](Product.md) | A product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bundle](Bundle.md) | A group of products |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen. It can be extracted or synthetic |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bacterium](Bacterium.md) | The bacterium as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fungus](Fungus.md) | The fungus as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prion](Prion.md) | The prion as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protozoan](Protozoan.md) | The protozoan as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Viroid](Viroid.md) | The viroid as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virus](Virus.md) | The virus as a biological material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protein](Protein.md) | A protein as a derived product from a pathogen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Service](Service.md) | A service |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Term](Term.md) | Word or phrase from a specialized area of knowledge |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AlternateName](AlternateName.md) | List of alternate names for things |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CommonName](CommonName.md) | Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Variant](Variant.md) | An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirusName](VirusName.md) | A virus vernacular name or a name that describes a group of viruses |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Country](Country.md) | The country as of ISO3166 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DOI](DOI.md) | A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExpressionVector](ExpressionVector.md) | A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicalOrigin](GeographicalOrigin.md) | The specific location or region where a physical item, originates or is naturally found |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IPLCOrigin](IPLCOrigin.md) | The IPLC area (Indigenous People and Local Communities) from which a physical item originates |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IATAClassification](IATAClassification.md) | The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IsolationHost](IsolationHost.md) | Host organism from which the pathogen was isolated |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Journal](Journal.md) | Periodical journal publishing scientific research |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Keyword](Keyword.md) | A term or phrase used to tag and categorize content |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PDBReference](PDBReference.md) | Identifier for 3D structural data as per the PDB (Protein Data Bank) database |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlasmidSelection](PlasmidSelection.md) | The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductCategory](ProductCategory.md) | A term used to classify a group of products that share common characteristics or functions, which helps in their organization |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProductionCellLine](ProductionCellLine.md) | A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PropagationHost](PropagationHost.md) | The organism used to grow and multiply the pathogen under controlled conditions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinTag](ProteinTag.md) | Peptide sequence genetically grafted onto a recombinant protein |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RiskGroup](RiskGroup.md) | Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpecialFeature](SpecialFeature.md) | Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonomicRank](TaxonomicRank.md) | The possible taxonomic ranks and their description |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TransmissionMethod](TransmissionMethod.md) | The process by which the pathogen spreads between hosts |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Provider](Provider.md) | A provider of products or services, as a specific organization |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RI](RI.md) | A research infrastructure |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Originator](Originator.md) | The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | An individual |
| [RecombinantPartIdentification](RecombinantPartIdentification.md) | Identification of a recombinant part |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) |  |
| [accessionNumber](accessionNumber.md) |  |
| [accessPointURL](accessPointURL.md) |  |
| [accessToPhysicalGeneticResource](accessToPhysicalGeneticResource.md) |  |
| [accidentalReleaseMeasures](accidentalReleaseMeasures.md) |  |
| [additionalCategory](additionalCategory.md) |  |
| [addressCountry](addressCountry.md) |  |
| [addressLocality](addressLocality.md) |  |
| [addressRegion](addressRegion.md) |  |
| [alpha2Code](alpha2Code.md) |  |
| [alternateName](alternateName.md) |  |
| [altText](altText.md) |  |
| [antibodyPurifiedByAffinity](antibodyPurifiedByAffinity.md) |  |
| [authors](authors.md) |  |
| [availability](availability.md) |  |
| [beforeDate](beforeDate.md) |  |
| [biologicalMaterialOrigin](biologicalMaterialOrigin.md) |  |
| [biologicalPartOrigin](biologicalPartOrigin.md) |  |
| [biologicalSourceType](biologicalSourceType.md) |  |
| [biosafetyRestrictions](biosafetyRestrictions.md) |  |
| [canItBeUsedToProduceGMO](canItBeUsedToProduceGMO.md) |  |
| [category](category.md) |  |
| [certification](certification.md) |  |
| [certificationDocument](certificationDocument.md) |  |
| [clinicalInformation](clinicalInformation.md) |  |
| [clonedIntoPlasmid](clonedIntoPlasmid.md) |  |
| [coInfectingViruses](coInfectingViruses.md) |  |
| [collection](collection.md) |  |
| [collectionDataProvider](collectionDataProvider.md) |  |
| [collectionDate](collectionDate.md) |  |
| [collectionItem](collectionItem.md) |  |
| [complementaryDocument](complementaryDocument.md) |  |
| [contactPoint](contactPoint.md) |  |
| [contaminationWithCoInfectingViruses](contaminationWithCoInfectingViruses.md) |  |
| [contentType](contentType.md) |  |
| [contentURL](contentURL.md) |  |
| [country](country.md) |  |
| [countryOfCollection](countryOfCollection.md) |  |
| [cultivability](cultivability.md) |  |
| [description](description.md) |  |
| [descriptionOfModificationsMadeFromTheReferenceSequences](descriptionOfModificationsMadeFromTheReferenceSequences.md) |  |
| [disposalConsiderations](disposalConsiderations.md) |  |
| [domain](domain.md) |  |
| [ecologicalInformation](ecologicalInformation.md) |  |
| [email](email.md) |  |
| [exposureControlsPersonalProtection](exposureControlsPersonalProtection.md) |  |
| [expressedAs](expressedAs.md) |  |
| [expressionSystem](expressionSystem.md) |  |
| [externalEquivalentTaxon](externalEquivalentTaxon.md) |  |
| [externalRelatedReference](externalRelatedReference.md) |  |
| [fireFightingMeasures](fireFightingMeasures.md) |  |
| [firstAidMeasures](firstAidMeasures.md) |  |
| [format](format.md) |  |
| [functionalCharacterization](functionalCharacterization.md) |  |
| [functionalTechnicalDescription](functionalTechnicalDescription.md) |  |
| [furtherInformation](furtherInformation.md) |  |
| [genomeSequencing](genomeSequencing.md) |  |
| [genotype](genotype.md) |  |
| [handlingAndStorage](handlingAndStorage.md) |  |
| [hasGbFileOfTheConstruct](hasGbFileOfTheConstruct.md) |  |
| [hasIATAClassification](hasIATAClassification.md) |  |
| [hasSOPFile](hasSOPFile.md) |  |
| [hasTAG](hasTAG.md) |  |
| [hazardsIdentification](hazardsIdentification.md) |  |
| [homePage](homePage.md) |  |
| [hostType](hostType.md) |  |
| [hybridomaDescription](hybridomaDescription.md) |  |
| [ID](ID.md) |  |
| [identificationTechnique](identificationTechnique.md) |  |
| [inclusionBodiesType](inclusionBodiesType.md) |  |
| [indigenousPoepleAndLocalCommunityOrigin](indigenousPoepleAndLocalCommunityOrigin.md) |  |
| [infectivity](infectivity.md) |  |
| [infectivityTest](infectivityTest.md) |  |
| [internalReference](internalReference.md) |  |
| [inVocabulary](inVocabulary.md) |  |
| [isItAClonedNucleicAcid](isItAClonedNucleicAcid.md) |  |
| [isolate](isolate.md) |  |
| [isolationConditions](isolationConditions.md) |  |
| [isolationHost](isolationHost.md) |  |
| [isolationTechnique](isolationTechnique.md) |  |
| [journal](journal.md) |  |
| [keywords](keywords.md) |  |
| [letterOfAuthority](letterOfAuthority.md) |  |
| [license](license.md) |  |
| [licensingOrAttribution](licensingOrAttribution.md) |  |
| [loginRequestMethod](loginRequestMethod.md) |  |
| [loginTokenName](loginTokenName.md) |  |
| [loginURL](loginURL.md) |  |
| [logo](logo.md) |  |
| [materialSafetyDataSheet](materialSafetyDataSheet.md) |  |
| [memberOfRI](memberOfRI.md) |  |
| [modelSpecies](modelSpecies.md) |  |
| [modelType](modelType.md) |  |
| [modificationsFromTheReferenceSequences](modificationsFromTheReferenceSequences.md) |  |
| [msdsContact](msdsContact.md) |  |
| [mutationObserved](mutationObserved.md) |  |
| [mycoplasmicContent](mycoplasmicContent.md) |  |
| [name](name.md) |  |
| [note](note.md) |  |
| [observedMutations](observedMutations.md) |  |
| [oRCIDiD](oRCIDiD.md) |  |
| [originator](originator.md) |  |
| [parentCategory](parentCategory.md) |  |
| [parentTaxon](parentTaxon.md) |  |
| [partIdentification](partIdentification.md) |  |
| [pasmidSelection](pasmidSelection.md) |  |
| [passage](passage.md) |  |
| [pathogenIdentification](pathogenIdentification.md) |  |
| [pathogenName](pathogenName.md) |  |
| [pathogenType](pathogenType.md) |  |
| [permitIdentifierForABS](permitIdentifierForABS.md) |  |
| [physicalChemicalProperties](physicalChemicalProperties.md) |  |
| [postalCode](postalCode.md) |  |
| [previouslyKnownAs](previouslyKnownAs.md) |  |
| [productionCellLine](productionCellLine.md) |  |
| [productionSystem](productionSystem.md) |  |
| [productPicture](productPicture.md) |  |
| [productsOfTheBundle](productsOfTheBundle.md) |  |
| [propagationHost](propagationHost.md) |  |
| [proteinPurification](proteinPurification.md) |  |
| [proteinTAG](proteinTAG.md) |  |
| [providedEntityType](providedEntityType.md) |  |
| [provider](provider.md) |  |
| [qualityGrading](qualityGrading.md) |  |
| [queryMethod](queryMethod.md) |  |
| [queryURL](queryURL.md) |  |
| [rank](rank.md) |  |
| [rankDataProvider](rankDataProvider.md) |  |
| [recombinantMaterial](recombinantMaterial.md) |  |
| [recombinantPartIdentification](recombinantPartIdentification.md) |  |
| [reference](reference.md) |  |
| [referenceLabel](referenceLabel.md) |  |
| [referenceProviderName](referenceProviderName.md) |  |
| [referenceProviderPrefix](referenceProviderPrefix.md) |  |
| [refSKU](refSKU.md) |  |
| [regionEncompassedInThisProduct](regionEncompassedInThisProduct.md) |  |
| [regulatoryInformation](regulatoryInformation.md) |  |
| [relatedDOI](relatedDOI.md) |  |
| [relatedPDB](relatedPDB.md) |  |
| [resourceURL](resourceURL.md) |  |
| [riskGroup](riskGroup.md) |  |
| [sequence](sequence.md) |  |
| [sequenceChecked](sequenceChecked.md) |  |
| [sequenceFASTA](sequenceFASTA.md) |  |
| [sequenceProvider](sequenceProvider.md) |  |
| [sequenceReference](sequenceReference.md) |  |
| [sequencing](sequencing.md) |  |
| [serotype](serotype.md) |  |
| [shippingConditions](shippingConditions.md) |  |
| [sourceOfInformation](sourceOfInformation.md) |  |
| [specialFeature](specialFeature.md) |  |
| [specificity](specificity.md) |  |
| [specificityDocumented](specificityDocumented.md) |  |
| [stabilityAndReactivity](stabilityAndReactivity.md) |  |
| [storageConditions](storageConditions.md) |  |
| [strain](strain.md) |  |
| [streetAddress](streetAddress.md) |  |
| [subspecies](subspecies.md) |  |
| [suspectedEpidemiologicalOrigin](suspectedEpidemiologicalOrigin.md) |  |
| [targetedAntigen](targetedAntigen.md) |  |
| [targetedRegion](targetedRegion.md) |  |
| [taxon](taxon.md) |  |
| [taxonDataProvider](taxonDataProvider.md) |  |
| [taxonomicID](taxonomicID.md) |  |
| [taxonomicNodeID](taxonomicNodeID.md) |  |
| [taxonomy](taxonomy.md) |  |
| [technicalRecommendation](technicalRecommendation.md) |  |
| [telephone](telephone.md) |  |
| [term](term.md) |  |
| [termDataProvider](termDataProvider.md) |  |
| [theTAGStatusOfTheSolubilizedProtein](theTAGStatusOfTheSolubilizedProtein.md) |  |
| [thirdPartyDistributionConsent](thirdPartyDistributionConsent.md) |  |
| [titer](titer.md) |  |
| [title](title.md) |  |
| [toxicologicalInformation](toxicologicalInformation.md) |  |
| [transmissionMethod](transmissionMethod.md) |  |
| [transportInformation](transportInformation.md) |  |
| [typeOfFunctionalCharacterization](typeOfFunctionalCharacterization.md) |  |
| [unitCost](unitCost.md) |  |
| [unitDefinition](unitDefinition.md) |  |
| [usageRestrictions](usageRestrictions.md) |  |
| [variant](variant.md) |  |
| [version](version.md) |  |
| [versionDataProvider](versionDataProvider.md) |  |
| [versionOf](versionOf.md) |  |
| [weight](weight.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Cultivability](Cultivability.md) |  |
| [ExpressedAs](ExpressedAs.md) |  |
| [ExpressionSystem](ExpressionSystem.md) |  |
| [FunctionalCharacterization](FunctionalCharacterization.md) |  |
| [GenomeSequencing](GenomeSequencing.md) |  |
| [HostType](HostType.md) |  |
| [InclusionBodiesType](InclusionBodiesType.md) |  |
| [Infectivity](Infectivity.md) |  |
| [LetterOfAuthority](LetterOfAuthority.md) |  |
| [LoginRequestMethod](LoginRequestMethod.md) |  |
| [PathogenType](PathogenType.md) |  |
| [ProteinPurification](ProteinPurification.md) |  |
| [QueryMethod](QueryMethod.md) |  |
| [SequenceProvider](SequenceProvider.md) |  |
| [Sequencing](Sequencing.md) |  |
| [TypeOfFunctionalCharacterization](TypeOfFunctionalCharacterization.md) |  |


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
