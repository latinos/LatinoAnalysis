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

        group.add_option('--triggerDoubleEleLegHigPt', dest='triggerDoubleEleLegHigPt', help='file with trigger efficiencies triggerDoubleEleLegHigPt', default=None)
        group.add_option('--triggerDoubleEleLegLowPt', dest='triggerDoubleEleLegLowPt', help='file with trigger efficiencies triggerDoubleEleLegLowPt', default=None)
        group.add_option('--triggerSingleEle',     dest='triggerSingleEle',     help='file with trigger efficiencies triggerSingleEle',     default=None)

        group.add_option('--triggerDoubleMuLegHigPt', dest='triggerDoubleMuLegHigPt', help='file with trigger efficiencies triggerDoubleMuLegHigPt', default=None)
        group.add_option('--triggerDoubleMuLegLowPt', dest='triggerDoubleMuLegLowPt', help='file with trigger efficiencies triggerDoubleMuLegLowPt', default=None)
        group.add_option('--triggerSingleMu',     dest='triggerSingleMu',     help='file with trigger efficiencies triggerSingleMu',     default=None)

        group.add_option('--triggerMuEleLegHigPt', dest='triggerMuEleLegHigPt', help='file with trigger efficiencies triggerMuEleLegHigPt', default=None)
        group.add_option('--triggerMuEleLegLowPt', dest='triggerMuEleLegLowPt', help='file with trigger efficiencies triggerMuEleLegLowPt', default=None)
        group.add_option('--triggerEleMuLegHigPt', dest='triggerEleMuLegHigPt', help='file with trigger efficiencies triggerEleMuLegHigPt', default=None)
        group.add_option('--triggerEleMuLegLowPt', dest='triggerEleMuLegLowPt', help='file with trigger efficiencies triggerEleMuLegLowPt', default=None)

        parser.add_option_group(group)
        return group 

    def checkOptions(self,opts):
       
        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.triggerDoubleEleLegHigPt == None :
          opts.triggerDoubleEleLegHigPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele17_12LegHigPt.txt'
        if opts.triggerDoubleEleLegLowPt == None :
          opts.triggerDoubleEleLegLowPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele17_12LegLowPt.txt'
        if opts.triggerSingleEle == None :
          opts.triggerSingleEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_Ele23Single.txt'

        if opts.triggerDoubleMuLegHigPt == None :
          opts.triggerDoubleMuLegHigPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_DoubleMuLegHigPt.txt'
        if opts.triggerDoubleMuLegLowPt == None :
          opts.triggerDoubleMuLegLowPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_DoubleMuLegLowPt.txt'
        if opts.triggerSingleMu == None :
          opts.triggerSingleMu = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_MuSingle.txt'

        if opts.triggerMuEleLegHigPt == None :
          opts.triggerMuEleLegHigPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_MuEleLegHigPt.txt'
        if opts.triggerMuEleLegLowPt == None :
          opts.triggerMuEleLegLowPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_MuEleLegLowPt.txt'

        if opts.triggerEleMuLegHigPt == None :
          opts.triggerEleMuLegHigPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_EleMuLegHigPt.txt'
        if opts.triggerEleMuLegLowPt == None :
          opts.triggerEleMuLegLowPt = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/HLT_EleMuLegLowPt.txt'

        file_triggerDoubleEleLegHigPt = open (opts.triggerDoubleEleLegHigPt)
        file_triggerDoubleEleLegLowPt = open (opts.triggerDoubleEleLegLowPt)
        file_triggerSingleEle     = open (opts.triggerSingleEle)

        file_triggerDoubleMuLegHigPt = open (opts.triggerDoubleMuLegHigPt)
        file_triggerDoubleMuLegLowPt = open (opts.triggerDoubleMuLegLowPt)
        file_triggerSingleMu     = open (opts.triggerSingleMu)

        file_triggerMuEleLegHigPt = open (opts.triggerMuEleLegHigPt)
        file_triggerMuEleLegLowPt = open (opts.triggerMuEleLegLowPt)
        file_triggerEleMuLegHigPt = open (opts.triggerEleMuLegHigPt)
        file_triggerEleMuLegLowPt = open (opts.triggerEleMuLegLowPt)
        
        self.list_triggers = {}
        
        self.list_triggers['triggerDoubleEleLegHigPt']   =    [line.rstrip().split() for line in file_triggerDoubleEleLegHigPt]
        self.list_triggers['triggerDoubleEleLegLowPt']   =    [line.rstrip().split() for line in file_triggerDoubleEleLegLowPt]
        self.list_triggers['triggerSingleEle']       =    [line.rstrip().split() for line in file_triggerSingleEle]

        self.list_triggers['triggerDoubleMuLegHigPt']    =    [line.rstrip().split() for line in file_triggerDoubleMuLegHigPt]
        self.list_triggers['triggerDoubleMuLegLowPt']    =    [line.rstrip().split() for line in file_triggerDoubleMuLegLowPt]
        self.list_triggers['triggerSingleMu']        =    [line.rstrip().split() for line in file_triggerSingleMu]
        
        self.list_triggers['triggerMuEleLegHigPt']       =    [line.rstrip().split() for line in file_triggerMuEleLegHigPt]
        self.list_triggers['triggerMuEleLegLowPt']       =    [line.rstrip().split() for line in file_triggerMuEleLegLowPt]
        self.list_triggers['triggerEleMuLegHigPt']       =    [line.rstrip().split() for line in file_triggerEleMuLegHigPt]
        self.list_triggers['triggerEleMuLegLowPt']       =    [line.rstrip().split() for line in file_triggerEleMuLegLowPt]

        #     eta              pt          value    error
        # '-2.5', '-2.0', '10.0', '15.0', '0.000', '0.000'
        #
        # or
        #
        #     eta              pt          value    error_high    error_low
        # '-2.5', '-2.0', '10.0', '15.0', '0.000', '0.000',     '0.000'
        #
        
    def _getEff (self, pt, eta, whichTrigger):
        
        for point in self.list_triggers[whichTrigger] :
           
           if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
               
               eff       = float(point[4])
               error_eff = float(point[5])
               
               error_eff_up = eff + error_eff
               error_eff_lo = eff - error_eff
               
               # muons and electrons have provided different formats!
               if len(point) > 6 :
                  error_eff_lo = float(point[6])
                  error_eff_lo = eff - error_eff_lo                  
               
               # correction not to have >1 probability!!!
               if error_eff_up > 1.0 : 
                 error_eff_up = 1.0
               if error_eff_lo < 0.0 :
                 error_eff_lo = 0.0
                 
               return eff, error_eff_lo, error_eff_up
        
        return 0. , 0., 0.
           
         
         
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

        # only if leptons!
        if kindLep1 > -20 and kindLep2 > -20 :
         
          self._fixOverflowUnderflow (kindLep1, pt1, eta1)  
          self._fixOverflowUnderflow (kindLep2, pt2, eta2)  
          
          #
          # ele = 11
          # mu  = 13
          #
          singleLegA = "-"
          singleLegB = "-"
          doubleLegHigPtA = "-"
          doubleLegHigPtB = "-"
          doubleLegLowPtA = "-"
          doubleLegLowPtB = "-"
          
          #print " kindLep1 = ", kindLep1, " kindLep2 = ", kindLep2
          
          
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
            singleLegA  = "triggerSingleEle"
            singleLegB  = "triggerSingleEle"
            doubleLegHigPtA = "triggerDoubleEleLegHigPt"
            doubleLegHigPtB = "triggerDoubleEleLegHigPt"
            doubleLegLowPtA = "triggerDoubleEleLegLowPt"
            doubleLegLowPtB = "triggerDoubleEleLegLowPt"
            
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            singleLegA  = "triggerSingleMu"
            singleLegB  = "triggerSingleMu"
            doubleLegHigPtA = "triggerDoubleMuLegHigPt"
            doubleLegHigPtB = "triggerDoubleMuLegHigPt"
            doubleLegLowPtA = "triggerDoubleMuLegLowPt"
            doubleLegLowPtB = "triggerDoubleMuLegLowPt"
       
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            singleLegA  = "triggerSingleMu"
            singleLegB  = "triggerSingleEle"
            doubleLegHigPtA = "triggerMuEleLegHigPt"
            doubleLegHigPtB = "triggerMuEleLegHigPt"
            doubleLegLowPtA = "triggerMuEleLegLowPt"
            doubleLegLowPtB = "triggerMuEleLegLowPt"
            
          if abs(kindLep1) == 11 and abs(kindLep2) == 13 :
            singleLegA  = "triggerSingleEle"
            singleLegB  = "triggerSingleMu"
            doubleLegHigPtA = "triggerEleMuLegHigPt"
            doubleLegHigPtB = "triggerEleMuLegHigPt"
            doubleLegLowPtA = "triggerEleMuLegLowPt"
            doubleLegLowPtB = "triggerEleMuLegLowPt"
       
          
          eff_dbl_1_leadingleg  , low_eff_dbl_1_leadingleg  , high_eff_dbl_1_leadingleg   = self._getEff (pt1, eta1, doubleLegHigPtA)
          eff_dbl_2_leadingleg  , low_eff_dbl_2_leadingleg  , high_eff_dbl_2_leadingleg   = self._getEff (pt2, eta2, doubleLegHigPtB)
          eff_dbl_1_trailingleg , low_eff_dbl_1_trailingleg , high_eff_dbl_1_trailingleg  = self._getEff (pt1, eta1, doubleLegLowPtA)
          eff_dbl_2_trailingleg , low_eff_dbl_2_trailingleg , high_eff_dbl_2_trailingleg  = self._getEff (pt2, eta2, doubleLegLowPtB)
          eff_sgl_1             , low_eff_sgl_1             , high_eff_sgl_1              = self._getEff (pt1, eta1, singleLegA)
          eff_sgl_2             , low_eff_sgl_2             , high_eff_sgl_2              = self._getEff (pt2, eta2, singleLegB)
          
          evt_eff = 1 - ( (1-eff_dbl_1_leadingleg)*(1-eff_dbl_2_leadingleg) + eff_dbl_1_leadingleg*(1-eff_dbl_2_trailingleg) + eff_dbl_2_leadingleg*(1-eff_dbl_1_trailingleg))  \
                    + eff_sgl_2*(1-eff_dbl_1_trailingleg)+ eff_sgl_1*(1-eff_dbl_2_trailingleg)
       
          # up variation ...
          
          eff_dbl_1_leadingleg  = high_eff_dbl_1_leadingleg    
          eff_dbl_2_leadingleg  = high_eff_dbl_2_leadingleg    
          eff_dbl_1_trailingleg = high_eff_dbl_1_trailingleg   
          eff_dbl_2_trailingleg = high_eff_dbl_2_trailingleg   
          eff_sgl_1             = high_eff_sgl_1               
          eff_sgl_2             = high_eff_sgl_2            
          
          evt_eff_error_up = 1 - ( (1-eff_dbl_1_leadingleg)*(1-eff_dbl_2_leadingleg) + eff_dbl_1_leadingleg*(1-eff_dbl_2_trailingleg) + eff_dbl_2_leadingleg*(1-eff_dbl_1_trailingleg))  \
                    + eff_sgl_2*(1-eff_dbl_1_trailingleg)+ eff_sgl_1*(1-eff_dbl_2_trailingleg)
       
       
          # and low variation ...
          eff_dbl_1_leadingleg  = low_eff_dbl_1_leadingleg   
          eff_dbl_2_leadingleg  = low_eff_dbl_2_leadingleg   
          eff_dbl_1_trailingleg = low_eff_dbl_1_trailingleg  
          eff_dbl_2_trailingleg = low_eff_dbl_2_trailingleg  
          eff_sgl_1             = low_eff_sgl_1              
          eff_sgl_2             = low_eff_sgl_2              
       
          evt_eff_error_low = 1 - ( (1-eff_dbl_1_leadingleg)*(1-eff_dbl_2_leadingleg) + eff_dbl_1_leadingleg*(1-eff_dbl_2_trailingleg) + eff_dbl_2_leadingleg*(1-eff_dbl_1_trailingleg))  \
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
          
          
          return evt_eff, evt_eff_error_low, evt_eff_error_up
        else : 
          # if for any reason it is not a lepton ... 
          return 1, 1, 1
       
       
       
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


