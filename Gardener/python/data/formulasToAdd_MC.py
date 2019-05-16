# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

#formulas = {}

formulas['XSWeight'] = 'event.baseW*\
                        event.GEN_weight_SM/abs(event.GEN_weight_SM) \
                        if hasattr(event, \'GEN_weight_SM\') else event.baseW'


formulas['SFweight1l'] = 'event.puW*\
                          event.effTrigW1l*\
                          event.std_vector_lepton_recoW[0]*\
                          event.std_vector_lepton_etaW[0]*event.std_vector_lepton_ptW[0]*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'std_vector_lepton_recoW\') else 1.'

formulas['SFweight2l'] = 'event.puW*\
                          event.effTrigW*\
                          event.std_vector_lepton_recoW[0]*\
                          event.std_vector_lepton_recoW[1]*\
                          event.electron_etaW_2l*event.electron_ptW_2l*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'std_vector_lepton_recoW\') else 1.'

formulas['SFweight3l'] = 'event.puW*\
                          event.effTrigW3l*\
                          event.std_vector_lepton_recoW[0]*\
                          event.std_vector_lepton_recoW[1]*\
                          event.std_vector_lepton_recoW[2]*\
                          event.electron_etaW_3l*event.electron_ptW_3l*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'std_vector_lepton_recoW\') else 1.'

formulas['SFweight4l'] = 'event.puW*\
                          event.effTrigW4l*\
                          event.std_vector_lepton_recoW[0]*\
                          event.std_vector_lepton_recoW[1]*\
                          event.std_vector_lepton_recoW[2]*\
                          event.std_vector_lepton_recoW[3]*\
                          event.electron_etaW_4l*event.electron_ptW_4l*\
                          event.veto_EMTFBug \
                          if hasattr(event, \'std_vector_lepton_recoW\') else 1.'

muWP='cut_Tight80x'
for eleWP in ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_80p_Iso2015','mva_80p_Iso2016','mva_90p_Iso2015','mva_90p_Iso2016'] :

  formulas['LepSF1l__ele_'+eleWP+'__mu_'+muWP] = 'event.std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[0]\
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

  formulas['LepSF2l__ele_'+eleWP+'__mu_'+muWP] = 'event.std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[1]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[0]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[1] \
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__mu_'+muWP] = 'event.std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[1]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[2]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[0]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[1]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[2] \
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.' 

  formulas['LepSF4l__ele_'+eleWP+'__mu_'+muWP] = 'event.std_vector_electron_idisoW_'+eleWP+'[0]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[1]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[2]*\
                                                  event.std_vector_electron_idisoW_'+eleWP+'[3]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[0]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[1]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[2]*\
                                                  event.std_vector_muon_idisoW_'+muWP+'[3] \
                                                  if hasattr(event, \'std_vector_electron_idisoW_'+eleWP+'\') and hasattr(event, \'std_vector_muon_idisoW_'+muWP+'\') else 1.'

  formulas['LepCut1l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'


  formulas['LepCut2l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepCut3l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[2]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[2]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepCut4l__ele_'+eleWP+'__mu_'+muWP] = '((event.std_vector_electron_isTightLepton_'+eleWP+'[0]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[0]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[1]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[1]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[2]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[2]>0.5) and \
                                                    (event.std_vector_electron_isTightLepton_'+eleWP+'[3]>0.5 or event.std_vector_muon_isTightLepton_'+muWP+'[3]>0.5)) \
                                                   if hasattr(event, \'std_vector_electron_isTightLepton_'+eleWP+'\') and hasattr(event, \'std_vector_muon_isTightLepton_'+muWP+'\') else 1.'

  formulas['LepSF2l__ele_'+eleWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

  formulas['LepSF2l__ele_'+eleWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[2]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[2])/(event.std_vector_electron_totSF_'+eleWP+'[2])+\
                                             (abs(event.std_vector_lepton_flavour[2]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

  formulas['LepSF3l__ele_'+eleWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[2]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[2])/(event.std_vector_electron_totSF_'+eleWP+'[2])+\
                                             (abs(event.std_vector_lepton_flavour[2]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

  formulas['LepSF4l__ele_'+eleWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[2]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[2])/(event.std_vector_electron_totSF_'+eleWP+'[2])+\
                                             (abs(event.std_vector_lepton_flavour[2]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[3]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Up[3])/(event.std_vector_electron_totSF_'+eleWP+'[3])+\
                                             (abs(event.std_vector_lepton_flavour[3]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

  formulas['LepSF4l__ele_'+eleWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[0])/(event.std_vector_electron_totSF_'+eleWP+'[0])+\
                                             (abs(event.std_vector_lepton_flavour[0]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[1]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[1])/(event.std_vector_electron_totSF_'+eleWP+'[1])+\
                                             (abs(event.std_vector_lepton_flavour[1]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[2]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[2])/(event.std_vector_electron_totSF_'+eleWP+'[2])+\
                                             (abs(event.std_vector_lepton_flavour[2]) == 13)) * \
                                            ((abs(event.std_vector_lepton_flavour[3]) == 11)*(event.std_vector_electron_totSF_'+eleWP+'_Down[3])/(event.std_vector_electron_totSF_'+eleWP+'[3])+\
                                             (abs(event.std_vector_lepton_flavour[3]) == 13)) \
                                            if hasattr(event, \'std_vector_electron_totSF_'+eleWP+'\') else 1.'

formulas['LepSF2l__mu_'+muWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'

formulas['LepSF2l__mu_'+muWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'
                                        
formulas['LepSF3l__mu_'+muWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[2]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[2])/(event.std_vector_muon_totSF_'+muWP+'[2])+\
                                         (abs(event.std_vector_lepton_flavour[2]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'

formulas['LepSF3l__mu_'+muWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[2]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[2])/(event.std_vector_muon_totSF_'+muWP+'[2])+\
                                         (abs(event.std_vector_lepton_flavour[2]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'

formulas['LepSF4l__mu_'+muWP+'__Up'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[2]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[2])/(event.std_vector_muon_totSF_'+muWP+'[2])+\
                                         (abs(event.std_vector_lepton_flavour[2]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[3]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Up[3])/(event.std_vector_muon_totSF_'+muWP+'[3])+\
                                         (abs(event.std_vector_lepton_flavour[3]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'

formulas['LepSF4l__mu_'+muWP+'__Do'] = '((abs(event.std_vector_lepton_flavour[0]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[0])/(event.std_vector_muon_totSF_'+muWP+'[0])+\
                                         (abs(event.std_vector_lepton_flavour[0]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[1]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[1])/(event.std_vector_muon_totSF_'+muWP+'[1])+\
                                         (abs(event.std_vector_lepton_flavour[1]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[2]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[2])/(event.std_vector_muon_totSF_'+muWP+'[2])+\
                                         (abs(event.std_vector_lepton_flavour[2]) == 11)) * \
                                        ((abs(event.std_vector_lepton_flavour[3]) == 13)*(event.std_vector_muon_totSF_'+muWP+'_Down[3])/(event.std_vector_muon_totSF_'+muWP+'[3])+\
                                         (abs(event.std_vector_lepton_flavour[3]) == 11)) \
                                        if hasattr(event, \'std_vector_muon_totSF_'+muWP+'\') else 1.'

formulas['GenLepMatch1l'] = 'event.std_vector_lepton_genmatched[0] \
                             if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '

formulas['GenLepMatch2l'] = 'event.std_vector_lepton_genmatched[0]*\
                             event.std_vector_lepton_genmatched[1] \
                             if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '

formulas['GenLepMatch3l'] = 'event.std_vector_lepton_genmatched[0]*\
                             event.std_vector_lepton_genmatched[1]*\
                             event.std_vector_lepton_genmatched[2] \
                             if hasattr(event, \'std_vector_lepton_genmatched\') else 1. '

formulas['GenLepMatch4l'] = 'event.std_vector_lepton_genmatched[0]*\
                             event.std_vector_lepton_genmatched[1]*\
                             event.std_vector_lepton_genmatched[2]*\
                             event.std_vector_lepton_genmatched[3] \
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


#formulas['METFilter_Common'] = METFilter_Common
#formulas['METFilter_MCver'] = METFilter_MCver
#formulas['METFilter_MCOld'] = METFilter_MCOld
#formulas['METFilter_MCNew'] = METFilter_MCNew
formulas['METFilter_MC'] = METFilter_MC

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

