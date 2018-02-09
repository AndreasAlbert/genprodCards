#!/bin/bash

### settings to modify
# specify batch system 
BATCH=SGE # SGE LSF 
# number of jobs 
NJOBS=1
# number of events per job 
NEVTS=250 
# valiation output tag  
OTAG=dyfxfx_2p6
# name of shower fragment 
GRIDPACK=${WORKDIR}/dyellell012j_5f_NLO_FXFX_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#GENFRAGMENT=Hadronizer_TuneCUETP8M1_13TeV_MLM_5f_max4j_LHE_pythia8_cff # wjets/zjets
GENFRAGMENT=Hadronizer_TuneCUETP8M1_13TeV_aMCatNLO_FXFX_5f_max2j_max0p_LHE_pythia8_cff # zjets fxfx
#GENFRAGMENT=Hadronizer_TuneCUETP8M1_13TeV_aMCatNLO_FXFX_5f_max2j_max1p_LHE_pythia8_cff # ttbar fxfx 
# path for private fragments not yet in cmssw
FRAGMENTDIR=SOMENAME
# release setup 
SCRAM_ARCH=slc6_amd64_gcc630
RELEASE=CMSSW_9_3_3
# path to submit jobs 
WORKDIR=`pwd`
# path to store output files
ODIR=${WORKDIR}/samples/${OTAG}
### done with settings 


### create outputpath 
mkdir -p ${ODIR}


### setup release 
if [ -r ${WORKDIR}/${RELEASE}/src ] ; then 
    echo release ${RELEASE} already exists
else
    scram p CMSSW ${RELEASE}
fi
cd ${WORKDIR}/${RELEASE}/src
eval `scram runtime -sh`


### checkout generator configs 
git-cms-addpkg --quiet Configuration/Generator
cd ${CMSSW_BASE}/src/Configuration/Generator/python/ 


### copy additional fragments if needed 
if [ -d "${FRAGMENTDIR}" ]; then 
    cp ${FRAGMENTDIR}/*.py . 
fi


### check that fragments are available 
echo "Check that fragments are available ..."
if [ ! -s ${GENFRAGMENT}.py ] ; then 
    echo "... cannot find ${GENFRAGMENT}.py"
    exit 0;
else
    echo "... found required fragments!"
fi


### create generator fragment 
CONFIG=${OTAG}_cff.py
if [ -f ${CONFIG} ] ; then 
    rm ${CONFIG} 
fi

cat > ${CONFIG} <<EOF
import FWCore.ParameterSet.Config as cms
externalLHEProducer = cms.EDProducer('ExternalLHEProducer', 
args = cms.vstring('${GRIDPACK}'),
nEvents = cms.untracked.uint32(5000),
numberOfParameters = cms.uint32(1),  
outputFile = cms.string('cmsgrid_final.lhe'),
scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
EOF
cat ${GENFRAGMENT}.py >> ${CONFIG}


### scram release 
cd ${CMSSW_BASE}/src
scram b 

### make validation fragment 
cmsDriver.py Configuration/Generator/python/${CONFIG} \
    -n ${NEVTS} --mc --no_exec --python_filename cmsrun_${OTAG}.py \
    -s LHE,GEN,VALIDATION:genvalid_all --datatier GEN,GEN-SIM,DQMIO --eventcontent LHE,RAWSIM,DQM \
    --conditions auto:run2_mc_FULL --beamspot Realistic8TeVCollision 

mv cmsrun_${OTAG}.py ${CMSSW_BASE}/src/Configuration/Generator/python/cmsrun_${OTAG}.py 


### move to submission directory 
cd ${WORKDIR}


### prepare submission script 
cat > subscript_${OTAG}.sh <<EOF 
#!/bin/bash
pushd ${CMSSW_BASE}/src/
eval \`scram runtime -sh\`
popd
cp ${CMSSW_BASE}/src/Configuration/Generator/python/cmsrun_\${OTAG}.py . 
### adjust random numbers 
LINE=\`egrep -n Configuration.StandardSequences.Services_cff cmsrun_\${OTAG}.py | cut -d: -f1 \`
SEED=\`echo "5267+\${OFFSET}" | bc\`
sed -i "\${LINE}"aprocess.RandomNumberGeneratorService.generator.initialSeed=\${SEED} cmsrun_\${OTAG}.py  
SEED=\`echo "289634+\${OFFSET}" | bc\`
sed -i "\${LINE}"aprocess.RandomNumberGeneratorService.externalLHEProducer.initialSeed=\${SEED} cmsrun_\${OTAG}.py  
### run config 
cmsRun cmsrun_\${OTAG}.py 
### copy output 
cp *_inDQM.root \${ODIR}/\${OTAG}_\${OFFSET}.root 
EOF
# adjust rights 
chmod 755 subscript_${OTAG}.sh

### submit jobs 
IJOBS=1
while [ "${IJOBS}" -le "${NJOBS}" ]; do
    if [ ! -s ${ODIR}/${OTAG}_${IJOBS}.root ] ; then 
        # submit to sge system 
	if [ "${BATCH}" == "SGE" ] ; then  
	    qsub -N ${OTAG}_${IJOBS} -V -v OFFSET=${IJOBS} -v OTAG=${OTAG} -v ODIR=${ODIR} -j y -m as -o ${ODIR}/${OTAG}_${IJOBS}.out -S /bin/bash -l h_rt=12:00:00,h_vmem=6G,distro=sld6 subscript_${OTAG}.sh
        # submit to lsf system 
	elif [ "${BATCH}" == "LSF" ] ; then  
            #suppress lsf emails
	    export LSB_JOB_REPORT_MAIL="N"
	    bsub -o ${ODIR}/${OTAG}_${IJOBS}.out  -q 1nd -C 0  -R "rusage[mem=6000:pool=10000]" -env "all , OFFSET=${IJOBS} , OTAG=${OTAG} , ODIR=${ODIR}" subscript_${OTAG}.sh
       	# unknown batch mode 
	else 
	    echo "Unknown batch system!"
	    exit 0 
	fi
    fi
    IJOBS=$(($IJOBS+1))
done






