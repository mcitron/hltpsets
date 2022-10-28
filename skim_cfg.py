import FWCore.ParameterSet.Config as cms

process = cms.Process("SkimTrigger")

process.simpleTriggerFilter = cms.EDFilter('SimpleTriggerFilter',
    triggerString = cms.vstring("HLT_HT425","HLT_PFMET100_PFMHT100_IDTight_PFHT60","HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60","HLT_CaloMET90_NotCleaned",
	"HLT_CaloMET60_DTCluster50","HLT_L1MET_DTCluster50","HLT_CaloMET60_DTClusterNoMB1S50","HLT_L1MET_DTClusterNoMB1S50")
)
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/home/users/mcitron/tsgGenerationTemp/output.root'
    )
)
process.hltOutputMinimal = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "output_skim.root" ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( 'AOD' ),
        filterName = cms.untracked.string( '' )
    ),
     SelectEvents = cms.untracked.PSet(
		SelectEvents = cms.vstring('p')
		),
    outputCommands = cms.untracked.vstring( 'drop *', 'keep *_hltAK4CaloJetsCorrected_*_*', 'keep *_hltEcalRecHit_*_*',
	'keep *_hltDt1DRecHits_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep GlobalAlgBlkBXVector_*_*_*',                  
        'keep GlobalExtBlkBXVector_*_*_*',
        'keep l1tEGammaBXVector_*_EGamma_*',
        'keep l1tEtSumBXVector_*_EtSum_*',
        'keep l1tJetBXVector_*_Jet_*',
        'keep l1tMuonBXVector_*_Muon_*',
        'keep l1tTauBXVector_*_Tau_*',
    )
)

process.p = cms.Path(process.simpleTriggerFilter)
process.schedule = cms.Schedule(process.p)
process.MinimalOutput = cms.FinalPath(process.hltOutputMinimal)
process.schedule.append( process.MinimalOutput )
