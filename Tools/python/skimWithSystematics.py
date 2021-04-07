#!/usr/bin/env python
import ROOT as R
import re
import os
import time
import argparse 
import subprocess
from LatinoAnalysis.NanoGardener.data.BranchMapping_cfg import branch_mapping


'''
This script implements a consistent skimming of events from nominal and suffix-based variation trees. 

The skimming cut can contain branches that are varied in the systematic trees: the brancMapping
mechanism is used to replace the branch and hava consistent selection. 

All the variation trees are joint to the nominal as Friends. 
Then the list of nominal and varied selection cut is applied to get entrylists. 
Finally an OR of the entry list is performed. 

(The entrylist calculation is not done using a single gigantic cut because of ROOT limitations).

Once the most inclusive set of entries to be kept has been calculated the trees are copied. 
Branches to keep and remove can be specified.

'''

def format_selection_variation(selection , variation):
    '''Function to replace the varied branches with regex'''
    if variation in  branch_mapping:
        suffix = branch_mapping[variation]['suffix'] 
        for br in branch_mapping[variation]['branches']:
            #print(r'(?<!\w)' +br+suffix+ r'(?=[\s\W])')
            selection = re.sub(r'(?<!\w)' +br+ r'(?=[\s\W])', br+suffix, selection)
            #print "Replaced branch: ", br, " --> ", selection
    return selection


def get_entrylist(selection, filename, variations_dict, basedir):
    '''
    Function that gets the most inclusive list of entries with a selection on 
    nominal and variation trees.  The selection string is modified to take into account 
    branch variations. 
    
    - filename:  e.g. WJetsToLNu_LO__part1.root
    - variation_dict:  a dictionary with ("variation_name" : folder). It needs to contain a "nominal" variation
    where branch mappings are not used
    - basedir:  folder containing nominal and variations folder
    '''
    root_files = []
    total_selection = None
    try:
        rfile = R.TFile.Open( os.path.join(basedir,variations_dict['nominal'],filename) ,"READ")
        total_tree = rfile.Get("Events")
        root_files.append(rfile)
    except:
        print "ERROR! Cannot read file: ", os.path.join(basedir,variations_dict['nominal'],filename) 
        exit(1)
   
    varied_selections = [] 

    # restrict alternative JES source
    if "2016" in basedir:
        JES_sources = ["Absolute",  "Absolute_2016", "BBEC1", "BBEC1_2016","EC2",  "EC2_2016",
                        "FlavorQCD","HF", "HF_2016",  "RelativeBal",  "RelativeSample_2016"]
    if "2017" in basedir:
        JES_sources = ["Absolute",  "Absolute_2017", "BBEC1", "BBEC1_2017","EC2",  "EC2_2017",
                        "FlavorQCD","HF", "HF_2017",  "RelativeBal",  "RelativeSample_2017"]
    if "2018" in basedir:
        JES_sources = ["Absolute",  "Absolute_2018", "BBEC1", "BBEC1_2018","EC2",  "EC2_2018",
                        "FlavorQCD","HF", "HF_2018",  "RelativeBal",  "RelativeSample_2018"]
    
    for variation_name, folder in variations_dict.items():
        print variation_name
        if variation_name in ['JESup','JESdo', 'fatjetJESup', 'fatjetJESdo']: 
            suffixed_selection = None
            # Apply mapping for all the JES sources
            for source in JES_sources:
                mapping_key = variation_name.replace('JES', 'JES'+source)
                tmp_suffixed_selection = format_selection_variation(selection, mapping_key)
                print 'Variation: ', mapping_key, " --> ", tmp_suffixed_selection
                if suffixed_selection == None:
                    suffixed_selection = "(" + tmp_suffixed_selection + ")"
                else:
                    suffixed_selection += " || (" + tmp_suffixed_selection + ")"
        else:     
            suffixed_selection = format_selection_variation(selection, variation_name)
            print 'Variation: ', variation_name, " --> ", suffixed_selection
        
        #build the total list of selections
        varied_selections.append(suffixed_selection)

        # do not load nominal tree again
        if variation_name == "nominal" : continue
        #Open friend tree checking for file presence
        try:
            friend_file = R.TFile.Open(os.path.join(basedir,folder,filename), "READ")
            root_files.append(friend_file)
            # Add the varied tree as a friend of the nominal one
            friend_tree = friend_file.Get("Events")
            total_tree.AddFriend(friend_tree)
        except:
            print "ERROR! Cannot read file: ", os.path.join(basedir,folder,filename)
            exit(1)
    
    if (total_tree.GetEntries() == 0):
        print "WARNING: empty tree, creating empty TEntryList!"
        total_entrylist = R.TEventList("total_list","total_list")
    else:
        for vselection in varied_selections:
            print "Applying selection --> ", vselection
            # Add the entries to the same total list to do an OR of the selections
            total_tree.Draw(">>+total_list", vselection)
    
    # Extract the entrylist from the TFile
    total_entrylist = R.gDirectory.Get("total_list")
    total_entrylist.SetDirectory(0)
    
    #cleanup
    for root_file in root_files:
        root_file.Close()
    
    return total_entrylist


def copy_trees(entrylist, filename, variations_dict, basedir, targetdir, branches_to_keep=["*"],branches_to_remove=[]):
    '''
    Function that copies the trees using an entrylist to restrict the events to be copied. 
    Branches to keep and remove can be specified optionally. 

    - basedir:  folder containing nominal and variations folder
    - targetdir:  folder in which the resulting trees will be produced (usually temporary folder)
    '''
    for variation_name, folder in variations_dict.items():
        print 'Variation: ', variation_name 
        try:
            iFile = R.TFile.Open(os.path.join(basedir,folder,filename), "READ")
            oldTree = iFile.Get("Events")
        except:
            print "ERROR! Cannot read file: ", os.path.join(basedir,folder,filename)
            exit(1)

        # Set branches
        for br in branches_to_keep:
            oldTree.SetBranchStatus(br, 1)
        for br in branches_to_remove:
            oldTree.SetBranchStatus(br, 0)
        # Set filter of entries
        oldTree.SetEventList(entrylist)
        # new file 
        try:
            oFile = R.TFile.Open(os.path.join(targetdir,folder,filename), "RECREATE")
            # Copy only the entries in the entrylist
            newTree = oldTree.CopyTree("")

            # Copy also other metadata in the file
            if iFile.GetListOfKeys().Contains("Runs"):             Runs_tree =  iFile.Get("Runs").CopyTree("")
            if iFile.GetListOfKeys().Contains("ParameterSets"):    ParameterSets_tree = iFile.Get("ParameterSets").CopyTree("")
            if iFile.GetListOfKeys().Contains("LuminosityBlocks"): LuminosityBlocks_tree = iFile.Get("LuminosityBlocks").CopyTree("")
            if iFile.GetListOfKeys().Contains("MetaData"):         MetaData_tree = iFile.Get("MetaData").CopyTree("")
            if iFile.GetListOfKeys().Contains("autoPU"):           autoPU_histo = iFile.Get("autoPU").Clone()

            oFile.Write()
            oFile.Close()
            iFile.Close()

        except:
            print "ERROR! Cannot create file: ", os.path.join(targetdir,folder,filename)
            exit(1)
    
class Skimmer:

    def __init__(self,filenames, basedir, targetdir, step, variations, selection,branches_to_keep=['*'], branched_to_remove=[]):
        self.filenames = filenames
        self.basedir = basedir
        self.step = step
        self.variations = variations 
        self.selection = selection 
        self.targetdir = targetdir
        self.branches_to_keep = branches_to_keep
        self.branches_to_remove = branched_to_remove

        if not os.path.exists(os.path.join(self.targetdir, self.step)):
            os.makedirs(os.path.join(self.targetdir, self.step))
        self.variations_dict =  { "nominal" : self.step }

        for variation in self.variations:
            for d in ["up","do"]:
                path = os.path.join(self.targetdir, self.step + "_" +variation +d )
                if not os.path.exists(path): os.makedirs(path)
                self.variations_dict[variation + d] = self.step + "_"+variation+d

        self.entrylists = {}

    def compute_entrylist(self):
        for filename in self.filenames:
            print "\n\n>>>>>>>>>>> Extracting entrylist on file: ", filename
            self.entrylists[filename] = get_entrylist(self.selection, filename, self.variations_dict, self.basedir)
            self.entrylists[filename].Print("all")

    def copy_trees(self):
        for filename, entrylist in self.entrylists.items():
            print "\n\n>>>>>>>>>>> Copying trees for file: ", filename
            copy_trees(entrylist, filename, self.variations_dict, 
                        self.basedir, self.targetdir, 
                        branches_to_keep=self.branches_to_keep, branches_to_remove=self.branches_to_remove)

    def save_entrylists(self, outputdir):
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        for filename, entrylist in self.entrylists.items():
            try:
                out = R.TFile.Open(os.path.join(outputdir, filename), "RECREATE")
                entrylist.Write()
                out.Close()
            except:
                print "ERROR! Cannot create entrylist file: ", os.path.join(outputdir, filename)
                exit(1)

    def hadd(self, outputfolder, outputfilename, hadd_script):
        for folder in self.variations_dict.values():
            #create destination folder
            if not os.path.exists(os.path.join(outputfolder, folder)):
                os.makedirs(os.path.join(outputfolder, folder))
            print "hadd ",folder
            files = [os.path.join(self.targetdir, folder,f) for f in os.listdir(os.path.join(self.targetdir, folder))]
            cmd = " ".join(["python", hadd_script, os.path.join(outputfolder, folder, outputfilename)]+files)
            with open("hadd_script.sh","a") as script:
                script.write(cmd+"\n")
