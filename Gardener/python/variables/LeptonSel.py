#
#  Lepton WP Code  
#  author: X. Janssen   
#                                

from LatinoAnalysis.Gardener.gardening import TreeCloner
import ROOT
import optparse
import os

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

        self.kindLep=int(opts.kindLep)
        self.nMinLep=int(opts.nMinLep) 

        # Create Elecron WP
        self.FakeObjElectronWPs = {}
        self.TightObjElectronWPs = {}
        self.WgStarObjElectronWPs = {}
 
        if self.cmssw in ElectronWP :
          if 'FakeObjWP' in ElectronWP[self.cmssw] : 
            for iWP in ElectronWP[self.cmssw]['FakeObjWP']  : self.FakeObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'FakeObjWP',iWP)
          if 'TightObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['TightObjWP'] : self.TightObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'TightObjWP',iWP)
          if 'WgStarObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['WgStarObjWP'] : self.WgStarObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'WgStarObjWP',iWP)


        # Create Muon WP
        self.FakeObjMuonWPs = {}
        self.TightObjMuonWPs = {}
        self.WgStarObjMuonWPs = {}

        if self.cmssw in MuonWP :
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

    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # Clone Tree
        self.namesNewBranchesVector = [] 
        self.namesNewBranchesVector.append('std_vector_lepton_isLooseLepton')
        for iWP in self.TightObjElectronWPs : self.namesNewBranchesVector.append('std_vector_electron_isTightLepton_'+iWP)
        for iWP in self.TightObjMuonWPs     : self.namesNewBranchesVector.append('std_vector_muon_isTightLepton_'+iWP)
        print self.namesNewBranchesVector
        self.clone(output,"")

        # new brances as std_vector
        self.newBranchesVector = {}
        for bname in self.namesNewBranchesVector:
          bvector =  ROOT.std.vector(float) ()
          self.newBranchesVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.newBranchesVector.iteritems():
          self.otree.Branch(bname,bvector)

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree

        # Lepton Tags container
        LeptonTags = {}

        # Loop
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        savedentries = 0

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        nentries = 50
        for i in xrange(nentries):

            itree.GetEntry(i)

#           print self.passWP(0)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Gep Letpon Tags: 

            LeptonTags ['Loose']  = []
            LeptonTags ['WgStar'] = []
            for iWP in self.TightObjElectronWPs : LeptonTags['electron_'+iWP] = []
            for iWP in self.TightObjMuonWPs     : LeptonTags['muon_'+iWP]     = [] 
            
            
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              
               # Electron
               if    abs(self.itree.std_vector_lepton_flavour[iLep]) == 11 :
                 for iWP in self.FakeObjElectronWPs  : LeptonTags ['Loose']         .append( self.FakeObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 for iWP in self.WgStarObjElectronWPs: LeptonTags ['WgStar']        .append( self.WgStarObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 for iWP in self.TightObjElectronWPs : LeptonTags ['electron_'+iWP] .append( self.TightObjElectronWPs[iWP].passWP(self.itree,iLep) )
                 # ... and 0 for muons
                 for iWP in self.TightObjMuonWPs : LeptonTags['muon_'+iWP] .append( 0 )
 
               # Muon
               elif  abs(self.itree.std_vector_lepton_flavour[iLep]) == 13 :
                 for iWP in self.FakeObjMuonWPs  : LeptonTags ['Loose']     .append( self.FakeObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 for iWP in self.WgStarObjMuonWPs: LeptonTags ['WgStar']    .append( self.WgStarObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 for iWP in self.TightObjMuonWPs : LeptonTags ['muon_'+iWP] .append( self.TightObjMuonWPs[iWP].passWP(self.itree,iLep) )
                 # ... and 0 for electrons
                 for iWP in self.TightObjElectronWPs : LeptonTags['electron_'+iWP] .append( 0 )
 
               # ... and 0 if not a lepton
               else:  
                 for iWP in self.FakeObjMuonWPs       : LeptonTags ['Loose']         .append( 0 )
                 for iWP in self.WgStarObjMuonWPs     : LeptonTags ['WgStar']        .append( 0 )
                 for iWP in self.TightObjElectronWPs  : LeptonTags ['electron_'+iWP] .append( 0 )
                 for iWP in self.TightObjMuonWPs      : LeptonTags ['muon_'+iWP]     .append( 0 ) 

            print LeptonTags

            # At least nLeptons of kindLep or throw away the event
            if   self.kindLep == 2 : CleanTag = 'Loose'
            elif self.kindLep == 3 : CleanTag = 'WgStar'  
            else:
              print 'ERROR: kindLep unavailable : ',self.kindLep
              exit() 
            if LeptonTags [CleanTag].count(1) >= self.nMinLep :   


              # Lepton cleaning
               
              # jet cleaning

#
#             for bname, bvector in self.newBranchesVector.iteritems():
#                bvector.clear()
#                if bname == 'std_vector_lepton_isLooseLepton' :
#                  bvector.push_back (LooseTag)
#                if bname == 'std_vector_lepton_isTightLepton' :
#                  bvector.push_back (TightTag)

  
              savedentries+=1     
              otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

 


