import optparse
import numpy
import ROOT
import os.path
import math
import random 

from LatinoAnalysis.Gardener.gardening import TreeCloner
                                                                                                                         
class rochester_corr(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a scale factor from Rochester corrections'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-d', '--data', dest='isdata', help='is data or not', default='0')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        self.isdata = int(opts.isdata)

        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/RoccoR.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/RoccoR.cc++g')
       
    def _corMET (self,met,lpt_org,lpt):
        newmet = met + lpt_org - lpt
        return newmet

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
     
        self.connect(tree,input)

        self.namesOldBranchesToBeModifiedVector = ['std_vector_lepton_pt']
  
        self.metvar1 = 'metPfType1'
        self.metvar2= 'metPfType1Phi' 
        self.namesOldBranchesToBeModifiedSimpleVariable = [self.metvar1,self.metvar2]

        #vectorsToChange = ['std_vector_lepton_','std_vector_muon_']
        #for b in self.itree.GetListOfBranches():
        #    branchName = b.GetName()
        #    for subString in vectorsToChange:
        #        if subString in branchName: self.namesOldBranchesToBeModifiedVector.append(branchName)

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector+self.namesOldBranchesToBeModifiedSimpleVariable)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCHES 

        # ... Old Branches:
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
            bvariable = numpy.ones(1, dtype=numpy.float32)
            self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems(): self.otree.Branch(bname,bvariable,bname+'/F') 

        cmssw_base = os.getenv('CMSSW_BASE')
        rochester_path = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/rcdata.2016.v3'
        print "scale factors from", rochester_path
        rc=ROOT.RoccoR(rochester_path)

        # Loop
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        savedentries = 0

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 10000

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree
        s=0
        m=0
       
        for i in xrange(nentries):

            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            leptonPtChanged = []

            oldmet = itree.metPfType1
            oldphi = itree.metPfType1Phi
            met_org = ROOT.TLorentzVector()
            met_org.SetPtEtaPhiM(oldmet, 0, oldphi, 0)
            newmet = ROOT.TLorentzVector()
            newmet = met_org

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

                if not (itree.std_vector_lepton_pt[iLep] > 0):
                    continue
                pt = itree.std_vector_lepton_pt [iLep]
                flavour = itree.std_vector_lepton_flavour [iLep]
                eta = itree.std_vector_lepton_eta [iLep]
                phi =itree.std_vector_lepton_phi [iLep]
                
                # Muons only
                if  abs(flavour) == 13 :
                    
                    charge = int(flavour/abs(flavour))
                    nl =int(itree.std_vector_muon_NValidHitsInTrk [iLep])
                    u1 =random.random()
                    #print charge, pt, eta, phi, nl, genpt, u1
                                      
                    if self.isdata == 1 :
                        #for each data muon in the loop, use this function to get a scale factor for its momentum
                        dataSF = rc.kScaleDT(charge,pt,eta,phi)
                        #dataSF= 1.5
                        newpt= pt*dataSF
                        leptonPtChanged.append(newpt)
                        #if i%step == 0.:
                        #    print dataSF
                    else :
                        genpt = itree.std_vector_leptonGen_pt [iLep]                
                        #for MC, if matched gen-level muon (genPt) is available, use this function
                        mcSF = rc.kScaleFromGenMC(charge, pt, eta, phi, nl, genpt, u1)
                        #mcSF= 1.5
                        newpt= pt*mcSF
                        leptonPtChanged.append(newpt)
                        #if i%step == 0.:
                        #    print mcSF
                       
                else:
                   leptonPtChanged.append( itree.std_vector_lepton_pt[iLep])

                l1 = ROOT.TLorentzVector()
                l1_org = ROOT.TLorentzVector()
                l1_org.SetPtEtaPhiM(pt,eta, phi,0)
                l1.SetPtEtaPhiM (newpt,eta,phi,0)

                newmet = self._corMET(newmet,l1_org,l1)

            leptonOrder = sorted(range(len(leptonPtChanged)), key=lambda k: leptonPtChanged[k], reverse=True) 

            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
             
                if 'std_vector_lepton_pt' in bname:
                    for i in range( len(leptonOrder) ) :
                        bvector.push_back ( leptonPtChanged[leptonOrder[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(leptonOrder) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, leptonOrder)

            # update met
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar1][0] = numpy.float32(newmet.Pt())
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar2][0] = numpy.float32(newmet.Phi())

            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
     
        
        



