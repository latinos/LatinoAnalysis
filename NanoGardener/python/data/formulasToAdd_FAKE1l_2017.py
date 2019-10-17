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
                     event.Flag_ecalBadCalibFilterV2\
                   )'

METFilter_FAKE   =  METFilter_Common + '*' + '(event.Flag_eeBadScFilter)'

formulas['METFilter_FAKE'] = METFilter_FAKE


muWP='cut_Tight_HWWW'
#eleWPlist = ['mvaFall17Iso_WP90', 'mvaFall17Iso_WP90_SS']
eleWPlist = ['mvaFall17V1Iso_WP90', 'mvaFall17V1Iso_WP90_SS','mvaFall17V2Iso_WP90', 'mvaFall17V2Iso_WP90_SS']

#muWP='cut_Tight80x'

# event.nCleanJet should count the number of CleanJet's with pt above 30
for eleWP in eleWPlist:

   Tag = 'ele_'+eleWP+'_mu_'+muWP



   formulas['fakeW1l_'+Tag]            = ' (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))'

   formulas['fakeW1l_'+Tag+'_EleUp']   = ' (event.fakeW_'+Tag+'_1l0jElUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1jElUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2jElUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW1l_'+Tag+'_EleDown'] = ' (event.fakeW_'+Tag+'_1l0jElDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1jElDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2jElDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW1l_'+Tag+'_MuUp']    = ' (event.fakeW_'+Tag+'_1l0jMuUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1jMuUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2jMuUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'
   formulas['fakeW1l_'+Tag+'_MuDown']  = ' (event.fakeW_'+Tag+'_1l0jMuDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1jMuDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2jMuDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                            event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                      (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                            event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                          if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                  event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                            (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                  event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                          else 0.'

   formulas['fakeW1l_'+Tag+'_statEleUp']   = ' (event.fakeW_'+Tag+'_1l0jstatElUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1jstatElUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                  (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2jstatElUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW1l_'+Tag+'_statEleDown'] = ' (event.fakeW_'+Tag+'_1l0jstatElDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1jstatElDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                    (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2jstatElDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW1l_'+Tag+'_statMuUp']    = ' (event.fakeW_'+Tag+'_1l0jstatMuUp*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1jstatMuUp*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                   (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2jstatMuUp*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'
   formulas['fakeW1l_'+Tag+'_statMuDown']  = ' (event.fakeW_'+Tag+'_1l0jstatMuDown*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1jstatMuDown*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                    (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2jstatMuDown*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              /(event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                          (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30))\
                                              if not (event.fakeW_'+Tag+'_1l0j*(event.nCleanJet == 0 or event.CleanJet_pt[0] < 30)+\
                                                      event.fakeW_'+Tag+'_1l1j*((event.nCleanJet == 1 and event.CleanJet_pt[0] >= 30) or \
                                                                                (event.nCleanJet > 1 and event.CleanJet_pt[0] >= 30 and event.CleanJet_pt[1] < 30))+\
                                                      event.fakeW_'+Tag+'_1l2j*(event.nCleanJet > 1 and event.CleanJet_pt[1] >= 30)) == 0. \
                                              else 0.'


#print(formulas)

