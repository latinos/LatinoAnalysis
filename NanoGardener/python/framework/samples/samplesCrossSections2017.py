# Cross section DB
# Units in pb
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
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
#       Z       H mumu AN (for synch)
#	X	Unknown! - Cross section not yet there


## W+jets
samples['WJetsToLNu']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO-ext']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO_ext1']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu_HT100_200']        	.extend( ['xsec=1395.00',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT100_200_ext1']      .extend( ['xsec=1395.00',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT100_200_ext2']      .extend( ['xsec=1395.00',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT200_400']        	.extend( ['xsec=407.9',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT200_400_ext1']      .extend( ['xsec=407.9',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT200_400_ext2']      .extend( ['xsec=407.9',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT400_600']        	.extend( ['xsec=57.48',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT400_600_ext1']      .extend( ['xsec=57.48',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT600_inf']        	.extend( ['xsec=18.7700',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT600_800']        	.extend( ['xsec=12.87',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT600_800_ext1']      .extend( ['xsec=12.87',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT800_1200']       	.extend( ['xsec=5.366',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT800_1200_ext1']  	.extend( ['xsec=5.366',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT1200_2500']      	.extend( ['xsec=1.074',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT1200_2500_ext1']    .extend( ['xsec=1.074',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT2500_inf']       	.extend( ['xsec=0.008001',	'kfact=1.21',		'ref=W'] )
samples['WJetsToLNu_HT2500_inf_ext1']     .extend( ['xsec=0.008001',	'kfact=1.21',		'ref=W'] )

samples['WJetsToLNu-0J'] .extend( ['xsec=54611.6',	'kfact=1.00',		'ref=I'] )
samples['WJetsToLNu-1J'] .extend( ['xsec=8966.2',	'kfact=1.00',		'ref=I'] )
samples['WJetsToLNu-2J'] .extend( ['xsec= 3643.12',	'kfact=1.00',		'ref=I'] )

## DY
samples['DYJetsToLL_M-10to50']        	   .extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50ext3']         .extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50']                 .extend( ['xsec=6189.39',    'kfact=1.000',          'ref=X'] ) # X = see https://hypernews.cern.ch/HyperNews/CMS/get/generators/4072.html 

samples['DYJetsToLL_M-50-UEup']                 .extend( ['xsec=6189.39',    'kfact=1.000',          'ref=X'] )
samples['DYJetsToLL_M-50-UEdo']                 .extend( ['xsec=6189.39',    'kfact=1.000',          'ref=X'] )
samples['DYJetsToLL_M-50-PSup']                 .extend( ['xsec=6189.39',    'kfact=1.000',          'ref=X'] )
samples['DYJetsToLL_M-50-PSdo']                 .extend( ['xsec=6189.39',    'kfact=1.000',          'ref=X'] )

samples['DYJetsToLL_M-5to50-LO']      	   .extend( ['xsec=81880.0',	'kfact=1.158',		'ref=W'] )
samples['DYJetsToLL_M-10to50-LO']          .extend( ['xsec=18610.0',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-10to50-LO_ext1']     .extend( ['xsec=18610.0',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-10to50-LO-ext1']     .extend( ['xsec=18610.0',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO']      	   .extend( ['xsec=6025.20',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50-LO_ext1']         .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO-ext1']         .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50_HT-70to100']      .extend( ['xsec=169.9',	'kfact=1.158',	'ref=I'] ) 
samples['DYJetsToLL_M-50_HT-100to200']     .extend( ['xsec=161.1',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-100to200_ext1'].extend( ['xsec=161.1',	'kfact=1.158',	'ref=W'] )  
samples['DYJetsToLL_M-50_HT-200to400']     .extend( ['xsec=48.66',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-200to400_ext1'].extend( ['xsec=48.66',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-400to600']     .extend( ['xsec=6.968',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-400to600_ext1'].extend( ['xsec=6.968',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-600toInf']     .extend( ['xsec=2.198',	'kfact=1.158',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-600toInf_ext1'].extend( ['xsec=2.198',	'kfact=1.158',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-600to800']     .extend( ['xsec=1.743',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-800to1200']    .extend( ['xsec=0.8052',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-1200to2500']   .extend( ['xsec=0.1933',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-2500toInf']    .extend( ['xsec=0.003468',	'kfact=1.158',	'ref=W'] ) 
samples['DYJetsToEE_Pow']                  .extend( ['xsec=1997',       'kfact=1.000',          'ref=E'] )
samples['DYJetsToTT_MuEle_M-50']           .extend( ['xsec=255.630',    'kfact=1.000',          'ref=X'] )  # (6025.20/3)*(0.352)^2
samples['DYJetsToTT_MuEle_M-50_ext1']           .extend( ['xsec=255.630',    'kfact=1.000',          'ref=X'] )  # (6025.20/3)*(0.352)^2
samples['DYJetsToTT_MuEle_M-50_PSWeights']           .extend( ['xsec=255.630',    'kfact=1.000',          'ref=X'] )  # (6025.20/3)*(0.352)^2

## DY (Low mass)
samples['DYJetsToLL_M-5to50_HT-70to100']   .extend( ['xsec=303.8',  'kfact=1.000',          'ref=I'] )
samples['DYJetsToLL_M-5to50_HT-100to200']  .extend( ['xsec=224.2',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-200to400']  .extend( ['xsec=37.2',   'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-400to600']  .extend( ['xsec=3.581',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-600toInf']  .extend( ['xsec=1.124',  'kfact=1.000',          'ref=E'] )

samples['DYJetsToLL_M-4to50_HT-100to200']       .extend( ['xsec=204.',   'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-100to200_ext1']  .extend( ['xsec=204.',   'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-100to200-ext1']  .extend( ['xsec=204.',   'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-200to400']       .extend( ['xsec=54.39',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-200to400_ext1']  .extend( ['xsec=54.39',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-200to400-ext1']  .extend( ['xsec=54.39',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-400to600']       .extend( ['xsec=5.697',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-400to600_ext1']  .extend( ['xsec=5.697',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-400to600-ext1']  .extend( ['xsec=5.697',  'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-600toInf']       .extend( ['xsec=1.85',   'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-600toInf_ext1']  .extend( ['xsec=1.85',   'kfact=1.000',          'ref=W'] )
samples['DYJetsToLL_M-4to50_HT-600toInf-ext1']  .extend( ['xsec=1.85',   'kfact=1.000',          'ref=W'] )

samples['DYJetsToLL_M-105To160']                .extend( ['xsec=47.12',  'kfact=1.000',          'ref=Z'] ) 


## VV 
samples['WW-LO']                        .extend( ['xsec=114.726',       'kfact=1.000',          'ref=E'] )  # 118.7 from E - 3.974 still from E
samples['WWTo2L2Nu']	             	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )		
samples['WWTo2L2Nu_PrivateNano']      	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )	
samples['WWJTo2L2Nu_NNLOPS']	             	.extend( ['xsec=1.3273',	'kfact=1.000',		'ref=I'] )		
samples['WWTo2L2Nu_CP5Up']             	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )		
samples['WWTo2L2Nu_CP5Down']             	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )		
samples['WWTo2L2Nu_aTGC_0-400']       	.extend( ['xsec=13.84637',	'kfact=1.000',		'ref=X'] )  # X = Guillelmo :)		
samples['WWTo2L2Nu_aTGC_400-600']      	.extend( ['xsec=1.31589',	'kfact=1.000',		'ref=X'] )		
samples['WWTo2L2Nu_aTGC_600-800']      	.extend( ['xsec=0.339499',	'kfact=1.000',		'ref=X'] )		
samples['WWTo2L2Nu_aTGC_800-Inf']      	.extend( ['xsec=0.241369',	'kfact=1.000',		'ref=X'] )		
samples['WWToLNuQQ']	             	.extend( ['xsec=49.997',	'kfact=1.000',		'ref=E'] )	
samples['WWToLNuQQext']	             	.extend( ['xsec=49.997',	'kfact=1.000',		'ref=E'] )
samples['WWTo4Q'] 	             	.extend( ['xsec=51.723',	'kfact=1.000',		'ref=E'] )
samples['WWTo2L2NuHerwigPS']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )	
samples['WWTo2L2Nu_CUETUp']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )
samples['WWTo2L2Nu_CUETDown']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )
samples['WZ']			        .extend( ['xsec=47.130',	'kfact=1.000',		'ref=E'] )
samples['WZTo3LNu']		        .extend( ['xsec=4.42965',	'kfact=1.000',		'ref=E'] )
samples['WZTo3LNu_noPSweights']		.extend( ['xsec=4.42965',	'kfact=1.000',		'ref=E'] )
samples['WZTo3LNu_mllmin01']	        .extend( ['xsec=58.59',		'kfact=0.601644',	'ref=N'] ) # kfact from gen-level Z0 comparision to WZTo3LNu
samples['WZTo3LNu_mllmin01_ext1']	.extend( ['xsec=58.59',		'kfact=0.601644',	'ref=N'] ) # kfact from gen-level Z0 comparision to WZTo3LNu
samples['WZJets']		        .extend( ['xsec=5.2890',	'kfact=1.000',		'ref=E'] ) 
samples['WZTo2L2Q']		        .extend( ['xsec=5.5950',	'kfact=1.000',		'ref=E'] )
samples['WZTo1L3Nu']                    .extend( ['xsec=3.033',         'kfact=1.000',          'ref=E'] )  # err 0.00206
samples['WZTo1L1Nu2Q']                  .extend( ['xsec=10.71',         'kfact=1.000',          'ref=E'] )
samples['VVTo2L2Nu']		        .extend( ['xsec=11.950',	'kfact=1.000',		'ref=E'] )
samples['VVTo2L2Nu_ext1']		        .extend( ['xsec=11.950',	'kfact=1.000',		'ref=E'] )


## ZZ
samples['ZZ']                           .extend( ['xsec=16.52300',	'kfact=1.000',		'ref=E'] )
samples['ZZTo2L2Q']                     .extend( ['xsec=3.220000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L']                       .extend( ['xsec=1.212000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L_ext1']                  .extend( ['xsec=1.212000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L_new_pmx']               .extend( ['xsec=1.212000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo2L2Nu']                    .extend( ['xsec=0.564000',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4e']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4m']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4m_ext1']                  .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4m_v2']                    .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4t']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2m']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2m_ext1']                .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2m_v3']                  .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2t']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2t_v3']                  .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2t_ext1']                .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2t']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2t_ext1']                .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2t_CP5']                 .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2n']                     .extend( ['xsec=0.001493',	'kfact=1.000',		'ref=Z'] )
samples['ggZZ2m2n_ext1']                .extend( ['xsec=0.001493',	'kfact=1.000',		'ref=Z'] )
samples['ggZZ2e2n']                     .extend( ['xsec=0.001493',	'kfact=1.000',		'ref=Z'] )
samples['ggZZ2e2n_ext1']                .extend( ['xsec=0.001493',	'kfact=1.000',		'ref=Z'] )
samples['ZZJJTo4L_EWK']                 .extend( ['xsec=0.0004453',	'kfact=1.000',		'ref=E'] )

## Single top
samples['ST_t-channel_antitop']         .extend( ['xsec=26.38',		'kfact=1.000',		'ref=E'] )
samples['ST_t-channel_top']             .extend( ['xsec=44.33',		'kfact=1.000',		'ref=E'] )
samples['ST_t-channel']                 .extend( ['xsec=70.69',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_antitop']                .extend( ['xsec=35.60',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_top']                    .extend( ['xsec=35.60',		'kfact=1.000',		'ref=E'] )
samples['ST_s-channel']                 .extend( ['xsec=3.360',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_antitop_noHad']          .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_antitop_noHad_ext1']          .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_top_noHad']              .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_top_noHad_ext1']              .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )

samples['ST_t-channel_antitop_5f']        .extend( ['xsec=80.95',         'kfact=1.000',          'ref=Z'] )
samples['ST_t-channel_antitop_5f_new_pmx'].extend( ['xsec=80.95',         'kfact=1.000',          'ref=Z'] )

samples['ST_tW_antitop_PSweights']        .extend( ['xsec=35.90',         'kfact=1.000',           'ref=Z'] )
samples['ST_tW_top_PSweights']            .extend( ['xsec=35.90',         'kfact=1.000',           'ref=Z'] )

samples['ST_t-channel_top_5f_new_pmx']    .extend( ['xsec=136.02',         'kfact=1.000',          'ref=Z'] )
samples['ST_t-channel_top_5f']            .extend( ['xsec=136.02',         'kfact=1.000',          'ref=Z'] )

samples['ST_s-channel_top']               .extend( ['xsec=2.069',         'kfact=1.000',           'ref=Z'] )
samples['ST_s-channel_antitop']           .extend( ['xsec=1.293',         'kfact=1.000',           'ref=Z'] )


## Top
samples['TT']                           .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTJets']                       .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTJets_more']                  .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu'] 	             	.extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_PSWeights'] 	             	.extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_PSWeights_CP5Up'] 	             	.extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_PSWeights_CP5Down'] 	             	.extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_ext1']               .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTJetsDiLep-LO']               .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTJetsDiLep-LO_ext1']          .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTWJetsToLNu']                 .extend( ['xsec=0.2043',	'kfact=1.000',		'ref=E'] )	
samples['TTWJetsToLNu_ext2']            .extend( ['xsec=0.2043',	'kfact=1.000',		'ref=E'] )	
samples['TTZToLLNuNu_M-10']             .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToLLNuNu_M-10_PSweights']   .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToQQ']                      .extend( ['xsec=0.5297',        'kfact=1.000',          'ref=E'] )
samples['TTZjets']                      .extend( ['xsec=0.7826',        'kfact=1.000',          'ref=X'] )
samples['TTZjets_ext1']                      .extend( ['xsec=0.7826',        'kfact=1.000',          'ref=X'] )
samples['TTWJetsToQQ']                  .extend( ['xsec=0.4062',        'kfact=1.000',          'ref=E'] )  
samples['TTWjets']                      .extend( ['xsec=0.6105',        'kfact=1.000',          'ref=E'] )  # 0.0462 + 0.2043
samples['TTWjets_ext1']                      .extend( ['xsec=0.6105',        'kfact=1.000',          'ref=E'] )  # 0.0462 + 0.2043
samples['TTTo2L2Nu_alphaS01108']        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTToSemiLeptonic']             .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TTToSemiLeptonic_PSweights']   .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TTToSemiLeptonic_alphaS01108'] .extend( ['xsec=364.35',	'kfact=1.000',		'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2

samples['TTWJetsToLNu_PSweights']               .extend( ['xsec=0.2001',	'kfact=1.000',	        'ref=Z'] )
samples['TTWJetsToLNu_PSweights_new_pmx']       .extend( ['xsec=0.2001',	'kfact=1.000',	        'ref=Z'] )


## GluGluWW
samples['GluGluWWTo2L2Nu_MCFM']      	.extend( ['xsec=0.5905',	'kfact=1.000',		'ref=E'] ) # 1.4*3.974*0.1086*.1086*9 --> 1.4 is a k-factor, 3.974 comes from the comment on the qqWW samples in reference E
samples['GluGluWWTo2L2NuHiggs_MCFM'] 	.extend( ['xsec=0.9544',	'kfact=1.000',		'ref=X'] ) # 1.4*0.6817 --> 1.4 is the same k-factor, 0.6817 is 0.07574*9, first number comes from MCFM, 9 is the lepton combinations
samples['GluGluToWWToENEN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToENMN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToENTN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToMNEN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToMNMN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToMNTN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToTNEN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToTNMN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)
samples['GluGluToWWToTNTN']      	.extend( ['xsec=0.06387',	'kfact=1.000',		'ref=I'] ) # 1.4*0.04562 --> 1.4 is a k-factor, 0.04562 comes from MCFM (GenXsecAnalyzer result divided by 1000)


## ggH,HWW
samples['GluGluHToWWTo2L2Nu_Mlarge']  	        .extend( ['xsec=0.6818',	'kfact=1.000',  'ref=X']  ) # 10GeV Higgs width 30.21(powheg)*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_alternative_M120']  .extend( ['xsec=0.9818',	'kfact=1.000',	'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M125']  .extend( ['xsec=0.9913',	'kfact=1.000',	'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M130']  .extend( ['xsec=0.9081',	'kfact=1.000',	'ref=X']  ) # 28.55(powheg)*0.303*0.108*0.108*9

samples['GluGluHToWWTo2L2Nu_M115']  	.extend( ['xsec=0.4842',	'kfact=1.000',		'ref=Y'] ) # 53.10*0.0859*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M120']  	.extend( ['xsec=0.7319',	'kfact=1.000',		'ref=Y'] ) # 48.90*0.141*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M124']      .extend( ['xsec=0.9698',	'kfact=1.000',		'ref=Y'] ) # 45.91*0.199*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M125']      .extend( ['xsec=1.0315',	'kfact=1.000',		'ref=Y'] ) # 45.20*0.215*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M125_PrivateNano']      .extend( ['xsec=1.0315',	'kfact=1.000',		'ref=Y'] ) # 45.20*0.215*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M126']      .extend( ['xsec=1.0909',	'kfact=1.000',		'ref=Y'] ) # 44.49*0.231*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M130']      .extend( ['xsec=1.3444',	'kfact=1.000',		'ref=Y'] ) # 41.80*0.303*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M135']      .extend( ['xsec=1.6474',	'kfact=1.000',		'ref=Y'] ) # 38.80*0.400*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M140']      .extend( ['xsec=1.9144',	'kfact=1.000',		'ref=Y'] ) # 36.00*0.501*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M145']      .extend( ['xsec=2.1335',	'kfact=1.000',		'ref=Y'] ) # 33.50*0.600*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M150']      .extend( ['xsec=2.3116',	'kfact=1.000',		'ref=Y'] ) # 31.29*0.696*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M155']      .extend( ['xsec=2.4683',	'kfact=1.000',		'ref=Y'] ) # 29.25*0.795*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M160']      .extend( ['xsec=2.6379',	'kfact=1.000',		'ref=Y'] ) # 27.37*0.908*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M165']      .extend( ['xsec=2.6147',	'kfact=1.000',		'ref=Y'] ) # 25.66*0.960*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M170']      .extend( ['xsec=2.4650',	'kfact=1.000',		'ref=Y'] ) # 24.09*0.964*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M175']      .extend( ['xsec=2.3032',	'kfact=1.000',		'ref=Y'] ) # 22.65*0.958*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M180']      .extend( ['xsec=2.1091',	'kfact=1.000',		'ref=Y'] ) # 21.32*0.932*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M190']      .extend( ['xsec=1.5818',	'kfact=1.000',		'ref=Y'] ) # 18.96*0.786*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M200']      .extend( ['xsec=1.3324',	'kfact=1.000',		'ref=Y'] ) # 16.94*0.741*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M210']      .extend( ['xsec=1.1665',	'kfact=1.000',		'ref=Y'] ) # 15.20*0.723*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M230']      .extend( ['xsec=0.9296',	'kfact=1.000',		'ref=Y'] ) # 12.37*0.708*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M250']      .extend( ['xsec=0.7590',	'kfact=1.000',		'ref=Y'] ) # 10.20*0.701*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M270']      .extend( ['xsec=0.6296',	'kfact=1.000',		'ref=Y'] ) # 8.510*0.697*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M300']      .extend( ['xsec=0.4841',	'kfact=1.000',		'ref=Y'] ) # 6.590*0.692*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M350']      .extend( ['xsec=0.3216',	'kfact=1.000',		'ref=Y'] ) # 4.480*0.676*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M400']      .extend( ['xsec=0.1952',	'kfact=1.000',		'ref=Y'] ) # 3.160*0.582*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M450']      .extend( ['xsec=0.1345',	'kfact=1.000',		'ref=Y'] ) # 2.300*0.551*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M500']      .extend( ['xsec=0.0990',	'kfact=1.000',		'ref=Y'] ) # 1.709*0.546*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M550']      .extend( ['xsec=0.0757',	'kfact=1.000',		'ref=Y'] ) # 1.297*0.550*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M600']      .extend( ['xsec=0.0593',	'kfact=1.000',		'ref=Y'] ) # 1.001*0.558*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M650']      .extend( ['xsec=0.0472',	'kfact=1.000',		'ref=Y'] ) # 0.7834*0.568*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M700']      .extend( ['xsec=0.0380',	'kfact=1.000',		'ref=Y'] ) # 0.6206*0.577*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M750']      .extend( ['xsec=0.0309',	'kfact=1.000',		'ref=Y'] ) # 0.4969*0.586*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M750_NWA']  .extend( ['xsec=0.0283',	'kfact=1.000',		'ref=Y'] ) # 0.460*0.586*0.1086*0.1086*9 - shall we keep the same BR for NWA?
samples['GluGluHToWWTo2L2Nu_M800']      .extend( ['xsec=0.0253',	'kfact=1.000',		'ref=Y'] ) # 0.4015*0.594*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M900']      .extend( ['xsec=0.0174',	'kfact=1.000',		'ref=Y'] ) # 0.2685*0.609*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M1000']     .extend( ['xsec=0.0122',	'kfact=1.000',		'ref=Y'] ) # 0.1845*0.621*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M1500']     .extend( ['xsec=0.00243',       'kfact=1.000',          'ref=Y'] ) # 0.0369*0.621*0.1086*0.1086*9 ###Note: BR for masses larger than 1 TeV are not given, so use that of 1 TeV instead (seems to be conservative anyway?)
samples['GluGluHToWWTo2L2Nu_M2000']     .extend( ['xsec=0.000633',       'kfact=1.000',          'ref=Y'] ) # 0.00960*0.621*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M2500']     .extend( ['xsec=0.000190',       'kfact=1.000',          'ref=Y'] ) # 0.00289*0.621*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M3000']     .extend( ['xsec=0.000062',      'kfact=1.000',          'ref=Y'] ) # 0.00094*0.621*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M4000']     .extend( ['xsec=0.0000075',      'kfact=1.000',          'ref=Y'] ) # 0.000114*0.621*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M5000']     .extend( ['xsec=0.00000092',      'kfact=1.000',          'ref=Y'] ) # 0.000014*0.621*0.1086*0.1086*9

samples['GluGluHToWWTo2L2Nu_JHUGen698_M300']      .extend( ['xsec=0.5731',      'kfact=1.000',          'ref=KF'] ) # 7.89*0.692*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M350']      .extend( ['xsec=0.5698',      'kfact=1.000',          'ref=KF'] ) # 8.03*0.676*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M400']      .extend( ['xsec=0.4360',      'kfact=1.000',          'ref=KF'] ) # 7.136*0.582*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M450']      .extend( ['xsec=0.2926',      'kfact=1.000',          'ref=KF'] ) # 5.059*0.551*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M500']      .extend( ['xsec=0.1926',      'kfact=1.000',          'ref=KF'] ) # 3.360*0.546*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M550']      .extend( ['xsec=0.1275',      'kfact=1.000',          'ref=KF'] ) # 2.209*0.550*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M600']      .extend( ['xsec=0.08599',     'kfact=1.000',          'ref=KF'] ) # 1.468*0.558*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M650']      .extend( ['xsec=0.0593',      'kfact=1.000',          'ref=KF'] ) # 0.994*0.568*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M700']      .extend( ['xsec=0.0416',      'kfact=1.000',          'ref=KF'] ) # 0.687*0.577*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M750']      .extend( ['xsec=0.0298',      'kfact=1.000',          'ref=KF'] ) # 0.485*0.586*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M800']      .extend( ['xsec=0.0218',      'kfact=1.000',          'ref=KF'] ) # 0.3493*0.594*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M900']      .extend( ['xsec=0.0123',      'kfact=1.000',          'ref=KF'] ) # 0.1920*0.609*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M1000']     .extend( ['xsec=0.0073',      'kfact=1.000',          'ref=KF'] ) # 0.1128*0.621*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M1500']     .extend( ['xsec=0.00096',     'kfact=1.000',          'ref=KF'] ) # 0.01465*0.621*0.108*0.108*9        
samples['GluGluHToWWTo2L2Nu_JHUGen698_M2000']     .extend( ['xsec=0.00041',     'kfact=1.000',          'ref=KF'] ) # 0.006227*0.621*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M2500']     .extend( ['xsec=0.00016',     'kfact=1.000',          'ref=KF'] ) # 0.002515*0.621*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_JHUGen698_M3000']     .extend( ['xsec=0.000078',     'kfact=1.000',         'ref=KF'] ) # 0.001186*0.621*0.108*0.108*9

samples['GluGluHToWWTo2L2NuAMCNLO_M125']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_private']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_CP5Up']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_CP5Down']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuHerwigPS_M125'] .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9

samples['GluGluHToWWTo2L2Nu_M125_herwigpp']  .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['GluGluHToWWTo2L2Nu_M125_CUETUp']  .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['GluGluHToWWTo2L2Nu_M125_CUETDown'].extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value

samples['GluGluHToWWToLNuQQ_M115']  	.extend( ['xsec=1.0018',	'kfact=1.000',		'ref=Y'] ) # 53.10*0.0859*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M120']  	.extend( ['xsec=1.5143',	'kfact=1.000',		'ref=Y'] ) # 48.90*0.141*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M124']      .extend( ['xsec=2.0065',	'kfact=1.000',		'ref=Y'] ) # 45.91*0.199*0.1086*3*0.6741 ### Interpolated Xsec
samples['GluGluHToWWToLNuQQ_M125']      .extend( ['xsec=2.1343',	'kfact=1.000',		'ref=Y'] ) # 45.20*0.215*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M126']      .extend( ['xsec=2.2571',	'kfact=1.000',		'ref=Y'] ) # 44.49*0.231*0.1086*3*0.6741 ### Interpolated Xsec
samples['GluGluHToWWToLNuQQ_M130']      .extend( ['xsec=2.7816',	'kfact=1.000',		'ref=Y'] ) # 41.80*0.303*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M135']      .extend( ['xsec=3.4085',	'kfact=1.000',		'ref=Y'] ) # 38.80*0.400*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M140']      .extend( ['xsec=3.9611',	'kfact=1.000',		'ref=Y'] ) # 36.00*0.501*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M145']      .extend( ['xsec=4.4144',	'kfact=1.000',		'ref=Y'] ) # 33.50*0.600*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M150']      .extend( ['xsec=4.7829',	'kfact=1.000',		'ref=Y'] ) # 31.29*0.696*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M155']      .extend( ['xsec=5.1070',	'kfact=1.000',		'ref=Y'] ) # 29.25*0.795*0.1086*3*0.6741 ### Interpolated Xsec
samples['GluGluHToWWToLNuQQ_M160']      .extend( ['xsec=5.5480',	'kfact=1.000',		'ref=Y'] ) # 27.37*0.908*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M165']      .extend( ['xsec=5.4101',	'kfact=1.000',		'ref=Y'] ) # 25.66*0.960*0.1086*3*0.6741 ### Interpolated Xsec
samples['GluGluHToWWToLNuQQ_M170']      .extend( ['xsec=5.1002',	'kfact=1.000',		'ref=Y'] ) # 24.09*0.964*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M175']      .extend( ['xsec=4.7655',	'kfact=1.000',		'ref=Y'] ) # 22.65*0.958*0.1086*3*0.6741 ### Interpolated Xsec
samples['GluGluHToWWToLNuQQ_M180']      .extend( ['xsec=4.3639',	'kfact=1.000',		'ref=Y'] ) # 21.32*0.932*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M190']      .extend( ['xsec=3.2729',	'kfact=1.000',		'ref=Y'] ) # 18.96*0.786*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M200']      .extend( ['xsec=2.7568',	'kfact=1.000',		'ref=Y'] ) # 16.94*0.741*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M210']      .extend( ['xsec=2.4136',	'kfact=1.000',		'ref=Y'] ) # 15.20*0.723*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M230']      .extend( ['xsec=1.9234',	'kfact=1.000',		'ref=Y'] ) # 12.37*0.708*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M250']      .extend( ['xsec=1.5703',	'kfact=1.000',		'ref=Y'] ) # 10.20*0.701*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M270']      .extend( ['xsec=1.3027',	'kfact=1.000',		'ref=Y'] ) # 8.510*0.697*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M300']      .extend( ['xsec=1.0015',	'kfact=1.000',		'ref=Y'] ) # 6.590*0.692*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M350']      .extend( ['xsec=0.6651',	'kfact=1.000',		'ref=Y'] ) # 4.480*0.676*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M400']      .extend( ['xsec=0.4039',	'kfact=1.000',		'ref=Y'] ) # 3.160*0.582*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M450']      .extend( ['xsec=0.2783',     	'kfact=1.000',		'ref=Y'] ) # 2.300*0.551*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M500']      .extend( ['xsec=0.2049',	'kfact=1.000',		'ref=Y'] ) # 1.709*0.546*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M550']      .extend( ['xsec=0.1567',	'kfact=1.000',		'ref=Y'] ) # 1.297*0.550*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M600']      .extend( ['xsec=0.1227',	'kfact=1.000',		'ref=Y'] ) # 1.001*0.558*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M650']      .extend( ['xsec=0.0977',     	'kfact=1.000',		'ref=Y'] ) # 0.7834*0.568*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M700']      .extend( ['xsec=0.0786',	'kfact=1.000',		'ref=Y'] ) # 0.6206*0.577*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M750']      .extend( ['xsec=0.0639',	'kfact=1.000',		'ref=Y'] ) # 0.4969*0.586*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M750_NWA']  .extend( ['xsec=0.0589',	'kfact=1.000',		'ref=Y'] ) # 0.460*0.586*0.1086*3*0.6741 - shall we keep the same BR for NWA?
samples['GluGluHToWWToLNuQQ_M800']      .extend( ['xsec=0.0524',	'kfact=1.000',		'ref=Y'] ) # 0.4015*0.594*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M900']      .extend( ['xsec=0.0359',	'kfact=1.000',		'ref=Y'] ) # 0.2685*0.609*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M1000']     .extend( ['xsec=0.0252',     	'kfact=1.000',		'ref=Y'] ) # 0.1845*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M1500']     .extend( ['xsec=0.00503',        'kfact=1.000',          'ref=Y'] ) # 0.0369*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M2000']     .extend( ['xsec=0.00131',       'kfact=1.000',          'ref=Y'] ) # 0.00960*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M2500']     .extend( ['xsec=0.000394',       'kfact=1.000',          'ref=Y'] ) # 0.00289*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M3000']     .extend( ['xsec=0.000128',       'kfact=1.000',          'ref=Y'] ) # 0.00094*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M4000']     .extend( ['xsec=0.0000115',      'kfact=1.000',          'ref=Y'] ) # 0.000114*0.621*0.1086*3*0.6741
samples['GluGluHToWWToLNuQQ_M5000']     .extend( ['xsec=0.0000019',      'kfact=1.000',          'ref=Y'] ) # 0.000014*0.621*0.1086*3*0.6741

samples['GluGluHToZZTo4L_M125']		.extend( ['xsec=0.0118',     	'kfact=1.000',		'ref=CF'] ) # 43.92*0.0264*0.033658*0.033658*9
samples['GluGluHToTauTau_M120']		.extend( ['xsec=2.2676',     	'kfact=1.000',		'ref=KF'] ) # 32.21*0.0704
samples['GluGluHToTauTau_M125']		.extend( ['xsec=2.7757',     	'kfact=1.000',		'ref=CF'] ) # 43.92*0.0632
samples['GluGluHToTauTau_M130']		.extend( ['xsec=1.5260',     	'kfact=1.000',		'ref=KF'] ) # 28.00*0.0545

samples['GluGluHToWWTo2L2Nu_M125_minloHJ_NNLOPS']   .extend( ['xsec=0.9913',  'kfact=1.000',    'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value

samples['GGHjjToWWTo2L2Nu_minloHJJ_M125']   .extend( ['xsec=0.8962',  'kfact=1.000',    'ref=I'] ) # 39.71*0.215*0.108*0.108*9 (39.71 from GenXSecAnalyzer)

## ggH H MuMu

samples['GluGluHToMuMu_M125_CP5']             .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_CP5_ext1']        .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_CP5up']           .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_CP5down']         .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_powheg_CP5']      .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_powheg_CP5_ext1'] .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_powheg_CP5up']    .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}
samples['GluGluHToMuMu_M125_powheg_CP5down']  .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4}

## W+H
samples['HWplusJ_HToWW_M120']          	.extend( ['xsec=0.1350',	'kfact=1.000',	       	'ref=EF'] ) # 0.956*0.141
samples['HWplusJ_HToWW_M125']          	.extend( ['xsec=0.1810',	'kfact=1.000',	       	'ref=EF'] ) # 0.842*0.215
samples['HWplusJ_HToWW_M125_PrivateNano']          	.extend( ['xsec=0.1810',	'kfact=1.000',	       	'ref=EF'] ) # 0.842*0.215
samples['HWplusJ_HToWW_M130']          	.extend( ['xsec=0.2250',	'kfact=1.000',	       	'ref=EF'] ) # 0.743*0.303

samples['WPlusH_HToMuMu_M125']          .extend( ['xsec=0.00018278400', 'kfact=1.000',          'ref=FT'] ) # 0.840*2.176*10^{-4}
samples['WPlusH_HToMuMu_M125_CP5up']    .extend( ['xsec=0.00018278400', 'kfact=1.000',          'ref=FT'] ) # 0.840*2.176*10^{-4}
samples['WPlusH_HToMuMu_M125_CP5down']  .extend( ['xsec=0.00018278400', 'kfact=1.000',          'ref=FT'] ) # 0.840*2.176*10^{-4}

## W-H
samples['HWminusJ_HToWW_M120']       	.extend( ['xsec=0.0866',     	'kfact=1.000',		'ref=EF'] ) # 0.614*0.141
samples['HWminusJ_HToWW_M125']  	.extend( ['xsec=0.1160',     	'kfact=1.000',		'ref=EF'] ) # 0.539*0.215
samples['HWminusJ_HToWW_M125_PrivateNano']  	.extend( ['xsec=0.1160',     	'kfact=1.000',		'ref=EF'] ) # 0.539*0.215
samples['HWminusJ_HToWW_M130'] 		.extend( ['xsec=0.1430',     	'kfact=1.000',		'ref=EF'] ) # 0.472*0.303

samples['WMinusH_HToMuMu_M125']         .extend( ['xsec=0.00011593728', 'kfact=1.000',          'ref=FT'] ) # 0.5328*2.176*10^{-4}
samples['WMinusH_HToMuMu_M125_CP5up']   .extend( ['xsec=0.00011593728', 'kfact=1.000',          'ref=FT'] ) # 0.5328*2.176*10^{-4}
samples['WMinusH_HToMuMu_M125_CP5down'] .extend( ['xsec=0.00011593728', 'kfact=1.000',          'ref=FT'] ) # 0.5328*2.176*10^{-4}

## Tau+H
samples['HWplusJ_HToTauTau_M120']	.extend( ['xsec=0.0673',     	'kfact=1.000',		'ref=EF'] ) # 0.956*0.0704
samples['HWplusJ_HToTauTau_M125']	.extend( ['xsec=0.0532',     	'kfact=1.000',		'ref=EF'] ) # 0.842*0.0632
samples['HWplusJ_HToTauTau_M130']	.extend( ['xsec=0.0405',     	'kfact=1.000',		'ref=EF'] ) # 0.743*0.0545

## Tau-H
samples['HWminusJ_HToTauTau_M120']	.extend( ['xsec=0.0432',     	'kfact=1.000',		'ref=EF'] ) # 0.614*0.0704
samples['HWminusJ_HToTauTau_M125']	.extend( ['xsec=0.0341',     	'kfact=1.000',		'ref=EF'] ) # 0.539*0.0632
samples['HWminusJ_HToTauTau_M130']	.extend( ['xsec=0.0257',     	'kfact=1.000',		'ref=EF'] ) # 0.472*0.0545


# HZ
samples['HZJ_HToWW_M120']  	       	.extend( ['xsec=0.121',       	'kfact=1.000',	      	'ref=EF'] ) # 0.855*0.141
samples['HZJ_HToWW_M125']  	       	.extend( ['xsec=0.187',       	'kfact=1.000',	      	'ref=EF'] ) # 0.8696*0.215
samples['HZJ_HToWW_M125_PrivateNano']  	       	.extend( ['xsec=0.187',       	'kfact=1.000',	      	'ref=EF'] ) # 0.8696*0.215
samples['HZJ_HToWW_M130']  	       	.extend( ['xsec=0.202',       	'kfact=1.000',	      	'ref=EF'] ) # 0.667*0.303
samples['HZJ_HToTauTau_M120']		.extend( ['xsec=0.0602',     	'kfact=1.000',		'ref=EF'] ) # 0.855*0.0704 
samples['HZJ_HToTauTau_M125']		.extend( ['xsec=0.0550',     	'kfact=1.000',		'ref=EF'] ) # 0.8696*0.0632
samples['HZJ_HToTauTau_M130']		.extend( ['xsec=0.0363',     	'kfact=1.000',		'ref=EF'] ) # 0.667*0.0545


## ttH
samples['ttHJetToNonbb_M120']		.extend( ['xsec=0.1971',     	'kfact=1.000',		'ref=OE'] ) # 0.5697*(1-0.654)
samples['ttHJetToNonbb_M125']		.extend( ['xsec=0.2120',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*(1-0.582)
samples['ttHJetToNonbb_M130']		.extend( ['xsec=0.2279',     	'kfact=1.000',		'ref=OE'] ) # 0.4539*(1-0.498)
samples['ttHJetToNonbb_M125_A']		.extend( ['xsec=0.2120',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*(1-0.582)
samples['ttHJetTobb_M120']		.extend( ['xsec=0.3726',     	'kfact=1.000',		'ref=OE'] ) # 0.5697*0.654
samples['ttHJetTobb_M125']		.extend( ['xsec=0.2951',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*0.582
samples['ttHJetTobb_M130']		.extend( ['xsec=0.2260',     	'kfact=1.000',		'ref=OE'] ) # 0.4539*0.498
samples['ttHJetTobb_M125_A']		.extend( ['xsec=0.2951',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*0.582
samples['ttHJetTobb_M125_B']		.extend( ['xsec=0.2951',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*0.582
samples['ttHJetTobb_M125_C']		.extend( ['xsec=0.2951',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*0.582
samples['ttHToNonbb_M125']		.extend( ['xsec=0.2120',     	'kfact=1.000',		'ref=OE'] ) # 0.5071*(1-0.582)

samples['ttHToMuMu_M125_CP5']           .extend( ['xsec=0.00011034496', 'kfact=1.000',          'ref=FT'] ) # 0.5071*2.176*10^{-4}
samples['ttHToMuMu_M125_CP5up']         .extend( ['xsec=0.00011034496', 'kfact=1.000',          'ref=FT'] ) # 0.5071*2.176*10^{-4}
samples['ttHToMuMu_M125_CP5down']       .extend( ['xsec=0.00011034496', 'kfact=1.000',          'ref=FT'] ) # 0.5071*2.176*10^{-4}


#### bbH
samples['bbHToWWTo2L2Nu_M125_yb2']      .extend( ['xsec=0.00882255',	 'kfact=1.000',		'ref=N'] ) # 0.00882255 = 0.3909*0.215*0.108*0.108*9
samples['bbHToWWTo2L2Nu_M125_ybyt']     .extend( ['xsec=0.000743225',    'kfact=1.000',         'ref=N'] ) # 0.000743225 = -0.03293*0.215*0.108*0.108*9


## VBF
samples['VBFHToWWTo2L2Nu_alternative_M120']	.extend( ['xsec=0.0579',	'kfact=1.000',	'ref=EF'] ) # 3.91*0.141*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_alternative_M125']	.extend( ['xsec=0.0846',	'kfact=1.000',	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_alternative_M130']	.extend( ['xsec=0.1148',	'kfact=1.000',	'ref=EF'] ) # 3.61*0.303*0.108*0.108*9

samples['VBFHToWWTo2L2Nu_M115']		.extend( ['xsec=0.0388',	'kfact=1.000',		'ref=Y'] ) # 4.255*0.0859*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M120']		.extend( ['xsec=0.0612',	'kfact=1.000',		'ref=Y'] ) # 4.086*0.141*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M124']		.extend( ['xsec=0.0836',	'kfact=1.000',		'ref=Y'] ) # 3.956*0.199*0.1086*0.1086*9 ### Interpolated Xsec
samples['VBFHToWWTo2L2Nu_M125']		.extend( ['xsec=0.0896',	'kfact=1.000',		'ref=Y'] ) # 3.925*0.215*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M125_PrivateNano']		.extend( ['xsec=0.0896',	'kfact=1.000',		'ref=Y'] ) # 3.925*0.215*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M126']		.extend( ['xsec=0.0955',	'kfact=1.000',		'ref=Y'] ) # 3.894*0.231*0.1086*0.1086*9 ### Interpolated Xsec
samples['VBFHToWWTo2L2Nu_M130']		.extend( ['xsec=0.1213',	'kfact=1.000',		'ref=Y'] ) # 3.773*0.303*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M135']		.extend( ['xsec=0.1541',	'kfact=1.000',		'ref=Y'] ) # 3.629*0.400*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M140']		.extend( ['xsec=0.1857',	'kfact=1.000',		'ref=Y'] ) # 3.492*0.501*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M145']		.extend( ['xsec=0.2141',	'kfact=1.000',		'ref=Y'] ) # 3.362*0.600*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M150']		.extend( ['xsec=0.2393',	'kfact=1.000',		'ref=Y'] ) # 3.239*0.696*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M155']		.extend( ['xsec=0.2635',	'kfact=1.000',		'ref=Y'] ) # 3.122*0.795*0.1086*0.1086*9 ### Interpolated Xsec
samples['VBFHToWWTo2L2Nu_M160']		.extend( ['xsec=0.2901',	'kfact=1.000',		'ref=Y'] ) # 3.010*0.908*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M165']		.extend( ['xsec=0.2959',	'kfact=1.000',		'ref=Y'] ) # 2.904*0.960*0.1086*0.1086*9 ### Interpolated Xsec
samples['VBFHToWWTo2L2Nu_M170']		.extend( ['xsec=0.2867',	'kfact=1.000',		'ref=Y'] ) # 2.802*0.964*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M175']		.extend( ['xsec=0.2751',	'kfact=1.000',		'ref=Y'] ) # 2.705*0.958*0.1086*0.1086*9 ### Interpolated Xsec
samples['VBFHToWWTo2L2Nu_M180']		.extend( ['xsec=0.2584',	'kfact=1.000',		'ref=Y'] ) # 2.612*0.932*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M190']		.extend( ['xsec=0.2036',	'kfact=1.000',		'ref=Y'] ) # 2.440*0.786*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M200']		.extend( ['xsec=0.1795',	'kfact=1.000',		'ref=Y'] ) # 2.282*0.741*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M210']		.extend( ['xsec=0.1641',	'kfact=1.000',		'ref=Y'] ) # 2.138*0.723*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M230']		.extend( ['xsec=0.1416',	'kfact=1.000',		'ref=Y'] ) # 1.884*0.708*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M250']		.extend( ['xsec=0.1242',	'kfact=1.000',		'ref=Y'] ) # 1.669*0.701*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M270']		.extend( ['xsec=0.1099',	'kfact=1.000',		'ref=Y'] ) # 1.485*0.697*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M300']		.extend( ['xsec=0.0923',	'kfact=1.000',		'ref=Y'] ) # 1.256*0.692*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M350']		.extend( ['xsec=0.0694',	'kfact=1.000',		'ref=Y'] ) # 0.9666*0.676*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M400']		.extend( ['xsec=0.0468',	'kfact=1.000',		'ref=Y'] ) # 0.7580*0.582*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M450']		.extend( ['xsec=0.0353',	'kfact=1.000',		'ref=Y'] ) # 0.6038*0.551*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M500']		.extend( ['xsec=0.0282',	'kfact=1.000',		'ref=Y'] ) # 0.4872*0.546*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M550']		.extend( ['xsec=0.0232',	'kfact=1.000',		'ref=Y'] ) # 0.3975*0.550*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M600']		.extend( ['xsec=0.0194',	'kfact=1.000',		'ref=Y'] ) # 0.3274*0.558*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M650']		.extend( ['xsec=0.0164',	'kfact=1.000',		'ref=Y'] ) # 0.2719*0.568*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M700']		.extend( ['xsec=0.0139',	'kfact=1.000',		'ref=Y'] ) # 0.2275*0.577*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M750']		.extend( ['xsec=0.0117',	'kfact=1.000',		'ref=Y'] ) # 0.1915*0.577*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M750_NWA']	.extend( ['xsec=0.0113',	'kfact=1.000',		'ref=KF'] ) # 0.186*0.577*0.1086*0.1086*9 - shall we keep the same BR for NWA?
samples['VBFHToWWTo2L2Nu_M800']		.extend( ['xsec=0.0102',	'kfact=1.000',		'ref=Y'] ) # 0.1622*0.594*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M900']		.extend( ['xsec=0.00763',	'kfact=1.000',		'ref=Y'] ) # 0.1180*0.609*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M1000']	.extend( ['xsec=0.00576',	'kfact=1.000',		'ref=Y'] ) # 0.08732*0.621*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M1500']        .extend( ['xsec=0.00151',        'kfact=1.000',          'ref=Y'] ) # 0.02288*0.621*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M2000']        .extend( ['xsec=0.000465',        'kfact=1.000',          'ref=Y'] ) # 0.007052*0.621*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M2500']        .extend( ['xsec=0.000156',        'kfact=1.000',          'ref=Y'] ) # 0.002360*0.621*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M3000']        .extend( ['xsec=0.0000544',       'kfact=1.000',          'ref=Y'] ) # 0.0008253*0.621*0.1086*0.1086*9

samples['VBFHToWWTo2L2Nu_JHUGen698_M300']               .extend( ['xsec=0.0960',        'kfact=1.000',          'ref=KF'] ) # 1.322*0.692*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M350']               .extend( ['xsec=0.0734',        'kfact=1.000',          'ref=KF'] ) # 1.035*0.676*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M400']               .extend( ['xsec=0.0514',        'kfact=1.000',          'ref=KF'] ) # 0.841*0.582*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M450']               .extend( ['xsec=0.0397',        'kfact=1.000',          'ref=KF'] ) # 0.686*0.551*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M500']               .extend( ['xsec=0.0319',        'kfact=1.000',          'ref=KF'] ) # 0.557*0.546*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M550']               .extend( ['xsec=0.0264',        'kfact=1.000',          'ref=KF'] ) # 0.457*0.550*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M600']               .extend( ['xsec=0.0221',        'kfact=1.000',          'ref=KF'] ) # 0.378*0.558*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M650']               .extend( ['xsec=0.0189',        'kfact=1.000',          'ref=KF'] ) # 0.317*0.568*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M700']               .extend( ['xsec=0.0163',        'kfact=1.000',          'ref=KF'] ) # 0.269*0.577*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M750']               .extend( ['xsec=0.0142',        'kfact=1.000',          'ref=KF'] ) # 0.235*0.577*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M800']               .extend( ['xsec=0.0125',        'kfact=1.000',          'ref=KF'] ) # 0.200*0.594*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M900']               .extend( ['xsec=0.0099',        'kfact=1.000',          'ref=KF'] ) # 0.1547*0.609*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M1000']              .extend( ['xsec=0.0080',        'kfact=1.000',          'ref=KF'] ) # 0.1228*0.621*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M1500']              .extend( ['xsec=0.0029',        'kfact=1.000',          'ref=KF'] ) # 0.04471*0.621*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M2000']              .extend( ['xsec=0.0023',        'kfact=1.000',          'ref=KF'] ) # 0.03488*0.621*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M2500']              .extend( ['xsec=0.0015',        'kfact=1.000',          'ref=KF'] ) # 0.02165*0.621*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_JHUGen698_M3000']              .extend( ['xsec=0.00092',       'kfact=1.000',          'ref=KF'] ) # 0.01413*0.621*0.108*0.108*9

samples['VBFHToWWTo2L2NuPowheg_M125'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuPowheg_M125_PrivateNano'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuPowheg_M125_private'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuPowheg_M125_CP5Up'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuPowheg_M125_CP5Down'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuAMCNLO_M125'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuHerwigPS_M125']	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_M125_herwigpp'] .extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value
samples['VBFHToWWTo2L2Nu_M125_CUETUp']	 .extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value
samples['VBFHToWWTo2L2Nu_M125_CUETDown'] .extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value

samples['VBFHToWWToLNuQQ_M115']		.extend( ['xsec=0.0803',	'kfact=1.000',		'ref=Y'] ) # 4.255*0.0859*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M120']		.extend( ['xsec=0.1265',	'kfact=1.000',		'ref=Y'] ) # 4.086*0.141*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M124']		.extend( ['xsec=0.1729',	'kfact=1.000',		'ref=Y'] ) # 3.956*0.199*0.1086*3*0.6741 ### Interpolated Xsec
samples['VBFHToWWToLNuQQ_M125']		.extend( ['xsec=0.1853',	'kfact=1.000',		'ref=Y'] ) # 3.925*0.215*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M126']		.extend( ['xsec=0.1976',	'kfact=1.000',		'ref=Y'] ) # 3.894*0.231*0.1086*3*0.6741 ### Interpolated Xsec
samples['VBFHToWWToLNuQQ_M130']		.extend( ['xsec=0.2511',	'kfact=1.000',		'ref=Y'] ) # 3.773*0.303*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M135']		.extend( ['xsec=0.3188',	'kfact=1.000',		'ref=Y'] ) # 3.629*0.400*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M140']		.extend( ['xsec=0.3842',	'kfact=1.000',		'ref=Y'] ) # 3.492*0.501*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M145']		.extend( ['xsec=0.4430',	'kfact=1.000',		'ref=Y'] ) # 3.362*0.600*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M150']		.extend( ['xsec=0.4951',	'kfact=1.000',		'ref=Y'] ) # 3.239*0.696*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M155']		.extend( ['xsec=0.5451',	'kfact=1.000',		'ref=Y'] ) # 3.122*0.795*0.1086*3*0.6741 ### Interpolated Xsec
samples['VBFHToWWToLNuQQ_M160']		.extend( ['xsec=0.6002',	'kfact=1.000',		'ref=Y'] ) # 3.010*0.908*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M165']		.extend( ['xsec=0.6123',	'kfact=1.000',		'ref=Y'] ) # 2.904*0.960*0.1086*3*0.6741 ### Interpolated Xsec
samples['VBFHToWWToLNuQQ_M170']		.extend( ['xsec=0.5932',	'kfact=1.000',		'ref=Y'] ) # 2.802*0.964*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M175']		.extend( ['xsec=0.5691',	'kfact=1.000',		'ref=Y'] ) # 2.705*0.958*0.1086*3*0.6741 ### Interpolated Xsec
samples['VBFHToWWToLNuQQ_M180']		.extend( ['xsec=0.5346',	'kfact=1.000',		'ref=Y'] ) # 2.612*0.932*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M190']		.extend( ['xsec=0.4212',	'kfact=1.000',		'ref=Y'] ) # 2.440*0.786*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M200']		.extend( ['xsec=0.3714',	'kfact=1.000',		'ref=Y'] ) # 2.282*0.741*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M210']		.extend( ['xsec=0.3395',	'kfact=1.000',		'ref=Y'] ) # 2.138*0.723*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M230']		.extend( ['xsec=0.2929',	'kfact=1.000',		'ref=Y'] ) # 1.884*0.708*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M250']		.extend( ['xsec=0.2570',	'kfact=1.000',		'ref=Y'] ) # 1.669*0.701*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M270']		.extend( ['xsec=0.2273',	'kfact=1.000',		'ref=Y'] ) # 1.485*0.697*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M300']		.extend( ['xsec=0.1909',	'kfact=1.000',		'ref=Y'] ) # 1.256*0.692*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M350']		.extend( ['xsec=0.1435',	'kfact=1.000',		'ref=Y'] ) # 0.9666*0.676*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M400']		.extend( ['xsec=0.0969',	'kfact=1.000',		'ref=Y'] ) # 0.7580*0.582*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M450']		.extend( ['xsec=0.0731',	'kfact=1.000',		'ref=Y'] ) # 0.6038*0.551*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M500']		.extend( ['xsec=0.0584',	'kfact=1.000',		'ref=Y'] ) # 0.4872*0.546*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M550']		.extend( ['xsec=0.0480',	'kfact=1.000',		'ref=Y'] ) # 0.3975*0.550*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M600']		.extend( ['xsec=0.0401',	'kfact=1.000',		'ref=Y'] ) # 0.3274*0.558*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M650']		.extend( ['xsec=0.0339',	'kfact=1.000',		'ref=Y'] ) # 0.2719*0.568*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M700']		.extend( ['xsec=0.0288',	'kfact=1.000',		'ref=Y'] ) # 0.2275*0.577*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M750']		.extend( ['xsec=0.0261',	'kfact=1.000',		'ref=Y'] ) # 0.1915*0.621*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M750_NWA']	.extend( ['xsec=0.0252',	'kfact=1.000',		'ref=KF'] ) # 0.186*0.621*0.1086*3*0.6741 - shall we keep the same BR for NWA?
samples['VBFHToWWToLNuQQ_M800']		.extend( ['xsec=0.0212',	'kfact=1.000',		'ref=Y'] ) # 0.1622*0.594*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M900']		.extend( ['xsec=0.0158',	'kfact=1.000',		'ref=Y'] ) # 0.1180*0.609*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M1000']	.extend( ['xsec=0.0119',	'kfact=1.000',		'ref=Y'] ) # 0.08732*0.621*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M1500']        .extend( ['xsec=0.00312',        'kfact=1.000',          'ref=Y'] ) # 0.02288*0.621*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M2000']        .extend( ['xsec=0.000962',        'kfact=1.000',          'ref=Y'] ) # 0.007052*0.621*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M2500']        .extend( ['xsec=0.000322',        'kfact=1.000',          'ref=Y'] ) # 0.002360*0.621*0.1086*3*0.6741
samples['VBFHToWWToLNuQQ_M3000']        .extend( ['xsec=0.000113',        'kfact=1.000',          'ref=Y'] ) # 0.0008253*0.621*0.1086*3*0.6741

samples['VBFHToTauTau_M120']		         .extend( ['xsec=0.275264',	'kfact=1.000',		'ref=EF'] ) # 3.91*0.0704
samples['VBFHToTauTau_M125']		         .extend( ['xsec=0.237000',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.0632
samples['VBFHToTauTau_M130']		         .extend( ['xsec=0.196745',	'kfact=1.000',		'ref=EF'] ) # 3.61*0.0545
samples['VBFHToTauTau_M125_HerwigPS']		 .extend( ['xsec=0.237000',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.0632
samples['VBFHToTauTau_M125_PythiaFragment_Up']	 .extend( ['xsec=0.237000',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.0632
samples['VBFHToTauTau_M125_PythiaFragment_Down'] .extend( ['xsec=0.237000',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.0632

### VBF H MuMu

samples['VBFHToMuMu_M125_CP5']                   .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5_ext1']              .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5up']                 .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5down']               .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_EEC5_powheg']           .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_EEC5_amcatnlo']         .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5_powheg']            .extend( ['xsec=0.00082296',   'kfact=1.000',          'ref=FT'] ) # 3.782*2.176*10^{-4}

# ggZH
samples['ggZH_HToWW_M120']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['ggZH_HToWW_M125']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['ggZH_HToWW_M125_PrivateNano']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['ggZH_HToWW_M130']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['GluGluZH_HToWW_M120']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['GluGluZH_HToWW_M125']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['GluGluZH_HToWW_M130']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )

# qqZH, H->WW
samples['HZJ_HToWWTo2L2Nu_M120_noHLT']  .extend( ['xsec=0.012743247',	'kfact=1.000',	'ref=FT'] ) #=(9.939-1.299)*0.1*0.1405*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_M125_noHLT']  .extend( ['xsec=0.017076282',	'kfact=1.000',	'ref=FT'] ) #=(8.839-1.227)*0.1*0.2137*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_M125']  .extend( ['xsec=0.017076282',	'kfact=1.000',	'ref=FT'] ) #=(8.839-1.227)*0.1*0.2137*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_M125_PrivateNano']  .extend( ['xsec=0.017076282',	'kfact=1.000',	'ref=FT'] ) #=(8.839-1.227)*0.1*0.2137*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_ZTo2L_M125']  .extend( ['xsec=0.0017242605',	'kfact=1.000',	'ref=FT'] ) #=(8.839-1.227)*0.1*0.2137*0.108*0.108*9*0.033658*3
samples['HZJ_HToWWTo2L2Nu_M130_noHLT']  .extend( ['xsec=0.021358874',	'kfact=1.000',	'ref=FT'] ) #=(7.899-1.164)*0.1*0.3021*0.108*0.108*9


# ggZH, H->WW
samples['GluGluZH_HToWWTo2L2Nu_M120']  .extend( ['xsec=0.00191591',  'kfact=1.000', 'ref=FT'] ) #=1.299*0.1*0.1405*0.108*0.108*9
samples['GluGluZH_HToWWTo2L2Nu_M125']  .extend( ['xsec=0.00275257',  'kfact=1.000', 'ref=FT'] ) #=1.227*0.1*0.2137*0.108*0.108*9
samples['GluGluZH_HToWWTo2L2Nu_M130']  .extend( ['xsec=0.00369142',  'kfact=1.000', 'ref=FT'] ) #=1.164*0.1*0.3021*0.108*0.108*9

# ggZH, H->tautau
samples['GluGluZH_HToTauTau_ZTo2L_M125']  .extend( ['xsec=0.075',  'kfact=1.000', 'ref=N'] )


## ZH tautau
samples['HZJ_HToTauTau_M120']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['HZJ_HToTauTau_M125']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['HZJ_HToTauTau_M130']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )

## ZH mumu

samples['ZH_HToMuMu_M125']              .extend( ['xsec=0.00019233664', 'kfact=1.000',          'ref=FT'] ) # 0.8839*2.176*10^{-4}
samples['ZH_HToMuMu_M125_CP5up']        .extend( ['xsec=0.00019233664', 'kfact=1.000',          'ref=FT'] ) # 0.8839*2.176*10^{-4}
samples['ZH_HToMuMu_M125_CP5down']      .extend( ['xsec=0.00019233664', 'kfact=1.000',          'ref=FT'] ) # 0.8839*2.176*10^{-4}

## VVV
samples['WWW']				.extend( ['xsec=0.18331',	'kfact=1.000',		'ref=H'] )
samples['WWZ']				.extend( ['xsec=0.16510',	'kfact=1.000',		'ref=E'] )
samples['WZZ']				.extend( ['xsec=0.05565',	'kfact=1.000',		'ref=E'] )
samples['ZZZ']				.extend( ['xsec=0.01398',	'kfact=1.000',		'ref=E'] )
samples['WWG']                          .extend( ['xsec=0.2147',        'kfact=1.000',          'ref=N'] )

samples['ZZZTo4L2Nu']				.extend( ['xsec=0.0001907',	'kfact=1.000',		'ref=N'] )
samples['WZZTo4L2Nu']				.extend( ['xsec=0.00027',	'kfact=1.000',		'ref=N'] )
samples['WWZTo4L2Nu']				.extend( ['xsec=0.0006024',	'kfact=1.000',		'ref=N'] )
samples['WWW_DiLeptonFilter']			.extend( ['xsec=0.007666',	'kfact=1.000',		'ref=N'] )


## Vg
samples['Wg_AMCNLOFXFX']  .extend( ['xsec=586.000',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['Wg_MADGRAPHMLM'] .extend( ['xsec=405.271',  'kfact=1.000',  'ref=E'] )       # LO
samples['Wg500']          .extend( ['xsec=1.00000',  'kfact=1.000',  'ref=X'] )
samples['WgStarLNuMuMu']  .extend( ['xsec=2.793',    'kfact=1.000',  'ref=X'] )
samples['WgStarLNuEE']    .extend( ['xsec=3.526',    'kfact=1.000',  'ref=X'] )
samples['Zg']             .extend( ['xsec=131.300',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['ZGToLLG']        .extend( ['xsec=58.83',  'kfact=1.000',  'ref=Rafael'] )  # 55.5*1.06
samples['ZgStar']         .extend( ['xsec=1.00000',  'kfact=1.000',  'ref=X'] )


## QCD
samples['QCD_Pt-15to20_MuEnrichedPt5']          .extend( ['xsec=2799000.0',	'kfact=1.000',	'ref=W'] )  #totxs 1273190000 ref=EN
samples['QCD_Pt-20to30_MuEnrichedPt5']          .extend( ['xsec=2526000.0', 	'kfact=1.000',	'ref=W'] )  #totxs 558528000  ref=EN
samples['QCD_Pt-30to50_MuEnrichedPt5']          .extend( ['xsec=1362000.0',	'kfact=1.000',	'ref=W'] )      #totxs 139803000  ref=N
samples['QCD_Pt-50to80_MuEnrichedPt5']          .extend( ['xsec=376600.0', 	'kfact=1.000',	'ref=W'] )      #totxs 19222500   ref=EN
samples['QCD_Pt-80to120_MuEnrichedPt5']         .extend( ['xsec=88930.0', 	'kfact=1.000',	'ref=W'] )      #totxs 2758420    ref=EN
samples['QCD_Pt-120to170_MuEnrichedPt5']        .extend( ['xsec=21230.0',  	'kfact=1.000',	'ref=W'] )      #totxs 469797   ref=EN
samples['QCD_Pt-170to300_MuEnrichedPt5']        .extend( ['xsec=7055.0',  	'kfact=1.000',	'ref=W'] )      #totxs 117989    ref=EN
samples['QCD_Pt-300to470_MuEnrichedPt5']        .extend( ['xsec=797.4',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-470to600_MuEnrichedPt5']        .extend( ['xsec=56.30',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-600to800_MuEnrichedPt5']        .extend( ['xsec=25.10',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-800to1000_MuEnrichedPt5']        .extend( ['xsec=4.707',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-1000toInf_MuEnrichedPt5']        .extend( ['xsec=1.621',  	'kfact=1.000',	'ref=I'] )

samples['QCD_Pt-20toInf_MuEnrichedPt15']  	    .extend( ['xsec=269900.0', 	'kfact=1.000',	'ref=W'] )      #totxs 720648000    ref=EN


samples['QCD_Pt-15to20_EMEnriched']       	.extend( ['xsec=1327000.0',	'kfact=1.000',	'ref=W'] )       #totxs 1273000000 ref=N It is 1279000000 in ref E
samples['QCD_Pt-20to30_EMEnriched']       	.extend( ['xsec=4908000.0', 'kfact=1.000',	'ref=W'] )      #totxs 557600000  ref=EN
samples['QCD_Pt-30to50_EMEnriched']       	.extend( ['xsec=6396000.0', 	'kfact=1.000',	'ref=W'] )      #totxs 136000000  ref=EN
samples['QCD_Pt-50to80_EMEnriched']       	.extend( ['xsec=1989000.0',  	'kfact=1.000',	'ref=W'] )      #totxs 19800000   ref=EN
#samples['QCD_Pt-50to80_EMEnriched_ext1']       	.extend( ['xsec=',  	'kfact=1.000',	'ref=W'] )  #totxs 19800000   ref=EN
samples['QCD_Pt-80to120_EMEnriched']       	.extend( ['xsec=380500.0',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-120to170_EMEnriched']       	.extend( ['xsec=66630.0',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-170to300_EMEnriched']       	.extend( ['xsec=20860.0',  	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt-300toInf_EMEnriched']       	.extend( ['xsec=1350.0',  	'kfact=1.000',	'ref=I'] )


samples['QCD_Pt-30toInf_DoubleEMEnriched']	.extend( ['xsec=162060000', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt_15to20_bcToE']    		.extend( ['xsec=232900',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_20to30_bcToE']    		.extend( ['xsec=362400',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_30to80_bcToE']    		.extend( ['xsec=418200',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_80to170_bcToE']    		.extend( ['xsec=39430',		'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_170to250_bcToE']    		.extend( ['xsec=2607',		'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_250toInf_bcToE']    		.extend( ['xsec=720.1',		'kfact=1.000',	'ref=I'] )

samples['QCD_HT200to300']                       .extend( ['xsec=1517000',       'kfact=1.000',  'ref=I'] )
samples['QCD_HT300to500']                       .extend( ['xsec=322300' ,       'kfact=1.000',  'ref=I'] )
samples['QCD_HT500to700']                       .extend( ['xsec=29380'  ,       'kfact=1.000',  'ref=I'] )
samples['QCD_HT700to1000']                      .extend( ['xsec=6363'   ,       'kfact=1.000',  'ref=I'] )
samples['QCD_HT1000to1500']                     .extend( ['xsec=1048'   ,       'kfact=1.000',  'ref=I'] )
samples['QCD_HT1500to2000']                     .extend( ['xsec=102.3'  ,       'kfact=1.000',  'ref=I'] )
samples['QCD_HT2000toInf']                      .extend( ['xsec=20.23'  ,       'kfact=1.000',  'ref=I'] )

samples['QCD_Pt_15to30']                        .extend( ['xsec=1245000000'  ,       'kfact=1.000',  'ref=I'] )
samples['QCD_Pt_30to50']                        .extend( ['xsec=106900000'   ,       'kfact=1.000',  'ref=I'] )

# GJets
samples['GJetsDR04_HT40To100'] .extend( ['xsec=17420', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT100To200'] .extend( ['xsec=5382', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT200To400'] .extend( ['xsec=1177', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT400To600'] .extend( ['xsec=132.8', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT600ToInf'] .extend( ['xsec=44.25', 'kfact=1.000', 'ref=I'] )
samples['GJets_HT40To100']      .extend( ['xsec=18740', 'kfact=1.000', 'ref=I'] )
samples['GJets_HT40To100-ext1'] .extend( ['xsec=18740', 'kfact=1.000', 'ref=I'] )
samples['GJets_HT40To100_ext1'] .extend( ['xsec=18740', 'kfact=1.000', 'ref=I'] )

# VBS
samples['WpWpJJ_EWK_QCD']   			.extend( ['xsec=0.05454',	'kfact=1.000',	'ref=I'] )
samples['WpWpJJ_EWK']                           .extend( ['xsec=0.02526',       'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_QCD']                           .extend( ['xsec=0.02474',       'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_QCD_aQGC']                  .extend( ['xsec=0.1390',        'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_aQGC']                  	.extend( ['xsec=0.1174',        'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_powheg']			.extend( ['xsec=0.02093',	'kfact=1.000',	'ref=I'] )
samples['WmWmJJ_EWK_powheg']			.extend( ['xsec=0.007868',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_EWK_QCD_noTop']   		.extend( ['xsec=2.66300',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_EWK_noTop']   			.extend( ['xsec=0.34520',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_QCD_noTop']   			.extend( ['xsec=2.160',	'kfact=1.000',	'ref=I'] ) #it was 2.42300 before
samples['WpWmJJ_EWK_QCD_noTop_noHiggs']         .extend( ['xsec=2.241',       'kfact=1.000',  'ref=I'] ) #it was 2.61600 before
samples['WpWmJJ_EWK_QCD_noHiggs']               .extend( ['xsec=35.45',       'kfact=1.000',  'ref=I'] ) #it was 39.88 before
samples['WpWmJJ_EWK'] 				.extend( ['xsec=0.4286',	'kfact=1.000',	'ref=I'] ) #it was 0.50310 before
samples['TWJ']   				.extend( ['xsec=0.28000',	'kfact=1.000',	'ref=X'] )
samples['tZq_ll']   				.extend( ['xsec=0.07580',	'kfact=1.000',	'ref=E'] )

samples['WLLJJToLNu_M-60_EWK_QCD']   		.extend( ['xsec=0.5295',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-60_EWK']   		.extend( ['xsec=0.04634',	'kfact=1.000',	'ref=I'] )
samples['WLLJJToLNu_M-60_QCD']   		.extend( ['xsec=0.49480',	'kfact=1.000',	'ref=I'] )
samples['WLLJJToLNu_M-4to60_EWK_QCD']  		.extend( ['xsec=0.4086',	'kfact=1.000',	'ref=N'] )
samples['WZJJ_EWK_QCD']   			.extend( ['xsec=0.48910',	'kfact=1.000',	'ref=I'] )
samples['WZJJ_EWK']   				.extend( ['xsec=0.03900',	'kfact=1.000',	'ref=X'] )
samples['WZJJ_QCD']   				.extend( ['xsec=0.45850',	'kfact=1.000',	'ref=I'] )
samples['WW_DoubleScattering']   		.extend( ['xsec=1.62000',	'kfact=1.000',	'ref=I'] )
samples['WWTo2L2Nu_DoubleScattering']   	.extend( ['xsec=0.1693',	'kfact=1.000',	'ref=I'] )
samples['DY1JetsToLL']   			.extend( ['xsec=1014.00',	'kfact=1.000',	'ref=I'] )
samples['DY2JetsToLL']   			.extend( ['xsec=333.300',	'kfact=1.000',	'ref=I'] )
samples['DY3JetsToLL']   			.extend( ['xsec=101.6',		'kfact=1.000',	'ref=I'] )
samples['DY4JetsToLL']   			.extend( ['xsec=54.22',		'kfact=1.000',	'ref=I'] )
samples['WGJJ']   				.extend( ['xsec=4.958',	'kfact=1.000',	'ref=I'] )
samples['EWKZ2Jets']				.extend( ['xsec=3.99800',	'kfact=1.000',	'ref=I'] )
samples['EWKZ2Jets_ZToLL_M-50']	                .extend( ['xsec=4.321',	        'kfact=1.000',	'ref=Z'] )
samples['WLLJJ_WToLNu_EWK']         .extend( ['xsec=0.01628',   'kfact=1.000',  'ref=N'] )
samples['WLLJJToLNu_M-60_EWK_4F']  		.extend( ['xsec=0.0176340', 	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_0Jet']  		.extend( ['xsec=0.5770677',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_1Jet']  		.extend( ['xsec=0.3445573',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_2Jet']  		.extend( ['xsec=0.0768421',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_3Jet']  		.extend( ['xsec=0.1112010',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To60_EWK_4F']  		.extend( ['xsec=0.0054845', 	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_0Jet']  	.extend( ['xsec=2.3011202',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_1Jet']  	.extend( ['xsec=0.5291347',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_2Jet']  	.extend( ['xsec=0.0819247',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_3Jet']  	.extend( ['xsec=0.0508602',	'kfact=1.000',	'ref=N'] )

# ttDM
samples['ttDM0001scalar00010'] .extend( ['xsec=19.59'           , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar0010']  .extend( ['xsec=19.59'           , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00020'] .extend( ['xsec=10.48'           , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00050'] .extend( ['xsec=2.941'           , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00100'] .extend( ['xsec=0.6723'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00200'] .extend( ['xsec=0.09327'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00300'] .extend( ['xsec=0.0295'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar00500'] .extend( ['xsec=0.00518'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar01000'] .extend( ['xsec=0.0003687'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar10000'] .extend( ['xsec=0.000000003342'  , 'kfact=1.000', 'ref=R'] )
samples['ttDM0010scalar00010'] .extend( ['xsec=0.09487'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar00015'] .extend( ['xsec=0.1202'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar00050'] .extend( ['xsec=2.942'           , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar00100'] .extend( ['xsec=0.6732'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar10000'] .extend( ['xsec=0.0000000033'    , 'kfact=1.000', 'ref=R'] )
samples['ttDM0050scalar00010'] .extend( ['xsec=0.001906'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050scalar00050'] .extend( ['xsec=0.002329'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050scalar00095'] .extend( ['xsec=0.006558'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050scalar00200'] .extend( ['xsec=0.09224'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050scalar00300'] .extend( ['xsec=0.02901'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050scalar10000'] .extend( ['xsec=0.000000002945'  , 'kfact=1.000', 'ref=R'] )
samples['ttDM0150scalar00010'] .extend( ['xsec=0.00008634'      , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150scalar00200'] .extend( ['xsec=0.00013'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150scalar00295'] .extend( ['xsec=0.000394'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150scalar00500'] .extend( ['xsec=0.003754'        , 'kfact=1.000', 'ref=J'] )

samples['ttDM0150scalar10000'] .extend( ['xsec=0.000000002076'  , 'kfact=1.000', 'ref=R'] )
samples['ttDM0500scalar00010'] .extend( ['xsec=0.0000007356'    , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500scalar00500'] .extend( ['xsec=0.0000009894'    , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500scalar00995'] .extend( ['xsec=0.0000073'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500scalar10000'] .extend( ['xsec=0.0000000004421' , 'kfact=1.000', 'ref=R'] )
samples['ttDM1000scalar00010'] .extend( ['xsec=0.000000006607'  , 'kfact=1.000', 'ref=J'] )
samples['ttDM1000scalar01000'] .extend( ['xsec=0.000000009433'  , 'kfact=1.000', 'ref=J'] )
samples['ttDM1000scalar10000'] .extend( ['xsec=0.00000000003886', 'kfact=1.000', 'ref=R'] )

samples['ttDM0001pseudo00010'] .extend( ['xsec=0.4409'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00020'] .extend( ['xsec=0.3992'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00050'] .extend( ['xsec=0.3032'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00100'] .extend( ['xsec=0.1909'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00200'] .extend( ['xsec=0.0836'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00300'] .extend( ['xsec=0.03999'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo00500'] .extend( ['xsec=0.005408'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo01000'] .extend( ['xsec=0.0003973'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo10000'] .extend( ['xsec=0.000000003814'  , 'kfact=1.000', 'ref=R'] )
samples['ttDM0010pseudo00010'] .extend( ['xsec=0.01499'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010pseudo00015'] .extend( ['xsec=0.01863'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010pseudo00050'] .extend( ['xsec=0.3034'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010pseudo00100'] .extend( ['xsec=0.1901'          , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010pseudo10000'] .extend( ['xsec=0.000000003722'  , 'kfact=1.000', 'ref=R'] )
samples['ttDM0050pseudo00010'] .extend( ['xsec=0.002444'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo00050'] .extend( ['xsec=0.002979'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo00095'] .extend( ['xsec=0.01067'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo00200'] .extend( ['xsec=0.08382'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo00300'] .extend( ['xsec=0.03989'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo10000'] .extend( ['xsec=0.00000000365'   , 'kfact=1.000', 'ref=R'] )
samples['ttDM0150pseudo00010'] .extend( ['xsec=0.0002364'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150pseudo00200'] .extend( ['xsec=0.0004124'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150pseudo00295'] .extend( ['xsec=0.003365'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150pseudo00500'] .extend( ['xsec=0.004611'        , 'kfact=1.000', 'ref=J'] )

samples['ttDM0150pseudo10000'] .extend( ['xsec=0.00000000296'   , 'kfact=1.000', 'ref=R'] )
samples['ttDM0500pseudo00010'] .extend( ['xsec=0.000002279'     , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500pseudo00500'] .extend( ['xsec=0.000003275'     , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500pseudo00995'] .extend( ['xsec=0.00006171'      , 'kfact=1.000', 'ref=J'] )
samples['ttDM0500pseudo10000'] .extend( ['xsec=0.0000000008437' , 'kfact=1.000', 'ref=R'] )
samples['ttDM1000pseudo00010'] .extend( ['xsec=0.00000002595'   , 'kfact=1.000', 'ref=J'] )
samples['ttDM1000pseudo01000'] .extend( ['xsec=0.00000003933'   , 'kfact=1.000', 'ref=J'] )
samples['ttDM1000pseudo10000'] .extend( ['xsec=0.0000000001039' , 'kfact=1.000', 'ref=R'] )


## monoHiggs 2HDM (gZ = 0.8)
samples['monoH_2HDM_MZp-600_MA0-300']  .extend( ['xsec=0.0103693772',         'kfact=1.000',   	'ref=M'] ) # 0.46223*0.2137*0.104976
samples['monoH_2HDM_MZp-800_MA0-300']  .extend( ['xsec=0.0063890241',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-300'] .extend( ['xsec=0.0033136333',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-300'] .extend( ['xsec=0.001753482',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-300'] .extend( ['xsec=0.0009576133',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-300'] .extend( ['xsec=0.0004160269',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-300'] .extend( ['xsec=0.0001929449',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-300'] .extend( ['xsec=0.00006009227143344',  'kfact=1.000',   	'ref=M'] ) 
                                                          
samples['monoH_2HDM_MZp-600_MA0-400']  .extend( ['xsec=0.0014650562',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-800_MA0-400']  .extend( ['xsec=0.0020947385',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-400'] .extend( ['xsec=0.0013579144',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-400'] .extend( ['xsec=0.000790552',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-400'] .extend( ['xsec=0.000455532',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-400'] .extend( ['xsec=0.000206571',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-400'] .extend( ['xsec=0.00009848025623088',  'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-400'] .extend( ['xsec=0.00003123173938464',  'kfact=1.000',   	'ref=M'] ) 
                                                          
samples['monoH_2HDM_MZp-600_MA0-500']  .extend( ['xsec=0.0001073841',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-800_MA0-500']  .extend( ['xsec=0.0008438537',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-500'] .extend( ['xsec=0.0007929524',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-500'] .extend( ['xsec=0.0005318055',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-500'] .extend( ['xsec=0.0003302865',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-500'] .extend( ['xsec=0.0001594362',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-500'] .extend( ['xsec=0.00007851231252576',  'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-500'] .extend( ['xsec=0.00002567723667552',  'kfact=1.000',   	'ref=M'] ) 
                                                          
samples['monoH_2HDM_MZp-600_MA0-600']  .extend( ['xsec=0.00002675628183024',  'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-800_MA0-600']  .extend( ['xsec=0.0002321935',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-600'] .extend( ['xsec=0.0004383929',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-600'] .extend( ['xsec=0.000364632',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-600'] .extend( ['xsec=0.0002517922',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-600'] .extend( ['xsec=0.0001311634',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-600'] .extend( ['xsec=0.00006727992356592',  'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-600'] .extend( ['xsec=0.00002285287524144',  'kfact=1.000',  	'ref=M'] ) 
                                                          
samples['monoH_2HDM_MZp-600_MA0-700']  .extend( ['xsec=0.0000274999480855',   'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-800_MA0-700']  .extend( ['xsec=0.000040092472341216', 'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-700'] .extend( ['xsec=0.0001978206',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-700'] .extend( ['xsec=0.0002324995',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-700'] .extend( ['xsec=0.0001854814',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-700'] .extend( ['xsec=0.0001071373',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-700'] .extend( ['xsec=0.000057914',          'kfact=1.000',    'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-700'] .extend( ['xsec=0.000020575439397216', 'kfact=1.000',    'ref=M'] ) 
                                                          
samples['monoH_2HDM_MZp-600_MA0-800']  .extend( ['xsec=0.000011418361607088', 'kfact=1.000',    'ref=M'] ) 
samples['monoH_2HDM_MZp-800_MA0-800']  .extend( ['xsec=0.000013804823635344', 'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1000_MA0-800'] .extend( ['xsec=0.000063693276178464', 'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1200_MA0-800'] .extend( ['xsec=0.0001309055',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1400_MA0-800'] .extend( ['xsec=0.0001282718',         'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-1700_MA0-800'] .extend( ['xsec=0.000085341',          'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2000_MA0-800'] .extend( ['xsec=0.00004919862637872',  'kfact=1.000',   	'ref=M'] ) 
samples['monoH_2HDM_MZp-2500_MA0-800'] .extend( ['xsec=0.000018451223478288', 'kfact=1.000',    'ref=M'] ) 


#Z' Baryonic

samples['monoH_ZpBaryonic_MZp-995_MChi-500']   .extend( ['xsec=0.0002494945927400', 'kfact=1.000', 'ref=U'] ) # 0.01112158268660*0.2137*0.104976
samples['monoH_ZpBaryonic_MZp-95_MChi-50']     .extend( ['xsec=0.0041635147703269', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-50_MChi-50']     .extend( ['xsec=0.0001611360430282', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-50_MChi-1']      .extend( ['xsec=0.0730446320948177', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-50_MChi-10']     .extend( ['xsec=0.0726517463594313', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-500_MChi-500']   .extend( ['xsec=0.0000004614622474', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-500_MChi-1']     .extend( ['xsec=0.0245347241338635', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-500_MChi-150']   .extend( ['xsec=0.0152485600039850', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-300_MChi-50']    .extend( ['xsec=0.0436808051850896', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-300_MChi-1']     .extend( ['xsec=0.0508603697121661', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-295_MChi-150']   .extend( ['xsec=0.0030036722473386', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-20_MChi-1']      .extend( ['xsec=0.0610728259816203', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-200_MChi-50']    .extend( ['xsec=0.0469403927027369', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-200_MChi-1']     .extend( ['xsec=0.0572441400052805', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-200_MChi-150']   .extend( ['xsec=0.0000715482351197', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-2000_MChi-500']  .extend( ['xsec=0.0002842723685013', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-2000_MChi-1']    .extend( ['xsec=0.0003126050472404', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-1995_MChi-1000'] .extend( ['xsec=0.0000163693988476', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-15_MChi-10']     .extend( ['xsec=0.0009379375550532', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-50']     .extend( ['xsec=0.0000045959561559', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-500']    .extend( ['xsec=0.0000000001011114', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-1']      .extend( ['xsec=0.0582090348191248', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-150']    .extend( ['xsec=0.0000000706331960', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-10']     .extend( ['xsec=0.0002675975570372', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10_MChi-1000']   .extend( ['xsec=0.0000000000006220', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-100_MChi-1']     .extend( ['xsec=0.0713436198584672', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-100_MChi-10']    .extend( ['xsec=0.0711933915549046', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-1000_MChi-1']    .extend( ['xsec=0.0045263757795535', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-1000_MChi-150']  .extend( ['xsec=0.0043971796912420', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-1000_MChi-1000'] .extend( ['xsec=0.0000000123730297', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-50']  .extend( ['xsec=0.0000000002655861', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-500'] .extend( ['xsec=0.0000000002145566', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-1']   .extend( ['xsec=0.0000000002673191', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-150'] .extend( ['xsec=0.0000000002598862', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-10']  .extend( ['xsec=0.0000000002676616', 'kfact=1.000', 'ref=U'] ) 
samples['monoH_ZpBaryonic_MZp-10000_MChi-1000'].extend( ['xsec=0.0000000001480138', 'kfact=1.000', 'ref=U'] ) 



# Stop T2tt FullSim
samples['T2tt_mStop425_mLSP325']             .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop500_mLSP325']             .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop850_mLSP100']             .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
# Stop T2tt FastSim Scans
samples['T2tt_mStop100-125_mLSP1to50']       .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop150-175_mLSP1to100']      .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop200_mLSP1to125']          .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop225_mLSP25to150']         .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop250_mLSP1to175']          .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop275_mLSP75to200']         .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop183to291_mLSP1to100']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop300to375_mLSP1to300']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop400to475_mLSP1to400']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop500-525-550_mLSP1to425-325to450-1to475'] .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop600-950_mLSP1to450']      .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop-150to250']               .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop-250to350']               .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop-350to400']               .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_mStop-400to1200']              .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_dM10to80']                     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tt_dM10to80_genHT160_genMET80']   .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
# Stop T2tb FastSim Scans
samples['T2tb_mStop200to325_mLSP0to150']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] ) 
samples['T2tb_mStop200to625_mLSP50to475']    .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tb_mStop350to400_mLSP0to225']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tb_mStop425to600_mLSP0to425']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tb_mStop625to850_mLSP0to450']     .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2tb_mStop875to1125_mLSP0to475']    .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
# Stop T2bW FastSim Scans
samples['T2bW_X05_mStop125to275_mLSP0to150'] .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2bW_X05_mStop300to400_mLSP0to275'] .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2bW_X05_mStop425to600_mLSP0to375'] .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2bW_X05_mStop625to950_mLSP0to350'] .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )
samples['T2bW']                              .extend( ['xsec=1.000','kfact=1.000',   'ref=X'] )

#alternative spin parity Higgs
samples['H0PM_ToWWTo2L2Nu'] .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0PH_ToWWTo2L2Nu']  .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0L1_ToWWTo2L2Nu'] .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0M_ToWWTo2L2Nu'] .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0PHf05_ToWWTo2L2Nu']  .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0L1f05_ToWWTo2L2Nu'] .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['H0Mf05_ToWWTo2L2Nu'] .extend( ['xsec=0.9913',  'kfact=1.000',        'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value

samples['VBF_H0PH_ToWWTo2L2Nu']	.extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 
samples['VBF_H0L1_ToWWTo2L2Nu']	.extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 
samples['VBF_H0M_ToWWTo2L2Nu'] 	.extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 
samples['VBF_H0PHf05_ToWWTo2L2Nu'].extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 
samples['VBF_H0L1f05_ToWWTo2L2Nu'].extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 
samples['VBF_H0Mf05_ToWWTo2L2Nu'] .extend( ['xsec=0.0846',	'kfact=1.000',		'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value 


samples['2HDMa_MH3_300_MH4_150'] .extend( ['xsec=0.041793',       'kfact=1.00',           'ref=N'] ) #Cross-section :   1.863 x 0.2137 x 0.104976                                                               
samples['2HDMa_MH3_500_MH4_150'] .extend( ['xsec=0.012327',       'kfact=1.00',           'ref=N'] )
samples['2HDMa_MH3_700_MH4_150'] .extend( ['xsec=0.0044396',       'kfact=1.00',           'ref=N'] )
samples['2HDMa_MH3_900_MH4_150'] .extend( ['xsec=0.0017289',       'kfact=1.00',           'ref=N'] )
samples['2HDMa_MH3_1200_MH4_150'] .extend( ['xsec=0.00023577',       'kfact=1.00',           'ref=N'] )


################
# VBS Semileptonic
samples['WmTo2J_ZTo2L']     .extend(['xsec=0.0298',     'kfact=1.000',   'ref=W' ])
samples['WmToLNu_WmTo2J']   .extend( ['xsec=0.0326',    'kfact=1.000',   'ref=W' ])
samples['WmToLNu_ZTo2J']    .extend( ['xsec=0.1000',    'kfact=1.000',   'ref=W' ])
samples['WpTo2J_WmToLNu']   .extend( ['xsec=0.9107',    'kfact=1.000',   'ref=W' ])
samples['WpTo2J_ZTo2L']     .extend( ['xsec=0.0540',    'kfact=1.000',   'ref=W' ])
samples['WpToLNu_WpTo2J']   .extend( ['xsec=0.0879',    'kfact=1.000',   'ref=W' ])
samples['WpToLNu_WmTo2J']   .extend( ['xsec=0.9114',    'kfact=1.000',   'ref=W' ])
samples['WpToLNu_ZTo2J']    .extend( ['xsec=0.1825',    'kfact=1.000',   'ref=W' ])
samples['ZTo2L_ZTo2J']      .extend( ['xsec=0.0159',    'kfact=1.000',   'ref=W' ])


# VV QCD production semilptonic
samples['WmTo2J_ZTo2L_QCD']     .extend( ['xsec=0.3862',    'kfact=1.000',   'ref=W' ])
samples['WmToLNu_WmTo2J_QCD']   .extend( ['xsec=0.03774',   'kfact=1.000',   'ref=W' ])
samples['WmToLNu_ZTo2J_QCD']    .extend( ['xsec=1.302',     'kfact=1.000',   'ref=W' ])
samples['WpTo2J_WmToLNu_QCD']   .extend( ['xsec=5.561',     'kfact=1.000',   'ref=W' ])
samples['WpTo2J_ZTo2L_QCD']     .extend( ['xsec=0.6409',    'kfact=1.000',   'ref=W' ])
samples['WpToLNu_WpTo2J_QCD']   .extend( ['xsec=0.08642',   'kfact=1.000',   'ref=W' ])
samples['WpToLNu_WmTo2J_QCD']   .extend( ['xsec=5.544',     'kfact=1.000',   'ref=W' ])
samples['WpToLNu_ZTo2J_QCD']    .extend( ['xsec=2.162',     'kfact=1.000',   'ref=W' ])
samples['ZTo2L_ZTo2J_QCD']      .extend( ['xsec=0.3756',    'kfact=1.000',   'ref=W' ])

# Wjets EWK production semileptonic analysis
# XS from AN CMS-SMP-17-161
samples['WLNuJJ_EWK'].extend (['xsec=20.44', 'kfact=1.000', 'ref=SMP-17-161'])

# HH bblnu
samples['GluGluToHHTo2B2WToLNu2J'].extend(['xsec=1.97', 'kfact=1.000', 'ref=?'])

#VBS Semileptonic aQGC samples
samples['ZTo2L_ZTo2J_aQGC']        .extend( ['xsec=3.361',    'kfact=1.000',   'ref=W' ])
samples['WmTo2L_WmTo2J_aQGC']      .extend( ['xsec=0.5065',    'kfact=1.000',   'ref=W' ])
samples['WmTo2J_ZTo2L_aQGC']       .extend( ['xsec=0.2222',    'kfact=1.000',   'ref=W' ])
samples['WpTo2L_ZTo2J_aQGC']       .extend( ['xsec=1.896',    'kfact=1.000',   'ref=W' ])
samples['WpTo2L_WpTo2J_aQGC']      .extend( ['xsec=3.453',    'kfact=1.000',   'ref=W' ])
samples['WpTo2L_WmTo2J_aQGC']      .extend( ['xsec=17.99',    'kfact=1.000',   'ref=W' ])
samples['WpTo2J_ZTo2L_aQGC']       .extend( ['xsec=0.569',    'kfact=1.000',   'ref=W' ])
samples['WpTo2J_WmTo2L_aQGC']      .extend( ['xsec=17.91',    'kfact=1.000',   'ref=W' ])
samples['WmTo2L_ZTo2J_aQGC']       .extend( ['xsec=0.7416',    'kfact=1.000',   'ref=W' ])
