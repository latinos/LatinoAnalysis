#       _                           _____              _                                   _   
#      | |                         |_   _|            | |                                 | |  
#      | |      ___  _ __    _ __    | |    ___   ___ | |  _   _  _ __    ___   ___  _ __ | |_ 
#      | |     / _ \| '_ \  | '_ \   | |   / __| / __|| | | | | || '_ \  / __| / _ \| '__|| __|
#      | |____|  __/| |_) | | |_) |  | |   \__ \| (__ | | | |_| || | | || (__ |  __/| |   | |_ 
#      \_____/ \___|| .__/  | .__/   \_/   |___/ \___||_|  \__,_||_| |_| \___| \___||_|    \__|
#                   | |     | |                                                                
#                   |_|     |_|                                                                
#      
#      

from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class LeppTScalerTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Lepton pT scaler acc to values given in leppTscaler.py'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c','--cmssw',dest='cmssw',help='cmssw version req for met vars',default='763')
        group.add_option('-f','--fileIn',dest='Filewithleptscalevalues',help='file with lep pT scale values for uncert calc',default=None)
        group.add_option('-v','--upordown',dest='variation',help='specify the variation whether pT scaled up(1) or down(-1)',default=None)
        group.add_option('-k','--lepFlavourToChange',dest='lepFlavourToChange',help='select the lepton  ele (11) or mu (13)', type='string', default=None)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        print " >>  checkOptions "
        leppTscaler = {}     

        self.lepFlavourToChange = opts.lepFlavourToChange
        if opts.lepFlavourToChange == None :
            print "please enter mu or ele=",opts.lepFlavourToChange
        self.cmssw=opts.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')

        if opts.cmssw == 'Full2016' :
          if opts.Filewithleptscalevalues == None and  not opts.lepFlavourToChange ==None:
              if opts.lepFlavourToChange == 'ele' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_el_80_remAOD.py'
              elif opts.lepFlavourToChange == 'mu' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_mu_80_remAOD.py'
              else:
                  print "please select mu or ele"      

        elif opts.cmssw == 'ICHEP2016' :
          if opts.Filewithleptscalevalues == None and  not opts.lepFlavourToChange ==None:
              if opts.lepFlavourToChange == 'ele' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_el_80_prompt.py'
              elif opts.lepFlavourToChange == 'mu' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_mu_80_prompt.py'
              else:
                  print "please select mu or ele"        

        else :   # 2015
          if opts.Filewithleptscalevalues == None and  not opts.lepFlavourToChange ==None:
              if opts.lepFlavourToChange == 'ele' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_el_76_rereco.py'
              elif opts.lepFlavourToChange == 'mu' :
                  opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_mu_76_rereco.py'
              else:
                  print "please select mu or ele"
        print " opts.Filewithleptscalevalues = " , opts.Filewithleptscalevalues


        self.variation = opts.variation
        if opts.variation == None :
            print "taking variations from file"
        else:
            self.variation    = 1.0 * float(opts.variation)
        print " amount of variation = ", self.variation

            
        if os.path.exists(opts.Filewithleptscalevalues) :
          print " opts.Filewithleptscalevalues = " , opts.Filewithleptscalevalues
          handle = open(opts.Filewithleptscalevalues,'r')
          exec(handle)
          handle.close()
        else :
          print "nothing ?"

        self.leppTscaler = leppTscaler
        self.minpt = 0
        self.maxpt = 200
        self.mineta = 0
        self.maxeta = 2.5


    # Strange algebra to be able to use raw phi angles
    def sgn_deltaphi(self, phi1, phi2) :
        dphi = phi1 - phi2
        if dphi < -ROOT.TMath.Pi() :
            dphi = dphi + 2*ROOT.TMath.Pi()
        elif dphi > ROOT.TMath.Pi() :
            dphi = dphi - 2*ROOT.TMath.Pi()
        return dphi
    
    # here I want to properly sum metphi and delta(metphi)
    def sum_deltaphi(self, phi, dphi) :
        result = phi + dphi
        if result < -ROOT.TMath.Pi() :
            result = result + 2*ROOT.TMath.Pi()
        elif result > ROOT.TMath.Pi() :
            result = result - 2*ROOT.TMath.Pi()
        return result


    def _getScale (self, kindLep, pt, eta):
        # fix underflow and overflow
        if pt < self.minpt:
          pt = self.minpt
        if pt > self.maxpt:
          pt = self.maxpt
        
        if eta < self.mineta:
          eta = self.mineta
        if eta > self.maxeta:
          eta = self.maxeta
        
        if kindLep in self.leppTscaler.keys() : 
            # get the scale values in bins of pT and eta
            for point in self.leppTscaler[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    return point[2]
            # default ... it should never happen!
            # print " default ???"
            return 1.0
           
        else:
            return 1.0
    
    
    # def _corMET (self,met,lpt_org,lpt):
    #     newmet = met + lpt_org - lpt
    #     return newmet
    
    
    def changeOrder(self, vectorname, vector, leptonOrderList) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified        
        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(leptonOrderList) ) :
          vector.push_back ( temp_vector[ leptonOrderList[i] ] )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(leptonOrderList) ) :
          vector.push_back ( -9999. )
          

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
                
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedevents = 0

        # met branches to be changed
        if self.cmssw == '74x' :
            self.metvar1 = 'pfType1Met'
            self.metvar2= 'pfType1Metphi' 
        else :
            self.metvar1 = 'metPfType1'
            self.metvar2= 'metPfType1Phi' 
        self.namesOldBranchesToBeModifiedSimpleVariable = [self.metvar1,self.metvar2]

        self.namesOldBranchesToBeModifiedVector = []
        vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
            branchName = b.GetName()
            for subString in vectorsToChange:
                if subString in branchName:
                    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # clone the tree with new branches added
        self.clone(output,self.namesOldBranchesToBeModifiedVector+self.namesOldBranchesToBeModifiedSimpleVariable)
      
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
         # print "debug 0 ", bname
         # connect branches for vectors
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
          self.otree.Branch(bname,bvector)            

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches for floats
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                        #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')         

        # input tree  
        itree = self.itree

        print '- Starting eventloop'
        step = 5000
        #step = 1

        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale lepton pt
            # Scale Up
            leptonPtChanged = []

            if self.cmssw == '74x' :
              oldmet = itree.pfType1Met
              oldphi = itree.pfType1Metphi
            else :
              oldmet = itree.metPfType1
              oldphi = itree.metPfType1Phi
            met_org = ROOT.TLorentzVector()
            met_org.SetPtEtaPhiM(oldmet, 0, oldphi, 0)
            newmet = ROOT.TLorentzVector()
#            newmet = met_org

            for i in range(itree.std_vector_lepton_pt.size()):
                #print " i = ", i, " -->  itree.std_vector_lepton_flavour[i] = ", itree.std_vector_lepton_flavour[i]
                #print "    -> ", abs(itree.std_vector_lepton_flavour[i])
                kindLep = 'lep' # ele or mu
                if not (itree.std_vector_lepton_pt[i] > 0):
                    continue
                pt_lep = itree.std_vector_lepton_pt[i]
                eta_lep = itree.std_vector_lepton_eta[i]
                phi_lep = itree.std_vector_lepton_phi[i] 
#                print "pt eta",pt_lep,eta_lep,phi_lep

                new_pt_lep = pt_lep
                
                if abs(itree.std_vector_lepton_flavour[i]) == 13:
                    kindLep = 'mu'
                elif abs(itree.std_vector_lepton_flavour[i]) == 11:
                    kindLep = 'ele'
                else:
                    print "not a el or muon"
#                print"from input",self.lepFlavourToChange
                if kindLep == self.lepFlavourToChange :
                    wt = self._getScale(kindLep,pt_lep,abs(eta_lep))
                    new_pt_lep = itree.std_vector_lepton_pt[i]*(1 + (self.variation*wt/100.0))
                    leptonPtChanged.append(itree.std_vector_lepton_pt[i]*(1 + (self.variation*wt/100.0)))
                else:
                    # print kindLep,"is not the specified lepton "
                    new_pt_lep = itree.std_vector_lepton_pt[i]*(1 + (0./100))
                    leptonPtChanged.append(itree.std_vector_lepton_pt[i]*(1 + (0./100)))

                l1 = ROOT.TLorentzVector()
                l1_org = ROOT.TLorentzVector()
                l1_org.SetPtEtaPhiM(pt_lep,    eta_lep, phi_lep,0)
                l1.SetPtEtaPhiM    (new_pt_lep,eta_lep,phi_lep,0)
             
                #newmet = self._corMET(newmet,l1_org,l1)

                # Recommended definition of newmet
                if self.lepFlavourToChange == 'ele' :
                    if self.variation == 1.0 :
                        print 'Elec Up'
                        newmetmodule = itree.metPfType1ElecEnUp
                        #newmetphi = itree.metPfRawPhiElecEnUp
                        myDelta = self.sgn_deltaphi(itree.metPfRawPhiElecEnUp, itree.metPfRawPhi)
                        newmetphi = self.sum_deltaphi(itree.metPfType1Phi,myDelta)
                        newmet.SetPtEtaPhiM(newmetmodule, 0, newmetphi, 0)
                    elif self.variation == -1.0 :
                        print 'Elec Down'
                        newmetmodule = itree.metPfType1ElecEnDn
                        #newmetphi = itree.metPfRawPhiElecEnDn
                        myDelta = self.sgn_deltaphi(itree.metPfRawPhiElecEnDn, itree.metPfRawPhi)
                        newmetphi = self.sum_deltaphi(itree.metPfType1Phi,myDelta)
                        newmet.SetPtEtaPhiM(newmetmodule, 0, newmetphi, 0)
                elif self.lepFlavourToChange == 'mu' :
                    if self.variation == 1.0 :
                        newmetmodule = itree.metPfType1MuonEnUp
                        #newmetphi = itree.metPfRawPhiMuonEnUp
                        myDelta = self.sgn_deltaphi(itree.metPfRawPhiMuonEnUp, itree.metPfRawPhi)
                        newmetphi = self.sum_deltaphi(itree.metPfType1Phi,myDelta)
                        newmet.SetPtEtaPhiM(newmetmodule, 0, newmetphi, 0)
                    elif self.variation == -1.0 :
                        newmetmodule = itree.metPfType1MuonEnDn
                        #newmetphi = itree.metPfRawPhiMuonEnDn
                        myDelta = self.sgn_deltaphi(itree.metPfRawPhiMuonEnDn, itree.metPfRawPhi)
                        newmetphi = self.sum_deltaphi(itree.metPfType1Phi,myDelta)
                        newmet.SetPtEtaPhiM(newmetmodule, 0, newmetphi, 0)
                        

            leptonOrder = sorted(range(len(leptonPtChanged)), key=lambda k: leptonPtChanged[k], reverse=True) 


            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
             
                if 'std_vector_lepton_pt' in bname:
                    for i in range( len(leptonOrder) ) :
                        bvector.push_back ( leptonPtChanged[leptonOrder[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(leptonOrder) ) :
                        bvector.push_back ( -9999. )
                elif not 'std_vector_lepton_rochester' in bname: 
               # else:
                    self.changeOrder( bname, bvector, leptonOrder)

            # update met
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar1][0] = numpy.float32(newmet.Pt())
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar2][0] = numpy.float32(newmet.Phi())
            # print " new met vars ",self.oldBranchesToBeModifiedSimpleVariable[self.metvar1][0]

            self.otree.Fill()
            savedevents += 1
            
            
        self.disconnect()
        print '- Eventloop completed'
        print '- Saved:', savedevents, 'events'
