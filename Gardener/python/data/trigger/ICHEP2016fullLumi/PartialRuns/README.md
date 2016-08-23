



cp HLT_MuSingle.txt HLT_MuSingle_Run_274094_275000.txt
cp HLT_MuSingle.txt HLT_MuSingle_Run_275001_275783.txt
cp HLT_MuSingle.txt HLT_MuSingle_Run_275784_276500.txt
cp HLT_MuSingle.txt HLT_MuSingle_Run_276501_276811.txt


cp HLT_DoubleMuLegHigPt.txt HLT_DoubleMuLegHigPt_Run_274094_275000.txt
cp HLT_DoubleMuLegHigPt.txt HLT_DoubleMuLegHigPt_Run_275001_275783.txt
cp HLT_DoubleMuLegHigPt.txt HLT_DoubleMuLegHigPt_Run_275784_276500.txt
cp HLT_DoubleMuLegHigPt.txt HLT_DoubleMuLegHigPt_Run_276501_276811.txt


cp HLT_EleMuLegLowPt.txt HLT_EleMuLegLowPt_Run_274094_275000.txt
cp HLT_EleMuLegLowPt.txt HLT_EleMuLegLowPt_Run_275001_275783.txt
cp HLT_EleMuLegLowPt.txt HLT_EleMuLegLowPt_Run_275784_276500.txt
cp HLT_EleMuLegLowPt.txt HLT_EleMuLegLowPt_Run_276501_276811.txt


cp HLT_DoubleMuLegLowPt.txt HLT_DoubleMuLegLowPt_Run_274094_275000.txt
cp HLT_DoubleMuLegLowPt.txt HLT_DoubleMuLegLowPt_Run_275001_275783.txt
cp HLT_DoubleMuLegLowPt.txt HLT_DoubleMuLegLowPt_Run_275784_276500.txt
cp HLT_DoubleMuLegLowPt.txt HLT_DoubleMuLegLowPt_Run_276501_276811.txt


cp HLT_MuEleLegHigPt.txt HLT_MuEleLegHigPt_Run_274094_275000.txt
cp HLT_MuEleLegHigPt.txt HLT_MuEleLegHigPt_Run_275001_275783.txt
cp HLT_MuEleLegHigPt.txt HLT_MuEleLegHigPt_Run_275784_276500.txt
cp HLT_MuEleLegHigPt.txt HLT_MuEleLegHigPt_Run_276501_276811.txt








http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html

export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.0.3/bin:$PATH



brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 271036 --end 274093

+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 9     | 27   | 12429 | 12429 | 0.648             | 0.622            |
+-------+------+-------+-------+-------------------+------------------+


brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 274094 --end 275000

+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 17    | 47   | 22141 | 22136 | 3.046             | 2.916            |
+-------+------+-------+-------+-------------------+------------------+


brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 275001 --end 275783 


+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 11    | 40   | 20073 | 20073 | 2.844             | 2.736            |
+-------+------+-------+-------+-------------------+------------------+



brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 275784 --end 276500 


+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 11    | 36   | 22527 | 22527 | 3.568             | 3.426            |
+-------+------+-------+-------+-------------------+------------------+



brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 276501 --end 276811 


+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 7     | 26   | 21648 | 21648 | 3.318             | 3.191            |
+-------+------+-------+-------+-------------------+------------------+









