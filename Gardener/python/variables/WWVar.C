
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
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass);

 void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 
 //! functions
 float pTWW();
 float dphill();
 float mll();
 float pt1();
 float pt2();
 float eta1();
 float eta2();
 float phi1();
 float phi2();
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
 float projpfmet();
 
 float mth();
 float mcoll();
 float dphillmet();
 float channel();
 float mjj();
 float detajj();
 float dphijj();
 float njet();
  
 //---- to reject Wg*
 float mllThird();
 
 
private:
 //! variables
 TLorentzVector L1,L2,L3;
 TLorentzVector MET;
 TLorentzVector J1, J2;
 float pid1, pid2;
 
 bool isOk;
 int  jetOk;
 
 std::vector<float> _jetspt;
 std::vector<float> _jetseta;
 std::vector<float> _jetsphi;
 std::vector<float> _jetsmass;

 std::vector<float> _leptonspt;
 std::vector<float> _leptonseta;
 std::vector<float> _leptonsphi;
 std::vector<float> _leptonsflavour;
 
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
 jetOk = 0;
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
 jetOk = 0;
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
 jetOk = 0;
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
 if( jetpt1>0) {
  J1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, jetmass1); //---- NB: jets are treated as massive
  if( jetpt2>0) {
   J2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, jetmass2); //---- NB: jets are treated as massive
   jetOk = 2;
  }
  else {
   jetOk = 1;
  }
 }
 
}


//! set functions

void WW::setJets(std::vector<float> invectorpt ) {
 _jetspt = invectorpt;
 jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta) {
 _jetspt  = invectorpt;
 _jetseta = invectoreta;
 jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass) {
 _jetspt   = invectorpt;
 _jetseta  = invectoreta;
 _jetsphi  = invectorphi;
 _jetsmass = invectormass;

 //---- need to update J1 and J2
 if (( _jetspt.size() > 1 && _jetspt.at(0) > 0 && _jetspt.at(1) <= 0 ) || ( _jetspt.size() == 1 && _jetspt.at(0) > 0)) {
  J1.SetPtEtaPhiM(_jetspt.at(0), _jetseta.at(0), _jetsphi.at(0), _jetsmass.at(0)); //---- NB: jets are treated as massive
  jetOk = 1;
 }
 else if ( _jetspt.size() > 1 && _jetspt.at(0) > 0 && _jetspt.at(1) > 0 ) {
  J1.SetPtEtaPhiM(_jetspt.at(0), _jetseta.at(0), _jetsphi.at(0), _jetsmass.at(0)); //---- NB: jets are treated as massive
  J2.SetPtEtaPhiM(_jetspt.at(1), _jetseta.at(1), _jetsphi.at(1), _jetsmass.at(1)); //---- NB: jets are treated as massive
  jetOk = 2;
 }
 else { 
  jetOk = 0;  //---- protection
 }
}

void WW::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 _leptonspt      = invectorpt;
 _leptonseta     = invectoreta;
 _leptonsphi     = invectorphi;
 _leptonsflavour = invectorflavour;
 
 //---- need to update L1 and L2
 if ( _leptonspt.size() > 0 && _leptonspt.at(0) > 0 ) {
  L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0); //---- NB: leptons are treated as massless
 }
 if ( _leptonspt.size() > 1 && _leptonspt.at(1) > 0 ) {
  L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0); //---- NB: leptons are treated as massless
 }
 if ( _leptonspt.size() > 2 && _leptonspt.at(2) > 0 ) {
  L3.SetPtEtaPhiM(_leptonspt.at(2), _leptonseta.at(2), _leptonsphi.at(2), 0); //---- NB: leptons are treated as massless
 }
 
}



void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);



//! functions

float WW::njet(){
 float njet = 0;
 for (int ijet=0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 30 && fabs(_jetseta.at(ijet))<4.7) {
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
  return fabs(L1.DeltaPhi(L2));
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
 if (isOk && jetOk >= 1) {
  return  fabs( (L1+L2).DeltaPhi(J1) );
 }
 else {
  return -9999.0;
 }
}


float WW::dphilljetjet(){ 
 if (isOk && jetOk >= 2) {
   return  fabs( (L1+L2).DeltaPhi(J1+J2) );
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet(){ 
 if (isOk) {
  float d1 = fabs((L1).DeltaPhi(MET));
  float d2 = fabs((L2).DeltaPhi(MET));
  if (d1<d2) return d1;
  else       return d2;
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet1(){ 
 if (isOk) {
  return fabs((L1).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}

float WW::dphilmet2(){ 
 if (isOk) {
  return fabs((L2).DeltaPhi(MET));
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


float WW::projpfmet(){
 
  if (isOk) {
    if (dphilmet() < TMath::Pi() / 2.)
      return sin(dphilmet()) * MET.Pt();
    else
      return MET.Pt();
  }
  else {
    return -9999.0;
  }
}


//---- pt
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

//---- eta
float WW::eta1(){
 
 if (isOk) {
  return L1.Eta();
 }
 else {
  return -9999.0;
 }
}


float WW::eta2(){
 
 if (isOk) {
  return L2.Eta();
 }
 else {
  return -9999.0;
 } 
}

//---- phi
float WW::phi1(){
 
 if (isOk) {
  return L1.Phi();
 }
 else {
  return -9999.0;
 }
}


float WW::phi2(){
 
 if (isOk) {
  return L2.Phi();
 }
 else {
  return -9999.0;
 } 
}


//---- mll
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


float WW::mcoll(){
 
 if (isOk) {
  
  //---- project met to lepton direction
  float et_par_1 = MET.Pt() * cos ( fabs( (L1).DeltaPhi(MET) ) );
  float et_par_2 = MET.Pt() * cos ( fabs( (L2).DeltaPhi(MET) ) ); 
  
  TLorentzVector L1_enhanced,L2_enhanced;
  
  L1_enhanced.SetPtEtaPhiM(pt1() + et_par_1, eta1(), phi1(), 0.);
  L2_enhanced.SetPtEtaPhiM(pt2() + et_par_2, eta2(), phi2(), 0.);
  
  return (L1_enhanced + L2_enhanced).M();

  
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
 
 if (jetOk >= 2) {
  return (J1+J2).M();
 }
 else {
  return -9999.0;
 }
}


float WW::detajj(){
 
 if (jetOk >= 2) {
  return abs(J1.Eta()-J2.Eta());
 }
 else {
  return -9999.0;
 } 
}


float WW::dphijj(){
 if (isOk) {
  return fabs(J1.DeltaPhi(J2));
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





//---- to reject Wg*

float WW::mllThird(){
 
 if (isOk) {
  
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   float newmll = - 9999.0;
   float mll13 = -9999.0;
   float mll23 = -9999.0;
   
   //---- same flavour and different charge
   if (fabs(flav1) == fabs(flav3) && flav1*flav3<0) {
    mll13 = (L1+L3).M();
   }
   if (fabs(flav2) == fabs(flav3) && flav2*flav3<0) {
    mll23 = (L2+L3).M();
   }
   
   //---- if both are ok (what the hell is it possible??? ... after it should not be possible, since I require ch1*ch2<0 !)
   //---- take the minimum of the two   
   if (mll23 >= 0 && mll13 >= 0) {
    if (mll23<mll13) { newmll = mll23; }
    else             { newmll = mll13; }
   }
   else {
    if (mll13 >= 0) { newmll = mll13; }
    if (mll23 >= 0) { newmll = mll23; }
   }
   return newmll;
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
  
}




