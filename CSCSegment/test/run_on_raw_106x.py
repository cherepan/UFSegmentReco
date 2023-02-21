## Process real data  events with CSC rechit & segment builders - Tim Cox - 19.02.2015                      
## This version runs in 75X IBs on a 73X relval real data (run1) sample
##     -- USING DEFAULT ALGO "ST" 
## Run on  100  events of a SingleMu dataset

import FWCore.ParameterSet.Config as cms
from Configuration.AlCa.autoCond import autoCond

process = cms.Process("TEST")

## Accesses both Reco & Sim geometries from database
process.load("Configuration.StandardSequences.GeometryDB_cff")

## Use the magic of autoCond instead of an explicit global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = autoCond["run2_data"]

#process.GlobalTag.globaltag = "106X_dataRun2_v32"

process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")

# --- NUMBER OF EVENTS --- 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.options   = cms.untracked.PSet( SkipEvent = cms.untracked.vstring("ProductNotFound") )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


process.source    = cms.Source("PoolSource",
                               duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                               fileNames = cms.untracked.vstring(
                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/5FE6A215-7096-6B41-B499-D12FE193A89B.root'
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/A0AE2F0B-740C-B646-BF3B-58EE0943A261.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/7E66C6C3-7AEB-C048-8450-58BBD7E70343.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/2ACDF7AC-B65B-BB4C-915F-A0AF22098386.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/4C8FFD75-6243-8A4E-848E-ED14C0F8B9B2.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/F427E364-B84C-FA4D-9C5F-B1DF11176D71.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/7FD2532C-A050-DE47-B3CC-5D9FECA2312D.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/CC95D6CA-A6FE-D14B-98BF-77307ACFBCEE.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/A46A6EAF-311C-E248-8B44-FB8F13FDB3D5.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/D5A55C35-CF1A-664C-855C-0317C6F518A8.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/CA91E075-380C-2142-B047-0D214F6822B6.root',
#                                   '/store/data/Run2018B/SingleMuon/RAW-RECO/ZMu-12Nov2019_UL2018-v2/270003/5DC4A3AC-206C-CC4A-9FBB-7080182ECDDD.root'

                               )
                           )

#process.source    = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(
#  "/store/relval/CMSSW_7_3_0/SingleMu/RAW/GR_H_V43A_RelVal_zMu2012D-v1/00000/1ED9BE30-8481-E411-8AE9-002618943874.root"
#    )
                                   #)



# -- ACCESSING 'DEEP' PARAMETERS OF THE ALGO IS TRICKY
# THE FOLLOWING FOUND BY EXPLORING CONFIG WITH python -i
# '3' is 4th algo CSCSegAlgoST; '0' and '1' are for ST_ME1234 and ST_ME1A configs
#process.cscSegments.algo_psets[4].algo_psets[0].CSCDebug = cms.untracked.bool(True)
#process.cscSegments.algo_psets[4].algo_psets[1].CSCDebug = cms.untracked.bool(True)

from Configuration.DataProcessing.RecoTLR import customiseDataRun2Common

#call to customisation function customiseDataRun2Common imported from Configuration.DataProcessing.RecoTLR
process = customiseDataRun2Common(process)

# --- Activate LogVerbatim IN CSCSegment
process.MessageLogger.categories.append("CSCSegment")
process.MessageLogger.destinations = cms.untracked.vstring("cout")
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string("INFO"),
    default   = cms.untracked.PSet( limit = cms.untracked.int32(0)  ),
    FwkReport = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
    CSCSegment = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
)    

### --- ACTIVATE LogTrace IN VARIOUS MODULES - NEED TO COMPILE *EACH MODULE* WITH 
### scram b -j8 USER_CXXFLAGS="-DEDM_ML_DEBUG"
### LogTrace output goes to cout; all other output to "junk.log"

#process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.categories.append("CSCRecHit")
#process.MessageLogger.categories.append("CSCSegment")
#process.MessageLogger.categories.append("CSCSegAlgoST")

###  module label is something like "muonCSCDigis"...
#process.MessageLogger.debugModules = cms.untracked.vstring("*")
#process.MessageLogger.destinations = cms.untracked.vstring("cout","junk")
#process.MessageLogger.cout = cms.untracked.PSet(
#    threshold = cms.untracked.string("DEBUG"),
#    default   = cms.untracked.PSet( limit = cms.untracked.int32(0)  ),
#    FwkReport = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
#    CSCRecHit = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
#    CSCSegment = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
#  , CSCSegAlgoST = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
#)

# Path and EndPath def
process.unpack = cms.Path(process.muonCSCDigis)
process.reco = cms.Path(process.csc2DRecHits * process.cscSegments)
#process.reco = cms.Path(process.cscSegments)
process.endjob = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.unpack, process.reco, process.endjob)
