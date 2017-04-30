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


class LeptonSel(TreeCloner):

    def __init__(self):
       pass

    def help(self):
       return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='Full2016', type='string') 
        group.add_option('-w', '--wpdic', dest='WPdic', help='WP Dictionnary', default='LatinoAnalysis/Gardener/python/variables/LeptonSel_cfg.py', type='string') 

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

        # Create Elecron WP
        self.FakeObjElectronWPs = {}
        self.TightObjElectronWPs = {}
 
        if self.cmssw in ElectronWP :
          if 'FakeObjWP' in ElectronWP[self.cmssw] : 
            for iWP in ElectronWP[self.cmssw]['FakeObjWP']  : self.FakeObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'FakeObjWP',iWP)
          if 'TightObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['TightObjWP'] : self.TightObjElectronWPs[iWP] = LeptonWP(self.cmssw,ElectronWP,'TightObjWP',iWP)

        # Create Muon WP
        self.FakeObjMuonWPs = {}
        self.TightObjMuonWPs = {}

        if self.cmssw in MuonWP :
          if 'FakeObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['FakeObjWP']  : self.FakeObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'FakeObjWP',iWP)
          if 'TightObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['TightObjWP'] : self.TightObjMuonWPs[iWP] = LeptonWP(self.cmssw,MuonWP,'TightObjWP',iWP)

        # What to do if more than 1 Fake Obj definition ?
        if  len(self.FakeObjMuonWPs) > 1 or len(self.FakeObjElectronWPs) > 1 :
          print 'ERROR: Can not handle more than 1 FakeObj definition'
          exit()

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # Clone Tree
        self.namesNewBranchesVector = ['std_vector_lepton_isLooseLepton', 'std_vector_lepton_isTightLepton']
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

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

              
               # Electron
               if    abs(self.itree.std_vector_lepton_flavour[iLep]) == 11 :
                 for iWP in self.FakeObjElectronWPs  : self.FakeObjElectronWPs[iWP].passWP(self.itree,iLep) 
                 for iWP in self.TightObjElectronWPs : self.TightObjElectronWPs[iWP].passWP(self.itree,iLep) 
      
               # Muon
               elif  abs(self.itree.std_vector_lepton_flavour[iLep]) == 13 :
                 for iWP in self.FakeObjMuonWPs  : self.FakeObjMuonWPs[iWP].passWP(self.itree,iLep)
                 for iWP in self.TightObjMuonWPs : self.TightObjMuonWPs[iWP].passWP(self.itree,iLep)

#             print iLep

#             LooseTag = 0
#             TightTag = 0 
#
#             for bname, bvector in self.newBranchesVector.iteritems():
#                bvector.clear()
#                if bname == 'std_vector_lepton_isLooseLepton' :
#                  bvector.push_back (LooseTag)
#                if bname == 'std_vector_lepton_isTightLepton' :
#                  bvector.push_back (TightTag)

       
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

 


