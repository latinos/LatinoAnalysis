### Skim inclusive TTToJets sample to get TTTo2L2Nu on one
### TEST!!!

TTJetsFile="root://eoscms//eos/cms/store/group/phys_higgs/cmshww/kbutanov/RunII/15Jul/25ns/latino_TTJets.root"  	

gardener.py filter -f "(abs(std_vector_leptonGen_mpid[0])==24 && abs(std_vector_leptonGen_mpid[1])==24) || (abs(std_vector_leptonGen_mpid[0])==24 && abs(std_vector_leptonGen_mpid[2])==24) || (abs(std_vector_leptonGen_mpid[0])==24 && abs(std_vector_leptonGen_mpid[3])==24) || (abs(std_vector_leptonGen_mpid[1])==24 && abs(std_vector_leptonGen_mpid[2])==24) || (abs(std_vector_leptonGen_mpid[2])==24 && abs(std_vector_leptonGen_mpid[3])==24)" $TTJetsFile ./latino_TTTo2L2Nu.root
