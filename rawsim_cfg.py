# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename TSG-Run3Winter21DRMiniAOD-00179_1_cfg.py --eventcontent FEVTDEBUGHLT --pileup Flat_10_50_25ns --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW --fileout file:TSG-Run3Winter21DRMiniAOD-00179_0.root --pileup_input dbs:/MinBias_TuneCP5_14TeV-pythia8/Run3Winter21GS-112X_mcRun3_2021_realistic_v15-v1/GEN-SIM --conditions 112X_mcRun3_2021_realistic_v16 --customise_commands process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80) \n process.mix.input.nbPileupEvents.probValue = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784) --step DIGI,L1,DIGI2RAW,HLT:GRun --geometry DB:Extended --filein dbs:/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/Run3Winter21GS-112X_mcRun3_2021_realistic_v15-v2/GEN-SIM --era Run3 --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('HLT',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_Flat_10_50_25ns_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/182b4f9b-2a2c-4d89-8d2e-e67928fe052d.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/33793651-5986-40dd-9aff-a07b30f9373b.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/34f5efb3-98eb-4b1b-bd59-7177b81d3036.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/4098aae2-e1e1-45ca-949b-d4eab41397b4.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/4a9af89c-292e-4c53-8fdd-0eb76f419616.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/6481845c-eef2-45f8-93c2-a0c03b80c290.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/6a1fb942-420a-4092-ae5b-2e48565df2b5.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/758502e1-9817-4996-9281-8ebcfba3538c.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/be0e311b-096e-4ce3-8d40-a7eeb6b5f34e.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/e4f2c63f-174c-456a-8e7c-cd2deabc1cd6.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/eb695ed5-6089-48ad-ad8c-8cf2d34eaf2a.root', 
        '/store/mc/Run3Winter21GS/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV-pythia8/GEN-SIM/112X_mcRun3_2021_realistic_v15-v2/70000/fe082628-80d7-421a-9502-6bc656e2278f.root'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:TSG-Run3Winter21DRMiniAOD-00179_0.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_mcRun3_2021_realistic_v16', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80) 
process.mix.input.nbPileupEvents.probValue = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784,0.01960784)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion