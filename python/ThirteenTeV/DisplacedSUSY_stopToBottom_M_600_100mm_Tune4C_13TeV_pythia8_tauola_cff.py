FLAVOR = 'stop'
COM_ENERGY = 13000. # GeV
MASS_POINT = 600   # GeV
CROSS_SECTION = 0.174599 # pb
CTAU_POINT = 100. # mm
PROCESS_FILE = 'SimG4Core/CustomPhysics/data/stophadronProcessList.txt'
PARTICLE_FILE = 'Configuration/Generator/data/particles_%s_%d_GeV.txt'  % (FLAVOR, MASS_POINT)
SLHA_FILE ='Configuration/Generator/data/DisplacedSUSY_%sToBottom_%d_%.1fmm_SLHA.spc' % (FLAVOR, MASS_POINT, CTAU_POINT)
PDT_FILE = 'Configuration/Generator/data/hscppythiapdt%s%d.tbl'  % (FLAVOR, MASS_POINT)
USE_REGGE = False

import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),
                         maxEventsToPrint = cms.untracked.int32(0),
                         SLHAFileForPythia8 = cms.string('%s' % SLHA_FILE), 
                         ExternalDecays = cms.PSet(
                             Tauola = cms.untracked.PSet(
                                 TauolaPolar,
                                 TauolaDefaultInputCards
                             ),
                             parameterSets = cms.vstring('Tauola')
                         ),
						 PythiaParameters = cms.PSet(
    processParameters = cms.vstring(
			  'Tune:pp  = 5',
			  'SUSY:all = off',
			  'SUSY:gg2squarkantisquark  = on',
			  'SUSY:qqbar2squarkantisquark= on',
			  'RHadrons:allow  = on',
			  'RHadrons:allowDecay = on',
			  'RHadrons:setMasses = on',
                          '1000006:tau0 = %.1f' % CTAU_POINT,
			  ),
    parameterSets = cms.vstring(
    'processParameters'
    )
    
    )
                         )
generator.hscpFlavor = cms.untracked.string(FLAVOR)
generator.massPoint = cms.untracked.int32(MASS_POINT)
generator.particleFile = cms.untracked.string(PARTICLE_FILE)
generator.slhaFile = cms.untracked.string(SLHA_FILE)
generator.processFile = cms.untracked.string(PROCESS_FILE)
generator.pdtFile = cms.FileInPath(PDT_FILE)
generator.useregge = cms.bool(USE_REGGE)

dirhadrongenfilter = cms.EDFilter("MCParticlePairFilter",
    #Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0., 0.),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(100., 100.),
    MinEta = cms.untracked.vdouble(-100, -100),
    ParticleCharge = cms.untracked.int32(0),
    ParticleID1 = cms.untracked.vint32(1000612,1000622,1000632,1000642,1000652,1006113,1006211,1006213,1006223,1006311,1006313,1006321,1006323,1006333),
    ParticleID2 = cms.untracked.vint32(1000612,1000622,1000632,1000642,1000652,1006113,1006211,1006213,1006223,1006311,1006313,1006321,1006323,1006333)
)

ProductionFilterSequence = cms.Sequence(generator*dirhadrongenfilter)
