import FWCore.ParameterSet.Config as cms

def nanoProdCustomise_HTXS1(process):
    print 'Hello'
    process.HTXSCategoryTable.name = cms.string("HTXS-Xavier")
    return process

def nanoProdCustomise_HTXS2(process):
    print 'Hello 2'
    process.HTXSCategoryTable.name = cms.string("HTXS-Xavier-2")
    return process
