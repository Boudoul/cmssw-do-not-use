import FWCore.ParameterSet.Config as cms

import sys
import os

# arguments
if (len(sys.argv)>2) :
    key=str(sys.argv[2])
else :
    key='Default'

process = cms.Process("L1ConfigWritePayloadDummy")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string('INFO')
process.MessageLogger.debugModules = cms.untracked.vstring('*')

# Generate dummy L1TriggerKeyList
process.load("CondTools.L1Trigger.L1TriggerKeyListDummy_cff")

# get 
process.load("CondTools.L1Trigger.L1TriggerKeyDummy_cff")
process.L1TriggerKeyDummy.objectKeys = cms.VPSet()
process.L1TriggerKeyDummy.label = cms.string('SubsystemKeysOnly')

# xxxKey = csctfKey, dttfKey, rpcKey, gmtKey, rctKey, gctKey, gtKey, or tsp0Key
process.L1TriggerKeyDummy.gctKey = cms.string(key)

# Subclass of L1ObjectKeysOnlineProdBase.
process.load("L1TriggerConfig.GctConfigProducers.L1GctRSObjectKeysOnline_cfi")
process.L1GctRSObjectKeysOnline.subsystemLabel = cms.string('')

# Get configuration data from OMDS.  This is the subclass of L1ConfigOnlineProdBase.
process.load("L1TriggerConfig.GctConfigProducers.L1GctChannelMaskOnline_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.getter1 = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(cms.PSet(
   record = cms.string('L1GctChannelMaskRcd'),
   data = cms.vstring('L1GctChannelMask')
   )),
   verbose = cms.untracked.bool(True)
)

process.p = cms.Path(
    process.getter1
)
