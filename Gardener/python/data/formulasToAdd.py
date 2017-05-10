# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not "&&")

#formulas = {}

formulas['XSWeight'] = 'event.baseW*\
                        event.GEN_weight_SM/abs(event.GEN_weight_SM) \
                        if hasattr(event, \'GEN_weight_SM\') else 1.'


formulas['SFweight'] = 'event.puW*\
                        event.bPogSF_CMVAL*\
                        event.effTrigW*\
                        event.std_vector_lepton_idisoWcut_WP_Tight80X[0]*\
                        event.std_vector_lepton_idisoWcut_WP_Tight80X[1]*\
                        event.veto_EMTFBug \
                        if hasattr(event, \'bPogSF_CMVAL\') else 1.'


formulas['GenLepMatch'] = 'event.std_vector_lepton_genmatched[0]*\
                           event.std_vector_lepton_genmatched[1] \
                           if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '

METFilter_Common = '(event.std_vector_trigger_special[0]*\
                     event.std_vector_trigger_special[1]*\
                     event.std_vector_trigger_special[2]*\
                     event.std_vector_trigger_special[3]*\
                     event.std_vector_trigger_special[5]\
                   )'

METFilter_DATA   =  METFilter_Common + '*' + '(event.std_vector_trigger_special[4]*\
                                              (not event.std_vector_trigger_special[6])*\
                                              (not event.std_vector_trigger_special[7])*\
                                              event.std_vector_trigger_special[8]*\
                                              event.std_vector_trigger_special[9])'

METFilter_MCver  =  '(event.std_vector_trigger_special[8]==-2.)'
METFilter_MCOld  =  '(event.std_vector_trigger_special[6]*event.std_vector_trigger_special[7])'
METFilter_MCNew  =  '(event.std_vector_trigger_special[8]*event.std_vector_trigger_special[9])'
METFilter_MC     =  METFilter_Common + '*' + '(('+METFilter_MCver+'*'+METFilter_MCOld+') or ((not '+METFilter_MCver+')*'+METFilter_MCNew+'))' 


formulas['METFilter_Common'] = METFilter_Common

formulas['METFilter_DATA'] = METFilter_DATA

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
