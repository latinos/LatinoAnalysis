from LatinoAnalysis.Gardener.gardening import TreeCloner

import optparse
import os
import sys
from ROOT import *
import numpy
import array
import re
import warnings
import os.path
from math import *
import math

#
#     ___ \       \   |     \   |
#     |    |    |\ \  |   |\ \  |                          _)         |      | 
#     |    |    | \ \ |   | \ \ |      \ \   /  _` |   __|  |   _` |  __ \   |   _ \ 
#     |    |    |  \  |   |  \  |       \ \ /  (   |  |     |  (   |  |   |  |   __/
#    _____/    _|   \_|  _|   \_|        \_/  \__,_| _|    _| \__,_| _.__/  _| \___|
#

#For test model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.optimizers import SGD, Adam, RMSprop, Adagrad, Adadelta, Adamax, Nadam
from keras.utils import np_utils
from keras.models import model_from_json

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

#loads the model
baseCMSSW = os.getenv('CMSSW_BASE')
smodel = baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/vbfdnn/model_20180604.json"
#smodel = "/afs/cern.ch/user/l/lusanche/KERAS/run_dnn/model.json"
sweight = baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/vbfdnn/model_20180604_weights_json.h5"
#sweight = "/afs/cern.ch/user/l/lusanche/KERAS/run_dnn/model_weights_json.h5"
json_file = open(smodel,'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(sweight)

opt = Adamax();

#compile the model
loaded_model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['acc'])

class DNNvarFiller(TreeCloner):
    def __init__(self):
       pass

    #def createDNNvar(self):
    #    self.AddVariable("DNNvar", (self.var))
        
    def help(self):
        return '''Add DNN variable'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        
        self.getDNNvar = None
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
        
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = ['DNNvar']
        
        self.clone(output,newbranches)

        DNNvar   = numpy.ones(1,dtype=numpy.float)

        self.otree.Branch('DNNvar',  DNNvar,  'DNNvar/D')

        #self.createDNNvar()
        
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        
        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        X_test = [[0 for i in range(12)] for j in range(nentries)]
        ientry = 0
        for i in itree:
            X_test[ientry][0] = i.std_vector_lepton_pt[0]
            X_test[ientry][1] = i.std_vector_lepton_eta[0]
            X_test[ientry][2] = i.std_vector_lepton_phi[0]
            X_test[ientry][3] = i.std_vector_lepton_pt[1]
            X_test[ientry][4] = i.std_vector_lepton_eta[1]
            X_test[ientry][5] = i.std_vector_lepton_phi[1]
            X_test[ientry][6] = i.std_vector_jet_pt[0]
            X_test[ientry][7] = i.std_vector_jet_eta[0]
            X_test[ientry][8] = i.std_vector_jet_phi[0]
            X_test[ientry][9] = i.std_vector_jet_pt[1]
            X_test[ientry][10] = i.std_vector_jet_eta[1]
            X_test[ientry][11] = i.std_vector_jet_phi[1]
            ientry = ientry + 1
        
        Y_pred  = loaded_model.predict(X_test)

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            DNNvar[0] = Y_pred[i][0]
             
            otree.Fill()
            
        otree.Write()
        self.disconnect()
print '- Eventloop completed'
