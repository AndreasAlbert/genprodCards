import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('13TeV_eegamma_50Mee13000_400ptg13000_Minus3Eta3'),
  SherpackLocation = cms.string('slc6_amd64_gcc481/13TeV/sherpa/2.1.1/EXO_llgamma/'),
  SherpackChecksum = cms.string('ceb40e385a91fc5863598f69a7cfacca'),
  FetchSherpack = cms.bool(True),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 73.8879 mb,",
				" non-diffractive xsec = 18.1593 mb with nd factor = 0.335."
                                                  ),
                              Run = cms.vstring(
				"(run){",
				" EVENTS = 100;",
				" EVENT_MODE = HepMC;",
				" HEPMC2_GENEVENT_OUTPUT = hepmc;",
				" # avoid comix re-init after runcard modification",
				" WRITE_MAPPING_FILE 3;",
				"}(run)",
				"(beam){",
				" BEAM_1 = 2212; BEAM_ENERGY_1 = 6500.;",
				" BEAM_2 = 2212; BEAM_ENERGY_2 = 6500.;",
				"}(beam)",
				"(processes){",
				" Process 93 93 -> 11 -11 22;",
				" Order_EW 3;",
				" CKKW sqr(20./E_CMS);",
				" Print_Graphs MyGraphs;",
				" # Integration_Error 0.01;",
				" End process;",
				"}(processes)",
				"(selector){",
				" Mass 11 -11 50 E_CMS;",
				" PT 22 400. E_CMS;",
				" # PT 11 50. E_CMS;",
				" # PT -11 50. E_CMS;",
				" PseudoRapidity 22 -3.0 3.0;",
				" PseudoRapidity 11 -3.0 3.0;",
				" PseudoRapidity -11 -3.0 3.0;",
				" DeltaR 22 11 0.6 100000",
				" DeltaR 22 -11 0.6 100000",
				"}(selector)",
				"(shower){",
				" CSS_EW_MODE = 1",
				"}(shower)",
				"(integration){",
				" FINISH_OPTIMIZATION = Off",
				"}(integration)",
				"(isr){",
				" PDF_LIBRARY     = LHAPDFSherpa",
				" PDF_SET         = CT10",
				" PDF_SET_VERSION = 0",
				" # PDF_GRID_PATH   = PDFsets",
				"}(isr)",
				"(me){",
				" # ME_SIGNAL_GENERATOR = Internal Comix",
				" ME_SIGNAL_GENERATOR = Amegic",
				" EVENT_GENERATION_MODE = Unweighted;",
				"}(me)",
				"(mi){",
				" MI_HANDLER = Amisic  # None or Amisic",
				"}(mi)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

