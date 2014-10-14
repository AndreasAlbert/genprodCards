import FWCore.ParameterSet.Config as cms
import os

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('13TeV_gamgam_0j3incl_loop_200mgg500_50ptg13000_Minus2p8Eta2p8'),
  SherpackLocation = cms.string('slc6_amd64_gcc472/13TeV/sherpa/2.1.1/'),
  SherpackChecksum = cms.string('1aabde1513db5256cfdea3d31f8eb570'),
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
				" semihard xsec = 74.3594 mb,",
				" non-diffractive xsec = 18.1593 mb with nd factor = 0.335."
                                                  ),
                              Run = cms.vstring(
				"(run){",
				" EVENTS = 100;",
				" EVENT_MODE = HepMC;",
				" # avoid comix re-init after runcard modification",
				" WRITE_MAPPING_FILE 3;",
				"}(run)",
				"(beam){",
				" BEAM_1 = 2212; BEAM_ENERGY_1 = 6500.;",
				" BEAM_2 = 2212; BEAM_ENERGY_2 = 6500.;",
				"}(beam)",
				"(processes){",
				" Process 21 21 -> 22 22",
				" Scales VAR{Abs2(p[2]+p[3])}",
				" Loop_Generator gg_yy",
				" End process;",
				" Process 93 93 -> 22 22 93{3};",
				" Order_EW 2;",
				" Enhance_Factor 2 {3};",
				" Enhance_Factor 5 {4};",
				" Enhance_Factor 10 {5};",
				" CKKW sqr(20./E_CMS);",
				" Integration_Error 0.005 {3};",
				" Integration_Error 0.03 {4};",
				" Integration_Error 0.05 {5};",
				" End process;",
				"}(processes)",
				"(selector){",
				" Mass  22 22 200. 500.;",
				" PT 22 50. E_CMS;",
				" PseudoRapidity 22 -2.8 2.8;",
				"}(selector)",
				"(shower){",
				" CSS_EW_MODE = 1",
				"}(shower)",
				"(integration){",
				" FINISH_OPTIMIZATION = Off",
				"}(integration)",
				"(isr){",
				" PDF_LIBRARY     = LHAPDFSherpa",
				" PDF_SET         = CT10.LHgrid",
				" PDF_SET_VERSION = 0",
				" PDF_GRID_PATH   = PDFsets",
				"}(isr)",
				"(me){",
				" ME_SIGNAL_GENERATOR = Internal Comix",
				" EVENT_GENERATION_MODE = Unweighted;",
				"}(me)",
				"(mi){",
				" MI_HANDLER = Amisic  # None or Amisic",
				"}(mi)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

