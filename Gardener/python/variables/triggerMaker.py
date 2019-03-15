import optparse
import numpy
import ROOT
import os.path
import copy
import math
import re

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

class triggerCalculator():
    def __init__ (self,Trigger,cmssw,iPeriod,isData=False):
       print "-------- triggerCalculator init() ---------", cmssw , iPeriod , isData
       self.EMTFBug = Trigger[cmssw][iPeriod]['EMTFBug']
       print 'EMTF Bug : ' ,self.EMTFBug

       if isData: 
         self.EleMu     = copy.deepcopy(Trigger[cmssw][iPeriod]['DATA']['EleMu']) 
         self.DoubleMu  = copy.deepcopy(Trigger[cmssw][iPeriod]['DATA']['DoubleMu']) 
         self.SingleMu  = copy.deepcopy(Trigger[cmssw][iPeriod]['DATA']['SingleMu']) 
         self.DoubleEle = copy.deepcopy(Trigger[cmssw][iPeriod]['DATA']['DoubleEle']) 
         self.SingleEle = copy.deepcopy(Trigger[cmssw][iPeriod]['DATA']['SingleEle']) 
         print 'EleMu     = ' , self.EleMu
         print 'DoubleMu  = ' , self.DoubleMu
         print 'SingleMu  = ' , self.SingleMu
         print 'DoubleEle = ' , self.DoubleEle
         print 'SingleEle = ' , self.SingleEle

       else:
         if 'MC' in Trigger[cmssw][iPeriod] :
           self.EleMu     = copy.deepcopy(Trigger[cmssw][iPeriod]['MC']['EleMu'])
           self.DoubleMu  = copy.deepcopy(Trigger[cmssw][iPeriod]['MC']['DoubleMu'])
           self.SingleMu  = copy.deepcopy(Trigger[cmssw][iPeriod]['MC']['SingleMu'])
           self.DoubleEle = copy.deepcopy(Trigger[cmssw][iPeriod]['MC']['DoubleEle'])
           self.SingleEle = copy.deepcopy(Trigger[cmssw][iPeriod]['MC']['SingleEle'])
           print 'EleMu     = ' , self.EleMu
           print 'DoubleMu  = ' , self.DoubleMu
           print 'SingleMu  = ' , self.SingleMu
           print 'DoubleEle = ' , self.DoubleEle
           print 'SingleEle = ' , self.SingleEle

         self.list_triggers = {}
         cmssw_base = os.getenv('CMSSW_BASE')
         print "DoubleEleLegHigPt : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleEleLegHigPt']
         print "DoubleEleLegLowPt : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleEleLegLowPt']
         print "SingleEle         : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['SingleEle']
  
         print "DoubleMuLegHigPt  : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleMuLegHigPt']
         print "DoubleMuLegLowPt  : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleMuLegLowPt']
         print "SingleMu          : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['SingleMu']
  
         print "MuEleLegHigPt     : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['MuEleLegHigPt']
         print "MuEleLegLowPt     : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['MuEleLegLowPt']
         print "EleMuLegHigPt     : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['EleMuLegHigPt']
         print "EleMuLegLowPt     : " , cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['EleMuLegLowPt']
  
  
         file_triggerDoubleEleLegHigPt = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleEleLegHigPt'])
         file_triggerDoubleEleLegLowPt = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleEleLegLowPt'])
         file_triggerSingleEle         = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['SingleEle'])
  
         file_triggerDoubleMuLegHigPt  = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleMuLegHigPt'])
         file_triggerDoubleMuLegLowPt  = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['DoubleMuLegLowPt'])
         file_triggerSingleMu          = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['SingleMu'])
  
         file_triggerMuEleLegHigPt     = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['MuEleLegHigPt'])
         file_triggerMuEleLegLowPt     = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['MuEleLegLowPt'])
         file_triggerEleMuLegHigPt     = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['EleMuLegHigPt'])
         file_triggerEleMuLegLowPt     = open (cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/'+Trigger[cmssw][iPeriod]['LegEff']['EleMuLegLowPt'])
  
         self.list_triggers['triggerDoubleEleLegHigPt']   =    [line.rstrip().split() for line in file_triggerDoubleEleLegHigPt        if '#' not in line]
         self.list_triggers['triggerDoubleEleLegLowPt']   =    [line.rstrip().split() for line in file_triggerDoubleEleLegLowPt        if '#' not in line]
         self.list_triggers['triggerSingleEle']           =    [line.rstrip().split() for line in file_triggerSingleEle                if '#' not in line]
  
         self.list_triggers['triggerDoubleMuLegHigPt']    =    [line.rstrip().split() for line in file_triggerDoubleMuLegHigPt        if '#' not in line]
         self.list_triggers['triggerDoubleMuLegLowPt']    =    [line.rstrip().split() for line in file_triggerDoubleMuLegLowPt        if '#' not in line]
         self.list_triggers['triggerSingleMu']            =    [line.rstrip().split() for line in file_triggerSingleMu                if '#' not in line]
  
         self.list_triggers['triggerMuEleLegHigPt']       =    [line.rstrip().split() for line in file_triggerMuEleLegHigPt        if '#' not in line]
         self.list_triggers['triggerMuEleLegLowPt']       =    [line.rstrip().split() for line in file_triggerMuEleLegLowPt        if '#' not in line]
         self.list_triggers['triggerEleMuLegHigPt']       =    [line.rstrip().split() for line in file_triggerEleMuLegHigPt        if '#' not in line]
         self.list_triggers['triggerEleMuLegLowPt']       =    [line.rstrip().split() for line in file_triggerEleMuLegLowPt        if '#' not in line]
  
         file_triggerDoubleEleLegHigPt.close()
         file_triggerDoubleEleLegLowPt.close()
         file_triggerSingleEle.close()
  
         file_triggerDoubleMuLegHigPt.close()
         file_triggerDoubleMuLegLowPt.close()
         file_triggerSingleMu.close()
  
         file_triggerMuEleLegHigPt.close()
         file_triggerMuEleLegLowPt.close()
         file_triggerEleMuLegHigPt.close()
         file_triggerEleMuLegLowPt.close()
 
         self.DZEff_DoubleEle = Trigger[cmssw][iPeriod]['DZEff']['DoubleEle'] 
         self.DZEff_DoubleMu  = Trigger[cmssw][iPeriod]['DZEff']['DoubleMu'] 
         self.DZEff_MuEle     = Trigger[cmssw][iPeriod]['DZEff']['MuEle'] 
         self.DZEff_EleMu     = Trigger[cmssw][iPeriod]['DZEff']['EleMu'] 

         print 'DZ Eff DoubleEle = ' , self.DZEff_DoubleEle
         print 'DZ Eff DoubleMu  = ' , self.DZEff_DoubleMu 
         print 'DZ Eff MuEle     = ' , self.DZEff_MuEle    
         print 'DZ Eff EleMu     = ' , self.DZEff_EleMu


         self.trkSFMu = copy.deepcopy(Trigger[cmssw][iPeriod]['trkSFMu'])
 
         self.minpt_mu = 10
         self.maxpt_mu = 200
         self.mineta_mu = -2.4
         self.maxeta_mu = 2.4
  
         self.minpt_ele = 10
         self.maxpt_ele = 100
         self.mineta_ele = -2.5
         self.maxeta_ele = 2.5

    def _getEff (self, pt, eta, whichTrigger):

        for point in self.list_triggers[whichTrigger] :
           #print " point = ", point
           if len(point) > 2 :
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

        #print " is 0 ... ", pt, "  ", eta, "   " , whichTrigger
        #if pt > 100:
          #for point in self.list_triggers[whichTrigger] :
            #print " ---> ", float(point[0]), " ", float(point[1]), " ", float(point[2]), " ", float(point[3])

        return 0. , 0., 0.

    def _fixOverflowUnderflow (self, kindLep, pt, eta):

        # formy education: read here, http://stackoverflow.com/questions/15148496/python-passing-an-integer-by-reference

        # fix underflow and overflow

        if abs(kindLep) == 11 :
          if pt[0] < self.minpt_ele:
            pt[0] = self.minpt_ele
          if pt[0] > self.maxpt_ele:
            pt[0] = self.maxpt_ele

          if eta[0] < self.mineta_ele:
            eta[0] = self.mineta_ele
          if eta[0] > self.maxeta_ele:
            eta[0] = self.maxeta_ele

        if abs(kindLep) == 13 :
          if pt[0] < self.minpt_mu:
            pt[0] = self.minpt_mu
          if pt[0] > self.maxpt_mu:
            pt[0] = self.maxpt_mu

          if eta[0] < self.mineta_mu:
            eta[0] = self.mineta_mu
          if eta[0] > self.maxeta_mu:
            eta[0] = self.maxeta_mu

        return pt[0], eta[0]

    def _getWeight (self, kindLep1, pt1, eta1, kindLep2, pt2, eta2):

        # only if leptons!
        if kindLep1 > -20 and kindLep2 > -20 :

          vpt1 = [pt1]
          veta1 = [eta1]
          vpt2 = [pt2]
          veta2 = [eta2]

          self._fixOverflowUnderflow (kindLep1, vpt1, veta1)
          self._fixOverflowUnderflow (kindLep2, vpt2, veta2)

          pt1 = vpt1[0]
          eta1 = veta1[0]
          pt2 = vpt2[0]
          eta2 = veta2[0]

          #if pt2>100:
            #print " ", kindLep2," ",  pt2, " ", eta2
          #if pt1>100:
            #print " ", kindLep1," ",  pt1, " ", eta1

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

          dz_eff = 1.00

          #                  ele                     ele
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
            singleLegA  = "triggerSingleEle"
            singleLegB  = "triggerSingleEle"
            doubleLegHigPtA = "triggerDoubleEleLegHigPt"
            doubleLegHigPtB = "triggerDoubleEleLegHigPt"
            doubleLegLowPtA = "triggerDoubleEleLegLowPt"
            doubleLegLowPtB = "triggerDoubleEleLegLowPt"
            dz_eff = self.DZEff_DoubleEle

          #                   mu                      mu            
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            singleLegA  = "triggerSingleMu"
            singleLegB  = "triggerSingleMu"
            doubleLegHigPtA = "triggerDoubleMuLegHigPt"
            doubleLegHigPtB = "triggerDoubleMuLegHigPt"
            doubleLegLowPtA = "triggerDoubleMuLegLowPt"
            doubleLegLowPtB = "triggerDoubleMuLegLowPt"
            dz_eff = self.DZEff_DoubleMu 

          #                   mu                     ele       
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            singleLegA  = "triggerSingleMu"
            singleLegB  = "triggerSingleEle"
            doubleLegHigPtA = "triggerMuEleLegHigPt"
            doubleLegHigPtB = "triggerEleMuLegHigPt"
            doubleLegLowPtA = "triggerEleMuLegLowPt"
            doubleLegLowPtB = "triggerMuEleLegLowPt"
            dz_eff = self.DZEff_MuEle

          #                   ele                     mu                   
          if abs(kindLep1) == 11 and abs(kindLep2) == 13 :
            singleLegA  = "triggerSingleEle"
            singleLegB  = "triggerSingleMu"
            doubleLegHigPtA = "triggerEleMuLegHigPt"
            doubleLegHigPtB = "triggerMuEleLegHigPt"
            doubleLegLowPtA = "triggerMuEleLegLowPt"
            doubleLegLowPtB = "triggerEleMuLegLowPt"
            dz_eff = self.DZEff_EleMu


          # Get Leg Efficiencies

          eff_dbl_1_leadingleg  , low_eff_dbl_1_leadingleg  , high_eff_dbl_1_leadingleg   = self._getEff (pt1, eta1, doubleLegHigPtA)
          eff_dbl_2_leadingleg  , low_eff_dbl_2_leadingleg  , high_eff_dbl_2_leadingleg   = self._getEff (pt2, eta2, doubleLegHigPtB)
          eff_dbl_1_trailingleg , low_eff_dbl_1_trailingleg , high_eff_dbl_1_trailingleg  = self._getEff (pt1, eta1, doubleLegLowPtA)
          eff_dbl_2_trailingleg , low_eff_dbl_2_trailingleg , high_eff_dbl_2_trailingleg  = self._getEff (pt2, eta2, doubleLegLowPtB)
          eff_sgl_1             , low_eff_sgl_1             , high_eff_sgl_1              = self._getEff (pt1, eta1, singleLegA)
          eff_sgl_2             , low_eff_sgl_2             , high_eff_sgl_2              = self._getEff (pt2, eta2, singleLegB)

          # Add 5% syst to SnglEle
          if singleLegA == "triggerSingleEle" :
            systdown       = eff_sgl_1 - low_eff_sgl_1
            systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05) 
            low_eff_sgl_1  = max(0.,eff_sgl_1 - systdown_new)
            systup         = high_eff_sgl_1 - eff_sgl_1
            systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
            high_eff_sgl_1 = min(1.,eff_sgl_1+systup_new)
          if singleLegB == "triggerSingleEle" :
            systdown       = eff_sgl_2 - low_eff_sgl_2
            systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05)
            low_eff_sgl_2  = max(0.,eff_sgl_2 - systdown_new)
            systup         = high_eff_sgl_2 - eff_sgl_2
            systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
            high_eff_sgl_2 = min(1.,eff_sgl_2+systup_new)



          # Tracker Muon SF

          if abs(kindLep1) == 13 :

             eff_sgl_1       *=  self.trkSFMu[0] 
             high_eff_sgl_1  *=  self.trkSFMu[1]
             low_eff_sgl_1   *=  self.trkSFMu[2]
              
             eff_dbl_1_leadingleg           *=  self.trkSFMu[0]
             high_eff_dbl_1_leadingleg      *=  self.trkSFMu[1]
             low_eff_dbl_1_leadingleg       *=  self.trkSFMu[2]

             eff_dbl_1_trailingleg          *=  self.trkSFMu[0]
             high_eff_dbl_1_trailingleg     *=  self.trkSFMu[1]
             low_eff_dbl_1_trailingleg      *=  self.trkSFMu[0]

          if abs(kindLep2) == 13 :

             eff_sgl_2       *=  self.trkSFMu[0]
             high_eff_sgl_2  *=  self.trkSFMu[1]
             low_eff_sgl_2   *=  self.trkSFMu[2]

             eff_dbl_2_leadingleg           *=  self.trkSFMu[0]
             high_eff_dbl_2_leadingleg      *=  self.trkSFMu[1]
             low_eff_dbl_2_leadingleg       *=  self.trkSFMu[2]

             eff_dbl_2_trailingleg          *=  self.trkSFMu[0]
             high_eff_dbl_2_trailingleg     *=  self.trkSFMu[1]
             low_eff_dbl_2_trailingleg      *=  self.trkSFMu[0]

          # Event Efficiency

          #evt_eff =   eff_sgl_1 + eff_sgl_2 -    \
          #            eff_sgl_1*eff_sgl_2 +   \
          #            (1-eff_sgl_1-(1-eff_sgl_1)*eff_sgl_2) *  \
          #            (eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg) *  \
          #            dz_eff

         
          eff_double = (eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg)


          evt_eff =   (eff_double + eff_sgl_1 * (1. - eff_dbl_2_trailingleg) + eff_sgl_2*(1. - eff_dbl_1_trailingleg))*    \
                      dz_eff          
 
          # Single lepton only

          #                   ele                    ele
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
            evt_eff_snglEle = eff_sgl_1 + (1-eff_sgl_1) * eff_sgl_2
            evt_eff_snglMu  = 0.0
          #                   mu                     mu
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            evt_eff_snglEle = 0.0
            evt_eff_snglMu  = eff_sgl_1 + (1-eff_sgl_1) * eff_sgl_2
          #                   mu                     ele       
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            evt_eff_snglEle = eff_sgl_2
            evt_eff_snglMu  = eff_sgl_1
          #                   ele                     mu                   
          if abs(kindLep1) == 11 and abs(kindLep2) == 13 :
            evt_eff_snglEle = eff_sgl_1
            evt_eff_snglMu  = eff_sgl_2

          eff_tl = eff_dbl_1_leadingleg * eff_dbl_2_trailingleg
          eff_lt = eff_dbl_2_leadingleg * eff_dbl_1_trailingleg
          #                   ele                    ele
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
            eff_tl *= dz_eff
            eff_lt *= dz_eff
            evt_eff_dbleEle = eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg #eff_tl + (1-eff_tl) * eff_lt
            evt_eff_dbleMu  = 0.0
            evt_eff_EleMu   = 0.0
          #                   mu                     mu
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            eff_tl *= dz_eff
            eff_lt *= dz_eff
            evt_eff_dbleEle = 0.0
            evt_eff_dbleMu  = eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg #eff_tl + (1-eff_tl) * eff_lt
            evt_eff_EleMu   = 0.0
          #                   mu                     ele       
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            evt_eff_dbleEle = 0.0
            evt_eff_dbleMu  = 0.0
            evt_eff_EleMu   = eff_tl + (1-eff_tl) * eff_lt
          #                   ele                     mu                   
          if abs(kindLep1) == 11 and abs(kindLep2) == 13 :
            evt_eff_dbleEle = 0.0
            evt_eff_dbleMu  = 0.0
            evt_eff_EleMu   = eff_tl + (1-eff_tl) * eff_lt

          # And the Trigger Emulation
          # 0: Combo / 1:SnglEle / 2: SnglMu / 3:DbleEle / 4:DbleMu / 5: EleMu

          TrgEmulator = [ False , False , False , False , False , False ]

          #                   ele                    ele
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
            # SnglEle
            Leg1 = eff_sgl_1  > ROOT.gRandom.Rndm()
            Leg2 = eff_sgl_2  > ROOT.gRandom.Rndm()
            TrgEmulator[1] = Leg1 or Leg2
            # DbleEle
            Leg1_tl  = eff_dbl_1_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_tl  = eff_dbl_2_trailingleg > ROOT.gRandom.Rndm()
            DZpass   = dz_eff > ROOT.gRandom.Rndm()
            Leg12_tl = Leg1_tl and Leg2_tl and DZpass
            Leg1_lt  = eff_dbl_2_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_lt  = eff_dbl_1_trailingleg > ROOT.gRandom.Rndm()
            DZpass   = dz_eff > ROOT.gRandom.Rndm()
            Leg12_lt = Leg1_lt and Leg2_lt and DZpass
            TrgEmulator[3] = Leg12_tl or Leg12_lt
          #                   mu                     mu
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            # SnglMu 
            Leg1 = eff_sgl_1  > ROOT.gRandom.Rndm()
            Leg2 = eff_sgl_2  > ROOT.gRandom.Rndm()
            TrgEmulator[2] = Leg1 or Leg2
            # DbleMu 
            Leg1_tl  = eff_dbl_1_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_tl  = eff_dbl_2_trailingleg > ROOT.gRandom.Rndm()
            DZpass   = dz_eff > ROOT.gRandom.Rndm()
            Leg12_tl = Leg1_tl and Leg2_tl and DZpass
            Leg1_lt  = eff_dbl_2_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_lt  = eff_dbl_1_trailingleg > ROOT.gRandom.Rndm()
            DZpass   = dz_eff > ROOT.gRandom.Rndm()
            Leg12_lt = Leg1_lt and Leg2_lt and DZpass
            TrgEmulator[4] = Leg12_tl or Leg12_lt
          #                   mu                     ele       
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            # SnglEle
            TrgEmulator[1] = eff_sgl_2  > ROOT.gRandom.Rndm()
            # SnglMu
            TrgEmulator[2] = eff_sgl_1  > ROOT.gRandom.Rndm()
            # EleMu 
            Leg1_tl  = eff_dbl_1_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_tl  = eff_dbl_2_trailingleg > ROOT.gRandom.Rndm()
            Leg12_tl = Leg1_tl and Leg2_tl
            Leg1_lt  = eff_dbl_2_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_lt  = eff_dbl_1_trailingleg > ROOT.gRandom.Rndm()
            Leg12_lt = Leg1_lt and Leg2_lt
            TrgEmulator[5] = Leg12_tl or Leg12_lt
          #                   ele                    mu        
          if abs(kindLep1) == 11 and abs(kindLep2) == 13 :
            # SnglEle
            TrgEmulator[1] = eff_sgl_1  > ROOT.gRandom.Rndm()
            # SnglMu
            TrgEmulator[2] = eff_sgl_2  > ROOT.gRandom.Rndm()
            # EleMu 
            Leg1_tl  = eff_dbl_1_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_tl  = eff_dbl_2_trailingleg > ROOT.gRandom.Rndm()
            Leg12_tl = Leg1_tl and Leg2_tl
            Leg1_lt  = eff_dbl_2_leadingleg  > ROOT.gRandom.Rndm()
            Leg2_lt  = eff_dbl_1_trailingleg > ROOT.gRandom.Rndm()
            Leg12_lt = Leg1_lt and Leg2_lt
            TrgEmulator[5] = Leg12_tl or Leg12_lt

          # ...And the grand combo:
          TrgEmulator[0] = TrgEmulator[1] or TrgEmulator[2] or TrgEmulator[3] or TrgEmulator[4] or TrgEmulator[5]

          # up variation ...

          eff_dbl_1_leadingleg  = high_eff_dbl_1_leadingleg
          eff_dbl_2_leadingleg  = high_eff_dbl_2_leadingleg
          eff_dbl_1_trailingleg = high_eff_dbl_1_trailingleg
          eff_dbl_2_trailingleg = high_eff_dbl_2_trailingleg
          eff_sgl_1             = high_eff_sgl_1
          eff_sgl_2             = high_eff_sgl_2

          eff_double_up = (eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg)


          evt_eff_error_up =   (eff_double + eff_sgl_1 * (1. - eff_dbl_2_trailingleg) + eff_sgl_2*(1. - eff_dbl_1_trailingleg))*    \
                                          dz_eff

          # and low variation ...
          eff_dbl_1_leadingleg  = low_eff_dbl_1_leadingleg
          eff_dbl_2_leadingleg  = low_eff_dbl_2_leadingleg
          eff_dbl_1_trailingleg = low_eff_dbl_1_trailingleg
          eff_dbl_2_trailingleg = low_eff_dbl_2_trailingleg
          eff_sgl_1             = low_eff_sgl_1
          eff_sgl_2             = low_eff_sgl_2

          eff_double_low = (eff_dbl_1_trailingleg*eff_dbl_2_leadingleg + eff_dbl_1_leadingleg*eff_dbl_2_trailingleg - eff_dbl_2_leadingleg*eff_dbl_1_leadingleg)


          evt_eff_error_low =   (eff_double + eff_sgl_1 * (1. - eff_dbl_2_trailingleg) + eff_sgl_2*(1. - eff_dbl_1_trailingleg))*    \
                               dz_eff

          return evt_eff, evt_eff_error_low, evt_eff_error_up ,  evt_eff_snglEle , evt_eff_snglMu , evt_eff_dbleEle , evt_eff_dbleMu , evt_eff_EleMu , TrgEmulator
        else :
          # if for any reason it is not a lepton ... 
          TrgEmulator = [ False , False , False , False , False , False ]
          return 1, 1, 1 , 1 , 1 , 1 , 1 , 1 , TrgEmulator


    def _get1lWeight (self, kindLep1, pt1, eta1):
        # Check that it is a lepton
        if kindLep1 > -20:
          vpt1 = [pt1]
          veta1 = [eta1]
          self._fixOverflowUnderflow (kindLep1, vpt1, veta1)
          pt1 = vpt1[0]
          eta1 = veta1[0]

          singleLeg = "-"

          #                  ele                     
          if abs(kindLep1) == 11 :
            singleLeg  = "triggerSingleEle"
          #                   mu                                 
          if abs(kindLep1) == 13:
            singleLeg  = "triggerSingleMu"

          # Get Leg Efficiencies
          eff_sgl_1, low_eff_sgl_1, high_eff_sgl_1 = self._getEff (pt1, eta1, singleLeg)

          # N.B: No reference for (Add 5% syst to SnglEle)
          # so skipping it!
          # if singleLeg == "triggerSingleEle" :
          #   systdown       = eff_sgl_1 - low_eff_sgl_1
          #   systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05) 
          #   low_eff_sgl_1  = max(0.,eff_sgl_1 - systdown_new)
          #   systup         = high_eff_sgl_1 - eff_sgl_1
          #   systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
          #   high_eff_sgl_1 = min(1.,eff_sgl_1+systup_new)

          # Tracker Muon SF
          if abs(kindLep1) == 13 :
             eff_sgl_1       *=  self.trkSFMu[0] 
             high_eff_sgl_1  *=  self.trkSFMu[1]
             low_eff_sgl_1   *=  self.trkSFMu[2]

          # Event Efficiency
          evt_eff = eff_sgl_1
                   
          # And the Trigger Emulation
          # 0: Combo / 1:SnglEle / 2: SnglMu / 3:DbleEle / 4:DbleMu / 5: EleMu

          TrgEmulator = [ False , False , False , False , False , False ]

          #                   ele      
          # Toss a coin for Trigger decision
          Leg1 = eff_sgl_1  > ROOT.gRandom.Rndm() 
          #                   mu  
          if abs(kindLep1) == 11 :
            # SnglEle          
            TrgEmulator[1] = Leg1 
            evt_eff_snglEle = evt_eff
            evt_eff_snglMu = 0.
          if abs(kindLep1) == 13 :
            # SnglMu 
            TrgEmulator[2] = Leg1
            evt_eff_snglEle = 0.
            evt_eff_snglMu = evt_eff

          # ...And the grand combo:
          TrgEmulator[0] = TrgEmulator[1] or TrgEmulator[2] or TrgEmulator[3] or TrgEmulator[4] or TrgEmulator[5]

          # up variation ...
          evt_eff_error_up      = high_eff_sgl_1
          # and low variation ...
          evt_eff_error_low     = low_eff_sgl_1

          return evt_eff, evt_eff_error_low, evt_eff_error_up , evt_eff_snglEle , evt_eff_snglMu ,TrgEmulator
        else :
          # if for any reason it is not a lepton ... 
          TrgEmulator = [ False , False , False , False , False , False ]
          return 1, 1, 1 , 1 , 1 , TrgEmulator

    def _get3lWeight(self, kindLep1, pt1, eta1, kindLep2, pt2, eta2, kindLep3, pt3, eta3):

        # only if leptons!
        if kindLep1 > -20 and kindLep2 > -20 and kindLep3 > -20 :
         
          vpt1 = [pt1]
          vpt2 = [pt2]
          vpt3 = [pt3]
          veta1 = [eta1]
          veta2 = [eta2]
          veta3 = [eta3]
          
          self._fixOverflowUnderflow(kindLep1, vpt1, veta1)
          self._fixOverflowUnderflow(kindLep2, vpt2, veta2)
          self._fixOverflowUnderflow(kindLep3, vpt3, veta3)
          
          pt1 = vpt1[0]
          pt2 = vpt2[0]
          pt3 = vpt3[0]
          eta1 = veta1[0]
          eta2 = veta2[0]
          eta3 = veta3[0]
          
          dz_eff_12 = 1.00
          dz_eff_13 = 1.00
          dz_eff_23 = 1.00

          single1 = "triggerSingleMu"
          single2 = "triggerSingleMu"
          single3 = "triggerSingleMu"

          if abs(kindLep1) == 11 : single1 = "triggerSingleEle"
          if abs(kindLep2) == 11 : single2 = "triggerSingleEle"
          if abs(kindLep3) == 11 : single3 = "triggerSingleEle"
  
          lead1trail2 = "-"
          lead1trail3 = "-"
          lead2trail1 = "-"
          lead2trail3 = "-"
          lead3trail1 = "-"
          lead3trail2 = "-"

          trail1lead2 = "-"
          trail1lead3 = "-"
          trail2lead1 = "-"
          trail2lead3 = "-"
          trail3lead1 = "-"
          trail3lead2 = "-"

          # ee ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          if abs(kindLep1) == 11 and abs(kindLep2) == 11 :
              lead1trail2 = "triggerDoubleEleLegHigPt"
              lead2trail1 = "triggerDoubleEleLegHigPt"
              trail1lead2 = "triggerDoubleEleLegLowPt"
              trail2lead1 = "triggerDoubleEleLegLowPt"
              dz_eff_12 = self.DZEff_DoubleEle
              
          if abs(kindLep1) == 11 and abs(kindLep3) == 11 :
              lead1trail3 = "triggerDoubleEleLegHigPt"
              lead3trail1 = "triggerDoubleEleLegHigPt"
              trail1lead3 = "triggerDoubleEleLegLowPt"
              trail3lead1 = "triggerDoubleEleLegLowPt"
              dz_eff_13 = self.DZEff_DoubleEle

          if abs(kindLep2) == 11 and abs(kindLep3) == 11 :
              lead2trail3 = "triggerDoubleEleLegHigPt"
              lead3trail2 = "triggerDoubleEleLegHigPt"
              trail2lead3 = "triggerDoubleEleLegLowPt"
              trail3lead2 = "triggerDoubleEleLegLowPt"
              dz_eff_23 = self.DZEff_DoubleEle

          # mm ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          if abs(kindLep1) == 13 and abs(kindLep2) == 13 :
            lead1trail2 = "triggerDoubleMuLegHigPt"
            lead2trail1 = "triggerDoubleMuLegHigPt"
            trail1lead2 = "triggerDoubleMuLegLowPt"
            trail2lead1 = "triggerDoubleMuLegLowPt"
            dz_eff_12 = self.DZEff_DoubleMu
            
          if abs(kindLep1) == 13 and abs(kindLep3) == 13 :
            lead1trail3 = "triggerDoubleMuLegHigPt"
            lead3trail1 = "triggerDoubleMuLegHigPt"
            trail1lead3 = "triggerDoubleMuLegLowPt"
            trail3lead1 = "triggerDoubleMuLegLowPt"
            dz_eff_13 = self.DZEff_DoubleMu

          if abs(kindLep2) == 13 and abs(kindLep3) == 13 :
            lead2trail3 = "triggerDoubleMuLegHigPt"
            lead3trail2 = "triggerDoubleMuLegHigPt"
            trail2lead3 = "triggerDoubleMuLegLowPt"
            trail3lead2 = "triggerDoubleMuLegLowPt"
            dz_eff_23 = self.DZEff_DoubleMu
            
          # em ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          if abs(kindLep1) == 13 and abs(kindLep2) == 11 :
            lead1trail2 = "triggerMuEleLegHigPt"
            lead2trail1 = "triggerEleMuLegHigPt"
            trail1lead2 = "triggerEleMuLegLowPt"
            trail2lead1 = "triggerMuEleLegLowPt"
            dz_eff_12 = self.DZEff_MuEle           
 
          if abs(kindLep1) == 13 and abs(kindLep3) == 11 :
            lead1trail3 = "triggerMuEleLegHigPt"
            lead3trail1 = "triggerEleMuLegHigPt"
            trail1lead3 = "triggerEleMuLegLowPt"
            trail3lead1 = "triggerMuEleLegLowPt"
            dz_eff_13 = self.DZEff_MuEle           

          if abs(kindLep2) == 13 and abs(kindLep1) == 11 :
            lead2trail1 = "triggerMuEleLegHigPt"
            lead1trail2 = "triggerEleMuLegHigPt"
            trail2lead1 = "triggerEleMuLegLowPt"
            trail1lead2 = "triggerMuEleLegLowPt"
            dz_eff_12 = self.DZEff_EleMu

          if abs(kindLep2) == 13 and abs(kindLep3) == 11 :
            lead2trail3 = "triggerMuEleLegHigPt"
            lead3trail2 = "triggerEleMuLegHigPt"
            trail2lead3 = "triggerEleMuLegLowPt"
            trail3lead2 = "triggerMuEleLegLowPt"
            dz_eff_23 = self.DZEff_MuEle           

          if abs(kindLep3) == 13 and abs(kindLep1) == 11 :
            lead3trail1 = "triggerMuEleLegHigPt"
            lead1trail3 = "triggerEleMuLegHigPt"
            trail3lead1 = "triggerEleMuLegLowPt"
            trail1lead3 = "triggerMuEleLegLowPt"
            dz_eff_13 = self.DZEff_EleMu

          if abs(kindLep3) == 13 and abs(kindLep2) == 11 :
            lead3trail2 = "triggerMuEleLegHigPt"
            lead2trail3 = "triggerEleMuLegHigPt"
            trail3lead2 = "triggerEleMuLegLowPt"
            trail2lead3 = "triggerMuEleLegLowPt"
            dz_eff_23 = self.DZEff_EleMu
          
          
          l1t2, low_l1t2, high_l1t2 = self._getEff(pt1, eta1, lead1trail2)
          l1t3, low_l1t3, high_l1t3 = self._getEff(pt1, eta1, lead1trail3)
          l2t1, low_l2t1, high_l2t1 = self._getEff(pt2, eta2, lead2trail1)
          l2t3, low_l2t3, high_l2t3 = self._getEff(pt2, eta2, lead2trail3)
          l3t1, low_l3t1, high_l3t1 = self._getEff(pt3, eta3, lead3trail1)
          l3t2, low_l3t2, high_l3t2 = self._getEff(pt3, eta3, lead3trail2)

          t1l2, low_t1l2, high_t1l2 = self._getEff(pt1, eta1, trail1lead2)
          t1l3, low_t1l3, high_t1l3 = self._getEff(pt1, eta1, trail1lead3)
          t2l1, low_t2l1, high_t2l1 = self._getEff(pt2, eta2, trail2lead1)
          t2l3, low_t2l3, high_t2l3 = self._getEff(pt2, eta2, trail2lead3)
          t3l1, low_t3l1, high_t3l1 = self._getEff(pt3, eta3, trail3lead1)
          t3l2, low_t3l2, high_t3l2 = self._getEff(pt3, eta3, trail3lead2)
          s1  , low_s1  , high_s1   = self._getEff(pt1, eta1, single1)
          s2  , low_s2  , high_s2   = self._getEff(pt2, eta2, single2)
          s3  , low_s3  , high_s3   = self._getEff(pt3, eta3, single3)

          # Add 5% syst to SnglEle
          if single1 == "triggerSingleEle" :
            systdown       = s1 - low_s1
            systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05)
            low_s1         = max(0.,s1 - systdown_new)
            systup         = high_s1 - s1
            systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
            high_s1        = min(1.,s1+systup_new)
          if single2 == "triggerSingleEle" :
            systdown       = s2 - low_s2
            systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05)
            low_s2         = max(0.,s2 - systdown_new)
            systup         = high_s2 - s2
            systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
            high_s2        = min(1.,s2+systup_new)
          if single3 == "triggerSingleEle" :
            systdown       = s3 - low_s3
            systdown_new   = math.sqrt(systdown*systdown + 0.05*0.05)
            low_s3         = max(0.,s3 - systdown_new)
            systup         = high_s3 - s3
            systup_new     = math.sqrt(systup*systup + 0.05*0.05) 
            high_s3        = min(1.,s3+systup_new)


          # Tracker Muon SF

          if abs(kindLep1) == 13 :

             s1        *= self.trkSFMu[0]
             high_s1   *= self.trkSFMu[1]
             low_s1    *= self.trkSFMu[2]

             l1t2      *= self.trkSFMu[0]
             high_l1t2 *= self.trkSFMu[1]
             low_l1t2  *= self.trkSFMu[2]

             l1t3      *= self.trkSFMu[0]
             high_l1t3 *= self.trkSFMu[1]
             low_l1t3  *= self.trkSFMu[2]

             t1l2      *= self.trkSFMu[0]
             high_t1l2 *= self.trkSFMu[1]
             low_t1l2  *= self.trkSFMu[2]

             t1l3      *= self.trkSFMu[0]
             high_t1l3 *= self.trkSFMu[1]
             low_t1l3  *= self.trkSFMu[2]

          if abs(kindLep2) == 13 :

             s2       *=  self.trkSFMu[0]
             high_s2  *=  self.trkSFMu[1]
             low_s2   *=  self.trkSFMu[2]

             l2t1      *= self.trkSFMu[0]
             high_l2t1 *= self.trkSFMu[1]
             low_l2t1  *= self.trkSFMu[2]

             l2t3      *= self.trkSFMu[0]
             high_l2t3 *= self.trkSFMu[1]
             low_l2t3  *= self.trkSFMu[2]

             t2l1      *= self.trkSFMu[0]
             high_t2l1 *= self.trkSFMu[1]
             low_t2l1  *= self.trkSFMu[2]

             t2l3      *= self.trkSFMu[0]
             high_t2l3 *= self.trkSFMu[1]
             low_t2l3  *= self.trkSFMu[2]


          if abs(kindLep3) == 13 :

             s3       *=  self.trkSFMu[0]
             high_s3  *=  self.trkSFMu[1]
             low_s3   *=  self.trkSFMu[2]

             l3t1      *= self.trkSFMu[0]
             high_l3t1 *= self.trkSFMu[1]
             low_l3t1  *= self.trkSFMu[2]

             l3t2      *= self.trkSFMu[0]
             high_l3t2 *= self.trkSFMu[1]
             low_l3t2  *= self.trkSFMu[2]

             t3l1      *= self.trkSFMu[0]
             high_t3l1 *= self.trkSFMu[1]
             low_t3l1  *= self.trkSFMu[2]

             t3l2      *= self.trkSFMu[0]
             high_t3l2 *= self.trkSFMu[1]
             low_t3l2  *= self.trkSFMu[2]


          ### SINGLE TRIGGERS ARE NOT YET INCLUDED ###
          ### XJ (6th July 2016: Putting single back)

          # Nominal values
          eff_sng= s1 + (1-s1)*s2 + (1-s1-(1-s1)*s2)*s3  
          eff12 = (l1t2*t2l1 + (1 - l1t2*t2l1) * l2t1*t1l2) * dz_eff_12
          eff13 = (l1t3*t3l1 + (1 - l1t3*t3l1) * l3t1*t1l3) * dz_eff_13
          eff23 = (l2t3*t3l2 + (1 - l2t3*t3l2) * l3t2*t2l3) * dz_eff_23
          eff_dbl = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23

          # XJ: That was double only 
          #evt_eff = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23
          evt_eff = eff_dbl + (1-eff_dbl) * eff_sng

          # Low values
          eff_sng= low_s1 + (1-low_s1)*low_s2 + (1-low_s1-(1-low_s1)*low_s2)*low_s3
          eff12 = (low_l1t2*low_t2l1 + (1 - low_l1t2*low_t2l1) * low_l2t1*low_t1l2) * dz_eff_12
          eff13 = (low_l1t3*low_t3l1 + (1 - low_l1t3*low_t3l1) * low_l3t1*low_t1l3) * dz_eff_13
          eff23 = (low_l2t3*low_t3l2 + (1 - low_l2t3*low_t3l2) * low_l3t2*low_t2l3) * dz_eff_23
          eff_dbl = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23

          #evt_eff_low = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23
          evt_eff_low = eff_dbl + (1-eff_dbl) * eff_sng

          # High values
          eff_sng= high_s1 + (1-high_s1)*high_s2 + (1-high_s1-(1-high_s1)*high_s2)*high_s3
          eff12 = (high_l1t2*high_t2l1 + (1 - high_l1t2*high_t2l1) * high_l2t1*high_t1l2) * dz_eff_12
          eff13 = (high_l1t3*high_t3l1 + (1 - high_l1t3*high_t3l1) * high_l3t1*high_t1l3) * dz_eff_13
          eff23 = (high_l2t3*high_t3l2 + (1 - high_l2t3*high_t3l2) * high_l3t2*high_t2l3) * dz_eff_23
          eff_dbl = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23

          #evt_eff_high = eff12 + (1 - eff12)*eff13 + (1 - eff12)*(1 - eff13)*eff23
          evt_eff_high = eff_dbl + (1-eff_dbl) * eff_sng
          
          return evt_eff, evt_eff_low, evt_eff_high 

        else : 

          return 1, 1, 1 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _getNlWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _getNlWeight(self, nLep):
        if nLep == 2:
            return _getWeight
        def _curriedWeight(*args):
            if len(args)%3 != 0:
                print "ERROR!! For each leg, 'kindLep pt eta' should be provides. Bad number of arguments."
                return 1, 1, 1
            toss_a_coin = ROOT.gRandom.Rndm()

            # Start from here!
            kindLep = [ args[i*3+0] for i in range(nLep) ]
            pt      = [ args[i*3+1] for i in range(nLep) ]
            eta     = [ args[i*3+2] for i in range(nLep) ]

            if  any([ p < -20 for p in kindLep ]):
                return 1,1,1

            for iLep in range(nLep):
                pt[iLep], eta[iLep] = self._fixOverflowUnderflow(kindLep[iLep],pt[iLep:iLep+1],eta[iLep:iLep+1])

            dz_eff_ee = self.DZEff_DoubleEle    # 0.995 
            dz_eff_em = self.DZEff_EleMu        # 1.00
            dz_eff_me = self.DZEff_MuEle        # 1.00
            dz_eff_mm = self.DZEff_DoubleMu     # 0.95

            # Find all possible leg combinations
            single = {}
            for iLep in range(nLep):
                keyname = 'single{0}'.format(iLep)
                single[keyname] = {}
                single[keyname]['whichTrigger'] = "triggerSingleMu" if abs(kindLep[iLep]) == 13 else "triggerSingleEle"
                single[keyname]['pt']           = pt [iLep]
                single[keyname]['eta']          = eta[iLep]

            double = {}
            for iLep in range(nLep):
                for jLep in range(iLep+1,nLep):
                    if abs(kindLep[iLep]) == abs(kindLep[jLep]):
                        flavorKey1 = "DoubleEle" if abs(kindLep[iLep]) == 11 else "DoubleMu"
                        flavorKey2 = ""
                        dz_eff    = dz_eff_ee if abs(kindLep[iLep]) == 11 else dz_eff_mm
                        specialKey = ""
                    else:
                        if abs(kindLep[iLep]) ==13:
                            flavorKey1 = "Mu"
                            flavorKey2 = "Ele"
                            dz_eff = dz_eff_me
                        else :
                            flavorKey1 = "Ele"
                            flavorKey2 = "Mu"
                            dz_eff = dz_eff_em
                        specialKey = ""
                    keyname = 'lead{0}trail{1}'.format(iLep,jLep)
                    double[keyname]={}
                    double[keyname]['whichTrigger'] = 'trigger{0}{1}{2}LegHigPt'.format(specialKey,flavorKey1,flavorKey2)
                    double[keyname]['pt']           = pt [iLep]
                    double[keyname]['eta']          = eta[iLep]
                    double[keyname]['dz_eff']       = dz_eff
                    keyname = 'lead{1}trail{0}'.format(iLep,jLep)
                    double[keyname]={}
                    double[keyname]['whichTrigger'] = 'trigger{0}{2}{1}LegHigPt'.format(specialKey,flavorKey1,flavorKey2)
                    double[keyname]['pt']           = pt [jLep]
                    double[keyname]['eta']          = eta[jLep]
                    double[keyname]['dz_eff']       = dz_eff
                    keyname = 'trail{0}lead{1}'.format(iLep,jLep)
                    double[keyname]={}
                    double[keyname]['whichTrigger'] = 'trigger{0}{2}{1}LegLowPt'.format(specialKey,flavorKey1,flavorKey2)
                    double[keyname]['pt']           = pt [iLep]
                    double[keyname]['eta']          = eta[iLep]
                    double[keyname]['dz_eff']       = dz_eff
                    keyname = 'trail{1}lead{0}'.format(iLep,jLep)
                    double[keyname]={}
                    double[keyname]['whichTrigger'] = 'trigger{0}{1}{2}LegLowPt'.format(specialKey,flavorKey1,flavorKey2)
                    double[keyname]['pt']           = pt [jLep]
                    double[keyname]['eta']          = eta[jLep]
                    double[keyname]['dz_eff']       = dz_eff

            # Fill efficiency for all possible legs.
            getEff = {}
            for keyname in double.keys():
                getEff[keyname] = {}
                getEff[keyname]['eff'], getEff[keyname]['eff_low'], getEff[keyname]['eff_high'] = self._getEff(double[keyname]['pt'],double[keyname]['eta'],double[keyname]['whichTrigger'])
            for keyname in single.keys():
                getEff[keyname] = {}
                getEff[keyname]['eff'], getEff[keyname]['eff_low'], getEff[keyname]['eff_high'] = self._getEff(single[keyname]['pt'],single[keyname]['eta'],single[keyname]['whichTrigger'])

            # Add 5% syst to SnglEle
            for keyname in single.keys():
                if single[keyname]['whichTrigger'] == "triggerSingleEle":
                    systdown = getEff[keyname]['eff']-getEff[keyname]['eff_low']
                    systdown_new = math.sqrt(systdown*systdown + 0.05*0.05)
                    getEff[keyname]['eff_low'] = max(0.,getEff[keyname]['eff']-systdown_new)
                    systhigh = getEff[keyname]['eff_high']-getEff[keyname]['eff']
                    systhigh_new = math.sqrt(systhigh*systhigh + 0.05*0.05)
                    getEff[keyname]['eff_high'] = min(1.,getEff[keyname]['eff']+systhigh_new)

            # Tracker Muon SF
            for iLep in range(nLep):
                if abs(kindLep[iLep])==13:
                    for keyname in double.keys():
                        if re.search("^(lead|trail)([0-9]+)(lead|trail)([0-9]+)$",keyname).group(2) == str(iLep):
                            getEff[keyname]['eff']      *= self.trkSFMu[0]
                            getEff[keyname]['eff_high'] *= self.trkSFMu[1]
                            getEff[keyname]['eff_low']  *= self.trkSFMu[2]
                    for keyname in single.keys():
                        if re.search("^single([0-9]+)$",keyname).group(1) == str(iLep):
                            getEff[keyname]['eff']      *= self.trkSFMu[0]
                            getEff[keyname]['eff_high'] *= self.trkSFMu[1]
                            getEff[keyname]['eff_low']  *= self.trkSFMu[2]

            def eff_sng_dbl(errEff):
                eff_dbl_inv = 1
                eff_sng_inv = 1
                eff  =  {}
                for iLep in range(nLep):
                    for jLep in range(iLep+1,nLep):
                        eff['eff'+str(iLep)+str(jLep)] = {}
                        eff['eff'+str(iLep)+str(jLep)][errEff] = ( getEff['lead'+str(iLep)+'trail'+str(jLep)][errEff]*getEff['trail'+str(jLep)+'lead'+str(iLep)][errEff] \
                                                               + ( 1 - getEff['lead'+str(iLep)+'trail'+str(jLep)][errEff]*getEff['trail'+str(jLep)+'lead'+str(iLep)][errEff]) \
                                                               * getEff['lead'+str(jLep)+'trail'+str(iLep)][errEff]*getEff['trail'+str(iLep)+'lead'+str(jLep)][errEff]) \
                                                               * double['trail'+str(iLep)+'lead'+str(jLep)]['dz_eff']
                        eff_dbl_inv = eff_dbl_inv * (1-eff['eff'+str(iLep)+str(jLep)][errEff])
                for iLep in range(nLep):
                    eff_sng_inv = eff_sng_inv * (1-getEff['single'+str(iLep)][errEff])
                return 1. - (eff_dbl_inv)*(eff_sng_inv)

            

            return eff_sng_dbl('eff'), eff_sng_dbl('eff_low'), eff_sng_dbl('eff_high')

        return _curriedWeight

    def _getTrigDecision(self,vector_trigger,isData):

        EleMu     = 0
        DoubleMu  = 0
        SingleMu  = 0
        DoubleEle = 0
        SingleEle = 0


        if isData :
          for iTrig in self.EleMu      : 
            if vector_trigger[iTrig] > 0 : EleMu      = 1
          for iTrig in self.DoubleMu   : 
            if vector_trigger[iTrig] > 0 : DoubleMu   = 1
          for iTrig in self.SingleMu   : 
            if vector_trigger[iTrig] > 0 : SingleMu   = 1
          for iTrig in self.DoubleEle  : 
            if vector_trigger[iTrig] > 0 : DoubleEle  = 1
          for iTrig in self.SingleEle  : 
            if vector_trigger[iTrig] > 0 : SingleEle  = 1

        return EleMu , DoubleMu , SingleMu , DoubleEle , SingleEle
 

    def _dPhi(self,phi1,phi2):
       PI=3.14159265359
       dphi=abs(phi1-phi2)*180./PI
       if dphi>180 : dphi=360-dphi
       return dphi

    def _phiCSC(self,pt,eta,phi,charge):
    # Approxiamtion from <andrewbrink@gmail.com> valid for pT>10 GeV
    # L1T phi = GEN phi + (GEN charge) x (1/GEN pT) x [10.48 - 5.1412 x GEN theta + 0.02308 x (GEN theta)^2]
        theta = 2. * math.atan ( math.exp(-1.*eta) )
        phiCSC = phi + charge * (1./pt) * ( 10.48 - 5.1412 * theta + 0.02308 * theta * theta ) 
        return phiCSC
 
    def _getEMTFBugVeto(self,vector_kind,vector_pt,vector_eta,vector_phi):

        if self.EMTFBug:
          vPhi = []
          vEta = []
          for iLep in range(0,len(vector_kind)):
            if abs(vector_kind[iLep]) == 13 and vector_pt[iLep] >= 10. and abs(vector_eta[iLep]) >= 1.24 :
              #print "Fill", iLep, vector_kind[iLep] , vector_eta[iLep]
              vEta.append(vector_eta[iLep])
              ch = 0.0 
              if    vector_kind[iLep] == 13 : ch =  1.0
              else :                          ch = -1.0
              phiCSC = self._phiCSC(vector_pt[iLep],vector_eta[iLep],vector_phi[iLep],ch)
              vPhi.append(vector_phi[iLep])
          if len(vPhi) >= 2 :
            for iLep1 in range(0,len(vPhi)):
              #print "A ",iLep1 , vEta[iLep1] , vPhi[iLep1]
              for iLep2 in range(0,len(vPhi)):
                if not iLep1 == iLep2 and vEta[iLep1]*vEta[iLep2] > 0 :
                  #print "B ", iLep2 , vEta[iLep2] , vPhi[iLep2]
                  #print self._dPhi(vPhi[iLep1],vPhi[iLep2])
                  if self._dPhi(vPhi[iLep1],vPhi[iLep2]) < 80. : return 0.
        return 1.

class triggerMaker(TreeCloner):

    def __init__(self):
        self.isData=False
        self.runPeriod=-1
        self.nPeriods=0
        self.fPeriods = []

    def help(self):
        return '''Add trigger efficiency weight. The source files must be passed as an option'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)

        group.add_option('-c', '--cmssw' , dest='cmssw'   , help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-p', '--pycfg' , dest='pycfg'   , help='Python Config describing the trigger' , default='DEFAULT' , type='string')
        group.add_option('-d', '--isdata', dest='isData'  , help='False=MC / True=Data' , default=False  , action="store_true")
        group.add_option('-k', '--keeprun', dest='keepRun', help='False=Redo run period / True=Keep run period' , default=False  , action="store_true")

        parser.add_option_group(group)
        return group 

    def checkOptions(self,opts):
 
        self.isData=opts.isData
        cmssw_base = os.getenv('CMSSW_BASE')
        
        # Define Luminosity and run periods              
        if opts.pycfg == "DEFAULT" : opts.pycfg = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/trigger/Trigger_cfg.py'
        print 'Loading Trigger config : ' , opts.pycfg
        Trigger = {}
        if os.path.exists(opts.pycfg) : 
          handle = open(opts.pycfg,'r')
          exec(handle)
          handle.close()
        # Remap 2015
        if '74' in opts.cmssw : opts.cmssw = 'Full2015' 
        if '76' in opts.cmssw : opts.cmssw = 'Full2015' 
    
        # Compute Lumi fractions
        self.keepRun  = opts.keepRun 
        self.nPeriods = len(Trigger.keys())
        LumiTot=0.
        for iPeriod in Trigger[opts.cmssw] : LumiTot += Trigger[opts.cmssw][iPeriod]['lumi']
        fSum = 0.
        self.fPeriods.append(fSum) 
        self.runPeriods = {}
        for iPeriod in Trigger[opts.cmssw] : 
           self.runPeriods[iPeriod] = {} 
           self.runPeriods[iPeriod]['begin'] = Trigger[opts.cmssw][iPeriod]['begin']
           self.runPeriods[iPeriod]['end']   = Trigger[opts.cmssw][iPeriod]['end']
           self.runPeriods[iPeriod]['lumi']  = Trigger[opts.cmssw][iPeriod]['lumi']
           fSum += Trigger[opts.cmssw][iPeriod]['lumi']/LumiTot
           self.fPeriods.append(fSum)
        
        print '------- Cfg for : ', opts.cmssw
        print Trigger[opts.cmssw]
        print '--------Lumi Frac -----------' 
        print 'Keep Run Period: ',self.keepRun
        print self.runPeriods
        print self.fPeriods
        print '---------------------' 
        self.triggerCalculators = []
        for iPeriod in Trigger[opts.cmssw] : self.triggerCalculators.append(triggerCalculator(Trigger,opts.cmssw,iPeriod,self.isData))

    def _getRunPeriod(self,run): 
        
        if     self.isData : 
          for iPeriod in self.runPeriods:
            if run >= self.runPeriods[iPeriod]['begin'] and run <= self.runPeriods[iPeriod]['end'] : return iPeriod
        else:  
          toss_a_coin = ROOT.gRandom.Rndm()
          for iPeriod in range(1,len(self.fPeriods)) : 
            if toss_a_coin >= self.fPeriods[iPeriod-1] and toss_a_coin < self.fPeriods[iPeriod] : return iPeriod
            if toss_a_coin == 1.0 : return len(self.fPeriods)-1
        return -1
       

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        if self.isData :
          self.namesBranches = [
           'veto_EMTFBug',
           'trig_SnglEle',
           'trig_SnglMu',
           'trig_DbleEle',
           'trig_DbleMu',
           'trig_EleMu',
          ]
          self.namesOldBranchesToBeModifiedVector = []

        else: 

          self.namesBranches = [
           'veto_EMTFBug',
           'effTrigW',
           'effTrigW_Up',
           'effTrigW_Down',
           'effTrigW1l',
           'effTrigW1l_Up',
           'effTrigW1l_Down',
           'effTrigW3l',
           'effTrigW3l_Up',
           'effTrigW3l_Down',
           'effTrigW4l',
           'effTrigW4l_Up',
           'effTrigW4l_Down',
           'effTrigW_SnglEle',
           'effTrigW_SnglMu',
           'effTrigW_DbleEle',
           'effTrigW_DbleMu',
           'effTrigW_EleMu',
           'effTrigW1l_SnglEle',
           'effTrigW1l_SnglMu',
          ]
          self.namesOldBranchesToBeModifiedVector = [
           'std_vector_TrgEmulator'
          ]

        if not self.keepRun : self.namesBranches.append('iRunPeriod')

        # clone the tree
        self.clone(output, self.namesBranches + self.namesOldBranchesToBeModifiedVector)

        self.branches = {}
        for bname in self.namesBranches:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.branches[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.branches.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        if not self.isData :
          bvector_TrgEmulator =  ROOT.std.vector(bool) ()
          self.otree.Branch('std_vector_TrgEmulator',bvector_TrgEmulator)

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


            # Get run period
            if not self.keepRun :
              self.runPeriod = self._getRunPeriod(itree.run) 
              self.branches['iRunPeriod'][0] = self.runPeriod 
            else:
              self.runPeriod = int(itree.iRunPeriod)

            # Compute the veto for the EMTF Bug in 2016
            vEMTF = self.triggerCalculators[self.runPeriod-1]._getEMTFBugVeto(itree.std_vector_lepton_flavour,itree.std_vector_lepton_pt,itree.std_vector_lepton_eta,itree.std_vector_lepton_phi)
            self.branches['veto_EMTFBug'] [0] = vEMTF
            #print vEMTF

            # DATA = compute trigger "bits" oer dataset 
            if self.isData :

              self.branches['trig_EleMu']         [0] , \
              self.branches['trig_DbleMu']        [0] , \
              self.branches['trig_SnglMu']        [0] , \
              self.branches['trig_DbleEle']       [0] , \
              self.branches['trig_SnglEle']       [0] = \
              self.triggerCalculators[self.runPeriod-1]._getTrigDecision(itree.std_vector_trigger,self.isData)

            # MC = compute efficiencies
            else: 

              self.branches['effTrigW']       [0] = 1.0
              self.branches['effTrigW_Up']    [0] = 1.0
              self.branches['effTrigW_Down']  [0] = 1.0
              self.branches['effTrigW1l']     [0] = 1.0
              self.branches['effTrigW1l_Up']  [0] = 1.0
              self.branches['effTrigW1l_Down'][0] = 1.0
              self.branches['effTrigW3l']     [0] = 1.0
              self.branches['effTrigW3l_Up']  [0] = 1.0
              self.branches['effTrigW3l_Down'][0] = 1.0
              self.branches['effTrigW4l']     [0] = 1.0
              self.branches['effTrigW4l_Up']  [0] = 1.0
              self.branches['effTrigW4l_Down'][0] = 1.0
              self.branches['effTrigW_SnglEle'][0] = 1.0
              self.branches['effTrigW_SnglMu'][0] = 1.0
              self.branches['effTrigW_DbleEle'][0] = 1.0
              self.branches['effTrigW_DbleMu'][0] = 1.0
              self.branches['effTrigW_EleMu'][0] = 1.0
              self.branches['effTrigW1l_SnglEle'][0] = 1.0
              self.branches['effTrigW1l_SnglMu'][0] = 1.0
  
              bvector_TrgEmulator.clear()
  
              #evt_eff_dbleEle , evt_eff_dble_Mu , evt_eff_EleMu , TrgEmulator
                 
              # ONLY 1 lepton trigger weight (exclusive) 
              if itree.std_vector_lepton_flavour.size() == 1 or  \
                        (itree.std_vector_lepton_flavour.size()>=2 and itree.std_vector_lepton_flavour[0] > -20 and \
                        itree.std_vector_lepton_flavour[1] < -20):

                self.branches['effTrigW1l'][0], self.branches['effTrigW1l_Down'][0], self.branches['effTrigW1l_Up'][0] , \
                self.branches['effTrigW1l_SnglEle'][0] , self.branches['effTrigW1l_SnglMu'][0] , \
                TrgEmulator = \
                    self.triggerCalculators[self.runPeriod-1]._get1lWeight(itree.std_vector_lepton_flavour[0], itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0])
                for iEmu in TrgEmulator: bvector_TrgEmulator.push_back(iEmu)
                # zeroing all other >1 lepton efficiencies
                self.branches['effTrigW']     [0] = 0.0
                self.branches['effTrigW_Down'][0] = 0.0
                self.branches['effTrigW_Up']  [0] = 0.0
                self.branches['effTrigW_SnglEle'][0] = 0.0
                self.branches['effTrigW_SnglMu'][0] = 0.0
                self.branches['effTrigW_DbleEle'][0] = 0.0
                self.branches['effTrigW_DbleMu'][0] = 0.0
                self.branches['effTrigW_EleMu'][0] = 0.0
                self.branches['effTrigW3l']     [0] = 0.0
                self.branches['effTrigW3l_Down'][0] = 0.0
                self.branches['effTrigW3l_Up']  [0] = 0.0
                self.branches['effTrigW4l']     [0] = 0.0
                self.branches['effTrigW4l_Down'][0] = 0.0
                self.branches['effTrigW4l_Up']  [0] = 0.0
              
              else:
                # > 1 lepton case
                self.branches["effTrigW1l"][0]       = 0.0
                self.branches["effTrigW1l_Down"][0]  = 0.0
                self.branches["effTrigW1l_Up"][0]    = 0.0

                
                # 2-lepton trigger weight
                if itree.std_vector_lepton_flavour.size() >= 2 :
                  self.branches['effTrigW'][0], self.branches['effTrigW_Down'][0], self.branches['effTrigW_Up'][0] , \
                  self.branches['effTrigW_SnglEle'][0] , self.branches['effTrigW_SnglMu'][0] , \
                  self.branches['effTrigW_DbleEle'][0] , self.branches['effTrigW_DbleMu'][0] , self.branches['effTrigW_EleMu'][0] , \
                  TrgEmulator = \
                      self.triggerCalculators[self.runPeriod-1]._getWeight(itree.std_vector_lepton_flavour[0], itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0],
                                      itree.std_vector_lepton_flavour[1], itree.std_vector_lepton_pt[1], itree.std_vector_lepton_eta[1])
                  for iEmu in TrgEmulator: bvector_TrgEmulator.push_back(iEmu)
                else :
                  self.branches['effTrigW']     [0] = 0.0
                  self.branches['effTrigW_Down'][0] = 0.0
                  self.branches['effTrigW_Up']  [0] = 0.0
                  self.branches['effTrigW_SnglEle'][0] = 0.0
                  self.branches['effTrigW_SnglMu'][0] = 0.0
                  self.branches['effTrigW_DbleEle'][0] = 0.0
                  self.branches['effTrigW_DbleMu'][0] = 0.0
                  self.branches['effTrigW_EleMu'][0] = 0.0
                  for x in range(0, 5): bvector_TrgEmulator.push_back(False)
  
                # 3-lepton trigger weight
                if itree.std_vector_lepton_flavour.size() >= 3 :
                    self.branches['effTrigW3l'][0], self.branches['effTrigW3l_Down'][0], self.branches['effTrigW3l_Up'][0] = \
                      self.triggerCalculators[self.runPeriod-1]._get3lWeight(itree.std_vector_lepton_flavour[0], itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0],
                                        itree.std_vector_lepton_flavour[1], itree.std_vector_lepton_pt[1], itree.std_vector_lepton_eta[1],
                                        itree.std_vector_lepton_flavour[2], itree.std_vector_lepton_pt[2], itree.std_vector_lepton_eta[2])
                else :
                  self.branches['effTrigW3l']     [0] = 0.0
                  self.branches['effTrigW3l_Down'][0] = 0.0
                  self.branches['effTrigW3l_Up']  [0] = 0.0
                
                # 4-lepton trigger weight
                if itree.std_vector_lepton_flavour.size() >= 4 :
                    self.branches['effTrigW4l'][0], self.branches['effTrigW4l_Down'][0], self.branches['effTrigW4l_Up'][0] = \
                      self.triggerCalculators[self.runPeriod-1]._getNlWeight(4)(itree.std_vector_lepton_flavour[0], itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0],
                                        itree.std_vector_lepton_flavour[1], itree.std_vector_lepton_pt[1], itree.std_vector_lepton_eta[1],
                                        itree.std_vector_lepton_flavour[2], itree.std_vector_lepton_pt[2], itree.std_vector_lepton_eta[2],
                                        itree.std_vector_lepton_flavour[3], itree.std_vector_lepton_pt[3], itree.std_vector_lepton_eta[3])
                else :
                  self.branches['effTrigW4l']     [0] = 0.0
                  self.branches['effTrigW4l_Down'][0] = 0.0
                  self.branches['effTrigW4l_Up']  [0] = 0.0

            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


