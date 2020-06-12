# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

formulas = {}

#from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2018
#METFilter_Common = '(event.Flag_goodVertices*\
#                     event.Flag_globalSuperTightHalo2016Filter*\
#                     event.Flag_HBHENoiseFilter*\
#                     event.Flag_HBHENoiseIsoFilter*\
#                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
#                     event.Flag_BadPFMuonFilter*\
#                     event.Flag_BadChargedCandidateFilter\
#                   )'

METFilter_Common = '(event.Flag_goodVertices*\
                     event.Flag_globalSuperTightHalo2016Filter*\
                     event.Flag_HBHENoiseFilter*\
                     event.Flag_HBHENoiseIsoFilter*\
                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
                     event.Flag_BadPFMuonFilter\
                   )'


METFilter_DATA   =  METFilter_Common + '*' + '(event.Flag_eeBadScFilter)'

formulas['METFilter_DATA'] = METFilter_DATA

#muWPList = ['cut_Tight80x','cut_Medium80x']
#eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016','mva_90p_Iso2016_SS']

#for eleWP in eleWPlist: 

formulas['LepCut2l__mu_cut_Tight80x__mu_cut_Medium80x'] = '((event.Lepton_isTightMuon_cut_Tight80x[0]>0.5 or event.Lepton_isTightMuon_cut_Medium80x[0]>0.5) and \
                                                    (event.Lepton_isTightMuon_cut_Tight80x[1]>0.5 or event.Lepton_isTightMuon_cut_Medium80x[1]>0.5)) \
                                                   if event.nLepton > 1 else 0.'
