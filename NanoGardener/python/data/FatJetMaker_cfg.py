
CleanFatJet_br = {
               'F': [
                     'CleanFatJet_pt',
                     'CleanFatJet_eta',
                     'CleanFatJet_phi',
                     'CleanFatJet_mass',
                     'CleanFatJet_tau21',
                    ],

               'I': [
                     'CleanFatJet_jetIdx', # Vectr of FatJet id for reference
                    ],
              }

CleanFatJet_var = ['pt', 'eta', 'phi']


# Fatjet JMS (central,uncertainty) for high purity category 
# Source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging
fatjet_mass_scale_sf = {
        2016: (1, 0.0094),           #  tau21 cut not specified
        2017: (0.982, 0.004),   # tau21 < 45 High Purity region
        2018: (0.997, 0.004),   # tau21 < 45 High Purity region
}

# Fatjet JMR (central,uncertainty) scale factors for high purity category
# Source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging
fatjet_mass_resolution_MC = {
        2016: 10.1,       #  tau21 cut not specified
        2017: 8.753,      # tau21 < 45 High Purity region
        2018: 8.257,      # tau21 < 45 High Purity region
}
fatjet_mass_resolution_sf = {
        2016: (1, 0.20),        #  tau21 cut not specified
        2017: (1.09, 0.05),      # tau21 < 45 High Purity region
        2018: (1.243, 0.041),    # tau21 < 45 High Purity region
}

