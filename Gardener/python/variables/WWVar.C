
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

class WW {
public:
 //! constructor
 WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 virtual ~WW() {}
 
 //! functions
 float pTWW();
 
private:
 //! variables
 TLorentzVector L1,L2;
 TLorentzVector MET;
 
 bool isOk;
 
};

//! constructor
WW::WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, 0, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, 0, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  isOk =  true;
 }
 else {
  isOk = false;
 }
 
}

//! functions

float WW::pTWW(){
 
 if (isOk) {
  return (L1+L2+MET).pT();
 }
 else {
  return -9999.0
 }
 
}





