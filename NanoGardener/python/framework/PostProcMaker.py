#!/usr/bin/env python
import os, sys

from LatinoAnalysis.NanoGardener.framework.PostProc_cfg import *

class PostProcMaker():

   def __init__(self,PostProcSteps) : 

     self._Steps = PostProcSteps

   def mkPyCfg(self,inputRootFiles,iStep,fPyName,isData=False):

     fPy = open(fPyName,'a') 
     
     # Common Header
     fPy.write('#!/usr/bin/env python \n')
     fPy.write('import os, sys \n')
     fPy.write('import ROOT \n')
     fPy.write('ROOT.PyConfig.IgnoreCommandLineOptions = True \n')
     fPy.write(' \n')
     fPy.write('from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor \n')
     fPy.write(' \n')

     # Import(s) of modules
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         if 'import' in self._Steps[iSubStep] :
           fPy.write('from '+self._Steps[iSubStep]['import']+' import *\n')  
     else:
       if 'import' in self._Steps[iStep] :
         fPy.write('from '+self._Steps[iStep]['import']+' import *\n') 
     fPy.write(' \n')

     # Declaration(s) of in-line modules
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         if 'declare' in self._Steps[iSubStep] :
           fPy.write(self._Steps[iSubStep]['declare']+'\n')
     else:
       if 'declare' in self._Steps[iStep] :
         fPy.write(self._Steps[iStep]['declare']+'\n') 
     fPy.write(' \n')

     # Files
     fPy.write('files=[')
     for iFile in inputRootFiles : fPy.write('"'+iFile+'",')
     fPy.write(']\n') 
     fPy.write(' \n')
     
     # Configure modules
     fPy.write('p = PostProcessor(  "."   ,          \n')
     fPy.write('                    files ,          \n')
     fPy.write('                    cut=None ,       \n')
     fPy.write('                    branchsel=None , \n')
     fPy.write('                    modules=[        \n')
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         fPy.write('                          '+self._Steps[iSubStep]['module']+',\n')
     else:
       fPy.write('                          '+self._Steps[iStep]['module']+'\n') 
     fPy.write('                            ],      \n') 
     fPy.write('                    provenance=True, \n')
     fPy.write('                    fwkJobReport=True, \n')
     fPy.write('                 ) \n')
     fPy.write(' \n')

     # Common footer
     fPy.write('p.run() \n')
     fPy.write(' \n')

     # Close file
     fPy.close()




pp = PostProcMaker(PostProcSteps)

pp.mkPyCfg (['a','b'],'TestChain','aa.py')
