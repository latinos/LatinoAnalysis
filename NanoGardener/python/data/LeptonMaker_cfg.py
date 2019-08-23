
Lepton_br = {
               'F': [
                     'Lepton_pt',
                     'Lepton_eta',
                     'Lepton_phi',
                     'Lepton_ptErr',
                   #'Lepton_isTriggMatched',
                   #'Lepton_eCorr',
                    ],

               'I': [
                     'Lepton_pdgId',
                     'Lepton_electronIdx',
                     'Lepton_muonIdx',
                    ],

               'D': []
         }

VetoLepton_br = {
               'F': [
                     'VetoLepton_pt',
                     'VetoLepton_eta',
                     'VetoLepton_phi',
                     'VetoLepton_ptErr',
                     #'VetoLepton_isTriggMatched',
                     #'VetoLepton_eCorr',
                    ],

               'I': [
                     'VetoLepton_pdgId',
                     'VetoLepton_electronIdx',
                     'VetoLepton_muonIdx',
                    ],

               'D': []
         }

CleanJet_br = {
               'F': [
                     'CleanJet_pt',
                     'CleanJet_eta',
                     'CleanJet_phi',
                     'CleanJet_rawFactor',
                     'CleanJet_rawPt',
                    ],

               'I': [
                     'CleanJet_jetIdx',
                    ],
              }

Lepton_var = ['pt', 'eta', 'phi', 'pdgId','ptErr']#,'isTriggMatched'] #, 'eCorr']
VetoLepton_var = ['pt', 'eta', 'phi', 'pdgId','ptErr']#,'isTriggMatched'] # , 'eCorr']
CleanJet_var = ['pt', 'eta', 'phi','rawFactor','rawPt']
