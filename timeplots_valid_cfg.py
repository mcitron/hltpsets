import FWCore.ParameterSet.Config as cms

process = cms.Process("Plots")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'file:tempOutput_RAW.root'
    )
)
# process.HLT_HT430_DelayedJet40_DoubleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","nCells"),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","emEnergy"),
#     triggerString = cms.string("HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless")
# )
# process.HLT_HT430_DelayedJet40_DoubleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","nCells"),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","emEnergy" ),
#     triggerString = cms.string("HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive")
# )
# process.HLT_HT430_DelayedJet40_SingleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtSingle" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","nCells" ),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","emEnergy" ),
#     triggerString = cms.string("HLT_HT430_DelayedJet40_SingleDelay1nsTrackless")
# )
process.triggerTimeAnalyser = cms.EDAnalyzer('DataTimePlotsAnalyzer',
    ClusterTag = cms.InputTag("cluster"),
    jets = cms.InputTag( "hltAK4CaloJetsCorrected" ),
    jetTimes = cms.InputTag( "jettime" ),
    jetCells = cms.InputTag( "jettime","jetCellsForTiming"),
    jetEmEnergy = cms.InputTag( "jettime","jetEcalEtForTiming"),
    triggerString = cms.string("HLT_HT430_DelayedJet40_SingleDelay2nsInclusive")
)
# process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPt" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","nCells"),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTiming","emEnergy"),
#     triggerString = cms.string("HLT_PFMET100_DelayedJet40_DoubleDelay1nsTrackless")
# )
# process.HLT_PFMET100_DelayedJet40_DoubleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducer" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","nCells" ),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingInclusive","emEnergy" ),
#     triggerString = cms.string("HLT_PFMET100_DelayedJet40_DoubleDelay1nsInclusive")
# )
# process.HLT_PFMET100_DelayedJet40_SingleDelay1nsTracklessPlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtSingle" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","nCells" ),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingle","emEnergy" ),
#     triggerString = cms.string("HLT_PFMET100_DelayedJet40_SingleDelay1nsTrackless")
# )
# process.HLT_PFMET100_DelayedJet40_SingleDelay1nsInclusivePlots = cms.EDAnalyzer('DataTimePlotsAnalyzer',
#     jets = cms.InputTag( "hltCentralCaloJetptLowPtCollectionProducerSingle" ),
#     jetTimes = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive" ),
#     jetCells = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","nCells" ),
#     jetEmEnergy = cms.InputTag( "hltDisplacedHLTCaloJetCollectionProducerLowPtTimingSingleInclusive","emEnergy" ),
#     triggerString = cms.string("HLT_PFMET100_DelayedJet40_SingleDelay1nsInclusive")
# )
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( "out.root" )
                                   )
# process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.p = cms.Path(process.triggerTimeAnalyser)
