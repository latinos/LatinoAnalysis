import optparse
import numpy
import ROOT
import os.path

from LatinoAnalysis.Gardener.gardening import TreeCloner

#from HWWAnalysis.ShapeAnalysis.triggerEffCombiner import TriggerEff

#
#  __ __|     _)                                ____|   _|   _| _)       _)                           
#     |   __|  |   _` |   _` |   _ \   __|      __|    |    |    |   __|  |   _ \  __ \    __|  |   | 
#     |  |     |  (   |  (   |   __/  |         |      __|  __|  |  (     |   __/  |   |  (     |   | 
#    _| _|    _| \__, | \__, | \___| _|        _____| _|   _|   _| \___| _| \___| _|  _| \___| \__, | 
#                |___/  |___/                                                                  ____/  
#
#

class EffTrgFiller(TreeCloner):

    def __init__(self):
        pass

    def help(self):
        return '''Add trigger efficiency weight. The source files must be passed as an option'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)

        group.add_option('--triggerDoubleEleLeg1', dest='triggerDoubleEleLeg1', help='file with trigger efficiencies triggerDoubleEleLeg1', default=None)
        group.add_option('--triggerDoubleEleLeg2', dest='triggerDoubleEleLeg2', help='file with trigger efficiencies triggerDoubleEleLeg2', default=None)
        group.add_option('--triggerSingleEle',     dest='triggerSingleEle',     help='file with trigger efficiencies triggerSingleEle',     default=None)


        parser.add_option_group(group)
        return group 

    def checkOptions(self,opts):
       
        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.triggerDoubleEleLeg1 == None :
          opts.triggerDoubleEleLeg1 = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele17_12Leg1.txt'
        if opts.triggerDoubleEleLeg2 == None :
          opts.triggerDoubleEleLeg2 = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele17_12Leg2.txt'
        if opts.triggerSingleEle == None :
          opts.triggerSingleEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele23_WPLoose.txt'


        file_triggerDoubleEleLeg1 = open (opts.triggerDoubleEleLeg1)
        file_triggerDoubleEleLeg2 = open (opts.triggerDoubleEleLeg2)
        file_triggerSingleEle     = open (opts.triggerSingleEle)
        
        self.list_triggers = {}
        
        self.list_triggers['triggerDoubleEleLeg1']   =    [line.rstrip().split() for line in file_triggerDoubleEleLeg1]
        self.list_triggers['triggerDoubleEleLeg2']   =    [line.rstrip().split() for line in file_triggerDoubleEleLeg2]
        self.list_triggers['triggerSingleEle']       =    [line.rstrip().split() for line in file_triggerSingleEle]
        
        #     eta              pt          value    error
        # '-2.5', '-2.0', '10.0', '15.0', '0.000', '0.000'


    def _getEff (self, kindLep, pt, eta, whichTrigger):

        
        for point in self.list_triggers[whichTrigger] :
           
           if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
               
               eff       = float(point[4])
               error_eff = float(point[5])
               
               return eff, error_eff
        
        return 0. , 0.
           
         
         
    def _fixOverflowUnderflow (self, kindLep, pt, eta):

        # fix underflow and overflow

        if kindLep == 'ele' :          
          if pt < self.minpt_ele:
            pt = self.minpt_ele
          if pt > self.maxpt_ele:
            pt = self.maxpt_ele
          
          if eta < self.mineta_ele:
            eta = self.mineta_ele
          if eta > self.maxeta_ele:
            eta = self.maxeta_ele

        if kindLep == 'mu' :          
          if pt < self.minpt_mu:
            pt = self.minpt_mu
          if pt > self.maxpt_mu:
            pt = self.maxpt_mu
          
          if eta < self.mineta_mu:
            eta = self.mineta_mu
          if eta > self.maxeta_mu:
            eta = self.maxeta_mu





    def _getWeight (self, kindLep1, pt1, eta1, kindLep2, pt2, eta2):

        self._fixOverflowUnderflow (kindLep1, pt1, eta1)  
        self._fixOverflowUnderflow (kindLep2, pt2, eta2)  
          
        eff_dbl_1_leadingleg  , error_eff_dbl_1_leadingleg    = self._getEff (kindLep1, pt1, eta1, 'triggerDoubleEleLeg1')
        eff_dbl_2_leadingleg  , error_eff_dbl_2_leadingleg    = self._getEff (kindLep2, pt2, eta2, 'triggerDoubleEleLeg1')
        eff_dbl_1_trailingleg , error_eff_dbl_1_trailingleg   = self._getEff (kindLep1, pt1, eta1, 'triggerDoubleEleLeg2')
        eff_dbl_2_trailingleg , error_eff_dbl_2_trailingleg   = self._getEff (kindLep2, pt2, eta2, 'triggerDoubleEleLeg2')
        eff_sgl_1             , error_eff_sgl_1               = self._getEff (kindLep1, pt1, eta1, 'triggerSingleEle')
        eff_sgl_2             , error_eff_sgl_2               = self._getEff (kindLep2, pt2, eta2, 'triggerSingleEle')
        
        evt_eff = 1 - ( (1-eff_dbl_1_leadingleg)*(1-eff_dbl_2_leadingleg) + eff_dbl_1_leadingleg*(1-eff_dbl_2_trailingleg) + eff_dbl_2_leadingleg*(1-eff_dbl_1_trailingleg))  \
                  + eff_sgl_2*(1-eff_dbl_1_trailingleg)+ eff_sgl_1*(1-eff_dbl_2_trailingleg)

        #  
        # probability of passing the double lepton trigger + probability of passing the single lepton - the probability of passing both
        #  
        # probability of passing the double lepton trigger  ---> 1 - probability of not passing the double lepton trigger =
        #                                                      = 1 - (probability for both leptons to fail the leading lepton
        #                                                             + probability for the first  lepton to pass the leading leg but the second fails the trailing leg 
        #                                                             + probability for the second lepton to pass the leading leg but the first  fails the trailing leg 
        #                                           NEGLECTED:        + probability for both leptons to fail the trailing lepton 
        #                                                            )
        # 
        # + probability of passing the single lepton trigger:
        #                                                + probability that the second lepton passes the single lepton but the first  is failing the trailing trigger
        #                                                + probability that the first  lepton passes the single lepton but the second is failing the trailing trigger
        #                                                + probability that the first  lepton passes the single lepton but the second is failing the leading trigger
        #                                                + probability that the seond  lepton passes the single lepton but the first  is failing the leading trigger
        #
        # - the probability of passing both:
        #
        #
        #
        # The part neglected above in the double lepton part is neglected because: 
        #     - for double electron/muon triggers: if a lepton fails the trailing lepton, it will fail the leading lepton 
        #                      --> then it is included in "probability for both leptons to fail the leading lepton" 
        #
        # why not adding?
        # + probability that the first  lepton passes the single lepton but the second is failing the leading trigger
        # + probability that the seond  lepton passes the single lepton but the first  is failing the leading trigger
        # and neglecting the probability of passing both?
        #
        #  why why why ???
        #
        # For emu or mue events:
        #   probability of passing the the trigger mu+e or the trigger e+mu or the single mu or the single e
        #                             - 
        
        
        return evt_eff, 1.0, 1.0
       
       
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)


        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'effTrigW',
           'effTrigW_Up',
           'effTrigW_Down'
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


        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0
                
        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
              print i,'events processed.'

            self.oldBranchesToBeModifiedSimpleVariable['effTrigW'][0]      = 1.0
            self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Up'][0]   = 1.0
            self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Down'][0] = 1.0
               
            # now calculate the trigger weight
            if itree.std_vector_lepton_flavour.size() >= 2 :
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW'][0], \
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Down'][0], \
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Up'][0] = \
                  self._getWeight ( itree.std_vector_lepton_flavour[0], itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0], \
                                    itree.std_vector_lepton_flavour[1], itree.std_vector_lepton_pt[1], itree.std_vector_lepton_eta[1])

            else :
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW'][0] = 0.0
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Down'][0] = 0.0
              self.oldBranchesToBeModifiedSimpleVariable['effTrigW_Up'][0] = 0.0
      
            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


