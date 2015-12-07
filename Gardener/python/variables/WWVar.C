
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

#include <TMinuit.h>
#include <vector>


class WW {
public:
 //! constructor
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2);
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi);
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi);
 WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 virtual ~WW() {}
 
 //! set functions
 void setJets(std::vector<float> invector);
 
 //! functions
 float pTWW();
 float dphill();
 float mll();
 float pt1();
 float pt2();
 float mT2();  //void functionMT2(int& npar, double* d, double& r, double par[], int flag);
 float yll();
 float ptll();
 float drll();
 
 float dphilljet();
 float dphilljetjet();
 float dphilmet();
 float dphilmet1();
 float dphilmet2();
 float mtw1();
 float mtw2();
 float pfmet();
 
 float mth();
 float dphillmet();
 float channel();
 float mjj();
 float detajj();
 float njet();
  
 
private:
 //! variables
 TLorentzVector L1,L2;
 TLorentzVector MET;
 TLorentzVector J1, J2;
 float pid1, pid2;
 
 bool isOk, jetOk;
 
 std::vector<float> jetspt;
 
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
 jetOk = false;
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  isOk =  true;
 }
 else {
  isOk = false;
 }
 jetOk = false;
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  pid1 = pidl1;
  pid2 = pidl2;
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  isOk =  true;
 }
 else {
  isOk = false;
 }
 jetOk = false;
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  pid1 = pidl1;
  pid2 = pidl2;
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  isOk =  true;
 }
 else {
  isOk = false;
 }
 if( jetpt1>0 && jetpt2 > 0) {
  J1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, jetmass1); //---- NB: jets are treated as massive
  J2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, jetmass2); //---- NB: jets are treated as massive
  jetOk = true;
 }
}

//! set functions

void WW::setJets(std::vector<float> invector) {
 jetspt = invector;
}



//! functions

float WW::njet(){
 float njet = 0;
 for (int ijet=0; ijet < jetspt.size(); ijet++) {
  if (jetspt.at(ijet) > 30) {
   njet += 1;
  }
 }
 return njet; 
}


float WW::ptll(){
 if (isOk) {
  return (L1+L2).Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::yll(){
 if (isOk) {
  return (L1+L2).Rapidity();
 }
 else {
  return -9999.0;
 }
}


float WW::pTWW(){ 
 if (isOk) {
  return (L1+L2+MET).Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::dphill(){
 if (isOk) {
  return L1.DeltaPhi(L2);
 }
 else {
  return -9999.0;
 } 
}


float WW::drll(){
 //---- https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00469
 if (isOk) {
  return L1.DeltaR(L2);
 }
 else {
  return -9999.0;
 } 
}

float WW::dphilljet(){ 
 if (isOk) {
  return  fabs( (L1+L2).DeltaPhi(J1) );
 }
 else {
  return -9999.0;
 }
}


float WW::dphilljetjet(){ 
 if (isOk) {
  return  fabs( (L1+L2).DeltaPhi(J1+J2) );
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet(){ 
 if (isOk) {
  float d1 = (L1).DeltaPhi(MET);
  float d2 = (L2).DeltaPhi(MET);
  if (d1<d2) return d1;
  else       return d2;
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet1(){ 
 if (isOk) {
  return (L1).DeltaPhi(MET);
 }
 else {
  return -9999.0;
 }
}

float WW::dphilmet2(){ 
 if (isOk) {
  return (L2).DeltaPhi(MET);
 }
 else {
  return -9999.0;
 }
}


float WW::mtw1(){ 
 if (isOk) {
  return sqrt(2 * pt1() * pfmet() * (1 - cos( dphilmet1() )));
 }
 else {
  return -9999.0;
 }
}


float WW::mtw2(){ 
 if (isOk) {
  return sqrt(2 * pt2() * pfmet() * (1 - cos( dphilmet2() )));
 }
 else {
  return -9999.0;
 }
}





float WW::pfmet(){
 
 if (isOk) {
  return MET.Pt();
 }
 else {
  return -9999.0;
 }
}





float WW::pt1(){
 
 if (isOk) {
  return L1.Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::pt2(){
 
 if (isOk) {
  return L2.Pt();
 }
 else {
  return -9999.0;
 } 
}


float WW::mll(){
 
 if (isOk) {
  return (L1+L2).M();
 }
 else {
  return -9999.0;
 }
 
}

float WW::dphillmet(){
 
 if (isOk) {
  return  fabs( (L1+L2).DeltaPhi(MET) );
 }
 else {
  return -9999.0;
 }
 
}

float WW::mth(){
 
 if (isOk) {
  return sqrt( 2. * ptll() * MET.Pt() * ( 1. - cos (dphillmet()) ));
//   AN 2011/155, v2, p19
//   sqrt( 2 * pTll() * met(metToUse) * ( 1 - cos(dPhillMet(metToUse)) ) );
 }
 else {
  return -9999.0;
 }
 
}

float WW::channel(){
 
 if (isOk) {
  if( abs(pid1) == 11 ) {
      if( abs(pid2) == 11 ) return 1; // ee
      else if( abs(pid2) == 13 ) return 2; // em
      else return -9999.0;
  }
  else if( abs(pid1) == 13 ){
      if( abs(pid2) == 11 ) return 3; // me
      else if( abs(pid2) == 13 ) return 0; // mm
      else return -9999.0;
  }
  else {
   return -9999.0;
  }
 }
 else {
   return -9999.0;
  }
 
}

// Jet Functions
float WW::mjj(){
 
 if (jetOk) {
  return (J1+J2).M();
 }
 else {
  return -9999.0;
 }
}


float WW::detajj(){
 
 if (jetOk) {
  return abs(J1.Eta()-J2.Eta());
 }
 else {
  return -9999.0;
 } 
}







//
//              __ __| ___ \
//      __ `__ \   |      ) |
//      |   |   |  |     __/
//     _|  _|  _| _|   _____|
//
//


//---- global variable, used for minuit ----
std::vector<double>* VectX = new std::vector<double>;



//---- max (mt_1,mt_2) ----
void functionMT2(int& npar, double* d, double& r, double par[], int flag){
 int n = VectX->size();
 double maxmt2 = 0.0;
 
 
 double px1 = VectX->at(0);
 double py1 = VectX->at(1);
 double px2 = VectX->at(2);
 double py2 = VectX->at(3);
 double metx = VectX->at(4);
 double mety = VectX->at(5);
 
 double met1    = par[0];
 double metphi1 = par[1];
 double metx1 = met1 * cos (metphi1);
 double mety1 = met1 * sin (metphi1);
 
 double metx2 = metx - metx1;
 double mety2 = mety - mety1;
 double met2 = sqrt(metx2*metx2 + mety2*mety2);
 
 double p1 = sqrt(px1*px1 + py1*py1);
 double p2 = sqrt(px2*px2 + py2*py2);
 double mt1 = 2. * p1 * met1 * (1.-(px1*metx1+py1*mety1)/(p1*met1));
 double mt2 = 2. * p2 * met2 * (1.-(px2*metx2+py2*mety2)/(p2*met2));
 
 if (mt1>mt2) maxmt2 = mt1;
 else maxmt2 = mt2;
 
 r = sqrt(maxmt2);
}


float WW::mT2(){
 
 if (isOk) {
  
  if (VectX->size() != 6) { 
   VectX->push_back( L1.X()  );
   VectX->push_back( L1.Y()  );
   VectX->push_back( L2.X()  );
   VectX->push_back( L1.Y()  );
   VectX->push_back( MET.X() );
   VectX->push_back( MET.Y() );
  }
  else {
   VectX->at(0) = L1.X()  ;
   VectX->at(1) = L1.Y()  ;
   VectX->at(2) = L2.X()  ;
   VectX->at(3) = L1.Y()  ;
   VectX->at(4) = MET.X() ;
   VectX->at(5) = MET.Y() ;
  }
  
  double mT2 = 0.;
  
  double met = 10;
  double PI = 3.14159266;
  
  const int nParametri = 2;
  TMinuit minuit(nParametri);
  minuit.SetFCN(functionMT2);
  
  minuit.SetPrintLevel(-1); // quiet
  
  met = MET.E();
  
  double par[nParametri]={met/2.,0.0};
  double stepSize[nParametri]={met/100.,0.001};
  double minVal[nParametri]={met/100.,0.0};
  double maxVal[nParametri]={30.*met,2.*PI};
  string parName[nParametri]={"met1","metphi1"};
  for (int i=0; i<nParametri; i++){
   minuit.DefineParameter(i,parName[i].c_str(),par[i],stepSize[i],minVal[i],maxVal[i]);
  }
  
  minuit.Migrad();
  //  double outParametri[nParametri];
  //  double errParametri[nParametri];
  //  for (int i=0; i<nParametri; i++){
  //   minuit.GetParameter(i,outParametri[i],errParametri[i]);
  //   std::cout << "outParametri[" << i << "] = " << outParametri[i] << " +/- " << errParametri[i] << std::endl;
  //  }
  
  mT2 = minuit.fAmin;
  //  std::cout << " "  << pxl1 << " ; " << pyl1 << " ; " << pxl2 << " ; " << pyl2 << " ; " << metx << " ; " << mety << " --> mT2 = " << mT2 << std::endl;
  return mT2;
  
 }
 else {
  return -9999.0;
 }
 
}







