#!/bin/bash

OUTPUTDIR=$1
OUTPUTNAME=$2
INPUTFILENAMES=$3
IFILE=$4
CMSSWVERSION=$5
SCRAMARCH=$6

# Make sure OUTPUTNAME doesn't have .root since we add it manually
OUTPUTNAME=$(echo $OUTPUTNAME | sed 's/\.root//')

export SCRAM_ARCH=${SCRAMARCH}

function getjobad {
    grep -i "^$1" "$_CONDOR_JOB_AD" | cut -d= -f2- | xargs echo
}

function setup_chirp {
    if [ -e ./condor_chirp ]; then
    # Note, in the home directory
        mkdir chirpdir
        mv condor_chirp chirpdir/
        export PATH="$PATH:$(pwd)/chirpdir"
        echo "[chirp] Found and put condor_chirp into $(pwd)/chirpdir"
    elif [ -e /usr/libexec/condor/condor_chirp ]; then
        export PATH="$PATH:/usr/libexec/condor"
        echo "[chirp] Found condor_chirp in /usr/libexec/condor"
    else
        echo "[chirp] No condor_chirp :("
    fi
}

function chirp {
    # Note, $1 (the classad name) must start with Chirp
    condor_chirp set_job_attr_delayed $1 $2
    ret=$?
    echo "[chirp] Chirped $1 => $2 with exit code $ret"
}

function stageout {
    COPY_SRC=$1
    COPY_DEST=$2
    retries=0
    COPY_STATUS=1
    until [ $retries -ge 3 ]
    do
        echo "Stageout attempt $((retries+1)): env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 7200 --verbose --checksum ADLER32 ${COPY_SRC} ${COPY_DEST}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 7200 --verbose --checksum ADLER32 ${COPY_SRC} ${COPY_DEST}
        COPY_STATUS=$?
        if [ $COPY_STATUS -ne 0 ]; then
            echo "Failed stageout attempt $((retries+1))"
        else
            echo "Successful stageout with $retries retries"
            break
        fi
        retries=$[$retries+1]
        echo "Sleeping for 30m"
        sleep 30m
    done
    if [ $COPY_STATUS -ne 0 ]; then
        echo "Removing output file because gfal-copy crashed with code $COPY_STATUS"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-rm --verbose ${COPY_DEST}
        REMOVE_STATUS=$?
        if [ $REMOVE_STATUS -ne 0 ]; then
            echo "Uhh, gfal-copy crashed and then the gfal-rm also crashed with code $REMOVE_STATUS"
            echo "You probably have a corrupt file sitting on hadoop now."
            exit 1
        fi
    fi
}

function setup_environment {
    if [ -r "$OSGVO_CMSSW_Path"/cmsset_default.sh ]; then
        echo "sourcing environment: source $OSGVO_CMSSW_Path/cmsset_default.sh"
        source "$OSGVO_CMSSW_Path"/cmsset_default.sh
    elif [ -r "$OSG_APP"/cmssoft/cms/cmsset_default.sh ]; then
        echo "sourcing environment: source $OSG_APP/cmssoft/cms/cmsset_default.sh"
        source "$OSG_APP"/cmssoft/cms/cmsset_default.sh
    elif [ -r /cvmfs/cms.cern.ch/cmsset_default.sh ]; then
        echo "sourcing environment: source /cvmfs/cms.cern.ch/cmsset_default.sh"
        source /cvmfs/cms.cern.ch/cmsset_default.sh
    else
        echo "ERROR! Couldn't find $OSGVO_CMSSW_Path/cmsset_default.sh or /cvmfs/cms.cern.ch/cmsset_default.sh or $OSG_APP/cmssoft/cms/cmsset_default.sh"
        exit 1
    fi
}

function setup_cmssw {
  CMSSW=$1
  export SCRAM_ARCH=$2
  scram p CMSSW $CMSSW
  cd $CMSSW
  eval $(scramv1 runtime -sh)
  cd -
}

function edit_psets {
    nevents=-1
    # recosim
    echo "process.maxEvents.input = $nevents" >> $recosimcfg
    if [ "$INPUTFILENAMES" != "dummyfile" ]; then 
        echo "process.source.fileNames = cms.untracked.vstring([" >> $recosimcfg
        for INPUTFILENAME in $(echo "$INPUTFILENAMES" | sed -n 1'p' | tr ',' '\n'); do
            INPUTFILENAME=$(echo $INPUTFILENAME | sed 's|^/hadoop/cms||')
            echo "\"${INPUTFILENAME}\"," >> $recosimcfg
        done
        echo "])" >> $recosimcfg
    fi
    echo "process.RECOSIMoutput.fileName = \"file:output_recosim.root\"" >> $recosimcfg

    # hltstep
    echo "process.maxEvents.input = $nevents" >> $hltcfg
    echo "process.source.fileNames = [\"file:output_recosim.root\"]" >> $hltcfg
    echo "process.RAWSIMoutput.fileName = cms.untracked.string(\"file:output_hlt.root\")" >> $hltcfg
    # echo "_customInfo['inputFile' ]=  [\"file:output_recosim.root\"]" >> $hltcfg
    # echo "process.hltOutputFull.fileName = cms.untracked.string(\"file:output_hlt.root\")" >> $hltcfg
    # echo "process = customizeHLTforAll(process,\"GRun\",_customInfo)" >> $hltcfg
    # echo "process = customizeHLTforCMSSW(process,\"GRun\")" >> $hltcfg
    # echo "modifyHLTforEras(process)" >> $hltcfg

    # darktime
    echo "process.maxEvents.input = $nevents" >> $darktimecfg
    echo "process.source.fileNames = [\"file:output_hlt.root\"]" >> $darktimecfg
    echo "process.TFileService.fileName = \"file:${OUTPUTNAME}.root\"" >> $darktimecfg

    # triggerplots
    echo "process.maxEvents.input = $nevents" >> $triggerplotscfg
    echo "process.source.fileNames = [\"file:output_hlt.root\"]" >> $triggerplotscfg
    echo "process.TFileService.fileName = \"file:${OUTPUTNAME}_plots.root\"" >> $triggerplotscfg

}

function setup_hltdarktime {
    pushd .
    export SCRAM_ARCH=slc7_amd64_gcc900
    cd CMSSW_11_3_2/src
    eval `scramv1 runtime -sh`
    scramv1 b ProjectRename
    eval `scramv1 runtime -sh`
    popd
}
# function setup_hltdarktime {
#     pushd .
#     cp -r lib bin python CMSSW_12_0_0_pre2
#     popd
# }



echo -e "\n--- begin header output ---\n" #                     <----- section division
echo "OUTPUTDIR: $OUTPUTDIR"
echo "OUTPUTNAME: $OUTPUTNAME"
echo "INPUTFILENAMES: $INPUTFILENAMES"
echo "IFILE: $IFILE"
echo "CMSSWVERSION: $CMSSWVERSION"
echo "SCRAMARCH: $SCRAMARCH"

echo "GLIDEIN_CMSSite: $GLIDEIN_CMSSite"
echo "hostname: $(hostname)"
echo "uname -a: $(uname -a)"
echo "time: $(date +%s)"
echo "args: $@"
echo "tag: $(getjobad tag)"
echo "taskname: $(getjobad taskname)"

echo -e "\n--- end header output ---\n" #                       <----- section division

recosimcfg="psets/recosim_cfg.py"
hltcfg="psets/hlt_cfg_metisr.py"
darktimecfg="psets/darktime_cfg.py"
triggerplotscfg="psets/triggerplots_cfg.py"

setup_chirp
setup_environment

ls . 

# Make temporary directory to keep original dir clean
# Go inside and extract the package tarball
mkdir temp
cd temp
cp ../*.gz .
# cp ../*.xml .
tar xf *.gz

ls .

edit_psets 

echo "before running: ls -lrth"
ls -lrth

echo -e "\n--- begin running ---\n" #                           <----- section division

chirp ChirpMetisStatus "before_cmsRun"

setup_cmssw CMSSW_11_2_2_patch1 slc7_amd64_gcc900
cmsRun $recosimcfg
# setup_cmssw CMSSW_12_0_0_pre2 slc7_amd64_gcc900 
setup_hltdarktime
cmsRun $hltcfg
cmsRun $darktimecfg
CMSRUN_STATUS=$?

chirp ChirpMetisStatus "after_cmsRun"

echo "after running: ls -lrth"
ls -lrth

if [[ $CMSRUN_STATUS != 0 ]]; then
    echo "Removing output file because cmsRun crashed with exit code $?"
    rm ${OUTPUTNAME}.root
    exit 1
fi

cmsRun $triggerplotscfg

if [[ $CMSRUN_STATUS != 0 ]]; then
    echo "Removing output file because cmsRun for plots crashed with exit code $?"
    rm ${OUTPUTNAME}_plots.root
    exit 1
fi

echo -e "\n--- end running ---\n" #                             <----- section division

echo -e "\n--- begin copying output ---\n" #                    <----- section division

echo "Sending output file $OUTPUTNAME.root"

if [ ! -e "$OUTPUTNAME.root" ]; then
    echo "ERROR! Output $OUTPUTNAME.root doesn't exist"
    exit 1
fi

if [ ! -e "${OUTPUTNAME}_plots.root" ]; then
    echo "ERROR! Output ${OUTPUTNAME}_plots.root doesn't exist"
    exit 1
fi

echo "time before copy: $(date +%s)"
chirp ChirpMetisStatus "before_copy"

COPY_SRC="file://`pwd`/${OUTPUTNAME}.root"
COPY_DEST="gsiftp://gftp.t2.ucsd.edu${OUTPUTDIR}/${OUTPUTNAME}_${IFILE}.root"
stageout $COPY_SRC $COPY_DEST

COPY_SRC="file://`pwd`/${OUTPUTNAME}_plots.root"
COPY_DEST="gsiftp://gftp.t2.ucsd.edu${OUTPUTDIR}/${OUTPUTNAME}_plots_${IFILE}.root"
stageout $COPY_SRC $COPY_DEST

# COPY_SRC="file://`pwd`/output_gensim.root"
# COPY_DEST="gsiftp://gftp.t2.ucsd.edu${OUTPUTDIR}/gensim/output_${IFILE}.root"
# stageout $COPY_SRC $COPY_DEST

echo -e "\n--- end copying output ---\n" #                      <----- section division

echo "time at end: $(date +%s)"

chirp ChirpMetisStatus "done"

