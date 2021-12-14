from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertaintiesLatinos import jetmetUncertaintiesProducer

import os
import sys

class UltraJetUncertaintiesProducer(jetmetUncertaintiesProducer, object):
    #----------------------------------------------------------------------------------------------
    # Ultra-Legacy Jet Energy Correction Ucertainties Producer (running on AK4 Jets)
    # - wrapper for official NanoAOD tool with 'Latinos' adjustments:
    #  -> override Jet collection by CleanJet collection ('jetFlav')
    #  -> loop over list of MET objects to pass JEC/JER corrections onto ('metBranchNames')
    #  -> turn ON/OFF storing nominal Jet/MET branches in case of re-calibration ('redoJEC')
    #  -> possibility to turn ON/OFF storing nominally JER-smeared Jet/MET branches ('applySmearing') 
    #  -> produce JER variations independently from JES variations ('jerUncert=True and jesUncert=[]')
    #  -> turn ON/OFF storing unclustered MET correction variations (TODO: no flag yet, turned off by default)
    # - taking advantage of originally implemented options:
    #  -> split JER uncertainty variations to bins of pT and eta ('jerUncert=True and splitJER=True') 
    #  -> save MET uncertainies of Type-1 and Type-1Smear (on top of JER-smeared non-Puppi MET) ('saveMETUncs')  
    # - backwards compatible with pre-UL era
    #  -> apply HEM fix (applyHEMfix)
    #---------------------------------------------------------------------------------------------- 
    def __init__(self, era, isMC=True, jerUncert=False, jesUncert=['Total'], kind=["Up"], jetFlav='AK4PFchs', jetColl='CleanJet', metBranchNames=["PuppiMET"], applySmearing=False, redoJEC=False, applyHEMfix=False, splitJER=False, saveMETUncs=True):
       #parse config with GTs
       cmsswBase = os.getenv('CMSSW_BASE')
       configName = "LatinoAnalysis/NanoGardener/python/data/UltraJECandJER_cfg.py"
       config = {}
       with open(cmsswBase + '/src/' + configName) as src:
           exec(src) #GTs now stored under 'config'
       if isMC:
           jecTag = config['jecTagsMC'][str(era)] 
       else: 
           jecTag = config['jecTagsDATA'][str(era)]
       jerTag = config['jerTagsMC'][str(era)] #only defined for MC

       #notify
       if not isinstance(jesUncert,list):
           print("[ERROR]: Please provide list of JEC uncertainties. String found.")
           sys.exit(1)
       else:
           uncerts_str = ", ".join(jesUncert).strip(", ")
       if not isinstance(jerUncert,bool):
           print("[ERROR]: Please use 'jerUncert' option as a boolean flag.") 
           print("         List of JER uncertainties is produced internally based on 'splitJER' option.")
           sys.exit(1) 
       if not isinstance(metBranchNames,list):
           print("[ERROR]: Please provide list of MET collections. String found.")
           sys.exit(1)
       else:
           mets_str = ", ".join(metBranchNames).strip(", ")
       if not isinstance(kind,list):
           print("[ERROR]: Please provide list of variation kinds (shifts). Both ['Up','Do'] is possible.")
           sys.exit(1)
       else:
           kind_str = ", ".join(kind).strip(", ")
       print("#-----------------------------------------------------")
       print("#------------UltraJetUncertaintiesProducer------------")
       print("#-----------------------------------------------------")
       print("isMC:              "+str(isMC))
       print("era:               "+str(era))
       print("jetType:           "+jetFlav)
       print("jetColl:           "+jetColl)
       print("metBranchNames:    "+mets_str)
       print("JEC uncertainties: "+uncerts_str)
       print("JEC GT:            "+jecTag)
       print("JEC re-calibration:"+str(redoJEC))
       print("JER uncertainties: "+str(jerUncert))
       print("JER splitting:     "+str(splitJER))
       print("JER GT:            "+jerTag)
       print("JER smearing       "+str(applySmearing))
       print("MET uncertainties: "+str(saveMETUncs))
       print("Variation kind:    "+kind_str)
       print("#-------------------------------------") 
       if len(jesUncert) != 0:
           jesUncert.insert(0,"Merged")
           print("[INFO]:    Using merged version of uncertainties.")       
       if jerUncert and not splitJER:
           print("[WARNING]: JER uncertainties will not be splitted.")
       if redoJEC or applySmearing:
           print("[WARNING]: Nominal recalibration will be stored for Jet and MET branches.")
       if not applyHEMfix:
           print("[WARNING]: HEM fix not applied.")
       if not saveMETUncs:
           print("[WARNING]: Corrections will not be translated to your MET branch.")
           _saveMETUncs=[]
       else:
           _saveMETUncs=['T1','T1Smear']
       if len(kind) > 1:
           print("[WARNING]: Both variations (Up/Do) will be stored.")    

       #initialize official tool
       if "AK4" in jetFlav:   
           super(UltraJetUncertaintiesProducer, self).__init__(
               era=str(era),  
               globalTag=jecTag,
               isData=(not isMC),
               jesUncertainties=jesUncert,
               jesShifts=kind,
               jerUncertainties=jerUncert,
               jerTag=jerTag,
               jetType=jetFlav,
               jetColl=jetColl, 
               metBranchNames=metBranchNames,
               applySmearing=applySmearing,
               redoJEC=redoJEC,    
               applyHEMfix=applyHEMfix,
               splitJER=splitJER,
               saveMETUncs=_saveMETUncs 
           )
       elif "AK8" in jetFlav:
           print("[ERROR]: This module is not intended for fat jet uncertainties. Use UltraFatJetUncertaintyProducer for AK8 jet type.")
           sys.exit(1)
       else:
           print("[ERROR]: Unknown jet type.")
           sys.exit(1)    
