Trigger = {


# --------------------------- Full2018v6 ---------------------------------

   # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
   # Using lumi obtained with normtag
   # Full 2018 lumi --> 58.826
   
   # export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
   # brilcalc lumi -u /fb -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt

        'Full2018v6'  :  {  
                          # Full 2018 
                          1  :  { 'begin' : 315252 , 'end' : 325175 , 'lumi' : 58.826 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2018v6/tightWP/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleEleLegLowPt' : 'Full2018v6/tightWP/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'SingleEle'         : 'Full2018v6/tightWP/Ele32_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleMuLegHigPt'  : 'Full2018v6/muon/Mu17_Mu8_leg1_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2018v6/muon/Mu17_Mu8_leg2_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'SingleMu'          : 'Full2018v6/muon/IsoMu24_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'MuEleLegHigPt'     : 'Full2018v6/muon/Mu23_pt_eta_2018_nominal_efficiency.txt',
                                                'MuEleLegLowPt'     : 'Full2018v6/tightWP/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegHigPt'     : 'Full2018v6/tightWP/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegLowPt'     : 'Full2018v6/muon/Mu12_pt_eta_2018_nominal_efficiency.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2018v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2018v6/DZEff_em_tight.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele32_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele32_WPTight_Gsf'] ,
                                              } ,

                                  },
                          },
}

NewVar_MC_dict = {
   'F': [
         'CBTriggerEffWeight_1l',
         'CBTriggerEffWeight_1l_u',
         'CBTriggerEffWeight_1l_d',
         'CBTriggerEffWeight_2l',
         'CBTriggerEffWeight_2l_u',
         'CBTriggerEffWeight_2l_d',
         'CBTriggerEffWeight_3l',
         'CBTriggerEffWeight_3l_u',
         'CBTriggerEffWeight_3l_d',
         'CBTriggerEffWeight_4l',
         'CBTriggerEffWeight_4l_u',
         'CBTriggerEffWeight_4l_d',
         'CBTriggerEffWeight_sngEl',
         'CBTriggerEffWeight_sngMu',
         'CBTriggerEffWeight_dblEl',
         'CBTriggerEffWeight_dblMu',
         'CBTriggerEffWeight_ElMu',
        ],
   'I': [
         'CBTriggerEmulator',
         #'EMTFbug_veto',
         #'run_period',
         'CBTrigger_sngEl',
         'CBTrigger_sngMu',
         'CBTrigger_dblEl',
         'CBTrigger_dblMu',
         'CBTrigger_ElMu'
         #'metFilter'
        ]        
}

NewVar_DATA_dict = {
   'F': [
        ],
   'I': [
         #'EMTFbug_veto',
         #'run_period',
         'CBTrigger_sngEl',
         'CBTrigger_sngMu',
         'CBTrigger_dblEl',
         'CBTrigger_dblMu',
         'CBTrigger_ElMu'
         #'metFilter'
        ]        
}



if __name__ == '__main__':
   for key in Trigger:
      print(Trigger[key])
   print(Trigger['Full2016'][6]['MC'])

