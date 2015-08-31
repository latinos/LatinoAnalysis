
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

#include <TMinuit.h>
#include <vector>


class WW {
public:
 //! constructor
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi);
 WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 virtual ~WW() {}
 
 //! functions
 float pTWW();
 float dphill();
 float mll();
 float pt1();
 float pt2();
 float mT2();  //void functionMT2(int& npar, double* d, double& r, double par[], int flag);
 float yll();
 float ptll();
 float mth();
 float dphillmet();
 
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
 
}

//! functions

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







