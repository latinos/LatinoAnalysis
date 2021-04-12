# Documentation:

## lfn2srm
Converts a logical file name to the phisical file name on a given site, including the part specifying the protocol.
Esample usage:

    lfn2srm --site T2_IT_Pisa /store/group/phys_higgs/cmshww/amassiro//HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5__MupTup//nanoLatino_WJetsToLNu_ext2__part48.root
    
will return:
 
      srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/group/phys_higgs/cmshww/amassiro//HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5__MupTup//nanoLatino_WJetsToLNu_ext2__part48.root

which you can then, e.g., copy from Pisa with

    gfal-copy srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/group/phys_higgs/cmshww/amassiro//HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5__MupTup//nanoLatino_WJetsToLNu_ext2__part48.root file.root
    
    
## copyProduction.py
Script to copy an entire production to a T2 site. Example usage:

    copyProduction.py Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5 T2_IT_Pisa -k nano
   
will create a transfer.in file with instucrions for copying everything that is under   /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5
to Pisa. 
The actual transver needt to be donw with:

    fts-transfer-submit -s https://fts3-pilot.cern.ch:8446 -f transfer.in
   
The command above will return a string, which can be used to check the status of the transfer.

    fts-transfer-status -s https://fts3-pilot.cern.ch:8446 [-l] <string from previous command>
  
A list of active transfers can be obtained with:

    fts-transfer-list -s https://fts3-pilot.cern.ch:8446
  
Most likely the copy of a large number of files will result in some failures. Please resubmit the copyProduction.py command once the first round of transfer is finisced with the -c option
which will compare the checksum of the source and destination files and place in the trasfer.in file only those files that failed the first time

    copyProduction.py Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5 T2_IT_Pisa -k nano -c   
    fts-transfer-submit -s https://fts3-pilot.cern.ch:8446 -f transfer.in
    
CAVEAT: I have noticed that sometimes when the chcksum differs it is needed to delete the file at the destination before trying to resubmit the trasfer.    

Note that with the -c option the code is much slower.

After the copy files can then be accessed via the LFN /store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5
