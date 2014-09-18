import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(3.495e+06),
	filterEfficiency = cms.untracked.double(0.01225),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		processParameters = cms.vstring(
			'Main:timesAllowErrors    = 10000',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tau0Max = 10',
			'HardQCD:all = on',
			'PhaseSpace:pTHatMin = 80',
			'PhaseSpace:pTHatMax = 170',
			'Tune:pp 5',
			'Tune:ee 3',

		),
		parameterSets = cms.vstring('processParameters')
	)
)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)

bctoefilter = cms.EDFilter("BCToEFilter",
                           filterAlgoPSet = cms.PSet(eTThreshold = cms.double(10),
                                                     genParSource = cms.InputTag("genParticlesForFilter")
                                                     )
                           )
    
configurationMetadata = cms.untracked.PSet(
       version = cms.untracked.string('\$Revision$'),
       name = cms.untracked.string('\$Source$'),
       annotation = cms.untracked.string('b/c->e filtered QCD pthat 80-170 GeV, 14 TeV, Tune4C')
)

# add your filters to this sequence
ProductionFilterSequence = cms.Sequence(generator * (genParticlesForFilter + bctoefilter ))
