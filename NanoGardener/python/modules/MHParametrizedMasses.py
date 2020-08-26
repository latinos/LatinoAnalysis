import ROOT
import math
import os.path
import random
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


class MHParametrizedMasses(Module):

    def __init__(self, sample_name, cfg_path, model='darkHiggs'):

        self.sample_name = sample_name
        self.model = model
      
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        self.isSignal = 0
        for sample_str in var['isSignal']:
            #print sample_str
            if sample_str == sample_name:

                self.isSignal = var['isSignal'][sample_str]
                break
        
        self.masses = var['masses_' + model]
        self.points = var['bitmap_' + model]
        # self.SignalMass = 0
        # for sample_str in var['masses_signal']:
        #     if sample_str in sample_name:
        #         self.SignalMass = var['masses_signal'][sample_str]
        #         break

        #self.masses = var['masses_' + model]
            
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree 
        self.out.branch(self.model+'_ParametrizedTrainingMass', 'I')
        self.inputTree = inputTree
        for mass in self.masses:
            self.out.branch(self.model+'_ParametrizedEvalMass_'+ str(mass), 'I')

        if(self.isSignal == 1 and self.model == 'darkHiggs'):
            self.out.branch(self.model+'_mhs', 'I')
            self.out.branch(self.model+'_mx', 'I')

        if(self.isSignal == 1 and self.model == '2HDMa'):
            self.out.branch(self.model+'_prod', 'I')
            self.out.branch(self.model+'_sinp', 'F')
            self.out.branch(self.model+'_tanb', 'F')
            self.out.branch(self.model+'_ma', 'I')
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #global TrainingMass, mhs, mx, prod, sinp, tanb, ma
        # print ""
        # print "--------------------"
        # print "self.sample_name"
        # print self.sample_name
        # print "self.isSignal"
        # print self.isSignal
        # print "self.model"
        # print self.model
        # print "self.isSignal == 1 and self.model == 'darkHiggs'"
        # print self.isSignal == 1 and self.model == 'darkHiggs'
        # print "------------------"
        # print ""
        TrainingMass = -9999
        mhs = -9999
        mx = -9999
        prod = -9999
        sinp = -9999.0
        tanb = -9999.0
        ma = -9999

        if(self.isSignal == 1 and self.model == 'darkHiggs'):
            for branch in self.points:
                if (self.inputTree.GetBranchStatus(branch) == True):
                    #print eval('event.'+branch)
                    if (eval('event.'+branch)):
                        start = str(branch).find('Zp_') + 3
                        end = str(branch).find('_Tu', start)
                        TrainingMass = int(str(branch)[start:end])
                        start = str(branch).find('hs_') + 3
                        end = str(branch).find('_mx', start)
                        mhs = int(str(branch)[start:end])
                        start = str(branch).find('mx_') + 3
                        end = str(branch).find('_mZ', start)
                        mx = int(str(branch)[start:end])

                        break
                    else:
                        continue
                else:
                    continue

        elif(self.isSignal == 1 and self.model == '2HDMa'):
            for branch in self.points:
                if (self.inputTree.GetBranchStatus(branch) == True):
#                    print branch
                    if (eval('event.'+branch)):
                        start = str(branch).find('H3_') + 3
                        end = str(branch).find('_MH', start)
                        TrainingMass = int(str(branch)[start:end])

                        start = str(branch).find('nu_') + 3
                        end = str(branch).find('_si', start)
                        if str(branch)[start:end] == 'gg':
                            prod = 1
                        else:
                            prod = 2
                        #prod = str(str(branch)[start:end])
                        start = str(branch).find('np_') + 3
                        end = str(branch).find('_ta', start)
                        if str(branch)[start:end] == '0p35':
                            sinp = 0.35
                        elif str(branch)[start:end] == '0p7':
                            sinp = 0.7
                        #sinp = str(str(branch)[start:end])
                        start = str(branch).find('nb_') + 3
                        end = str(branch).find('_mX', start)
                        if str(branch)[start:end] == '0p5':
                            tanb = 0.5
                        elif str(branch)[start:end] == '1p0':
                            tanb = 1.0
                        elif str(branch)[start:end] == '1p5':
                            tanb = 1.5
                        elif str(branch)[start:end] == '2p0':
                            tanb = 2.0
                        elif str(branch)[start:end] == '4p0':
                            tanb = 4.0
                        elif str(branch)[start:end] == '8p0':
                            tanb = 8.0
                        #tanb =str(str(branch)[start:end])
                        start = str(branch).find('H4_') + 3
                        end = str(branch).find('_MH', start)
                        ma = int(str(branch)[start:end])

                        break
                    else:
                        continue
                else:
                    continue

        else:
            TrainingMass = random.choice(self.masses)

        self.out.fillBranch(self.model+'_ParametrizedTrainingMass', TrainingMass)
        for mass in self.masses:
            self.out.fillBranch(self.model+'_ParametrizedEvalMass_'+ str(mass), mass)

        if(self.isSignal == 1 and self.model == 'darkHiggs'):
            self.out.fillBranch(self.model+'_mhs', mhs)
            self.out.fillBranch(self.model+'_mx', mx)

        if(self.isSignal == 1 and self.model == '2HDMa'):
            self.out.fillBranch(self.model+'_prod', prod)
            self.out.fillBranch(self.model+'_sinp', sinp)
            self.out.fillBranch(self.model+'_tanb', tanb)
            self.out.fillBranch(self.model+'_ma', ma)

        return True

