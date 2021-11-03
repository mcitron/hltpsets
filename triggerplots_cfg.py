import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/home/users/mcitron/tsgGeneration/output.root'
    )
)
process.HLT_HT430_DelayedJet40_DoubleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","nCells"),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","emEnergy"),
    triggerString = cms.string("HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless")
)
process.HLT_HT430_DelayedJet40_DoubleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","nCells"),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","emEnergy" ),
    triggerString = cms.string("HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive")
)
process.HLT_HT430_DelayedJet40_SingleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtSingle" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","nCells" ),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","emEnergy" ),
    triggerString = cms.string("HLT_HT430_DelayedJet40_SingleDelay1nsTrackless")
)
process.HLT_HT430_DelayedJet40_SingleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducerSingle" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","nCells"),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","emEnergy"),
    triggerString = cms.string("HLT_HT430_DelayedJet40_SingleDelay1nsInclusive")
)
process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","nCells"),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","emEnergy"),
    triggerString = cms.string("HLT_PFMET100_DelayedJet40_DoubleDelay1nsTrackless")
)
process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","nCells" ),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","emEnergy" ),
    triggerString = cms.string("HLT_PFMET100_DelayedJet40_DoubleDelay1nsInclusive")
)
process.HLT_PFMET100_DelayedJet40_SingleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtSingle" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","nCells" ),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","emEnergy" ),
    triggerString = cms.string("HLT_PFMET100_DelayedJet40_SingleDelay1nsTrackless")
)
process.HLT_PFMET100_DelayedJet40_SingleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducerSingle" ),
    jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive" ),
    jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","nCells" ),
    jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","emEnergy" ),
    triggerString = cms.string("HLT_PFMET100_DelayedJet40_SingleDelay1nsInclusive")
)
process.HLT_L1MET_DTCluster50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterCollectionProducer" ),
    triggerString = cms.string("HLT_L1MET_DTCluster50")
)
process.HLT_CaloMET60_DTCluster50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterCollectionProducer" ),
    triggerString = cms.string("HLT_CaloMET60_DTCluster50")
)
process.HLT_PFMET100_DTCluster50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterCollectionProducer" ),
    triggerString = cms.string("HLT_PFMET100_DTCluster50")
)
process.HLT_PFMET100_DTClusterNoMB1S50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterNoMB1SCollectionProducer" ),
    triggerString = cms.string("HLT_PFMET100_DTClusterNoMB1S50")
)
process.HLT_HT430_DTCluster50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterCollectionProducer" ),
    triggerString = cms.string("HLT_HT430_DTCluster50")
)
process.HLT_HT430_DTClusterNoMB1S50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterNoMB1SCollectionProducer" ),
    triggerString = cms.string("HLT_HT430_DTClusterNoMB1S50")
)
process.HLT_L1MET_DTClusterNoMB1S50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterNoMB1SCollectionProducer" ),
    triggerString = cms.string("HLT_L1MET_DTClusterNoMB1S50")
)
process.HLT_CaloMET60_DTClusterNoMB1S50Plots = cms.EDAnalyzer('DTPlotsAnalyzer',
    dtClusters = cms.InputTag( "hltDisplacedHLTDTClusterNoMB1SCollectionProducer" ),
    triggerString = cms.string("HLT_CaloMET60_DTClusterNoMB1S50")
)
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( "out.root" )
                                   )
import FWCore.PythonUtilities.LumiList as LumiList
goldenjson="psets/json.txt"
lumilist = LumiList.LumiList(filename=goldenjson).getCMSSWString().split(',')
print("Found json list of lumis to process with {} lumi sections from {}".format(len(lumilist),goldenjson))
process.source.lumisToProcess = cms.untracked(cms.VLuminosityBlockRange()+lumilist)
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.p = cms.Path(process.HLT_HT430_DelayedJet40_DoubleDelay1nsTracklessPlots+process.HLT_HT430_DelayedJet40_DoubleDelay1nsInclusivePlots+process.HLT_HT430_DelayedJet40_SingleDelay1nsTracklessPlots+process.HLT_HT430_DelayedJet40_SingleDelay1nsInclusivePlots+process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsTracklessPlots+process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsInclusivePlots+process.HLT_PFMET100_DelayedJet40_SingleDelay1nsTracklessPlots+process.HLT_PFMET100_DelayedJet40_SingleDelay1nsInclusivePlots+process.HLT_L1MET_DTCluster50Plots+process.HLT_L1MET_DTClusterNoMB1S50Plots+process.HLT_CaloMET60_DTCluster50Plots+process.HLT_CaloMET60_DTClusterNoMB1S50Plots+process.HLT_PFMET100_DTCluster50Plots+process.HLT_PFMET100_DTClusterNoMB1S50Plots+process.HLT_HT430_DTCluster50Plots+process.HLT_HT430_DTClusterNoMB1S50Plots)
