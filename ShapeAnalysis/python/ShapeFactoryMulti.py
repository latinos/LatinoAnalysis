#!/usr/bin/env python

import ROOT
import copy
import os.path
import shutil
import time
import collections
import tempfile
import subprocess
import logging
import numpy as np
import root_numpy as rnp
from array import array

ROOT.ROOT.EnableThreadSafety()

ROOT.gSystem.Load('libLatinoAnalysisMultiDraw.so')
try:
  ROOT.multidraw.MultiDraw
except:
  raise RuntimeError('Failed to load libMultiDraw')

import LatinoAnalysis.Tools.userConfig as userConfig
from LatinoAnalysis.NanoGardener.data.BranchMapping_cfg import branch_mapping

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

        #in case some aliases need a compiled function
        for aliasName, alias in self.aliases.iteritems():
          if alias.has_key('linesToAdd'):
            linesToAdd = alias['linesToAdd']
            for line in linesToAdd:
              ROOT.gROOT.ProcessLineSync(line)

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
          outputFileName = outputDir+'/plots_'+self._tag+"_"+str(number)+".root"
        else :
          outputFileName = outputDir+'/plots_'+self._tag+".root"

        print " outputFileName = ", outputFileName
        os.system ("mkdir -p " + outputDir + "/")

        ROOT.TH1.SetDefaultSumw2(True)

        #---- Open the output file and create the ROOT directory structure
        dtemp = tempfile.mkdtemp()
        tmpPath = dtemp + '/' + os.path.basename(outputFileName)
        outFile = ROOT.TFile.Open(tmpPath, 'recreate')
        # Speed up TFile::Close - see https://root-forum.cern.ch/t/tfile-close-slow/24179
        ROOT.gROOT.GetListOfFiles().Remove(outFile)

        print ''
        print '  <cuts>'
        for cutName, cut in self._cuts.iteritems():
          print "cut = ", cutName, " :: ", self._cuts[cutName]
          if type(cut) is dict and 'categories' in cut:
            for catname in cut['categories']:
              outFile.mkdir(cutName + '_' + catname)

              for variableName, variable in self._variables.iteritems():
                if 'cuts' not in variable or cutName in variable['cuts'] or cutName + '/' + catname in variable['cuts']:
                  outFile.mkdir(cutName+"_"+catname+"/"+variableName)

          else:
            outFile.mkdir(cutName)

            for variableName, variable in self._variables.iteritems():
              if 'cuts' not in variable or cutName in variable['cuts']:
                outFile.mkdir(cutName+"/"+variableName)

        #---- just print the variables
        print ''
        print '  <variables>'
        for variableName, variable in self._variables.iteritems():
          line = "    variable = " + variableName + " :: "
          if 'name' in variable:
            line += str(variable['name'])
          elif 'class' in variable:
            line += variable['class']
          elif 'tree' in variable:
            line += 'tree (%d branches)' % len(variable['tree'])
          print line
          if 'range' in variable:
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
        _allplots = set()

        print ''
        print '  <start histogram filling>'

        # One MultiDraw per sample = tree
        for sampleName, sample in self._samples.iteritems():
          print "    sample =", sampleName
          print "    name:", sample['name']
          #print "    weight:", sample['weight']

          if 'outputFormat' in sample:
            outputFormat = sample['outputFormat']
          else:
            outputFormat = '{sample}{subsample}{nuisance}'
          print "    outputFormat:", outputFormat

          if 'weights' not in sample:
            sample['weights'] = ['1'] * len(sample['name'])

          # label each tree as data / MC
          if 'isData' in sample:
            if len(sample['isData']) == 1 and sample['isData'][0] == 'all':
              # if you put 'all', all the root files are considered "data"
              isData = [True] * len(sample['name'])
            else:
              isData = []
              for iT in range(len(sample['name'])):
                try:
                  isData.append((int(sample['isData'][iT]) != 0))
                except IndexError:
                  isData.append(False)
          else:
            isData = [False] * len(sample['name'])

          treeweights = []
          if 'weights' in sample:
            lumiscale = None
            for iw, weight in enumerate(sample['weights']):
              treeweight = ShapeFactory._make_reweight(weight)
              # add the lumi scale factor for MC trees
              if not isData[iw]:
                if lumiscale is None:
                  lumiscale = ROOT.multidraw.ReweightSource(str(self._lumi))

                treeweight = ROOT.multidraw.ReweightSource(treeweight, lumiscale)

              treeweights.append(treeweight)
          else:
            treeweights = [None] * len(sample['name'])

          if len(treeweights) != len(sample['name']):
            raise RuntimeError('Number of tree-by-tree weights doesn\'t match the number of trees')

          if type(sample['weight']) is list:
            # compound weight
            sampleweight = ShapeFactory._make_reweight(sample['weight'][0])
            for w in sample['weight'][1:]:
              sampleweight = ROOT.multidraw.ReweightSource(sampleweight, ShapeFactory._make_reweight(w))
          else:
            sampleweight = ShapeFactory._make_reweight(sample['weight'])

          # Create the nominal drawer

          drawer = self._connectInputs(sampleName, sample['name'], inputDir, skipMissingFiles=False)

          # Create the drawers for tree- and map-type nuisances

          nuisanceDrawers = {}
          ndrawers = [] # flat list for convenience

          basenames = [os.path.basename(s) if '###' in s else s for s in sample['name']]

          for nuisanceName, nuisance in nuisances.iteritems():
            if 'kind' not in nuisance:
              continue

            nkind = nuisance['kind']

            if not (nkind.startswith('tree') or nkind.startswith('suffix') or nkind.startswith('branch_custom')): ##
              continue

            if sampleName not in nuisance['samples']:
              continue

            twosided = ('OneSided' not in nuisance or not nuisance['OneSided'])
            nuisanceDrawers[nuisanceName] = collections.OrderedDict()

            if nkind == 'tree' or nkind == 'suffix' or nkind == 'branch_custom': ##jhchoi
              if twosided:
                variations = ['Up', 'Down']
              else:
                variations = ['Up']
            else:
              variations = ['V%dVar' % ivar for ivar in range(len(nuisance['samples'][sampleName]))]

            skipMissing = ('synchronized' in nuisance and not nuisance['synchronized'])
            if 'nominalAsAlt' in nuisance and nuisance['nominalAsAlt']:
              # Workaround for missing nuisance files - don't use this regularly!
              if sample['name'][0].startswith('###'):
                altDir = os.path.dirname(sample['name'][0].replace('###', ''))
              else:
                altDir = inputDir
            else:
              altDir = ''

            if nkind.startswith('tree'):
              # Sept 2017
              # Tree kind nuisances can be hanndled in two ways:
              # usual way: a full tree for the variation up and a full tree for the variation down
              # This behavior is activated by the presence in the nuisances.py file of the tags 'folderUp' and 'folderDown'
              # alternative way: a combination of trees holding only the varied branches and the central tree for all the unvaried branches.
              # This behavior is activated by the presence in the nuisances.py file of the tags: 'unskimmedFolderUp', 'unskimmedFolderDown', 'unskimmedFriendTreeDir'.
              # Note that one has to use trees before skimming. The skimming can be applied on top is the additional tags 'skimListFolderUp' and 'skimListFolderDown'
              # are present. These tags hold the path to the directories holding the files holding the "prunerlist" event list

              for var in variations:
                if 'folder' + var in nuisance:
                  if 'unskimmedFriendTreeDir' in nuisance.keys():
                    unskimmedFriendsDir = nuisance['unskimmedFriendTreeDir']
    
                    try:
                      skimListFolderVar = nuisance['skimListFolder' + var]
                    except KeyError:
                      skimListFolderVar = None
    
                    ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, basenames, nuisance['unskimmedFolder' + var], skipMissingFiles=skipMissing, friendsDir=(unskimmedFriendsDir, nuisanceName + var), skimListDir=skimListFolderVar, altDir=altDir)
    
                  else:
                    ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, basenames, nuisance['folder' + var], skipMissingFiles=skipMissing, altDir=altDir)
    
                elif 'files' + var in nuisance:
                  # TODO this feature is not fully working - I can't come up with a good way to assign variation files to batch jobs
                  ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, nuisance['files' + var][sampleName], '', skipMissingFiles=False)
                  
                ndrawers.append(ndrawer)

            elif nkind.startswith('suffix'):
              for var in variations:
                if 'folder' + var in nuisance:
                  friendAlias = nuisanceName + var
                  ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, sample['name'], inputDir, skipMissingFiles=False, friendsDir=(nuisance['folder' + var], friendAlias))
                  prefix = friendAlias + '.'
                else:
                  ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, sample['name'], inputDir, skipMissingFiles=False)
                  prefix = ''

                # there are various ways to set up branch mapping in NanoGardener, but in practice we use only the branches-suffix configuration
                bmap = branch_mapping[nuisance['map' + var]]
                for bname in bmap['branches']:
                  ndrawer.replaceBranch(bname, prefix + bname + bmap['suffix'])

                ndrawers.append(ndrawer)
            elif nkind.startswith('branch_custom'): ##[jhchoi]pick up sysbranch and sysfiles to replace given nominal
              print "--branch_custom--"
              for var in variations:
                
                friendAlias = nuisanceName + var
                ndrawer = nuisanceDrawers[nuisanceName][var] = self._connectInputs(sampleName, sample['name'], inputDir, skipMissingFiles=False, friendsDir=(nuisance['folder' + var], friendAlias))
                prefix = friendAlias+'.' ##read friendAlias as treename
                for From,To in nuisance['BrFromTo'+var].items(): ##nuisance['BrFromToUp]  : a dictionary whose key =From , value ; To
                  ndrawer.replaceBranch(From,prefix+To)
                  print "From=",From,"To",To
                ndrawers.append(ndrawer)
          # Filters and aliases

          drawer.setFilter(supercut)
          for ndrawer in ndrawers:
            ndrawer.setFilter(supercut)

          for aliasName, alias in self.aliases.iteritems():
            if 'samples' in alias and sampleName not in alias['samples']:
              continue

            if 'class' in alias:
              drawer.addAlias(aliasName, ShapeFactory._make_ttreefunction(alias))
            else:
              drawer.addAlias(aliasName, alias['expr'])

            if 'nominalOnly' in alias and alias['nominalOnly']:
              continue

            for ndrawer in ndrawers:
              if 'class' in alias:
                ndrawer.addAlias(aliasName, ShapeFactory._make_ttreefunction(alias))
              else:
                ndrawer.addAlias(aliasName, alias['expr'])

          # Set overall weights on the nominal drawer
          drawer.setReweight(sampleweight)

          for it, w in enumerate(treeweights):
            if w is not None:
              drawer.setTreeReweight(it, False, w)

          # Set overall weights on the nuisance up/down drawers
          for nuisanceName, ndrawers in nuisanceDrawers.iteritems():
            # tree-type nuisances can in addition have weights for up / down
            nuisance = nuisances[nuisanceName]
            sampleVarWeights = nuisance['samples'][sampleName]

            for ivar, (var, ndrawer) in enumerate(ndrawers.iteritems()):
              if float(sampleVarWeights[ivar]) != 1.:
                nuisanceShift = ShapeFactory._make_reweight(sampleVarWeights[ivar])
                nuisanceweight = ROOT.multidraw.ReweightSource(sampleweight, nuisanceShift)
              else:
                nuisanceweight = sampleweight

              ndrawer.setReweight(nuisanceweight)

              # if the nuisance drawer is built from independent files, length of chain can be
              # different from the length of tree weights
              tocheck = 'files' + var
              if tocheck in nuisances[nuisanceName] and len(nuisances[nuisanceName][tocheck][sampleName]) != len(treeweights):
                warnIfTreeWeight = True
              else:
                warnIfTreeWeight = False

              for it, w in enumerate(treeweights):
                if w is not None:
                  ndrawer.setTreeReweight(it, False, w)
                  if warnIfTreeWeight:
                    print 'Nuisance', nuisanceName, 'tree filler for sample', sampleName, 'has different number of trees from the nominal filler. Tree-based reweighting may cause problems.'
                    warnIfTreeWeight = False

          # Set up cuts

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
              slabel = '_' + ssName
              cutFullName = '%s__%s' % cutKey
              print "    subsample/cut =", '%s/%s' % cutKey, "::", cut['expr']
            else:
              cutName = cutKey
              slabel = ''
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

              # setup cuts for tree-type nuisances
              if nuisanceName in nuisanceDrawers:
                for ndrawer in nuisanceDrawers[nuisanceName].itervalues():
                  ndrawer.addCut(cutFullName, cut['expr'])
                  if 'categorization' in cut:
                    ndrawer.setCategorization(cutFullName, cut['categorization'])
                  else:
                    for catname in categoryOrdering:
                      ndrawer.addCategory(cutFullName, cut['categories'][catname])

            # now loop over all the variables ...
            for variableName, variable in self._variables.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              if 'cuts' in variable and cutName not in variable['cuts']:
                continue

              # create histogram
              if 'name' in variable:
                self._logger.debug('Formula: '+str(variable['name']))
              elif 'class' in variable:
                self._logger.debug('Class: '+str(variable['class']))
              self._logger.debug('Cut:     '+cutFullName)

              if 'weight' in variable:
                reweight = ShapeFactory._make_reweight(variable['weight'])
              else:
                reweight = None

              if 'tree' in variable: # variable is actually a tree definition
                def setup_filler(drawer, reweight, variation=''):
                  if variation:
                    nlabel = '_' + variation
                  else:
                    nlabel = ''

                  treeName = 'tree_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=nlabel)

                  if 'categories' in cut:
                    treelist = ROOT.TObjArray()

                    for catname in categoryOrdering:
                      outFile.cd(cutName + '_' + catname + '/' + variableName)

                      tree = ROOT.TTree(treeName, treeName)
                      _allplots.add(tree)
                      treelist.Add(tree)

                    filler = drawer.addTreeList(treelist, cutFullName)

                  else:
                    outFile.cd(cutName + '/' + variableName)

                    tree = ROOT.TTree(treeName, treeName)
                    _allplots.add(tree)

                    filler = drawer.addTree(tree, cutFullName)

                  for bname in sorted(variable['tree'].iterkeys()):
                    filler.addBranch(bname, variable['tree'][bname])

                  if reweight is not None:
                    filler.setReweight(reweight)

                  return filler

              else: # variable is a real variable defined by an expression ('name') or an object ('class')
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

                elif 'class' in variable:
                  xexpr = ShapeFactory._make_ttreefunction(variable)
                  yexpr = ''

                def setup_filler(drawer, reweight, variation=''):
                  if variation:
                    nlabel = '_' + variation
                  else:
                    nlabel = ''

                  histoName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=nlabel)

                  if 'categories' in cut:
                    histlist = ROOT.TObjArray()

                    for catname in categoryOrdering:
                      outFile.cd(cutName + '_' + catname + '/' + variableName)

                      hTotal = self._makeshape(histoName, variable['range'])
                      _allplots.add(hTotal)
                      hTotal.SetTitle(histoName)
                      hTotal.SetName(histoName)
                      histlist.Add(hTotal)

                    if yexpr:
                      filler = drawer.addPlotList2D(histlist, xexpr, yexpr, cutFullName)
                    else:
                      filler = drawer.addPlotList(histlist, xexpr, cutFullName)

                  else:
                    outFile.cd(cutName + '/' + variableName)

                    hTotal = self._makeshape(histoName, variable['range'])
                    _allplots.add(hTotal)
                    hTotal.SetTitle(histoName)
                    hTotal.SetName(histoName)

                    if yexpr:
                      filler = drawer.addPlot2D(hTotal, xexpr, yexpr, cutFullName)
                    else:
                      filler = drawer.addPlot(hTotal, xexpr, cutFullName)

                  if reweight is not None:
                    filler.setReweight(reweight)

                  return filler

              # end "if 'tree' in variable: ... else: ..."

              nominal_filler = setup_filler(drawer, reweight)

              for nuisanceName, nuisance in applicableNuisances.iteritems():
                if nuisanceName == 'stat' or 'kind' not in nuisance:
                  continue

                sampleVarWeights = nuisance['samples'][sampleName]

                if nuisanceName in nuisanceDrawers:
                  for var, ndrawer in nuisanceDrawers[nuisanceName].iteritems():
                    setup_filler(ndrawer, reweight, nuisance['name'] + var)

                else:
                  if nuisance['kind'] == 'weight':
                    variations = ['Up']
                    if 'OneSided' not in nuisance or not nuisance['OneSided']:
                      variations.append('Down')
                  else:
                    variations = ['V%dVar' % ivar for ivar in range(len(sampleVarWeights))]

                  for ivar, var in enumerate(variations):
                    if 'tree' in variable:
                      # add a reweighting branch to the nominal tree instead of creating an entirely new tree with only the weight branch modified
                      nominal_filler.addBranch('reweight_' + nuisance['name'] + var, sampleVarWeights[ivar])
                    else:
                      reweightNuis = ROOT.multidraw.ReweightSource(sampleVarWeights[ivar])
                      if reweight is not None:
                        # compound reweight
                        reweightNuis = ROOT.multidraw.ReweightSource(reweight, reweightNuis)

                      setup_filler(drawer, reweightNuis, nuisance['name'] + var)

            # Done setting up one cut
            print ''

          # We now defined all plots for this sample - execute the drawers and fill the histograms

          # make a scratch ROOT file for MultiDraw aliases tree
          with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            pass
          tmpROOTFile = ROOT.TFile.Open(tmpfile.name, 'recreate')
          tmpROOTFile.cd()

          print 'Start nominal histogram fill'
          drawer.execute(nevents, firstEvent)

          # tree-type nuisances
          for nuisanceName in nuisanceDrawers.keys():
            ndrawers = nuisanceDrawers.pop(nuisanceName)
            for var, ndrawer in ndrawers.iteritems():
              print 'Start', nuisanceName + var, 'histogram fill'
              ndrawer.execute(nevents, firstEvent)

          tmpROOTFile.Close()
          os.unlink(tmpfile.name)

          print 'Postfill'

          # Post-processing
          for cutKey, cut in cuts.iteritems():
            if type(cutKey) is tuple:
              ssName, cutName = cutKey
              slabel = '_' + ssName
              cutFullName = '%s__%s' % cutKey
              print "  subsample/cut =", '%s/%s' % cutKey, "::", cut['expr']
            else:
              cutName = cutKey
              slabel = ''
              cutFullName = cutName
              print "  cut = ", cutFullName, " :: ", cut['expr']

            histoName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='')

            for variableName, variable in self._variables.iteritems():
              if 'tree' in variable:
                continue

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
                outDir = outFile.GetDirectory(cutName + catsuffix + '/' + variableName)
                outDir.cd()

                # fold if needed
                if 'fold' in variable:
                  print '   ', cutName + catsuffix + '/' + variableName + '/' + histoName
                  print "    variable[fold] = ", variable['fold']
                  doFold = variable['fold']
                else:
                  doFold = 0

                unroll2d = 'unroll' not in variable or variable['unroll']

                hTotal = outDir.Get(histoName)

                _allplots.remove(hTotal)
                outputsHisto = self._postplot(hTotal, doFold, cutName, sample, True, unroll2d=unroll2d)
                _allplots.add(outputsHisto)

                for nuisanceName, nuisance in nuisances.iteritems():
                  if sampleName not in nuisance['samples'] or \
                     ('cuts' in nuisance and cutName not in nuisance['cuts']):
                    continue

                  twosided = ('OneSided' not in nuisance or not nuisance['OneSided'])

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

                      upName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='_statUp')
                      downName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='_statDown')
                      outputsHistoUp = outputsHisto.Clone(upName)
                      outputsHistoDo = outputsHisto.Clone(downName)
                      _allplots.add(outputsHistoUp)
                      _allplots.add(outputsHistoDo)
                      # scale up/down
                      self._scaleHistoStat(outputsHistoUp,  1)
                      self._scaleHistoStat(outputsHistoDo, -1)

                    # bin-by-bin
                    elif configurationNuis['typeStat'] == 'bbb' :
                      #print "     >> bin-by-bin"
                      keepNormalization = 'keepNormalization' in configurationNuis and int(configurationNuis['keepNormalization'])
                      print " keepNormalization = ", keepNormalization
                      zeroMC = 'zeroMCError' in configurationNuis and int(configurationNuis['zeroMCError'])

                      for iBin in range(1, rnp.hist2array(outputsHisto, copy=False).size + 1):
                        # take histogram --> outputsHisto
                        upName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='_ibin_%d_statUp' % iBin)
                        downName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='_ibin_%d_statDown' % iBin)
                        outputsHistoUp = outputsHisto.Clone(upName)
                        outputsHistoDo = outputsHisto.Clone(downName)
                        _allplots.add(outputsHistoUp)
                        _allplots.add(outputsHistoDo)
                        #print "########### DEBUG: scaleHistoStatBBB sample", sampleName
                        self._scaleHistoStatBBB(outputsHistoUp,  1, iBin, keepNormalization, zeroMC)
                        self._scaleHistoStatBBB(outputsHistoDo, -1, iBin, keepNormalization, zeroMC)

                        # fix negative bins not consistent
                        self._fixNegativeBin(outputsHistoUp, outputsHisto)
                        self._fixNegativeBin(outputsHistoDo, outputsHisto)

                    continue

                  if 'kind' not in nuisance:
                    continue

                  if nuisance['kind'].endswith('_envelope') or nuisance['kind'].endswith('_rms'):
                    for ivar in range(len(configurationNuis)):
                      histoNameVar = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sV%dVar' % (nuisance['name'], ivar)))
                      hTotalVar = outDir.Get(histoNameVar)
                      _allplots.remove(hTotalVar)
                      outputsHistoVar = self._postplot(hTotalVar, doFold, cutName, sample, False, unroll2d=unroll2d)
                      _allplots.add(outputsHistoVar)
                      
                    continue

                  histoNameUp = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sUp' % nuisance['name']))
                  histoNameDown = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sDown' % nuisance['name']))

                  hTotalUp = outDir.Get(histoNameUp)
                  _allplots.remove(hTotalUp)
                  outputsHistoUp = self._postplot(hTotalUp, doFold, cutName, sample, False, unroll2d=unroll2d)
                  _allplots.add(outputsHistoUp)

                  if twosided:
                    hTotalDown = outDir.Get(histoNameDown)
                    _allplots.remove(hTotalDown)
                    outputsHistoDo = self._postplot(hTotalDown, doFold, cutName, sample, False, unroll2d=unroll2d)
                  else:
                    outputsHistoDo = outputsHisto.Clone(histoNameDown)

                  _allplots.add(outputsHistoDo)

                  # check if I need to symmetrize:
                  #    - the up will be symmetrized
                  #    - down ->   down - (up - down)
                  #    - if we really want to symmetrize, typically the down fluctuation is set to be the default
                  if 'symmetrize' in nuisance:
                    self._symmetrize(outputsHistoUp, outputsHistoDo)
  
                  if 'suppressNegativeNuisances' in sample and (cutName in sample['suppressNegativeNuisances'] or 'all' in sample['suppressNegativeNuisances']):
                    # fix negative bins not consistent
                    self._fixNegativeBin(outputsHistoUp, outputsHisto)
                    if twosided:
                      self._fixNegativeBin(outputsHistoDo, outputsHisto)


          # end of one sample
          print ''

        outFile.cd()
        outFile.Write()
        outFile.Close()

        print 'Copying', outFile.GetName(), 'to', outputFileName

        realOutDir = os.path.realpath(os.path.dirname(outputFileName))

        for _ in range(10):
          try:
            if realOutDir.startswith('/eos/cms'):
              cmd = ['xrdcp', '-f', outFile.GetName(), 'root://eoscms.cern.ch/' + realOutDir + '/' + os.path.basename(outputFileName)]
              print ' '.join(cmd)
              subprocess.Popen(cmd).communicate()
            else:
              shutil.copyfile(outFile.GetName(), outputFileName)
          except:
            continue
          else:
            break
        else:
          raise IOError('Failed to copy output')

        shutil.rmtree(os.path.dirname(outFile.GetName()))

    # _____________________________________________________________________________
    @staticmethod
    def _symmetrize(hUp, hDo):
      # What is this function doing?? Symmetrize with respect to what??
      
      vup = rnp.hist2array(hUp, copy=False)
      vdo = rnp.hist2array(hDo, copy=False)

      vdo[:] = (2. * vdo - vup).flat

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
    @staticmethod
    def _postplot(hTotal, doFold, cutName, sample, fixZeros, unroll2d=True):
        if doFold == 1 or doFold == 3:
          ShapeFactory._fold(hTotal, 0, 1)
        if doFold == 2 or doFold == 3 :
          ShapeFactory._fold(hTotal, -1, -2)

        if unroll2d and hTotal.InheritsFrom(ROOT.TH2.Class()):
          # --- transform 2D into 1D
          #
          #      3    6    9
          #      2    5    8
          #      1    4    7
          #
          # over/underflow are discarded
          hTotal2d = hTotal
          cwd = ROOT.gDirectory.GetDirectory('')
          hTotal2d.GetDirectory().cd()

          nx = hTotal2d.GetNbinsX()
          ny = hTotal2d.GetNbinsY()
          name = hTotal.GetName()
          hTotal2d.SetName(name + '_tmp')
          hTotal = ROOT.TH1D(name, hTotal.GetTitle(), nx * ny, 0., float(nx * ny))
          hTotal.GetXaxis().SetTitle(hTotal2d.GetXaxis().GetTitle())

          # contents
          cont = rnp.hist2array(hTotal2d, copy=False).reshape(-1)
          # array2hist for TH2 returns [x, y] arrays -> reshape -1 achieves the desired bin numbering
          rnp.array2hist(cont, hTotal)

          # sumw2
          # Sumw2 array follows the ROOT bin numbering (y-major)
          sumw22d = rnp.array(hTotal2d.GetSumw2(), copy=False).reshape((ny + 2, nx + 2))
          # chop off overflow and underflow bins
          sumw22d = sumw22d[1:-1, 1:-1]
          sumw2 = rnp.array(hTotal.GetSumw2(), copy=False)
          # transpose to change the bin numbering
          sumw2[1:-1] = sumw22d.T.flat

          # stats
          stats2d = ROOT.TArrayD(7)
          hTotal2d.GetStats(stats2d.GetArray())
          stats1d = ROOT.TArrayD(4)
          stats1d[0] = stats2d[0]
          stats1d[1] = stats2d[1]
          stats1d[2] = stats2d[2] + stats2d[4]
          stats1d[3] = stats2d[3] + stats2d[5]
          hTotal.PutStats(stats1d.GetArray())

          hTotal2d.Delete()

          cwd.cd()

        # fix negative (almost never happening)
        # don't do it here by default, because you may have interference that is actually negative!
        # do this only if triggered: use with caution!
        # This also checks that only in specific phase spaces this is activated, "cutName"
        #
        # To be used with caution -> do not use this option if you don't know what you are playing with
        #
        if fixZeros and 'suppressNegative' in sample and (cutName in sample['suppressNegative'] or 'all' in sample['suppressNegative']):
          ShapeFactory._fixNegativeBinAndError(hTotal)

        return hTotal

    @staticmethod
    def _fold(h, ifrom, ito):
      cont = rnp.hist2array(h, copy=False, include_overflow=True)
      sumw2 = rnp.array(h.GetSumw2(), copy=False)

      if h.GetDimension() == 1:
        cont[ito] += cont[ifrom]
        cont[ifrom] = 0.
        sumw2[ito] += sumw2[ifrom]
        sumw2[ifrom] = 0.

      elif h.GetDimension() == 2:
        cont[ito, :] += cont[ifrom, :]
        cont[ifrom, :] = 0.
        cont[:, ito] += cont[:, ifrom]
        cont[:, ifrom] = 0.

        # sumw2 is y-major
        nx = h.GetNbinsX()
        ny = h.GetNbinsY()
        sumw2 = np.reshape(sumw2, (ny + 2, nx + 2))
        sumw2[ito, :] += sumw2[ifrom, :]
        sumw2[ifrom, :] = 0.
        sumw2[:, ito] += sumw2[:, ifrom]
        sumw2[:, ifrom] = 0.

    # _____________________________________________________________________________
    @staticmethod
    def _scaleHistoStat(histo, direction):
      # .T ensures that cont will be in the same order as sumw2
      cont = rnp.hist2array(histo, copy=False, include_overflow=True).T
      sumw2 = rnp.array(histo.GetSumw2(), copy=False).reshape(cont.shape)
      cont += np.sqrt(sumw2) * direction

    # _____________________________________________________________________________
    def _scaleHistoStatBBB(self, histo, direction, iBinToChange, keepNormalization, zeroMC=False):
      cont = rnp.hist2array(histo, copy=False)

      integral = np.sum(cont)

      if cont.flat[iBinToChange - 1] == 0. and zeroMC and direction == 1:
        # how to handle the case when you have a bin with 0 MC
        # if the flag is activated, put the equivalent FC coverage 1.64 * 1 MC for the up variation
        if histo.GetEntries() > 0.:
          basew = histo.Integral() / histo.GetEntries() / self._lumi
        else:
          basew = 0.

        cont.flat[iBinToChange - 1] = 1.64 * float(self._lumi) * basew

      else:
        cont_uo = rnp.hist2array(histo, copy=False, include_overflow=True).T
        sumw2 = rnp.array(histo.GetSumw2(), copy=False).reshape(cont_uo.shape)
        # chop off the over/underflow bins and transpose to align the bin numbering with cont
        if len(sumw2.shape) == 2:
          sumw2 = sumw2[1:-1, 1:-1].T
        else:
          sumw2 = sumw2[1:-1]
        cont.flat[iBinToChange - 1] += direction * np.sqrt(sumw2.flat[iBinToChange - 1])

      if keepNormalization:
        integralVaried = np.sum(cont)
        if integralVaried != 0:
          cont *= integral / integralVaried

    # _____________________________________________________________________________
    @staticmethod
    def _fixNegativeBin(histoNew, histoReference):
      # if a histogram has a bin >/< 0
      # than also the variation has to have the bin in the
      # same sign, because combine cannot handle it otherwise!

      cnew = rnp.hist2array(histoNew, copy=False).flat
      cref = rnp.hist2array(histoReference, copy=False).flat

      indices = np.nonzero(cnew[:] * cref[:] <= 0.)[0]
      cnew[indices] = cref[indices] * 1.e-4

    # _____________________________________________________________________________
    @staticmethod
    def _fixNegativeBinAndError(histogram_to_be_fixed):
      # if a histogram has a bin < 0
      # then put the gin content to 0
      # and also if a histogram has uncertainties that go <0,
      # then put the uncertainty to the maximum allowed

      cont = rnp.hist2array(histogram_to_be_fixed, copy=False, include_overflow=True).T.flat
      sumw2 = rnp.array(histogram_to_be_fixed.GetSumw2(), copy=False).flat

      indices = np.nonzero(cont[:] < 0.)[0]
      cont[indices] = 0.

      indices = np.nonzero(cont[:] - np.sqrt(sumw2) < 0.)[0]
      sumw2[indices] = np.square(cont[indices])

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
    def _connectInputs(self, process, filenames, inputDir, skipMissingFiles, friendsDir=None, skimListDir=None, altDir=''):
	if "sdfarm" in os.uname()[1]:
	  inputDir = inputDir.replace("xrootd","xrd")

        print "  connectInputs from", inputDir

        print '  (%d files)' % len(filenames)

        drawer = ROOT.multidraw.MultiDraw(self._treeName)
        drawer.setWeightBranch('')
        drawer.setPrintLevel(1)
        drawer.setDoTimeProfile(True)
        drawer.setInputMultiplexing(int(self._nThreads))

        # lists[process] = []

        # if the filenames start with "###" the folder will be reset
        # and the name of the tree will start directly from the "filename" listed
        # disregarding any "inputDir" given
        #    This is useful in case we need to use multiple eos folders,
        #    some of them under iteos, some under the standard eos

        # use inputDir if no "###"           otherwise     just use f (after removing the "###" from the name)
        files = []
        for f in filenames:
          if '###' in f: # full path given
            files.append(f.replace('#', ''))
          else:
            files.append(inputDir + '/' + f)

        self._buildchain(drawer, files, skipMissingFiles, altDir=altDir)

        # if we specify a friends tree directory we need to load the friend trees and attch them
        if friendsDir is not None:
          # friendsDir is (directory, alias)
          files = [friendsDir[0] + '/' + os.path.basename(f) for f in filenames]
          self._buildchain(drawer, files, False, friendtree=(self._treeName, friendsDir[1]))

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
    def _testLocalFile(self,path):
      if not os.path.exists(path):
        return False

      try:
        f = ROOT.TFile.Open(path)
        if not f or f.IsZombie():
          return False
      finally:
        if f:
          f.Close()

      return True

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
    def _buildchain(self, drawer, files, skipMissingFiles, friendtree=None, altDir=''):
        def testFile(path):
          if "eoscms.cern.ch" in path or "eosuser.cern.ch" in path:
            exists = self._testEosFile(path)
            location = 'CERN'
          elif "maite.iihe.ac.be" in path:
            exists = self._testIiheFile(path)
            location = 'IIHE'
          elif "cluster142.knu.ac.kr" in path:
            # already checked the file at mkShape.py
            exists = True
            location = 'KNU'
          elif "sdfarm" in path:
            exists = self._test_sdfarm_File(path)
            location = 'sdfarm.kr'
          elif 'root://' in path:
            exists = self._test_xrootdFile(path)
            location = 'AAA'
          else:
            exists = self._testLocalFile(path)
            location = 'local'

          if not exists:
            print 'File '+path+' doesn\'t exist @', location

          return exists

        if friendtree is not None:
          paths = []

        ntrees = 0

        for path in files:
          for att in range(5): # try opening the file 5 times
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)

            exists = testFile(path)
            if not exists:
              if altDir and testFile(altDir + '/' + os.path.basename(path)):
                path = altDir + '/' + os.path.basename(path)
                exists = True

            if exists:
              if friendtree is not None:
                paths.append(path)
              else:
                drawer.addInputPath(path)

              ntrees += 1
              break

            elif skipMissingFiles:
              break

            time.sleep(10)

          else: # exhausted all attempts
            print 'File '+path+' doesn\'t exist and skipMissingFiles=False in buildChain.'
            print 'If you are trying to build a chain for a tree-based nuisance which has different number of'\
                ' files wrt nominal (e.g. UE and PS variations), set "synchronized": False in the nuisance specification.'
            raise RuntimeError('File '+path+' doesn\'t exist')

        if friendtree is not None:
          # friendtree is (treename, alias)
          objarr = ROOT.TObjArray()
          for path in paths:
            objarr.Add(ROOT.TObjString(path))
          drawer.addFriend(friendtree[0], objarr, friendtree[1])

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

    @staticmethod
    def _make_ttreefunction(expr):
      try:
        args = expr['args']
      except KeyError:
        args = tuple()
      else:
        if type(args) is not tuple:
          args = (args,)

      return getattr(ROOT, expr['class'])(*args)

    @staticmethod
    def _make_compiledsource(expr):
      func = ShapeFactory._make_ttreefunction(expr)
      return ROOT.multidraw.CompiledExprSource(func)

    @staticmethod
    def _make_reweight(weight):
      if type(weight) is str:
        return ROOT.multidraw.ReweightSource(weight)

      try:
        fname, _, objname = weight['source'].partition(':')
      except KeyError:
        wsource = None
      else:
        ftmp = ROOT.TFile.Open(fname)
        wsource = ftmp.Get(objname)
        try:
          wsource.SetDirectory(0)
        except:
          pass
        ftmp.Close()

      if 'class' in weight:
        expr = ShapeFactory._make_compiledsource(weight)
        return ROOT.multidraw.ReweightSource(expr, wsource)

      else:
        if 'expr' in weight:
          xexpr = weight['expr']
          yexpr = None
        else:
          xexpr = weight['xexpr']
          if 'yexpr' in weight:
            yexpr = weight['yexpr']
          else:
            yexpr = None

        if type(xexpr) is dict:
          xexpr = ShapeFactory._make_compiledsource(xexpr)
          if yexpr is not None:
            yexpr = ShapeFactory._make_compiledsource(yexpr)

        if yexpr is not None:
          return ROOT.multidraw.ReweightSource(xexpr, yexpr, wsource)
        else:
          return ROOT.multidraw.ReweightSource(xexpr, wsource)

    @staticmethod
    def postprocess_nuisance_variations(nuisance, samples, cuts, variables, outFile):
      twosided = ('OneSided' not in nuisance or not nuisance['OneSided'])

      for cutName, cut in cuts.iteritems():
        if 'cuts' in nuisance and cutName not in nuisance['cuts']:
          continue

        if 'categories' in cut:
            catsuffixes = ['_' + catname for catname in cut['categories']]
        else:
          catsuffixes = ['']

        for catsuffix in catsuffixes:
          for variableName, variable in variables.iteritems():
            if 'tree' in variable:
              continue
    
            if 'cuts' in variable and cutName not in variable['cuts']:
              continue

            dname = cutName + catsuffix + '/' + variableName
            outDir = outFile.GetDirectory(dname)
            outDir.cd()

            for sampleName, sample in samples.iteritems():
              if sampleName not in nuisance['samples']:
                continue

              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              configurationNuis = nuisance['samples'][sampleName]

              if 'outputFormat' in sample:
                outputFormat = sample['outputFormat']
              else:
                outputFormat = '{sample}{subsample}{nuisance}'
    
              if 'subsamples' in sample:
                slabels = list('_%s' % ss for ss in sample['subsamples'].iterkeys())
              else:
                slabels = ['']
    
              for slabel in slabels:
                histoName = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance='')
                nominal = outDir.Get(histoName)
                vnominal = rnp.hist2array(nominal, copy=False)

                variations = np.empty((len(configurationNuis), vnominal.size), dtype=vnominal.dtype)

                for ivar in range(len(configurationNuis)):
                  histoNameVar = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sV%dVar' % (nuisance['name'], ivar)))
                  hTotalVar = outDir.Get(histoNameVar)
                  variations[ivar, :] = rnp.hist2array(hTotalVar, copy=True).flat
                  if hasattr(userConfig, 'shapeFactoryDeleteVariations') and userConfig.shapeFactoryDeleteVariations:
                    outDir.Delete(histoNameVar + ';*')

                if nuisance['kind'].endswith('_envelope'):
                  arrup = np.max(variations, axis=0)
                  arrdown = np.min(variations, axis=0)

                elif nuisance['kind'].endswith('_rms'):
                  arrnom = np.tile(vnominal.flat, (variations.shape[0], 1))
                  arrv = np.sqrt(np.mean(np.square(variations - arrnom), axis=0))
                  arrup = vnominal.flat[:] + arrv
                  arrdown = vnominal.flat[:] - arrv

                arrup = arrup.reshape(vnominal.shape)
                arrdown = arrdown.reshape(vnominal.shape)

                histoNameUp = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sUp' % nuisance['name']))
                histoNameDown = 'histo_' + outputFormat.format(sample=sampleName, subsample=slabel, nuisance=('_%sDown' % nuisance['name']))

                outputsHistoUp = nominal.Clone(histoNameUp)
                rnp.array2hist(arrup, outputsHistoUp)
                outputsHistoUp.Write()
                outputsHistoDown = nominal.Clone(histoNameDown)
                if twosided:
                  rnp.array2hist(arrdown, outputsHistoDown)
                outputsHistoDown.Write()
