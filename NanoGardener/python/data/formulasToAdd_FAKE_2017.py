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

'''
import os
cmssw_base = os.getenv('CMSSW_BASE')
btagfile = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/btagging.py'

if os.path.exists(btagfile) :
  handle = open(btagfile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", btagfile, " does not exist."

for name,btags in tagger.iteritems():
  for wp in btags:
    if 'algo' in wp: continue
    formulas['bveto_'+name+wp] = '    ( event.std_vector_jet_pt[0] < 20 or event.std_vector_jet_'+btags['algo']+'[0] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[1] < 20 or event.std_vector_jet_'+btags['algo']+'[1] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[2] < 20 or event.std_vector_jet_'+btags['algo']+'[2] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[3] < 20 or event.std_vector_jet_'+btags['algo']+'[3] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[4] < 20 or event.std_vector_jet_'+btags['algo']+'[4] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[5] < 20 or event.std_vector_jet_'+btags['algo']+'[5] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[6] < 20 or event.std_vector_jet_'+btags['algo']+'[6] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[7] < 20 or event.std_vector_jet_'+btags['algo']+'[7] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[8] < 20 or event.std_vector_jet_'+btags['algo']+'[8] < '+str(btags[wp])+' ) \
                                  and ( event.std_vector_jet_pt[9] < 20 or event.std_vector_jet_'+btags['algo']+'[9] < '+str(btags[wp])+' ) '

'''

muWP='cut_Tight_HWWW'
#eleWPlist = ['mvaFall17Iso_WP90', 'mvaFall17Iso_WP90_SS']
eleWPlist = ['mvaFall17V1Iso_WP90', 'mvaFall17V1Iso_WP90_SS','mvaFall17V2Iso_WP90', 'mvaFall17V2Iso_WP90_SS']
eleWPlist += ['cutFall17V1Iso_Tight','cutFall17V1Iso_Tight_SS','cutFall17V2Iso_Tight','cutFall17V2Iso_Tight_SS']
#muWP='cut_Tight80x'

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

