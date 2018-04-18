
TrigNames = [ 
        'HLT_Ele27_eta2p1_WPLoose_Gsf',                                    # 0
        'HLT_Ele23_WPLoose_Gsf',                                           # 1
        'HLT_Ele22_eta2p1_WPLoose_Gsf',                                    # 2
        'HLT_Ele27_eta2p1_WPTight_Gsf',                                    # 3
                                                                                
                                                                                
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL',                          # 4
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',                       # 5
     
     
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL',                  # 6
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL',                  # 7
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',                 # 8
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',                 # 9

        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ',                             # 10
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL',                                # 11
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ',                           # 12
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL',                              # 13
        'HLT_Mu27_TkMu8',                                                  # 14

        'HLT_IsoMu27',                                                     # 15
        'HLT_IsoMu20',                                                     # 16
        'HLT_IsoTkMu20',                                                   # 17


        # Muon (8 paths)
        'HLT_Mu8',                                                         # 18
        'HLT_Mu17',                                                        # 19
        'HLT_Mu24',                                                        # 20
        'HLT_Mu34',                                                        # 21
        'HLT_Mu8_TrkIsoVVL',                                               # 22
        'HLT_Mu17_TrkIsoVVL',                                              # 23
        'HLT_Mu24_TrkIsoVVL',                                              # 24
        'HLT_Mu34_TrkIsoVVL',                                              # 25

        # EG (9 paths)
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30',                               # 26
        'HLT_Ele12_CaloIdM_TrackIdM_PFJet30',                              # 27
        'HLT_Ele18_CaloIdM_TrackIdM_PFJet30',                              # 28
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30',                              # 29
        'HLT_Ele33_CaloIdM_TrackIdM_PFJet30',                              # 30
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30',                        # 31
        'HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30',                        # 32
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30',                        # 33
        'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30',                        # 34
        
        
        # 3 lepton triggers        
        'HLT_TripleMu_12_10_5',                                            # 35
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL',                                 # 36
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL',                                # 37
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL',                           # 38
        
        # same as analysis triggers
        'HLT_IsoTkMu18',                                                   # 39
        'HLT_IsoMu18',                                                     # 40
        
        # Add new triggers always at the end, to preserve backcompatibility
        # new ones in 2016
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL',                  # 41

        'HLT_IsoTkMu22',                                                   # 42
        'HLT_IsoMu22',                                                     # 43
        'HLT_IsoTkMu24',                                                   # 44
        'HLT_IsoMu24',                                                     # 45
        
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',                       # 46
        'HLT_Ele27_WPLoose_Gsf',                                           # 47

        # for fakes
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL',                                # 48
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL',                                # 49
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL',                                # 50
        
        # new for fakes

        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30',                         # 51
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30',                              # 52
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30',                        # 53
        
        # new for higher luminosity
        'HLT_Ele25_WPTight_Gsf',                                           # 54
        'HLT_Ele35_WPLoose_Gsf',                                           # 55

        # and even higher!
        'HLT_Ele45_WPLoose_Gsf',                                           # 56


        # post-ICHEP new triggers
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',              # 57
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ',               # 58
        
        
        # Orthogonal triggers added on September 27th
        # Available from run 278820 [ Run2016G ] which corresponds to the Sep27_NoL1T latino processing
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067',          # 59
        'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight',                       # 60
        'HLT_DiCentralPFJet55_PFMET110',                                   # 61
        'HLT_DoubleMu3_PFMET50',                                           # 62
        'HLT_MET200',                                                      # 63
        'HLT_MET250',                                                      # 64
        'HLT_MET300',                                                      # 65
        'HLT_MET600',                                                      # 66
        'HLT_MET60_IsoTrk35_Loose',                                        # 67
        'HLT_MET700',                                                      # 68
        'HLT_MET75_IsoTrk50',                                              # 69
        'HLT_MET90_IsoTrk50',                                              # 70
        'HLT_MonoCentralPFJet80_PFMETNoMu100_PFMHTNoMu100_IDTight',        # 71
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight',        # 72
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight',        # 73
        'HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight',          # 74
        'HLT_Mu14er_PFMET100',                                             # 75
        'HLT_Mu3er_PFHT140_PFMET125',                                      # 76
        'HLT_Mu6_PFHT200_PFMET100',                                        # 77
        'HLT_Mu6_PFHT200_PFMET80_BTagCSV_p067',                            # 78
        'HLT_PFMET100_PFMHT100_IDTight',                                   # 79
        'HLT_PFMET110_PFMHT110_IDTight',                                   # 80
        'HLT_PFMET120_BTagCSV_p067',                                       # 81
        'HLT_PFMET120_Mu5',                                                # 82
        'HLT_PFMET120_PFMHT120_IDTight',                                   # 83
        'HLT_PFMET300',                                                    # 84
        'HLT_PFMET400',                                                    # 85
        'HLT_PFMET500',                                                    # 86
        'HLT_PFMET600',                                                    # 87
        'HLT_PFMET90_PFMHT90_IDTight',                                     # 88
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight',                           # 89
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight',                           # 90
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight',                           # 91
        'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight',                             # 92
        
        # Trigger update for Rereco data
        'HLT_Ele27_WPTight_Gsf',                                           # 93
        'HLT_Ele32_WPTight_Gsf',                                           # 94
        'HLT_Ele32_eta2p1_WPTight_Gsf',                                    # 95
        
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL',                 # 96
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ',              # 97
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ',               # 98
        
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL',                            # 99
        'HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ',                         # 100
        
        'HLT_Mu20',                                                        # 101
        'HLT_Mu27',                                                        # 102
        'HLT_Mu50',                                                        # 103
        'HLT_Mu55',                                                        # 104
        'HLT_Mu24_eta2p1',                                                 # 105
        'HLT_Mu45_eta2p1',                                                 # 106
        'HLT_IsoMu22_eta2p1',                                              # 107
        'HLT_IsoMu24_eta2p1',                                              # 108
        'HLT_IsoTkMu22_eta2p1',                                            # 109
        'HLT_IsoTkMu24_eta2p1',                                            # 110
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf',                           # 111
        'HLT_Ele25_eta2p1_WPTight_Gsf'                                     # 112
]

SPTrigNames = [
        'Flag_HBHENoiseFilter',
        'Flag_HBHENoiseIsoFilter',
        'Flag_EcalDeadCellTriggerPrimitiveFilter',
        'Flag_goodVertices',
        'Flag_eeBadScFilter',
        'Flag_globalTightHalo2016Filter',
        'Flag_duplicateMuons',
        'Flag_muonBadTrackFilter'
]

if __name__ == '__main__':
   print('Trigger names:')
   for name in TrigNames:
      print(name)
   
   print('Special Trigger names:')
   for name in SPTrigNames:
      print(name)

