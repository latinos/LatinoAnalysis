# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

formulas = {}

METFilter_Common = '(event.Flag_goodVertices*\
                     event.Flag_globalSuperTightHalo2016Filter*\
                     event.Flag_HBHENoiseFilter*\
                     event.Flag_HBHENoiseIsoFilter*\
                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
                     event.Flag_BadPFMuonFilter*\
                     event.Flag_BadChargedCandidateFilter*\
                     event.Flag_ecalBadCalibFilter\
                   )'

METFilter_DATA   =  METFilter_Common + '*' + '(event.Flag_eeBadScFilter)'

formulas['METFilter_DATA'] = METFilter_DATA


formulas['LepCut2l'] = '(event.nLepton>=2 and (event.Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[1]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5) )' 

formulas['LepCut3l'] = '(event.nLepton>=3 and (event.Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[1]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[2]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[2]>0.5) )'

formulas['LepCut4l'] = '(event.nLepton>=4 and (event.Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[1]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[2]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[2]>0.5) and \
                                              (event.Lepton_isTightElectron_mvaFall17Iso_WP90[3]>0.5 or event.Lepton_isTightMuon_cut_Tight_HWWW[3]>0.5) )'
