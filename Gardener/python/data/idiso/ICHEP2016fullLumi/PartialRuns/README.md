

cp muons.txt muons_Run_271036_275783.txt
cp muons.txt muons_Run_275784_276500.txt
cp muons.txt muons_Run_276501_276811.txt


cp muons_iso_loose.txt muons_iso_loose_Run_271036_275783.txt
cp muons_iso_loose.txt muons_iso_loose_Run_275784_276500.txt
cp muons_iso_loose.txt muons_iso_loose_Run_276501_276811.txt


cp muons_iso_tight.txt muons_iso_tight_Run_271036_275783.txt
cp muons_iso_tight.txt muons_iso_tight_Run_275784_276500.txt
cp muons_iso_tight.txt muons_iso_tight_Run_276501_276811.txt



http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html

export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.0.3/bin:$PATH


brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 271036 --end 275783   \
--hltpath "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*"




brilcalc lumi -b "STABLE BEAMS" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt  --begin 271036 --end 275783

+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/fb) | totrecorded(/fb) |
+-------+------+-------+-------+-------------------+------------------+
| 36    | 114  | 54643 | 54638 | 6.538             | 6.274            |
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
