#!/usr/bin/env python

import ROOT
import copy
import os.path
import shutil
import time
import collections
import tempfile
import logging
from array import array

ROOT.ROOT.EnableThreadSafety()

ROOT.gSystem.Load('libLatinoAnalysisMultiDraw.so')
try:
  ROOT.multidraw.MultiDraw
except:
  raise RuntimeError('Failed to load libMultiDraw')

# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):
      
        variables = {}
        self._variables = variables

        cuts = {} # {name: expr} or {name: {'expr': expr, 'samples': []}}
        self._cuts = cuts

        samples = {}
        self._samples = samples


        self._treeName = 'latino'

        # Alias TTree expressions
        self.aliases = {}

    # _____________________________________________________________________________
    def __del__(self):
        pass

    # _____________________________________________________________________________
    def makeNominals(self, inputDir, outputDir, variables, cuts, samples, nuisances, supercut, number=99999, firstEvent=0, nevents=-1):

        print "======================"
        print "==== makeNominals ===="
        print "======================"

        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        #in case some variables need a compiled function 
        for variableName, variable in self._variables.iteritems():
          if variable.has_key('linesToAdd'):
            linesToAdd = variable['linesToAdd']
            for line in linesToAdd:
              ROOT.gROOT.ProcessLineSync(line)
        
        #in case some samples need a compiled function 
        for sampleName, sample in self._samples.iteritems():
          if sample.has_key('linesToAdd'):
            linesToAdd = sample['linesToAdd']
            for line in linesToAdd:
              ROOT.gROOT.ProcessLineSync(line)
        
        print " supercut = ", supercut
        
        if number != 99999 :
          self._outputFileName = outputDir+'/plots_'+self._tag+"_"+str(number)+".root"
        else :
          self._outputFileName = outputDir+'/plots_'+self._tag+".root"

        print " outputFileName = ", self._outputFileName
        os.system ("mkdir -p " + outputDir + "/")
        
        ROOT.TH1.SetDefaultSumw2(True)

        #---- first create the structure in gROOT. We'll write to a file at the end
        print ''
        print '  <cuts>'
        for cutName, cut in self._cuts.iteritems():
          print "cut = ", cutName, " :: ", self._cuts[cutName]
          if type(cut) is dict and 'categories' in cut:
            for catname in cut['categories']:
              ROOT.gROOT.mkdir(cutName + '_' + catname)

              for variableName, variable in self._variables.iteritems():
                if 'cuts' not in variable or cutName in variable['cuts'] or cutName + '/' + catname in variable['cuts']:
                  ROOT.gROOT.mkdir(cutName+"_"+catname+"/"+variableName)

          else:
            ROOT.gROOT.mkdir(cutName)
            
            for variableName, variable in self._variables.iteritems():
              if 'cuts' not in variable or cutName in variable['cuts']:
                ROOT.gROOT.mkdir(cutName+"/"+variableName)

        #---- just print the variables
        print ''
        print '  <variables>'
        for variableName, variable in self._variables.iteritems():
          line = "    variable = " + variableName + " :: "
          if 'name' in variable:
            line += str(variable['name'])
          elif 'class' in variable:
            line += variable['class']
          print line
          print "      range:", variable['range']
          if 'samples' in variable:
            print "      samples:", variable['samples']

        print ''
        print '  <nuisances>'

        for nuisanceName, nuisance in nuisances.iteritems():
          line = "    nuisance = " + nuisanceName
          if 'name' in nuisance:
            line += " :: " + nuisance['name']
          print line
          if 'kind' in nuisance:
              print "      kind:", nuisance['kind']
          print "      type:", nuisance['type']

          if nuisanceName == "stat":
            for item in nuisance["samples"].itervalues():
              if "zeroMCError" not in item:
                item["zeroMCError"] = '0'
            
        #############################################
        # Use MultiDraw to fill the plots in one go #
        #############################################

        # Need to keep a python reference to all plot objects (otherwise python will garbage-collect)
        _allplots = []

        print ''
        print '  <start histogram filling>'

        # One MultiDraw per sample = tree
        for sampleName, sample in self._samples.iteritems():
          print "    sample =", sampleName
          #print "    name:", sample['name']
          #print "    weight:", sample['weight']

          if 'weights' not in sample:
            sample['weights'] = ['1'] * len(sample['name'])

          # then add the lumi scale factor, unless the tree is data
          dataTrees = []
          if 'isData' in sample:
            if len(sample['isData']) == 1 and sample['isData'][0] == 'all':
              # if you put 'all', all the root files are considered "data"
              dataTrees = range(len(sample['name']))
            else:
              for iT in range(len(sample['name'])):
                if sample['isData'][iT] != '0':
                  dataTrees.append(iT)
                  
          for iT in range(len(sample['name'])):
            if iT not in dataTrees:
              # default is "scale to luminosity"
              sample['weights'][iT] = "( (" + sample['weights'][iT] + ") * " + str(self._lumi) + ")"
              print "      sample ['weights'][" + str(iT) + "] = ", sample['weights'][iT]

          drawer = self._connectInputs(sampleName, sample['name'], inputDir, skipMissingFiles=False)
          drawer.setFilter(supercut)

          # Set overall weights on the nominal drawer
          drawer.setReweight(sample['weight'])

          if 'weights' in sample:
            weights = sample['weights']
            print "  weights:", weights
            if len(weights) != 0 and len(weights) != len(sample['name']):
              raise RuntimeError('Number of tree-by-tree weights doesn\'t match the number of trees')
          else:
            weights = []

          for it, w in enumerate(weights):
            if w != '-':
              drawer.setTreeReweight(it, False, w)

          # Set up drawers for tree-type nuisances

          drawersNuisanceUp   = {}
          drawersNuisanceDown = {}

          for nuisanceName, nuisance in nuisances.iteritems():
            if 'kind' not in nuisance or nuisance['kind'] != 'tree':
              continue

            # Sept 2017
            # Tree kind nuisances can be hanndled in two ways:
            # usual way: a full tree for the variation up and a full tree for the variation down
            # This behavior is activated by the presence in the nuisances.py file of the tags 'folderUp' and 'folderDown'
            # alternative way: a combination of trees holding only the varied branches and the central tree for all the unvaried branches.
            # This behavior is activated by the presence in the nuisances.py file of the tags: 'unskimmedFolderUp', 'unskimmedFolderDown', 'unskimmedFriendTreeDir'.
            # Note that one has to use trees before skimming. The skimming can be applied on top is the additional tags 'skimListFolderUp' and 'skimListFolderDown'
            # are present. These tags hold the path to the directories holding the files holding the "prunerlist" event list

            if sampleName not in nuisance['samples']:
              continue

            filenames = [os.path.basename(s) if '###' in s else s for s in sample['name']]

            if 'unskimmedFriendTreeDir' in nuisance.keys():
              unskimmedFriendsDir = nuisance['unskimmedFriendTreeDir']

              try:
                skimListFolderUp = nuisance['skimListFolderUp']
              except KeyError:
                skimListFolderUp = None
              try:
                skimListFolderDown = nuisance['skimListFolderDown']
              except KeyError:
                skimListFolderDown = None

              drawersNuisanceUp[nuisanceName] = self._connectInputs(sampleName, filenames, nuisance['unskimmedFolderUp'], True, unskimmedFriendsDir, skimListFolderUp)
              drawersNuisanceDown[nuisanceName] = self._connectInputs(sampleName, filenames, nuisance['unskimmedFolderDown'], True, unskimmedFriendsDir, skimListFolderDown)

            else:
              drawersNuisanceUp[nuisanceName] = self._connectInputs(sampleName, filenames, nuisance['folderUp'], skipMissingFiles = True)
              drawersNuisanceDown[nuisanceName] = self._connectInputs(sampleName, filenames, nuisance['folderDown'], skipMissingFiles = True)

          # Set overall weights on the nuisance up/down drawers
          for idir, nuisanceDrawers in enumerate([drawersNuisanceUp, drawersNuisanceDown]):
            for nuisanceName, ndrawer in nuisanceDrawers.iteritems():
              configurationNuis = nuisances[nuisanceName]['samples'][sampleName]

              ndrawer.setFilter(supercut)
              ndrawer.setReweight('(%s) * (%s)' % (sample['weight'], configurationNuis[idir]))
  
              for it, w in enumerate(weights):
                if w != '-':
                  ndrawer.setTreeReweight(it, False, w)

          cuts = collections.OrderedDict()
          if 'subsamples' in sample:
            # If the sample has "subsamples" defined (e.g. signal sample for differential),
            # we multiplex the cuts
            for ssName in sorted(sample['subsamples'].iterkeys()):
              ssCut = sample['subsamples'][ssName]
              for cutName, cut in self._cuts.iteritems():
                if type(cut) is dict:
                  if 'samples' not in cut or sampleName in cut['samples'] or (sampleName + '/' + ssName) in cut['samples']:
                    cuts[(ssName, cutName)] = copy.deepcopy(cut)
                    cuts[(ssName, cutName)]['expr'] = '(%s) * (%s)' % (ssCut, cut['expr'])
                else:
                  cuts[(ssName, cutName)] = {'expr': '(%s) * (%s)' % (ssCut, cut)}
          else:
            for cutName, cut in self._cuts.iteritems():
              if type(cut) is dict:
                if 'samples' not in cut or sampleName in cut['samples']:
                  cuts[cutName] = copy.deepcopy(cut)
              else:
                cuts[cutName] = {'expr': cut}

          print ''
          # Loop over cuts ("cut" is a dict)
          for cutKey, cut in cuts.iteritems():
            if type(cutKey) is tuple:
              # sample is split into subsamples
              ssName, cutName = cutKey
              subsampleName = sampleName + '_' + ssName
              cutFullName = '%s__%s' % cutKey
              print "    subsample/cut =", '%s/%s' % cutKey, "::", cut['expr']
            else:
              cutName = cutKey
              subsampleName = sampleName
              cutFullName = cutKey
              print "    cut =", cutFullName, "::", cut['expr']

            drawer.addCut(cutFullName, cut['expr'])

            categoryOrdering = []
            if 'categories' in cut:
              if type(cut['categories']) is dict:
                print '    categories =', ', '.join(cut['categories'].iterkeys())
                for catname, expr in cut['categories'].iteritems():
                  categoryOrdering.append(catname)
                  drawer.addCategory(cutFullName, expr)
              else:
                # is a list
                categoryOrdering = list(cut['categories'])
                print '    categorization =', cut['categorization']
                drawer.setCategorization(cutFullName, cut['categorization'])

            # keep only the nuisances that are applicable to this cut & sample
            applicableNuisances = {}

            for nuisanceName, nuisance in nuisances.iteritems():
              # If "cuts" is not defined in nuisances.py, then it is assumed to affect
              # all the cuts phase spaces
              if (sampleName not in nuisance['samples']) or \
                    ('cuts' in nuisance and cutName not in nuisance['cuts']):
                # this nuisance does not apply to the current sample / phase space
                continue

              applicableNuisances[nuisanceName] = nuisance

              if 'kind' not in nuisance or nuisance['kind'] != 'tree':
                continue

              for nuisanceDrawers in [drawersNuisanceUp, drawersNuisanceDown]:
                try:
                  ndrawer = nuisanceDrawers[nuisanceName]
                except KeyError:
                  continue

                ndrawer.addCut(cutFullName, cut['expr'])
                if 'categorization' in cut:
                  ndrawer.setCategorization(cutFullName, cut['categorization'])
                else:
                  for catname in categoryOrdering:
                    ndrawer.addCategory(cutFullName, cut['categories'][catname])

            histoName = 'histo_' + subsampleName

            # now loop over all the variables ...
            for variableName, variable in self._variables.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              if 'cuts' in variable and cutName not in variable['cuts']:
                continue
             
              # create histogram
              self._logger.debug('---'+subsampleName+'---')
              if 'name' in variable:
                self._logger.debug('Formula: '+str(variable['name']))
              elif 'class' in variable:
                self._logger.debug('Class: '+str(variable['class']))
              self._logger.debug('Cut:     '+cutFullName)

              if 'weight' in variable:
                wgtspec = variable['weight']
                if type(wgtspec) is str:
                  reweight = ROOT.multidraw.ReweightSource(wgtspec)
                else:
                  if 'source' in wgtspec:
                    fname, _, objname = wgtspec['source'].partition(':')
                    ftmp = ROOT.TFile.Open(fname)
                    wsource = ftmp.Get(objname)
                    try:
                      wsource.SetDirectory(0)
                    except:
                      pass
                    ftmp.Close()
                  else:
                    wsource = None
  
                  if 'xexpr' in wgtspec:
                    if 'yexpr' in wgtspec:
                      reweight = ROOT.multidraw.ReweightSource(wgtspec['xexpr'], wgtspec['yexpr'], wsource)
                      print 'Reweighting:', reweight
                    else:
                      reweight = ROOT.multidraw.ReweightSource(wgtspec['xexpr'], wsource)
                  elif 'class' in wgtspec:
                    if 'args' in wgtspec:
                      if type(wgtspec['args']) is tuple:
                        args = wgtspec['args']
                      else:
                        args = (wgtspec['args'],)
                    else:
                      args = tuple()
  
                    func = getattr(ROOT, wgtspec['class'])(*args)
                    reweight = ROOT.multidraw.ReweightSource(ROOT.multidraw.CompiledExprSource(func), wsource)
              else:
                reweight = None

              if 'name' in variable:
                if type(variable['name']) is str:
                  try:
                    xexpr, yexpr = ShapeFactory._splitexpr(variable['name'])
                  except (RuntimeError, TypeError):
                    xexpr, yexpr = variable['name'], ''
                elif type(variable['name']) is tuple:
                  if len(variable['name']) == 1:
                    xexpr = variable['name'][0]
                    yexpr = ''
                  elif len(variable['name']) == 2:
                    yexpr, xexpr = variable['name']
                  else:
                    raise NotImplementedError('Cannot plot >=3D distributions')

              else:
                if 'args' in variable:
                  if type(variable['args']) is tuple:
                    args = variable['args']
                  else:
                    args = (variable['args'],)
                else:
                  args = tuple()
                xexpr = getattr(ROOT, variable['class'])(*args)
                yexpr = ''

              if 'categories' in cut:
                histlist = ROOT.TObjArray()

                for catname in categoryOrdering:
                  ROOT.gROOT.cd(cutName + '_' + catname + '/' + variableName)

                  hTotal = self._makeshape(histoName, variable['range'])
                  _allplots.append(hTotal)
                  hTotal.SetTitle(histoName)
                  hTotal.SetName(histoName)
                  histlist.Add(hTotal)

                if yexpr:
                  filler = drawer.addPlotList2D(histlist, xexpr, yexpr, cutFullName)
                else:
                  filler = drawer.addPlotList(histlist, xexpr, cutFullName)

              else:
                ROOT.gROOT.cd(cutName + '/' + variableName)

                hTotal = self._makeshape(histoName, variable['range'])
                _allplots.append(hTotal)
                hTotal.SetTitle(histoName)
                hTotal.SetName(histoName)

                if yexpr:
                  filler = drawer.addPlot2D(hTotal, xexpr, yexpr, cutFullName)
                else:
                  filler = drawer.addPlot(hTotal, xexpr, cutFullName)

              if reweight is not None:
                filler.setReweight(reweight)
                  
              for nuisanceName, nuisance in applicableNuisances.iteritems():
                if nuisanceName == 'stat' or 'kind' not in nuisance:
                  continue

                configurationNuis = nuisance['samples'][sampleName]

                for idir, (ndrawers, variation) in enumerate([(drawersNuisanceUp, 'Up'), (drawersNuisanceDown, 'Down')]):
                  if nuisance['kind'] == 'tree':
                    try:
                      ndrawer = ndrawers[nuisanceName]
                    except KeyError:
                      # nuisance drawer for the specific sample may not exist if there is no nuisance tree corresponding to the nominal
                      # can be the case e.g. for UE and PS trees with FilesPerJob = 1
                      continue

                    reweightNuis = reweight

                  elif nuisance['kind'] == 'weight':
                    reweightNuis = ROOT.multidraw.ReweightSource(configurationNuis[idir])
                    if reweight is not None:
                      # compound reweight
                      reweightNuis = ROOT.multidraw.ReweightSource(reweight, reweightNuis)

                    ndrawer = drawer

                  subsampleNameNuis = subsampleName + '_' + nuisance['name'] + variation

                  if 'categories' in cut:
                    histlistNuis = ROOT.TObjArray()
  
                    for catname in categoryOrdering:
                      ROOT.gROOT.cd(cutName + '_' + catname + '/' + variableName)
  
                      histoNameNuis = 'histo_' + subsampleNameNuis
                      hTotalNuis = self._makeshape(histoNameNuis, variable['range'])
                      _allplots.append(hTotalNuis)
                      hTotalNuis.SetTitle(histoNameNuis)
                      hTotalNuis.SetName(histoNameNuis)
                      histlistNuis.Add(hTotalNuis)

                    if yexpr:
                      filler = ndrawer.addPlotList2D(histlistNuis, xexpr, yexpr, cutFullName)
                    else:
                      filler = ndrawer.addPlotList(histlistNuis, xexpr, cutFullName)
                    
                  else:
                    ROOT.gROOT.cd(cutName + '/' + variableName)
  
                    histoNameNuis = 'histo_' + subsampleNameNuis
                    hTotalNuis = self._makeshape(histoNameNuis, variable['range'])
                    _allplots.append(hTotalNuis)
                    hTotalNuis.SetTitle(histoNameNuis)
                    hTotalNuis.SetName(histoNameNuis)
    
                    if yexpr:
                      filler = ndrawer.addPlot2D(hTotalNuis, xexpr, yexpr, cutFullName)
                    else:
                      filler = ndrawer.addPlot(hTotalNuis, xexpr, cutFullName)

                  if reweightNuis is not None:
                    filler.setReweight(reweightNuis)

            # Done setting up one cut
            print ''

          # We now defined all plots for this sample - execute the drawers and fill the histograms
          print 'Start nominal histogram fill'
          drawer.execute(nevents, firstEvent)
          # We don't need this drawer any more - can reduce the number of open FDs?
          del drawer

          for ndrawers, variation in [(drawersNuisanceUp, 'Up'), (drawersNuisanceDown, 'Down')]:
            for nuisanceName, ndrawer in ndrawers.iteritems():
              print 'Start', nuisanceName + variation, 'histogram fill'
              ndrawer.execute(nevents, firstEvent)

          drawersNuisanceUp = None
          drawersNuisanceDown = None

          print 'Postfill'
          
          # Post-processing
          for cutKey, cut in cuts.iteritems():
            if type(cutKey) is tuple:
              ssName, cutName = cutKey
              subsampleName = sampleName + '_' + ssName
              cutFullName = '%s__%s' % cutKey
              print "  subsample/cut =", '%s/%s' % cutKey, "::", cut['expr']
            else:
              cutName = cutKey
              subsampleName = sampleName
              cutFullName = cutName
              print "  cut = ", cutFullName, " :: ", cut['expr']

            histoName = 'histo_' + subsampleName

            for variableName, variable in self._variables.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              if 'cuts' in variable and cutName not in variable['cuts']:
                continue

              if 'categories' in cut:
                # 'categories' is either a list (use elements) or dict (use keys)
                catsuffixes = ['_' + catname for catname in cut['categories']]
              else:
                catsuffixes = ['']

              for catsuffix in catsuffixes:
                hTotal = ROOT.gROOT.Get(cutName + catsuffix + '/' + variableName + '/' + histoName)

                # fold if needed
                if 'fold' in variable:
                  print '   ', cutName + catsuffix + '/' + variableName + '/' + histoName
                  print "    variable[fold] = ", variable['fold']
                  doFold = variable['fold']
                else:
                  doFold = 0

                outputsHisto = self._postplot(hTotal, doFold, cutName, sample, True)
                if outputsHisto is not hTotal:
                  _allplots.append(outputsHisto)
                  _allplots.remove(hTotal)
              
                for nuisanceName, nuisance in nuisances.iteritems():
                  if sampleName not in nuisance['samples'] or \
                     ('cuts' in nuisance and cutName not in nuisance['cuts']):
                    continue

                  configurationNuis = nuisance['samples'][sampleName]
                    
                  if nuisanceName == 'stat':
                    # 'stat' has a separate treatment, it's the MC/data statistics
                    # prepare nuisance MC/data statistics
                    # - uniform
                    # - uniform method 2
                    # - bin by bin (in selected bins)
                    # run only if this nuisance will affect the phase space defined in "cut"
            
                    if configurationNuis['typeStat'] == 'uni' :
                      #print "     >> uniform"
                      # take histogram --> outputsHisto
                      outputsHistoUp = outputsHisto.Clone("histo_"+sampleName+"_statUp")
                      outputsHistoDo = outputsHisto.Clone("histo_"+sampleName+"_statDown")
                      # scale up/down
                      self._scaleHistoStat (outputsHistoUp,  1 )
                      self._scaleHistoStat (outputsHistoDo, -1 )
                
                    # bin-by-bin
                    elif configurationNuis['typeStat'] == 'bbb' :
                      #print "     >> bin-by-bin"
                      keepNormalization = 0 # do not keep normalization, put 1 to keep normalization                       
                      if 'keepNormalization' in configurationNuis.keys() :
                        keepNormalization = configurationNuis['keepNormalization']
                        print " keepNormalization = ", keepNormalization
            
                      # scale up/down
                      zeroMC = False
                      if  configurationNuis['zeroMCError'] == '1' : zeroMC = True
            
                      for iBin in range(1, outputsHisto.GetNbinsX()+1):
                        # take histogram --> outputsHisto
                        outputsHistoUp = outputsHisto.Clone("histo_" + sampleName + "_ibin_" + str(iBin) + "_statUp")
                        outputsHistoDo = outputsHisto.Clone("histo_" + sampleName + "_ibin_" + str(iBin) + "_statDown")
                        #print "########### DEBUG: scaleHistoStatBBB sample", sampleName
                        self._scaleHistoStatBBB (outputsHistoUp,  1, iBin, keepNormalization, zeroMC)
                        self._scaleHistoStatBBB (outputsHistoDo, -1, iBin, keepNormalization, zeroMC)
            
                        # fix negative bins not consistent
                        self._fixNegativeBin(outputsHistoUp, outputsHisto)
                        self._fixNegativeBin(outputsHistoDo, outputsHisto)
            
                  # if nuisanceName == 'stat'
                  else:
                    if 'kind' not in nuisance:
                      continue

                    #print '     ', nuisanceName

                    subsampleNameUp = subsampleName + '_' + nuisance['name'] + 'Up'
                    subsampleNameDown = subsampleName + '_' + nuisance['name'] + 'Down'

                    histoNameUp = 'histo_' + subsampleNameUp
                    histoNameDown = 'histo_' + subsampleNameDown
  
                    hTotalUp = ROOT.gROOT.Get(cutName + catsuffix + '/' + variableName + '/' + histoNameUp)
                    hTotalDown = ROOT.gROOT.Get(cutName + catsuffix + '/' + variableName + '/' + histoNameDown)
  
                    outputsHistoUp = self._postplot(hTotalUp, doFold, cutName, sample, False)
                    outputsHistoDo = self._postplot(hTotalDown, doFold, cutName, sample, False)
  
                    if outputsHistoUp is not hTotalUp:
                      _allplots.append(outputsHistoUp)
                      _allplots.remove(hTotalUp)
                    if outputsHistoDo is not hTotalDown:
                      _allplots.append(outputsHistoDo)
                      _allplots.remove(hTotalDown)

                    if nuisance['kind'] == 'tree':      
                      # check if I need to symmetrize:
                      #    - the up will be symmetrized
                      #    - down ->   down - (up - down)
                      #    - if we really want to symmetrize, typically the down fluctuation is set to be the default
                      if 'symmetrize' in nuisance:
                        self._symmetrize(outputsHistoUp, outputsHistoDo)
            
                    if 'suppressNegativeNuisances' in sample.keys() and (cutName in sample['suppressNegativeNuisances'] or 'all' in sample['suppressNegativeNuisances']):
                      # fix negative bins not consistent
                      self._fixNegativeBin(outputsHistoUp, outputsHisto)
                      self._fixNegativeBin(outputsHistoDo, outputsHisto)

          # end of one sample
          print ''

        print 'Writing histograms to', self._outputFileName

        dtemp = tempfile.mkdtemp()
        tmpPath = dtemp + '/' + os.path.basename(self._outputFileName)
        outFile = ROOT.TFile.Open(tmpPath, 'recreate')
        # Speed up TFile::Close - see https://root-forum.cern.ch/t/tfile-close-slow/24179
        ROOT.gROOT.GetListOfFiles().Remove(outFile)

        def fullpath(tdir):
          path = tdir.GetName()
          d = tdir.GetMother()
          while d:
            path = d.GetName() + '/' + path
            d = d.GetMother()
          path = '/' + path
          return path

        def writeDirectory(indir, outdir):
          for obj in indir.GetList():
            if obj.IsA() == ROOT.TDirectory.Class():
              outdir.mkdir(obj.GetName())
              writeDirectory(obj, outdir.GetDirectory(obj.GetName()))
            else:
              outdir.cd()
              obj.SetDirectory(outdir)
              obj.Write()
              obj.Delete()

        print 'Writing in-memory histograms to', tmpPath
        writeDirectory(ROOT.gROOT, outFile)
        print 'Closing', tmpPath
        outFile.Close()

        print 'Copying', tmpPath, 'to', self._outputFileName
        shutil.copyfile(tmpPath, self._outputFileName)
        shutil.rmtree(dtemp)

    # _____________________________________________________________________________
    def _symmetrize(self, hUp, hDo): 

        #print " >> fold underflow"
        if hUp.GetDimension() == 1:
          nx = hUp.GetNbinsX()
          for iBin in range(1, nx+1):
            valueUp = hUp.GetBinContent(iBin)
            valueDo = hDo.GetBinContent(iBin) 
            newValueDo = valueDo - (valueUp-valueDo)
            hDo.SetBinContent(iBin, newValueDo)
        else :
          print 'No way! I am not going to symmetrize something that is not already folded into 1D'
        

    # _____________________________________________________________________________
    def _filterTrees(self, global_weight, weights, cut, inputs, cutName, sampleName, evlists = []):       
        '''
        global_weight :   the global weight for the samples
        weights       :   the wieghts 'root file' dependent
        cut           :   the selection
        inputs        :   the list of input files for this particular sample
        '''
        self._logger.info('filter Trees to speed up')
        #print "_filterTrees cut = ",cut
        numTree = 0

        for itree, tree in enumerate(inputs):
          globalCut = "(" + cut + ") * (" + global_weight + ")"  
          #print "_filterTrees globalCut = ",globalCut
          # if weights vector is not given, do not apply file dependent weights
          if len(weights) != 0 :
            # if weight is not given for a given root file, '-', do not apply file dependent weight for that root file
            if weights[numTree] != '-' :
              globalCut = "(" + globalCut + ") * (" +  weights[numTree] + ")" 
          
          #print " '>> myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName = ", '>> myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName
          #print " ::: ", tree.GetEntries(),
          # clear list
          # GIULIO do not clear the pruner list
          tree.SetEntryList(0)
          # get the list
          if len(evlists):
            print "applying the following event list to the input tree", tree.GetFile().GetName()
            evlists[itree].Print()
            tree.SetEventList(evlists[itree])
          myList = ROOT.TEventList('myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName,"")
          #myList = ROOT.TEntryList('myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName,"")
          #myList = ROOT.TEntryList(tree)
          #tree.Draw('>> myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName, globalCut, "entrylist");
          tree.Draw('>> myList'+'_'+str(numTree)+'_'+sampleName+'_'+cutName, globalCut);
          #myList.Print("all")
          #gDirectory = ROOT.gROOT.GetGlobal("gDirectory")
          #gDirectory.Print()
          #myList = gDirectory.Get("myList")
          #myList.Print("all")
          # apply the list
          #print " BEFORE List --> ", tree.GetEntries()
          #tree.SetEntryList(myList)
          tree.SetEventList(myList)
          #print " AFTER List --> ", tree.GetEntries()
          print "filtered."   
          numTree += 1

    # _____________________________________________________________________________
    def _postplot(self, hTotal, doFold, cutName, sample, fixZeros):
        if doFold == 1 or doFold == 3 :
          self._FoldOverflow(hTotal)
        if doFold == 2 or doFold == 3 :
          self._FoldUnderflow(hTotal)
  
        # go 1d
        hTotalFinal = self._h2toh1(hTotal)
  
        # fix negative (almost never happening)
        # don't do it here by default, because you may have interference that is actually negative!
        # do this only if triggered: use with caution!
        # This also checks that only in specific phase spaces this is activated, "cutName"
        #
        # To be used with caution -> do not use this option if you don't know what you are playing with
        #
        if fixZeros and 'suppressNegative' in sample and (cutName in sample['suppressNegative'] or 'all' in sample['suppressNegative']):
          self._fixNegativeBinAndError(hTotalFinal)

        return hTotalFinal


    def _FoldUnderflow(self, h):       

        #print " >> fold underflow"
        if h.GetDimension() == 1:
          nx = h.GetNbinsX()
          # 0 --> 1
          ShapeFactory._moveAddBin(h, (0,),(1,) )
          return
        elif h.GetDimension() == 2:
          nx = h.GetNbinsX()
          ny = h.GetNbinsY()
          for i in xrange(1,nx+1):
            ShapeFactory._moveAddBin(h,(i,0   ),(i, 1 ) )

          for j in xrange(1,ny+1):
            ShapeFactory._moveAddBin(h,(0,    j),(1, j) )

          # 0,0 -> 1,1
          # 0,ny+1 -> 1,ny+1
          # nx+1,0 -> nx+1,1
          
          ShapeFactory._moveAddBin(h, (0,0),(1,1) )
          ShapeFactory._moveAddBin(h, (0,ny+1),(1,ny+1) )
          ShapeFactory._moveAddBin(h, (nx+1,0),(nx+1,1) )
          
        
        
    def _FoldOverflow(self, h):       

        #print " >> fold overflow"
        if h.GetDimension() == 1:
          nx = h.GetNbinsX()
          # n+1 --> n
          ShapeFactory._moveAddBin(h, (nx+1,),(nx,) )
          return
        elif h.GetDimension() == 2:
          nx = h.GetNbinsX()
          ny = h.GetNbinsY()
          for i in xrange(1,nx+1):
            ShapeFactory._moveAddBin(h,(i,ny+1),(i, ny) )

          for j in xrange(1,ny+1):
            ShapeFactory._moveAddBin(h,(nx+1, j),(nx,j) )

            # 0,ny+1 -> 0,ny
            # nx+1,0 -> nx,0
            # nx+1,ny+1 ->nx,ny

            ShapeFactory._moveAddBin(h, (0,ny+1),(0,ny) )
            ShapeFactory._moveAddBin(h, (nx+1,0),(nx,0) )
            ShapeFactory._moveAddBin(h, (nx+1,ny+1),(nx,ny) )


# --- transform 2D into 1D: unrolling
# 
#      3    6    9
#      2    5    8
#      1    4    7
#
    def _h2toh1(self, h):
        import array
        
        if not isinstance(h,ROOT.TH2):
            return h

        name = h.GetName()
        h.GetDirectory().cd()

#         H1class = getattr(ROOT,h.__class__.__name__.replace('2','1'))
        nx = h.GetNbinsX()
        ny = h.GetNbinsY()

        h_flat = ROOT.TH1D(name + '_tmpflat',name,nx*ny,0,nx*ny)
 
        sumw2 = h.GetSumw2()
        sumw2_flat = h_flat.GetSumw2()

        for i in xrange(1,nx+1):
            for j in xrange(1,ny+1):
                # i,j must be mapped in 
                b2d = h.GetBin( i,j )
#                 b2d = h.GetBin( j,i )
#                 b1d = ((i-1)+(j-1)*nx)+1
                b1d = ((j-1)+(i-1)*ny)+1

                h_flat.SetAt( h.At(b2d), b1d )
                sumw2_flat.SetAt( sumw2.At(b2d), b1d ) 

        h_flat.SetEntries(h.GetEntries())
        
        stats2d = array.array('d',[0]*7)
        h.GetStats(stats2d)

        stats1d = array.array('d',[0]*4)
        stats1d[0] = stats2d[0]
        stats1d[1] = stats2d[1]
        stats1d[2] = stats2d[2]+stats2d[4]
        stats1d[3] = stats2d[3]+stats2d[5]

        h_flat.PutStats(stats1d)

        xtitle = h.GetXaxis().GetTitle()
        #v1,v2 = xtitle.split(':') # we know it's a 2d filled by an expr like y:x
        #xtitle = '%s #times %s bin' % (v1,v2)

        h_flat.GetXaxis().SetTitle(xtitle)

        h.Delete()
        h_flat.SetName(name)

        return h_flat
       
    # _____________________________________________________________________________
    def _scaleHistoStat(self, histo, direction):
        
        for iBin in range(1, histo.GetNbinsX()+1):
          error = histo.GetBinError(iBin)
          value = histo.GetBinContent(iBin)
          newvalue = value + direction * error
          histo.SetBinContent(iBin, newvalue)
  
    # _____________________________________________________________________________
    def _scaleHistoStatBBB(self, histo, direction, iBinToChange, keepNormalization, zeroMC=False):
  

        integral = 0.
        integralVaried = 0.

        if zeroMC == False:
          for iBin in range(1, histo.GetNbinsX()+1):
            error = histo.GetBinError(iBin)
            value = histo.GetBinContent(iBin)
            integral += value
            if iBin == iBinToChange : 
              newvalue = value + direction * error
            else :
              newvalue = value            

            integralVaried += newvalue
            histo.SetBinContent(iBin, newvalue)

        else:
          # how to handle the case when you have a bin with 0 MC
          # if the flag is activated, put the equivalent FC coverage 1.64 * 1 MC for the up variation
          basew = self._getBaseW(histo)
          print "###DEBUG: Effective baseW = ", basew
          for iBin in range(1, histo.GetNbinsX()+1):
            error = histo.GetBinError(iBin)
            value = histo.GetBinContent(iBin)
            integral += value
            if iBin == iBinToChange :
              if value == 0:
                print "###DEBUG: 0 MC stat --> value = ", value, " error = ", error
                if direction == 1:
                  print "###DEBUG: lumi = ", float(self._lumi), " basew = ", basew
                  newvalue = 1.64*float(self._lumi)*basew
                  print "###DEBUG: new value up = ", newvalue
                else:
                  newvalue = 0
              else:
                newvalue = value + direction * error
            else :
              newvalue = value
            integralVaried += newvalue
            histo.SetBinContent(iBin, newvalue)

        if keepNormalization == 1 :
          if integralVaried != 0 :
            histo.Scale (integral / integralVaried)


    # _____________________________________________________________________________
    def _fixNegativeBin(self, histoNew, histoReference):
        # if a histogram has a bin >/< 0
        # than also the variation has to have the bin in the 
        # same sign, because combine cannot handle it otherwise!
       
        for ibin in range(1, histoNew.GetNbinsX()+1) :
          # Why ? 
          if histoNew.GetBinContent(ibin) * histoReference.GetBinContent(ibin) < 0 :
            histoNew.SetBinContent(ibin, histoReference.GetBinContent(ibin) * 0.0001)  # do not put 0 to avoid bogus pogus ...
          # I think this is correct fix to our BOGUS problem
	  if histoNew.GetBinContent(ibin) == 0 and not histoReference.GetBinContent(ibin) == 0 :
            histoNew.SetBinContent(ibin, histoReference.GetBinContent(ibin) * 0.0001)  # do not put 0 to avoid bogus pogus ...
          if not histoNew.GetBinContent(ibin) == 0 and histoReference.GetBinContent(ibin) == 0 :
            histoNew.SetBinContent(ibin, 0)

    # _____________________________________________________________________________
    def _fixNegativeBinAndError(self, histogram_to_be_fixed):
        # if a histogram has a bin < 0
        # then put the gin content to 0
        # and also if a histogram has uncertainties that go <0, 
        # then put the uncertainty to the maximum allowed
       
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
          if histogram_to_be_fixed.GetBinContent(ibin)  < 0 :
            histogram_to_be_fixed.SetBinContent(ibin, 0) 

        # the SetBinError does not allow asymmetric -> fine, maximum uncertainty set
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
          if histogram_to_be_fixed.GetBinContent(ibin) - histogram_to_be_fixed.GetBinErrorLow(ibin)  < 0 :
            histogram_to_be_fixed.SetBinError(ibin, histogram_to_be_fixed.GetBinContent(ibin))   


    # _____________________________________________________________________________
    def _getBaseW(self, histo):
 
      ### returns the effective baseW
      baseW = histo.Integral()/histo.GetEntries()/self._lumi if histo.GetEntries()>0 else 0

      ### old method 
      #tree.GetEntry(0)
      #baseW = eval("tree.baseW")     

      return baseW 

    # _____________________________________________________________________________
    @staticmethod
    def _moveAddBin(h, fromBin, toBin ):
        if not isinstance(fromBin,tuple) or not isinstance(toBin,tuple):
            raise ValueError('Arguments must be tuples')

        dims = [h.GetDimension(), len(fromBin), len(toBin) ]

        if dims.count(dims[0]) != len(dims):
            raise ValueError('histogram and the 2 bins don\'t have the same dimension')
        
        #print " h = " , h.GetTitle(), " --> ", h.GetNbinsX()
        
        # get bins
        b1 = h.GetBin( *fromBin )
        b2 = h.GetBin( *toBin )

        # move contents
        c1 = h.At( b1 )
        c2 = h.At( b2 )

        h.SetAt(0, b1)
        h.SetAt(c1+c2, b2)

        # move weights as well
        sumw2 = h.GetSumw2()

        w1 = sumw2.At( b1 )
        w2 = sumw2.At( b2 )

        sumw2.SetAt(0, b1)
        sumw2.SetAt(w1+w2, b2)


    # _____________________________________________________________________________
    @staticmethod
    def _bins2hclass( bins ):
        '''
        Fixed bin width
        bins = (nx,xmin,xmax)
        bins = (nx,xmin,xmax, ny,ymin,ymax)
        Variable bin width
        bins = ([x0,...,xn])
        bins = ([x0,...,xn],[y0,...,ym])  
        '''

        from array import array
        if not bins:
            return name,0
        elif not ( isinstance(bins, tuple) or isinstance(bins,list)):
            raise RuntimeError('bin must be an ntuple or an arrays')

        l = len(bins)
        # 1D variable binning
        if l == 1 and isinstance(bins[0],list):
            ndim=1
            hclass = ROOT.TH1D
            xbins = bins[0]
            hargs = (len(xbins)-1, array('d',xbins))
        elif l == 2 and  isinstance(bins[0],list) and  isinstance(bins[1],list):
            ndim=2
            hclass = ROOT.TH2D
            xbins = bins[0]
            ybins = bins[1]
            hargs = (len(xbins)-1, array('d',xbins),
                    len(ybins)-1, array('d',ybins))
        elif l == 3:
            # nx,xmin,xmax
            ndim=1
            hclass = ROOT.TH1D
            hargs = bins
        elif l == 6:
            # nx,xmin,xmax,ny,ymin,ymax
            ndim=2
            hclass = ROOT.TH2D
            hargs = bins
        else:
            # only 1d or 2 d hist
            raise RuntimeError('What a mess!!! bin malformed!')
        
        return hclass,hargs,ndim

    @staticmethod
    def _bins2dim(bins):
        hclass,hargs,ndim = ShapeFactory._bins2hclass( bins )
        return ndim

    @staticmethod
    def _makeshape( name, bins ):
        hclass,hargs,ndim = ShapeFactory._bins2hclass( bins )
        return hclass(name, name, *hargs)
      
    @staticmethod
    def _splitexpr(expr):
        """Split a y:x expression and return (x, y)"""
        pos = 0
        while pos < len(expr):
          pos = expr.find(':', pos)
          if pos == -1:
            break
          elif expr[pos + 1] == ':': #make sure this is not a double-colon
            pos += 2
          else:
            return expr[pos + 1:], expr[:pos]

        raise RuntimeError('Expression ' + expr + ' is not 2D')
 
    # _____________________________________________________________________________
    def _connectInputs(self, process, filenames, inputDir, skipMissingFiles, friendsDir = None, skimListDir = None):
	if "sdfarm" in os.uname()[1]:
	  inputDir = inputDir.replace("xrootd","xrd")

        print "  connectInputs from", inputDir

        print '  (%d files)' % len(filenames)

        drawer = ROOT.multidraw.MultiDraw(self._treeName)
        drawer.setWeightBranch('')
        drawer.setPrintLevel(1)
        drawer.setDoTimeProfile(True)
        drawer.setInputMultiplexing(int(self._nThreads))

        for name, alias in self.aliases.iteritems():
          if 'samples' in alias and process not in alias['samples']:
            continue

          drawer.addAlias(name, alias['expr'])

        # lists[process] = []
        
        # if the filenames start with "###" the folder will be reset
        # and the name of the tree will start directly from the "filename" listed
        # disregarding any "inputDir" given
        #    This is useful in case we need to use multiple eos folders,
        #    some of them under iteos, some under the standard eos          
       
        # use inputDir if no "###"           otherwise     just use f (after removing the "###" from the name)
        files = [(inputDir + '/' + f) if '###' not in f else f.replace("#", "") for f in filenames]
        nfiles = self._buildchain(drawer, files, skipMissingFiles)

        # if we specify a friends tree directory we need to load the friend trees and attch them 
        if friendsDir != None:
          files = [(friendsDir + '/' + f) if '###' not in f else f.replace("#", "") for f in filenames]
          self._buildchain(drawer, files, False, friendtree = self._treeName)

        #if we specify a directory with skim event lists we need to load them and skim    
        #if skimListDir != None:
        #  eventlists = self._geteventlists("prunerlist",  [(skimListDir + '/' + f)       if '###' not in f     else     f.replace("#", "")           for f in filenames])
        #  lists[process] = eventlists
        #  for itree, tree in enumerate(trees):
        #    print eventlists[itree]
        #    eventlists[itree].Print()
        #    tree.SetEventList(eventlists[itree])

        # FIXME: add possibility to add Friend Trees for new variables   

        return drawer

    # _____________________________________________________________________________
    def _testEosFile(self,path): 
      eoususer='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select'
      if 'eosuser.cern.ch' in path: 
        if os.system(eoususer+' ls '+path.split('/eosuser.cern.ch/')[1]+' >/dev/null 2>&1') == 0 : return True
      if 'eoscms.cern.ch' in path:
        if os.system('eos ls '+path.split('/eoscms.cern.ch/')[1]+' >/dev/null 2>&1') == 0 : return True 
      return False 

    # _____________________________________________________________________________
    def _testIiheFile(self,path): 
      if 'maite.iihe.ac.be' in path: 
        return os.path.exists(path.split('dcap://maite.iihe.ac.be/')[1])

    def _test_sdfarm_File(self,path): 
      if 'cms-xrdr.sdfarm.kr' in path:
	if 'xrd//store' in path:
	  cmd = 'xrd cms-xrdr.sdfarm.kr existfile /xrd/store/'+path.split('xrd//store/')[1]
	  #cmd = 'gfal-ls -l srm://cms-se.sdfarm.kr:8443/srm/v2/server?SFN=/xrootd/store/'+path.split('xrd//store/')[1]
	elif 'xrd/store' in path:
	  cmd = 'xrd cms-xrdr.sdfarm.kr existfile /xrd/store/'+path.split('xrd/store/')[1]
	  #cmd = 'gfal-ls -l srm://cms-se.sdfarm.kr:8443/srm/v2/server?SFN=/xrootd/store/'+path.split('xrd/store/')[1]
	else : return False
	print 'checking ', cmd
	if os.system(cmd) == 0 : return True 
	else: return False
      else: return False

    # _____________________________________________________________________________
    def _test_xrootdFile(self, path):
      xrdserver=path.lstrip("root://").split("/")[0]
      cmd='xrd '+xrdserver+' existfile '+path.split('root://'+xrdserver)[1]
      if os.system(cmd) == 0 : return True
      return False  

    # _____________________________________________________________________________
    def _buildchain(self, multidraw, files, skipMissingFiles, friendtree = None):
        if friendtree is not None:
          paths = []

        ntrees = 0

        for path in files:
          for att in range(5): # try opening the file 5 times
            doesFileExist = True

            self._logger.debug('     '+str(os.path.exists(path))+' '+path)

            if "eoscms.cern.ch" in path or "eosuser.cern.ch" in path:
              if not self._testEosFile(path):
                print 'File '+path+' doesn\'t exist'
                doesFileExist = False
            elif "maite.iihe.ac.be" in path:
              if not self._testIiheFile(path):
                print 'File '+path+' doesn\'t exist @ IIHE'
                doesFileExist = False
	    elif "cluster142.knu.ac.kr" in path:
	      pass # already checked the file at mkShape.py
            elif "sdfarm" in path:
              if not self._test_sdfarm_File(path):
                print 'File '+path+' doesn\'t exist @ sdfarm.kr'
                doesFileExist = False
            elif 'root://' in path:
              if not self._test_xrootdFile(path):
                print 'File '+path+' doesn\'t exist @ sdfarm.kr'
                doesFileExist = False 
            else:
              if not os.path.exists(path):
                print 'File '+path+' doesn\'t exist'
                doesFileExist = False

            if doesFileExist:
              if friendtree is not None:
                paths.append(path)
              else:
                multidraw.addInputPath(path)

              ntrees += 1
              break

            time.sleep(10)

          else: # exhausted all attempts
            if not skipMissingFiles:
              raise RuntimeError('File '+path+' doesn\'t exist')

          if friendtree is not None:
            objarr = ROOT.TObjArray()
            for path in paths:
              objarr.Add(ROOT.TObjString(path))
              multidraw.addFriend(friendtree, objarr)

        return ntrees

    # _____________________________________________________________________________
    def _geteventlists(self, listName, files):
      lists = []
      if not hasattr(self, 'filesToKeepAround'):
        self.filesToKeepAround = []
      for path in files:
        doesFileExist = True
        self._logger.debug('     '+str(os.path.exists(path))+' '+path)
        if "eoscms.cern.ch" in path or "eosuser.cern.ch" in path:
          if not self._testEosFile(path):
            print 'File '+path+' doesn\'t exists'
            doesFileExist = False
            raise RuntimeError('File '+path+' doesn\'t exists')
        elif "maite.iihe.ac.be" in path:
          if not self._testIiheFile(path):
            print 'File '+path+' doesn\'t exists @ IIHE'
            doesFileExist = False
            raise RuntimeError('File '+path+' doesn\'t exists')
        elif "cluster142.knu.ac.kr" in path:
          pass # already checked the file at mkShape.py
        else:
          if not os.path.exists(path):
            print 'File '+path+' doesn\'t exists'
            doesFileExist = False
            raise RuntimeError('File '+path+' doesn\'t exists')
        self.filesToKeepAround.append(ROOT.TFile(path))
        evlist = self.filesToKeepAround[-1].Get(listName)
        lists.append(evlist)

      return lists
        

