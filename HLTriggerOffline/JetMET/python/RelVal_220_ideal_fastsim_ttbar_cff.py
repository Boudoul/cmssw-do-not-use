import FWCore.ParameterSet.Config as cms

# maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/12327160-CEB9-DD11-BFB6-000423D9997E.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/543E3036-CDB9-DD11-AC27-0019DB2F3F9B.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/581C9369-CDB9-DD11-965C-000423D60FF6.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/8C54D5CE-CDB9-DD11-AA9F-000423D98844.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/B42CD5F6-CDB9-DD11-AEE8-001617DBD556.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/C48973D2-CDB9-DD11-9ACD-001617DBD5AC.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0000/F6F5F4D0-CDB9-DD11-8372-001617E30D0A.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/0ED39EAB-44BA-DD11-8060-000423D94534.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/124CC2F0-45BA-DD11-95DA-001617C3B78C.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/12ADDBF8-45BA-DD11-8C60-000423D94E70.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/14110D84-46BA-DD11-AA75-000423D174FE.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/1AC77127-46BA-DD11-BB0A-000423D999CA.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/204EBC27-46BA-DD11-A302-000423D987E0.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/2A98BA02-46BA-DD11-AFE4-000423D94E1C.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/2ADA50F8-45BA-DD11-AC4F-000423D94A04.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/3EEAEC2D-46BA-DD11-B2DB-000423D944FC.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/448F6573-46BA-DD11-8D70-000423D98AF0.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/4AD86704-46BA-DD11-AFE8-000423D98950.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/5849781F-46BA-DD11-AA29-001617C3B76E.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/741B1008-46BA-DD11-8D08-000423D9890C.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/743CBA5A-46BA-DD11-A720-000423D98B28.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/74F77327-46BA-DD11-9BA6-000423D98EC4.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/7A4E855E-46BA-DD11-9CDE-000423D33970.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/7AC70B2D-46BA-DD11-9A5B-000423D99264.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/88986E09-46BA-DD11-8504-000423D996C8.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/94AEDD63-46BA-DD11-8CAE-000423D98B5C.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/A855B706-46BA-DD11-BD8F-001617E30D00.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0001/FE467F24-46BA-DD11-A46B-000423D986C4.root',
       '/store/relval/CMSSW_2_2_0/RelValTTbar/GEN-SIM-DIGI-RECO/IDEAL_V9_FastSim_v3/0002/6AF387D0-FFBA-DD11-9B92-000423DD2F34.root'
       ] );


secFiles.extend( [
               ] )
