Trigger = {


# ---------------------------- Full2016v6 ---------------------------------

#   ------------------------------
#     dataset | from run | to run
#   ----------+----------+--------
#    Run2016B |   272007 | 275376  -> 5.788 /fb                             f_BCDEF = 0.294
#    Run2016C |   275657 | 276283  -> 2.573 /fb                             f_BCDEF = 0.130
#    Run2016D |   276315 | 276811  -> 4.248 /fb                             f_BCDEF = 0.215
#    Run2016E |   276831 | 277420  -> 4.009 /fb                             f_BCDEF = 0.203
#    Run2016F |   277772 | 278808  -> 3.102 /fb -> B+C+D+E+F : 19.720 / fb  f_BCDEF = 0.157
#    Run2016G |   278820 | 280385  -> 7.540 /fb
#    Run2016H |   280919 |         -> 8.606 /fb --> G+H: 16.146 /fb
#    Total lumi: 35.867 /fb (brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt -u /fb)
#   ------------------------------

        'Full2016v6'  :  { 
                          # Lower Muon efficiency at begin of 2016 + L1 EMTF Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.616 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
                          # L1 EMFT Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          2  :  { 'begin' : 274095 , 'end' : 277165 , 'lumi' : 15.005  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=277166: L1 EMTF Bug fixed ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.059  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
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
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=278273: Switch to DZ version of E-Mu triggers
                          # OLD: 4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                          4  :  { 'begin' : 278273 , 'end' : 278808 , 'lumi' : 2.041  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/muon/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v6/DZEff_me_mva.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v6/DZEff_em_mva.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # No change of trigger, same as period 4
                          # END of HIP problem -> Muon ID/ISO SF change
                          #    Run2016G |   278820 | 280385
                          #    Run2016H |   280919 |
                          5  :  { 'begin' : 278820 , 'end' : 281612 , 'lumi' : 7.540  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/muon/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v6/DZEff_me_mva.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v6/DZEff_em_mva.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=281613: Switch to DZ version of Double Mu triggersA : Lumi 8.606 - 0.860 = 7.746 (to accomodate space for pseudo period 7)
                          6  :  { 'begin' : 281613 , 'end' : 284042 , 'lumi' : 7.746  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/muon/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2016v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v6/DZEff_me_mva.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v6/DZEff_em_mva.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                }, 
                          # Run>=281613: Switch to DZ version of Double Mu triggers ... Few LS where HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL is seeded by L1_Mu23_EG10 
                          # Attributed to last run as a trick to switch to the lower efficiency
                          7  :  { 'begin' : 284043 , 'end' : 284044 , 'lumi' : 0.860  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v6/mvaWP90/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v6/muon/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v6/muon/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v6/muon/DoubleMu_IsoMu23_l1pt23_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v6/mvaWP90/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v6/muon/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v6/DZEff_ee_mva.txt' } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2016v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v6/DZEff_me_mva.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v6/DZEff_em_mva.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
                         },


# ---------------------------- Full2017v6 ---------------------------------


        'Full2017v6'  :  {  
                          # Run B 
                          1  :  { 'begin' : 297020 , 'end' : 299329 , 'lumi' : 4.793 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017v6/mvaWP90/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v6/muon/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017v6/muon/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v6/muon/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v6/muon/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'pt1:pt2' : 'Full2017v6/DZEff_me_mva.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v6/DZEff_em_mva.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [0.934,0.005],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.934,0.005],
                                                'EleMu'     : [0.934,0.005],
                                                'SingleEle' : [0.934,0.005],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },

                          # Run C
                          2  :  { 'begin' : 299337 , 'end' : 302029 , 'lumi' : 9.633 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v6/mvaWP90/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v6/muon/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017v6/muon/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v6/muon/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v6/muon/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v6/DZEff_em_mva.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.992+-0.001
                                  'GlEff'  :  { 'DoubleEle' : [0.992,0.001],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.992,0.001],
                                                'EleMu'     : [0.992,0.001],
                                                'SingleEle' : [0.992,0.001],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017D       302030  303434     4.248

                          3  :  { 'begin' : 302030 , 'end' : 303434  , 'lumi' : 4.248 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v6/mvaWP90/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v6/muon/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017v6/muon/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v6/muon/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v6/muon/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v6/DZEff_em_mva.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017E       303435  304826     9.315

                          4  :  { 'begin' : 303435 , 'end' : 304826  , 'lumi' : 9.315 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v6/mvaWP90/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v6/muon/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'SingleMu'          : 'Full2017v6/muon/IsoMu27_pt_eta_efficiency_Run2017E.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v6/muon/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v6/muon/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v6/DZEff_em_mva.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },


                          # Run2017F       304911  306462    13.540

                          5  :  { 'begin' : 304911 , 'end' : 306462  , 'lumi' : 13.540 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'SingleEle'         : 'Full2017v6/mvaWP90/Ele35_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v6/muon/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v6/muon/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'SingleMu'          : 'Full2017v6/muon/IsoMu27_pt_eta_efficiency_Run2017F.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v6/muon/Mu23_pt_eta_efficiency_withSys_Run2017F.txt',
                                                'MuEleLegLowPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v6/muon/Mu12_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v6/DZEff_em_mva.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },



                       },   

# --------------------------- Full2018v5 ---------------------------------

   # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
   # Using lumi obtained with normtag
   # Full 2018 lumi --> 58.826
   
   # export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
   # brilcalc lumi -u /fb -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt

        'Full2018v6'  :  {
                          # Full 2018 
                          1  :  { 'begin' : 315252 , 'end' : 325175 , 'lumi' : 58.826 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2018v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleEleLegLowPt' : 'Full2018v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'SingleEle'         : 'Full2018v6/mvaWP90/Ele32_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleMuLegHigPt'  : 'Full2018v6/muon/Mu17_Mu8_leg1_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2018v6/muon/Mu17_Mu8_leg2_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'SingleMu'          : 'Full2018v6/muon/IsoMu24_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'MuEleLegHigPt'     : 'Full2018v6/muon/Mu23_pt_eta_2018_nominal_efficiency.txt',
                                                'MuEleLegLowPt'     : 'Full2018v6/mvaWP90/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegHigPt'     : 'Full2018v6/mvaWP90/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegLowPt'     : 'Full2018v6/muon/Mu12_pt_eta_2018_nominal_efficiency.txt' ,
                                              } ,
                                  'DZEff'  :  {
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2018v6/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2018v6/DZEff_em_mva.txt' } ,
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


        'Full2018v5'  :  {  
                          # Full 2018 
                          1  :  { 'begin' : 315252 , 'end' : 325175 , 'lumi' : 58.826 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2018v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleEleLegLowPt' : 'Full2018v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'SingleEle'         : 'Full2018v5/Ele32_pt_eta_efficiency_withSys_Run2018.txt',
                                                'DoubleMuLegHigPt'  : 'Full2018v5/Mu17_Mu8_leg1_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2018v5/Mu17_Mu8_leg2_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'SingleMu'          : 'Full2018v5/IsoMu24_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'MuEleLegHigPt'     : 'Full2018v5/Mu23_pt_eta_2018_nominal_efficiency.txt',
                                                'MuEleLegLowPt'     : 'Full2018v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegHigPt'     : 'Full2018v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2018.txt',
                                                'EleMuLegLowPt'     : 'Full2018v5/Mu12_pt_eta_2018_nominal_efficiency.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2018v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2018v5/DZEff_em.txt' } ,
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

# --------------------------- Full2018 ---------------------------------

   # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
   # Using lumi obtained with normtag
   # Full 2018 lumi --> 58.826
   
   # export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
   # brilcalc lumi -u /fb -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt

        'Full2018'  :  {  
                          # Full 2018 
                          1  :  { 'begin' : 315252 , 'end' : 325175 , 'lumi' : 58.826 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2018/Ele23_Ele12_leg1_pt_eta_2018_EGM_nominal_efficiency.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2018/Ele23_Ele12_leg2_pt_eta_2018_EGM_nominal_efficiency.txt' ,
                                                'SingleEle'         : 'Full2018/Ele32_pt_eta_2018_EGM_nominal_efficiency.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2018/Mu17_Mu8_leg1_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2018/Mu17_Mu8_leg2_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'SingleMu'          : 'Full2018/IsoMu24_pt_eta_2018_SingleMu_nominal_efficiency.txt' ,
                                                'MuEleLegHigPt'     : 'Full2018/Mu23_pt_eta_2018_nominal_efficiency.txt',
                                                'MuEleLegLowPt'     : 'Full2018/Ele23_Ele12_leg2_pt_eta_2018_EGM_nominal_efficiency.txt' ,
                                                'EleMuLegHigPt'     : 'Full2018/Ele23_Ele12_leg1_pt_eta_2018_EGM_nominal_efficiency.txt' ,
                                                'EleMuLegLowPt'     : 'Full2018/Mu12_pt_eta_2018_nominal_efficiency.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2018/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2018/DZEff_em.txt' } ,
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


# --------------------------- Full2017 ---------------------------------


#ERA	       Absolute Run Number	
#                From Run To Run  Lumi (/fb)  Run Preiod	
#Run2017B	297020	299329	   4.794      -> 1
#Run2017C	299337	302029	   9.633      -> 2
#Run2017D	302030	303434	   4.248      -> 3
#Run2017E	303435	304826	   9.315      -> 4 
#Run2017F	304911	306462	  13.540      -> 5
# TOTAL                           41.529

#brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF
#/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt -u /fb
# --begin 299337 --end  302029

        'Full2017v2'  :  {  
                          # Run B 
                          1  :  { 'begin' : 297020 , 'end' : 299329 , 'lumi' : 4.793 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'pt1:pt2' : 'Full2017/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [0.934,0.005],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.934,0.005],
                                                'EleMu'     : [0.934,0.005],
                                                'SingleEle' : [0.934,0.005],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },

                          # Run C
                          2  :  { 'begin' : 299337 , 'end' : 302029 , 'lumi' : 9.633 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.992+-0.001
                                  'GlEff'  :  { 'DoubleEle' : [0.992,0.001],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.992,0.001],
                                                'EleMu'     : [0.992,0.001],
                                                'SingleEle' : [0.992,0.001],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017D       302030  303434     4.248

                          3  :  { 'begin' : 302030 , 'end' : 303434  , 'lumi' : 4.248 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017E       303435  304826     9.315

                          4  :  { 'begin' : 303435 , 'end' : 304826  , 'lumi' : 9.315 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017E.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },


                          # Run2017F       304911  306462    13.540

                          5  :  { 'begin' : 304911 , 'end' : 306462  , 'lumi' : 13.540 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017F.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017F.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },



                       },   

# ----------------------------


        'Full2017v2LP19'  :  {  
                          # Run B 
                          1  :  { 'begin' : 297020 , 'end' : 299329 , 'lumi' : 4.793 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017v2LP19/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'pt1:pt2' : 'Full2017/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [0.934,0.005],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.934,0.005],
                                                'EleMu'     : [0.934,0.005],
                                                'SingleEle' : [0.934,0.005],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },

                          # Run C
                          2  :  { 'begin' : 299337 , 'end' : 302029 , 'lumi' : 9.633 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v2LP19/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.992+-0.001
                                  'GlEff'  :  { 'DoubleEle' : [0.992,0.001],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.992,0.001],
                                                'EleMu'     : [0.992,0.001],
                                                'SingleEle' : [0.992,0.001],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017D       302030  303434     4.248

                          3  :  { 'begin' : 302030 , 'end' : 303434  , 'lumi' : 4.248 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v2LP19/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017E       303435  304826     9.315

                          4  :  { 'begin' : 303435 , 'end' : 304826  , 'lumi' : 9.315 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v2LP19/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017E.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },


                          # Run2017F       304911  306462    13.540

                          5  :  { 'begin' : 304911 , 'end' : 306462  , 'lumi' : 13.540 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'SingleEle'         : 'Full2017v2LP19/Ele35_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017F.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017F.txt',
                                                'MuEleLegLowPt'     : 'Full2017v2LP19/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v2LP19/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },



                       },   


# ----------------------------


        'Full2017v5'  :  {  
                          # Run B 
                          1  :  { 'begin' : 297020 , 'end' : 299329 , 'lumi' : 4.793 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017v5/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v5/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v5/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017v5/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v5/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v5/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'pt1:pt2' : 'Full2017v5/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v5/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [0.934,0.005],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.934,0.005],
                                                'EleMu'     : [0.934,0.005],
                                                'SingleEle' : [0.934,0.005],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },

                          # Run C
                          2  :  { 'begin' : 299337 , 'end' : 302029 , 'lumi' : 9.633 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v5/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v5/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v5/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017v5/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v5/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v5/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v5/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.992+-0.001
                                  'GlEff'  :  { 'DoubleEle' : [0.992,0.001],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.992,0.001],
                                                'EleMu'     : [0.992,0.001],
                                                'SingleEle' : [0.992,0.001],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017D       302030  303434     4.248

                          3  :  { 'begin' : 302030 , 'end' : 303434  , 'lumi' : 4.248 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v5/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v5/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v5/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017v5/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v5/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v5/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v5/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017E       303435  304826     9.315

                          4  :  { 'begin' : 303435 , 'end' : 304826  , 'lumi' : 9.315 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017v5/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v5/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v5/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017E.txt' ,
                                                'SingleMu'          : 'Full2017v5/IsoMu27_pt_eta_efficiency_Run2017E.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v5/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v5/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v5/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },


                          # Run2017F       304911  306462    13.540

                          5  :  { 'begin' : 304911 , 'end' : 306462  , 'lumi' : 13.540 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'SingleEle'         : 'Full2017v5/Ele35_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017v5/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017v5/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017F.txt' ,
                                                'SingleMu'          : 'Full2017v5/IsoMu27_pt_eta_efficiency_Run2017F.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017v5/Mu23_pt_eta_efficiency_withSys_Run2017F.txt',
                                                'MuEleLegLowPt'     : 'Full2017v5/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017v5/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017v5/Mu12_pt_eta_efficiency_withSys_Run2017F.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017v5/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017v5/DZEff_em.txt' } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False ,
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },



                       },   

# --------------------------- 2015 ---------------------------------

#        'Full2015'  :  { 1  :  { 'begin' : 1 , 'end' : 999999 , 'lumi' :  5.0 ,
#                                 'LegEff' :  { 'DoubleEleLegHigPt' : 'HLT_Ele17_12LegHigPt.txt' ,
#                                               'DoubleEleLegLowPt' : 'HLT_Ele17_12LegLowPt.txt' ,
#                                               'SingleEle'         : 'HLT_Ele23Single.txt'      ,
#                                               'DoubleMuLegHigPt'  : 'HLT_DoubleMuLegHigPt.txt' ,
#                                               'DoubleMuLegLowPt'  : 'HLT_DoubleMuLegLowPt.txt' ,
#                                               'SingleMu'          : 'HLT_MuSingle.txt' ,
#                                               'MuEleLegHigPt'     : 'HLT_MuEleLegHigPt.txt' ,
#                                               'MuEleLegLowPt'     : 'HLT_MuEleLegLowPt.txt' ,
#                                               'EleMuLegHigPt'     : 'HLT_EleMuLegHigPt.txt' ,
#                                               'EleMuLegLowPt'     : 'HLT_EleMuLegLowPt.txt' ,
#                                             } ,
#                                 'DZEff'  :  { 'DoubleEle' : 0.995 ,
#                                               'DoubleMu'  : 0.95  ,
#                                               'MuEle'     : 1.0   ,
#                                               'EleMu'     : 1.0   ,
#                                             } ,
#                                 'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
#                                 'EMTFBug':  False , 
#                               },
#                       },


# --------------------------- Full2016 ---------------------------------

#   ------------------------------
#     dataset | from run | to run
#   ----------+----------+--------
#    Run2016B |   272007 | 275376  -> 5.788 /fb                             f_BCDEF = 0.294
#    Run2016C |   275657 | 276283  -> 2.573 /fb                             f_BCDEF = 0.130
#    Run2016D |   276315 | 276811  -> 4.248 /fb                             f_BCDEF = 0.215
#    Run2016E |   276831 | 277420  -> 4.009 /fb                             f_BCDEF = 0.203
#    Run2016F |   277772 | 278808  -> 3.102 /fb -> B+C+D+E+F : 19.720 / fb  f_BCDEF = 0.157
#    Run2016G |   278820 | 280385  -> 7.540 /fb
#    Run2016H |   280919 |         -> 8.606 /fb --> G+H: 16.146 /fb
#    Total lumi: 35.867 /fb (brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt -u /fb)
#   ------------------------------

        'Full2016v2'  :  { 
                          # Lower Muon efficiency at begin of 2016 + L1 EMTF Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.616 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
                          # L1 EMFT Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          2  :  { 'begin' : 274095 , 'end' : 277165 , 'lumi' : 15.005  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  { 
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=277166: L1 EMTF Bug fixed ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.059  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleIsoMu17Mu8_IsoMu8leg_Run2016BCDEF_RunLt278273_PTvsETA.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
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
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=278273: Switch to DZ version of E-Mu triggers
                          # OLD: 4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                          4  :  { 'begin' : 278273 , 'end' : 278808 , 'lumi' : 2.041  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_BCDEF_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v2/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v2/DZEff_em.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # No change of trigger, same as period 4
                          # END of HIP problem -> Muon ID/ISO SF change
                          #    Run2016G |   278820 | 280385
                          #    Run2016H |   280919 |
                          5  :  { 'begin' : 278820 , 'end' : 281612 , 'lumi' : 7.540  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v2/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v2/DZEff_em.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                },
                          # Run>=281613: Switch to DZ version of Double Mu triggersA : Lumi 8.606 - 0.860 = 7.746 (to accomodate space for pseudo period 7)
                          6  :  { 'begin' : 281613 , 'end' : 284042 , 'lumi' : 7.746  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt20_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2016v2/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v2/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v2/DZEff_em.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                }, 
                          # Run>=281613: Switch to DZ version of Double Mu triggers ... Few LS where HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL is seeded by L1_Mu23_EG10 
                          # Attributed to last run as a trick to switch to the lower efficiency
                          7  :  { 'begin' : 284043 , 'end' : 284044 , 'lumi' : 0.860  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'SingleEle'         : 'Full2016v2/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2016v2/Mu17_Mu8_leg1_pt_eta_Iso_nominal2016_GH_efficiency.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2016v2/DoubleMu_IsoMu8orIsoTkMu8leg_Run2016GH_PTvsETA_HWW.txt' ,
                                                'SingleMu'          : 'Full2016v2/SingleMu_IsoMu24orIsoTkMu24_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegHigPt'     : 'Full2016v2/DoubleMu_IsoMu23_l1pt23_Run2016GH_PTvsETA_HWW.txt' ,
                                                'MuEleLegLowPt'     : 'Full2016v2/HLT_DoubleEleLegLowPt_Legacy2016.txt' ,
                                                'EleMuLegHigPt'     : 'Full2016v2/HLT_DoubleEleLegHigPt_Legacy2016.txt' ,
                                                'EleMuLegLowPt'     : 'Full2016v2/DoubleMu_IsoMu12_Run2016FGH_RunGe278273_PTvsETA_HWW.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'nvtx'    : 'Full2016v2/DZEff_ee.txt' } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2016v2/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'nvtx'    : 'Full2016v2/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2016v2/DZEff_em.txt' } ,
                                              } ,
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
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoTkMu24', 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'SingleEle' : [ 'HLT_Ele27_WPTight_Gsf' , 'HLT_Ele25_eta2p1_WPTight_Gsf'] ,
                                              } ,

                                },
        
                       }
}

Trigger['Full2016v4'] = Trigger['Full2016v2'] 
Trigger['Full2016v5'] = Trigger['Full2016v2'] 
Trigger['Full2016v5_mh'] = Trigger['Full2016v2'] 
Trigger['Full2017v4'] = Trigger['Full2017v2'] 
#Trigger['Full2017v2LP19'] = Trigger['Full2017v2'] 
Trigger['Full2018v4'] = Trigger['Full2018'] 

# Set v6 to V5

NewVar_MC_dict = {
   'F': [
         'TriggerEffWeight_1l',
         'TriggerEffWeight_1l_u',
         'TriggerEffWeight_1l_d',
         'TriggerEffWeight_2l',
         'TriggerEffWeight_2l_u',
         'TriggerEffWeight_2l_d',
         'TriggerEffWeight_3l',
         'TriggerEffWeight_3l_u',
         'TriggerEffWeight_3l_d',
         'TriggerEffWeight_4l',
         'TriggerEffWeight_4l_u',
         'TriggerEffWeight_4l_d',
         'TriggerEffWeight_sngEl',
         'TriggerEffWeight_sngMu',
         'TriggerEffWeight_dblEl',
         'TriggerEffWeight_dblMu',
         'TriggerEffWeight_ElMu',
        ],
   'I': [
         'TriggerEmulator',
         'EMTFbug_veto',
         'run_period',
         'Trigger_sngEl',
         'Trigger_sngMu',
         'Trigger_dblEl',
         'Trigger_dblMu',
         'Trigger_ElMu'
         #'metFilter'
        ]        
}

NewVar_DATA_dict = {
   'F': [
        ],
   'I': [
         'EMTFbug_veto',
         'run_period',
         'Trigger_sngEl',
         'Trigger_sngMu',
         'Trigger_dblEl',
         'Trigger_dblMu',
         'Trigger_ElMu'
         #'metFilter'
        ]        
}



if __name__ == '__main__':
   for key in Trigger:
      print(Trigger[key])
   print(Trigger['Full2016'][6]['MC'])

