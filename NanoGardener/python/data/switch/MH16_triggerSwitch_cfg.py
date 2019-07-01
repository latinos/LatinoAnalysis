

SwitchDict = {
    # DoubleEle33
    'MHTrig2016_ee': {
        'threshold': [
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ]
    },

    # Mu33_Ele33 || Mu50
    'MHTrig2016_mu': {
        'threshold': [
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ]
    },

    # Mu30_TkMu11 || Mu50
    'MHTrig2016_mm': {
        'threshold': [
            'abs(event.Lepton_pdgId[0])==13',
            'abs(event.Lepton_pdgId[1])==13',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>13',
        ]
    },

    # drll
    'MHTrig2016_drll': {
        'threshold': [
            'event.drll>0.3',
        ]
    },
}
