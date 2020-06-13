####  VBSjjlnu semileptonic samples and configs

# Mainly 2017 as a inclusive starting point
vbsjjlnu_samples_bkg = ['WmTo2J_ZTo2L_QCD','WmToLNu_WmTo2J_QCD','WmToLNu_ZTo2J_QCD','WpTo2J_WmToLNu_QCD','WpTo2J_ZTo2L_QCD',
                'WpToLNu_WpTo2J_QCD','WpToLNu_ZTo2J_QCD','ZTo2L_ZTo2J_QCD','WpToLNu_WmTo2J_QCD',
                'WWW','WWZ','WZZ','ZZZ','WWG',
                'WLNuJJ_EWK','EWKZ2Jets_ZToLL_M-50',
                'DYJetsToLL_M-5to50-LO',
                'DYJetsToLL_M-10to50-LO', 'DYJetsToLL_M-10to50-LO_ext1', 
                'DYJetsToLL_M-50-LO', 'DYJetsToLL_M-50-LO_ext1', 
                'DYJetsToLL_M-50','DYJetsToLL_M-50_ext1',
                'DYJetsToLL_M-4to50_HT-100to200','DYJetsToLL_M-4to50_HT-100to200_ext1',
                'DYJetsToLL_M-4to50_HT-200to400','DYJetsToLL_M-4to50_HT-200to400_ext1',
                'DYJetsToLL_M-4to50_HT-400to600','DYJetsToLL_M-4to50_HT-400to600_ext1',
                'DYJetsToLL_M-4to50_HT-600toInf','DYJetsToLL_M-4to50_HT-600toInf_ext1',
                'DYJetsToLL_M-50_HT-70to100', #---> missing XS
                'DYJetsToLL_M-50_HT-100to200',
                'DYJetsToLL_M-50_HT-200to400','DYJetsToLL_M-50_HT-200to400_ext1',
                'DYJetsToLL_M-50_HT-400to600_ext1','DYJetsToLL_M-50_HT-400to600_ext2',
                'DYJetsToLL_M-50_HT-600to800',
                'DYJetsToLL_M-50_HT-800to1200',
                'DYJetsToLL_M-50_HT-1200to2500',
                'DYJetsToLL_M-50_HT-2500toInf',
                'ST_t-channel_top', 'ST_t-channel_antitop',
                'ST_tW_antitop','ST_tW_top','ST_tW_antitop_ext1','ST_tW_top_ext1',
                'ST_s-channel','ST_s-channel_ext1',
                'TTTo2L2Nu',
                'TTToSemiLeptonic',
                'TTWjets','TTWjets_ext1',
                'TTZjets','TTZjets_ext1',
                'WJetsToLNu-LO', 'WJetsToLNu-LO_ext1',
                'WJetsToLNu_HT70_100',
                'WJetsToLNu_HT100_200',
                'WJetsToLNu_HT200_400',
                'WJetsToLNu_HT400_600',
                'WJetsToLNu_HT600_800',
                'WJetsToLNu_HT800_1200',
                'WJetsToLNu_HT1200_2500',
                'WJetsToLNu_HT2500_inf',
                'WJetsToLNu_Pt50to100',
                'WJetsToLNu_Pt100to250',
                'WJetsToLNu_Pt250to400',
                'WJetsToLNu_Pt400to600',
                'WJetsToLNu_Pt600toInf',
                'WJetsToLNu_0J',
                'WJetsToLNu_1J',
                'WJetsToLNu_2J',
                'WJetsToLNu-LO_1J',
                'WJetsToLNu-LO_2J',
                'WJetsToLNu-LO_3J',
                'WJetsToLNu-LO_4J',
                # 'QCD_Pt-15to20_MuEnrichedPt5','QCD_Pt-20to30_MuEnrichedPt5','QCD_Pt-30to50_MuEnrichedPt5',
                # 'QCD_Pt-50to80_MuEnrichedPt5','QCD_Pt-80to120_MuEnrichedPt5','QCD_Pt-120to170_MuEnrichedPt5',
                # 'QCD_Pt-170to300_MuEnrichedPt5','QCD_Pt-20to30_EMEnriched','QCD_Pt-30to50_EMEnriched','QCD_Pt-50to80_EMEnriched'
                ]


vbsjjlnu_samples_bkg_2016 = [
    'DYJetsToLL_M-5to50_HT-70to100', # not exist 2016 DYJetsToLL_M-5to50 on das
    'DYJetsToLL_M-5to50_HT-100to200',
    'DYJetsToLL_M-5to50_HT-100to200_ext1',
    'DYJetsToLL_M-5to50_HT-200to400',
    'DYJetsToLL_M-5to50_HT-200to400_ext1',
    'DYJetsToLL_M-5to50_HT-400to600',
    'DYJetsToLL_M-5to50_HT-400to600_ext1',
    'DYJetsToLL_M-5to50_HT-600toinf_ext1',
    'DYJetsToLL_M-5to50_HT-600toinf',
    'DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1',
    'DYJetsToLL_M-50',
    'DYJetsToLL_M-50_HT-70to100',
    'DYJetsToLL_M-50_HT-100to200',
    'DYJetsToLL_M-50_HT-100to200_ext1',
    'DYJetsToLL_M-50_HT-200to400',
    'DYJetsToLL_M-50_HT-200to400_ext1',
    'DYJetsToLL_M-50_HT-400to600',
    'DYJetsToLL_M-50_HT-400to600_ext1',
    'DYJetsToLL_M-50_HT-600to800',
    'DYJetsToLL_M-50_HT-800to1200',
    'DYJetsToLL_M-50_HT-1200to2500',
    'DYJetsToLL_M-50_HT-2500toinf',
    'TTWJetsToLNu_ext2',

    'WJetsToLNu', 'WJetsToLNu_ext2', 'WJetsToLNu-LO_ext2',
    'WJetsToLNu_HT100_200_ext2', 'WJetsToLNu_HT200_400_ext2', 'WJetsToLNu_HT400_600_ext1',
    'WJetsToLNu_HT600_800_ext1', 'WJetsToLNu_HT800_1200_ext1', 'WJetsToLNu_HT1200_2500_ext1',
    'WJetsToLNu_HT2500_inf_ext1',
    'WJetsToLNu_Pt100To250_ext4', 'WJetsToLNu_Pt250To400_ext4', 'WJetsToLNu_Pt400To600_ext4', 'WJetsToLNu_Pt600ToInf_ext4',
    'WJetsToLNu_Wpt100t0200_ext1','WJetsToLNu_Wpt200toInf_ext1',                    
]


vbsjjlnu_samples_bkg_2018 = [  'DYJetsToLL_M-50_ext2', 'TTWJetsToLNu', 'TTToSemiLeptonic_ext3', 
                                   'Zg', 'Wg_AMCNLOFXFX','WZTo3LNu_mllmin01','Wg_MADGRAPHMLM']


vbsjjlnu_samples_bkg += vbsjjlnu_samples_bkg_2016
vbsjjlnu_samples_bkg += vbsjjlnu_samples_bkg_2018

vbsjjlnu_samples_signal = [ 'WmTo2J_ZTo2L','WmToLNu_WmTo2J','WmToLNu_ZTo2J','WpTo2J_WmToLNu','WpTo2J_ZTo2L',
                    'WpToLNu_WpTo2J', 'WpToLNu_ZTo2J','ZTo2L_ZTo2J','WpToLNu_WmTo2J',
                     'WmTo2J_ZTo2L_aQGC', 'WmToLNu_WmTo2J_aQGC','WmToLNu_ZTo2J_aQGC','WpTo2J_WmToLNu_aQGC','WpTo2J_ZTo2L_aQGC',
                    'WpToLNu_WpTo2J_aQGC', 'WpToLNu_ZTo2J_aQGC','ZTo2L_ZTo2J_aQGC','WpToLNu_WmTo2J_aQGC']

vbsjjlnu_samples_data2016 = ['SingleElectron_Run2016B-Nano1June2019_ver2-v1','SingleElectron_Run2016C-Nano1June2019-v1',
                            'SingleElectron_Run2016D-Nano1June2019-v1','SingleElectron_Run2016E-Nano1June2019-v1',
                             'SingleElectron_Run2016F-Nano1June2019-v1','SingleElectron_Run2016G-Nano1June2019-v1', 
                             'SingleElectron_Run2016H-Nano1June2019-v1','SingleMuon_Run2016B-Nano1June2019_ver2-v1',
                             'SingleMuon_Run2016C-Nano1June2019-v1','SingleMuon_Run2016D-Nano1June2019-v1',
                             'SingleMuon_Run2016E-Nano1June2019-v1', 'SingleMuon_Run2016F-Nano1June2019-v1',
                             'SingleMuon_Run2016G-Nano1June2019-v1', 'SingleMuon_Run2016H-Nano1June2019-v1']
vbsjjlnu_samples_data2017 = ['SingleElectron_Run2017B-Nano1June2019-v1','SingleElectron_Run2017C-Nano1June2019-v1',
                            'SingleElectron_Run2017D-Nano1June2019-v1','SingleElectron_Run2017E-Nano1June2019-v1',
                             'SingleElectron_Run2017F-Nano1June2019-v1','SingleMuon_Run2017B-Nano1June2019-v1',
                             'SingleMuon_Run2017C-Nano1June2019-v1','SingleMuon_Run2017D-Nano1June2019-v1',
                             'SingleMuon_Run2017E-Nano1June2019-v1','SingleMuon_Run2017F-Nano1June2019-v1']
vbsjjlnu_samples_data2018 = ['SingleMuon_Run2018A-Nano25Oct2019-v1','SingleMuon_Run2018B-Nano25Oct2019-v1',
                              'SingleMuon_Run2018C-Nano25Oct2019-v1','SingleMuon_Run2018D-Nano25Oct2019_ver2-v1',
                              'EGamma_Run2018A-Nano25Oct2019-v1','EGamma_Run2018B-Nano25Oct2019-v1',
                              'EGamma_Run2018C-Nano25Oct2019-v1','EGamma_Run2018D-Nano25Oct2019_ver2-v1']


CombJJLNu_preselections = {
     "2016": {
          "MC": '"nLepton>=1  && Lepton_pt[0]>25 \
                          && (  Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight80x[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight80x[1],0) < 0.5 )  \
                        "',
         "DATA": '"nLepton>=1  && Lepton_pt[0]>25 \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                        && (  Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight80x[1],0) < 0.5 )  \
                        "'
     }, 
     "2017": {
          "MC": '"nLepton>=1  && Lepton_pt[0]>25 \
                          && (  Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',
          "DATA":  '"nLepton>=1  && Lepton_pt[0]>25 \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "'
     }, 
     "2018": {
          "MC": '"nLepton>=1  && Lepton_pt[0]>25 \
                          && (  Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',
          "DATA":  '"nLepton>=1  && Lepton_pt[0]>25 \
                        && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "'
     }
}
