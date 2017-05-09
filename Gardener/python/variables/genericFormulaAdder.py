#   _____                      _        ______                         _                     _     _           
#  / ____|                    (_)      |  ____|                       | |           /\      | |   | |          
# | |  __  ___ _ __   ___ _ __ _  ___  | |__ ___  _ __ _ __ ___  _   _| | __ _     /  \   __| | __| | ___ _ __ 
# | | |_ |/ _ \ '_ \ / _ \ '__| |/ __| |  __/ _ \| '__| '_ ` _ \| | | | |/ _` |   / /\ \ / _` |/ _` |/ _ \ '__|
# | |__| |  __/ | | |  __/ |  | | (__  | | | (_) | |  | | | | | | |_| | | (_| |  / ____ \ (_| | (_| |  __/ |   
#  \_____|\___|_| |_|\___|_|  |_|\___| |_|  \___/|_|  |_| |_| |_|\__,_|_|\__,_| /_/    \_\__,_|\__,_|\___|_|   

from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class genericFormulaAdder(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add branches corresponding to formulas of tree variables'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        parser.add_option_group(group)

        return group


    def checkOptions(self,opts):
        pass
       
       
    def process(self,**kwargs):

        print " starting ..."

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        cmssw_base = os.getenv('CMSSW_BASE')
        formulasFile = "data/formulasToAdd.py"
        formulasFile_path = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+formulasFile

        formulas = {}

        if os.path.exists(formulasFile_path) :
          handle = open(formulasFile_path,'r')
          exec(handle)
          handle.close()
        else:
         print "cannot find file", formulasFile_path

        #now convert the formulas to lambdas, so that we don't need to do eval on every event
        for key in formulas.keys():
          formulas[key] = eval('lambda event:'+formulas[key])

        #prepare a new branch with the formula key name for each formula to add  
        newbranches={}
        for key in formulas.keys():
          newbranches[key] = numpy.ones(1, dtype=numpy.float32)

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        self.clone(output,newbranches.keys())


        for key in formulas.keys():
          self.otree.Branch(key  , newbranches[key]  , key+'/F')
   
        
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        itree     = self.itree
        otree     = self.otree


      
        print '- start event loop'
        i = 0
        step=5000
        for event in itree:

            if i > 0 and i%step == 0.:
                print i,'events processed.'
            
            for key in formulas.keys():
              newbranches[key][0] = formulas[key](event)
              

            otree.Fill()

            i+=1

        self.disconnect()
        print '- Eventloop completed'

