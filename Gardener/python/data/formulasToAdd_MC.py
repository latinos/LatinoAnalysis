# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

#formulas = {}

formulas['XSWeight'] = 'event.baseW*\
                        event.GEN_weight_SM/abs(event.GEN_weight_SM) \
                        if hasattr(event, \'GEN_weight_SM\') else 1.'


formulas['SFweight2l'] = 'event.puW*\
                          event.bPogSF_CMVAL*\
                          event.effTrigW*\
                          std_vector_lepton_recoW[0]*\
                          std_vector_lepton_recoW[1]*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'bPogSF_CMVAL\') else 1.'

formulas['SFweight3l'] = 'event.puW*\
                          event.bPogSF_CMVAL*\
                          event.effTrigW3l*\
                          std_vector_lepton_recoW[0]*\
                          std_vector_lepton_recoW[1]*\
                          std_vector_lepton_recoW[2]*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'bPogSF_CMVAL\') else 1.'

muWP='cut_Tight80x'
for eleWP in ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_80p_Iso2015','mva_80p_Iso2016','mva_90p_Iso2015','mva_90p_Iso2016'] :

  formulas['LepSF2l__ele_'+eleWP+'__mu_'+muWP] = 'std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  std_vector_electron_idisoW_'+eleWP+'[1]*\
                                                  std_vector_muon_idisoW_'+muWP+'[0]*\
                                                  std_vector_muon_idisoW_'+muWP+'[1] \
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__mu_'+muWP] = 'std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  std_vector_electron_idisoW_'+eleWP+'[1]*\
                                                  std_vector_electron_idisoW_'+eleWP+'[2]*\
                                                  std_vector_muon_idisoW_'+muWP+'[0]*\
                                                  std_vector_muon_idisoW_'+muWP+'[1]*\
                                                  std_vector_muon_idisoW_'+muWP+'[3] \
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.' 

  formulas['LepCut2l__ele_'+eleWP+'__mu_'+muWP] = '((std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or std_vector_muon_isTightLepton_'+muWP+'[1]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepCut3l__ele_'+eleWP+'__mu_'+muWP] = '((std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or std_vector_muon_isTightLepton_'+muWP+'[1]>0.5) and \
                                                    (std_vector_electron_isTightLepton_'+eleWP+'[2]>0.5 or std_vector_muon_isTightLepton_'+muWP+'[2]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepSF2l__ele_'+eleWP+'__Up'] = '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Up[0])/(std_vector_electron_idisoW_'+eleWP+'[0])+\
                                             (abs(std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Up[1])/(std_vector_electron_idisoW_'+eleWP+'[1])+\
                                             (abs(std_vector_lepton_flavour[1]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') else 1.'

  formulas['LepSF2l__ele_'+eleWP+'__Do'] = '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Down[0])/(std_vector_electron_idisoW_'+eleWP+'[0])+\
                                             (abs(std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Down[1])/(std_vector_electron_idisoW_'+eleWP+'[1])+\
                                             (abs(std_vector_lepton_flavour[1]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__Up'] = '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Up[0])/(std_vector_electron_idisoW_'+eleWP+'[0])+\
                                             (abs(std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Up[1])/(std_vector_electron_idisoW_'+eleWP+'[1])+\
                                             (abs(std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[2]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Up[2])/(std_vector_electron_idisoW_'+eleWP+'[2])+\
                                             (abs(std_vector_lepton_flavour[2]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__Do'] = '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Down[0])/(std_vector_electron_idisoW_'+eleWP+'[0])+\
                                             (abs(std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Down[1])/(std_vector_electron_idisoW_'+eleWP+'[1])+\
                                             (abs(std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(std_vector_lepton_flavour[2]) == 11)*(std_vector_electron_idisoW_'+eleWP+'_Down[2])/(std_vector_electron_idisoW_'+eleWP+'[2])+\
                                             (abs(std_vector_lepton_flavour[2]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') else 1.'

formulas['LepSF2l__mu_'+muWP+'__Up'] = '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Up[0])/(std_vector_muon_idisoW_'+muWP+'[0])+\
                                         (abs(std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Up[1])/(std_vector_muon_idisoW_'+muWP+'[1])+\
                                         (abs(std_vector_lepton_flavour[1]) == 11)) \
                                        if and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

formulas['LepSF2l__mu_'+muWP+'__Do'] = '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Down[0])/(std_vector_muon_idisoW_'+muWP+'[0])+\
                                         (abs(std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Down[1])/(std_vector_muon_idisoW_'+muWP+'[1])+\
                                         (abs(std_vector_lepton_flavour[1]) == 11)) \
                                        if and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'
                                        
formulas['LepSF3l__mu_'+muWP+'__Up'] = '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Up[0])/(std_vector_muon_idisoW_'+muWP+'[0])+\
                                         (abs(std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Up[1])/(std_vector_muon_idisoW_'+muWP+'[1])+\
                                         (abs(std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[2]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Up[2])/(std_vector_muon_idisoW_'+muWP+'[2])+\
                                         (abs(std_vector_lepton_flavour[2]) == 11)) \
                                        if and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

formulas['LepSF3l__mu_'+muWP+'__Do'] = '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Down[0])/(std_vector_muon_idisoW_'+muWP+'[0])+\
                                         (abs(std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Down[1])/(std_vector_muon_idisoW_'+muWP+'[1])+\
                                         (abs(std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(std_vector_lepton_flavour[2]) == 13)*(std_vector_muon_idisoW_'+muWP+'_Down[2])/(std_vector_muon_idisoW_'+muWP+'[2])+\
                                         (abs(std_vector_lepton_flavour[2]) == 11)) \
                                        if and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

formulas['GenLepMatch2l'] = 'event.std_vector_lepton_genmatched[0]*\
                             event.std_vector_lepton_genmatched[1] \
                             if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '

formulas['GenLepMatch3l'] = 'event.std_vector_lepton_genmatched[0]*\
                             event.std_vector_lepton_genmatched[1]*\
                             event.std_vector_lepton_genmatched[2] \
                             if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '


METFilter_Common = '(event.std_vector_trigger_special[0]*\
                     event.std_vector_trigger_special[1]*\
                     event.std_vector_trigger_special[2]*\
                     event.std_vector_trigger_special[3]*\
                     event.std_vector_trigger_special[5]\
                   )'

METFilter_MCver  =  '(event.std_vector_trigger_special[8]==-2.)'
METFilter_MCOld  =  '(event.std_vector_trigger_special[6]*event.std_vector_trigger_special[7])'
METFilter_MCNew  =  '(event.std_vector_trigger_special[8]*event.std_vector_trigger_special[9])'
METFilter_MC     =  METFilter_Common + '*' + '(('+METFilter_MCver+'*'+METFilter_MCOld+') or ((not '+METFilter_MCver+')*'+METFilter_MCNew+'))' 


formulas['METFilter_Common'] = METFilter_Common
formulas['METFilter_MCver'] = METFilter_MCver
formulas['METFilter_MCOld'] = METFilter_MCOld
formulas['METFilter_MCNew'] = METFilter_MCNew
formulas['METFilter_MC'] = METFilter_MC


formulas['bveto'] = '    ( event.std_vector_jet_pt[0] < 20 or event.std_vector_jet_cmvav2[0] < -0.715 ) \
                     and ( event.std_vector_jet_pt[1] < 20 or event.std_vector_jet_cmvav2[1] < -0.715 ) \
                     and ( event.std_vector_jet_pt[2] < 20 or event.std_vector_jet_cmvav2[2] < -0.715 ) \
                     and ( event.std_vector_jet_pt[3] < 20 or event.std_vector_jet_cmvav2[3] < -0.715 ) \
                     and ( event.std_vector_jet_pt[4] < 20 or event.std_vector_jet_cmvav2[4] < -0.715 ) \
                     and ( event.std_vector_jet_pt[5] < 20 or event.std_vector_jet_cmvav2[5] < -0.715 ) \
                     and ( event.std_vector_jet_pt[6] < 20 or event.std_vector_jet_cmvav2[6] < -0.715 ) \
                     and ( event.std_vector_jet_pt[7] < 20 or event.std_vector_jet_cmvav2[7] < -0.715 ) \
                     and ( event.std_vector_jet_pt[8] < 20 or event.std_vector_jet_cmvav2[8] < -0.715 ) \
                     and ( event.std_vector_jet_pt[9] < 20 or event.std_vector_jet_cmvav2[9] < -0.715 ) '
