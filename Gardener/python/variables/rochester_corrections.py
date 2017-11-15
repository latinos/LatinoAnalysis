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

    def howCloseIsAToB(self, a_Eta, a_Phi, b_Eta, b_Phi) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
            dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        #print ">> dR = ", math.sqrt(dR2), " :: ", dPhi, " (+) ", (b_Eta - a_Eta) 
        return dR2
       

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

        self.namesOldBranchesToBeModifiedVector = []
        vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)

        self.metvar1 = 'metPfType1'
        self.metvar2= 'metPfType1Phi' 
        self.namesOldBranchesToBeModifiedSimpleVariable = [self.metvar1,self.metvar2]

        self.namesNewBranchesToBeAddedVector = ['std_vector_lepton_rochesterMCSF','std_vector_lepton_rochesterDataSF']


        #vectorsToChange = ['std_vector_lepton_','std_vector_muon_']
        #for b in self.itree.GetListOfBranches():
        #    branchName = b.GetName()
        #    for subString in vectorsToChange:
        #        if subString in branchName: self.namesOldBranchesToBeModifiedVector.append(branchName)

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector+self.namesOldBranchesToBeModifiedSimpleVariable+self.namesNewBranchesToBeAddedVector)

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

        # New branches
        self.newBranchesToBeAddedVector = {}
        for bname in self.namesNewBranchesToBeAddedVector:
          bvector =  ROOT.std.vector(float) ()
          self.newBranchesToBeAddedVector[bname] = bvector
        for bname, bvector in self.newBranchesToBeAddedVector.iteritems(): self.otree.Branch(bname,bvector)

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
            MCSFlist = []
            DataSFlist= []
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
                newpt = pt
                # Muons only
                if  abs(flavour) == 13 :
                    
                    charge = int(flavour/abs(flavour))
                    nl =int(itree.std_vector_muon_NValidHitsInTrk [iLep])
                    u1 =random.random()
                    u2 =random.random()
                    #print charge, pt, eta, phi, nl, genpt, u1, u2
                                      
                    if self.isdata == 1 :
                        #for each data muon in the loop, use this function to get a scale factor for its momentum
                        dataSF = rc.kScaleDT(charge,pt,eta,phi)
                        #self.newBranchesToBeAddedVector.items(std_vector_lepton_rochesterDataSF).push_back (dataSF)
                        DataSFlist.append(dataSF)
                        #dataSF= 1.5
                        newpt= pt*dataSF
                        leptonPtChanged.append(newpt)
                        
                        #if i%step == 0.:
                        #    print dataSF
                    else :
                        # Look for the Gen lepton that best matches 
                        minimumdR2 = 10
                        matchedgenpt = -1
                        for iGenLep in xrange(len(itree.std_vector_leptonGen_pt)) :
                            if self.itree.std_vector_leptonGen_pt[iGenLep] > 0 \
                                    and  self.itree.std_vector_leptonGen_status[iGenLep] == 1 \
                                    and  (abs(self.itree.std_vector_leptonGen_pid[iGenLep]) == 13)   : 
                                # and if the reco lepton is close to this gen lepton
                               dR2 = self.howCloseIsAToB(self.itree.std_vector_lepton_eta[iLep],    self.itree.std_vector_lepton_phi[iLep],
                                                    self.itree.std_vector_leptonGen_eta[iGenLep], self.itree.std_vector_leptonGen_phi[iGenLep])
                               if dR2 < minimumdR2 :
                                   matchedgenpt = self.itree.std_vector_leptonGen_pt[iGenLep]
                                   minimumdR2 = dR2
                                  
                        if matchedgenpt == -1 :
                            matchedgenpt = pt
                       
                        #for MC, if matched gen-level muon (genPt) is available, use this function
                        mcSF = rc.kScaleFromGenMC(charge, pt, eta, phi, nl, matchedgenpt, u1)
                        #self.newBranchesToBeAddedVector.items(std_vector_lepton_rochesterMCSF).push_back (mcSF)
                        MCSFlist.append(mcSF)
                        if mcSF < 0.5 :
                            mcSF =1
                        if math.isnan(mcSF) ==1 :
                            mcSF =1
                        #    print charge, pt, eta, phi, nl, matchedgenpt, u1
                        #if abs(eta)>2.1 :
                        #    print mcSF
                        #if not, then:
                        #else :
                        #    mcSF = rc.kScaleAndSmearMC(charge, pt, eta, phi, nl, u1, u2)
                        #mcSF= 1.5
                        newpt= pt*mcSF
                        leptonPtChanged.append(newpt)
                       
                        #if i%step == 0.:
                        #    print mcSF
                       
                else:
                   leptonPtChanged.append(newpt)

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

            for bname, bvector in self.newBranchesToBeAddedVector.iteritems():
                bvector.clear()
             
                if 'MC' in bname:
                    for i in range( len(MCSFlist) ) :
                        bvector.push_back ( MCSFlist[i] )
                    for i in range( len(getattr(self.itree, 'std_vector_lepton_eta')) - len(MCSFlist) ) :
                        bvector.push_back ( -9999. )
                else:
                    for i in range( len(DataSFlist) ) :
                        bvector.push_back ( DataSFlist[i] )
                    for i in range( len(getattr(self.itree, 'std_vector_lepton_eta')) - len(DataSFlist) ) :
                        bvector.push_back ( -9999. )

            # update met
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar1][0] = numpy.float32(newmet.Pt())
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar2][0] = numpy.float32(newmet.Phi())

            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
     
        
        



