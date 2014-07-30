import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
    scriptName = cms.FileInPath("GeneratorInterface/LHEInterface/data/run_madgraph_gridpack.sh"),
    outputFile = cms.string("events_final.lhe"),
    args = cms.vstring('slc5_amd64_gcc472/13TeV/madgraph/V5_1.5.11/QCD_HT-100To250_13TeV-madgraph/v1',
    'QCD_HT-100To250_13TeV-madgraph','false','false','qcd','5','15','true','2','4'),
    nEvents = cms.uint32(100000)
)
