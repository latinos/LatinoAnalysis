

SwitchDict = {
    # DoubleEle33
    'MHTrig2017_ee_DoubleEle33': {
        'threshold': [
            'event.run_period<3',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>40',
            'event.Lepton_pt[1]>40',
        ]
    },

    # DoubleEle25
    'MHTrig2017_ee_DoubleEle25': {
        'threshold': [
            'event.run_period>2',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ]
    },

    # Mu27_Ele37 || Mu37_Ele27 || Mu50
    'MHTrig2017_mu': {
        'threshold': [
            'event.run_period>2',
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            'event.Lepton_pt[0]>42',
            'event.Lepton_pt[1]>32',
        ]
    },

    # Mu37_TkMu27 || Mu50
    'MHTrig2017_mm': {
        'threshold': [
            'event.run_period>2',
            'abs(event.Lepton_pdgId[0])==13',
            'abs(event.Lepton_pdgId[1])==13',
            'event.Lepton_pt[0]>40',
            'event.Lepton_pt[1]>30',
        ]
    },

    # drll
    'MHTrig2017_drll': {
        'threshold': [
            'event.drll>0.3',
        ]
    },
}
