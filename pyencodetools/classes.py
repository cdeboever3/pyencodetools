from base import EncodeObject

class AntibodyLotReview(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Antibody
        # See antibody_lot.json for available identifiers.
        if 'antibody' in d.keys():
            self.antibody.append(AntibodyLot(t, fetch=False))
        # Target: The name of the gene whose expression or product is the intended goal of the antibody.
        # See target.json for available identifiers.
        if 'target' in d.keys():
            self.target.append(Target(t, fetch=False))
        # Characterizations: Antibody characterizations under review.
        if 'characterizations' in d.keys():
            self.characterizations = []
            for t in d['characterizations']:
                self.characterizations.append(AntibodyCharacterization(t, fetch=False))

class AntibodyCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Antibody characterized
        # See antibody_lot.json for available identifiers.
        if 'characterizes' in d.keys():
            self.characterizes.append(AntibodyLot(t, fetch=False))
        # Primary characterization lane reviews: Characterization details reviewed by each cell type for immunoblot and immunoprecipitation primary characterizations only.
        # Do not submit status, it is assigned by DCC when reviewing the characterization.
        if 'characterization_reviews' in d.keys():
            self.characterization_reviews = []
            for t in d['characterization_reviews']:
debug
                # Characterization status: The current state of the characterization for a particular cell type.
                if 'lane_status' in d.keys():
                    self.lane_status = d['lane_status']
                assert self.lane_status in [u'pending dcc review', u'compliant', u'not compliant']
debug
                # Lane
                if 'lane' in d.keys():
                    self.lane = int(d['lane'])
debug
                # Ontology ID: Ontology identifier describing biosample.
                # NTR is a new term request identifier provided by the DCC.
                if 'biosample_term_id' in d.keys():
                    self.biosample_term_id = d['biosample_term_id']
debug
                # Biosample type: The categorization of the biosample.
                if 'biosample_type' in d.keys():
                    self.biosample_type = d['biosample_type']
                assert self.biosample_type in [u'primary cell', u'immortalized cell line', u'tissue', u'in vitro differentiated cells', u'induced pluripotent stem cell line', u'stem cell']
debug
                # Ontology term: Ontology term describing biosample.
                if 'biosample_term_name' in d.keys():
                    self.biosample_term_name = d['biosample_term_name']
debug
                # Organism
                # See organism.json for available identifiers.
                if 'organism' in d.keys():
                    self.organism.append(Organism(t, fetch=False))
        # Target: The name of the gene whose expression or product is the intended goal of the antibody.
        # See target.json for available identifiers.
        if 'target' in d.keys():
            self.target.append(Target(t, fetch=False))

class AntibodyLot(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Antigen sequence: The amino acid sequence of the antigen.
        if 'antigen_sequence' in d.keys():
            self.antigen_sequence = d['antigen_sequence']
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Isotype: The class of antibody ( e.g. IgA, IgD, IgE, IgG or IgM)
        if 'isotype' in d.keys():
            self.isotype = d['isotype']
        assert self.isotype in [u'IgA1', u'IgA2', u'IgD', u'IgG', u'IgG\u03ba', u'IgG1', u'IgG1\u03ba', u'IgG1\u03bb', u'IgG2', u'IgG2\u03ba', u'IgG2\u03bb', u'IgG2a', u'IgG2a\u03ba', u'IgG2a\u03bb', u'IgG2b', u'IgG2b\u03ba', u'IgG2b\u03bb', u'IgG3', u'IgG3\u03ba', u'IgG4', u'IgA', u'IgM', u'IgM\u03ba', u'IgE', u'serum']
        # Lot ID aliases: The lot identifiers for this lot deemed to be exactly the same by the vendor.
        if 'lot_id_alias' in d.keys():
            self.lot_id_alias = []
            for t in d['lot_id_alias']:
                self.lot_id_alias.append(t)
        # ENCODE accession
        self.accession = d['accession']
        # URL: An external resource with additional information about the antibody.
        if 'url' in d.keys():
            self.url = d['url']
        # Antigen description: The plain text description of the antigen used in raising the antibody (e.g. amino acid residue locations of the antigen).
        if 'antigen_description' in d.keys():
            self.antigen_description = d['antigen_description']
        # Purification methods: The purification protocols used to isolate the antibody.
        if 'purifications' in d.keys():
            self.purifications = []
            for t in d['purifications']:
                self.purifications.append(t)
        # Host: The organism the antibody was grown in.
        # See organism.json for available identifiers.
        if 'host_organism' in d.keys():
            self.host_organism.append(Organism(t, fetch=False))
        # Lot ID: The lot identifier provided by the originating lab or vendor.
        if 'lot_id' in d.keys():
            self.lot_id = d['lot_id']
        # Antibody clonality: The diversification of the immune cell lineage to make the antibody.
        if 'clonality' in d.keys():
            self.clonality = d['clonality']
        assert self.clonality in [u'polyclonal', u'monoclonal']

class Grant(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Description
        if 'description' in d.keys():
            self.description = d['description']
        # End date
        # Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'end_date' in d.keys():
            self.end_date = d['end_date']
        # Name: The grant name from the NIH database, if applicable.
        if 'title' in d.keys():
            self.title = d['title']
        # URL: An external resource with additional information about the grant.
        if 'url' in d.keys():
            self.url = d['url']
        # BioProject: The collection of biological data related to a single initiative, originating from a consortium.
        if 'project' in d.keys():
            self.project = d['project']
        # Phase: The name of the bioproject phase.
        if 'rfa' in d.keys():
            self.rfa = d['rfa']
        # P.I.: Principle Investigator of the grant.
        # See user.json for available identifiers.
        if 'pi' in d.keys():
            self.pi.append(User(t, fetch=False))
        # Start date
        # Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'start_date' in d.keys():
            self.start_date = d['start_date']
        # Number: The official grant number from the NIH database, if applicable
        if 'name' in d.keys():
            self.name = d['name']

class Biosample(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # ENCODE accession
        self.accession = d['accession']
        # Passage number: In calculating passage number, include passages from the source.
        if 'passage_number' in d.keys():
            self.passage_number = int(d['passage_number'])
        # Starting amount: The initial quantity of cells or tissue obtained.
        # The pattern is only enforced when the value supplied is a string.
            try:
                self.starting_amount = float(d['starting_amount'])
            except ValueError:
                self.starting_amount = d['starting_amount']
        # Post-synchronization time units
        # Use in conjunction with post_synchronization_time to specify time elapsed post-synchronization.
        if 'post_synchronization_time_units' in d.keys():
            self.post_synchronization_time_units = d['post_synchronization_time_units']
        assert self.post_synchronization_time_units in [u'minute', u'hour', u'day', u'week', u'month', u'year', u'stage']
        # Culture harvest date: For cultured samples, the date the biosample was taken.
        # Date can be submitted in as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM.
        if 'culture_harvest_date' in d.keys():
            self.culture_harvest_date = d['culture_harvest_date']
        # RNAi vectors: RNAi vectors stably or transiently transfected.
        if 'rnais' in d.keys():
            self.rnais = []
            for t in d['rnais']:
                self.rnais.append(RNAiVector(t, fetch=False))
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Model organism donor age:  The age or age range of the model donor organism when biological material was sampled.
        if 'model_organism_age' in d.keys():
            self.model_organism_age = d['model_organism_age']
        if 'depleted_in_term_id' in d.keys():
            self.depleted_in_term_id = []
            for t in d['depleted_in_term_id']:
                self.depleted_in_term_id.append(t)
        # Note: Additional information pertaining to the biosample.
        if 'note' in d.keys():
            self.note = d['note']
        # Fly life stage
        if 'fly_life_stage' in d.keys():
            self.fly_life_stage = d['fly_life_stage']
        assert self.fly_life_stage in [u'embryonic', u'first instar larva', u'second instar larva', u'third instar larva', u'wandering third instar larva', u'prepupa', u'pupa', u'adult']
        # Subcellular fraction ID: The GO (Gene Ontology) identifier for cellular component that constitutes the biosample.
        # Based on the choice in subcellular_fraction_term_name use the following guide: nucleus - GO:0005634, cytosol - GO:0005829, chromatin - GO:0000785, membrane - GO:0016020, mitochondria - GO:0005739, nuclear matrix - GO:0016363, nucleolus - GO:0005730, nucleoplasm - GO:0005654, polysome - GO:0005844.
        if 'subcellular_fraction_term_id' in d.keys():
            self.subcellular_fraction_term_id = d['subcellular_fraction_term_id']
        assert self.subcellular_fraction_term_id in [u'GO:0005634', u'GO:0005829', u'GO:0000785', u'GO:0016020', u'GO:0005739', u'GO:0016363', u'GO:0005730', u'GO:0005654', u'GO:0005844']
        # Post-synchronization time
        # Use in conjunction with fly_sychronization_stage or worm_synchronization_stage to specify time elapsed post-synchronization.
        if 'post_synchronization_time' in d.keys():
            self.post_synchronization_time = d['post_synchronization_time']
        # Donor
        # For human biosamples, see human_donor.json for available identifiers. For mouse biosamples, see mouse_donor.json for available identifiers.
        if 'donor' in d.keys():
            self.donor.append(Donor(t, fetch=False))
        # Pooled from: The biosamples from which aliquots were pooled to form the biosample.
        if 'pooled_from' in d.keys():
            self.pooled_from = []
            for t in d['pooled_from']:
                self.pooled_from.append(Biosample(t, fetch=False))
        # Model organism donor age units
        if 'model_organism_age_units' in d.keys():
            self.model_organism_age_units = d['model_organism_age_units']
        assert self.model_organism_age_units in [u'minute', u'hour', u'day', u'week', u'month', u'year', u'stage']
        # Separated from: A biosample from which a discrete component was taken. That component is this biosample.
        # See biosamples.json for available identifiers.
        if 'part_of' in d.keys():
            self.part_of.append(Biosample(t, fetch=False))
        # Description: A plain text description of the biosample. Do not include experiment details, constructs or treatments.
        if 'description' in d.keys():
            self.description = d['description']
        # DNA constructs: Expression or targeting vectors stably or transiently transfected (not RNAi).
        if 'constructs' in d.keys():
            self.constructs = []
            for t in d['constructs']:
                self.constructs.append(DNAConstruct(t, fetch=False))
        # Treatments
        if 'treatments' in d.keys():
            self.treatments = []
            for t in d['treatments']:
                self.treatments.append(Treatment(t, fetch=False))
        if 'depleted_in_term_name' in d.keys():
            self.depleted_in_term_name = []
            for t in d['depleted_in_term_name']:
                self.depleted_in_term_name.append(t)
        # Subcellular fraction name: The GO (Gene Ontology) term name for cellular component that constitutes the biosample.
        if 'subcellular_fraction_term_name' in d.keys():
            self.subcellular_fraction_term_name = d['subcellular_fraction_term_name']
        assert self.subcellular_fraction_term_name in [u'nucleus', u'cytosol', u'chromatin', u'membrane', u'mitochondria', u'nuclear matrix', u'nucleolus', u'nucleoplasm', u'polysome']
        # Protocol documents: Documents that describe the biosample preparation.
        if 'protocol_documents' in d.keys():
            self.protocol_documents = []
            for t in d['protocol_documents']:
                self.protocol_documents.append(Document(t, fetch=False))
        # Cell-cycle phase
        if 'phase' in d.keys():
            self.phase = d['phase']
        assert self.phase in [u'G1', u'G1b', u'G2', u'S1', u'S2', u'S3', u'S4']
        # Fly synchronization stage
        # Stage at which flies were synchronized. Use in conjunction with time and time units post-synchronization.
        if 'fly_synchronization_stage' in d.keys():
            self.fly_synchronization_stage = d['fly_synchronization_stage']
        assert self.fly_synchronization_stage in [u'fertilization', u'puff stage: PS (1-2), dark blue gut', u'puff stage: PS (3-6), light blue gut', u'puff stage: PS (7-9), clear gut', u'white prepupa', u'eclosion']
        # Date obtained: For tissue samples, the date the biosample was taken.
        # Date can be submitted in as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'date_obtained' in d.keys():
            self.date_obtained = d['date_obtained']
        # Starting amount units
        if 'starting_amount_units' in d.keys():
            self.starting_amount_units = d['starting_amount_units']
        assert self.starting_amount_units in [u'g', u'mg', u'cells/ml', u'cells', u'whole embryos', u'items', u'\u03bcg', u'whole animals']
        # Culture start date: For cultured samples, the date the culture was started. For cell lines, the date this particular growth was started, not the date the line was established.
        # Date can be submitted in as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD ((TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'culture_start_date' in d.keys():
            self.culture_start_date = d['culture_start_date']
        # Model organism sex
        if 'model_organism_sex' in d.keys():
            self.model_organism_sex = d['model_organism_sex']
        assert self.model_organism_sex in [u'male', u'female', u'unknown', u'mixed', u'hermaphrodite']
        # URL: An external resource with additional information about the biosample.
        if 'url' in d.keys():
            self.url = d['url']
        # Organism
        # See organism.json for available identifiers.
        if 'organism' in d.keys():
            self.organism.append(Organism(t, fetch=False))
        # Model organism donor health status
        if 'model_organism_health_status' in d.keys():
            self.model_organism_health_status = d['model_organism_health_status']
        # Worm life stage
        if 'worm_life_stage' in d.keys():
            self.worm_life_stage = d['worm_life_stage']
        assert self.worm_life_stage in [u'early embryonic', u'late embryonic', u'embryonic', u'L1 larva', u'L2 larva', u'L2d larva', u'L3 larva', u'L4 larva', u'dauer', u'young adult', u'adult']
        # Derived from: A biosample that the sample derives from via a construct or treatment.
        # See biosample.json for available identifiers.
        if 'derived_from' in d.keys():
            self.derived_from.append(Biosample(t, fetch=False))
        # Mating status: The mating status of the animal.
        if 'model_organism_mating_status' in d.keys():
            self.model_organism_mating_status = d['model_organism_mating_status']
        assert self.model_organism_mating_status in [u'mated', u'virgin', u'sterile', u'mixed']
        # Transfection type: The persistence of the transfection construct.
        if 'transfection_type' in d.keys():
            self.transfection_type = d['transfection_type']
        assert self.transfection_type in [u'stable', u'transient']
        # Mouse life stage
        if 'mouse_life_stage' in d.keys():
            self.mouse_life_stage = d['mouse_life_stage']
        assert self.mouse_life_stage in [u'adult', u'unknown', u'embryonic', u'postnatal']
        # Worm synchronization stage
        # Stage at which worms were synchronized. Use in conjunction with time and time units post-synchronization.
        if 'worm_synchronization_stage' in d.keys():
            self.worm_synchronization_stage = d['worm_synchronization_stage']
        assert self.worm_synchronization_stage in [u'fertilization', u'egg laying', u'starved L1 larva', u'dauer exit']
        # Life stage
        if 'life_stage' in d.keys():
            self.life_stage = d['life_stage']
        # System slims
        if 'system_slims' in d.keys():
            self.system_slims = d['system_slims']
        # Age units
        if 'age_units' in d.keys():
            self.age_units = d['age_units']
        # Age
        if 'age' in d.keys():
            self.age = d['age']
        # Organ slims
        if 'organ_slims' in d.keys():
            self.organ_slims = d['organ_slims']
        # Health status
        if 'health_status' in d.keys():
            self.health_status = d['health_status']
        # Sex
        if 'sex' in d.keys():
            self.sex = d['sex']
        # Ontology synonyms
        if 'synonyms' in d.keys():
            self.synonyms = d['synonyms']
        # Synchronization
        if 'synchronization' in d.keys():
            self.synchronization = d['synchronization']
        # Developmental slims
        if 'developmental_slims' in d.keys():
            self.developmental_slims = d['developmental_slims']

class BiosampleCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Biosample characterized
        # See biosample.json for available identifiers.
        if 'characterizes' in d.keys():
            self.characterizes.append(Biosample(t, fetch=False))

class BaseCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Comment: Additional information pertaining to the characterization.
        if 'comment' in d.keys():
            self.comment = d['comment']
        # Method: Experimental method of the characterization.
        if 'characterization_method' in d.keys():
            self.characterization_method = d['characterization_method']
        assert self.characterization_method in [u'immunoblot', u'immunoprecipitation', u'immunofluorescence', u'knockdown or knockout', u'immunoprecipitation followed by mass spectrometry', u'ChIP-seq comparison', u'motif enrichment', u'dot blot assay', u'peptide array assay', u'peptide ELISA assay', u'peptide competition assay', u'mutant organism', u'mutant histone modifier', u'mutant histone', u'annotation enrichment', u'FACs analysis', u'qPCR analysis']
        # The specific entity for which the characterization applies.
        if 'characterizes' in d.keys():
            self.characterizes = d['characterizes']
        # Caption: A plain text description about the characterization. Characterizations for antibodies should include brief methods, expected MW, cell line(s), labels and justification for acceptance, if necessary
        if 'caption' in d.keys():
            self.caption = d['caption']
        # Date: The date that the characterization was run on.
        # Date can be submitted in as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'date' in d.keys():
            self.date = d['date']

class DNAConstruct(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Integration site: Genomic coordinates where construct is integrated, if known. Use NCBI assembly version:chromosome number:5' nucleotide position (e.g. GRCh37:21:3393939).
        # TODO
        if 'genomic_integration_site' in d.keys():
            self.genomic_integration_site = d['genomic_integration_site']
        # Construct documents: Documents that describe the construct.
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        # Type: The type of sequence expressed from the construct.
        if 'construct_type' in d.keys():
            self.construct_type = d['construct_type']
        assert self.construct_type in [u'fusion protein', u'zinc-finger knockout', u'TALEN']
        # Description: A plain text description of the construct. May include backbone name, description of the insert or purpose of the construct.
        if 'description' in d.keys():
            self.description = d['description']
        # Protein tags: Recombinant tags in the construct.
        if 'tags' in d.keys():
            self.tags = []
            for t in d['tags']:
debug
                if 'name' in d.keys():
                    self.name = d['name']
                assert self.name in [u'eGFP', u'V5', u'HA', u'ER', u'3xFLAG', u'DsRed', u'TRE', u'T2A', u'YFP']
debug
                if 'location' in d.keys():
                    self.location = d['location']
                assert self.location in [u'N-terminal', u'C-terminal', u'other', u'unknown']
        # URL: An external resource with additional information about the construct.
        if 'url' in d.keys():
            self.url = d['url']
        # Promoter genome coordinates: Genomic coordinates of the promoter. Use NCBI assembly version:chromosome number:nucleotide range (e.g. WBcel235:III:1433720-1434340).
        # TODO
        if 'promoter_genome_coordinates' in d.keys():
            self.promoter_genome_coordinates = d['promoter_genome_coordinates']
        # Promoter used in construct: The name of the gene that the promoter regulates natively.
        # See target.json for available identifiers.
        if 'promoter_used' in d.keys():
            self.promoter_used.append(Target(t, fetch=False))
        # Insert genome coordinates: Genomic coordinates of the insert. Use NCBI assembly version:chromosome number:nucleotide range (e.g. GRCh37:15:2800021-28344458).
        # TODO
        if 'insert_genome_coordinates' in d.keys():
            self.insert_genome_coordinates = d['insert_genome_coordinates']
        # Backbone Name: The name of the vector backbone used for the construct.
        if 'vector_backbone_name' in d.keys():
            self.vector_backbone_name = d['vector_backbone_name']
        # Promoter position relative to target: Relative distance of promoter sequence in the construct upstream of the target gene TSS.
        # Distance in bp upstream of target gene TSS in the construct
        # Insert Sequence: DNA sequence inserted into the vector backbone.
        # TODO
        if 'insert_sequence' in d.keys():
            self.insert_sequence = d['insert_sequence']
        # Target: The name of the gene whose expression or product is modified by the construct.
        # See target.json for available identifiers.
        if 'target' in d.keys():
            self.target.append(Target(t, fetch=False))

class DNAConstructCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Construct characterized
        # See contstruct.json for available identifiers.
        if 'characterizes' in d.keys():
            self.characterizes.append(DNAConstruct(t, fetch=False))

class Dataset(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Documents: Documents that provide additional information about the dataset (not data files).
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        # Additional data files: List of data files to be associated with the dataset.
        if 'related_files' in d.keys():
            self.related_files = []
            for t in d['related_files']:
                self.related_files.append(DataFile(t, fetch=False))
        # Description: A plain text description of the dataset.
        if 'description' in d.keys():
            self.description = d['description']
        # ENCODE accession
        self.accession = d['accession']
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Type: The category that best describes the dataset.
        if 'dataset_type' in d.keys():
            self.dataset_type = d['dataset_type']
        assert self.dataset_type in [u'project', u'composite', u'publication', u'spike-ins', u'paired set']
        # Date released
        # Do not submit, value is assigned whe the object is releaesd.
        if 'date_released' in d.keys():
            self.date_released = d['date_released']
        # Files
        if 'files' in d.keys():
            self.files = []
            for t in d['files']:
                self.files.append(DataFile(t, fetch=False))
        # Revoked Files
        if 'revoked_files' in d.keys():
            self.revoked_files = []
            for t in d['revoked_files']:
                self.revoked_files.append(DataFile(t, fetch=False))
        # Assembly
        if 'assembly' in d.keys():
            self.assembly = d['assembly']
        # Track hub
        if 'hub' in d.keys():
            self.hub = d['hub']

class Document(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # URLs: External resources with additional information to the document.
        if 'urls' in d.keys():
            self.urls = []
            for t in d['urls']:
                self.urls.append(t)
        # Type: The category that best describes the document.
        if 'document_type' in d.keys():
            self.document_type = d['document_type']
        assert self.document_type in [u'growth protocol', u'extraction protocol', u'certificate of analysis', u'differentiation protocol', u'dedifferentiation protocol', u'data sheet', u'treatment protocol', u'general protocol', u'excision protocol', u'transfection protocol', u'construct image', u'cell isolation protocol', u'iPS reprogramming protocol', u'standards document', u'strain generation protocol', u'spike-in concentrations', u'other']
        # Description: A plain text description of the document.
        if 'description' in d.keys():
            self.description = d['description']

class Donor(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # URL: An external resource with additional information about the donor.
        if 'url' in d.keys():
            self.url = d['url']
        # Organism: Organism of the donor.
        # Do not submit, value is assigned by the object.
        if 'organism' in d.keys():
            self.organism.append(Organism(t, fetch=False))
        # ENCODE accession
        self.accession = d['accession']

class DonorCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Model organism donor (strain) characterized
        # See donor.json for available identifiers.
        if 'characterizes' in d.keys():
            self.characterizes.append(Donor(t, fetch=False))

class EDWCreateAccessKey(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Programmatic access key username: 
        if 'username' in d.keys():
            self.username = d['username']
        # Email: Email address of user in database
        if 'email' in d.keys():
            self.email = d['email']
        # Secret access key hash: EDW hashed password.
        if 'pwhash' in d.keys():
            self.pwhash = d['pwhash']

class Experiment(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Controls: Experiments that contain files that can serve as scientific controls for this experiment.
        if 'possible_controls' in d.keys():
            self.possible_controls = []
            for t in d['possible_controls']:
                self.possible_controls.append(Experiment(t, fetch=False))
        # Target: For assays, such as ChIP-seq or RIP-seq, the name of the gene whose expression or product is under investigation for the experiment.
        # See target.json for available identifiers.
        if 'target' in d.keys():
            self.target.append(Target(t, fetch=False))
        # Assay ID: OBI (Ontology for Biomedical Investigations) ontology identifier for the assay.
        if 'assay_term_id' in d.keys():
            self.assay_term_id = d['assay_term_id']
        # Assay name: OBI (Ontology for Biomedical Investigations) ontology term for the assay.
        if 'assay_term_name' in d.keys():
            self.assay_term_name = d['assay_term_name']
        # Type
        # Do not need to submit, value is assigned by server.
        if 'dataset_type' in d.keys():
            self.dataset_type = d['dataset_type']
        assert self.dataset_type in [u'experiment']
        # Protocols or other documents that describe the assay or the results (not data files).
        if 'documents' in d.keys():
            self.documents = d['documents']
        # Files
        if 'files' in d.keys():
            self.files = []
            for t in d['files']:
                self.files.append(DataFile(t, fetch=False))
        # Run type
        if 'run_type' in d.keys():
            self.run_type = d['run_type']
        # System slims
        if 'system_slims' in d.keys():
            self.system_slims = d['system_slims']
        # Track hub
        if 'hub' in d.keys():
            self.hub = d['hub']
        # Month releases
        if 'month_released' in d.keys():
            self.month_released = d['month_released']
        # Organ slims
        if 'organ_slims' in d.keys():
            self.organ_slims = d['organ_slims']
        # Synonyms
        if 'synonyms' in d.keys():
            self.synonyms = d['synonyms']
        # Developmental slims
        if 'developmental_slims' in d.keys():
            self.developmental_slims = d['developmental_slims']
        # Assembly
        if 'assembly' in d.keys():
            self.assembly = d['assembly']
        # Revoked Files
        if 'revoked_files' in d.keys():
            self.revoked_files = []
            for t in d['revoked_files']:
                self.revoked_files.append(DataFile(t, fetch=False))

class DataFile(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Original file name: The local file name used at time of submission.
        if 'submitted_file_name' in d.keys():
            self.submitted_file_name = d['submitted_file_name']
        # Paired End Identifier: Which pair the file belongs to (if paired end library)
        if 'paired_end' in d.keys():
            self.paired_end = d['paired_end']
        assert self.paired_end in [u'1', u'2']
        # Mapping assembly: UCSC genome assembly that files were mapped to.
        # Applies for mapped files (e.g. BAM, BED and BigWig).
        if 'assembly' in d.keys():
            self.assembly = d['assembly']
        assert self.assembly in [u'mm9', u'hg19', u'mm10', u'ce10', u'dm3', u'dm6']
        # File format
        if 'file_format' in d.keys():
            self.file_format = d['file_format']
        # MD5sum
        if 'md5sum' in d.keys():
            self.md5sum = d['md5sum']
        # ENCODE accession
        self.accession = d['accession']
        # Supercedes: The files that this file replaces.
        if 'supercedes' in d.keys():
            self.supercedes = []
            for t in d['supercedes']:
                self.supercedes.append(DataFile(t, fetch=False))
        # Platform: The measurement device used to collect data.
        # See platform.json for available identifiers.
        if 'platform' in d.keys():
            self.platform.append(Platform(t, fetch=False))
        # Flowcells: For high-throughput sequencing, the flowcells used for the sequencing of the replicate.
        if 'flowcell_details' in d.keys():
            self.flowcell_details = []
            for t in d['flowcell_details']:
debug
                # Machine Name: The lab specific name of the machine used.
                if 'machine' in d.keys():
                    self.machine = d['machine']
debug
                # Lane
                if 'lane' in d.keys():
                    self.lane = d['lane']
debug
                # Barcode
                if 'barcode' in d.keys():
                    self.barcode = d['barcode']
debug
                # Flowcell ID
                if 'flowcell' in d.keys():
                    self.flowcell = d['flowcell']
        # Replicate: The experimental replicate designation for the file.
        # See replicate.json for available identifiers.
        if 'replicate' in d.keys():
            self.replicate.append(Replicate(t, fetch=False))
        # File pairing: The file that corresponds with this file.
        # See file.json for a list of available identifiers.
        if 'paired_with' in d.keys():
            self.paired_with.append(DataFile(t, fetch=False))
        # Derived from: The files participating as inputs into software to produce this output file.
        if 'derived_from' in d.keys():
            self.derived_from = []
            for t in d['derived_from']:
                self.derived_from.append(DataFile(t, fetch=False))
        # File size
        # File size is specified in bytes
        if 'file_size' in d.keys():
            self.file_size = int(d['file_size'])
        # Controlled by: The files that control this file. 
        if 'controlled_by' in d.keys():
            self.controlled_by = []
            for t in d['controlled_by']:
                self.controlled_by.append(DataFile(t, fetch=False))
        # Output type: A description of the file's purpose or contents.
        if 'output_type' in d.keys():
            self.output_type = d['output_type']
        # Dataset: The experiment or dataset the file belongs to.
        # For experiments, see experiment.json for available identifiers. For datasets, see dataset.json for available identifiers.
        if 'dataset' in d.keys():
            if d['dataset'] == Experiment:
                self.dataset = Experiment(d['dataset'], fetch=False)
            if d['dataset'] == Dataset:
                self.dataset = Dataset(d['dataset'], fetch=False)
        # Download URL
        if 'href' in d.keys():
            self.href = d['href']

class DataFileRelationships(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Superseded by: The file that has replaced this file.
        # See file.json for a list of available identifiers.
        if 'replaced_by' in d.keys():
            self.replaced_by.append(DataFile(t, fetch=False))
        # File pairing: The file that corresponds with this file.
        # See file.json for a list of available identifiers.
        if 'paired_with' in d.keys():
            self.paired_with.append(DataFile(t, fetch=False))
        # Generated from: The files participating as inputs into software to produce this output file.
        if 'derived_from' in d.keys():
            self.derived_from = []
            for t in d['derived_from']:
                self.derived_from.append(DataFile(t, fetch=False))
        # Controls for: The data files that this file serves as a scientific control. 
        if 'controls_for' in d.keys():
            self.controls_for = []
            for t in d['controls_for']:
                self.controls_for.append(DataFile(t, fetch=False))
        # External identifiers: Unique identifiers from external resources.
        if 'dbxref' in d.keys():
            self.dbxref = []
            for t in d['dbxref']:
                self.dbxref.append(t)

class FlyDonor(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Strain documents: Documents that describe the strain and its generation.
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        if 'organism' in d.keys():
            self.organism = d['organism']
        # The genotype of the strain according to accepted nomenclature conventions: http://flybase.org/static_pages/docs/nomenclature/nomenclature3.html
        if 'genotype' in d.keys():
            self.genotype = d['genotype']

class HumanDonor(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Fraternal twin
        # For human biosamples, see human_donor.json for available identifiers. For mouse biosamples, see mouse_donor.json for available identifiers.
        if 'fraternal_twin' in d.keys():
            self.fraternal_twin.append(Donor(t, fetch=False))
        # Donor age units
        if 'age_units' in d.keys():
            self.age_units = d['age_units']
        assert self.age_units in [u'day', u'week', u'month', u'year']
        if 'organism' in d.keys():
            self.organism = d['organism']
        # Donor age:  The age or age range of the donor when biological material was sampled.
        if 'age' in d.keys():
            self.age = d['age']
        # Life stage
        if 'life_stage' in d.keys():
            self.life_stage = d['life_stage']
        assert self.life_stage in [u'fetal', u'newborn', u'child', u'adult', u'unknown', u'embryonic', u'postnatal']
        # Sex
        if 'sex' in d.keys():
            self.sex = d['sex']
        assert self.sex in [u'male', u'female', u'unknown', u'mixed']
        # Donor health status
        if 'health_status' in d.keys():
            self.health_status = d['health_status']
        # Parents: Donor IDs of biological parents, if known.
        if 'parents' in d.keys():
            self.parents = []
            for t in d['parents']:
                self.parents.append(Donor(t, fetch=False))
        # Siblings: Donors that have at least one parent in common.
        if 'siblings' in d.keys():
            self.siblings = []
            for t in d['siblings']:
                self.siblings.append(Donor(t, fetch=False))
        # Identical twin: A donor that have identical genetic material.
        # For human biosamples, see human_donor.json for available identifiers. For mouse biosamples, see mouse_donor.json for available identifiers.
        if 'identical_twin' in d.keys():
            self.identical_twin.append(Donor(t, fetch=False))
        # Children: Donors that genetic material was supplied to.
        if 'children' in d.keys():
            self.children = []
            for t in d['children']:
                self.children.append(Donor(t, fetch=False))
        # Ethnicity
        if 'ethnicity' in d.keys():
            self.ethnicity = d['ethnicity']

class Image(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Caption
        if 'caption' in d.keys():
            self.caption = d['caption']

class Lab(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # City
        if 'city' in d.keys():
            self.city = d['city']
        # Fax number: A fax number for the lab (with country code).
        if 'fax' in d.keys():
            self.fax = d['fax']
        # Primary phone number: The lab's primary phone number (with country code).
        if 'phone1' in d.keys():
            self.phone1 = d['phone1']
        # Name: A short unique name for the lab, current convention is lower cased and hyphen delimited of PI's first and last name (e.g. john-doe).
        if 'name' in d.keys():
            self.name = d['name']
        # Title: A unique name for affiliation identification, current convention is comma separated PI's first & last name and institute label. (e.g. John Doe, UNI).
        if 'title' in d.keys():
            self.title = d['title']
        # Alternate phone number: The lab's alternative phone number (with country code).
        if 'phone2' in d.keys():
            self.phone2 = d['phone2']
        # Institute label: An abbreviation for the institute the lab is associated with.
        if 'institute_label' in d.keys():
            self.institute_label = d['institute_label']
        # Address line 2
        if 'address2' in d.keys():
            self.address2 = d['address2']
        # Institute: The name for the institute the lab is associated with.
        if 'institute_name' in d.keys():
            self.institute_name = d['institute_name']
        # Country
        if 'country' in d.keys():
            self.country = d['country']
        # URL: An external resource with additional information about the lab.
        if 'url' in d.keys():
            self.url = d['url']
        # State/Province/Region
        if 'state' in d.keys():
            self.state = d['state']
        # Grants: Grants associated with the lab.
        if 'awards' in d.keys():
            self.awards = []
            for t in d['awards']:
                self.awards.append(Grant(t, fetch=False))
        # Address line 1
        if 'address1' in d.keys():
            self.address1 = d['address1']
        # ZIP/Postal code
        if 'postal_code' in d.keys():
            self.postal_code = d['postal_code']
        # P.I.: Principle Investigator of the lab.
        # See user.json for available identifiers.
        if 'pi' in d.keys():
            self.pi.append(User(t, fetch=False))

class Library(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # ENCODE accession
        self.accession = d['accession']
        # The lot identifier provided by the vendor, for nucleic acids or proteins purchased directly from a vendor (e.g. total RNA).
        if 'lot_id' in d.keys():
            self.lot_id = d['lot_id']
        # Nucleic acid starting quantity units: The units used for starting amount of nucleic acid.
        if 'nucleic_acid_starting_quantity_units' in d.keys():
            self.nucleic_acid_starting_quantity_units = d['nucleic_acid_starting_quantity_units']
        assert self.nucleic_acid_starting_quantity_units in [u'cells', u'cell-equivalent', u'ng', u'pg', u'mg']
        # Protocol documents: Documents that describe the preparation of the library.
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        # Fragmentation date: The date that the nucleic acid was fragmented.
        # Date can be submitted in as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).
        if 'fragmentation_date' in d.keys():
            self.fragmentation_date = d['fragmentation_date']
        if 'depleted_in_term_id' in d.keys():
            self.depleted_in_term_id = []
            for t in d['depleted_in_term_id']:
                self.depleted_in_term_id.append(t)
        # Strand specificity: The preparation of the library using a strand-specific protocol.
        # Fragmentation method: A short description or reference of the nucleic acid fragmentation protocol used in library preparation, if applicable.
        if 'fragmentation_method' in d.keys():
            self.fragmentation_method = d['fragmentation_method']
        # Lysis method: A short description or reference of the cell lysis protocol used in library preparation, if applicable
        if 'lysis_method' in d.keys():
            self.lysis_method = d['lysis_method']
        # The vendor, for nucleic acids or proteins purchased directly from a vendor (e.g. total RNA).
        if 'source' in d.keys():
            self.source = d['source']
        # Biosample: The biosample that nucleic acid was isolated from to generate the library.
        # See biosample.json for available identifiers.
        if 'biosample' in d.keys():
            self.biosample.append(Biosample(t, fetch=False))
        # Extraction method: A short description or reference of the nucleic acid extraction protocol used in library preparation, if applicable.
        if 'extraction_method' in d.keys():
            self.extraction_method = d['extraction_method']
        # Size selection method: A short description or reference of the size selection protocol used in library preparation, if applicable.
        if 'library_size_selection_method' in d.keys():
            self.library_size_selection_method = d['library_size_selection_method']
        # Nucleic acid term: SO (Sequence Ontology) term best matching the nucleic acid isolated to generate the library (e.g. 'RNA' for a total RNA library, even if that library is subsequently reverse transcribed for DNA sequencing.)
        if 'nucleic_acid_term_name' in d.keys():
            self.nucleic_acid_term_name = d['nucleic_acid_term_name']
        assert self.nucleic_acid_term_name in [u'DNA', u'RNA', u'polyadenylated mRNA', u'miRNA']
        # Crosslinking method: A short description or reference of the crosslinking protocol used in library preparation, if applicable.
        if 'crosslinking_method' in d.keys():
            self.crosslinking_method = d['crosslinking_method']
        assert self.crosslinking_method in [u'formaldehyde', u'ultraviolet irradiation']
        # Treatments
        if 'treatments' in d.keys():
            self.treatments = []
            for t in d['treatments']:
                self.treatments.append(Treatment(t, fetch=False))
        if 'depleted_in_term_name' in d.keys():
            self.depleted_in_term_name = []
            for t in d['depleted_in_term_name']:
                self.depleted_in_term_name.append(t)
        # Paired ended: Whether or not the library was prepared with paired ends
        # The product identifier provided by the vendor, for nucleic acids or proteins purchased directly from a vendor (e.g. total RNA).
        if 'product_id' in d.keys():
            self.product_id = d['product_id']
        # Size range: The measured size range of the purified nucleic acid, in bp.
        if 'size_range' in d.keys():
            self.size_range = d['size_range']
        # Nucleic acid ID: SO (Sequence Ontology) identifier best matching the nucleic acid isolated to generate the library (e.g. 'SO:0000356' for a total RNA library, even if that library is subsequently reverse transcribed for DNA sequencing.)
        # Based on the choice in nucleic_acid_term_name use the following guide: DNA - SO:0000352, RNA - SO:0000356,  polyadenylated mRNA - SO:0000871 or miRNA - SO:0000276
        if 'nucleic_acid_term_id' in d.keys():
            self.nucleic_acid_term_id = d['nucleic_acid_term_id']
        assert self.nucleic_acid_term_id in [u'SO:0000352', u'SO:0000356', u'SO:0000871', u'SO:0000276']
        # Nucleic acid starting quantity: The starting amount of nucleic acid before selection and purification.
        if 'nucleic_acid_starting_quantity' in d.keys():
            self.nucleic_acid_starting_quantity = d['nucleic_acid_starting_quantity']

class MouseDonor(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Littermates: Donors comprising the same litter.
        if 'littermates' in d.keys():
            self.littermates = []
            for t in d['littermates']:
                self.littermates.append(Donor(t, fetch=False))
        if 'organism' in d.keys():
            self.organism = d['organism']

class Organism(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Binomial name: The genus species for the organism (e.g. 'Mus musculus').
        if 'scientific_name' in d.keys():
            self.scientific_name = d['scientific_name']
        # Taxon ID: The NCBI taxon ID for the organism (e.g. 10090).
        if 'taxon_id' in d.keys():
            self.taxon_id = d['taxon_id']
        # Common name: A short unique name for the organism (e.g. 'mouse' or 'human').
        if 'name' in d.keys():
            self.name = d['name']

class Page(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Title: The name shown in the browser's title bar and tabs.
        if 'title' in d.keys():
            self.title = d['title']
        # Page Layout: Hierarchical description of the page layout.
        # Parent Page
            try:
                self.parent = d['parent']
            except ValueError:
                self.parent = None
        # URL Name: The name shown in this page's URL.
        if 'name' in d.keys():
            self.name = d['name']

class Platform(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # URL: An external resource with additional information about the measurement device.
        if 'url' in d.keys():
            self.url = d['url']
        # Platform ID: OBI (Ontology for Biomedical Investigations) ontology identifier for the measurement device.
        # NTR is a new term request identifier provided by the DCC.
        if 'term_id' in d.keys():
            self.term_id = d['term_id']
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Platform name: OBI (Ontology for Biomedical Investigations) ontology term for the measurement device.
        if 'term_name' in d.keys():
            self.term_name = d['term_name']

class Publication(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Title: Title of the publication or communication.
        if 'title' in d.keys():
            self.title = d['title']
        # Journal: The journal of the publication.
        if 'journal' in d.keys():
            self.journal = d['journal']
        # Data used
        if 'data_used' in d.keys():
            self.data_used = d['data_used']
        # Abstract: Abstract of the publication or communication.
        if 'abstract' in d.keys():
            self.abstract = d['abstract']
        # Volume: The volume of the publication.
        if 'volume' in d.keys():
            self.volume = d['volume']
        # Date published
        if 'date_published' in d.keys():
            self.date_published = d['date_published']
        # Published by
        if 'published_by' in d.keys():
            self.published_by = []
            for t in d['published_by']:
                self.published_by.append(t)
        # Date revised
        if 'date_revised' in d.keys():
            self.date_revised = d['date_revised']
        # Authors
        if 'authors' in d.keys():
            self.authors = d['authors']
        # Issue: The issue of the publication.
        if 'issue' in d.keys():
            self.issue = d['issue']
        # Page: Pagination of the reference
        if 'page' in d.keys():
            self.page = d['page']
        # Categories
        if 'categories' in d.keys():
            self.categories = []
            for t in d['categories']:
                self.categories.append(t)
        # Publication year
        if 'publication_year' in d.keys():
            self.publication_year = d['publication_year']

class Replicate(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Biological replicate: Data collection under the same methods using a different biological source, measuring the variability in the biological source.
        if 'biological_replicate_number' in d.keys():
            self.biological_replicate_number = int(d['biological_replicate_number'])
        # RBNS protein concentration units
        # The unit for the dependant rbns_protein_concentration.
        if 'rbns_protein_concentration_units' in d.keys():
            self.rbns_protein_concentration_units = d['rbns_protein_concentration_units']
        assert self.rbns_protein_concentration_units in [u'nM']
        # RBNS protein concentration: For use only with RNA Bind-n-Seq replicates to indicate the protein concentration.
        # Only for use with RBNS replicates.
        if 'rbns_protein_concentration' in d.keys():
            self.rbns_protein_concentration = int(d['rbns_protein_concentration'])
        # Read length units
        if 'read_length_units' in d.keys():
            self.read_length_units = d['read_length_units']
        assert self.read_length_units in [u'nt']
        # Read length: For high-throughput sequencing, the number of contiguous nucleotides determined by sequencing.
        # When submitting read length, must submit value for read length units.
        if 'read_length' in d.keys():
            self.read_length = int(d['read_length'])
        # Flowcells: For high-throughput sequencing, the flowcells used for the sequencing of the replicate.
        if 'flowcell_details' in d.keys():
            self.flowcell_details = []
            for t in d['flowcell_details']:
debug
                # Machine Name: The lab specific name of the machine used.
                if 'machine' in d.keys():
                    self.machine = d['machine']
debug
                # Lane
                if 'lane' in d.keys():
                    self.lane = d['lane']
debug
                # Barcode
                if 'barcode' in d.keys():
                    self.barcode = d['barcode']
debug
                # Flowcell ID
                if 'flowcell' in d.keys():
                    self.flowcell = d['flowcell']
        # Technical replicate: Data collection under the same methods using the same biological source, measuring the variability in the method.
        if 'technical_replicate_number' in d.keys():
            self.technical_replicate_number = int(d['technical_replicate_number'])
        # Platform: The measurement device used to collect data.
        # See platform.json for available identifiers.
        if 'platform' in d.keys():
            self.platform.append(Platform(t, fetch=False))
        # Paired-end sequencing: The utilization of sequencing both ends of the DNA fragment in a library.
        # Experiment: The experiment the replicate belongs to.
        # See experiment.json for available identifiers.
        if 'experiment' in d.keys():
            self.experiment.append(Experiment(t, fetch=False))
        # Library: The nucleic acid library used in this replicate.
        # See library.json for available identifiers.
        if 'library' in d.keys():
            self.library.append(Library(t, fetch=False))
        # Antibody: For Immunoprecipitation assays, the antibody used.
        # See antibody_lot.json for available identifiers.
        if 'antibody' in d.keys():
            self.antibody.append(AntibodyLot(t, fetch=False))

class RNAiVector(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Target sequence: Genomic sequence targeted by the RNA.
        if 'rnai_target_sequence' in d.keys():
            self.rnai_target_sequence = d['rnai_target_sequence']
        # RNAi documents: Documents that describe the RNAi construct.
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        # Target: The name of the gene whose expression or product is modified by the RNAi construct.
        # See target.json for available identifiers.
        if 'target' in d.keys():
            self.target.append(Target(t, fetch=False))
        # Class: The classification of the interfering RNA (e.g. shRNA or siRNA).
        if 'rnai_type' in d.keys():
            self.rnai_type = d['rnai_type']
        assert self.rnai_type in [u'shRNA', u'siRNA']
        # URL: An external resource with additional information about the RNAi construct.
        if 'url' in d.keys():
            self.url = d['url']
        # RNAi sequence: Sequence of the inhibitory RNA.
        if 'rnai_sequence' in d.keys():
            self.rnai_sequence = d['rnai_sequence']
        # Backbone name: The name of the vector backbone used for the construct.
        if 'vector_backbone_name' in d.keys():
            self.vector_backbone_name = d['vector_backbone_name']

class RNAiVectorCharacterization(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # RNAi characterized
        # See rnai.json for available identifiers.
        if 'characterizes' in d.keys():
            self.characterizes.append(RNAiVector(t, fetch=False))

class Software(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Name: Unique name of the software package, lower cased version of title.
        if 'name' in d.keys():
            self.name = d['name']
        # Title: The preferred viewable name of the software.
        if 'title' in d.keys():
            self.title = d['title']
        # URL: An external resource with additional information about the software.
        if 'url' in d.keys():
            self.url = d['url']
        # Used by project
        if 'used_by' in d.keys():
            self.used_by = []
            for t in d['used_by']:
                self.used_by.append(t)
        # Source URL: An external resource to the code base.
        if 'source_url' in d.keys():
            self.source_url = d['source_url']
        # References
        if 'references' in d.keys():
            self.references = []
            for t in d['references']:
                self.references.append(Publication(t, fetch=False))
        # Purpose in project: The purpose that the software was used for in the project.
        if 'purpose' in d.keys():
            self.purpose = []
            for t in d['purpose']:
                self.purpose.append(t)
        # Bug tracker URL: An external resource to track bugs for the software.
        if 'bug_tracker_url' in d.keys():
            self.bug_tracker_url = d['bug_tracker_url']
        # Types: The classification of the software
        if 'software_type' in d.keys():
            self.software_type = []
            for t in d['software_type']:
                self.software_type.append(t)
        # Description: A plain text description of the software.
        if 'description' in d.keys():
            self.description = d['description']

class Source(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # URL: An external resource with additional information about the source.
        if 'url' in d.keys():
            self.url = d['url']
        # Do not submit, value is auto generated from the title as lower cased and hyphen delimited.
        if 'name' in d.keys():
            self.name = d['name']
        # Description: A plain text description of the source.
        if 'description' in d.keys():
            self.description = d['description']
        # Name: The complete name of the originating lab or vendor. 
        if 'title' in d.keys():
            self.title = d['title']

class Target(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Common name with modification: Common name for the target including post-translational modifications, if any.
        # Submit the common name of the gene with modification (e.g. H3K4me3, eGFP-E2F1, or POLR2AphosphoS2).
        if 'label' in d.keys():
            self.label = d['label']
        # External identifiers: Unique identifiers from external resources (e.g. HGNC, GeneID, UniProtKB or ENSEMBL).
        if 'dbxref' in d.keys():
            self.dbxref = []
            for t in d['dbxref']:
                self.dbxref.append(t)
        # Organism: Organism bearing the target.
        # See organism.json for available identifiers.
        if 'organism' in d.keys():
            self.organism.append(Organism(t, fetch=False))
        # Gene name: HGNC or MGI identifier for the target.
        # Submit only the identifier (e.g. HMFN0395 or 22809).
        if 'gene_name' in d.keys():
            self.gene_name = d['gene_name']

class Treatment(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # External identifiers: Unique identifiers from external resources.
        if 'dbxrefs' in d.keys():
            self.dbxrefs = []
            for t in d['dbxrefs']:
                self.dbxrefs.append(t)
        # Term name: Ontology term describing a component in the treatment.
        if 'treatment_term_name' in d.keys():
            self.treatment_term_name = d['treatment_term_name']
        # Temperature
        # Term ID: Ontology identifier describing a component in the treatment.
        if 'treatment_term_id' in d.keys():
            self.treatment_term_id = d['treatment_term_id']
        # Type: The classification of the treatment.
        if 'treatment_type' in d.keys():
            self.treatment_type = d['treatment_type']
        assert self.treatment_type in [u'protein', u'chemical', u'exposure', u'infection']
        # Lab: Lab associated with the submission.
        # See lab.json for list of available identifiers.
        if 'lab' in d.keys():
            self.lab.append(Lab(t, fetch=False))
        # Duration
        # Duration units
        if 'duration_units' in d.keys():
            self.duration_units = d['duration_units']
        assert self.duration_units in [u'second', u'minute', u'hour', u'day']
        # Concentration units
        if 'concentration_units' in d.keys():
            self.concentration_units = d['concentration_units']
        assert self.concentration_units in [u'pM', u'nM', u'\u03bcM', u'\u03bcg/mL', u'mM', u'mg/mL', u'ng/mL', u'M', u'percent', u'units', u'U/mL']
        # Concentration
        # Protocol documents: Documents that describe the treatment protocol.
        if 'protocols' in d.keys():
            self.protocols = []
            for t in d['protocols']:
                self.protocols.append(Document(t, fetch=False))
        # Temperature units
        if 'temperature_units' in d.keys():
            self.temperature_units = d['temperature_units']
        assert self.temperature_units in [u'Celsius', u'Fahrenheit', u'Kelvin']

class User(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # First name: The user's first (given) name.
        if 'first_name' in d.keys():
            self.first_name = d['first_name']
        # Last name: The user's last (family) name.
        if 'last_name' in d.keys():
            self.last_name = d['last_name']
        # Submits for: Labs user is authorized to submit data for.
        if 'submits_for' in d.keys():
            self.submits_for = []
            for t in d['submits_for']:
                self.submits_for.append(Lab(t, fetch=False))
        # Primary phone number: The user's primary phone number (with country code).
        if 'phone1' in d.keys():
            self.phone1 = d['phone1']
        # Fax number: A FAX number for the user (with country code).
        if 'fax' in d.keys():
            self.fax = d['fax']
        # Affiliation: Lab user is primarily associated with.
        # See lab.json for available identifiers.
        if 'lab' in d.keys():
            self.lab.append(Lab(t, fetch=False))
        # Alternate phone number: The user's secondary phone number (with country code).
        if 'phone2' in d.keys():
            self.phone2 = d['phone2']
        # Google ID
        if 'google' in d.keys():
            self.google = d['google']
        # Groups: Additional access control groups
        if 'groups' in d.keys():
            self.groups = []
            for t in d['groups']:
                self.groups.append(t)
        # Skype ID
        if 'skype' in d.keys():
            self.skype = d['skype']
        # Timezone: The timezone the user is associated with.
        if 'timezone' in d.keys():
            self.timezone = d['timezone']
        assert self.timezone in [u'Africa/Abidjan', u'Africa/Accra', u'Africa/Addis_Ababa', u'Africa/Algiers', u'Africa/Asmara', u'Africa/Bamako', u'Africa/Bangui', u'Africa/Banjul', u'Africa/Bissau', u'Africa/Blantyre', u'Africa/Brazzaville', u'Africa/Bujumbura', u'Africa/Cairo', u'Africa/Casablanca', u'Africa/Ceuta', u'Africa/Conakry', u'Africa/Dakar', u'Africa/Dar_es_Salaam', u'Africa/Djibouti', u'Africa/Douala', u'Africa/El_Aaiun', u'Africa/Freetown', u'Africa/Gaborone', u'Africa/Harare', u'Africa/Johannesburg', u'Africa/Juba', u'Africa/Kampala', u'Africa/Khartoum', u'Africa/Kigali', u'Africa/Kinshasa', u'Africa/Lagos', u'Africa/Libreville', u'Africa/Lome', u'Africa/Luanda', u'Africa/Lubumbashi', u'Africa/Lusaka', u'Africa/Malabo', u'Africa/Maputo', u'Africa/Maseru', u'Africa/Mbabane', u'Africa/Mogadishu', u'Africa/Monrovia', u'Africa/Nairobi', u'Africa/Ndjamena', u'Africa/Niamey', u'Africa/Nouakchott', u'Africa/Ouagadougou', u'Africa/Porto-Novo', u'Africa/Sao_Tome', u'Africa/Tripoli', u'Africa/Tunis', u'Africa/Windhoek', u'America/Adak', u'America/Anchorage', u'America/Anguilla', u'America/Antigua', u'America/Araguaina', u'America/Argentina/Buenos_Aires', u'America/Argentina/Catamarca', u'America/Argentina/Cordoba', u'America/Argentina/Jujuy', u'America/Argentina/La_Rioja', u'America/Argentina/Mendoza', u'America/Argentina/Rio_Gallegos', u'America/Argentina/Salta', u'America/Argentina/San_Juan', u'America/Argentina/San_Luis', u'America/Argentina/Tucuman', u'America/Argentina/Ushuaia', u'America/Aruba', u'America/Asuncion', u'America/Atikokan', u'America/Bahia', u'America/Bahia_Banderas', u'America/Barbados', u'America/Belem', u'America/Belize', u'America/Blanc-Sablon', u'America/Boa_Vista', u'America/Bogota', u'America/Boise', u'America/Cambridge_Bay', u'America/Campo_Grande', u'America/Cancun', u'America/Caracas', u'America/Cayenne', u'America/Cayman', u'America/Chicago', u'America/Chihuahua', u'America/Costa_Rica', u'America/Creston', u'America/Cuiaba', u'America/Curacao', u'America/Danmarkshavn', u'America/Dawson', u'America/Dawson_Creek', u'America/Denver', u'America/Detroit', u'America/Dominica', u'America/Edmonton', u'America/Eirunepe', u'America/El_Salvador', u'America/Fortaleza', u'America/Glace_Bay', u'America/Godthab', u'America/Goose_Bay', u'America/Grand_Turk', u'America/Grenada', u'America/Guadeloupe', u'America/Guatemala', u'America/Guayaquil', u'America/Guyana', u'America/Halifax', u'America/Havana', u'America/Hermosillo', u'America/Indiana/Indianapolis', u'America/Indiana/Knox', u'America/Indiana/Marengo', u'America/Indiana/Petersburg', u'America/Indiana/Tell_City', u'America/Indiana/Vevay', u'America/Indiana/Vincennes', u'America/Indiana/Winamac', u'America/Inuvik', u'America/Iqaluit', u'America/Jamaica', u'America/Juneau', u'America/Kentucky/Louisville', u'America/Kentucky/Monticello', u'America/Kralendijk', u'America/La_Paz', u'America/Lima', u'America/Los_Angeles', u'America/Lower_Princes', u'America/Maceio', u'America/Managua', u'America/Manaus', u'America/Marigot', u'America/Martinique', u'America/Matamoros', u'America/Mazatlan', u'America/Menominee', u'America/Merida', u'America/Metlakatla', u'America/Mexico_City', u'America/Miquelon', u'America/Moncton', u'America/Monterrey', u'America/Montevideo', u'America/Montreal', u'America/Montserrat', u'America/Nassau', u'America/New_York', u'America/Nipigon', u'America/Nome', u'America/Noronha', u'America/North_Dakota/Beulah', u'America/North_Dakota/Center', u'America/North_Dakota/New_Salem', u'America/Ojinaga', u'America/Panama', u'America/Pangnirtung', u'America/Paramaribo', u'America/Phoenix', u'America/Port-au-Prince', u'America/Port_of_Spain', u'America/Porto_Velho', u'America/Puerto_Rico', u'America/Rainy_River', u'America/Rankin_Inlet', u'America/Recife', u'America/Regina', u'America/Resolute', u'America/Rio_Branco', u'America/Santa_Isabel', u'America/Santarem', u'America/Santiago', u'America/Santo_Domingo', u'America/Sao_Paulo', u'America/Scoresbysund', u'America/Shiprock', u'America/Sitka', u'America/St_Barthelemy', u'America/St_Johns', u'America/St_Kitts', u'America/St_Lucia', u'America/St_Thomas', u'America/St_Vincent', u'America/Swift_Current', u'America/Tegucigalpa', u'America/Thule', u'America/Thunder_Bay', u'America/Tijuana', u'America/Toronto', u'America/Tortola', u'America/Vancouver', u'America/Whitehorse', u'America/Winnipeg', u'America/Yakutat', u'America/Yellowknife', u'Antarctica/Casey', u'Antarctica/Davis', u'Antarctica/DumontDUrville', u'Antarctica/Macquarie', u'Antarctica/Mawson', u'Antarctica/McMurdo', u'Antarctica/Palmer', u'Antarctica/Rothera', u'Antarctica/South_Pole', u'Antarctica/Syowa', u'Antarctica/Vostok', u'Arctic/Longyearbyen', u'Asia/Aden', u'Asia/Almaty', u'Asia/Amman', u'Asia/Anadyr', u'Asia/Aqtau', u'Asia/Aqtobe', u'Asia/Ashgabat', u'Asia/Baghdad', u'Asia/Bahrain', u'Asia/Baku', u'Asia/Bangkok', u'Asia/Beirut', u'Asia/Bishkek', u'Asia/Brunei', u'Asia/Choibalsan', u'Asia/Chongqing', u'Asia/Colombo', u'Asia/Damascus', u'Asia/Dhaka', u'Asia/Dili', u'Asia/Dubai', u'Asia/Dushanbe', u'Asia/Gaza', u'Asia/Harbin', u'Asia/Hebron', u'Asia/Ho_Chi_Minh', u'Asia/Hong_Kong', u'Asia/Hovd', u'Asia/Irkutsk', u'Asia/Jakarta', u'Asia/Jayapura', u'Asia/Jerusalem', u'Asia/Kabul', u'Asia/Kamchatka', u'Asia/Karachi', u'Asia/Kashgar', u'Asia/Kathmandu', u'Asia/Khandyga', u'Asia/Kolkata', u'Asia/Krasnoyarsk', u'Asia/Kuala_Lumpur', u'Asia/Kuching', u'Asia/Kuwait', u'Asia/Macau', u'Asia/Magadan', u'Asia/Makassar', u'Asia/Manila', u'Asia/Muscat', u'Asia/Nicosia', u'Asia/Novokuznetsk', u'Asia/Novosibirsk', u'Asia/Omsk', u'Asia/Oral', u'Asia/Phnom_Penh', u'Asia/Pontianak', u'Asia/Pyongyang', u'Asia/Qatar', u'Asia/Qyzylorda', u'Asia/Rangoon', u'Asia/Riyadh', u'Asia/Sakhalin', u'Asia/Samarkand', u'Asia/Seoul', u'Asia/Shanghai', u'Asia/Singapore', u'Asia/Taipei', u'Asia/Tashkent', u'Asia/Tbilisi', u'Asia/Tehran', u'Asia/Thimphu', u'Asia/Tokyo', u'Asia/Ulaanbaatar', u'Asia/Urumqi', u'Asia/Ust-Nera', u'Asia/Vientiane', u'Asia/Vladivostok', u'Asia/Yakutsk', u'Asia/Yekaterinburg', u'Asia/Yerevan', u'Atlantic/Azores', u'Atlantic/Bermuda', u'Atlantic/Canary', u'Atlantic/Cape_Verde', u'Atlantic/Faroe', u'Atlantic/Madeira', u'Atlantic/Reykjavik', u'Atlantic/South_Georgia', u'Atlantic/St_Helena', u'Atlantic/Stanley', u'Australia/Adelaide', u'Australia/Brisbane', u'Australia/Broken_Hill', u'Australia/Currie', u'Australia/Darwin', u'Australia/Eucla', u'Australia/Hobart', u'Australia/Lindeman', u'Australia/Lord_Howe', u'Australia/Melbourne', u'Australia/Perth', u'Australia/Sydney', u'Canada/Atlantic', u'Canada/Central', u'Canada/Eastern', u'Canada/Mountain', u'Canada/Newfoundland', u'Canada/Pacific', u'Europe/Amsterdam', u'Europe/Andorra', u'Europe/Athens', u'Europe/Belgrade', u'Europe/Berlin', u'Europe/Bratislava', u'Europe/Brussels', u'Europe/Bucharest', u'Europe/Budapest', u'Europe/Busingen', u'Europe/Chisinau', u'Europe/Copenhagen', u'Europe/Dublin', u'Europe/Gibraltar', u'Europe/Guernsey', u'Europe/Helsinki', u'Europe/Isle_of_Man', u'Europe/Istanbul', u'Europe/Jersey', u'Europe/Kaliningrad', u'Europe/Kiev', u'Europe/Lisbon', u'Europe/Ljubljana', u'Europe/London', u'Europe/Luxembourg', u'Europe/Madrid', u'Europe/Malta', u'Europe/Mariehamn', u'Europe/Minsk', u'Europe/Monaco', u'Europe/Moscow', u'Europe/Oslo', u'Europe/Paris', u'Europe/Podgorica', u'Europe/Prague', u'Europe/Riga', u'Europe/Rome', u'Europe/Samara', u'Europe/San_Marino', u'Europe/Sarajevo', u'Europe/Simferopol', u'Europe/Skopje', u'Europe/Sofia', u'Europe/Stockholm', u'Europe/Tallinn', u'Europe/Tirane', u'Europe/Uzhgorod', u'Europe/Vaduz', u'Europe/Vatican', u'Europe/Vienna', u'Europe/Vilnius', u'Europe/Volgograd', u'Europe/Warsaw', u'Europe/Zagreb', u'Europe/Zaporozhye', u'Europe/Zurich', u'GMT', u'Indian/Antananarivo', u'Indian/Chagos', u'Indian/Christmas', u'Indian/Cocos', u'Indian/Comoro', u'Indian/Kerguelen', u'Indian/Mahe', u'Indian/Maldives', u'Indian/Mauritius', u'Indian/Mayotte', u'Indian/Reunion', u'Pacific/Apia', u'Pacific/Auckland', u'Pacific/Chatham', u'Pacific/Chuuk', u'Pacific/Easter', u'Pacific/Efate', u'Pacific/Enderbury', u'Pacific/Fakaofo', u'Pacific/Fiji', u'Pacific/Funafuti', u'Pacific/Galapagos', u'Pacific/Gambier', u'Pacific/Guadalcanal', u'Pacific/Guam', u'Pacific/Honolulu', u'Pacific/Johnston', u'Pacific/Kiritimati', u'Pacific/Kosrae', u'Pacific/Kwajalein', u'Pacific/Majuro', u'Pacific/Marquesas', u'Pacific/Midway', u'Pacific/Nauru', u'Pacific/Niue', u'Pacific/Norfolk', u'Pacific/Noumea', u'Pacific/Pago_Pago', u'Pacific/Palau', u'Pacific/Pitcairn', u'Pacific/Pohnpei', u'Pacific/Port_Moresby', u'Pacific/Rarotonga', u'Pacific/Saipan', u'Pacific/Tahiti', u'Pacific/Tarawa', u'Pacific/Tongatapu', u'Pacific/Wake', u'Pacific/Wallis', u'US/Alaska', u'US/Arizona', u'US/Central', u'US/Eastern', u'US/Hawaii', u'US/Mountain', u'US/Pacific', u'UTC']
        # Email
        if 'email' in d.keys():
            self.email = d['email']
        # Job title
        if 'job_title' in d.keys():
            self.job_title = d['job_title']

class WormDonor(EncodeObject):
    def __init__(self, accession, fetch=True):
        EncodeObject.__init__(self, accession)
        if fetch:
            self.fetch()

    def _populate(self):
        d = self.json_dict
        # Strain documents: Documents that describe the strain and its generation.
        if 'documents' in d.keys():
            self.documents = []
            for t in d['documents']:
                self.documents.append(Document(t, fetch=False))
        if 'organism' in d.keys():
            self.organism = d['organism']
        # The genotype of the strain according to accepted nomenclature conventions: http://www.wormbase.org/about/userguide/nomenclature#k89607hgcf24ea13jbid5--10.
        if 'genotype' in d.keys():
            self.genotype = d['genotype']
        # Number of times outcrossed: The number of out/backcrossed when constructing the strain
        if 'num_times_outcrossed' in d.keys():
            self.num_times_outcrossed = d['num_times_outcrossed']

