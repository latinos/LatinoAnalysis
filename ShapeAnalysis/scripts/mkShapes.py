#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
#import hwwinfo
#import hwwsamples
#import hwwtools
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
#from HWWAnalysis.Misc.ROOTAndUtils import TH1AddDirSentry
import traceback
from array import array



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):
        self._stdWgt = 'baseW*puW*effW*triggW'
        self._systByWeight = {}
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

        outputFile = {}
        self._outputFile = outputFile




    # _____________________________________________________________________________
    def __del__(self):
        pass

    # _____________________________________________________________________________
    def getvariable(self,tag,mass,cat):

        if tag in self._variables :
            try:
                theVariable = (self._variables[tag])(mass,cat)
            except KeyError as ke:
                self._logger.error('Variable '+tag+' not available. Possible values: '+', '.join(self._variables.iterkeys()) )
                raise ke
        else :
            theVariable = tag

        return theVariable


    # _____________________________________________________________________________
    def makeNominals(self, inputDir, outputDir, variables, cuts, samples):

        print "======================"
        print "==== makeNominals ===="
        print "======================"
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts
        
        
        self._outputFileName = outputDir+'/plots_'+self._tag+".root"
        print " outputFileName = ", self._outputFileName
        self._outFile = ROOT.TFile.Open( self._outputFileName, 'recreate')
        
        ROOT.TH1.SetDefaultSumw2(True)
        shapeFiles = []

        selections = "1"

        #---- first create structure in ourput root file
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          self._outFile.mkdir (cutName)
          for variableName, variable in self._variables.iteritems():
            self._outFile.mkdir (cutName+"/"+variableName)
            print "variable[name]  = ", variable ['name']
            print "variable[range] = ", variable ['range']
            #for nuisance in self._nuisances :
              #print "nuisance = ", nuisance
              # open the root file

       
        #---- now plot and save into output root file
        for cutName, cut in self._cuts.iteritems():
          print "cut = ", cutName, " :: ", cut
          for variableName, variable in self._variables.iteritems():
            print "variable[name]  = ", variable['name']
            print "variable[range] = ", variable['range']
            self._outFile.cd (cutName+"/"+variableName)
            for sampleName, sample in self._samples.iteritems():
              print "sample[name]    = ", sample ['name']
              print "sample[weight]  = ", sample ['weight']
              print "sample[weights] = ", sample ['weights']

              # get the weight
              # open the root file
              # plot
              # self._draw(doalias, rng, selections, output, inputs)
              # save histogram

                 #print 'Output file:',self._outputFile

                 # - then disconnect the files
                 #self._disconnectInputs(inputs)
                 #shapeFiles.append(output)
        
            #for nuisance in self._nuisances :
              #print "nuisance = ", nuisance
              #for sample in self._samples :
                 #print "sample = ", sample
                 
                 # get the weight
                 # open the root file
                 # plot
                 #self._draw(doalias, rng, selections, output, inputs)
                 # save histogram

                 #print 'Output file:',self._outputFile

                 # - then disconnect the files
                 #self._disconnectInputs(inputs)
                 #shapeFiles.append(output)
        #return shapeFiles


    
    # _____________________________________________________________________________
    def _draw(self, var, rng, selections, output, inputs):
        '''
        var :       the variable to plot
        selection : the selection to draw
        output :    the output file path
        inputs :    the process-input files map
        '''
        self._logger.info('Yields by process')
        print output
        outFile = ROOT.TFile.Open(output,'recreate')
        print outFile
        vdim = var.count(':')+1
#         hproto,hdim = ShapeFactory._projexpr(rng)
        # 3 items per dimention
        hdim = self._bins2dim( rng )

        if vdim != hdim:
            raise ValueError('The variable\'s and range number of dimensions are mismatching')

        #print 'selections = ', selections

        print 'var: '+var
        if 'WW' in selections : 
          print 'selection (for WW  as example): '+selections['WW']
        if 'WWlow' in selections : 
          print 'selection (for WWlow  as example): '+selections['WWlow']

        if 'WW1' in selections : 
          print 'selection (for WW1  as example): '+selections['WW1']

        if 'ggH' in selection :
          print 'selection (for ggH as example): '+selections['ggH']
        #print 'inputs = ', inputs

        for process,tree  in inputs.iteritems():
#             print ' '*3,process.ljust(20),':',tree.GetEntries(),
            print '    {0:<20} : {1:^9}'.format(process,tree.GetEntries()),
            # new histogram
            shapeName = 'histo_'+process
#             hstr = shapeName+hproto

            outFile.cd()

            # prepare a dummy to fill
            shape = self._makeshape(shapeName,rng)
            cut = selections[process]

            self._logger.debug('---'+process+'---')
            self._logger.debug('Formula: '+var+'>>'+shapeName)
            self._logger.debug('Cut:     '+cut)
            self._logger.debug('ROOTFiles:'+'\n'.join([f.GetTitle() for f in tree.GetListOfFiles()]))
            entries = tree.Draw( var+'>>'+shapeName, cut, 'goff')
#             print ' >> ',entries,':',shape.Integral()
            shape = outFile.Get(shapeName)
            shape.SetTitle(process+';'+var)


            if isinstance(shape,ROOT.TH2):
                shape2d = shape
                # puts the over/under flows in
                self._reshape( shape )
                # go 1d
                shape = self._h2toh1(shape2d)
                # rename the old
                shape2d.SetName(shape2d.GetName()+'_2d')
                shape2d.Write()
                shape.SetDirectory(outFile)

            print '>> {0:>9} : {1:>9.2f}'.format(entries,shape.Integral())
            shape.Write()
        outFile.Close()
        del outFile

 
    # _____________________________________________________________________________
    def _connectInputs(self, var, samples, dirmap, mask=None):
        inputs = {}
        treeName = 'latino'
        for process,filenames in samples.iteritems():
            if mask and process not in mask:
                continue
            tree = self._buildchain(treeName,[ (dirmap['base']+'/'+f) for f in filenames])
            if 'bdt' in var:
                bdttreeName = 'latinobdt'
                bdtdir = self._paths[var]
                bdttree = self._buildchain(bdttreeName,[ (dirmap[var]+'/'+f) for f in filenames])
                
                if tree.GetEntries() != bdttree.GetEntries():
                    raise RuntimeError('Mismatching number of entries: '
                                       +tree.GetName()+'('+str(tree.GetEntries())+'), '
                                       +bdttree.GetName()+'('+str(bdttree.GetEntries())+')')
                logging.debug('{0:<20} - master: {1:<20} friend {2:<20}'.format(process,tree.GetEntries(), bdttree.GetEntries()))
                tree.AddFriend(bdttree)

            inputs[process] = tree

        return inputs

    # _____________________________________________________________________________
    def _disconnectInputs(self,inputs):
        for n in inputs.keys():
            friends = inputs[n].GetListOfFriends()
            if friends.__nonzero__():
                for fe in friends:
                    friend = fe.GetTree()
                    inputs[n].RemoveFriend(friend)
                    ROOT.SetOwnership(friend,True)
                    del friend
            del inputs[n]
    
    # _____________________________________________________________________________
    def _buildchain(self,treeName,files):
        tree = ROOT.TChain(treeName)
        for path in files:
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)
            if not os.path.exists(path):
                raise RuntimeError('File '+path+' doesn\'t exists')
            tree.Add(path) 

        return tree



if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------
   ___|   |                               \  |         |                
 \___ \   __ \    _` |  __ \    _ \      |\/ |   _` |  |  /   _ \   __| 
       |  | | |  (   |  |   |   __/      |   |  (   |    <    __/  |    
 _____/  _| |_| \__,_|  .__/  \___|     _|  _| \__,_| _|\_\ \___| _|    
                       _|                                               
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'         , dest='sigset'         , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory'                            , default='./data/')
          
    # read default pargin options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi
    
    print " inputDir =           ", opt.inputDir
    print " outputDir =          ", opt.outputDir
 
    

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._tag       = opt.tag
    
    
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    
    factory.makeNominals( opt.inputDir ,opt.outputDir, variables, cuts, samples)
    
        
        
        
        
        
        
        
        

    #except Exception as e:
        #print '*'*80
        #print 'Fatal exception '+type(e).__name__+': '+str(e)
        #print '*'*80
        #exc_type, exc_value, exc_traceback = sys.exc_info()
        #traceback.print_tb(exc_traceback, file=sys.stdout)
##         traceback.print_tb(exc_traceback, limit=3, file=sys.stdout)
        #print '*'*80
    #finally:
        #print 'Used options'
        #print ', '.join([ '{0} = {1}'.format(a,b) for a,b in opt.__dict__.iteritems()])
