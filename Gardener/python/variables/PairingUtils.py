from ROOT import TLorentzVector
from itertools import combinations
from operator import itemgetter, attrgetter
from math import cosh, sqrt

def get_hard_partons(event, debug=False):
    partons = []
    pids = []
    for pt, eta, phi, pid, isHard in    \
                zip(event.std_vector_partonGen_pt, event.std_vector_partonGen_eta,
                event.std_vector_partonGen_phi, event.std_vector_partonGen_pid,
                event.std_vector_partonGen_isHardProcess):
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

def get_jets(event, ptmin=20., debug=False):
    jets = []
    for pt, eta, phi, mass , in  zip(event.std_vector_jet_pt, 
                     event.std_vector_jet_eta, event.std_vector_jet_phi,
                     event.std_vector_jet_mass):
        if pt < ptmin or pt<0: 
            break
        if abs(eta) < 10 :
            p = pt * cosh(eta)
            en = sqrt(p**2 + mass**2)
            vec = TLorentzVector()
            vec.SetPtEtaPhiE(pt, eta, phi, en)
            # check if different from the previous one
            if debug:
                print "Jet > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
            jets.append(vec)
    return jets

def get_jets_byindex(event, indexes, ptmin=20., debug=False):
    jets = []
    for i, (pt, eta, phi, mass) , in  enumerate(zip(event.std_vector_jet_pt, 
                     event.std_vector_jet_eta, event.std_vector_jet_phi,
                     event.std_vector_jet_mass)):
                     
        if pt < ptmin or pt<0: 
            break
        if i in indexes:
            if abs(eta) < 10 :
                p = pt * cosh(eta)
                en = sqrt(p**2 + mass**2)
                vec = TLorentzVector()
                vec.SetPtEtaPhiE(pt, eta, phi, en)
                # check if different from the previous one
                if debug:
                    print "Jet > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
                jets.append(vec)
    return jets

def associate_vectors(jets, partons, dist):
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
        if results[0][njr] == -1 and distance <= dist:
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

    
def mjj_pairs(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], (vectors[i]+ vectors[k]).M() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l

def deltaeta_pairs(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], abs(vectors[i].Eta()- vectors[k].Eta()) ) )
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l

def deltaR_pairs(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], vectors[i].DeltaR(vectors[k])) )
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l

def max_deltaeta_pair(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], abs(vectors[i].Eta() - vectors[k].Eta())))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

def max_mjj_pair(vectors):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], (vectors[i]+ vectors[k]).M() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

def max_pt_pair(vectors):
    ''' Returns the pair with highest Pt'''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(( [i,k], (vectors[i]+ vectors[k]).Pt() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

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

def mass_of_nearest_mass_pair(vectors, mass):
    ''' Returns mass of the pair of vectors with invariant mass nearest to 
    the given mass'''
    l = []
    pair_mass = 0
    for i ,k  in combinations(range(len(vectors)),2):
        pair_mass = (vectors[i]+ vectors[k]).M()
        l.append(([i,k], abs(mass - pair_mass ), pair_mass))  
    l = sorted(l, key=itemgetter(1))
    return l[0][2]

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



#Functions to put in PairingUtils
def get_jets_and_bscore(event, ptmin=20., debug=False):
    jets = []
    b_scores = []

    for pt, eta, phi,mass, bvalue in  zip(event.std_vector_jet_pt, 
                     event.std_vector_jet_eta, event.std_vector_jet_phi, 
                     event.std_vector_jet_mass, event.std_vector_jet_DeepCSVB):

        if pt < 0 or pt < ptmin:
            break
        if abs(eta) < 10 :
            p = pt * cosh(eta)
            vec = TLorentzVector()
            en = sqrt(p**2 + mass**2)
            vec.SetPtEtaPhiE(pt, eta, phi, en)
            jets.append(vec)
            b_scores.append(bvalue)
    
    return jets, b_scores


def nearest_mass_pair_notH(vectors, mass, hpair):
    ''' Returns the pair of vectors with invariant mass nearest to 
    the given mass, checking if it isn't the bb pair '''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(([i,k], abs(mass - (vectors[i]+ vectors[k]).M() )))  
    l = sorted(l, key=itemgetter(1))
    for i in range(len(l)):
        if  l[i][0][0] != hpair[0] and l[i][0][0] != hpair[1]  and \
            l[i][0][1] != hpair[0] and l[i][0][1] != hpair[1]:
            return l[i][0]

def max_pt_pair_notH(vectors, hpair):
    ''' Returns the pair with highest Pt, , checking that it isn't the bb pair'''
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append(( [i,k], (vectors[i]+ vectors[k]).Pt() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    l = sorted(l, key=itemgetter(1))
    for i in range(len(l)):
        if l[i][0][0] != hpair[0] and l[i][0][0] != hpair[1] and \
           l[i][0][1] != hpair[0] and l[i][0][1] != hpair[1]:
            return l[i][0]

def min_deltaeta_pairs_notH(vectors, hpair):
    l = []
    for i ,k  in combinations(range(len(vectors)),2):
        l.append( ([i,k], abs(vectors[i].Eta()- vectors[k].Eta()) ) )
    l = sorted(l, key=itemgetter(1))
    for i in range(len(l)):
        if  l[i][0][0] != hpair[0] and l[i][0][0] != hpair[1] and \
            l[i][0][1] != hpair[0] and l[i][0][1] != hpair[1] :
            return l[i][0]

