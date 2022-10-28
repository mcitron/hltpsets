import FWCore.ParameterSet.Config as cms

process = cms.Process("JETTIME")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi");
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi");
process.load("Geometry.CaloEventSetup.CaloTopology_cfi");
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'/store/user/mcitron/ProjectMetis/ZeroBias18_Run2022B-v1_RAW_v7_run3BDataValid_updateCfgSkimAddDT/output_1930.root'
	# 'file:/ceph/cms//store/user/mcitron/ProjectMetis/ZeroBias0_Run2022B-v1_RAW_v2_run3BDataValid/output_1.root'
    )
)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = '124X_dataRun3_HLT_v4'

process.jettime = cms.EDProducer('HLTCaloJetTimingProducer',
    jets = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    barrelJets = cms.bool(True),
)
process.cluster = cms.EDProducer( "DTrechitClusterProducer",
    nRechitMin = cms.int32( 50 ),
    rParam = cms.double( 0.4 ),
    nStationThres = cms.int32( 10 ),
    recHitLabel = cms.InputTag( "hltDt1DRecHits" )
)

# process.caloTimingTestFilter = cms.EDFilter('HLTJetTimingFilter',
#     saveTags = cms.bool( True ),
# )
process.output = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "./tempOutput_RAW.root" ),
    outputCommands = cms.untracked.vstring('keep *','drop *_hltDt1DRecHits_*_*','drop *_hltEcalRecHit_*_*', 'drop *_*_*_HLT', 'drop *_hltGtStage2Digis_*_*','drop *_hltGtStage2ObjectMap_*_*')
    # outputCommands = cms.untracked.vstring('keep *')
    # outputCommands = cms.untracked.vstring( 'drop *','keep *_hltAK4CaloJetsCorrected_*_*','keep *_*_*_JETTIME' )
    )
# process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')

process.p = cms.Path(process.jettime+process.cluster)
process.Output = cms.EndPath(process.output)
