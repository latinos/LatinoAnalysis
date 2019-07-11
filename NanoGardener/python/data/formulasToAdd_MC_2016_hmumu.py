# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

formulas = {}

# from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2018
METFilter_Common = '(event.Flag_goodVertices*\
                     event.Flag_globalSuperTightHalo2016Filter*\
                     event.Flag_HBHENoiseFilter*\
                     event.Flag_HBHENoiseIsoFilter*\
                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
                     event.Flag_BadPFMuonFilter\
                   )'

METFilter_DATA   =  METFilter_Common 

formulas['METFilter_MC'] = METFilter_DATA

# Common Weights


formulas['XSWeight'] = 'event.baseW*\
                        event.genWeight \
                        if hasattr(event, \'genWeight\') else event.baseW'


formulas['SFweight2l'] = 'event.puWeight*\
                          event.TriggerEffWeight_2l*\
                          event.Lepton_RecoSF[0]*\
                          event.Lepton_RecoSF[1]*\
                          event.EMTFbug_veto \
                          if event.nLepton > 1 else 0.'

# Lepton WP

#muWPList = ['cut_Tight80x','cut_Medium80x']
#eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016']

# Lepton scale factor
formulas['LepSF2l__mu_cut_Tight80x__mu_cut_Medium80x'] = 'event.Lepton_tightMuon_cut_Tight80x_IdIsoSF[0]*\
                                                  event.Lepton_tightMuon_cut_Tight80x_IdIsoSF[1]*\
                                                  event.Lepton_tightMuon_cut_Medium80x_IdIsoSF[0]*\
                                                  event.Lepton_tightMuon_cut_Medium80x_IdIsoSF[1] \
                                                  if event.nLepton > 1 else 0.'

# Lepton cut
formulas['LepCut2l__mu_cut_Tight80x__mu_cut_Medium80x'] = '((event.Lepton_isTightMuon_cut_Tight80x[0]>0.5 or event.Lepton_isTightMuon_cut_Medium80x[0]>0.5) and \
                                                    (event.Lepton_isTightMuon_cut_Tight80x[1]>0.5 or event.Lepton_isTightMuon_cut_Medium80x[1]>0.5)) \
                                                    if event.nLepton > 1 else 0.'


# Lepton scale factor up/down
formulas['LepSF2l__mu_cut_Tight80x__Up'] = '((abs(event.Lepton_pdgId[0]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Up[0])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[0])+\
                                         (abs(event.Lepton_pdgId[0]) == 11)) * \
                                        ((abs(event.Lepton_pdgId[1]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Up[1])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[1])+\
                                         (abs(event.Lepton_pdgId[1]) == 11)) \
                                        if event.nLepton > 1 else 0.'

formulas['LepSF2l__mu_cut_Tight80x__Do'] = '((abs(event.Lepton_pdgId[0]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Down[0])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[0])+\
                                         (abs(event.Lepton_pdgId[0]) == 11)) * \
                                        ((abs(event.Lepton_pdgId[1]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Down[1])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[1])+\
                                         (abs(event.Lepton_pdgId[1]) == 11)) \
                                        if event.nLepton > 1 else 0.'
        
formulas['LepSF2l__mu_cut_Medium80x__Up'] = '((abs(event.Lepton_pdgId[0]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Up[0])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[0])+\
                                         (abs(event.Lepton_pdgId[0]) == 11)) * \
                                        ((abs(event.Lepton_pdgId[1]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Up[1])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[1])+\
                                         (abs(event.Lepton_pdgId[1]) == 11)) \
                                        if event.nLepton > 1 else 0.'

formulas['LepSF2l__mu_cut_Medium80x__Do'] = '((abs(event.Lepton_pdgId[0]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Down[0])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[0])+\
                                         (abs(event.Lepton_pdgId[0]) == 11)) * \
                                        ((abs(event.Lepton_pdgId[1]) == 13)*(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'_Down[1])/(event.Lepton_tightMuon_cut_Tight80x_TotSF'+'[1])+\
                                         (abs(event.Lepton_pdgId[1]) == 11)) \
                                        if event.nLepton > 1 else 0.'



# Is this needed?
formulas['GenLepMatch2l'] = 'event.Lepton_genmatched[0]*\
                             event.Lepton_genmatched[1] \
                             if event.nLepton > 1 else 0.'

