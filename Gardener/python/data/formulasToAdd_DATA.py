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
btagfile = "btagging.py"

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
  formulas['LepCut2l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepCut3l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[2]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[2]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepCut4l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[2]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[2]>0.5)) \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[3]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[3]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'
