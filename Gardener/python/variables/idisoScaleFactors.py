import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner

#
#  _ _|      |         /     _ _|                    ___|                |            ____|             |                           
#    |    _` |        /        |    __|   _ \      \___ \    __|   _` |  |   _ \      |     _` |   __|  __|   _ \    __|  __| 
#    |   (   |       /         |  \__ \  (   |           |  (     (   |  |   __/      __|  (   |  (     |    (   |  |   \__ \ 
#  ___| \__,_|     _/        ___| ____/ \___/      _____/  \___| \__,_| _| \___|     _|   \__,_| \___| \__| \___/  _|   ____/ 
#                                                                                                                             
#

class IdIsoSFFiller(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a new lepton scale factor weight based on id/isolation scale factors data/MC.'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-e', '--isoidele', dest='idIsoScaleFactorsFileEle' , help='file with scale factors for isolation and id for electrons', default=None)
        group.add_option('-m', '--isoidmu' , dest='idIsoScaleFactorsFileMuon', help='file with scale factors for isolation and id for muons',     default=None)

        parser.add_option_group(group)
        return group



    def checkOptions(self,opts):
       
        # ~~~~
        idIsoScaleFactors = {}

        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.idIsoScaleFactorsFileEle == None :
          opts.idIsoScaleFactorsFileEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/electrons_Moriond74x.py'
        if opts.idIsoScaleFactorsFileMuon == None :
          opts.idIsoScaleFactorsFileMuon = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/electrons_Moriond74x.py'
           
        os.path.exists(opts.idIsoScaleFactorsFileEle) 
        handleEle = open(opts.idIsoScaleFactorsFileEle,'r')
        exec(handleEle)
        handleEle.close()

        os.path.exists(opts.idIsoScaleFactorsFileMuon)
        handleMu = open(opts.idIsoScaleFactorsFileMuon,'r')
        exec(handleMu)
        handleMu.close()

        #print " idIsoScaleFactors = ", self.idIsoScaleFactors
        self.idIsoScaleFactors = idIsoScaleFactors

        self.minpt_mu = 10
        self.maxpt_mu = 200
        self.mineta_mu = -2.4
        self.maxeta_mu = 2.4
        
        self.minpt_ele = 10
        self.maxpt_ele = 200
        self.mineta_ele = -2.5
        self.maxeta_ele = 2.5


    def _getWeight (self, kindLep, pt, eta):

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
 
 
        #print " self.idIsoScaleFactors = ", self.idIsoScaleFactors
        
        if kindLep in self.idIsoScaleFactors.keys() : 
          # get the efficiency
          if kindLep == 'ele' :
            for point in self.idIsoScaleFactors[kindLep] : 
              #   (( #   eta          ), (|    pt        |),   (   eff_data   stat   |     eff_mc   stat |      other nuisances
              #  (( -2.500 ,  -2.000 ), ( 10.000 ,  20.000 ), ( 0.358 ,   0.009 ),     (  0.286 ,   0.002  ), ( 0.094 ,   0.048 ,   0.071 ,   0.127 ,   -1   ,    -1  ) ), 
              
              if ( eta >= point[0][0] and eta <= point[0][1] and         # the "=" in both directions is only used by the overflow bin
                   pt  >= point[1][0] and pt  <= point[1][1] ) :         # in other cases the set is (min, max]
                  data = point[2][0]
                  mc   = point[3][0]
      
                  sigma_data = point[2][1]
                  sigma_mc   = point[3][1]
                  
                  scaleFactor = data / mc
                  error_scaleFactor = math.sqrt((sigma_data / mc) * (sigma_data / mc) + (data / mc / mc * sigma_mc)*(data / mc / mc * sigma_mc))
                  
                  return scaleFactor, error_scaleFactor, error_scaleFactor
      
            # default ... it should never happen!
            # print " default ???"
            return 1.0, 0.0, 0.0


          elif kindLep == 'mu' :
            for point in self.idIsoScaleFactors[kindLep] : 
            #     Data                                                                                                   MC
            # etamin  etamax            ptmin   ptmax         eff     deff_high       deff_low                                     eff     deff_high       deff_low
            # ((  -2.4  ,  -2.1  ),   (  10  ,    12  ),   (  0.609191   ,     0.0505912    ,    0.046392      )      ,    (      0.662717    ,    0.0318054    ,    0.0310346    )  ),
  
              if ( eta >= point[0][0] and eta <= point[0][1] and         # the "=" in both directions is only used by the overflow bin
                   pt  >= point[1][0] and pt  <= point[1][1] ) :         # in other cases the set is (min, max]
                  data = point[2][0]
                  mc   = point[3][0]
      
                  sigma_up_data = point[2][1]
                  sigma_up_mc   = point[3][1]

                  sigma_do_data = point[2][2]
                  sigma_do_mc   = point[3][2]
                  
                  scaleFactor = data / mc
                  error_scaleFactor_up = (data + sigma_up_data) / (mc - sigma_do_mc)  - scaleFactor
                  error_scaleFactor_do = scaleFactor -   (data - sigma_do_data) / (mc + sigma_up_mc)  
                  
                  return scaleFactor, error_scaleFactor_do, error_scaleFactor_up
      
            # default ... it should never happen!
            # print " default ???"
            return 1.0, 0.0, 0.0

      
          # not a lepton ... like some default value: and what can it be if not a lepton? ah ah 
          # --> it happens for default values -9999.
          return 1.0, 0.0, 0.0

        # not a lepton ... like some default value: and what can it be if not a lepton? ah ah 
        # --> it happens for default values -9999.
        return 1.0, 0.0, 0.0



   
   
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        self.namesOldBranchesToBeModifiedVector = [
           'std_vector_lepton_idisoW',
           'std_vector_lepton_idisoW_Up',
           'std_vector_lepton_idisoW_Down'                              
           ]
        
        self.clone(output,self.namesOldBranchesToBeModifiedVector)


        bvector_idiso =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoW',bvector_idiso)
        bvector_idiso_Up =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoW_Up',bvector_idiso_Up)
        bvector_idiso_Down =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoW_Down',bvector_idiso_Down)
            
            
            
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

            bvector_idiso.clear()
            bvector_idiso_Up.clear()
            bvector_idiso_Down.clear()

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
             
              pt = itree.std_vector_lepton_pt [iLep]
              eta = itree.std_vector_lepton_eta [iLep]
              flavour = itree.std_vector_lepton_flavour [iLep]
              
              kindLep = 'nonlep' # ele or mu
              if abs (flavour) == 11 : 
                kindLep = 'ele'
              elif abs (flavour) == 13 :
                kindLep = 'mu'
 
 
              w, error_w_lo, error_w_up = self._getWeight (kindLep, pt, eta)
             
              bvector_idiso.push_back(w)
              bvector_idiso_Up.push_back(w+error_w_up)
              bvector_idiso_Down.push_back(w-error_w_lo)             


            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


