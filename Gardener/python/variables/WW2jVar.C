
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

class WW2j {
public:
 //! constructor
 WW2j(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2,     float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2);
 virtual ~WW2j() {}
 
 //! functions
 float Mljcloser();
 float Mljfarther();
 float Mlj(int l, int j);
 
private:
 //! variables
 TLorentzVector L1,L2;
 TLorentzVector J1,J2;
 
};

//! constructor
WW2j::WW2j(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2,     float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2) {
 
 L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
 L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
 
 if (jetpt1 > 0) {
  J1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, 0.);
 } else {
  J1.SetPtEtaPhiM(jetpt1, 0., 0., 0.);
 }
 
 if (jetpt2 > 0) {
  J2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, 0.);
 }
 else {
  J2.SetPtEtaPhiM(jetpt2, 0., 0., 0.);
 }
 
 //  std::cout << " pt1, eta1, phi1 = " << pt1 << ", " << eta1 << ", " << phi1  << ", " << std::endl;
 //  std::cout << " pt2, eta2, phi2 = " << pt2 << ", " << eta2 << ", " << phi2  << ", " << std::endl;
 //
 //  std::cout << " jetpt1, jeteta1, jetphi1 = " << jetpt1 << ", " << jeteta1 << ", " << jetphi1  << ", " << std::endl;
 //  std::cout << " jetpt2, jeteta2, jetphi2 = " << jetpt2 << ", " << jeteta2 << ", " << jetphi2  << ", " << std::endl;
 
}

//! functions

float WW2j::Mljcloser(){
 
 if (J2.Pt() > 0) {
  float DR_l1_j1 = L1.DeltaR(J1); //-- 0
  float DR_l1_j2 = L1.DeltaR(J2); //-- 1
  float DR_l2_j1 = L2.DeltaR(J1); //-- 2
  float DR_l2_j2 = L2.DeltaR(J2); //-- 3
  
  int min = -1;
  float minalue = 1000; 
  if (DR_l1_j1<DR_l1_j2) {min = 0; minalue = DR_l1_j1;} else {min = 1; minalue = DR_l1_j2;} 
  if (DR_l2_j1< minalue) {min = 2; minalue = DR_l2_j1;}
  if (DR_l2_j2< minalue) {min = 3; minalue = DR_l2_j2;}
  
  if (min == 0) {return (L1+J1).M();}
  if (min == 1) {return (L1+J2).M();}
  if (min == 2) {return (L2+J1).M();}
  if (min == 3) {return (L2+J2).M();}
 }
 else {
  return -1;
 }
}


float WW2j::Mljfarther(){
 
 if (J2.Pt() > 0) {
  float DR_l1_j1 = L1.DeltaR(J1); //-- 0
  float DR_l1_j2 = L1.DeltaR(J2); //-- 1
  float DR_l2_j1 = L2.DeltaR(J1); //-- 2
  float DR_l2_j2 = L2.DeltaR(J2); //-- 3
  
  int min = -1;
  float minalue = 1000; 
  if (DR_l1_j1<DR_l1_j2) {min = 0; minalue = DR_l1_j1;} else {min = 1; minalue = DR_l1_j2;} 
  if (DR_l2_j1< minalue) {min = 2; minalue = DR_l2_j1;}
  if (DR_l2_j2< minalue) {min = 3; minalue = DR_l2_j2;}
  
  //---- the other pairs
  if (min == 0) {return (L2+J2).M();}
  if (min == 1) {return (L2+J1).M();}
  if (min == 2) {return (L1+J2).M();}
  if (min == 3) {return (L1+J1).M();}
 }
 else {
  return -1;
 }
 
}




float WW2j::Mlj(int l, int j){
 
 if (J2.Pt() > 0) {
  if (l==1 && j==1) {
   return (L1+J1).M();
  }
  else if (l==1 && j==2) {
   return (L1+J2).M();
  }
  else if (l==2 && j==1) {
   return (L2+J1).M();
  }
  else if (l==2 && j==2) {
   return (L2+J2).M();
  }
  else {
   return -1;
  }
 }
 else {
  return -1;
 }
}





