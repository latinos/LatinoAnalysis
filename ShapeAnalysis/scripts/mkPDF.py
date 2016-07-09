#!/usr/bin/env python

import json
import sys
from sys import exit
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
import traceback
from array import array
from collections import OrderedDict
import math

#import os.path



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):

        cuts = {}
        self._cuts = cuts

        samples = OrderedDict()
        self._samples = samples

        outputDirPDF = {}
        self._outputDirPDF = outputDirPDF

    # _____________________________________________________________________________
    def _connectInputs(self, samples, inputDir, skipMissingFiles):
        inputs = {}
        histoName = 'list_vectors_weights'
        for process,filenames in samples.iteritems():
          histo = self._buildchainHisto(histoName,[ (inputDir + '/' + f) for f in filenames], skipMissingFiles)
          inputs[process] = histo 
          #print ' process -> ', process, ' => ', inputs[process]
        return inputs

    # _____________________________________________________________________________
    def _buildchainHisto(self, histoName, files, skipMissingFiles):
        
        self._outFile.cd()
        #histoSum = ROOT.TH1F
        isFirstOne = True
        for path in files:
            doesFileExist = True
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)
            if "eos.cern.ch" not in path and "eosuser.cern.ch" not in path:
              if not os.path.exists(path):
                print 'File '+path+' doesn\'t exists'
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            else:
              if not self._testEosFile(path):
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            if doesFileExist :
              fileIn = ROOT.TFile(path)
              print " path = ", path
              if isFirstOne :
                self._outFile.cd()
                histoSum = (fileIn.Get(histoName)).Clone()   
                #print ' histogram found : ', histoSum, ' :: ', histoName
                isFirstOne = False
              else :
                histoSumTemp = fileIn.Get(histoName)   
                histoSum.Add(histoSumTemp)
                #print ' histogram found again: ', histoSum
              
        return histoSum


    # _____________________________________________________________________________
    def _testEosFile(self,path): 
      eoususer='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select'
      if 'eosuser.cern.ch' in path: 
        if os.system(eoususer+' ls '+path.split('/eosuser.cern.ch/')[1]) == 0 : return True
      return False 



    # _____________________________________________________________________________
    def makePDF(self, inputFile, outputDirPDF, cuts, samples, inputDir):

        print "================="
        print "==== makePDF ===="
        print "================="

        # NB: the samples have to be OF THE SAME GENERATOR
        #     you cannot get pdf/qcd uncertainty mixing different samples
        #     like mixing A+B, where A is powheg and B is MG5.
        #     If you want to do this
        #     you "mix" it by hand from the output of this code ;)
        #
        
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirPDF = outputDirPDF
        os.system ("mkdir " + outputDirPDF + "/") 

        fileIn = ROOT.TFile(inputFile, "READ")

        self._outFile = ROOT.TFile.Open( self._outputDirPDF + '/results_unc.root', 'recreate')       
        #ROOT.TH1.SetDefaultSumw2(True)

        # get the pre-any-cut histogram
        list_of_trees_to_connect = {}
        for sampleName, sample in self._samples.iteritems():
          list_of_trees_to_connect[sampleName] = sample['name']
              
        #                                                                    skipMissingFiles
        preCutsHistograms = self._connectInputs( list_of_trees_to_connect, inputDir, False)
        
        print ' preCutsHistograms = ', preCutsHistograms
        
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          
          summaryNuisanceFileQCD = open(self._outputDirPDF + '/summary_nuisance_qcd_' + cutName + '.py', 'w')

          summaryNuisanceFileQCD.write("nuisances['QCDscale_qqbar_accept']  = { \n")
          summaryNuisanceFileQCD.write("    'name'  : 'QCDscale_qqbar_accept', \n")
          summaryNuisanceFileQCD.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileQCD.write("    'samples'  : { \n")
            


          summaryNuisanceFilePDF = open(self._outputDirPDF + '/summary_nuisance_pdf_' + cutName + '.py', 'w')

          summaryNuisanceFilePDF.write("nuisances['{pdf_qq_accept']  = { \n")
          summaryNuisanceFilePDF.write("    'name'  : 'pdf_qq_accept', \n")
          summaryNuisanceFilePDF.write("    'type'  : 'lnN', \n")
          summaryNuisanceFilePDF.write("    'samples'  : { \n")



          summaryNuisanceFileAlpha = open(self._outputDirPDF + '/summary_nuisance_alpha_' + cutName + '.py', 'w')

          summaryNuisanceFileAlpha.write("nuisances['Alphascale_qqbar_accept']  = { \n")
          summaryNuisanceFileAlpha.write("    'name'  : 'Alphascale_qqbar_accept', \n")
          summaryNuisanceFileAlpha.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileAlpha.write("    'samples'  : { \n")



          for sampleName, sample in self._samples.iteritems():
            
            tcanvas  = ROOT.TCanvas( "c_unc_" + cutName + "_" + sampleName,      "cc"     , 800, 600 )

            nominalRatio = 1.

            # get the after-cut histogram

            # qcd uncertainty
            low_qcd = 1
            high_qcd = 1
            for ipdf in range(0,10):
              if (ipdf == 0 or ipdf == 5 or ipdf == 9) :
              
                variableName = 'weight_' + str(ipdf)
                shapeName = cutName+"/"+variableName+'/histo_' + sampleName
                histoAfterCuts = fileIn.Get(shapeName)
                totalWeighted = 0
                for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                   totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
                
                denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
                
                if ipdf == 0 :
                  nominalRatio = totalWeighted/denominator
                elif ipdf == 4:
                  low_qcd = totalWeighted/denominator/nominalRatio
                elif ipdf == 8:
                  high_qcd = totalWeighted/denominator/nominalRatio

            string_to_write = "         '" +  sampleName +  "': " +  str(low_qcd) + "/" + str(high_qcd) + " ,\n"
            summaryNuisanceFileQCD.write( string_to_write )
 
 
            # alpha uncertainty
            low_alpha = 1
            high_alpha = 1
            for ipdf in range(109,111):
              if (ipdf == 108 or ipdf == 109) :
              
                variableName = 'weight_' + str(ipdf)
                shapeName = cutName+"/"+variableName+'/histo_' + sampleName
                histoAfterCuts = fileIn.Get(shapeName)
                totalWeighted = 0
                for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                   totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
                
                denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
                
                if ipdf == 109 :
                  low_alpha = totalWeighted/denominator/nominalRatio
                elif ipdf == 110:
                  high_alpha = totalWeighted/denominator/nominalRatio
 
            string_to_write = "         '" +  sampleName +  "': " +  str(low_alpha) + "/" + str(high_alpha) + " ,\n"
            summaryNuisanceFileAlpha.write( string_to_write )

        
            # pdf uncertainty
            histoRatioPDF = ROOT.TH1F('ratio_pdf_', cutName + '_' + sampleName, 100,0, 2)
            for ipdf in range(10,109):
              variableName = 'weight_' + str(ipdf)
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              #print '     -> shapeName = ', shapeName,
              histoAfterCuts = fileIn.Get(shapeName)
              totalWeighted = 0
              #print ' mean*integral = ', histoAfterCuts.GetMean(), ' * ', histoAfterCuts.Integral(), ' = ', histoAfterCuts.GetMean() * histoAfterCuts.Integral(),
              for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                 totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
              #print ' ---> integral = ',    totalWeighted
              
              #print 'preCutsHistograms[', sampleName, '] = ', preCutsHistograms[sampleName]
              
              denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
              
              histoRatioPDF.Fill(totalWeighted/denominator/nominalRatio)


            histoRatioPDF.Draw()
            tcanvas.SaveAs(self._outputDirPDF + "/" + "c_unc_" + cutName + "_" + sampleName + ".png")
            tcanvas.SaveAs(self._outputDirPDF + "/" + "c_unc_" + cutName + "_" + sampleName + ".root")

            tcanvas.Write()
            string_to_write = "         '" +  sampleName +  "': " +  str(1. + histoRatioPDF.GetRMS()) + " ,\n"
            summaryNuisanceFilePDF.write( string_to_write )


          summaryNuisanceFilePDF.write("    }, \n")
          summaryNuisanceFilePDF.write(" } \n")
          summaryNuisanceFilePDF.close()

          summaryNuisanceFileQCD.write("    }, \n")
          summaryNuisanceFileQCD.write(" } \n")
          summaryNuisanceFileQCD.close()

          summaryNuisanceFileAlpha.write("    }, \n")
          summaryNuisanceFileAlpha.write(" } \n")
          summaryNuisanceFileAlpha.close()
          
          
        print " >> all but really all "
        


   # _____________________________________________________________________________
   # --- squared sum
    def SumQ(self, A, B):
       return math.sqrt(A*A + B*B)

   # _____________________________________________________________________________
   # --- Ratio: if denominator is zero, then put 0!
    def Ratio(self, A, B):
       if B == 0:
         #print "divide by 0"
         return 0.
       else :
         return A / B
 
                  
   # _____________________________________________________________________________
    def GetMaximumIncludingErrors(self, histo):
        maxWithErrors = 0.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin) + histo.GetBinError (iBin)
          if binHeight > maxWithErrors :
            maxWithErrors = binHeight
      
        return maxWithErrors;

   # _____________________________________________________________________________
    def GetMinimum(self, histo):
        minimum = -1.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin)
          if binHeight < minimum or minimum<0:
            minimum = binHeight
      
        return minimum;
 
 
    # _____________________________________________________________________________
    def defineStyle(self):

        print "=================="
        import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        
   


if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------



   _ \   __ \   ____|                                      |          _)         |          
  |   |  |   |  |          |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
  ___/   |   |  __|        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
 _|     ____/  _|         \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
                                                                                     ____/  

 
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputDirPDF'   , dest='outputDirPDF'   , help='output directory for values and plots'           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                      , default='input.root')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory where to find the default trees' , default='./data/')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile          = ", opt.inputFile
    print " outputDirPDF       = ", opt.outputDirPDF
    print " inputDir           = ", opt.inputDir
     
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
   
    factory.makePDF( opt.inputFile ,opt.outputDirPDF, cuts, samples, opt.inputDir)
    
    print '... and now closing ...'
        
       
