# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

#formulas = {}

METFilter_Common = '(event.std_vector_trigger_special[0]*\
                     event.std_vector_trigger_special[1]*\
                     event.std_vector_trigger_special[2]*\
                     event.std_vector_trigger_special[3]*\
                     event.std_vector_trigger_special[5]\
                   )'

METFilter_DATA   =  METFilter_Common + '*' + '(event.std_vector_trigger_special[4]*\
                                              event.std_vector_trigger_special[8]*\
                                              event.std_vector_trigger_special[9])'

formulas['METFilter_DATA'] = METFilter_DATA


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


muWP='cut_Tight80x'
for eleWP in ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_80p_Iso2015','mva_80p_Iso2016','mva_90p_Iso2015','mva_90p_Iso2016'] :

   Tag = 'ele_'+eleWP+'_mu_'+muWP

   formulas['fakeW2l_'+Tag]            = '(event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))'

   formulas['fakeW2l_'+Tag+'_EleUp']   = '  (event.fakeW_'+Tag+'_2l0jElUp*(event.njet==0)+event.fakeW_'+Tag+'_2l1jElUp*(event.njet==1)+event.fakeW_'+Tag+'_2l2jElUp*(event.njet>=2)) \
                                          / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_EleDown'] = '  (event.fakeW_'+Tag+'_2l0jElDown*(event.njet==0)+event.fakeW_'+Tag+'_2l1jElDown*(event.njet==1)+event.fakeW_'+Tag+'_2l2jElDown*(event.njet>=2)) \
                                          / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_MuUp']    = '  (event.fakeW_'+Tag+'_2l0jMuUp*(event.njet==0)+event.fakeW_'+Tag+'_2l1jMuUp*(event.njet==1)+event.fakeW_'+Tag+'_2l2jMuUp*(event.njet>=2)) \
                                          / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_MuDown']  = '  (event.fakeW_'+Tag+'_2l0jMuDown*(event.njet==0)+event.fakeW_'+Tag+'_2l1jMuDown*(event.njet==1)+event.fakeW_'+Tag+'_2l2jMuDown*(event.njet>=2)) \
                                          / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                          if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'

   formulas['fakeW2l_'+Tag+'_statEleUp']   = '  (event.fakeW_'+Tag+'_2l0jstatElUp*(event.njet==0)+event.fakeW_'+Tag+'_2l1jstatElUp*(event.njet==1)+event.fakeW_'+Tag+'_2l2jstatElUp*(event.njet>=2)) \
                                              / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_statEleDown'] = '  (event.fakeW_'+Tag+'_2l0jstatElDown*(event.njet==0)+event.fakeW_'+Tag+'_2l1jstatElDown*(event.njet==1)+event.fakeW_'+Tag+'_2l2jstatElDown*(event.njet>=2)) \
                                              / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_statMuUp']    = '  (event.fakeW_'+Tag+'_2l0jstatMuUp*(event.njet==0)+event.fakeW_'+Tag+'_2l1jstatMuUp*(event.njet==1)+event.fakeW_'+Tag+'_2l2jstatMuUp*(event.njet>=2)) \
                                              / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'
   formulas['fakeW2l_'+Tag+'_statMuDown']  = '  (event.fakeW_'+Tag+'_2l0jstatMuDown*(event.njet==0)+event.fakeW_'+Tag+'_2l1jstatMuDown*(event.njet==1)+event.fakeW_'+Tag+'_2l2jstatMuDown*(event.njet>=2)) \
                                              / (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2))\
                                              if not (event.fakeW_'+Tag+'_2l0j*(event.njet==0)+event.fakeW_'+Tag+'_2l1j*(event.njet==1)+event.fakeW_'+Tag+'_2l2j*(event.njet>=2)) == 0. else 0.'

