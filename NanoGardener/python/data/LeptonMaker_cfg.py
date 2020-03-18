
Lepton_br = {
               'F': [
                     'Lepton_pt',
                     'Lepton_eta',
                     'Lepton_phi',
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
                    ],

               'I': [
                     'CleanJet_jetIdx',
                    ],
              }

CleanbJet_br = {
               'F': [
                     'CleanbJet_pt',
                     'CleanbJet_eta',
                     'CleanbJet_phi',
                    ],

               'I': [
                     'CleanbJet_bjetIdx',
                    ],
              }


Lepton_var = ['pt', 'eta', 'phi', 'pdgId'] #, 'eCorr']
VetoLepton_var = ['pt', 'eta', 'phi', 'pdgId'] # , 'eCorr']
CleanJet_var = ['pt', 'eta', 'phi']
CleanbJet_var = ['pt', 'eta', 'phi']
