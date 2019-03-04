
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

#include <TMinuit.h>
#include <vector>


class WW {
public:
 //! constructor
 WW();
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2);
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi);
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi);
 WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi, float metsum, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2);
 virtual ~WW() {}
 
 //! check
 void checkIfOk();
  
 //! set functions
 void setJets(std::vector<float> invector);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass);

 void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 
 void setMET   (float met, float metphi);
 void setTkMET (float met, float metphi);
 void setSumET (float summet);
 
 //! functions
 float recoil();
 float jetpt1_cut();
 float jetpt2_cut();
 float dphilljet_cut();
 float dphilljetjet_cut();
 float dphijet1met_cut();
 float dphijet2met_cut();
 float PfMetDivSumMet();
 float upara();
 float uperp();
 float m2ljj20();
 float m2ljj30();

 float pTWW();
 float mTi();
 float mTe();
 float choiMass();
 float mT2();  //void functionMT2(int& npar, double* d, double& r, double par[], int flag);

 float dphill();
 float mll();
 float pt1();
 float pt2();
 float eta1();
 float eta2();
 float phi1();
 float phi2();
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
 float dphiltkmet();
 float projtkmet();
 float mpmet();
 
 float mth();
 float mcoll();
 float mcollWW();
 float mR();
 float dphillmet();
 float channel();
 float mjj();
 float detajj();
 float dphijj();
 float njet();

 float dphijet1met();  
 float dphijet2met();  
 float dphijjmet();    
 float dphijjmet_cut();    
 float dphilep1jet1(); 
 float dphilep1jet2(); 
 float dphilep2jet1(); 
 float dphilep2jet2(); 

 float vht_pt();
 float vht_phi();
 float ht();
 
 //---- to reject Wg*
 float mllThird();
 float mllWgSt();
 float drllWgSt();
 //int   WgSt_channel(){return _WgSt_channel;}
 float mllOneThree();
 float mllTwoThree();
 float drllOneThree();
 float drllTwoThree();
 
 //---- for VBF training
 float ptTOT_cut();
 float mTOT_cut();
 float OLV1_cut();
 float OLV2_cut();
 float Ceta_cut();
 
//whss
 float mlljj20_whss();
 float mlljj30_whss();
 
private:
 //! variables
 TLorentzVector L1,L2,L3;
 TLorentzVector MET;
 TLorentzVector J1, J2;
 float pid1, pid2;
 float _SumEt ;
 TLorentzVector TkMET;
 
 bool _isOk;
 int  _jetOk;
 int  _lepOk;
 bool _isTkMET;
 //int _WgSt_channel; // (1; el, el, el) (2; el, el, mu) (3; el, mu, mu) (4; mu, mu, mu)

 
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
WW::WW() {
 _isOk = false;
 _jetOk = 0;
 _lepOk = 0;
 _isTkMET = false;
}

WW::WW(float pt1, float pt2, float phi1, float phi2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, 0, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, 0, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  _isOk =  true;
 }
 else {
  _isOk = false;
 }
 _jetOk = 0;
 _isTkMET = false; 
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi, float metsum, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2) {

 if (pt1>0 && pt2>0) {
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0., metphi, 0.);
  _SumEt = metsum;
  _isOk =  true;
 }
 else {
  _isOk = false;
 }
 if( jetpt1>0) {
  J1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, jetmass1); //---- NB: jets are treated as massive
  if( jetpt2>0) {
   J2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, jetmass2); //---- NB: jets are treated as massive
   _jetOk = 2;
  }
  else {
   _jetOk = 1;
  }
 }
 _isTkMET = false;
}


WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  _isOk =  true;
 }
 else {
  _isOk = false;
 }
 _jetOk = 0;
 _isTkMET = false;
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  pid1 = pidl1;
  pid2 = pidl2;
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  _isOk =  true;
 }
 else {
  _isOk = false;
 }
 _jetOk = 0;
 _isTkMET = false;
}

WW::WW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2) {
 
 if (pt1>0 && pt2>0) {  
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  pid1 = pidl1;
  pid2 = pidl2;
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  _isOk =  true;
 }
 else {
  _isOk = false;
 }
 if( jetpt1>0) {
  J1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, jetmass1); //---- NB: jets are treated as massive
  if( jetpt2>0) {
   J2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, jetmass2); //---- NB: jets are treated as massive
   _jetOk = 2;
  }
  else {
   _jetOk = 1;
  }
 }
 
 _isTkMET = false;
}

//! check if ok

//---- a function to check if "at least 2 leptons + met information" requirement is available
//---- and to check if at least two jets are available
void WW::checkIfOk() {
 
 //---- leptons
 if (_leptonspt.size() == _leptonseta.size()    &&   
     _leptonspt.size() == _leptonsphi.size()    &&   
     _leptonspt.size() == _leptonsflavour.size())
  {
   
   int numLep = 0;   
   for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
    if (_leptonspt.at(ilep) > 0.) numLep ++;
   }
   
   //---- if 2 leptons and met is set
   if (numLep >=2 && MET.E() > 0) {
    _isOk = true;
    _lepOk = numLep;
    
    if (TkMET.E() > 0) {
     _isTkMET = true;
    }
   }
  }
  
 //---- jets
 
 if (_jetspt.size() == _jetseta.size()    &&   
     _jetspt.size() == _jetsphi.size()    &&   
     _jetspt.size() == _jetsmass.size())
 {
  
  
  int numJet = 0;
  for (unsigned int ijet = 0; ijet < _jetspt.size(); ijet++) {
   if (_jetspt.at(ijet) > 0.) numJet ++;
  }
  
  //---- if 1 jets
  if (numJet >=1) {
   _jetOk = numJet;
  }
  
 }
 
}


//! set functions

void WW::setMET(float met, float metphi) {
 MET.SetPtEtaPhiM(met, 0, metphi, 0.);
}


void WW::setTkMET(float met, float metphi) {
 TkMET.SetPtEtaPhiM(met, 0, metphi, 0.);
 _isTkMET = true;
}


void WW::setSumET(float sumet) {
  _SumEt = sumet;  
}




void WW::setJets(std::vector<float> invectorpt ) {
 _jetspt = invectorpt;
 _jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta) {
 _jetspt  = invectorpt;
 _jetseta = invectoreta;
 _jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass) {
 _jetspt   = invectorpt;
 _jetseta  = invectoreta;
 _jetsphi  = invectorphi;
 _jetsmass = invectormass;

 //---- need to update J1 and J2
 if (( _jetspt.size() > 1 && _jetspt.at(0) > 0 && _jetspt.at(1) <= 0 ) || ( _jetspt.size() == 1 && _jetspt.at(0) > 0)) {
  J1.SetPtEtaPhiM(_jetspt.at(0), _jetseta.at(0), _jetsphi.at(0), _jetsmass.at(0)); //---- NB: jets are treated as massive
  _jetOk = 1;
 }
 else if ( _jetspt.size() > 1 && _jetspt.at(0) > 0 && _jetspt.at(1) > 0 ) {
  J1.SetPtEtaPhiM(_jetspt.at(0), _jetseta.at(0), _jetsphi.at(0), _jetsmass.at(0)); //---- NB: jets are treated as massive
  J2.SetPtEtaPhiM(_jetspt.at(1), _jetseta.at(1), _jetsphi.at(1), _jetsmass.at(1)); //---- NB: jets are treated as massive
  _jetOk = 2;
 }
 else { 
  _jetOk = 0;  //---- protection
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






//! functions

float WW::njet(){
 float njet = 0;
 for (unsigned int ijet=0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 30 && fabs(_jetseta.at(ijet))<4.7) {
   njet += 1;
  }
 }
 return njet; 
}


float WW::ptll(){
 if (_isOk) {
  return (L1+L2).Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::yll(){
 if (_isOk) {
  return (L1+L2).Rapidity();
 }
 else {
  return -9999.0;
 }
}


float WW::pTWW(){
 if (_isOk) {
  return (L1+L2+MET).Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::recoil(){ 
 if (_isOk) {
  return fabs((L1+L2+MET).Pt());
 }
 else {
  return -9999.0;
 }
}


float WW::dphill(){
 if (_isOk) {
  return fabs(L1.DeltaPhi(L2));
 }
 else {
  return -9999.0;
 } 
}


float WW::drll(){
 //---- https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00469
 if (_isOk) {
  return L1.DeltaR(L2);
 }
 else {
  return -9999.0;
 } 
}

float WW::dphilljet(){
 if (_isOk && _jetOk >= 1) { 
  return  fabs( (L1+L2).DeltaPhi(J1) );
 }
 else {
  return -9999.0;
 }
}



float WW::jetpt1_cut(){
 if (_isOk && _jetOk >= 1 && J1.Pt()>15.0) {
  return J1.Pt();
 }
 else {
  return -1.0;
 }
}

float WW::jetpt2_cut(){
 if (_isOk && _jetOk >= 2 && J2.Pt()>15.0) {
  return J2.Pt();
 }
 else {
  return -1.0;
 }
}

float WW::dphilljet_cut(){ 
 if (_isOk && _jetOk >= 1 && J1.Pt()>15.0 ) {
  return fabs( (L1+L2).DeltaPhi(J1) );
 }
 else {
  return -1.0;
 }
}

float WW::dphijet1met_cut(){
 if (_isOk && _jetOk >= 1 && J1.Pt()>15.0 ) {
  return fabs(J1.DeltaPhi(MET));
 }
 else {
  return -1.0;
 }
}

float WW::dphijet2met_cut(){
 if (_isOk && _jetOk >= 1 && J2.Pt()>15.0 ) {
  return fabs(J2.DeltaPhi(MET));
 }
 else {
  return -1.0;
 }
}

float WW::dphilljetjet(){ 
 if (_isOk && _jetOk >= 2) {
   return  fabs( (L1+L2).DeltaPhi(J1+J2) );
 }
 else {
  return -9999.0;
 }
}

float WW::dphilljetjet_cut(){
 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
   return  fabs( (L1+L2).DeltaPhi(J1+J2) );
 }
 else {
  return -1.0;
 }
}

float WW::ptTOT_cut(){
 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
   return  fabs( (L1+L2+J1+J2+MET).Pt() );
 }
 else {
  return -1.0;
 }
}

float WW::mTOT_cut(){
 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
   return  fabs( (L1+L2+J1+J2+MET).M() );
 }
 else {
  return -1.0;
 }
}

float WW::OLV1_cut(){
 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
   return  2 * abs(((L1.Eta()-((J1.Eta()+J2.Eta())/2))/(J1.Eta()-J2.Eta())));
 }
 else {
  return -1.0;
 }
}

float WW::OLV2_cut(){
 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
   return  2 * abs(((L2.Eta()-((J1.Eta()+J2.Eta())/2))/(J1.Eta()-J2.Eta())));
 }
 else {
  return -1.0;
 }
}

float WW::Ceta_cut(){

 if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
  return (OLV1_cut()+OLV2_cut());
 }
 else {
  return -1.0;
 }
}


float WW::dphilmet(){ 
 if (_isOk) {
  float d1 = fabs((L1).DeltaPhi(MET));
  float d2 = fabs((L2).DeltaPhi(MET));
  if (d1<d2) return d1;
  else       return d2;
 }
 else {
  return -9999.0;
 }
}

float WW::dphiltkmet(){ 
 if (_isOk && _isTkMET) {
  float d1 = fabs((L1).DeltaPhi(TkMET));
  float d2 = fabs((L2).DeltaPhi(TkMET));
  if (d1<d2) return d1;
  else       return d2;
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet1(){ 
 if ( L1.Pt() > 0 && MET.E() > 0 ) {
  return fabs((L1).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}


float WW::dphilmet2(){ 
 if (_isOk) {
  return fabs((L2).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}


float WW::mtw1(){ 
 if ( L1.Pt() > 0 && MET.E() > 0 ) {
  return sqrt(2 * pt1() * pfmet() * (1 - cos( dphilmet1() )));
 }
 else {
  return -9999.0;
 }
}


float WW::mtw2(){ 
 if (_isOk) {
  return sqrt(2 * pt2() * pfmet() * (1 - cos( dphilmet2() )));
 }
 else {
  return -9999.0;
 }
}



float WW::pfmet(){
 
 if ( MET.E() > 0 ) {
  return MET.Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::PfMetDivSumMet(){

 if (_isOk) {
  return MET.Pt()/sqrt(_SumEt);
 }
 else {
  return -9999.0;
 }
}


float WW::upara(){

 if (_isOk) {
  TLorentzVector utv = (-MET-(L1+L2));
  float ut = utv.P();
  float uphi = utv.DeltaPhi(L1+L2);
  return ut*cos(uphi);
 }
 else {
  return -9999.0;
 }
}

float WW::uperp(){

 if (_isOk) {
  TLorentzVector utv = (-MET-(L1+L2));
  float ut = utv.P();
  float uphi = utv.DeltaPhi(L1+L2);
  return ut*sin(uphi);
 }
 else {
  return -9999.0;
 }
}


float WW::projpfmet(){
 
  if (_isOk) {
    if (dphilmet() < TMath::Pi() / 2.)
      return sin(dphilmet()) * MET.Pt();
    else
      return MET.Pt();
  }
  else {
    return -9999.0;
  }
}


float WW::projtkmet(){
 
 if (_isOk && _isTkMET) {
  if (dphiltkmet() < TMath::Pi() / 2.)
   return sin(dphiltkmet()) * TkMET.Pt();
  else
   return TkMET.Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::mpmet(){
 
 if (_isOk && _isTkMET) {
  return min(projtkmet(),projpfmet());
 }
 else {
  return -9999.0;
 }
}

//---- pt
float WW::pt1(){
 
 if ( L1.Pt() > 0 ) {
  return L1.Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::pt2(){
 
 if (_isOk) {
  return L2.Pt();
 }
 else {
  return -9999.0;
 } 
}

//---- eta
float WW::eta1(){
 
 if ( L1.Pt() > 0 ) {
  return L1.Eta();
 }
 else {
  return -9999.0;
 }
}


float WW::eta2(){
 
 if (_isOk) {
  return L2.Eta();
 }
 else {
  return -9999.0;
 } 
}

//---- phi
float WW::phi1(){
 
 if ( L1.Pt() > 0 ) {
  return L1.Phi();
 }
 else {
  return -9999.0;
 }
}


float WW::phi2(){
 
 if (_isOk) {
  return L2.Phi();
 }
 else {
  return -9999.0;
 } 
}


//---- mll
float WW::mll(){
 
 if (_isOk) {
  return (L1+L2).M();
 }
 else {
  return -9999.0;
 }
 
}

float WW::dphillmet(){
 
 if (_isOk) {
  return  fabs( (L1+L2).DeltaPhi(MET) );
 }
 else {
  return -9999.0;
 }
 
}

float WW::mth(){
 
 if (_isOk) {
  return sqrt( 2. * ptll() * MET.Pt() * ( 1. - cos (dphillmet()) ));
//   AN 2011/155, v2, p19
//   sqrt( 2 * pTll() * met(metToUse) * ( 1 - cos(dPhillMet(metToUse)) ) );
 }
 else {
  return -9999.0;
 }
 
}


float WW::mcoll(){
 
 if (_isOk) {
  
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



float WW::mcollWW(){
 
 if (_isOk) {
  
  //---- project met to lepton direction
  float et_par_1 = MET.Pt() * cos ( fabs( (L1).DeltaPhi(MET) ) );
  float et_par_2 = MET.Pt() * cos ( fabs( (L2).DeltaPhi(MET) ) ); 
  
  TLorentzVector L1_enhanced,L2_enhanced;
  
  L1_enhanced.SetPtEtaPhiM(pt1() + et_par_1, eta1(), phi1(), 80.385);
  L2_enhanced.SetPtEtaPhiM(pt2() + et_par_2, eta2(), phi2(), 80.385);
  
  return (L1_enhanced + L2_enhanced).M();
  
  
 }
 else {
  return -9999.0;
 }
 
}


float WW::mTi(){

 if (_isOk) {
  return (L1+L2+MET).M();
 }
 else{
  return -9999.0;
 }

}


float WW::choiMass(){

 //TVector3 METvec, ptllvec, pt1vec, pt2vec;
 //METvec.SetXYZ(MET.X(),MET.Y(),MET.Z());
 //ptllvec.SetXYZ((L1+L2).X(),(L1+L2).Y(),(L1+L2).Z());
 //pt1vec.SetXYZ((L1).X(),(L1).Y(),0);
 //pt2vec.SetXYZ((L2).X(),(L2).Y(),0);
 if (_isOk) {
  return sqrt( 2*(pt1()*pt1()) + 2*(pt2()*pt2()) + 3*(pt1()*pt2() + (MET.Pt())*(pt1()+pt2()) - MET.Pt()*ptll()*cos(dphillmet()) - 2*pt1()*pt2()*cos(dphill())) );
 }
 else{
  return -9999.0;
 }
 
}


float WW::mR(){

 if (_isOk) {
  return sqrt( 0.5*( mll()*mll() - MET.Pt()*ptll()*cos(dphillmet()) + sqrt( ( mll()*mll() + ptll()*ptll() )*( mll()*mll() + MET.Pt()*MET.Pt()  )  )  )  );
 }
 else{
  return -9999.0;
 }

}


float WW::mTe(){

 if (_isOk) {
  TLorentzVector L1_enhanced,L2_enhanced;

  L1_enhanced.SetPtEtaPhiM(pt1(), eta1(), phi1(), 80.385);
  L2_enhanced.SetPtEtaPhiM(pt2(), eta2(), phi2(), 80.385);

  return (L1_enhanced + L2_enhanced+MET).M();
 }
 else {
  return -9999.0;
 }

}


float WW::channel(){
 
 if (_isOk) {
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
 
 if (_jetOk >= 2) {
  return (J1+J2).M();
 }
 else {
  return -9999.0;
 }
}


float WW::detajj(){
 
 if (_jetOk >= 2) {
  return abs(J1.Eta()-J2.Eta());
 }
 else {
  return -9999.0;
 } 
}


float WW::dphijj(){
 if (_isOk) {
  return fabs(J1.DeltaPhi(J2));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphijet1met(){
 if (_isOk && _jetOk >= 1) {
  return fabs(J1.DeltaPhi(MET));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphijet2met(){
 if (_isOk && _jetOk >= 2) {
  return fabs(J2.DeltaPhi(MET));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphijjmet(){
  if (_isOk && _jetOk >= 2) {
    return fabs((J1+J2).DeltaPhi(MET));
  }
  else {
    return -9999.0;
  } 
}

float WW::dphijjmet_cut(){
  if (_isOk && _jetOk >= 2 && J1.Pt()>15.0 && J2.Pt()>15.0) {
    return fabs((J1+J2).DeltaPhi(MET));
  }
  else {
    return -1.0;
  }
}

float WW::dphilep1jet1(){
 if (_isOk && _jetOk >= 1) {
  return fabs(L1.DeltaPhi(J1));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphilep2jet1(){
 if (_isOk && _jetOk >= 1) {
  return fabs(L2.DeltaPhi(J1));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphilep1jet2(){
 if (_isOk && _jetOk >= 2) {
  return fabs(L1.DeltaPhi(J2));
 }
 else {
  return -9999.0;
 } 
}


float WW::dphilep2jet2(){
 if (_isOk && _jetOk >= 2) {
  return fabs(L2.DeltaPhi(J2));
 }
 else {
  return -9999.0;
 } 
}


float WW::m2ljj20(){
 if (_isOk && _jetOk >= 1 && J1.Pt()>30) {
  if (J2.Pt()>20) 
    return (L1+L2+J1+J2).M();
  else
    return (L1+L2+J1).M();
 }
 else {
  return -9999.0;
 }
}


float WW::m2ljj30(){
 if (_isOk && _jetOk >= 1 && J1.Pt()>30) {
  if (J2.Pt()>30) 
    return (L1+L2+J1+J2).M();
  else
    return (L1+L2+J1).M();
 }
 else {
  return -9999.0;
 }
}


float WW::ht(){ 
 if (_isOk && _leptonspt.size() > 0) {
  float ht_value = 0;
  for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
   if (_leptonspt.at(ilep) > 0) {
    ht_value += _leptonspt.at(ilep);
   }
  }
  for (unsigned int ijet = 0; ijet < _jetspt.size(); ijet++) {
   if (_jetspt.at(ijet) > 30) {
    ht_value += _jetspt.at(ijet);
    }
  }
  ht_value += MET.Pt();
  return  ht_value;
 }
 else {
  return -9999.0;
 }
}



float WW::vht_pt(){ 
 if (_isOk && _leptonspt.size() > 0) {
   TLorentzVector vht_Vector;
   for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
    if (_leptonspt.at(ilep) > 10) {  //---- 10 GeV threshold for leptons
     TLorentzVector Ltemp;
     Ltemp.SetPtEtaPhiM(_leptonspt.at(ilep), _leptonseta.at(ilep), _leptonsphi.at(ilep), 0.);
     vht_Vector += Ltemp;
    }
   }
   for (unsigned int ijet = 0; ijet < _jetspt.size(); ijet++) {
    if (_jetspt.at(ijet) > 30) {
     TLorentzVector Jtemp;
     Jtemp.SetPtEtaPhiM(_jetspt.at(ijet), _jetseta.at(ijet), _jetsphi.at(ijet), 0.);
     vht_Vector += Jtemp;
    }
   }
   return vht_Vector.Pt();
 }
 else {
  return -9999.0;
 }
}


float WW::vht_phi(){ 
 if (_isOk && _leptonspt.size() > 0) {
  TLorentzVector vht_Vector;
  for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
   if (_leptonspt.at(ilep) > 0) {
    TLorentzVector Ltemp;
    Ltemp.SetPtEtaPhiM(_leptonspt.at(ilep), _leptonseta.at(ilep), _leptonsphi.at(ilep), 0.);
    vht_Vector += Ltemp;
   }
  }
  for (unsigned int ijet = 0; ijet < _jetspt.size(); ijet++) {
   if (_jetspt.at(ijet) > 30) {
    TLorentzVector Jtemp;
    Jtemp.SetPtEtaPhiM(_jetspt.at(ijet), _jetseta.at(ijet), _jetsphi.at(ijet), 0.);
    vht_Vector += Jtemp;
   }
  }
  return vht_Vector.Phi();
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

 if (_isOk) {

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
  double xPI = 3.14159266;

  const int nParametri = 2;
  TMinuit minuit(nParametri);
  minuit.SetFCN(functionMT2);

  minuit.SetPrintLevel(-1); // quiet

  met = MET.E();

  double par[nParametri]={met/2.,0.0};
  double stepSize[nParametri]={met/100.,0.001};
  double minVal[nParametri]={met/100.,0.0};
  double maxVal[nParametri]={30.*met,2.*xPI};
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

float WW::mllWgSt(){ // smallest mll out of three combination

 float mll_small = -9999.0;
 float mll12     = -9999.0;
 float mll13     = -9999.0;
 float mll23     = -9999.0;

 //_WgSt_channel = -9999;
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>8 GeV
  if (_leptonspt.size()>3  ) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   
   //---- same flavour and different charge
   if (fabs(flav1) == fabs(flav2) && flav1*flav2<0) {
    mll12 = (L1+L2).M();
   }
   if (fabs(flav1) == fabs(flav3) && flav1*flav3<0) {
    mll13 = (L1+L3).M();
   }
   if (fabs(flav2) == fabs(flav3) && flav2*flav3<0) {
    mll23 = (L2+L3).M();
   }
  
   // check flavor channel
   //
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*11*11 ) _WgSt_channel = 1; // el, el, el 
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*11*13 ) _WgSt_channel = 2; // el, el, mu
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*13*13 ) _WgSt_channel = 3; // el, mu, mu
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 13*13*13 ) _WgSt_channel = 4; // mu, mu, mu

   if(mll12 >= 0)if(mll13 <  0)if(mll23 <  0)                  mll_small = mll12;
   if(mll12 <  0)if(mll13 >= 0)if(mll23 <  0)                  mll_small = mll13;
   if(mll12 <  0)if(mll13 <  0)if(mll23 >= 0)                  mll_small = mll23;

   if(mll12 >= 0){if(mll13 >= 0){if(mll23 <  0){if(mll12 < mll13){mll_small = mll12;}else{mll_small = mll13;}}}}
   if(mll12 >= 0){if(mll13 <  0){if(mll23 >= 0){if(mll12 < mll23){mll_small = mll12;}else{mll_small = mll23;}}}}
   if(mll12 <  0){if(mll13 >= 0){if(mll23 >= 0){if(mll13 < mll23){mll_small = mll13;}else{mll_small = mll23;}}}}

   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll12 < mll13)if(mll12 < mll23){mll_small = mll12;}
   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll13 < mll12)if(mll13 < mll23){mll_small = mll13;}
   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll23 < mll12)if(mll23 < mll13){mll_small = mll23;}

   return mll_small;
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
  
}
float WW::drllWgSt(){ // smallest mll out of three combination

 float mll_small = -9999.0;
 float drll_small = -9999.0;

 float mll12     = -9999.0;
 float drll12     = -9999.0;

 float mll13     = -9999.0;
 float drll13     = -9999.0;

 float mll23     = -9999.0;
 float drll23     = -9999.0;

 //_WgSt_channel = -9999;
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>8 GeV
  if (_leptonspt.size()>3  ) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   
   //---- same flavour and different charge
   if (fabs(flav1) == fabs(flav2) && flav1*flav2<0) {
    mll12 = (L1+L2).M();
    drll12 = L1.DeltaR(L2);
   }
   if (fabs(flav1) == fabs(flav3) && flav1*flav3<0) {
    mll13 = (L1+L3).M();
    drll13 = L1.DeltaR(L3);
   }
   if (fabs(flav2) == fabs(flav3) && flav2*flav3<0) {
    mll23 = (L2+L3).M();
    drll23 = L2.DeltaR(L3);
   }
  
   // check flavor channel
   //
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*11*11 ) _WgSt_channel = 1; // el, el, el 
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*11*13 ) _WgSt_channel = 2; // el, el, mu
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 11*13*13 ) _WgSt_channel = 3; // el, mu, mu
   //if(fabs(flav1) * fabs(flav2) * fabs(flav3) == 13*13*13 ) _WgSt_channel = 4; // mu, mu, mu

   if(mll12 >= 0)if(mll13 <  0)if(mll23 <  0)                  drll_small = drll12;
   if(mll12 <  0)if(mll13 >= 0)if(mll23 <  0)                  drll_small = drll13;
   if(mll12 <  0)if(mll13 <  0)if(mll23 >= 0)                  drll_small = drll23;

   if(mll12 >= 0){if(mll13 >= 0){if(mll23 <  0){if(mll12 < mll13){drll_small = drll12;}else{drll_small = drll13;}}}}
   if(mll12 >= 0){if(mll13 <  0){if(mll23 >= 0){if(mll12 < mll23){drll_small = drll12;}else{drll_small = drll23;}}}}
   if(mll12 <  0){if(mll13 >= 0){if(mll23 >= 0){if(mll13 < mll23){drll_small = drll13;}else{drll_small = drll23;}}}}

   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll12 < mll13)if(mll12 < mll23){drll_small = drll12;}
   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll13 < mll12)if(mll13 < mll23){drll_small = drll13;}
   if(mll12 >= 0)if(mll13 >= 0)if(mll23 >= 0)if(mll23 < mll12)if(mll23 < mll13){drll_small = drll23;}

   return drll_small;
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
  
}


float WW::mllThird(){
 
 if (_isOk) {
  
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



float WW::mllOneThree(){
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   float newmll = - 9999.0;
   float mll13 = -9999.0;
   
   //---- same flavour and different charge
   mll13 = (L1+L3).M();
   return mll13;
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
 
}



float WW::mllTwoThree(){
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   float newmll = - 9999.0;
   float mll23 = -9999.0;
   
   //---- same flavour and different charge
   mll23 = (L2+L3).M();
   return mll23;
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
 
}





float WW::drllOneThree(){
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   return L1.DeltaR(L3);
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
 
}



float WW::drllTwoThree(){
 
 if (_isOk) {
  
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float flav1 = _leptonsflavour.at(0);
   float flav2 = _leptonsflavour.at(1);
   float flav3 = _leptonsflavour.at(2);
   
   return L2.DeltaR(L3);
  }   
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
  return -9999.0;
 }
 
}

//=== mass variable needed for WH same sign

float WW::mlljj20_whss(){
TLorentzVector tmpLV;
if (_isOk && _jetOk >= 1 && J1.Pt()>30) {
 float dphi1;
 float dphi2;
 float mass = 0.;
   if(J2.Pt() > 20.) {
   dphi1 = fabs(L1.DeltaPhi(J1+J2));
   dphi2 = fabs(L2.DeltaPhi(J1+J2));
     if(dphi1 <= dphi2) tmpLV = L1;
     else tmpLV = L2;
     mass =  ((tmpLV+tmpLV+J1+J2).M());
   }
   if(J2.Pt() < 20.) {
   dphi1 = fabs(L1.DeltaPhi(J1));
   dphi2 = fabs(L2.DeltaPhi(J1));
     if(dphi1 <= dphi2) tmpLV = L1;
     else tmpLV = L2;
     mass =  ((tmpLV+tmpLV+J1).M());
}
return mass;
}
else {
  return -9999.0;
}
}

float WW::mlljj30_whss(){
TLorentzVector tmpLV;
if (_isOk && _jetOk >= 2 && J1.Pt()>30 && J2.Pt() > 30.) {
 float dphi1;
 float dphi2;
 float mass = 0.;
 dphi1 = fabs(L1.DeltaPhi(J1+J2));
 dphi2 = fabs(L2.DeltaPhi(J1+J2));
 if(dphi1 <= dphi2) tmpLV = L1;
 else tmpLV = L2;
      mass =  ((tmpLV+tmpLV+J1+J2).M());
 return mass;
}
else {
  return -9999.0;
}
}
