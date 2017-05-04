#
#  Lepton WP Code  
#  author: X. Janssen   
#                                

from LatinoAnalysis.Gardener.gardening import TreeCloner
import ROOT
import optparse
import os
import numpy
from collections import OrderedDict

class LeptonWP():

    def __init__ (self,cmssw,WPDic,WPType,WP):
      print "-------- LeptonWP init() ---------"  
      print WPType,WP
      self.WPType = WPType
      self.WP     = WP

      self.Variables = {}
      if 'Variables' in WPDic[cmssw] :
        for iVar in WPDic[cmssw]['Variables'] :
          self.Variables[iVar] = WPDic[cmssw]['Variables'][iVar]

      self.WP = {}
      for iCond in WPDic[cmssw][WPType][WP] :
        nCut = 0     
        Cut = ''
        for iCut in WPDic[cmssw][WPType][WP][iCond]: 
          if nCut != 0 : Cut += ' and '
          nCut += 1
          Cut += '(' + iCut + ')'

        self.WP[iCond] = Cut    

      print self.WP

    def passWP(self,itree,iLep):

       #print 'Applying', self.WPType , self.WP

       # Create variables if needed
       for iVar in self.Variables : exec (iVar+'='+self.Variables[iVar].replace('[]','[iLep]'))

       # Apply WP
       res = 1
       for iCond in self.WP :
         if ( eval(iCond.replace('[]','[iLep]')) ) and not ( eval(self.WP[iCond].replace('[]','[iLep]')) ) : res = 0

       return res

    def isAcloseToB(self, a_Eta, a_Phi, b_Eta, b_Phi, drmax) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        if dR2 < (drmax*drmax):
            return True
        else:
            return False


    def isoConeOverlapRemoval(self,itree,iLep):

        pt_to_be_removed_from_overlap = 0
        isoConSize = 0.4
        for jLep in xrange(len(itree.std_vector_lepton_pt)):
          if jLep != iLep and itree.std_vector_lepton_pt[jLep]>0 :
            if self.isAcloseToB(itree.std_vector_lepton_eta[jLep], itree.std_vector_lepton_phi[jLep],
                                itree.std_vector_lepton_eta[iLep], itree.std_vector_lepton_phi[iLep],
                                isoConSize) :
                   pt_to_be_removed_from_overlap += itree.std_vector_lepton_pt[jLep]

        return pt_to_be_removed_from_overlap

class LeptonSel(TreeCloner):

    def __init__(self):
       pass

    def help(self):
       return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw',   dest='cmssw', help='cmssw version (naming convention may change)', default='Full2016', type='string') 
        group.add_option('-w', '--wpdic',   dest='WPdic', help='WP Dictionnary', default='LatinoAnalysis/Gardener/python/variables/LeptonSel_cfg.py', type='string') 
        group.add_option('-k', '--kind' ,   dest='kindLep', help='Kind of mininal lepton to select and use for jet cleaning (2=Fake/3=WgStar/4=Loose)' , default=1)
        group.add_option('-n', '--nMinLep', dest='nMinLep', help='Minimal number of leptons of selected kind' , default = 1 )

    def checkOptions(self,opts):
        
        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        self.WPdic = cmssw_base+'/src/'+opts.WPdic
        print self.WPdic 
        if os.path.exists(self.WPdic) :
          handle = open(self.WPdic,'r')
          exec(handle)
          handle.close()
        else:
          print 'ERROR: No WP'
          exit()  

        # Lepton cleaning options
        self.kindLep=int(opts.kindLep)
        self.nMinLep=int(opts.nMinLep) 
        self.pTLeptCut = [18.0,8.0]  # Only applied up to nMinLep

        # Jet cleaning options
        self.jetCleaning_minpTLep = 10.
        self.jetCleaning_dRmax    = 0.3
        self.jetCleaning_dR2max   = self.jetCleaning_dRmax * self.jetCleaning_dRmax
        self.jetCleaning_absEta   = 5.0

        # Create Elecron WP
        self.VetoObjElectronWPs   = {}
        self.FakeObjElectronWPs   = {}
        self.TightObjElectronWPs  = {}
        self.WgStarObjElectronWPs = {}
 
        if self.cmssw in ElectronWP :
          if 'VetoObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['VetoObjWP']   : self.VetoObjElectronWPs[iWP]   = LeptonWP(self.cmssw,ElectronWP,'VetoObjWP',iWP)
          if 'FakeObjWP' in ElectronWP[self.cmssw] : 
            for iWP in ElectronWP[self.cmssw]['FakeObjWP']   : self.FakeObjElectronWPs[iWP]   = LeptonWP(self.cmssw,ElectronWP,'FakeObjWP',iWP)
          if 'TightObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['TightObjWP']  : self.TightObjElectronWPs[iWP]  = LeptonWP(self.cmssw,ElectronWP,'TightObjWP',iWP)
          if 'WgStarObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['WgStarObjWP'] : self.WgStarObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'WgStarObjWP',iWP)


        # Create Muon WP
        self.VetoObjMuonWPs   = {}
        self.FakeObjMuonWPs   = {}
        self.TightObjMuonWPs  = {}
        self.WgStarObjMuonWPs = {}

        if self.cmssw in MuonWP :
          if 'VetoObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['VetoObjWP']  : self.VetoObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'VetoObjWP',iWP)
          if 'FakeObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['FakeObjWP']  : self.FakeObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'FakeObjWP',iWP)
          if 'TightObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['TightObjWP'] : self.TightObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'TightObjWP',iWP)
          if 'WgStarObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['WgStarObjWP'] : self.WgStarObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'WgStarObjWP',iWP)

        # What to do if more than 1 Fake Obj definition ?
        if  len(self.FakeObjMuonWPs) > 1 or len(self.FakeObjElectronWPs) > 1 :
          print 'ERROR: Can not handle more than 1 FakeObj definition'
          exit()

        # What to do if more than 1 WgStar Obj definition ?
        if  len(self.WgStarObjMuonWPs) > 1 or len(self.WgStarObjElectronWPs) > 1 :
          print 'ERROR: Can not handle more than 1 WgStarObj definition'
          exit()


    def changeOrder(self, vectorname, vector, goodleptonslist) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified
        
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(goodleptonslist) ) :
          #print " --> [", i, " :: ", len(goodleptonslist) ,"] :::>> ", len(temp_vector), " --> ", goodleptonslist[i]      
          # otree."vectorname"[i] = temp_vector[goodleptonslist[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ goodleptonslist[i] ])
          vector.push_back ( temp_vector[ goodleptonslist[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(goodleptonslist) ) :
          vector.push_back ( -9999. )
          
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(goodleptonslist), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

    def jetIsLepton(self, jetEta, jetPhi, lepEta, lepPhi) :
        #dR = ROOT.TMath.Sqrt( ROOT.TMath.Power(lepEta - jetEta, 2) + ROOT.TMath.Power(ROOT.TMath.Abs(ROOT.TMath.Abs(lepPhi - jetPhi)-ROOT.TMath.Pi())-ROOT.TMath.Pi(), 2) )
        dPhi = ROOT.TMath.Abs(lepPhi - jetPhi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi
        if dR2 < self.jetCleaning_dR2max :
            return True
        else:
            return False

    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # Lepton Tags container
        LeptonTags = {}
        # And target variables:
        self.namesNewBranchesVector = [] 
        self.namesNewBranchesVector.append('std_vector_lepton_isLooseLepton')
        self.namesNewBranchesVector.append('std_vector_lepton_isWgsLepton')
        for iWP in self.TightObjElectronWPs : self.namesNewBranchesVector.append('std_vector_electron_isTightLepton_'+iWP)
        for iWP in self.TightObjMuonWPs     : self.namesNewBranchesVector.append('std_vector_muon_isTightLepton_'+iWP)

        # Veto lepton 4-vectors        
        self.namesNewBranchesVector.append('std_vector_vetolepton_pt')
        self.namesNewBranchesVector.append('std_vector_vetolepton_eta')
        self.namesNewBranchesVector.append('std_vector_vetolepton_phi')
        self.namesNewBranchesVector.append('std_vector_vetolepton_flavour')
        self.namesNewBranchesVector.append('std_vector_vetolepton_cleanId')

        # Get list of jet and lepton std_vector branches from tree
        self.namesOldBranchesToBeModifiedVector = []
        vectorsToChange = ['std_vector_lepton_','std_vector_electron_','std_vector_muon_','std_vector_jet_','std_vector_puppijet_']
        for b in self.itree.GetListOfBranches():
          branchName = b.GetName()
          for subString in vectorsToChange:
            if subString in branchName: self.namesOldBranchesToBeModifiedVector.append(branchName)

        # And same for soem float varaibles linked to jets with the structure "std_vector_jet_"NAME to be migrated to "jet"NAME"+number.
        # e.g. jetpt1, jeteta1, jetpt2, jeteta2, ...
        self.jetVariables = [
            'pt',
            'eta',
            'phi',
            'mass',
            #'mva',
            #'id',
            'tche'
            # NChgQC, ChgptCut1, NHM, NNeutralptCut, PhM, bjpb, ... ?
            # jetRho ?
            ]
        self.jetVarList = []
        # maximum number of "single jet" variables to be saved
        maxnjets = 2 # 7 --> everything is available in form of std::vector -> these will be deprecated
        for jetVar in self.jetVariables:
          for i in xrange(maxnjets):
            self.jetVarList.append("jet"+jetVar+str(i+1))

        # AND some variables we compute in this code like veto leptons
        self.namesOfSpecialSimpleVariable = [
           'metFilter',
           'dmZllRecoMuon'
        ]


        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOfSpecialSimpleVariable + self.jetVarList + self.namesNewBranchesVector)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES 

        # ... New Branches: lepton Tags and veto leptons 4-vectors 
        self.newBranchesVector = {}
        for bname in self.namesNewBranchesVector:
          bvector =  ROOT.std.vector(float) ()
          self.newBranchesVector[bname] = bvector
        for bname, bvector in self.newBranchesVector.iteritems(): self.otree.Branch(bname,bvector)        

        # ... Old Branches: lepton and jets std_vector
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        # .... jet Variables
        self.jetVarDic = OrderedDict()
        for bname in self.jetVarList:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.jetVarDic[bname] = bvariable
        for bname, bvariable in self.jetVarDic.iteritems(): self.otree.Branch(bname,bvariable,bname+'/F') 

        # ... Special variables
        self.oldBranchesToBeModifiedSpecialSimpleVariable = {}
        for bname in self.namesOfSpecialSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSpecialSimpleVariable[bname] = bvariable
        for bname, bvariable in self.oldBranchesToBeModifiedSpecialSimpleVariable.iteritems():  self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        # Loop
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        savedentries = 0

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Gep Letpon Tags: 

            LeptonTags ['Veto']   = []
            LeptonTags ['Loose']  = []
            LeptonTags ['WgStar'] = []
            for iWP in self.TightObjElectronWPs : LeptonTags['electron_'+iWP] = []
            for iWP in self.TightObjMuonWPs     : LeptonTags['muon_'+iWP]     = [] 
            
            
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              
               # Electron
               if    abs(self.itree.std_vector_lepton_flavour[iLep]) == 11 :
                 if len(self.VetoObjElectronWPs)   == 0 : LeptonTags ['Veto']   .append( 0 ) 
                 else :  
                   for iWP in self.VetoObjElectronWPs   : LeptonTags ['Veto']   .append( self.VetoObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 if len(self.FakeObjElectronWPs)   == 0 : LeptonTags ['Loose']  .append( 0 )
                 else :                                   
                   for iWP in self.FakeObjElectronWPs   : LeptonTags ['Loose']  .append( self.FakeObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 if len(self.WgStarObjElectronWPs) == 0 : LeptonTags ['WgStar'] .append( 0 )
                 else :                                  
                   for iWP in self.WgStarObjElectronWPs : LeptonTags ['WgStar'] .append( self.WgStarObjElectronWPs[iWP].passWP(self.itree,iLep) ) 
                 for iWP in self.TightObjElectronWPs : LeptonTags ['electron_'+iWP] .append( self.TightObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 # ... and 0 for muons
                 for iWP in self.TightObjMuonWPs : LeptonTags['muon_'+iWP] .append( 0 )
                  

               # Muon
               elif  abs(self.itree.std_vector_lepton_flavour[iLep]) == 13 :
                 if len(self.VetoObjMuonWPs)   == 0 : LeptonTags ['Veto']   .append( 0 )
                 else :
                   for iWP in self.VetoObjMuonWPs   : LeptonTags ['Veto']   .append( self.VetoObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 if len(self.FakeObjMuonWPs)   == 0 : LeptonTags ['Loose']  .append( 0 )
                 else :
                   for iWP in self.FakeObjMuonWPs   : LeptonTags ['Loose']  .append( self.FakeObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 if len(self.WgStarObjMuonWPs) == 0 : LeptonTags ['WgStar'] .append( 0 )
                 else :
                   for iWP in self.WgStarObjMuonWPs : LeptonTags ['WgStar'] .append( self.WgStarObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 for iWP in self.TightObjMuonWPs : LeptonTags ['muon_'+iWP] .append( self.TightObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 # ... and 0 for electrons
                 for iWP in self.TightObjElectronWPs : LeptonTags['electron_'+iWP] .append( 0 )
 
               # ... and 0 if not a lepton
               else:  
                 LeptonTags ['Veto']   .append( 0 )
                 LeptonTags ['Loose']  .append( 0 )
                 LeptonTags ['WgStar'] .append( 0 )
                 for iWP in self.TightObjElectronWPs  : LeptonTags ['electron_'+iWP] .append( 0 )
                 for iWP in self.TightObjMuonWPs      : LeptonTags ['muon_'+iWP]     .append( 0 ) 


            # At least nLeptons of kindLep or throw away the event
            if   self.kindLep == 2 : CleanTag = 'Loose'
            elif self.kindLep == 3 : CleanTag = 'WgStar'  
            else:
              print 'ERROR: kindLep unavailable : ',self.kindLep
              exit() 

            # Lepton Cuts
            kLepCut = True
            # ... at least nLeptons
            if LeptonTags [CleanTag].count(1) < self.nMinLep :   kLepCut = False
            # ... pT cuts
            if kLepCut:
              jLep = 0
              for iLep in range(len(LeptonTags[CleanTag])) :
                if LeptonTags[CleanTag][iLep] :
                  if jLep < len(self.pTLeptCut) and jLep < self.nMinLep : 
                    if itree.std_vector_lepton_pt[iLep] < self.pTLeptCut[jLep] : kLepCut = False
                  jLep+=1

            # Now we can start cleaning the leptons and fill the tree?
            if kLepCut :   

              maxNumLeptons = len(itree.std_vector_lepton_pt)

              # Clean All vectors
              for bname, bvector in self.newBranchesVector.iteritems()             : bvector.clear()
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems() : bvector.clear()

              # Link to good leptons
              goodLepLinks = []
              goodLeps = []
              jLep = 0 
              for iLep in range(len(LeptonTags[CleanTag])) :
                if LeptonTags[CleanTag][iLep] == 1 : 
                  goodLeps.append(iLep) 
                  goodLepLinks.append(jLep)
                  jLep+=1
                else:
                  goodLepLinks.append(-1)

              # Compute Veto and/or save Veto lepton pt,eta,phi,flavour +link to position in CleanTag
              for iLep in range(len(LeptonTags['Veto'])) :
                if LeptonTags['Veto'][iLep] == 1 :                 
                  for bname, bvector in self.newBranchesVector.iteritems() :
                    if ("std_vector_vetolepton_pt"      == bname) : bvector.push_back(itree.std_vector_lepton_pt[iLep])
                    if ("std_vector_vetolepton_eta"     == bname) : bvector.push_back(itree.std_vector_lepton_eta[iLep])
                    if ("std_vector_vetolepton_phi"     == bname) : bvector.push_back(itree.std_vector_lepton_phi[iLep])
                    if ("std_vector_vetolepton_flavour" == bname) : bvector.push_back(itree.std_vector_lepton_flavour[iLep])
                    if ("std_vector_vetolepton_cleanId" == bname) : bvector.push_back(goodLepLinks[iLep])
              for remainingLep in range( maxNumLeptons - len(otree.std_vector_vetolepton_cleanId) ) :
                  for bname, bvector in self.newBranchesVector.iteritems() :
                    if ("std_vector_vetolepton_pt"      == bname) : bvector.push_back( -9999. )
                    if ("std_vector_vetolepton_eta"     == bname) : bvector.push_back( -9999. )
                    if ("std_vector_vetolepton_phi"     == bname) : bvector.push_back( -9999. )
                    if ("std_vector_vetolepton_flavour" == bname) : bvector.push_back( -9999. )
                    if ("std_vector_vetolepton_cleanId" == bname) : bvector.push_back( -9999. )
          
              # Lepton cleaning
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                 if ("vector_lepton" in bname) or ("vector_electron" in bname) or ("vector_muon" in bname): self.changeOrder( bname, bvector, goodLeps )              

              # Save Lepton tags for cleaned leptons
              for bname, bvector in self.newBranchesVector.iteritems():
                # Fake Obj
                if ("std_vector_lepton_isLooseLepton" == bname) : 
                  for iLep in goodLeps : bvector.push_back(LeptonTags['Loose'][iLep])
                  for remainingLep in range( maxNumLeptons - len(goodLeps) ) : bvector.push_back ( -9999. )
                # WgStar Obj
                if ("std_vector_lepton_isWgsLepton" == bname) : 
                  for iLep in goodLeps : bvector.push_back(LeptonTags['WgStar'][iLep])
                  for remainingLep in range( maxNumLeptons - len(goodLeps) ) : bvector.push_back ( -9999. )
                # Tight Electron
                for iWP in self.TightObjElectronWPs :
                  lTag = 'electron_'+iWP
                  vTag = 'std_vector_electron_isTightLepton_'+iWP
                  if vTag == bname :
                    for iLep in goodLeps : bvector.push_back(LeptonTags[lTag][iLep])
                    for remainingLep in range( maxNumLeptons - len(goodLeps) ) : bvector.push_back ( -9999. )
                # Tight Muons
                for iWP in self.TightObjMuonWPs :
                  lTag = 'muon_'+iWP
                  vTag = 'std_vector_muon_isTightLepton_'+iWP
                  if vTag == bname :
                    for iLep in goodLeps : bvector.push_back(LeptonTags[lTag][iLep])
                    for remainingLep in range( maxNumLeptons - len(goodLeps) ) : bvector.push_back ( -9999. )

              # jet cleaning
              goodJets = []
              for iJet in xrange(len(itree.std_vector_jet_pt)) :
                isLepton = False;
                for iLep in goodLeps :
                  if itree.std_vector_lepton_pt[iLep] < self.jetCleaning_minpTLep:
                    break;
                  if self.jetIsLepton(itree.std_vector_jet_eta[iJet],itree.std_vector_jet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                    isLepton = True;
                if not isLepton:
                  if abs(itree.std_vector_jet_eta[iJet]) <= self.jetCleaning_absEta :
                    goodJets.append(iJet)

              goodPuppiJets = []
              for iJet in xrange(len(itree.std_vector_puppijet_pt)) :
                  isLepton = False;
                  for iLep in goodLeps :
                      if itree.std_vector_lepton_pt[iLep] < self.jetCleaning_minpTLep:
                          break;
                      if self.jetIsLepton(itree.std_vector_puppijet_eta[iJet],itree.std_vector_puppijet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                          isLepton = True;
                  if not isLepton:
                    if abs(itree.std_vector_puppijet_eta[iJet]) <= self.jetCleaning_absEta :
                      goodPuppiJets.append(iJet)

              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                   if (("vector_jet" in bname) or (("vector_puppijet") in bname)) and not (("vector_lepton" in bname) or ("vector_electron" in bname) or ("vector_muon" in bname)):
                       if "vector_puppijet" in bname:
                           self.changeOrder( bname, bvector, goodPuppiJets)
                       else:
                           self.changeOrder( bname, bvector, goodJets)
         
              # refill the single jet variables
              counter = 0
              varCounter = 0
              for bname, bvariable in self.jetVarDic.iteritems():
                  bvariable[0] = (getattr(self.otree, 'std_vector_jet_'+self.jetVariables[varCounter]))[counter]
                  counter += 1
                  if counter == maxnjets:
                      varCounter += 1
                      counter = 0
 
              # met filters: "bool" (as weight)  -- This is used prior to Full2016 Only I think (Xavier)
              if self.cmssw == '763' or self.cmssw == 'ICHEP2016' or self.cmssw == 'Rereco2016' or self.cmssw == 'Full2016' :
                pass_met_filters = 1.
                #print " min =", min( 8 , len(itree.std_vector_trigger_special) )
                for metfilters in range( min( 8 , len(itree.std_vector_trigger_special) ) ) :
                  if itree.std_vector_trigger_special[metfilters] == 0. : pass_met_filters = 0.
                  #print " i: ", i, " :: metfilters ", metfilters, " --> ", itree.std_vector_trigger_special[metfilters]
                self.oldBranchesToBeModifiedSpecialSimpleVariable['metFilter'][0] = pass_met_filters

 
              savedentries+=1     
              otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

 


