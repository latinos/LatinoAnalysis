#!/usr/bin/env python

from  LatinoAnalysis.ShapeAnalysis.ShapeFactoryMulti import ShapeFactory as SF
import array
from sklearn.utils import resample
import tempfile
import root_numpy as rnp
import numpy as np
import math
from numpy import linalg as LA

# Common Tools & batch
from LatinoAnalysis.Tools.commonTools import *


# ----------------------------------------------------- KernelFactory --------------------------------------

class KernelFactory:

    # _____________________________________________________________________________
    def __init__(self):
      
        self._fileIn = None
        self._skipMissingNuisance = False


    def datasetFromTree(self, treeIn, roovars, name, reweight=""):
      if reweight == "":
        rooweight = ROOT.RooRealVar('weight', 'weight', -1000., 1000)
        return ROOT.RooDataSet (name, name, treeIn, ROOT.RooArgSet(*(roovars + [rooweight])), "", "weight")
      
      origweight = ROOT.RooRealVar('weight', 'weight', -1000., 1000)
      rew = ROOT.RooRealVar(reweight, reweight, -1000., 1000)
      origdataset = ROOT.RooDataSet (name, name, treeIn, ROOT.RooArgSet(*(roovars + [origweight, rew])), "")
      wFunc = ROOT.RooFormulaVar('reweighted', 'reweighted', 'weight*'+reweight, ROOT.RooArgList(origweight, rew))
      w = origdataset.addColumn(wFunc)
      return ROOT.RooDataSet (origdataset.GetName(), origdataset.GetTitle(), origdataset, origdataset.get(), "", w.GetName())
  

    # _____________________________________________________________________________
    # _____________________________________________________________________________
    def runAlgo(self, fileTreeIn, treeName, cutName, variableName, variable, sampleName, newSampleName, reweight = "", saveEigenVariations=True, resamples=100):
      treeInOrig = fileTreeIn.Get(cutName + "/" + treeName +"/"+treeName+'_'+sampleName)
      if treeInOrig == None:
         raise RuntimeError('Missing tree '+ cutName + "/" + treeName+"/"+treeName+'_'+sampleName)
      #print variable   
      branches = variable['name'].split(':')
      for branch in branches:
        if treeInOrig.GetBranch(branch) == None:
          raise RuntimeError('Missing branch ' + branch + ' in tree '+ cutName + "/" + variableName+"/"+treeName+'_'+sampleName)
      if treeInOrig.GetBranch('weight') == None:
        raise RuntimeError("Missing branch weight in tree "+ cutName + "/" + variableName+"/"+treeName+'_'+sampleName)
      if reweight != "":
        if treeInOrig.GetBranch(reweight) == None:
          raise RuntimeError('Missing branch weight'+reweight+" in tree "+ cutName + "/" + variableName+"/"+treeName+'_'+sampleName) 
      shape = SF._makeshape(variableName, variable['range']) 
      if len(branches) != shape.GetDimension():
        raise RuntimeError('Mismatch between expression '+variable['name']+" and dimension of the allocated shape "+str(shape.GetDimension()))
      fold = 0
      if 'fold' in variable.keys():
        fold = variable['fold']
      # select only events with weight different from 0
      selectionW = "abs(weight) > 0."
      #if weightSuffix != "":
      #  selectionW = "abs(weight"+weightSuffix+") > 0."
      treeIn = treeInOrig.CopyTree(selectionW)

      roovars = []
      vbinedges = []
      # remember y:x
      for ib, branch in enumerate(reversed(branches)):
        if ib == 0:
          axis = shape.GetXaxis()
        elif ib == 1:
          axis = shape.GetYaxis()
        else:
          raise RuntimeError("cannot handle histo with "+len(branches)+" dimensions")
        lowerbound = shape.GetXaxis().GetXmin() if fold != 1 and fold != 3 else 0  # will not work for non positive deined observables
        upperbound = shape.GetXaxis().GetXmax() if fold != 2 and fold != 3 else shape.GetXaxis().GetXmax()*20 
        binning = ROOT.RooBinning(lowerbound, upperbound)
        binedges = [lowerbound]
        for ibin in range(1, axis.GetNbins()):
          edge = axis.GetBinUpEdge(ibin)
          binning.addBoundary(edge)
          binedges.append(edge)
        binedges.append(upperbound) 
        vbinedges.append(binedges)
        roovar = ROOT.RooRealVar(branch, branch, lowerbound, upperbound)
        #roovar.setBinning(binning)
        roovars.append(roovar)
      print vbinedges
      if treeIn.GetEntries() == 0:
        print "WARNING: tree"+ cutName + "/" + variableName+"/"+treeName+'_'+sampleName+" has 0 entries"
        return 0
     
      dataset = self.datasetFromTree(treeIn, roovars, 'dataset', reweight) 
      if len(branches)==1:
        pdf = ROOT.RooKeysPdf ("weighted", "weighted", roovars[0], dataset, ROOT.RooKeysPdf.MirrorBoth)
      else:
        pdf = ROOT.RooNDKeysPdfAnalytical("weighted", "weighted", ROOT.RooArgList(*roovars), dataset, "mad")
    
      nvariarions = (len(vbinedges[0])-1) if len(branches)==1 else (len(vbinedges[0])-1)*(len(vbinedges[1])-1)
      # in this case do not do resampling 
      if not saveEigenVariations:
        average=np.empty([(len(vbinedges[0])-1) if len(branches)==1 else (len(vbinedges[0])-1)*(len(vbinedges[1])-1)])
        for binX in range(len(vbinedges[0])-1):
            if len(branches)==1:
              roovars[0].setRange("binX"+str(binX), vbinedges[0][binX], vbinedges[0][binX+1])
              value = pdf.createIntegral(roovars[0], roovars[0], "binX"+str(bin)).getVal()
              average[binX] = value
            else:
              for binY in range(len(vbinedges[1])-1):
                rangename = "binX"+str(binX)+"binY"+str(binY)
                roovars[0].setRange(vbinedges[0][binX], vbinedges[0][binX+1])
                roovars[1].setRange(vbinedges[1][binY], vbinedges[1][binY+1])
                value = pdf.analyticalIntegral(1)
                average[binX*(len(vbinedges[1])-1)+binY] = value if not math.isnan(value) else 0 # protect? 
        average /= np.sum(average) 
      # in this case we resample
      else:
        atree = rnp.tree2array(treeIn)
        tf = tempfile.NamedTemporaryFile()
        fileout=ROOT.TFile(tf.name, "recreate")
        fileout.cd()
        integrals=np.empty([resamples, (len(vbinedges[0])-1) if len(branches)==1 else (len(vbinedges[0])-1)*(len(vbinedges[1])-1)])
        for ir in range(resamples):
          sumw = -999
          while sumw < 0:
            atreesub = resample(atree, n_samples=treeIn.GetEntries(), random_state=1000+ir)
            sumw = np.sum(atreesub['weight'])
          treesub = rnp.array2tree(atreesub)
          for ivar in range(len(branches)):
            roovars[ivar].setRange(vbinedges[0][0], vbinedges[ivar][-1])
          datasetsub = self.datasetFromTree(treesub, roovars, "datasetsub"+str(ir), reweight)
          print datasetsub.sumEntries()
          datasetsub.get().Print()
           #ROOT.RooDataSet("datasetsub"+str(ir), "datasetsub"+str(ir), treesub, ROOT.RooArgSet(*(roovars + [rooweight])), "", "weight")
          if len(branches)==1:
            pdf = ROOT.RooKeysPdf ("weighted"+str(ir), "weighted"+str(ir), roovars[0], datasetsub, ROOT.RooKeysPdf.MirrorBoth)
          else:
            pdf = ROOT.RooNDKeysPdfAnalytical ("weighted"+str(ir), "weighted"+str(ir), ROOT.RooArgList(*roovars), datasetsub, "mad")
          #normalization = pdf.analyticalIntegral(1)  
          for binX in range(len(vbinedges[0])-1):
            if len(branches)==1:
              roovars[0].setRange("binX"+str(binX), vbinedges[0][binX], vbinedges[0][binX+1])
              value = pdf.createIntegral(roovars[0], roovars[0], "binX"+str(bin)).getVal()
              integrals[i, binX] = value 
            else:
              for binY in range(len(vbinedges[1])-1):
                rangename = "binX"+str(binX)+"binY"+str(binY)
                roovars[0].setRange(vbinedges[0][binX], vbinedges[0][binX+1])
                roovars[1].setRange(vbinedges[1][binY], vbinedges[1][binY+1])
                value = pdf.analyticalIntegral(1)
                print "setting bin", binX*(len(vbinedges[1])-1)+binY, "to", value 
                integrals[ir, binX*(len(vbinedges[1])-1)+binY] = value if not math.isnan(value) else 0 # protect? 
          del datasetsub
          del pdf
        print integrals
        normalizations = np.sum(integrals, axis=1)
        #print normalizations
        integrals = integrals[normalizations>0, :]
        normalizations = normalizations[normalizations>0]
        #print normalizations
        integrals /= np.where(normalizations == 0, 1, normalizations)[:, np.newaxis]
        #print normalizations, integrals
        #print integrals.sum(axis = 1)
        average = np.mean(integrals, axis=0)
        #print average
         
        cova_m = np.cov(np.transpose(integrals))
        try:
          w, v = LA.eig(cova_m)
          invv = LA.inv(v)
        except:
          w = np.zeros_like(average)
          v = np.identity(average.shape[0])
          invv = v

        #protect against negative eigenvalues
        w  = w.clip(0,10000)
        print v.shape
        print w
        print average.shape
        sqrtw = np.sqrt(w)
        average_rotated = np.matmul(v,average)
        
        # compute a number of variations equal to the number of bins, but in the orthogonal space
        variations_up=np.empty([nvariarions, nvariarions])
        variations_do=np.empty([nvariarions, nvariarions])
        
        for bin in range(nvariarions):
          average_rotated_shifted_up = np.copy(average_rotated)
          average_rotated_shifted_up[bin] =  average_rotated_shifted_up[bin]+sqrtw[bin]
          shifted_up = np.matmul(invv,average_rotated_shifted_up)
          variations_up[bin] = shifted_up

          average_rotated_shifted_do = np.copy(average_rotated)
          average_rotated_shifted_do[bin] =  average_rotated_shifted_do[bin]-sqrtw[bin]
          shifted_do = np.matmul(invv,average_rotated_shifted_do)
          variations_do[bin] = shifted_do
        #print average
        #print variations_up
        #print variations_do      
      
      self._fileOut.cd ( cutName + "/" + variableName)
      nominal = ROOT.TH1D("histo_"+newSampleName, "histo_"+newSampleName, nvariarions, 0., float(nvariarions))
      rnp.array2hist(average*dataset.sumEntries(), nominal)
      nominal.Write()
      
      if saveEigenVariations == True:
        for ivar in range(nvariarions):
          variedUp =  ROOT.TH1D("histo_"+newSampleName+"_eigenVariation"+str(ivar)+"Up", "histo_"+newSampleName+"_eigenVariation"+str(ivar)+"Up", nvariarions, 0., float(nvariarions))
          rnp.array2hist(variations_up[ivar]*dataset.sumEntries(), variedUp)
          variedDown =  ROOT.TH1D("histo_"+newSampleName+"_eigenVariation"+str(ivar)+"Down", "histo_"+newSampleName+"_eigenVariation"+str(ivar)+"Down", nvariarions, 0., float(nvariarions))
          rnp.array2hist(variations_do[ivar]*dataset.sumEntries(), variedDown)
          variedUp.Write()
          variedDown.Write()
      #return nominal
      
        
  


    def mkKernel( self, inputFile, outputFile, fileWithTree, treeName, variables, cuts, samples, structureFile, nuisances, samplesToTreat):
    
        print "=================="
        print "==== mkKernel ===="
        print "=================="
        
        #
        # copied from mkdatacards.py
        #
        if os.path.isdir(inputFile):
          # ONLY COMPATIBLE WITH OUTPUTS MERGED TO SAMPLE LEVEL!!
          self._fileIn = {}
          for sampleName in samples:
            self._fileIn[sampleName] = ROOT.TFile.Open(inputFile+'/plots_%s_ALL_%s.root' % (self._tag, sampleName))
            if not self._fileIn[sampleName]:
              raise RuntimeError('Input file for sample ' + sampleName + ' missing')
        else:
          self._fileIn = ROOT.TFile(inputFile, "READ")

        # get the tree from the file with the correct tree:
        if not os.path.exists(fileWithTree):
          raise RuntimeError('Input file ' + fileWithTree + ' missing')
        fileTreeIn = ROOT.TFile(fileWithTree, "READ")


        #
        # the new output file with histograms
        #
                
        self._fileOut = ROOT.TFile(outputFile, "recreate")

        #
        # and prepare the structure of the output file as it is the input file
        #
        for cutName in cuts:
          self._fileOut.mkdir ( cutName )
          for variableName, variable in variables.iteritems():
            self._fileOut.mkdir ( cutName + "/" + variableName)


        #
        # loop over cuts
        #
        for cutName in cuts:
          
          #
          # prepare the signals and background list of samples
          # after removing the ones not to be used in this specific phase space
          #
  
          for sampleName in samples:
          
            # loop over variables
            for variableName, variable in variables.iteritems():
              # skip trees
              if 'name' not in variable.keys():
                continue
              
              self._fileOut.cd ( cutName + "/" + variableName)
              
              #
              # check if this variable is available only for a selected list of cuts
              #
              if 'cuts' in variable and cutName not in variable['cuts']:
                continue
                
              #print "  variableName = ", variableName
  
              histo = self._getHisto(cutName, variableName, sampleName)
              try:
                # save "events unmodified, just change the name"
                float(variable['name'])
                histo.SetName("histo_"+sampleName+"_KEYS")
                histo.SetTitle("histo_"+sampleName+"_KEYS")
                print "saving unmodified", cutName, variableName, sampleName
                histo.Write()
                for nuisanceName, nuisance in nuisances.iteritems():
                  if nuisanceName == 'stat':
                    continue
                  histoUp = self._getHisto(cutName, variableName, sampleName, "_"+nuisance['name']+"Up")
                  if histoUp != None:
                    histoUp.SetName(str(histoUp.GetName()).replace("histo_"+sampleName, "histo_"+sampleName+"_KEYS"))
                    histoUp.Write()
                    print "saving unmodified", cutName, variableName, sampleName, nuisanceName+"Up"
                  histoDown = self._getHisto(cutName, variableName, sampleName, "_"+nuisance['name']+"Down")
                  if histoDown != None:
                    histoDown.SetName(str(histoDown.GetName()).replace("histo_"+sampleName, "histo_"+sampleName+"_KEYS"))
                    histoDown.Write()
                    print "saving unmodified", cutName, variableName, sampleName, nuisanceName+"Down"
                continue
              except ValueError:
                pass
              
              if structureFile[sampleName]['isData'] == 1 :
                pass
              elif  sampleName in samplesToTreat:
                self.runAlgo(fileTreeIn, treeName, cutName, variableName, variable, sampleName, sampleName+"_KEYS", "", True)

      
                #
                # Now check the nuisances: 
                #     Nuisances
                #             
      
                for nuisanceName, nuisance in nuisances.iteritems():
                  if 'type' not in nuisance:
                    raise RuntimeError('Nuisance ' + nuisanceName + ' is missing the type specification')
      
                  if nuisanceName == 'stat' or nuisance['type'] == 'rateParam' or nuisance['type'] in ['lnN', 'lnU']:
                    # nothing to do ...
                    continue
      
                  # check if a nuisance can be skipped because not in this particular cut
                  if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                    continue
      
                  if 'samples' in nuisance and sampleName not in nuisance['samples']:
                    continue
                    
                  if nuisance['type'] == 'shape':
                    if nuisance['kind'] == 'weight':
                      self.runAlgo(fileTreeIn, treeName, cutName, variableName, variable, sampleName, sampleName+"_KEYS_"+nuisance['name']+"Up", 'reweight_'+nuisance['name']+"Up", saveEigenVariations=False)
                      self.runAlgo(fileTreeIn, treeName, cutName, variableName, variable, sampleName, sampleName+"_KEYS_"+nuisance['name']+"Down", 'reweight_'+nuisance['name']+"Down", saveEigenVariations=False)
                  

                    #elif nuisance['kind'] == 'tree'
                    #

        self._fileOut.Close()
        print "-------------------------"
        print " outputFile written : " , outputFile
        print "-------------------------"
            

        if type(self._fileIn) is dict:
          for source in self._fileIn.values():
            source.Close()
        else:
          self._fileIn.Close()

    # _____________________________________________________________________________
    def _getHisto(self, cutName, variableName, sampleName, suffix = None):
        shapeName = '%s/%s/histo_%s' % (cutName, variableName, sampleName)
        if suffix:
            shapeName += suffix

        if type(self._fileIn) is dict:
            # by-sample ROOT file
            histo = self._fileIn[sampleName].Get(shapeName)
        else:
            # Merged single ROOT file
            histo = self._fileIn.Get(shapeName)

        #if not histo:
            #print shapeName, 'not found'
      
        return histo

