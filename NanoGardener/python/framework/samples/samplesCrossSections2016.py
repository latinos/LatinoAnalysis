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
#   W       https://cms-gen-dev.cern.ch/xsdb/
#       Z   http://cms.cern.ch/iCMS/analysisadmin/cadilines?line=SMP-18-006
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
#    A1 https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf 
#	X	Unknown! - Cross section not yet there


## W+jets
samples['WJetsToLNu']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu_ext2']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )
samples['WJetsToLNu-LO_ext2']                	.extend( ['xsec=61526.7',	'kfact=1.00',		'ref=E'] )

samples['WJetsToLNu_HT70_100']          .extend( ['xsec=1353.0',       'kfact=1.0',           'ref=W'] )   
samples['WJetsToLNu_HT100_200']        	.extend( ['xsec=1345.00',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT100_200_ext1']      .extend( ['xsec=1345.00',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT100_200_ext2']      .extend( ['xsec=1345.00',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT200_400']        	.extend( ['xsec=359.700',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT200_400_ext1']      .extend( ['xsec=359.700',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT200_400_ext2']      .extend( ['xsec=359.700',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT400_600']        	.extend( ['xsec=48.9100',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT400_600_ext1']      .extend( ['xsec=48.9100',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT600_inf']        	.extend( ['xsec=18.7700',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT600_800']        	.extend( ['xsec=12.0500',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT600_800_ext1']      .extend( ['xsec=12.0500',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT800_1200']       	.extend( ['xsec=5.50100',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT800_1200_ext1']  	.extend( ['xsec=5.50100',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT1200_2500']      	.extend( ['xsec=1.32900',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT1200_2500_ext1']    .extend( ['xsec=1.32900',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT2500_inf']       	.extend( ['xsec=0.03216',	'kfact=1.21',		'ref=E'] )
samples['WJetsToLNu_HT2500_inf_ext1']     .extend( ['xsec=0.03216',	'kfact=1.21',		'ref=E'] )

samples['WJetsToLNu_Pt100to250']                	.extend( ['xsec=689.749632',	'kfact=1.0',		'ref=A1'] )  
samples['WJetsToLNu_Pt250to400']                	.extend( ['xsec=24.5069015',	'kfact=1.0',		'ref=A1'] )
samples['WJetsToLNu_Pt400to600']                	.extend( ['xsec=3.110130566',	'kfact=1.0',		'ref=A1'] )
samples['WJetsToLNu_Pt600toInf']                   .extend( ['xsec=0.4683178368',	'kfact=1.0',		'ref=A1'] )

samples['WJetsToLNu_Wpt100to200']  .extend( [ 'xsec=457.8', 'kfact=1.0', 'ref=XSDB' ])
samples['WJetsToLNu_Wpt200toInf']  .extend( [ 'xsec=50.48', 'kfact=1.0', 'ref=XSDB' ])

samples['WJetsToLNu_0J']  .extend( [ 'xsec=50131.98', 'kfact=1.0', 'ref=A1' ])
samples['WJetsToLNu_1J']  .extend( [ 'xsec=8426.09', 'kfact=1.0', 'ref=A1' ])
samples['WJetsToLNu_2J']  .extend( [ 'xsec=3172.96', 'kfact=1.0', 'ref=A1' ])

samples['WJetsToLNu-LO_1J'].extend( [ 'xsec=9578.0', 'kfact=1.0', 'ref=W'])
samples['WJetsToLNu-LO_2J'].extend( [ 'xsec=3154.0', 'kfact=1.0', 'ref=W'])
samples['WJetsToLNu-LO_3J'].extend( [ 'xsec=958.0',  'kfact=1.0', 'ref=W'])
samples['WJetsToLNu-LO_4J'].extend( [ 'xsec=495.7',  'kfact=1.0', 'ref=W'])

samples['DYJetsToLL_0J']  .extend( [ 'xsec=4620.52', 'kfact=1.0', 'ref=A1' ])
samples['DYJetsToLL_1J']  .extend( [ 'xsec=859.59', 'kfact=1.0', 'ref=A1' ])
samples['DYJetsToLL_2J']  .extend( [ 'xsec=338.26', 'kfact=1.0', 'ref=A1' ])


## DY
samples['DYJetsToLL_M-10to50']        	   .extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50_ext1']        	   .extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50ext3']         .extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50_ext2']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )

samples['DYJetsToLL_M-50-UEup']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-UEdo']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-PSup']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-PSdo']                 .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )

samples['DYJetsToLL_M-5to50-LO']      	   .extend( ['xsec=71310.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50-LO']          .extend( ['xsec=18610.0',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO']      	   .extend( ['xsec=6025.20',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50-LO_ext1']         .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO_ext2']         .extend( ['xsec=6025.20',    'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50_HT-70to100']      .extend( ['xsec=169.9',	'kfact=1.230889',	'ref=I'] ) 
samples['DYJetsToLL_M-50_HT-100to200']     .extend( ['xsec=147.40',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-100to200_ext1'].extend( ['xsec=147.40',	'kfact=1.230889',	'ref=E'] )  
samples['DYJetsToLL_M-50_HT-200to400']     .extend( ['xsec=40.99',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-200to400_ext1'].extend( ['xsec=40.99',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-400to600']     .extend( ['xsec=5.678',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-400to600_ext1'].extend( ['xsec=5.678',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-600toInf']     .extend( ['xsec=2.198',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-600toInf_ext1'].extend( ['xsec=2.198',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-600to800']     .extend( ['xsec=1.367',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-800to1200']    .extend( ['xsec=0.6304',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-1200to2500']   .extend( ['xsec=0.1514',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-2500toInf']    .extend( ['xsec=0.003565',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToLL_M-50_HT-2500toinf']    .extend( ['xsec=0.003565',	'kfact=1.230889',	'ref=E'] ) 
samples['DYJetsToEE_Pow']                  .extend( ['xsec=1997',       'kfact=1.000',          'ref=E'] )
samples['DYJetsToTT_MuEle_M-50']           .extend( ['xsec=248.849',    'kfact=1.000',          'ref=E'] )  # (6025.20/3)*(0.352)^2
samples['DYJetsToTT_MuEle_M-50_ext1']           .extend( ['xsec=248.849',    'kfact=1.000',          'ref=E'] )  # (6025.20/3)*(0.352)^2

## DY (Low mass)
samples['DYJetsToLL_M-5to50_HT-70to100']   .extend( ['xsec=303.8',  'kfact=1.000',          'ref=I'] )
samples['DYJetsToLL_M-5to50_HT-100to200']  .extend( ['xsec=224.2',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-100to200_ext1']  .extend( ['xsec=224.2',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-200to400']  .extend( ['xsec=37.2',   'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-200to400_ext1']  .extend( ['xsec=37.2',   'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-400to600']  .extend( ['xsec=3.581',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-400to600_ext1']  .extend( ['xsec=3.581',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-600toInf']  .extend( ['xsec=1.124',  'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-5to50_HT-600toinf']  .extend( ['xsec=1.124',  'kfact=1.000',          'ref=E'] )

## DY (Higgs mass)
samples['DYJetsToLL_M-105To160']    .extend( ['xsec=42.73',  'kfact=1.000',          'ref=M'] ) # 42.73

samples['EWK_LLJJ_MLL-50_MJJ-120']  .extend( ['xsec=1.664',  'kfact=1.000',          'ref=M'] ) # 1.664

## VV 
samples['WW-LO']                        .extend( ['xsec=114.726',       'kfact=1.000',          'ref=E'] )  # 118.7 from E - 3.974 still from E
samples['WW-LOext1']                        .extend( ['xsec=114.726',       'kfact=1.000',          'ref=E'] )  # 118.7 from E - 3.974 still from E
samples['WWTo2L2Nu']	             	.extend( ['xsec=12.178',	'kfact=1.000',		'ref=I'] )		
samples['WWJTo2L2Nu_NNLOPS']	             	.extend( ['xsec=1.3273',	'kfact=1.000',		'ref=E'] )		
samples['WWTo2L2Nu_aTGC_0-400']       	.extend( ['xsec=13.84637',	'kfact=1.000',		'ref=X'] )  # X = Guillelmo :)		
samples['WWTo2L2Nu_aTGC_400-600']      	.extend( ['xsec=1.31589',	'kfact=1.000',		'ref=X'] )		
samples['WWTo2L2Nu_aTGC_600-800']      	.extend( ['xsec=0.339499',	'kfact=1.000',		'ref=X'] )		
samples['WWTo2L2Nu_aTGC_800-Inf']      	.extend( ['xsec=0.241369',	'kfact=1.000',		'ref=X'] )		
samples['WWToLNuQQ']	             	.extend( ['xsec=49.997',	'kfact=1.000',		'ref=E'] )	
samples['WWToLNuQQext']	             	.extend( ['xsec=49.997',	'kfact=1.000',		'ref=E'] )
samples['WWToLNuQQ_AMCNLOFXFX']         .extend( ['xsec=49.997',        'kfact=1.000',          'ref=E'] )
samples['WWTo4Q'] 	             	.extend( ['xsec=51.723',	'kfact=1.000',		'ref=E'] )
samples['WWTo2L2NuHerwigPS']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )	
samples['WWTo2L2Nu_CUETUp']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )
samples['WWTo2L2Nu_CUETDown']	        .extend( ['xsec=12.178',	'kfact=1.000',		'ref=E'] )
samples['WZ']			        .extend( ['xsec=47.130',	'kfact=1.000',		'ref=E'] )
samples['WZ_ext']			.extend( ['xsec=47.130',	'kfact=1.000',		'ref=E'] )
samples['WZ_ext1']			.extend( ['xsec=47.130',	'kfact=1.000',		'ref=E'] )
samples['WZ_AMCNLO']                    .extend( ['xsec=5.26'  ,        'kfact=1.000',          'ref=E'] )
samples['WZTo3LNu']		        .extend( ['xsec=4.42965',	'kfact=1.000',		'ref=E'] )
samples['WZTo3LNu_ext1']		        .extend( ['xsec=4.42965',	'kfact=1.000',		'ref=E'] )
samples['WZTo3LNu_ext']                 .extend( ['xsec=4.42965',       'kfact=1.000',          'ref=E'] )
samples['WZTo3LNu_AMCNLO']                 .extend( ['xsec=4.42965',       'kfact=1.000',          'ref=E'] )
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
samples['ZZTo2L2Q_AMCNLOFXFX']          .extend( ['xsec=3.22',          'kfact=1.000',          'ref=E'] )
samples['ZZTo4L']                       .extend( ['xsec=1.212000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L_AMCNLOFXFX']            .extend( ['xsec=1.212000',      'kfact=1.000',          'ref=E'] )
samples['ZZTo2L2Nu']                    .extend( ['xsec=0.564000',	'kfact=1.000',		'ref=E'] )
samples['ZZTo2L2Nu_ext1']               .extend( ['xsec=0.564000',      'kfact=1.000',          'ref=E'] )
samples['ggZZ4e']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4e_DS']                    .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4m']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ4t']                       .extend( ['xsec=0.001586',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2m']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2t']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2t']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2n']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2m2n']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ggZZ2e2t']                     .extend( ['xsec=0.003194',	'kfact=1.000',		'ref=E'] )
samples['ZZJJTo4L_EWK']                 .extend( ['xsec=0.0004453',	'kfact=1.000',		'ref=E'] )
samples['ZZTo2L2Nu_EWK']		            .extend( ['xsec=0.0003014',	'kfact=1.000',		'ref=I'] ) #Run SMP-RunIISummer15wmLHEGS-00086

## Single top
samples['ST_t-channel_antitop']         .extend( ['xsec=26.38',		'kfact=1.000',		'ref=E'] )
samples['ST_t-channel_top']             .extend( ['xsec=44.33',		'kfact=1.000',		'ref=E'] )
samples['ST_t-channel_top_PSweights']             .extend( ['xsec=44.33',		'kfact=1.000',		'ref=E'] )
samples['ST_t-channel']                 .extend( ['xsec=70.69',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_antitop']                .extend( ['xsec=35.60',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_top']                    .extend( ['xsec=35.60',		'kfact=1.000',		'ref=E'] )
samples['ST_s-channel']                 .extend( ['xsec=3.360',		'kfact=1.000',		'ref=E'] )
samples['ST_tW_antitop_noHad']          .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_antitop_noHad_ext1']          .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_top_noHad']              .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )
samples['ST_tW_top_noHad_ext1']              .extend( ['xsec=1.000',         'kfact=1.000',          'ref=X'] )

samples['tZq_ll_4f']                    .extend( ['xsec=0.0758',        'kfact=1.000',          'ref=E'] )

## Top
samples['TT']                           .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTJets']                       .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTJets_more']                  .extend( ['xsec=831.76',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu'] 	             	.extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu_ext1']               .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTJetsDiLep-LO']               .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTJetsDiLep-LO-ext1']          .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTWJetsToLNu']                 .extend( ['xsec=0.2043',	'kfact=1.000',		'ref=E'] )	
samples['TTWJetsToLNu_ext1']            .extend( ['xsec=0.2043',	'kfact=1.000',		'ref=E'] )	
samples['TTWJetsToLNu_ext2']            .extend( ['xsec=0.2043',	'kfact=1.000',		'ref=E'] )	
samples['TTZToLLNuNu_M-10']             .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToLLNuNu_M-10_ext1']        .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToLLNuNu_M-10_ext2']        .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToLLNuNu_M-10_ext3']        .extend( ['xsec=0.2529',	'kfact=1.000',		'ref=E'] )
samples['TTZToQQ']                      .extend( ['xsec=0.5297',        'kfact=1.000',          'ref=E'] )
samples['TTZjets']                      .extend( ['xsec=0.7826',        'kfact=1.000',          'ref=X'] )
samples['TTWJetsToQQ']                  .extend( ['xsec=0.4062',        'kfact=1.000',          'ref=E'] )      
samples['TTTo2L2Nu_alphaS01108']        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )
samples['TTToSemiLeptonic']             .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TTToSemiLeptonic_alphaS01108'] .extend( ['xsec=364.35',	'kfact=1.000',		'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TTToSemiLepton']               .extend( ['xsec=364.35',	'kfact=1.000',	        'ref=E'] )  # 831.76 * 0.6760 * 0.1080 * 3 * 2
samples['TT_TuneCUETP8M2T4']            .extend( ['xsec=831.76',        'kfact=1.000',          'ref=E'] )  # only change of tuning 
samples['TTJets_DiLept']                .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )
samples['TTJets_DiLept_ext1']           .extend( ['xsec=87.310',        'kfact=1.000',          'ref=E'] )


## GluGluWW
samples['GluGluWWTo2L2Nu_MCFM']      	.extend( ['xsec=0.5905',	'kfact=1.000',		'ref=E'] ) # 1.4*3.974*0.1086*.1086*9 --> 1.4 is a k-factor, 3.974 comes from the comment on the qqWW samples in reference E
samples['GluGluWWTo2L2NuHiggs_MCFM'] 	.extend( ['xsec=0.9544',	'kfact=1.000',		'ref=X'] ) # 1.4*0.6817 --> 1.4 is the same k-factor, 0.6817 is 0.07574*9, first number comes from MCFM, 9 is the lepton combinations


## ggH,HWW
samples['GluGluHToWWTo2L2Nu_Mlarge']  	        .extend( ['xsec=0.6818',	'kfact=1.000',  'ref=X']  ) # 10GeV Higgs width 30.21(powheg)*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2Nu_alternative_M120']  .extend( ['xsec=0.9818',	'kfact=1.000',	'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M125']  .extend( ['xsec=0.9913',	'kfact=1.000',	'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M130']  .extend( ['xsec=0.9081',	'kfact=1.000',	'ref=X']  ) # 28.55(powheg)*0.303*0.108*0.108*9

samples['GluGluHToWWTo2L2Nu_M115']  	.extend( ['xsec=0.4842',	'kfact=1.000',		'ref=Y'] ) # 53.10*0.0859*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M120']  	.extend( ['xsec=0.7319',	'kfact=1.000',		'ref=Y'] ) # 48.90*0.141*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M124']      .extend( ['xsec=0.9698',	'kfact=1.000',		'ref=Y'] ) # 45.91*0.199*0.1086*0.1086*9 ### Interpolated Xsec
samples['GluGluHToWWTo2L2Nu_M125']      .extend( ['xsec=1.0315',	'kfact=1.000',		'ref=Y'] ) # 45.20*0.215*0.1086*0.1086*9
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
samples['GluGluHToWWTo2L2Nu_M750_NWA']  .extend( ['xsec=0.0283',	'kfact=1.000',		'ref=KF'] ) # 0.460*0.586*0.1086*0.1086*9 - shall we keep the same BR for NWA?
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
samples['GluGluHToWWTo2L2Nu_JHUGen714_M4000']     .extend( ['xsec=0.000001917',     'kfact=1.000',         'ref=X'] ) # Self derived
samples['GluGluHToWWTo2L2Nu_JHUGen714_M5000']     .extend( ['xsec=0.0000001250',     'kfact=1.000',         'ref=X'] ) # Self derived


samples['GluGluHToWWTo2L2NuAMCNLO_M125']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_private']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowhegNNLOPS_M125_private']   .extend( ['xsec=0.9913',	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
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
samples['GluGluHToWWToLNuQQ_M750_NWA']  .extend( ['xsec=0.0589',	'kfact=1.000',		'ref=KF'] ) # 0.460*0.586*0.1086*3*0.6741 - shall we keep the same BR for NWA?
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


samples['GluGluHToMuMu_M125_CP5']        .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4} 
samples['GluGluHToMuMu_M125_CP5up']      .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4} 
samples['GluGluHToMuMu_M125_CP5down']    .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4} 
samples['GluGluHToMuMu_M125_powheg']     .extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4} 
samples['GluGluHToMuMu_M125_powheg_ext1'].extend(['xsec=0.010571',      'kfact=1.000',           'ref=FT'] ) # 48.58*2.176*10^{-4} 


## W+H
samples['HWplusJ_HToWW_M120']          	.extend( ['xsec=0.1350',	'kfact=1.000',	       	'ref=EF'] ) # 0.956*0.141
samples['HWplusJ_HToWW_M125']          	.extend( ['xsec=0.1810',	'kfact=1.000',	       	'ref=EF'] ) # 0.842*0.215
samples['HWplusJ_HToWW_M130']          	.extend( ['xsec=0.2250',	'kfact=1.000',	       	'ref=EF'] ) # 0.743*0.303

samples['WPlusH_HToMuMu_M125']       	.extend( ['xsec=0.00018278400',	'kfact=1.000',	       	'ref=FT'] ) # 0.840*2.176*10^{-4}
samples['WPlusH_HToMuMu_M125_CP5']    	.extend( ['xsec=0.00018278400',	'kfact=1.000',	       	'ref=FT'] ) # 0.840*2.176*10^{-4}
samples['WPlusH_HToMuMu_M125_CP5up']   	.extend( ['xsec=0.00018278400',	'kfact=1.000',	       	'ref=FT'] ) # 0.840*2.176*10^{-4}
samples['WPlusH_HToMuMu_M125_CP5down'] 	.extend( ['xsec=0.00018278400',	'kfact=1.000',	       	'ref=FT'] ) # 0.840*2.176*10^{-4}

## W-H
samples['HWminusJ_HToWW_M120']       	.extend( ['xsec=0.0866',     	'kfact=1.000',		'ref=EF'] ) # 0.614*0.141
samples['HWminusJ_HToWW_M125']  	.extend( ['xsec=0.1160',     	'kfact=1.000',		'ref=EF'] ) # 0.539*0.215
samples['HWminusJ_HToWW_M130'] 		.extend( ['xsec=0.1430',     	'kfact=1.000',		'ref=EF'] ) # 0.472*0.303

samples['WMinusH_HToMuMu_M125']       	.extend( ['xsec=0.00011593728',	'kfact=1.000',	       	'ref=FT'] ) # 0.5328*2.176*10^{-4}
samples['WMinusH_HToMuMu_M125_CP5']    	.extend( ['xsec=0.00011593728',	'kfact=1.000',	       	'ref=FT'] ) # 0.5328*2.176*10^{-4}
samples['WMinusH_HToMuMu_M125_CP5up']   .extend( ['xsec=0.00011593728',	'kfact=1.000',	       	'ref=FT'] ) # 0.5328*2.176*10^{-4}
samples['WMinusH_HToMuMu_M125_CP5down'] .extend( ['xsec=0.00011593728',	'kfact=1.000',	       	'ref=FT'] ) # 0.5328*2.176*10^{-4}

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

samples['ttHToMuMu_M125_CP5']		.extend( ['xsec=0.00011034496',	'kfact=1.000',		'ref=FT'] ) # 0.5071*2.176*10^{-4}
samples['ttHToMuMu_M125_CP5up']		.extend( ['xsec=0.00011034496',	'kfact=1.000',		'ref=FT'] ) # 0.5071*2.176*10^{-4}
samples['ttHToMuMu_M125_CP5down']	.extend( ['xsec=0.00011034496',	'kfact=1.000',		'ref=FT'] ) # 0.5071*2.176*10^{-4}


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
samples['VBFHToWWTo2L2NuPowheg_M125_private'] 	 .extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
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

samples['VBFHToMuMu_M125_CP5']		         .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5up']	         .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5down']	         .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_EEC5_powheg']	         .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_EEC5_amcatnlo']	 .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}
samples['VBFHToMuMu_M125_CP5_powheg']	         .extend( ['xsec=0.00082296',	'kfact=1.000',		'ref=FT'] ) # 3.782*2.176*10^{-4}

# ggZH
samples['ggZH_HToWW_M120']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['ggZH_HToWW_M125']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['ggZH_HToWW_M130']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )


# qqZH, H->WW
samples['HZJ_HToWWTo2L2Nu_M120_noHLT']  .extend( ['xsec=0.012743247',	'kfact=1.000',	'ref=FT'] ) #=(9.939-1.299)*0.1*0.1405*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_M125_noHLT']  .extend( ['xsec=0.017076282',	'kfact=1.000',	'ref=FT'] ) #=(8.839-1.227)*0.1*0.2137*0.108*0.108*9
samples['HZJ_HToWWTo2L2Nu_M130_noHLT']  .extend( ['xsec=0.021358874',	'kfact=1.000',	'ref=FT'] ) #=(7.899-1.164)*0.1*0.3021*0.108*0.108*9


# ggZH, H->WW
samples['GluGluZH_HToWWTo2L2Nu_M120_noHLT']  .extend( ['xsec=0.00191591',  'kfact=1.000', 'ref=FT'] ) #=1.299*0.1*0.1405*0.108*0.108*9
samples['GluGluZH_HToWWTo2L2Nu_M125_noHLT']  .extend( ['xsec=0.00275257',  'kfact=1.000', 'ref=FT'] ) #=1.227*0.1*0.2137*0.108*0.108*9
samples['GluGluZH_HToWWTo2L2Nu_M130_noHLT']  .extend( ['xsec=0.00369142',  'kfact=1.000', 'ref=FT'] ) #=1.164*0.1*0.3021*0.108*0.108*9

# ggZH, H->tautau
samples['GluGluZH_HToTauTau_ZTo2L_M125']  .extend( ['xsec=0.075',  'kfact=1.000', 'ref=N'] ) 

## ZH tautau
samples['HZJ_HToTauTau_M120']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['HZJ_HToTauTau_M125']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )
samples['HZJ_HToTauTau_M130']		.extend( ['xsec=1.0000',	'kfact=1.000',		'ref=X'] )

## ZH mumu

samples['ZH_HToMuMu_M125']	        .extend( ['xsec=0.00019233664',	'kfact=1.000',		'ref=FT'] ) # 0.8839*2.176*10^{-4}
samples['ZH_HToMuMu_M125_CP5']	        .extend( ['xsec=0.00019233664',	'kfact=1.000',		'ref=FT'] ) # 0.8839*2.176*10^{-4}
samples['ZH_HToMuMu_M125_CP5up']        .extend( ['xsec=0.00019233664',	'kfact=1.000',		'ref=FT'] ) # 0.8839*2.176*10^{-4}
samples['ZH_HToMuMu_M125_CP5down']      .extend( ['xsec=0.00019233664',	'kfact=1.000',		'ref=FT'] ) # 0.8839*2.176*10^{-4}

## VVV
samples['WWW']				.extend( ['xsec=0.18331',	'kfact=1.000',		'ref=H'] )
samples['WWZ']				.extend( ['xsec=0.16510',	'kfact=1.000',		'ref=E'] )
samples['WZZ']				.extend( ['xsec=0.05565',	'kfact=1.000',		'ref=E'] )
samples['ZZZ']				.extend( ['xsec=0.01398',	'kfact=1.000',		'ref=E'] )
samples['WWG']                          .extend( ['xsec=0.2147',        'kfact=1.000',          'ref=N'] )


## Vg
samples['Wg_AMCNLOFXFX']  .extend( ['xsec=586.000',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['Wg_AMCNLOFXFX_ext2']  .extend( ['xsec=586.000',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['Wg_AMCNLOFXFX_ext3']  .extend( ['xsec=586.000',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['Wg_MADGRAPHMLM'] .extend( ['xsec=405.271',  'kfact=1.000',  'ref=E'] )       # LO
samples['Wg500']          .extend( ['xsec=1.00000',  'kfact=1.000',  'ref=X'] )
samples['WgStarLNuMuMu']  .extend( ['xsec=2.793',    'kfact=1.000',  'ref=X'] )
samples['WgStarLNuEE']    .extend( ['xsec=3.526',    'kfact=1.000',  'ref=X'] )
samples['Zg']             .extend( ['xsec=131.300',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['Zg_ext1']             .extend( ['xsec=131.300',  'kfact=1.000',  'ref=Rafael'] )  # NNLO
samples['ZgStar']         .extend( ['xsec=1.00000',  'kfact=1.000',  'ref=X'] )


## QCD
samples['QCD_Pt-15to20_MuEnrichedPt5']          .extend( ['xsec=3819570.0',	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-20to30_MuEnrichedPt5']          .extend( ['xsec=2960198.4', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-30to50_MuEnrichedPt5']          .extend( ['xsec=1652471.5',	'kfact=1.000',	'ref=N'] )  
samples['QCD_Pt-50to80_MuEnrichedPt5']          .extend( ['xsec=437504.1', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-80to120_MuEnrichedPt5']         .extend( ['xsec=106033.6648', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-120to170_MuEnrichedPt5']        .extend( ['xsec=25190.5151',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-170to300_MuEnrichedPt5']        .extend( ['xsec=8654.4932',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-300to470_MuEnrichedPt5']        .extend( ['xsec=797.3527',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-470to600_MuEnrichedPt5']        .extend( ['xsec=79.02554',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-600to800_MuEnrichedPt5']        .extend( ['xsec=25.09506',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-800to1000_MuEnrichedPt5']        .extend( ['xsec=4.707368',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-1000toInf_MuEnrichedPt5']        .extend( ['xsec=1.621317',  	'kfact=1.000',	'ref=EN'] )    
samples['QCD_Pt-20toInf_MuEnrichedPt15']  	.extend( ['xsec=302672.16', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-15to20_EMEnriched']       	.extend( ['xsec=2302200.0',	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-20to30_EMEnriched']       	.extend( ['xsec=5352960.0', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-30to50_EMEnriched']       	.extend( ['xsec=9928000.0', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-30to50_EMEnriched_ext1']       	.extend( ['xsec=9928000.0', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-50to80_EMEnriched']       	    .extend( ['xsec=2233000.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-50to80_EMEnriched_ext1']       	.extend( ['xsec=2233000.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-80to120_EMEnriched']       	.extend( ['xsec=350000.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-120to170_EMEnriched']       	.extend( ['xsec=62964.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-170to300_EMEnriched']       	.extend( ['xsec=18810.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-300toInf_EMEnriched']       	.extend( ['xsec=1350.0',  	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt-30toInf_DoubleEMEnriched']	.extend( ['xsec=259296.0', 	'kfact=1.000',	'ref=EN'] )
samples['QCD_Pt_15to20_bcToE']    		.extend( ['xsec=232900',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_20to30_bcToE']    		.extend( ['xsec=362400',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_30to80_bcToE']    		.extend( ['xsec=418200',	'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_80to170_bcToE']    		.extend( ['xsec=39430',		'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_170to250_bcToE']    		.extend( ['xsec=2607',		'kfact=1.000',	'ref=I'] )
samples['QCD_Pt_250toInf_bcToE']    		.extend( ['xsec=720.1',		'kfact=1.000',	'ref=I'] )

# GJets
samples['GJetsDR04_HT40To100'] .extend( ['xsec=17420', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT100To200'] .extend( ['xsec=5382', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT200To400'] .extend( ['xsec=1177', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT400To600'] .extend( ['xsec=132.8', 'kfact=1.000', 'ref=I'] )
samples['GJetsDR04_HT600ToInf'] .extend( ['xsec=44.25', 'kfact=1.000', 'ref=I'] )
samples['GJets_HT40To100']      .extend( ['xsec=18740', 'kfact=1.000', 'ref=I'] )
samples['GJets_HT40To100-ext1'] .extend( ['xsec=18740', 'kfact=1.000', 'ref=I'] )

# VBS
samples['WpWpJJ_EWK_QCD']   			.extend( ['xsec=0.05454',	'kfact=1.000',	'ref=I'] )
samples['WpWpJJ_EWK']                           .extend( ['xsec=0.02526',       'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_QCD']                           .extend( ['xsec=0.02474',       'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_QCD_aQGC']                  .extend( ['xsec=0.1390',        'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_aQGC']                  	.extend( ['xsec=0.1174',        'kfact=1.000',  'ref=I'] )
samples['WpWpJJ_EWK_POWHEG']			.extend( ['xsec=0.02093',	'kfact=1.000',	'ref=I'] )
samples['WmWmJJ_EWK_powheg']			.extend( ['xsec=0.007868',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_EWK_QCD_noTop']   		.extend( ['xsec=2.66300',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_EWK_noTop']   			.extend( ['xsec=0.34520',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_QCD_noTop']   			.extend( ['xsec=2.42300',	'kfact=1.000',	'ref=I'] )
samples['WpWmJJ_EWK_QCD_noTop_noHiggs']         .extend( ['xsec=2.61600',       'kfact=1.000',  'ref=I'] )
samples['WpWmJJ_EWK_QCD_noHiggs']               .extend( ['xsec=39.88',       'kfact=1.000',  'ref=I'] )
samples['WpWmJJ_EWK'] 				.extend( ['xsec=0.50310',	'kfact=1.000',	'ref=I'] )
samples['TWJ']   				.extend( ['xsec=0.28000',	'kfact=1.000',	'ref=X'] )
samples['tZq_ll']   				.extend( ['xsec=0.07580',	'kfact=1.000',	'ref=E'] )
samples['tZq_ll_4f_PSweights']   		.extend( ['xsec=0.07580',	'kfact=1.000',	'ref=E'] )

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
samples['WGJJ']   				.extend( ['xsec=5.66200',	'kfact=1.000',	'ref=I'] )
samples['EWKZ2Jets']				.extend( ['xsec=3.99800',	'kfact=1.000',	'ref=I'] )
samples['WLLJJ_WToLNu_EWK']  		.extend( ['xsec=0.01762', 	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_0Jet']  		.extend( ['xsec=0.5754',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_1Jet']  		.extend( ['xsec=0.3436',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_2Jet']  		.extend( ['xsec=0.07668',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-50_QCD_3Jet']  		.extend( ['xsec=0.1111',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_0Jet']  	.extend( ['xsec=2.304',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_1Jet']  	.extend( ['xsec=0.5289',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_2Jet']  	.extend( ['xsec=0.08209',	'kfact=1.000',	'ref=N'] )
samples['WLLJJToLNu_M-4To50_QCD_3Jet']  	.extend( ['xsec=0.05082',	'kfact=1.000',	'ref=N'] )

# ttDM
# ttDM
samples['DMScalar_ttbar01j_Mchi1_Mphi10_Private2019'] .extend( ['xsec=19.76', 'kfact=1.000', 'ref=W'] )
samples['DMScalar_ttbar01j_Mchi1_Mphi50_Private2019'] .extend( ['xsec=3.006', 'kfact=1.000', 'ref=W'] )
samples['DMScalar_ttbar01j_Mchi1_Mphi100_Private2019'] .extend( ['xsec=0.696', 'kfact=1.000', 'ref=W'] )
samples['DMScalar_ttbar01j_Mchi1_Mphi500_Private2019'] .extend( ['xsec=0.0059', 'kfact=1.000', 'ref=W'] )

samples['DMPseudo_ttbar01j_Mchi1_Mphi10_Private2019'] .extend( ['xsec=0.4463', 'kfact=1.000', 'ref=W'] )
samples['DMPseudo_ttbar01j_Mchi1_Mphi50_Private2019'] .extend( ['xsec=0.3072', 'kfact=1.000', 'ref=W'] )
samples['DMPseudo_ttbar01j_Mchi1_Mphi100_Private2019'] .extend( ['xsec=0.1941', 'kfact=1.000', 'ref=W'] )
samples['DMPseudo_ttbar01j_Mchi1_Mphi500_Private2019'] .extend( ['xsec=0.005943', 'kfact=1.000', 'ref=W'] )

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



# VBSlnujj semileptonic 

samples['WpToLNu_WmTo2J']   .extend( ['xsec=0.9114',    'kfact=1.000',   'ref=Z' ])
samples['WpTo2J_WmToLNu']   .extend( ['xsec=0.9107',    'kfact=1.000',   'ref=Z' ])
samples['WpToLNu_WpTo2J']   .extend( ['xsec=0.0879',    'kfact=1.000',   'ref=Z' ])
samples['WmToLNu_WmTo2J']   .extend( ['xsec=0.0326',    'kfact=1.000',   'ref=Z' ])
samples['WpToLNu_ZTo2J']    .extend( ['xsec=0.1825',    'kfact=1.000',   'ref=Z' ])
samples['WpTo2J_ZTo2L']     .extend( ['xsec=0.0540',    'kfact=1.000',   'ref=Z' ])
samples['WmToLNu_ZTo2J']    .extend( ['xsec=0.1000',    'kfact=1.000',   'ref=Z' ])
samples['WmTo2J_ZTo2L']     .extend(['xsec=0.0298',     'kfact=1.000',   'ref=Z' ])
samples['ZTo2L_ZTo2J']      .extend(['xsec=0.0159',     'kfact=1.000',   'ref=Z' ])


# HH_WWbb_bblnujj semileptonic 2016
# FIXME: insert reference
samples['HH_bblnjj']        .extend(['xsec=1.97', 'kfact=1.000', 'ref=??'])

# Dummies for Susy samples
samples['T2tt__mStop-150to250']     .extend(['xsec=1.',     'kfact=1.000',   'ref=X' ])
samples['T2tt__mStop-250to350']     .extend(['xsec=1.',     'kfact=1.000',   'ref=X' ])
samples['T2tt__mStop-350to400']     .extend(['xsec=1.',     'kfact=1.000',   'ref=X' ])
samples['T2tt__mStop-400to1200']    .extend(['xsec=1.',     'kfact=1.000',   'ref=X' ])
samples['T2tt__mStop-1200to2000']   .extend(['xsec=1.',     'kfact=1.000',   'ref=X' ])


#PrivateNanoSamples
samples['GluGluHToWWTo2L2Nu_M125_PrivateNano']      .extend( ['xsec=1.0315',    'kfact=1.000',          'ref=Y'] ) # 45.20*0.215*0.1086*0.1086*9
samples['GluGluHToWWTo2L2Nu_M125_herwigpp_PrivateNano']  .extend( ['xsec=0.9913',       'kfact=1.000',          'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['GluGluHToWWTo2L2NuAMCNLO_M125_PrivateNano']   .extend( ['xsec=0.9913', 'kfact=1.000',          'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano']   .extend( ['xsec=0.9913', 'kfact=1.000',          'ref=CF'] ) # 43.92*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_M125_PrivateNano']             .extend( ['xsec=0.0896',        'kfact=1.000',          'ref=Y'] ) # 3.925*0.215*0.1086*0.1086*9
samples['VBFHToWWTo2L2Nu_M125_herwigpp_PrivateNano'] .extend( ['xsec=0.0846',   'kfact=1.000',          'ref=EF'] ) # 3.75*0.215*0.108*0.108*9 YR value
samples['ggZH_HToWW_M125_PrivateNano']          .extend( ['xsec=1.0000',        'kfact=1.000',          'ref=X'] )
samples['HZJ_HToTauTau_M125_PrivateNano']               .extend( ['xsec=0.0550',        'kfact=1.000',          'ref=EF'] ) # 0.8696*0.0632
samples['HWminusJ_HToWW_M125_PrivateNano']      .extend( ['xsec=0.1160',        'kfact=1.000',          'ref=EF'] ) # 0.539*0.215
samples['HWplusJ_HToWW_M125_PrivateNano']               .extend( ['xsec=0.1810',        'kfact=1.000',          'ref=EF'] ) # 0.842*0.215
samples['HWminusJ_HToTauTau_M125_PrivateNano']  .extend( ['xsec=0.0341',        'kfact=1.000',          'ref=EF'] ) # 0.539*0.0632
samples['HWplusJ_HToTauTau_M125_PrivateNano']   .extend( ['xsec=0.0532',        'kfact=1.000',          'ref=EF'] ) # 0.842*0.0632
samples['HZJ_HToWW_M125_PrivateNano']           .extend( ['xsec=0.187',         'kfact=1.000',          'ref=EF'] ) # 0.8696*0.215
samples['bbHToWWTo2L2Nu_M125_ybyt_PrivateNano']     .extend( ['xsec=0.000743225',    'kfact=1.000',         'ref=N'] ) # 0.000743225 = -0.03293*0.215*0.108*0.108*9
