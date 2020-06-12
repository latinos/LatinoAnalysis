SwitchDict = {}

SwitchDict['Full2018'] = {
    'MHTrig_ee': {
    # DoubleEle25
        'True': [
            'event.run_period>2',
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ],
    },

    'MHTrig_me': {
    # Mu27_Ele37 || Mu37_Ele27 || Mu50
        'True': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            'event.Lepton_pt[0]>42',
            'event.Lepton_pt[1]>35',
        ],
    },

    'MHTrig_mm': {
    # Mu37_TkMu27 || Mu50
        'True': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==13',
            'abs(event.Lepton_pdgId[1])==13',
            'event.Lepton_pt[0]>40',
            'event.Lepton_pt[1]>30',
        ],
    },

    'MHTrig_drll': {
    # drll
        'True': [
            'event.drll>0.3',
        ],
    },
}

SwitchDict['Full2018v4'] = SwitchDict['Full2018']

SwitchDict['Full2017v2'] = {
    'MHTrig_ee': {
    # DoubleEle33
        'event.run_period<3': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>40',
            'event.Lepton_pt[1]>40',
        ],
    # DoubleEle25
        'event.run_period>2': [
            'event.run_period>2',
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ],
    },

    'MHTrig_me': {
    # Mu27_Ele37 || Mu37_Ele27 || Mu50
        'event.run_period<3': [ 'False' ],
        'event.run_period>2': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            'event.Lepton_pt[0]>42',
            'event.Lepton_pt[1]>32',
        ],
    },

    'MHTrig_mm': {
    # Mu37_TkMu27 || Mu50
        'event.run_period<3': [ 'False' ],
        'event.run_period>2': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==13',
            'abs(event.Lepton_pdgId[1])==13',
            'event.Lepton_pt[0]>40',
            'event.Lepton_pt[1]>30',
        ],
    },

    'MHTrig_drll': {
    # drll
        'True': [
            'event.drll>0.3',
        ],
    },
}

SwitchDict['Full2017v4'] = SwitchDict['Full2017v2']
SwitchDict['Full2017v5'] = SwitchDict['Full2017v2']


SwitchDict['Full2016v2'] = {
    'MHTrig_ee': {
    # DoubleEle33
        'True': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==11',
            'abs(event.Lepton_pdgId[1])==11',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>35',
        ]
    },

    'MHTrig_me': {
    # Mu27_Ele37 || Mu33_Ele33 || Mu50
        'event.run_period>3': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            '(abs(event.Lepton_pdgId[0]) == 11 and event.Lepton_pt[0]>35) or (abs(event.Lepton_pdgId[1]) == 11 and event.Lepton_pt[1]>35)',
            '(abs(event.Lepton_pdgId[0]) == 13 and event.Lepton_pt[0]>30) or (abs(event.Lepton_pdgId[1]) == 13 and event.Lepton_pt[1]>30)',
            #'event.Lepton_pt[0]>35',
            #'event.Lepton_pt[1]>35',
        ],
    # Mu27_Ele37 || Mu50
        'event.run_period<4': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0]*event.Lepton_pdgId[1])==11*13',
            '(abs(event.Lepton_pdgId[0]) == 11 and event.Lepton_pt[0]>39) or (abs(event.Lepton_pdgId[1]) == 11 and event.Lepton_pt[1]>39)',
            '(abs(event.Lepton_pdgId[0]) == 13 and event.Lepton_pt[0]>30) or (abs(event.Lepton_pdgId[1]) == 13 and event.Lepton_pt[1]>30)',
        ]
    },

    'MHTrig_mm': {
    # Mu30_TkMu11 || Mu50
        'True': [
            'event.nLepton > 1',
            'abs(event.Lepton_pdgId[0])==13',
            'abs(event.Lepton_pdgId[1])==13',
            'event.Lepton_pt[0]>35',
            'event.Lepton_pt[1]>13',
        ]
    },

    'MHTrig_drll': {
    # drll
        'True': [
            'event.drll>0.3',
        ]
    },
}

SwitchDict['Full2016v4'] = SwitchDict['Full2016v2']
SwitchDict['Full2016v5'] = SwitchDict['Full2016v2']
SwitchDict['Full2016v5_mh'] = SwitchDict['Full2016v2']

SwitchDict['Full2016v6'] = SwitchDict['Full2016v5']
SwitchDict['Full2017v6'] = SwitchDict['Full2017v5']
SwitchDict['Full2018v6'] = SwitchDict['Full2018']

