
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

class XWW {
public:
 //! constructor
 XWW(float pt1, float pt2, float phi1, float phi2, float eta1, float eta2, float met=0, float metphi=0);
 virtual ~XWW() {}
 
 //! functions
 float M2l();
 
private:
 //! variables
 TLorentzVector L1,L2;
 TLorentzVector MET;
 TLorentzVector L1_double,L2_double;
 TLorentzVector X;
 
 float WMass;
 
 bool isOk;
 
};

//! constructor
XWW::XWW(float pt1, float pt2, float phi1, float phi2, float eta1, float eta2, float met, float metphi) {
 
 WMass = 80.4; // GeV
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  isOk =  true;
 }
 else {
  isOk = false;
 }
 
}

//! functions

float XWW::M2l(){
 
 if (isOk) {
  
  //---- hypothesis of neutrinos collinear to leptons
  //----  and neutrino energy ~ lepton energy
  //----  plus mW masss
  
  L1_double.SetPtEtaPhiM(2*L1.Pt(), L1.Eta(), L1.Phi(), WMass);
  L2_double.SetPtEtaPhiM(2*L2.Pt(), L2.Eta(), L2.Phi(), WMass);
  
  X = L1_double + L2_double;
  
  //Now calculate X invariant mass
  return X.M();
 }
 else {
  return -9999.0;
 }
 
}





