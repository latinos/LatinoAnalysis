# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import ElectronWP
from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import MuonWP

formulas = {}

# from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2018
METFilter_Common = '(event.Flag_goodVertices*\
                     event.Flag_globalSuperTightHalo2016Filter*\
                     event.Flag_HBHENoiseFilter*\
                     event.Flag_HBHENoiseIsoFilter*\
                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
                     event.Flag_BadPFMuonFilter*\
                     event.Flag_ecalBadCalibFilterV2\
                   )'

METFilter_DATA   =  METFilter_Common 

formulas['METFilter_MC'] = METFilter_DATA

# Common Weights


formulas['XSWeight'] = 'event.baseW*\
                        event.genWeight \
                        if hasattr(event, \'genWeight\') else event.baseW'


# Lepton WP
muWPlist = [wp for wp in MuonWP['Full2018v7']['TightObjWP']]
eleWPlist = [wp for wp in ElectronWP['Full2018v7']['TightObjWP']]

for eleWP in eleWPlist:
  for muWP in muWPlist:

    formulas['LepCut2l__ele_'+eleWP+'__mu_'+muWP] = '((event.Lepton_isTightElectron_'+eleWP+'[0]>0.5 or event.Lepton_isTightMuon_'+muWP+'[0]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[1]>0.5 or event.Lepton_isTightMuon_'+muWP+'[1]>0.5)) \
                                                     if event.nLepton > 1 else 0.'
  
    formulas['LepCut3l__ele_'+eleWP+'__mu_'+muWP] = '((event.Lepton_isTightElectron_'+eleWP+'[0]>0.5 or event.Lepton_isTightMuon_'+muWP+'[0]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[1]>0.5 or event.Lepton_isTightMuon_'+muWP+'[1]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[2]>0.5 or event.Lepton_isTightMuon_'+muWP+'[2]>0.5)) \
                                                     if event.nLepton > 2 else 0.'
  
    formulas['LepCut4l__ele_'+eleWP+'__mu_'+muWP] = '((event.Lepton_isTightElectron_'+eleWP+'[0]>0.5 or event.Lepton_isTightMuon_'+muWP+'[0]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[1]>0.5 or event.Lepton_isTightMuon_'+muWP+'[1]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[2]>0.5 or event.Lepton_isTightMuon_'+muWP+'[2]>0.5) and \
                                                      (event.Lepton_isTightElectron_'+eleWP+'[3]>0.5 or event.Lepton_isTightMuon_'+muWP+'[3]>0.5)) \
                                                     if event.nLepton > 3 else 0.'
