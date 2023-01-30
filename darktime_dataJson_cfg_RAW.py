import FWCore.ParameterSet.Config as cms
import os
topDir = os.getenv("CMSSW_BASE")+"/src/darktime/"
jsons = {}
jsons["2016"] = topDir+"Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
jsons["2017"] = topDir+"Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
jsons["2018"] = topDir+"Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
jsons["2022C"] =topDir+"Cert_Collisions2022_eraC_355862_357482_Golden.json" 
jsons["2022D"] =topDir+"Cert_Collisions2022_eraD_357538_357900_Golden.json" 
jsons["2022E"] =topDir+"Cert_Collisions2022_eraE_359022_360331_Golden.json" 
jsons["2022F"] =topDir+"Cert_Collisions2022_eraF_360390_362167_Golden.json" 
jsons["2022G"] =topDir+"Cert_Collisions2022_eraG_362433_362760_Golden.json" 

process = cms.Process("Demo")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi");
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi");
process.load("Geometry.CaloEventSetup.CaloTopology_cfi");
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = '124X_dataRun3_Prompt_v4'
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing ('analysis')
options.outputFile = 'dataRun3.root'
options.inputFiles = [
        # 'file:/home/users/mcitron/tsgGeneration/CMSSW_12_0_0_pre2/src/triggerOutputClean.root'
      '/store/data/Run2022D/DisplacedJet/AOD/EXODelayedJet-PromptReco-v2/000/357/734/00000/14e800f8-9d6c-4c4c-9e9d-755a79771393.root'
]
options.maxEvents = 2000
options.register ('era',
                  "2022D", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "ERA")

options.parseArguments()


process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        options.inputFiles
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_25/src/ecalTiming/QCDGen5_1000_1500_AOD.root'
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/T1qqqqLL10000/T1qqqqLL1000_AOD_all_10000.root',
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/T1qqqqLL1000/T1qqqqLL1000_AOD_500To999.root',
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/T1qqqqLL1000/T1qqqqLL1000_AOD_200.root',
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/T1qqqqLL1000/T1qqqqLL1000_AOD_200To500.root'
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/T1qqqqLL0p001/T1qqqqLL1000_AOD_all_0p001.root'
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_27/src/ecalTiming/tempT1qqqqLL1000_AOD_all_10000.root'
        # 'file:/vols/build/cms/mc3909/timingCMSSW/CMSSW_8_0_25/src/dataFiles/2017_04_13_16_39_PRnewco_80X_dataRun2_2016LegacyRepro_v3-v1.root'
        #'file:/vols/build/cms/mc3909/qcdAODSIM.root'
    )
)
from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
# process.jec = cms.ESSource('PoolDBESSource',
#     CondDBSetup,
#     connect = cms.string('sqlite:Autumn18_V3_MC.db'),
#     toGet = cms.VPSet(
#         cms.PSet(
#             record = cms.string('JetCorrectionsRecord'),
#             tag    = cms.string('JetCorrectorParametersCollection_Autumn18_V3_MC_AK4PFchs'),
#             label  = cms.untracked.string('AK4PFchs')
#         ),
#         cms.PSet(
#             record = cms.string('JetCorrectionsRecord'),
#             tag    = cms.string('JetCorrectorParametersCollection_Autumn18_V3_MC_AK4PF'),
#             label  = cms.untracked.string('AK4PF')
#         ),
#     )
# )
# process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')


process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

cleaningAlgoConfig = cms.PSet(
        # apply cleaning in EB above this threshold in GeV  
        cThreshold_barrel=cms.double(4),
        # apply cleaning in EE above this threshold in GeV 
        cThreshold_endcap=cms.double(15),
        # mark spike in EB if e4e1 <  e4e1_a_barrel_ * log10(e) + e4e1_b_barrel_
        e4e1_a_barrel=cms.double(0.02),
        e4e1_b_barrel=cms.double(0.02),
        # ditto for EE
        e4e1_a_endcap=cms.double(0.02),
        e4e1_b_endcap=cms.double(-0.0125),

        #when calculating e4/e1, ignore hits below this threshold
        e4e1Threshold_barrel= cms.double(0.080),
        e4e1Threshold_endcap= cms.double(0.300),

        # near cracks raise the energy threshold by this factor
        tightenCrack_e1_single=cms.double(1),
        # near cracks, divide the e4e1 threshold by this factor
        tightenCrack_e4e1_single=cms.double(2.5),
        # same as above for double spike
        tightenCrack_e1_double=cms.double(2),
        tightenCrack_e6e2_double=cms.double(3),
        # consider for double spikes if above this threshold
        cThreshold_double =cms.double(10),
        # mark double spike if e6e2< e6e2thresh
        e6e2thresh=cms.double(0.04),
        # ignore rechits flagged kOutOfTime above this energy threshold in EB
        ignoreOutOfTimeThresh=cms.double(1e9)
        )
process.demo = cms.EDAnalyzer('DarkTimeAnalyzer',
                    data=cms.untracked.bool(False),
                    skimMet=cms.untracked.bool(False),
                    addCaloCellBranches=cms.untracked.bool(False),
                    addTowerBranches=cms.untracked.bool(False),
                    era = cms.untracked.string(""),
                    cleaningConfig = cleaningAlgoConfig,
                    barrelJets = cms.untracked.bool(True),
                    endcapJets = cms.untracked.bool(False),
		    dataTier = cms.untracked.string("RAW"),
		    triggerProcess = cms.untracked.string("HLT"),
                   )

process.demo.data=True
process.demo.era=options.era
# autoFindEra = True
# if autoFindEra:
#     process.demo.era = process.source.fileNames.value()[0].split("Run")[1].split("/")[0]

import FWCore.PythonUtilities.LumiList as LumiList
goldenjson = jsons[process.demo.era.value()]
lumilist = LumiList.LumiList(filename=goldenjson).getCMSSWString().split(',')
print("Found json list of lumis to process with {} lumi sections from {}".format(len(lumilist),goldenjson))
process.source.lumisToProcess = cms.untracked(cms.VLuminosityBlockRange()+lumilist)

process.demo.addCaloCellBranches=False
if process.demo.addCaloCellBranches:
    print ("WARNING add calo cell bool is true - tree will be very large!")

process.TFileService = cms.Service("TFileService",
                                               fileName = cms.string(options.outputFile)
                                                                                  )

# process.p = cms.Path(process.demo)
process.p = cms.Path(process.ak4PFL1FastL2L3CorrectorChain+process.ak4PFL1FastL2L3ResidualCorrectorChain+process.demo)

