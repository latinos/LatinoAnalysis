#!/usr/bin/env python

'''
This is the same as jetmetHelperRun2 and it is needed to use Regrouped JEC and JER for FatJets
'''

import os, sys
import subprocess

from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.fatJetUncertainties import *

# JEC dict
jecTagsMC = {'2016' : 'Summer16_07Aug2017_V11_MC', 
             '2017' : 'Fall17_17Nov2017_V32_MC', 
             '2018' : 'Autumn18_V19_MC'}

jecTagsFastSim = {'2016' : 'Summer16_FastSimV1_MC',
                  '2017' : 'Fall17_FastSimV1_MC',
                  '2018' : 'Autumn18_FastSimV1_MC'}

archiveTagsDATA = {'2016' : 'Summer16_07Aug2017_V11_DATA', 
                   '2017' : 'Fall17_17Nov2017_V32_DATA', 
                   '2018' : 'Autumn18_V19_DATA'
                  }

jecTagsDATA = { '2016B' : 'Summer16_07Aug2017BCD_V11_DATA', 
                '2016C' : 'Summer16_07Aug2017BCD_V11_DATA', 
                '2016D' : 'Summer16_07Aug2017BCD_V11_DATA', 
                '2016E' : 'Summer16_07Aug2017EF_V11_DATA', 
                '2016F' : 'Summer16_07Aug2017EF_V11_DATA', 
                '2016G' : 'Summer16_07Aug2017GH_V11_DATA', 
                '2016H' : 'Summer16_07Aug2017GH_V11_DATA', 
                '2017B' : 'Fall17_17Nov2017B_V32_DATA', 
                '2017C' : 'Fall17_17Nov2017C_V32_DATA', 
                '2017D' : 'Fall17_17Nov2017DE_V32_DATA', 
                '2017E' : 'Fall17_17Nov2017DE_V32_DATA', 
                '2017F' : 'Fall17_17Nov2017F_V32_DATA', 
                '2018A' : 'Autumn18_RunA_V19_DATA',
                '2018B' : 'Autumn18_RunB_V19_DATA',
                '2018C' : 'Autumn18_RunC_V19_DATA',
                '2018D' : 'Autumn18_RunD_V19_DATA',
                } 

jerTagsMC = {'2016' : 'Summer16_25nsV1_MC',
             '2017' : 'Fall17_V3_MC',
             '2018' : 'Autumn18_V7_MC'
            }

#jet mass resolution: https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
#nominal, up, down
jmrValues = {'2016' : [1.0, 1.2, 0.8],
             '2017' : [1.09, 1.14, 1.04],
             '2018' : [1.24, 1.20, 1.28]
            }

#jet mass scale
#W-tagging PUPPI softdrop JMS values: https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
#2016 values 
jmsValues = { '2016' : [1.00, 0.9906, 1.0094], #nominal, down, up
              '2017' : [0.982, 0.978, 0.986],
              '2018' : [0.997, 0.993, 1.001]
            }

def createFatjetCorrector(globalTag, dataYear, jetType="AK8PFPuppi", isMC=True, jesUncert=["Total"], redojec=True, applySmearing=True, isFastSim=False):
    
    noGroom=False

    jerTag_ = jerTagsMC[dataYear] 

    jmrValues_ = jmrValues[dataYear]
    jmsValues_ = jmsValues[dataYear]

    archiveTag_ = archiveTagsDATA[dataYear]

    print 'Jet type=', jetType, 'JEC=', globalTag, '\t JER=', jerTag_

    jmeCorrections = None
    #jme corrections

    if isMC:
        jmeCorrections = lambda : fatJetUncertaintiesProducer(era=dataYear, globalTag=globalTag, 
                                                            jesUncertainties=jesUncert, redoJEC=redojec, 
                                                            jetType = jetType, jerTag=jerTag_, 
                                                            jmrVals = jmrValues_, jmsVals = jmsValues_, 
                                                            applySmearing = applySmearing)
    else:
        jmeCorrections = lambda : fatJetUncertaintiesProducer(era=dataYear, archive=archiveTag_, 
                                                            globalTag=globalTag, 
                                                            jesUncertainties=jesUncert, redoJEC=redojec, 
                                                            jetType = jetType, jerTag=jerTag_, 
                                                            jmrVals = jmrValues_, jmsVals = jmsValues_, 
                                                            isData=True)

    return jmeCorrections

