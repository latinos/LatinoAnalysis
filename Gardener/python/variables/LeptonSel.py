#
#  Lepton WP Code  
#  author: X. Janssen   
#                                

from LatinoAnalysis.Gardener.gardening import TreeCloner
import ROOT
import optparse

class ElectronWP():

    def __init__ (self):
      print "-------- ElectronWP init() ---------"  
      self.ptMin   =  0.
      self.etaMax  = 2.5

      self.cut  = "    ( itree.std_vector_lepton_pt[$ILEP] >       " + str(self.ptMin)  + " )" 
      self.cut += "and ( abs(itree.std_vector_lepton_eta[$ILEP]) < " + str(self.etaMax) + " )"
      print self.cut

    def _passWP(self,itree,iLep):

      return eval(self.cut.replace('$ILEP',str(iLep)))


class MuonWP():

    def __init__ (self):
      print "-------- MuonWP init() ---------"  
      self.ptMin   =  0.
      self.etaMax  = 2.4

      self.cut  = "    ( itree.std_vector_lepton_pt[$ILEP] >       " + str(self.ptMin)  + " )"      
      self.cut += "and ( abs(itree.std_vector_lepton_eta[$ILEP]) < " + str(self.etaMax) + " )"
      print self.cut

    def _passWP(self,itree,iLep):

      return eval(self.cut.replace('$ILEP',str(iLep))) 


class LeptonSel(TreeCloner):

    def __init__(self):
       pass

    def help(self):
       return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='Full2016', type='string') 

    def checkOptions(self,opts):
        
        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
     
        self.ElectronWPs = []
        self.MuonWPs     = []
        self.ElectronWPs .append(ElectronWP())
        self.MuonWPs     .append(MuonWP()) 

    def passWP(self,iLep):
        if   abs(self.itree.std_vector_lepton_flavour[iLep]) == 11 : return self.ElectronWPs[0]._passWP(self.itree,iLep)
        elif abs(self.itree.std_vector_lepton_flavour[iLep]) == 13 : return self.MuonWPs[0]._passWP(self.itree,iLep)
        else : return False 


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

            print self.passWP(0)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

              LooseTag = 0
              TightTag = 0 

              for bname, bvector in self.newBranchesVector.iteritems():
                 bvector.clear()
                 if bname == 'std_vector_lepton_isLooseLepton' :
                   bvector.push_back (LooseTag)
                 if bname == 'std_vector_lepton_isTightLepton' :
                   bvector.push_back (TightTag)

       
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

 


