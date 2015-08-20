
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

class DM {
public:
 //! constructor
 DM(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 virtual ~DM() {}
 
 //! functions
 float dphillStar();
 float mllStar();
 
private:
 //! variables
 TLorentzVector L1,L2;
 TLorentzVector MET;
 float HiggsMass;
 
 bool isOk;
 
};

//! constructor
DM::DM(float pt1, float pt2, float phi1, float phi2, float met, float metphi) {
 
 HiggsMass = 125.0;
 
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

float DM::dphillStar(){
 
 if (isOk) {
  
  // Boost lepton system to rest in transverse plane, using MET
  
  float metpt = MET.Pt();
  float metphi = MET.Phi();
  
  float beta =  sqrt(metpt*metpt / (metpt*metpt + HiggsMass*HiggsMass));
  
  TVector3 BL (beta * cos(metphi), beta * sin(metphi), 0);
  
  TLorentzVector L1star,L2star;
  
  L1star = L1;
  L2star = L2;
  
  L1star.Boost(BL);
  L2star.Boost(BL);
  
  //Now, re-calculate the delta phi
  // in the new reference frame:
  return L1star.DeltaPhi(L2star);
 }
 else {
  return -9999.0;
 }
 
}




float DM::mllStar(){
 
 if (isOk) {
  
  // Boost lepton system to rest in transverse plane, using MET
  
  float metpt = MET.Pt();
  float metphi = MET.Phi();
  
  float beta =  sqrt(metpt*metpt / (metpt*metpt + HiggsMass*HiggsMass));
  
  TVector3 BL (beta * cos(metphi), beta * sin(metphi), 0);
  
  TLorentzVector L1star,L2star;
  
  L1star = L1;
  L2star = L2;
  
  L1star.Boost(BL);
  L2star.Boost(BL);
  
  //Now, re-calculate the mll
  // in the new reference frame:
  return (L1star + L2star).M();
 }
 else {
  return -9999.0;
 }
 
}




