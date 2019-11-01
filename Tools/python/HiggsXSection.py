#!/usr/bin/env python
import sys, re, os, os.path, string
import ROOT
from ROOT import *
from array import array 

class HiggsXSection:

   def file2map(self,x):
        ret = {}; headers = []
        for x in open(x,"r"):
            cols = x.split()
            if len(cols) < 2: continue
            if "mH" in x:
                headers = [i.strip() for i in cols[1:]]
            else:
                fields = [ float(i) for i in cols ]
                ret[fields[0]] = dict(zip(headers,fields[1:]))
        return ret

   def __init__(self):
      self._cmssw=os.environ["CMSSW_BASE"]
      self._basepath=self._cmssw+'/src/LatinoAnalysis/Tools/data/'
      self._YR = {}       
      
      self.readYR('YR2','7TeV')
      self.readYR('YR2','8TeV')

      self.readYR('YR3','7TeV')
      self.readYR('YR3','8TeV')
      
      self.readYR('YR4','13TeV')
      self.readYR('YR4','13TeV','bsm')
      self.readYR('YR4prel','13TeV')
      self.readYR('YR4prel','13TeV','bsm')
      
      self._UseggZH = True

      self._br = {}
      self._br['W2lv'] = 0.108*3.0
      self._br['W2QQ'] = 0.676
      self._br['Z2ll'] = 0.033658*3.0


   def readYR(self,YRversion,energy,model='sm'):
      if not YRversion in ['YR2','YR3','YR4prel','YR4'] : return
      if not energy in ['7TeV','8TeV','13TeV' ] : return
      # Create Structure
      if not YRversion in self._YR : self._YR[YRversion] = {}
      if not model  in self._YR[YRversion] : self._YR[YRversion][model] = {}
      if not 'xs' in self._YR[YRversion][model] : self._YR[YRversion][model]['xs'] = {}
      if not 'br' in self._YR[YRversion][model] : self._YR[YRversion][model]['br'] = {}
     
      # Add x-sections
      # ... SM
      if model == 'sm' : 

        if YRversion in  ['YR2','YR3'] :
          if not energy in ['7TeV','8TeV'] : return  
          if not energy in self._YR[YRversion][model]['xs'] : self._YR[YRversion][model]['xs'][energy] = {}
          self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggH.txt') 
          self._YR[YRversion][model]['xs'][energy]['vbfH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-vbfH.txt') 
          self._YR[YRversion][model]['xs'][energy]['WH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-WH.txt') 
          self._YR[YRversion][model]['xs'][energy]['ZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ZH.txt') 
          self._YR[YRversion][model]['xs'][energy]['ttH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ttH.txt') 
    
        if YRversion in  ['YR4prel','YR4'] :
          if not energy in ['13TeV'] : return  
          if not energy in self._YR[YRversion][model]['xs'] : self._YR[YRversion][model]['xs'][energy] = {}
          self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggH.txt') 
          self._YR[YRversion][model]['xs'][energy]['vbfH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-vbfH.txt') 
          self._YR[YRversion][model]['xs'][energy]['WH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-WH.txt') 
          self._YR[YRversion][model]['xs'][energy]['ZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ZH.txt') 
          self._YR[YRversion][model]['xs'][energy]['ggZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggZH.txt') 
          # Only have full uncertainty breakdown between qq/gg for 125.0 GeV in ZH case (YR4 only as well)
          if YRversion in ['YR4'] :
            self._YR[YRversion][model]['xs'][energy]['qqZH125'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-qqZH125.txt')
            self._YR[YRversion][model]['xs'][energy]['ggZH125'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggZH125.txt')
          self._YR[YRversion][model]['xs'][energy]['bbH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-bbH.txt') 
          self._YR[YRversion][model]['xs'][energy]['ttH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ttH.txt') 
  
      # ... BSM (high mass NWA Higgs-like)
      N3LO = False # Switch to use either N3LO or NNLO+NNLL ggH cross sections
      if model == 'bsm' :
        if YRversion in  ['YR4prel','YR4'] :
          if not energy in ['13TeV'] : return
          if not energy in self._YR[YRversion][model]['xs'] : self._YR[YRversion][model]['xs'][energy] = {}
          if N3LO == False and YRversion != 'YR4prel' :
            self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-ggH-NNLO-NLL.txt') 
          else:
            self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-ggH.txt') 
          self._YR[YRversion][model]['xs'][energy]['vbfH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-vbfH.txt') 
          self._YR[YRversion][model]['xs'][energy]['WH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-WH.txt')
          self._YR[YRversion][model]['xs'][energy]['ZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-ZH.txt')
          #self._YR[YRversion][model]['xs'][energy]['ggZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-ggZH.txt')
          self._YR[YRversion][model]['xs'][energy]['bbH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-bbH.txt')
          self._YR[YRversion][model]['xs'][energy]['ttH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/xs/'+energy+'/'+energy+'-ttH.txt')


      # BR
      # ... SM
      if model == 'sm' : 

        if YRversion in  ['YR2'] : 
          self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR.txt')
          self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR1.txt')
        if YRversion in  ['YR3'] : 
          self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR2bosons.txt')
          self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR2fermions.txt')
        if YRversion in  ['YR4prel','YR4'] :  
          self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR4.txt')
          self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR4.txt')

      # ... BSM (high mass NWA Higgs-like)
      if model == 'bsm' :
        if YRversion in  ['YR4prel','YR4'] :
          self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/br/BR4.txt')
          self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/bsm/br/BR4.txt')

   def printYR(self):
      print self._YR

   def GetYR(self):
     return self._YR


   def GetYRVal(self,YRDic,mh,Key):
     iMass=float(mh)
     if iMass in YRDic :
       if not Key in YRDic[iMass] : return 0.
       return YRDic[iMass][Key]
     else:
       n=len(YRDic.keys())
       x=[]
       y=[]
       for jMass in sorted(YRDic.keys()):
         if  Key in YRDic[jMass] :
           x.append(jMass)
           y.append(YRDic[jMass][Key])
       if iMass < x[0] or iMass > x[n-1] : return 0
       gr = TGraph(n,array('f',x),array('f',y));
       sp = TSpline3("YR",gr);
       return sp.Eval(iMass)
     return 0

   def GetHiggsProdXS(self,YRversion,energy,proc,mh,model='sm'):
     if not YRversion in self._YR                                 : return 0
     if not model     in self._YR[YRversion]                      : return 0
     if not 'xs'      in self._YR[YRversion][model]               : return 0
     if not energy    in self._YR[YRversion][model]['xs']         : return 0
     if proc in ['HWplus','HWminus'] :
       if not 'WH'      in self._YR[YRversion][model]['xs'][energy]  : return 0 
     else:
       if not proc      in self._YR[YRversion][model]['xs'][energy]  : return 0 
    
     #print 'Hello',proc 
     if proc == 'ZH' :
       xs_ZH = self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'XS_pb')
       if self._UseggZH and 'YR4' in YRversion and not model == 'bsm' :
         xs_ggZH = self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['ggZH'],mh,'XS_pb')
       else:
         xs_ggZH = 0.
       return xs_ZH-xs_ggZH
     elif proc == 'HWplus' :
       if 'YR4' in YRversion :
         return self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['WH'],mh,'XS_W_plus_pb')
       else:
         return 0.
     elif proc == 'HWminus' :
       if 'YR4' in YRversion :
         return self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['WH'],mh,'XS_W_minus_pb')
       else:
         return 0.
     else:
       return self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'XS_pb')

   def GetHiggsProdXSNP(self,YRversion,energy,proc,mh,np='scale',model='sm'):
     # np= 'scale' or 'pdf'
     if not np in ['scale','pdf']                                 : return '1.0'
     if not YRversion in self._YR                                 : return '1.0'
     if not model     in self._YR[YRversion]                      : return '1.0'
     if not 'xs'      in self._YR[YRversion][model]               : return '1.0'
     if not energy    in self._YR[YRversion][model]['xs']         : return '1.0'
     if proc in ['HWplus','HWminus'] :
       if not 'WH'      in self._YR[YRversion][model]['xs'][energy]  : return '1.0'
     else:
       if not proc      in self._YR[YRversion][model]['xs'][energy]  : return '1.0'
        
     if    np == 'scale' :
       if   proc == 'ZH' and YRversion in ['YR4'] and float(mh) == 125.0 and model == 'sm' :
         return str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['qqZH125'],mh,'Scale_neg')/100.) + '/' + str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['qqZH125'],mh,'Scale_pos')/100.)
       elif proc == 'ggZH' and YRversion in ['YR4'] and float(mh) == 125.0 and model == 'sm' :
         return str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['ggZH125'],mh,'Scale_neg')/100.) + '/' + str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['ggZH125'],mh,'Scale_pos')/100.)
       elif proc == 'ggZH':
         return '1.37'  # Number from Run-I CMS/ATLAS combination !
       else:
         return str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'Scale_neg')/100.) + '/' + str(1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'Scale_pos')/100.)

     elif  np == 'pdf' :
       if   proc == 'ZH' and YRversion in ['YR4'] and float(mh) == 125.0 and model == 'sm' :
         return str( 1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['qqZH125'],mh,'PDF_plus_alpha_s')/100.  )
       elif proc == 'ggZH' and YRversion in ['YR4'] and float(mh) == 125.0 and model == 'sm' :
         return str( 1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy]['ggZH125'],mh,'PDF_plus_alpha_s')/100.  )
       elif proc == 'ggZH':
         return '1.15'  # Number from Run-I CMS/ATLAS combination !
       else:  
         return str( 1.0+self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'PDF_plus_alpha_s')/100.  )





   def YR4dec(self,YRversion,decay):
     if not YRversion in ['YR4prel','YR4' ] : return decay
     if decay == 'H_bb'       : return 'hbb'
     if decay == 'H_tautau'   : return 'htt'
     if decay == 'H_mumu'     : return 'hmm'
     if decay == 'H_ssbar'    : return 'hss'
     if decay == 'H_ccbar'    : return 'hcc'
     if decay == 'H_ttbar'    : return 'htoptop'
     if decay == 'H_gg'       : return 'hgluglu'
     if decay == 'H_gamgam'   : return 'hgg'
     if decay == 'H_Zgam'     : return 'hzg'
     if decay == 'H_WW'       : return 'hww'
     if decay == 'H_ZZ'       : return 'hzz'
     return decay

   def GetHiggsBR(self,YRversion,decay,mh,model='sm'):
     if not YRversion in self._YR                                 : return 0
     if not model     in self._YR[YRversion]                      : return 0
     if not 'br'      in self._YR[YRversion][model]               : return 0
     if   decay in [ 'H_bb', 'H_tautau' , 'H_mumu' , 'H_ssbar'  , 'H_ccbar'  , 'H_ttbar' ] : 
       return self.GetYRVal(self._YR[YRversion][model]['br']['ff'],mh,self.YR4dec(YRversion,decay))
     elif decay in [ 'H_gg', 'H_gamgam', 'H_Zgam', 'H_WW' , 'H_ZZ', 'Total_Width_GeV' ] : 
       return self.GetYRVal(self._YR[YRversion][model]['br']['VV'],mh,self.YR4dec(YRversion,decay))
     return 0

   def GetHiggsXS4Sample(self,YRVersion,energy,SampleName):
     HiggsXS = {}
     HiggsXS['Sample'] = SampleName
     HiggsXS['Energy'] = energy
     # ... Higgs production mechanism
     HiggsProdXS = 0.
     ProdMode = 'unknown'
     if 'Mlarge' in SampleName : ProdMode = 'unknown' ## 
     elif 'GluGluH'  in SampleName : ProdMode = 'ggH'
     elif 'VBFH'     in SampleName : ProdMode = 'vbfH'
     elif 'HZJ'      in SampleName : ProdMode = 'ZH'
     elif 'ggZH'     in SampleName : ProdMode = 'ggZH'
     elif 'GluGluZH' in SampleName : ProdMode = 'ggZH'
     elif 'HWplusJ'  in SampleName : ProdMode = 'HWplus'
     elif 'HWminusJ' in SampleName : ProdMode = 'HWminus'
     elif 'ttH'      in SampleName : ProdMode = 'ttH'  
     # Alternative JCP gg->H samples
     elif 'VBF_H0' in SampleName and '_ToWWTo2L2Nu' in SampleName : ProdMode = 'vbfH'  
     elif 'H0'     in SampleName and '_ToWWTo2L2Nu' in SampleName : ProdMode = 'ggH'  
     #elif 'H0ph_ToWWTo2L2Nu' in SampleName or 'H0m_ToWWTo2L2Nu' in SampleName or 'H0pm_ToWWTo2L2Nu' in SampleName or 'H0L1_ToWWTo2L2Nu' in SampleName : ProdMode = 'ggH'
     HiggsMass   = 0.
     if 'Mlarge' in SampleName : HiggsMass = '0.0'
     elif '_M' in SampleName : HiggsMass = SampleName.split('_M')[1]
     if '_' in str(HiggsMass) : HiggsMass = HiggsMass.split('_')[0]
     #if 'large' in HiggsMass : ProdMode = 'unknown'
     # Alternative JCP gg->H samples
     if 'H0'     in SampleName and '_ToWWTo2L2Nu' in SampleName : HiggsMass = 125.0
     #if 'H0ph_ToWWTo2L2Nu' in SampleName or 'H0m_ToWWTo2L2Nu' in SampleName or 'H0pm_ToWWTo2L2Nu' in SampleName or 'H0L1_ToWWTo2L2Nu' in SampleName : HiggsMass = 125.0
     if not ProdMode == 'unknown' :
       if float(HiggsMass) <= 130 and float(HiggsMass) >= 120: 
         HiggsProdXS = self.GetHiggsProdXS(YRVersion,energy,ProdMode,HiggsMass)
       else:
         HiggsProdXS = self.GetHiggsProdXS(YRVersion,energy,ProdMode,HiggsMass,'bsm')
     
     HiggsXS['ProdMode']  = ProdMode
     HiggsXS['HiggsMass'] = HiggsMass
     HiggsXS['ProdXS']    = HiggsProdXS

     # ... Higgs decay
     HiggsBR = 0.
     DecayMode =  'unknown'
     if 'HToWW'       in SampleName : DecayMode = 'H_WW'
     if 'HToZZ'       in SampleName : DecayMode = 'H_ZZ'
     if 'HToTauTau'   in SampleName : DecayMode = 'H_tautau'
     if 'HJetTobb'    in SampleName : DecayMode = 'H_bb'
     if 'HJetToNonbb' in SampleName : DecayMode = 'H_bb'
     # Alternative JCP gg->H samples
     if 'H0'     in SampleName and '_ToWWTo2L2Nu' in SampleName : DecayMode = 'H_WW'
     #if 'H0ph_ToWWTo2L2Nu' in SampleName or 'H0m_ToWWTo2L2Nu' in SampleName or 'H0pm_ToWWTo2L2Nu' in SampleName or 'H0L1_ToWWTo2L2Nu' in SampleName : DecayMode = 'H_WW'
     #if 'large' in HiggsMass : DecayMode = 'unknown'
     if not DecayMode == 'unknown' :
       if float(HiggsMass) <= 130 :
         HiggsBR = self.GetHiggsBR(YRVersion,DecayMode,HiggsMass)
       else:
         HiggsBR = self.GetHiggsBR(YRVersion,DecayMode,HiggsMass,'bsm')    
       if 'HJetToNonbb' in SampleName : HiggsBR = 1.0 - HiggsBR

     HiggsXS['DecayMode'] = DecayMode
     HiggsXS['HiggsBR'  ] = HiggsBR
     
     # ... Final states
     FinalState =  'unknown'
     FinalStateBR = 1.

     if 'WWTo2L2Nu' in SampleName :  
        FinalState   = 'WW->2l2v'
        FinalStateBR = self._br['W2lv']*self._br['W2lv']
     if 'WWToLNuQQ' in SampleName or 'WWToNuQQ' in SampleName:  
        FinalState   = 'WW->lvQQ'
        FinalStateBR = self._br['W2lv']*self._br['W2QQ']
     if 'ZZTo4L'    in SampleName :  
        FinalState   = 'ZZ->4l'
        FinalStateBR = self._br['Z2ll']*self._br['Z2ll']

     # ...... WH with W decays BR 
     if ProdMode == 'HWplus' or ProdMode == 'HWminus' :
        if '_WToLNu_'  in SampleName : 
           FinalState   += ' + W->lv'
           FinalStateBR *= self._br['W2lv']
        elif '_LNu_' in SampleName :
           FinalState   += ' + W->lv'
           FinalStateBR *= self._br['W2lv'] 
        elif '_WToQQ_'   in SampleName :  
           FinalState   += ' + W->QQ'
           FinalStateBR *= self._br['W2QQ']
     # ...... ZH with Z decays BR
     if ProdMode == 'ZH' or ProdMode == 'ggZH' :
        if '_ZTo2L_' in SampleName :
           FinalState   += ' + Z->ll'
           FinalStateBR *= self._br['Z2ll'] 

     HiggsXS['FinalState']   = FinalState
     HiggsXS['FinalStateBR'] = FinalStateBR

     # Final X-Section
     HiggsXS['xs'] =  HiggsProdXS * HiggsBR * FinalStateBR    
     print HiggsXS
     return HiggsXS

### Below some examples of usage :

#HiggsXS = HiggsXSection()
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_JHUGen698_M900')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_JHUGen698_M2000')
#print HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','pdf','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.0','pdf','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','pdf','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.0','pdf','sm')

#print HiggsXS.GetHiggsBR('YR4prel','H_WW','500.0','bsm')
#print HiggsXS.GetHiggsBR('YR4prel','H_WW','1000.0','bsm')
#print HiggsXS.GetHiggsBR('YR4prel','H_WW','1500.0','bsm')
#print HiggsXS.GetHiggsBR('YR4','H_WW','125.0','bsm')

#HiggsXS = HiggsXSection() 
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_M130')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_M750')

#HiggsXS.printYR()
#print HiggsXS.GetHiggsProdXS('YR2','8TeV','ggH','125.0')
#print HiggsXS.GetHiggsProdXS('YR3','8TeV','ggH','125.0')
#print HiggsXS.GetHiggsProdXS('YR4prel','13TeV','ggH','125.0')

#print HiggsXS.GetHiggsBR('YR2','H_WW','125.0')
#print HiggsXS.GetHiggsBR('YR3','H_WW','125.0')
#print HiggsXS.GetHiggsBR('YR4prel','H_WW','125.0')

#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToZZTo4L_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','VBFHToTauTau_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWToLNuQQ_M650')
#
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','VBFHToTauTau_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','HWplusJ_HToWW_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','ggZH_HToWW_M130')

#print HiggsXS.GetHiggsXS4Sample('YR4prel','13TeV','GluGluHToWWTo2L2Nu_M125')
#print HiggsXS.GetHiggsXS4Sample('YR4','13TeV','GluGluHToWWTo2L2Nu_M125')
#print HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','scale','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','pdf','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.0','scale','sm')
#print HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.0','pdf','sm')

