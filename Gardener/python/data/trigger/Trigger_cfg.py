#Trigger = {}

# --------------------------- 2015 ---------------------------------

Trigger['Full2015'] =  { 1  :  { 'begin' : 1 , 'end' : 999999 , 'lumi' :  5.0 ,
                                 'LegEff' :  { 'DoubleEleLegHigPt' : 'HLT_Ele17_12LegHigPt.txt' ,
                                               'DoubleEleLegLowPt' : 'HLT_Ele17_12LegLowPt.txt' ,
                                               'SingleEle'         : 'HLT_Ele23Single.txt'      ,
                                               'DoubleMuLegHigPt'  : 'HLT_DoubleMuLegHigPt.txt' ,
                                               'DoubleMuLegLowPt'  : 'HLT_DoubleMuLegLowPt.txt' ,
                                               'SingleMu'          : 'HLT_MuSingle.txt' ,
                                               'MuEleLegHigPt'     : 'HLT_MuEleLegHigPt.txt' ,
                                               'MuEleLegLowPt'     : 'HLT_MuEleLegLowPt.txt' ,
                                               'EleMuLegHigPt'     : 'HLT_EleMuLegHigPt.txt' ,
                                               'EleMuLegLowPt'     : 'HLT_EleMuLegLowPt.txt' ,
                                             } ,
                                 'DZEff'  :  { 'DoubleEle' : 0.995 ,
                                               'DoubleMu'  : 0.95  ,
                                               'MuEle'     : 1.0   ,
                                               'EleMu'     : 1.0   ,
                                             } ,
                                 'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
                                 'EMTFBug':  False , 
                               },
                       },

# --------------------------- ICHEP2016 ---------------------------------

Trigger['ICHEP2016'] =  { 1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.632 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt_BeforeRun274094.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt_BeforeRun274094.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle_BeforeRun274094.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt_BeforeRun274094.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt_BeforeRun274094.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 0.995 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'trkSFMu':  [ 0.99 , 0.99 , 0.98 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  {
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 42 , 43 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 0  , 56 ] ,
                                              } ,
                                },
                          2  :  { 'begin' : 274094 , 'end' : 999999 , 'lumi' : 11.798  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.995 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'trkSFMu':  [ 0.99 , 0.99 , 0.98 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 42 , 43 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 0  , 56 ] ,
                                              } ,
                                },
                        }
        
        


# --------------------------- Full2016 ---------------------------------

#   ------------------------------
#     dataset | from run | to run
#   ----------+----------+--------
#    Run2016B |   272007 | 275376
#    Run2016C |   275657 | 276283
#    Run2016D |   276315 | 276811
#    Run2016E |   276831 | 277420
#    Run2016F |   277772 | 278808
#    Run2016G |   278820 | 280385
#    Run2016H |   280919 |
#    Total lumi: 35.867 /fb (brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt -u /fb)
#   ------------------------------

Trigger['Full2016'] =  { 
                          # Lower Muon efficiency at begin of 2016 + L1 EMTF Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.616 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt_BeforeRun274094.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt_BeforeRun274094.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle_BeforeRun274094.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt_BeforeRun274094.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt_BeforeRun274094.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'trkSFMu':  [ 0.99 , 0.99 , 0.98 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  {
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                },
                          # L1 EMFT Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          2  :  { 'begin' : 274095 , 'end' : 277165 , 'lumi' : 15.005  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'trkSFMu':  [ 0.99 , 0.99 , 0.98 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                },
                          # Run>=277166: L1 EMTF Bug fixed ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.059  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                },
                          # Run>=278273: Switch to DZ version of E-Mu triggers
                          # OLD: 4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                          4  :  { 'begin' : 278273 , 'end' : 278808 , 'lumi' : 2.041  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 0.961 ,
                                                'EleMu'     : 0.942 ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  { 
                                                'EleMu'     : [ 57 , 97 ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                },
                          # No change of trigger, same as period 4
                          # END of HIP problem -> Muon ID/ISO SF change
                          #    Run2016G |   278820 | 280385
                          #    Run2016H |   280919 |
                          5  :  { 'begin' : 278820 , 'end' : 281612 , 'lumi' : 7.540  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 0.961 ,
                                                'EleMu'     : 0.942 ,
                                              } ,
                                  'EMTFBug':  False ,
                                  'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  {
                                                'EleMu'     : [ 57 , 97 ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                },
                          # Run>=281613: Switch to version of Double Mu triggers
                          6  :  { 'begin' : 281613 , 'end' : 284044 , 'lumi' : 8.606  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.993 ,
                                                'DoubleMu'  : 0.994 ,
                                                'MuEle'     : 0.961 ,
                                                'EleMu'     : 0.942 ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ]
                                  'DATA'   :  { 
                                                'EleMu'     : [ 57 , 97 ] ,
                                                'DoubleMu'  : [ 10 , 100] ,
                                                'SingleMu'  : [ 44 , 45 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 93  , 112 ] ,
                                              } ,
                                }, 
                                  
                        }
