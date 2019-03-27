import optparse
import numpy
import ROOT
import os.path
from ROOT import TLorentzVector
from itertools import combinations
from operator import itemgetter, attrgetter

from LatinoAnalysis.Gardener.gardening import TreeCloner

def get_hard_partons(event, debug=False):
    partons = []
    pids = []
    for pt, eta, phi, pid, isHard in    \
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
                    print "Parton > pid: ", pid, " pt:", pt ," eta:", eta, " phi:", phi
                partons.append(vec)
                pids.append(int(pid))
    return partons, pids

def get_jets(event, debug=False):
    jets = []
    for pt, eta, phi in  zip(event.std_vector_jet_pt, 
                     event.std_vector_jet_eta, event.std_vector_jet_phi):
        if abs(eta) < 10 :
            p = pt * cosh(eta)
            vec = TLorentzVector()
            vec.SetPtEtaPhiE(pt, eta, phi, p)
            # check if different from the previous one
            if debug:
                print "Jet > pid: ", pid, " pt:", pt ," eta:", eta, " phi:", phi
            jets.append(vec)
    return jets
        

def associate_vectors(jets, partons, params):
    ''' The params influences the flag of the event:
    0 = OK
    1 = Overlapping partons
    2 = At least one parton not associated 
    '''
    flag = 0
    ntotjets = len(jets)
    ntotpartons = len(partons)
    comb = []
    for nj, j in enumerate(jets):
        for njr, jr in enumerate(partons):
            comb.append( (nj, njr, j.DrEtaPhi(jr)))
    comb = sorted(comb, key=itemgetter(2))
    results = [[-1]*ntotpartons,[0.]*ntotpartons]
    assigned_part = 0
    for nj, njr, distance  in comb:        
        # the jet can be reused if the parton
        # is nearer than the max_distance
        if results[0][njr] == -1 and distance <= params["max_distance"]:
                if nj in results[0]:
                    # the jet is already associated with a parton
                    # This is an overlapping parton
                    flag = 1
                results[0][njr] = nj
                results[1][njr] = distance 
                assigned_part+=1
        if assigned_part == ntotpartons:
            break  #early exit when partons are all assigned
    # Check if at least one parton is not associated
    if -1 in results[0]:
        flag = 2
    return results, flag

def nearest_mass_pair(vectors, mass):
    ''' Returns the pair of vectors with invariant mass nearest to 
    the given mass '''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(([i,k], abs(mass - (vectors[i]+ vectors[k]).M() )))  
    l = sorted(l, key=itemgetter(1))
    return l[0][0]
    
def nearest_masses_pair(vectors, masses):
    ''' Returns the pair of vectors with invariant mass nearest to one of the 
    masses in the parameter'''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        distances= [abs(mass - (vectors[i]+ vectors[k]).M() ) for mass in masses]
        l.append(([i,k], min(distances)))  
    l = sorted(l, key=itemgetter(1))
    return l[0][0]

def nearest_R_pair(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(([i,k], vectors[i].DeltaR(vectors[k]) ))  
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]
    
def get_nearest_vector(target, vectors):
    ''' Return the nearest vector from target in the vectors list'''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(([i,k], vectors[i].DeltaR(target) ))  
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0][0]



class jetPairingGen(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Identify pairs of jets for semileptonic analyses'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-a', '--analysis',  dest='analysis',  help='Analysis (HH, VBS)',  default='VBS')
        group.add_option('-d', '--debug',  dest='debug',  help='Debug flag',  default="0")
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.analysis = opts.analysis
        self.debug = (opts.debug == "1")
        print "Working for analysis: ", self.analysis

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["hasTopGen" ]
        if self.analysis == "VBS:
            newbranches += ["V_jets", "VBS_jets"]
        elif self.analysis == "HH:
            newbranches += ["V_jets", "H_jets"]

        self.clone(output,newbranches)
        
        hasTopGen = numpy.zeros(1, dtype=numpy.float32)
        V_jets = numpy.zeros(2, dtype=numpy.int32)
        self.otree.Branch('hasTopGen',  hasTopGen,  'hasTopGen/F')
        self.otree.Branch('V_jets',  V_jets,  'V_jets/I')

        if self.analysis == "VBS:
            VBS_jets = numpy.zeros(2, dtype=numpy.int32)
            self.otree.Branch('VBS_jets',  VBS_jets,  'VBS_jets/I')
        elif self.analysis == "HH":
            H_jets = numpy.zeros(2, dtype=numpy.int32)
            self.otree.Branch('H_jets',  H_jets,  'H_jets/I')
        
    
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            partons, pids = get_hard_partons(itree, self.debug)
            if 6 in pids or -6 in pids:
                hasTopGen = 1.
            else:
                hasTopGen = 0.

            jets =  get_jets(itree, self.debug)

            if self.analysis == "VBS":
                
                # Get pair of partons nearest to 
                # get the pair nearest  to W or Z mass
                vpair = nearest_masses_pair(jets, [80.385, 91.1876])
                print(vpair)
                v_partons = [partons.pop(vpair[0]), partons.pop(vpair[1]-1)]
                vbs_partons = partons
                

            
            
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

