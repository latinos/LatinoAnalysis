from math import *
from ROOT import TLorentzVector

def reconstruct_neutrino(muon, met, type="pz_mu"):
    a = 80**2 - muon.M()**2 + 2*(muon.Px()*met.Px() 
                                + muon.Py()*met.Py())
    A = 4*(muon.E()**2  - muon.Pz()**2)
    B = -4 * a * muon.Pz()
    C = 4*(muon.E()**2) * (met.Pt()**2) - a**2
    delta = B**2 -4*A*C

    pz = 0
    px = met.Px()
    py = met.Py()

    if delta>=0:
        sols =  ((-B + sqrt(delta))/(2*A),
                 (-B - sqrt(delta))/(2*A))

        if type == "pz_mu&central":
            if abs(sols[0] - muon.Pz())< abs(sols[1] - muon.Pz()):
                pz = sols[0]
            else:
                pz = sols[1]
            # Check the pt
            if (pz > 300):
                # Take the most central one
                if abs(sols[0]) < abs(sols[1]):
                    pz = sols[0]
                else:
                    pz = sols[1]
        elif type == "pz_mu":
            if abs(sols[0] - muon.Pz()) < abs(sols[1] - muon.Pz()):
                pz = sols[0]
            else:
                pz = sols[1]
        elif type == "central":
            if abs(sols[0]) < abs(sols[1]):
                pz = sols[0]
            else:
                pz = sols[1]
    else:
        pz = -B/(2*A)
        pt = _calculate_pt_neutrino(muon, met)
        px = pt * cos(met.Phi())
        py = pt * sin(met.Phi())
    
    # return neutrino vector
    nu = TLorentzVector(px, py, pz, sqrt(px**2+py**2+pz**2))
    return nu


def reconstruct_neutrino_recursive(muon, met, type="pz_mu", corr=False):
    a = 80**2 - muon.M()**2 + 2*(muon.Px()*met.Px() 
                                + muon.Py()*met.Py())
    A = 4*(muon.E()**2  - muon.Pz()**2)
    B = -4 * a * muon.Pz()
    C = 4*(muon.E()**2) * (met.Pt()**2) - a**2
    delta = B**2 -4*A*C

    pz = 0
    px = met.Px()
    py = met.Py()

    if delta>=0:
        sols =  ((-B + sqrt(delta))/(2*A),
                 (-B - sqrt(delta))/(2*A))

        if type == "pz_mu&central":
            if abs(sols[0] - muon.Pz())< abs(sols[1] - muon.Pz()):
                pz = sols[0]
            else:
                pz = sols[1]
            # Check the pt
            if (pz > 300):
                # Take the most central one
                if abs(sols[0]) < abs(sols[1]):
                    pz = sols[0]
                else:
                    pz = sols[1]
        elif type == "pz_mu":
            if abs(sols[0] - muon.Pz()) < abs(sols[1] - muon.Pz()):
                pz = sols[0]
            else:
                pz = sols[1]
        elif type == "central":
            if abs(sols[0]) < abs(sols[1]):
                pz = sols[0]
            else:
                pz = sols[1]
    else:
        #pz = -B/(2*A)
        pt = _calculate_pt_neutrino(muon, met)
        px = pt * cos(met.Phi())
        py = pt * sin(met.Phi())
        newnu = TLorentzVector(px, py, 0, sqrt(px**2+py**2))
        return reconstruct_neutrino_recursive(muon, newnu, corr=True)

    # return neutrino vector
    nu = TLorentzVector(px, py, pz, sqrt(px**2+py**2+pz**2))
    return (nu, corr)



def _calculate_pt_neutrino(muon, met):
    alfa = muon.Pt()*cos(met.Phi()- muon.Phi())
    a = 4*(muon.Pz()**2 - muon.E()**2 + alfa**2)
    b = 4*alfa
    c = 80**2 - muon.M()**2

    sols = ((-b + sqrt(b**2 -4*a*c) )/(2*a) ,
            (-b - sqrt(b**2 -4*a*c) )/(2*a) )

    if abs(sols[0] - met.Pt()) < abs(sols[1] -met.Pt()):
        return sols[0]
    else:
        return sols[1]