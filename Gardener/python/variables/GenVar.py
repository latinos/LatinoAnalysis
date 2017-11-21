#
#
#
#      ___|                  \ \     /            _)         |      |             
#     |       _ \  __ \       \ \   /  _` |   __|  |   _` |  __ \   |   _ \   __| 
#     |   |   __/  |   |       \ \ /  (   |  |     |  (   |  |   |  |   __/ \__ \ 
#    \____| \___| _|  _|        \_/  \__,_| _|    _| \__,_| _.__/  _| \___| ____/ 
#                                                                                 
#
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class genVariablesFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add generator variables'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        #group.add_option('-m', '--mcsample' , dest='mcsample', help='Name of the mc sample to be considered. Possible options [powheg, mcatnlo, madgraph]',default='random')
        parser.add_option_group(group)

        return group


    def checkOptions(self,opts):
        pass
       
       

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
 
        #
        # create branches for otree, the ones that will be modified!
        # These variables NEED to be defined as functions in GenVar.C
        # e.g. mll, dphill, ...
        # if you add a new variable here, be sure it IS defined in GenVar.C
        #
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'gen_ptllmet',
           'gen_ptll',
           'gen_mll',
           'gen_llchannel',
           'gen_mlvlv',
           'lhe_mlvlv',
           'lhe_mWp',
           'lhe_mWm',
           ]
        
        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/GenVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/GenVar.C++g')
        #----------------------------------------------------------------------------------------------------

        GenVar = ROOT.GenVar()

        # get some information 
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0
        
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):
        #for i in xrange(100):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            GenVar = ROOT.GenVar()
            # if no gen information, don't fill the variable
            if hasattr(itree, 'std_vector_leptonGen_pt') :
  
              if hasattr(itree, 'std_vector_leptonGen_MotherPID') :
                GenVar.setLeptons(itree.std_vector_leptonGen_pt, itree.std_vector_leptonGen_eta, itree.std_vector_leptonGen_phi,
                                  itree.std_vector_leptonGen_pid,
                                  itree.std_vector_leptonGen_status,
                                  itree.std_vector_leptonGen_isPrompt,
                                  itree.std_vector_leptonGen_MotherPID,
                                  itree.std_vector_leptonGen_MotherStatus
                                  )
              else : 
                GenVar.setLeptons(itree.std_vector_leptonGen_pt, itree.std_vector_leptonGen_eta, itree.std_vector_leptonGen_phi, itree.std_vector_leptonGen_pid)
              
              GenVar.setJets   (itree.std_vector_partonGen_pt, itree.std_vector_partonGen_eta, itree.std_vector_partonGen_phi, itree.std_vector_partonGen_pid)
  
              # add GenMET information
              if hasattr(itree, 'metGenpt') and hasattr(itree, 'metGenphi'):
                GenVar.setMET(itree.metGenpt, itree.metGenphi)
  
              # if LHE information is available
              if hasattr(itree, 'std_vector_LHElepton_pt') :
                GenVar.setLHELeptons  (itree.std_vector_LHElepton_pt, itree.std_vector_LHElepton_eta, itree.std_vector_LHElepton_phi, itree.std_vector_LHElepton_id)
                GenVar.setLHENeutrinos(itree.std_vector_LHEneutrino_pt, itree.std_vector_LHEneutrino_eta, itree.std_vector_LHEneutrino_phi, itree.std_vector_LHEneutrino_id)
 
             # now fill the variables like "mll", "dphill", ...
              for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                bvariable[0] = getattr(GenVar, bname)()
  
            otree.Fill()
            savedentries+=1
            

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
        print '   Total: ', nentries 



