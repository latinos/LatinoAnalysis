#
#
#
#   \ \        / \ \        /       \  |  |      |
#    \ \  \   /   \ \  \   /         \ |  |      |
#     \ \  \ /     \ \  \ /        |\  |  |      |
#      \_/\_/       \_/\_/        _| \_| _____| _____|
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

class wwNLLcorrectionWeightFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add weight for WW NLL reweighting'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-m', '--mcsample'    , dest='mcsample', help='Name of the mc sample to be considered. Possible options [powheg, mcatnlo, madgraph]',)
        parser.add_option_group(group)

        return group


    def checkOptions(self,opts):
        if (
             not hasattr(opts,'mcsample')      ) :
            raise RuntimeError('Missing parameter')

        self.mcsample = opts.mcsample

    def process(self,**kwargs):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/wwNLLcorrectionWeight.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/wwNLLcorrectionWeight.C++g')
        #----------------------------------------------------------------------------------------------------

        wwNLL = ROOT.wwNLL(self.mcsample, 
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/central.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/resum_up.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/resum_down.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/scale_up.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/scale_down.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/nnlo_central.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_nlo.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_qup_nlo.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_qdown_nlo.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_sup_nlo.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_sdown_nlo.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/powheg_2l2nu_nnlo.dat'
                           )

        print " starting ..."

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = ['nllnnloW', 'nllW', 'nllW_Rup', 'nllW_Qup', 'nllW_Rdown', 'nllW_Qdown', 'gen_mww', 'gen_ptww']
        self.clone(output,newbranches)


        nllnnloW    = numpy.ones(1, dtype=numpy.float32)
        nllW        = numpy.ones(1, dtype=numpy.float32)
        nllW_Rup    = numpy.ones(1, dtype=numpy.float32)
        nllW_Qup    = numpy.ones(1, dtype=numpy.float32)
        nllW_Rdown  = numpy.ones(1, dtype=numpy.float32)
        nllW_Qdown  = numpy.ones(1, dtype=numpy.float32)
        gen_mww     = numpy.ones(1, dtype=numpy.float32)
        gen_ptww    = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('nllnnloW'  , nllnnloW  , 'nllnnloW/F')
        self.otree.Branch('nllW'  , nllW  , 'nllW/F')
        self.otree.Branch('nllW_Rup'  , nllW_Rup  , 'nllW_Rup/F')
        self.otree.Branch('nllW_Qup'  , nllW_Qup  , 'nllW_Qup/F')
        self.otree.Branch('nllW_Rdown'  , nllW_Rdown  , 'nllW_Rdown/F')
        self.otree.Branch('nllW_Qdown'  , nllW_Qdown  , 'nllW_Qdown/F')
        self.otree.Branch('gen_mww'  , gen_mww   , 'gen_mww/F')
        self.otree.Branch('gen_ptww' , gen_ptww  , 'gen_ptww/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):
        #for i in xrange(100):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            # after ISR but before QED FSR
            # because at calculation step these are not defined
            # and they don't know about photons
            # use lvlv status=3 (?? why not 1??) particles

            #number1 = -1
            #number2 = -1
            
            #for numlepton in range(0, itree.std_vector_leptonGen_pt.size()):
              #if itree.std_vector_leptonGen_isHardProcess.at(numlepton) == 1 :
                #if number1 == -1 :
                  #number1 = numlepton
                #else :
                  #number2 = numlepton
                  
            #print "     number1 = ",  number1           
            #print "     number2 = ",  number2

            #numberneutrino1 = -1
            #numberneutrino2 = -1
            
            #for numlepton in range(0, itree.std_vector_neutrinoGen_pt.size()):
              #if itree.std_vector_neutrinoGen_isHardProcess.at(numlepton) == 1 :
                #if numberneutrino1 == -1 :
                  #numberneutrino1 = numlepton
                #else :
                  #numberneutrino2 = numlepton

            #print "     numberneutrino1 = ",  numberneutrino1           
            #print "     numberneutrino2 = ",  numberneutrino2


            #ptl1 = itree.std_vector_leptonGen_pt.at(number1)
            #ptl2 = itree.std_vector_leptonGen_pt.at(number2)
            #phil1 = itree.std_vector_leptonGen_phi.at(number1)
            #phil2 = itree.std_vector_leptonGen_phi.at(number2)

            #ptv1 = itree.std_vector_neutrinoGen_pt.at(numberneutrino1)
            #ptv2 = itree.std_vector_neutrinoGen_pt.at(numberneutrino2)
            #phiv1 = itree.std_vector_neutrinoGen_phi.at(numberneutrino1)
            #phiv2 = itree.std_vector_neutrinoGen_phi.at(numberneutrino2)

            #wwNLL.SetPTWW(ptl1, phil1, ptl2, phil2, ptv1, phiv1, ptv2, phiv2)



            number1 = -1
            number2 = -1
            
            #print "--------"
            #print " size = ", itree.std_vector_VBoson_pt.size()
            
            for numlepton in range(0, itree.std_vector_VBoson_pt.size()):
              #print " - ", numlepton, " :: ", itree.std_vector_VBoson_fromHardProcessBeforeFSR.at(numlepton), " :: ", abs(itree.std_vector_VBoson_pid.at(numlepton))
              if itree.std_vector_VBoson_fromHardProcessBeforeFSR.at(numlepton) == 1 and abs(itree.std_vector_VBoson_pid.at(numlepton)) == 24 :
                if number1 == -1 :
                  number1 = numlepton
                else :
                  number2 = numlepton

            #print "     number1 = ",  number1           
            #print "     number2 = ",  number2

            if number1 != -1 and number2 != -1 : 
              ptV1 = itree.std_vector_VBoson_pt.at(number1)
              ptV2 = itree.std_vector_VBoson_pt.at(number2)
              phiV1 = itree.std_vector_VBoson_phi.at(number1)
              phiV2 = itree.std_vector_VBoson_phi.at(number2)
              etaV1 = itree.std_vector_VBoson_eta.at(number1)
              etaV2 = itree.std_vector_VBoson_eta.at(number2)

              wwNLL.SetPTWW(ptV1, phiV1, etaV1, ptV2, phiV2, etaV2)
              
              gen_ptww[0]  = wwNLL.GetPTWW()
              gen_mww[0]   = wwNLL.GetMWW()
              
            else :
              gen_mww[0]  = -9999.
              gen_ptww[0] = -9999.
              

            nllnnloW[0] = wwNLL.nllnnloWeight(0)
            nllW[0]   = wwNLL.nllWeight(0)
            nllW_Rup[0]   = wwNLL.nllWeight(1,1)
            nllW_Qup[0]   = wwNLL.nllWeight(1,0)
            nllW_Rdown[0] = wwNLL.nllWeight(-1,1)
            nllW_Qdown[0] = wwNLL.nllWeight(-1,0)

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'

