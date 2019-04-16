# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

formulas = {}

METFilter_Common = '(event.Flag_goodVertices*\
                     event.Flag_globalSuperTightHalo2016Filter*\
                     event.Flag_HBHENoiseFilter*\
                     event.Flag_HBHENoiseIsoFilter*\
                     event.Flag_EcalDeadCellTriggerPrimitiveFilter*\
                     event.Flag_BadPFMuonFilter\
                   )'

METFilter_FAKE   =  METFilter_Common + '*' + '(event.Flag_eeBadScFilter)'

formulas['METFilter_FAKE'] = METFilter_FAKE

muWP='cut_Tight80x'
eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016']

# event.nCleanJet should count the number of CleanJet's with pt above 30
for eleWP in eleWPlist:

   Tag = 'ele_'+eleWP+'_mu_'+muWP

   formulas['fakeW2l_'+Tag]            = ' (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))'

   formulas['fakeW2l_'+Tag+'_EleUp']   = ' (event.fakeW_'+Tag+'_2l0jElUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1jElUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2jElUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW2l_'+Tag+'_EleDown'] = ' (event.fakeW_'+Tag+'_2l0jElDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1jElDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2jElDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW2l_'+Tag+'_MuUp']    = ' (event.fakeW_'+Tag+'_2l0jMuUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1jMuUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2jMuUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW2l_'+Tag+'_MuDown']  = ' (event.fakeW_'+Tag+'_2l0jMuDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1jMuDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2jMuDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'

   formulas['fakeW2l_'+Tag+'_statEleUp']   = ' (event.fakeW_'+Tag+'_2l0jstatElUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1jstatElUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                  (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2jstatElUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW2l_'+Tag+'_statEleDown'] = ' (event.fakeW_'+Tag+'_2l0jstatElDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1jstatElDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                    (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2jstatElDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW2l_'+Tag+'_statMuUp']    = ' (event.fakeW_'+Tag+'_2l0jstatMuUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1jstatMuUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                   (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2jstatMuUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW2l_'+Tag+'_statMuDown']  = ' (event.fakeW_'+Tag+'_2l0jstatMuDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1jstatMuDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                    (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2jstatMuDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_2l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_2l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'


#print(formulas)

