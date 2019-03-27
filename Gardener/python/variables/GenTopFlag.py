import optparse
import numpy
import ROOT
import os.path
from ROOT import TLorentzVector

from LatinoAnalysis.Gardener.gardening import TreeCloner

def get_hard_partons(event, debug=False):
    partons = []
    pids = []
    for i, (pt, eta, phi, pid, isHard) in enumerate(
            zip(event.std_vector_partonGen_pt, event.std_vector_partonGen_eta,
                event.std_vector_partonGen_phi, event.std_vector_partonGen_pid,
                event.std_vector_partonGen_isHardProcess)):
        if isHard==1 and abs(eta) < 10 :
            p = pt * cosh(eta)
            vec = TLorentzVector()
            vec.SetPtEtaPhiE(pt, eta, phi, p)
            # check if different from the previous one
            if len(partons)==0 or vec != partons[-1]:
                if debug:
                    print "pid: ", pid, " pt:", pt ," eta:", eta, " phi:", phi
                partons.append(vec)
                pids.append(int(pid))
    return partons, pids


class GetTopFlag(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Identify pairs of jets for semileptonic analyses'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["hasTopGen"]

        self.clone(output,newbranches)
        
        hasTopGen = numpy.zeros(1, dtype=numpy.float32)
        self.otree.Branch('hasTopGen',  hasTopGen,  'hasTopGen/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            partons,pids = get_hard_partons(itree)
            if 6 in pids or -6 in pids:
                hasTopGen = 1.
            else:
                hasTopGen = 0.
            
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

