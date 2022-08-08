# Cross section DB for Ultra-Legacy samples
# Units in pb
#
# Detailed references at: https://docs.google.com/spreadsheets/d/1IEfle0H1V3ih2JVFpYckmTd-ACTBqgBRIsFydegGgPQ/edit?usp=sharing
#
# References
#
#	A	https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV		
#	B	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO		
#	C	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV		
#	D	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec		
#	E	https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#       F       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV
#	F2	https://github.com/latinos/LatinoAnalysis/blob/master/Tools/python/HiggsXSection.py
#	G	https://twiki.cern.ch/twiki/bin/view/CMS/GenXsecTaskForce		
#	H	http://arxiv.org/pdf/1307.7403v1.pdf		
#	I	https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer		
#	J	https://svnweb.cern.ch/cern/wsvn/LHCDMF/trunk/doc/tex/TTBar_Xsecs_Appendix.tex
#	K	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProductionMassScan (powheg numbers)
#	L	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProduction (powheg numbers)
#       M       https://github.com/shu-xiao/MadGraphScanning/blob/master/diffCrossSection/madGraph.txt
#       N       MCM
#       O       https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx
#       P       https://drive.google.com/file/d/0B7mfFpGbPaMvb0ZtMlJfdXhJb2M/view
#       Q       #https://indico.cern.ch/event/448517/session/0/contribution/16/attachments/1164999/1679225/Long_Generators_WZxsec_05_10_15.pdf
#	R	https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=B2G-RunIISummer15GS*&dataset_name=TTbarDMJets_*scalar_Mchi-*_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#       S       https://docs.google.com/spreadsheets/d/1b4qnWfZrimEGYc1z4dHl21-A9qyJgpqNUbhOlvCzjbE/edit?usp=sharing
#       T       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
#       U       https://twiki.cern.ch/twiki/pub/CMS/MonoHCombination/crossSection_ZpBaryonic_gq0p25.txt
#	V	https://twiki.cern.ch/twiki/bin/viewauth/CMS/SameSignDilepton2016
#       W       https://cms-gen-dev.cern.ch/xsdb/
#       Z       http://cms.cern.ch/iCMS/analysisadmin/cadilines?line=SMP-18-006
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
#       A1      https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf 
#	X	Unknown! - Cross section not yet there

### W+jets
samples['WJetsToLNu']                   	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu_Sherpa']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )

# XSDB: WJets-LO XS = 53870 pb
# WJets-NNLO XS = 61526.7 pb
# k-fact = 1.14
samples['WJetsToLNu_HT70To100']                 .extend( ['xsec=1264.0',        'kfact=1.14',           'ref=W'] )   
samples['WJetsToLNu_HT100To200']          	.extend( ['xsec=1256.00',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT200To400']          	.extend( ['xsec=335.500',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT400To600']           	.extend( ['xsec=45.2500',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT600To800']          	.extend( ['xsec=10.9700',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT800To1200']         	.extend( ['xsec=4.93300',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT1200To2500']        	.extend( ['xsec=1.16000',	'kfact=1.14',		'ref=W'] )
samples['WJetsToLNu_HT2500ToInf']         	.extend( ['xsec=0.02678',	'kfact=1.00',		'ref=I'] )

samples['WJetsToLNu_Pt-100To250']               .extend( ['xsec=763.7',	        'kfact=1.0',		'ref=W'] )  
samples['WJetsToLNu_Pt-250To400']               .extend( ['xsec=27.55', 	'kfact=1.0',		'ref=W'] )
samples['WJetsToLNu_Pt-400To600']               .extend( ['xsec=3.477', 	'kfact=1.0',		'ref=W'] )
samples['WJetsToLNu_Pt-600ToInf']               .extend( ['xsec=0.5415',	'kfact=1.0',		'ref=W'] )

# Sum of XS: 53330 + 8875 + 3338 = 65543
# NNLO XS = 61526.7
# k factor = 61526.7 / 65543
samples['WJetsToLNu_0J']                        .extend( [ 'xsec=53330',        'kfact=0.94',           'ref=W' ] )
samples['WJetsToLNu_1J']                        .extend( [ 'xsec=8875',         'kfact=0.94',           'ref=W' ] )
samples['WJetsToLNu_2J']                        .extend( [ 'xsec=3338',         'kfact=0.94',           'ref=W' ] )


### DY
samples['DYJetsToLL_M-10to50']          	.extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50-LO']               .extend( ['xsec=18610.0',       'kfact=1.000',          'ref=E'] )

samples['DYJetsToLL_M-50']                      .extend( ['xsec=6077.22',       'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO']      	        .extend( ['xsec=6077.22',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50-LO_ext1']     	        .extend( ['xsec=6077.22',	'kfact=1.000',		'ref=E'] )

samples['DYJetsToTT_MuEle_M-50']                .extend( ['xsec=250.997',       'kfact=1.000',          'ref=E'] )  # (6077.22/3)*(0.352)^2

# DYJetsToLL_M-50 = 6077.22 --> 5129 + 951.5 + 361.4 = 6441.9 --> k-factor = 0.94
samples['DYJetsToLL_0J']                        .extend( [ 'xsec=5129',         'kfact=0.94',           'ref=W' ] )
samples['DYJetsToLL_1J']                        .extend( [ 'xsec=951.5',        'kfact=0.94',           'ref=W' ] )
samples['DYJetsToLL_2J']                        .extend( [ 'xsec=361.4',        'kfact=0.94',           'ref=W' ] )

samples['DYJetsToLL_M-50_HT-70to100']           .extend( ['xsec=146.5',   	'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-100to200']          .extend( ['xsec=160.7',	        'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-200to400']          .extend( ['xsec=48.63',	        'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-400to600']          .extend( ['xsec=6.993',	        'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-600to800']          .extend( ['xsec=1.761',	        'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-800to1200']         .extend( ['xsec=0.8021',	'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-1200to2500']        .extend( ['xsec=0.1937',	'kfact=1.23',	        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-2500toInf']         .extend( ['xsec=0.003514',	'kfact=1.23',	        'ref=W'] ) 

samples['DYJetsToLL_M-4to50_HT-100to200']       .extend( ['xsec=204.',          'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-200to400']       .extend( ['xsec=54.39',         'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-400to600']       .extend( ['xsec=5.697',         'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-600toInf']       .extend( ['xsec=1.85',          'kfact=1.000',          'ref=W'] )

samples['EWKZ2Jets_ZToLL_M-50']                 .extend( ['xsec=6.215',         'kfact=1.000',          'ref=W'] )

### Wgamma
samples['WGToLNuG']                             .extend( ['xsec=412.7',         'kfact=1.000',          'ref=W'] )

### WW
samples['WWTo2L2Nu']	                 	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )
samples['WWTo2L2Nu_TuneCP5Up']                	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )		
samples['WWTo2L2Nu_TuneCP5Down']               	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )		

# 1.4*0.0368 --> 1.4 is a k-factor, 0.0368 comes from XSDB, divided by 1000
samples['GluGluToWWToENEN']      	        .extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToENMN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToENTN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToMNEN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToMNMN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToMNTN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToTNEN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToTNMN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )
samples['GluGluToWWToTNTN']              	.extend( ['xsec=0.05152',	'kfact=1.000',		'ref=W'] )


### WZ
samples['WZ']			                .extend( ['xsec=47.130',	'kfact=1.000',		'ref=E'] )

samples['WZTo3LNu']		                .extend( ['xsec=4.666',  	'kfact=1.000',		'ref=X'] ) # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf
Samples['WZTo3LNu_mllmin4p0']	                .extend( ['xsec=4.666',   	'kfact=1.000',		'ref=X'] ) # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf BUT KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
Samples['WZTo3LNu_mllmin0p1']	                .extend( ['xsec=4.666',   	'kfact=1.000',		'ref=X'] ) # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf BUT KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
samples['WZTo2Q2L_mllmin4p0']	                .extend( ['xsec=5.5950',	'kfact=1.000',		'ref=E'] ) # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
samples['WZTo1L3Nu']                            .extend( ['xsec=3.033',         'kfact=1.000',          'ref=E'] )

samples['WZJJ_Inclusive']                       .extend( ['xsec=0.01627',       'kfact=1.000',          'ref=W'] )
samples['WZJJ_LL']                              .extend( ['xsec=0.001375',      'kfact=1.000',          'ref=W'] )
samples['WZJJ_TL']                              .extend( ['xsec=0.003186',      'kfact=1.000',          'ref=W'] )
samples['WZJJ_LT']                              .extend( ['xsec=0.002824',      'kfact=1.000',          'ref=W'] )
samples['WZJJ_TT']                              .extend( ['xsec=0.008854',      'kfact=1.000',          'ref=W'] )

samples['WZG']                                  .extend( ['xsec=0.04345',       'kfact=1.000',          'ref=E'] )

### ZZ
samples['ZZ']                                   .extend( ['xsec=16.52300', 	'kfact=1.000',		'ref=E'] )
samples['ZZTo2Q2L']                             .extend( ['xsec=2.33',  	'kfact=1.000',		'ref=E'] ) # 16.523 * (3*0.033658)*(0.69911)*2
samples['ZZTo2Q2L_mllmin4p0']                   .extend( ['xsec=2.33',  	'kfact=1.000',		'ref=E'] ) # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
samples['ZZTo2Nu2Q']                            .extend( ['xsec=4.62',  	'kfact=1.000',		'ref=E'] ) # 16.52300 * (0.20)*(0.69911)*2
samples['ZZTo4L']                               .extend( ['xsec=1.325', 	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L_M-1toInf']                      .extend( ['xsec=1.374', 	'kfact=1.000',		'ref=E'] ) # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
samples['ZZTo2L2Nu']                            .extend( ['xsec=0.667', 	'kfact=1.000',		'ref=E'] ) # 16.52300 *(3*0.033658)*(0.20)*2
samples['ZZTo2Q2Nu']                            .extend( ['xsec=4.62',  	'kfact=1.000',		'ref=E'] ) # 16.52300 *(3*0.69911)*(0.20)*2
samples['ZZTo4Q']                               .extend( ['xsec=8.076', 	'kfact=1.000',		'ref=E'] ) # 16.52300*(0.69911)**2

samples['ZZGTo4L']                              .extend( ['xsec=0.02202',	'kfact=1.000',		'ref=W'] )

### ZG
samples['ZGToLLG']                              .extend( ['xsec=51.1',          'kfact=1.000',          'ref=W'] )


### Top
samples['TTJets-LO']                            .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )

samples['TT_DiLept'] 	             	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )

samples['TTTo2L2Nu'] 	             	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_TuneCP5Up']         	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_TuneCP5Down']       	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_hdampUp']         	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_hdampDown']         	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )

samples['TTJets_DiLept']                        .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )

samples['TTToSemiLeptonic']                     .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TTToSemiLeptonic_TuneCP5Up']           .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )
samples['TTToSemiLeptonic_TuneCP5Down']         .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )
samples['TTToSemiLeptonic_hdampUp']             .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )
samples['TTToSemiLeptonic_hdampDown']           .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )

samples['ST_t-channel_top']                     .extend( ['xsec=44.07048',	'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_top_TuneCP5Up']           .extend( ['xsec=44.07048',	'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_top_TuneCP5Down']         .extend( ['xsec=44.07048',	'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_top_hdampUp']             .extend( ['xsec=44.07048',	'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_top_hdampDown']           .extend( ['xsec=44.07048',	'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_top_5f']                  .extend( ['xsec=136.02',        'kfact=1.000',          'ref=Z'] )

samples['ST_t-channel_antitop']                 .extend( ['xsec=26.2278',       'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_antitop_TuneCP5Up']       .extend( ['xsec=26.2278',       'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_antitop_TuneCP5Down']     .extend( ['xsec=26.2278',       'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_antitop_hdampUp']         .extend( ['xsec=26.2278',       'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_antitop_hdampDown']       .extend( ['xsec=26.2278',       'kfact=1.000',		'ref=D'] )
samples['ST_t-channel_antitop_5f']              .extend( ['xsec=80.95',         'kfact=1.000',		'ref=D'] )

samples['ST_tW_antitop']                        .extend( ['xsec=35.85',		'kfact=1.000',		'ref=D'] )
samples['ST_tW_antitop_noHad']                  .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_antitop_noHad_TuneCP5Up']        .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_antitop_noHad_TuneCP5Down']      .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_antitop_noHad_hdampUp']          .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_antitop_noHad_hdampDown']        .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_antitop_noHad_PDF']              .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1

samples['ST_tW_top']                            .extend( ['xsec=35.85',		'kfact=1.000',		'ref=D'] )
samples['ST_tW_top_noHad']                      .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_top_noHad_TuneCP5Up']            .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_top_noHad_TuneCP5Down']          .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_top_noHad_hdampUp']              .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_top_noHad_hdampDown']            .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1
samples['ST_tW_top_noHad_PDF']                  .extend( ['xsec=3.76',          'kfact=1.000',          'ref=D'] ) # 35.85 * (3*0.108)^2 - previously XS = 1

samples['ST_s-channel']                         .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_TuneCP5Up']               .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_TuneCP5Down']             .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_TuneCP5CR1']              .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_TuneCP5CR2']              .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_erdON']                   .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )
samples['ST_s-channel_JMENano']                 .extend( ['xsec=3.34368',	'kfact=1.000',		'ref=D'] )

samples['TTWJetsToQQ']                          .extend( ['xsec=0.4377',        'kfact=1.000',          'ref=W'] )      
samples['TTZToQQ']                              .extend( ['xsec=0.5297',        'kfact=1.000',          'ref=E'] )
samples['TTZToQQ_Dilept']                       .extend( ['xsec=0.0568',        'kfact=1.000',          'ref=W'] )

samples['TTWJetsToLNu']                         .extend( ['xsec=0.2161',	'kfact=1.000',		'ref=E'] )	
samples['TTWJetsToLNu_TuneCP5Up']               .extend( ['xsec=0.2161',	'kfact=1.000',		'ref=E'] )	
samples['TTWJetsToLNu_TuneCP5Down']             .extend( ['xsec=0.2161',	'kfact=1.000',		'ref=E'] )	

samples['TTZToLLNuNu_M-10']                     .extend( ['xsec=0.2439',	'kfact=1.000',		'ref=W'] )
samples['TTZToLLNuNu_M-10_TuneCP5Up']           .extend( ['xsec=0.2439',	'kfact=1.000',		'ref=W'] )
samples['TTZToLLNuNu_M-10_TuneCP5Down']         .extend( ['xsec=0.2439',	'kfact=1.000',		'ref=W'] )

samples['tZq_ll']   				.extend( ['xsec=0.07580',	'kfact=1.000',	        'ref=E'] )
samples['tZq_ll_TuneCP5Up']   			.extend( ['xsec=0.07580',	'kfact=1.000',	        'ref=E'] )
samples['tZq_ll_TuneCP5Down'] 			.extend( ['xsec=0.07580',	'kfact=1.000',	        'ref=E'] )

samples['tZq_ll_4f']                            .extend( ['xsec=0.0761',        'kfact=1.000',          'ref=W'] )
samples['tZq_ll_4f_TuneCP5Up']                  .extend( ['xsec=0.0761',        'kfact=1.000',          'ref=W'] )
samples['tZq_ll_4f_TuneCP5Down']                .extend( ['xsec=0.0761',        'kfact=1.000',          'ref=W'] )


## VVV
samples['WWW']			        	.extend( ['xsec=0.2158',	'kfact=1.000',		'ref=W'] )
samples['WWW_ext1']			        .extend( ['xsec=0.2158',	'kfact=1.000',		'ref=W'] )
                                               
samples['WWZ']				        .extend( ['xsec=0.1707',	'kfact=1.000',		'ref=W'] )
samples['WWZ_ext1']     			.extend( ['xsec=0.1707',	'kfact=1.000',		'ref=W'] )
                                               
samples['WZZ']	 			        .extend( ['xsec=0.05709',	'kfact=1.000',		'ref=W'] )
samples['WZZ_ext1']			        .extend( ['xsec=0.05709',	'kfact=1.000',		'ref=W'] )
                                               
samples['ZZZ']				        .extend( ['xsec=0.01476',	'kfact=1.000',		'ref=W'] )
samples['ZZZ_ext1']			        .extend( ['xsec=0.01476',	'kfact=1.000',		'ref=W'] )
                                               
samples['WWG']                                  .extend( ['xsec=0.2147',        'kfact=1.000',          'ref=E'] )

samples['WWW_DiLeptonFilter']			.extend( ['xsec=0.007205',	'kfact=1.000',		'ref=W'] )

samples['WWZTo4L2Nu']				.extend( ['xsec=0.001809',	'kfact=1.000',		'ref=W'] ) # 0.1707*(3*0.108)*(3*0.108)*(3*0.033658)


### QCD
samples['QCD_Pt_15to20_bcToE']    		.extend( ['xsec=186200',	'kfact=1.000',  	'ref=I'] )
samples['QCD_Pt_20to30_bcToE']    		.extend( ['xsec=303800',	'kfact=1.000',  	'ref=I'] )
samples['QCD_Pt_30to80_bcToE']    		.extend( ['xsec=362300',	'kfact=1.000',  	'ref=I'] )
samples['QCD_Pt_80to170_bcToE']    		.extend( ['xsec=33700',		'kfact=1.000',  	'ref=I'] )
samples['QCD_Pt_170to250_bcToE']    		.extend( ['xsec=2125',		'kfact=1.000',  	'ref=I'] )
samples['QCD_Pt_250toInf_bcToE']    		.extend( ['xsec=562.5',		'kfact=1.000',  	'ref=I'] )

samples['QCD_HT200to300']                       .extend( ['xsec=1555000',       'kfact=1.000',          'ref=W'] )
samples['QCD_HT300to500']                       .extend( ['xsec=324500' ,       'kfact=1.000',          'ref=W'] )
samples['QCD_HT500to700']                       .extend( ['xsec=30310'  ,       'kfact=1.000',          'ref=W'] )
samples['QCD_HT700to1000']                      .extend( ['xsec=6444'   ,       'kfact=1.000',          'ref=W'] )
samples['QCD_HT1000to1500']                     .extend( ['xsec=1127'   ,       'kfact=1.000',          'ref=W'] )
samples['QCD_HT1500to2000']                     .extend( ['xsec=109.8'  ,       'kfact=1.000',          'ref=W'] )
samples['QCD_HT2000toInf']                      .extend( ['xsec=21.98'  ,       'kfact=1.000',          'ref=W'] )

samples['QCD_Pt_15to30']                        .extend( ['xsec=1244000000',    'kfact=1.000',          'ref=W'] )
samples['QCD_Pt_30to50']                        .extend( ['xsec=106500000',     'kfact=1.000',          'ref=W'] )


### Signals - XS are dummy and taken from YR4 N3LO

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
# BR (H-->WW) = 0.2152
# BR (H-->tt) = 0.06256
# BR (H-->ZZ) = 0.02641

# ggH - XS = 48.52 pb
# 58.52*0.2152*(3*0.108)*(3*0.108)
samples['GluGluHToWWTo2L2Nu_M125']    		.extend( ['xsec=1.32200',	'kfact=1.000',	'ref=F'] )
samples['GluGluHToWWTo2L2Nu_M125_TuneCP5Up']    .extend( ['xsec=1.32200',       'kfact=1.000',  'ref=F'] )
samples['GluGluHToWWTo2L2Nu_M125_TuneCP5Down']  .extend( ['xsec=1.32200',       'kfact=1.000',  'ref=F'] )
samples['GluGluHToWWTo2L2Nu_M125_Powheg']       .extend( ['xsec=1.32200',       'kfact=1.000',  'ref=F'] )
samples['GluGluHToWWTo2L2Nu_M125_noPDF']        .extend( ['xsec=1.32200',       'kfact=1.000',  'ref=F'] )
samples['GluGluHToWWTo2L2Nu_M125_Pohweg_noPDF'] .extend( ['xsec=1.32200',       'kfact=1.000',  'ref=F'] )

samples['GGHjjToWWTo2L2Nu_minloHJJ_M125']       .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] ) 

# 48.52*0.06256
samples['GluGluHToTauTau_M125']    		.extend( ['xsec=3.0354',	'kfact=1.000',	'ref=F'] )
samples['GluGluHToTauTau_M125_Powheg'] 		.extend( ['xsec=3.0354',	'kfact=1.000',	'ref=F'] )
samples['GluGluHToTauTau_M125_FXFX'] 		.extend( ['xsec=3.0354',	'kfact=1.000',	'ref=F'] )

# 48.52*0.02641*(3*0.033658)*(3*0.033658)
samples['GluGluHToZZTo4L_M125']    		.extend( ['xsec=0.01306',	'kfact=1.000',	'ref=F'] )
samples['GluGluHToZZTo4L_M125_TuneCP5Up']       .extend( ['xsec=0.01306',       'kfact=1.000',  'ref=F'] )
samples['GluGluHToZZTo4L_M125_TuneCP5Down']     .extend( ['xsec=0.01306',       'kfact=1.000',  'ref=F'] )

# VBF - XS = 3.779 pb
# 3.779*0.2152*(3*0.108)*(3*0.108) 
samples['VBFHToWWTo2L2Nu_M125']    		.extend( ['xsec=0.08537',	'kfact=1.000',	'ref=F'] )
samples['VBFHToWWTo2L2Nu_M125_TuneCP5Up']       .extend( ['xsec=0.08537',       'kfact=1.000',  'ref=F'] ) 
samples['VBFHToWWTo2L2Nu_M125_TuneCP5Down']     .extend( ['xsec=0.08537',       'kfact=1.000',  'ref=F'] )
samples['VBFHToWWTo2L2Nu_M125_noPDF']           .extend( ['xsec=0.08537',       'kfact=1.000',  'ref=F'] )   

# 3.779*0.06256
samples['VBFHToTauTau_M125']    		.extend( ['xsec=0.236',  	'kfact=1.000',	'ref=F'] )

# WH - XS(W+H) = 0.8380 pb and XS(W-H) = 0.5313 pb
# 0.5313*0.2152
samples['HWminusJ_HToWW_M125']    		.extend( ['xsec=0.114',  	'kfact=1.000',	'ref=F'] )
# 0.05967*0.2152*(3*0.108)*(3*0.108) 
samples['HWminusJ_HToWWTo2L2Nu_WToLNu_M125']    .extend( ['xsec=0.001348',      'kfact=1.000',  'ref=F'] ) 

# 0.8380*0.2152
samples['HWplusJ_HToWW_M125']                   .extend( ['xsec=0.1803',        'kfact=1.000',  'ref=F'] )
# 0.09404*0.2152*(3*0.108)*(3*0.108) 
samples['HWplusJ_HToWWTo2L2Nu_WToLNu_M125']     .extend( ['xsec=0.002124',      'kfact=1.000',  'ref=F'] )  

# ZH -  XS = 0.8824 pb 
# XS(ggZH) = 0.1227 pb
# XS(HZJ)  = 0.8824 - 0.1227 = 0.7597 pb
# 0.7597*0.2152
samples['HZJ_HToWW_M125']    	        	.extend( ['xsec=0.1635',	'kfact=1.000',	'ref=F'] )
# 0.7597*0.2152*(3*0.033658)*(3*0.108)*(3*0.108)
samples['HZJ_HToWWTo2L2Nu_ZTo2L_M125']    	.extend( ['xsec=0.0017329',	'kfact=1.000',	'ref=F'] )

# 0.1227*0.2152
samples['ggZH_HToWW_M125']        		.extend( ['xsec=0.0264',	'kfact=1.000',	'ref=F'] )
# 0.1227*0.2152*(3*0.033658)*(3*0.108)*(3*0.108)
samples['ggZH_HToWWTo2L2Nu_ZTo2L_M125']         .extend( ['xsec=0.000279889',   'kfact=1.000',  'ref=F'] )

samples['GluGluHToZZTo4L_MiNLOHJJ_M125']            .extend( ['xsec=1',         'kfact=1.000',  'ref=X'] )
samples['GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Up']  .extend( ['xsec=1',         'kfact=1.000',  'ref=X'] )
samples['GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Down'].extend( ['xsec=1',         'kfact=1.000',  'ref=X'] )

# ttH - XS = 0.5065
# 0.5065*(1-0.5809)
samples['ttHToNonbb_M125']       		.extend( ['xsec=0.2123',	'kfact=1.000',	'ref=F'] )


# Additional Higgs signals with non-SM parameters 
# All XS set to 1. I haven't even looked at them
Samples['H0PM_ToWWTo2L2Nu']                     .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0PH_ToWWTo2L2Nu']                     .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0PHf05_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0M_ToWWTo2L2Nu']                      .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0Mf05_ToWWTo2L2Nu']                   .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0L1_ToWWTo2L2Nu']                     .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['H0L1f05_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )

Samples['VBF_H0PM_ToWWTo2L2Nu']                 .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0PH_ToWWTo2L2Nu']                 .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0PHf05_ToWWTo2L2Nu']              .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0M_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0Mf05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0L1_ToWWTo2L2Nu']                 .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['VBF_H0L1Zgf05_ToWWTo2L2Nu']            .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )

Samples['WH_H0PM_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0PH_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0PHf05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0M_ToWWTo2L2Nu']                   .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0Mf05_ToWWTo2L2Nu']                .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0L1_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['WH_H0L1f05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )

Samples['ZH_H0PM_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0PH_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0PHf05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0M_ToWWTo2L2Nu']                   .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0Mf05_ToWWTo2L2Nu']                .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0L1_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0L1f05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ZH_H0LZgf05_ToWWTo2L2Nu']              .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )

Samples['GGHjj_H0PM_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['GGHjj_H0M_ToWWTo2L2Nu']                .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['GGHjj_H0Mf05_ToWWTo2L2Nu']             .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )

Samples['ttH_H0PM_ToWWTo2L2Nu']                 .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ttH_H0M_ToWWTo2L2Nu']                  .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )
Samples['ttH_H0Mf05_ToWWTo2L2Nu']               .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] )        

samples['SSWW']                                 .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )

samples['VBS_SSWW_cW_INT']                      .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )
samples['VBS_SSWW_cW_BSM']                      .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )
samples['VBS_SSWW_cHW_INT']                     .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )
samples['VBS_SSWW_cHW_BSM']                     .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )
samples['VBS_SSWW_cW_cHW']                      .extend( ['xsec=1',             'kfact=1.000',  'ref=W'] )
