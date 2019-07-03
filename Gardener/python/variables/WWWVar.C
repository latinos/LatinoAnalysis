
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

#include <TMinuit.h>
#include <vector>


class WWW {
public:
 //! constructor
 WWW();
 WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2);
 WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi);
 WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi);
 WWW(float pt1, float pt2, float phi1, float phi2, float met, float metphi);
 WWW(float pt1, float pt2, float pt3, float eta1, float eta2, float eta3, float phi1, float phi2, float phi3, float met, float metphi);
 WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2, float jetbtag1, float jetbtag2);

 virtual ~WWW() {}
 
 //! check
 void checkIfOk();
  
 //! set functions
 void setJets(std::vector<float> invector);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass);
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass, std::vector<float> invectorbtag);

// void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour, std::vector<float> invectorcharge); 
 void setNotZLepton();

 void setMET  (float met, float metphi);
 void setTkMET(float met, float metphi);
 
 //! functions
 float mllmin3l();
 float pt1();
 float pt2();
 float pt3();
 float eta1();
 float eta2();
 float eta3();
 float phi1();
 float phi2();
 float phi3();
 float drllmin3l();
 float zveto_3l(); 
 float pfmet();
 float channel();
 float njet_3l();
 float nbjet_3l();
 float chlll();
 float mlll();
 float flagOSSF();
 float mtwww();
 float mtw1_wh3l();
 float mtw2_wh3l();
 float mtw3_wh3l();
 float minmtw_wh3l();
 float mindphi_lmet();
 float dphilllmet();
 float ptlll();
 float pTWWW();
 float dphilmet1_wh3l();
 float dphilmet2_wh3l();
 float dphilmet3_wh3l();

 float pt12();
 float pt13();
 float pt23();
 float ptbest();
 
 float z4lveto();
 float dmjjmW();
 float mtw_notZ();
 float pdgid_notZ();
 float dphilmetjj();
 float dphilmetj();
 float mTlmetjj();
 float pTlmetjj();
 float pTlmetj();
 float ptz();
 float checkmZ();

private:
 //! variables
 TLorentzVector L1,L2,L3;
 TLorentzVector notZlep;	// for Zh
 float pid_notZ;	// for Zh
 TLorentzVector Zlep1, Zlep2;	// for Zh
 TLorentzVector MET;
 TLorentzVector J1, J2;
 float pid1, pid2;
 TLorentzVector TkMET;
 
 bool _isOk;
 int  _jetOk;
 int  _lepOk;
 bool _isTkMET;
 
 std::vector<float> _jetspt;
 std::vector<float> _jetseta;
 std::vector<float> _jetsphi;
 std::vector<float> _jetsmass;
 std::vector<float> _jetsbtag;

 std::vector<float> _leptonspt;
 std::vector<float> _leptonseta;
 std::vector<float> _leptonsphi;
 std::vector<float> _leptonsflavour;
 std::vector<float> _leptonscharge; 

};

//! constructor
WWW::WWW() {
 _isOk = false;
 _jetOk = 0;
 _lepOk = 0;
 _isTkMET = false;
}

WWW::WWW(float pt1, float pt2, float phi1, float phi2, float met, float metphi) {
 
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

WWW::WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float met, float metphi) {
 
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

WWW::WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi) {
 
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

WWW::WWW(float pt1, float pt2, float pt3, float eta1, float eta2, float eta3, float phi1, float phi2, float phi3, float met, float metphi) {

 if (pt1>0 && pt2>0 && pt3>0) {
  L1.SetPtEtaPhiM(pt1, eta1, phi1, 0.);
  L2.SetPtEtaPhiM(pt2, eta2, phi2, 0.);
  L3.SetPtEtaPhiM(pt3, eta3, phi3, 0.);
  MET.SetPtEtaPhiM(met, 0, metphi, 0.);
  _isOk =  true;
  setNotZLepton();
 }
 else {
  _isOk = false;
 }
 _jetOk = 0;
 _isTkMET = false;
}


WWW::WWW(float pt1, float pt2, float eta1, float eta2, float phi1, float phi2, float pidl1, float pidl2, float met, float metphi, float jetpt1, float jetpt2, float jeteta1, float jeteta2, float jetphi1, float jetphi2, float jetmass1, float jetmass2) {
 
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
void WWW::checkIfOk() {
 
 //---- leptons
 if (_leptonspt.size() == _leptonseta.size()    &&   
     _leptonspt.size() == _leptonsphi.size()    &&   
     _leptonspt.size() == _leptonsflavour.size() &&
     _leptonspt.size() == _leptonscharge.size())
          
  {
   
   int numLep = 0;   
   for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
    if (_leptonspt.at(ilep) > 0.) numLep ++;
   }
   
   //---- if 2 leptons and met is set
   if (numLep >=3 && MET.E() > 0) {
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
  
  //---- if 2 jets
  if (numJet >=2) {
   _jetOk = numJet;
  }
  
 }
 // cout << "At end of checkIfOk, _jetOk = " << _jetOk << endl;
 
}


//! set functions

void WWW::setMET(float met, float metphi) {
 MET.SetPtEtaPhiM(met, 0, metphi, 0.);
}

void WWW::setTkMET(float met, float metphi) {
 TkMET.SetPtEtaPhiM(met, 0, metphi, 0.);
 _isTkMET = true;
}



void WWW::setJets(std::vector<float> invectorpt ) {
 _jetspt = invectorpt;
 _jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WWW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta) {
 _jetspt  = invectorpt;
 _jetseta = invectoreta;
 _jetOk = 0;  //---- protection need to update J1 and J2, but eta, phi and mass are missing!
}

void WWW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass) {
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

 // cout << "At end of setJetsA, _jetOk = " << _jetOk << endl;
}

void WWW::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass, std::vector<float> invectorbtag) {
 _jetspt   = invectorpt;
 _jetseta  = invectoreta;
 _jetsphi  = invectorphi;
 _jetsmass = invectormass;
 _jetsbtag = invectorbtag;

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
 // cout << "At end of setJetsB, _jetOk = " << _jetOk << endl;
}


void WWW::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour, std::vector<float> invectorcharge) {
 _leptonspt      = invectorpt;
 _leptonseta     = invectoreta;
 _leptonsphi     = invectorphi;
 _leptonsflavour = invectorflavour;
 _leptonscharge = invectorcharge;
 
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

 setNotZLepton();
}

// Set not-Z-lepton (W candidate) for Zh 
void WWW::setNotZLepton() {

  float Zmass = 91.1876;

  float L1Charge = _leptonsflavour.at(0);
  float L2Charge = _leptonsflavour.at(1);
  float L3Charge = _leptonsflavour.at(2);
  float L1flavour = _leptonscharge.at(0);
  float L2flavour = _leptonscharge.at(1);
  float L3flavour = _leptonscharge.at(2);

  // cout << endl;
  // cout << "Charges " << L1Charge << " " << L2Charge << " " << L3Charge << endl;
  // cout << "Flavours " << L1flavour << " " << L2flavour << " " << L3flavour << endl;

  double dlep = 0.;
  double mindlep = 99999.;

  if((L1Charge * L2Charge < 0) && (fabs(L1flavour) == fabs(L2flavour))){
    mindlep = fabs((L1 + L2).M()-Zmass);
    // cout << "Z = L1+L2; m = " << (L1 + L2).M() << endl;
    notZlep = L3;
    Zlep1 = L1;
    Zlep2 = L2;
    pid_notZ = L3flavour;
    // cout << "chose L3" << endl;
  }

  if((L2Charge * L3Charge < 0) && (fabs(L2flavour) == fabs(L3flavour))){
    dlep = fabs((L2 + L3).M()-Zmass);
    // cout << "Z = L2+L3; m = " << (L2 + L3).M() << endl;
    if (dlep < mindlep) {
      mindlep = dlep;
      notZlep = L1;
      Zlep1 = L2;
      Zlep2 = L3;
      pid_notZ = L1flavour;
      // cout << "chose L1" << endl;
    }
  }

  if((L1Charge * L3Charge < 0) && (fabs(L1flavour) == fabs(L3flavour))){
    dlep = fabs((L1 + L3).M()-Zmass);
    // cout << "Z = L1+L3; m = " << (L1 + L3).M() << endl;
    if (dlep < mindlep) {
      mindlep = dlep;
      notZlep = L2;
      Zlep1 = L1;
      Zlep2 = L3;
      pid_notZ = L2flavour;
      // cout << "chose L2" << endl;
    }
  }

}

/*
void WWW::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorcharge) {
 _leptonspt      = invectorpt;
 _leptonseta     = invectoreta;
 _leptonsphi     = invectorphi;
 _leptonscharge = invectorcharge;
 
 if ( _leptonspt.size() > 0 && _leptonspt.at(0) > 0 ) {
  L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0); //---- NB: leptons are treated as massless
 }
 if ( _leptonspt.size() > 1 && _leptonspt.at(1) > 0 ) {
  L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0); //---- NB: leptons are treated as massless
 }
 if ( _leptonspt.size() > 2 && _leptonspt.at(2) > 0 ) {
  L3.SetPtEtaPhiM(_leptonspt.at(2), _leptonseta.at(2), _leptonsphi.at(2), 0); //---- NB: leptons are treated as massless
 }
 
 }invectorflavour
*/

//! functions

float WWW::flagOSSF() {
if (_isOk) {
float flag_OSSF = 0.;
 float L1Charge = _leptonsflavour.at(0);
 float L2Charge = _leptonsflavour.at(1);
 float L3Charge = _leptonsflavour.at(2);
 float L1flavour = _leptonscharge.at(0);
 float L2flavour = _leptonscharge.at(1);
 float L3flavour = _leptonscharge.at(2);

//1e2mu case
if(((fabs(L1flavour) ==11 && fabs(L2flavour) == 13 && fabs(L3flavour) == 13) && (L2flavour * L3flavour < 0)) || ((fabs(L1flavour) == 13 && fabs(L2flavour) == 11 && fabs(L3flavour) == 13) && (L1flavour * L3flavour < 0)) || ((fabs(L1flavour) == 13 && fabs(L2flavour) == 13 && fabs(L3flavour) == 11) && (L1flavour * L2flavour < 0))) {
flag_OSSF = 1.;
}
//2e1mu case
if(((fabs(L1flavour) ==11 && fabs(L2flavour) == 11 && fabs(L3flavour) == 13) && (L1flavour * L2flavour < 0)) || ((fabs(L1flavour) ==11 && fabs(L2flavour) == 13 && fabs(L3flavour) == 11) && (L1flavour * L3flavour < 0)) || ((fabs(L1flavour) ==13 && fabs(L2flavour) == 11 && fabs(L3flavour) == 11) && (L2flavour * L3flavour < 0))) {
flag_OSSF = 1.;
}
//3mu case
if(fabs(L1flavour) ==13 && fabs(L2flavour) == 13 && fabs(L3flavour) == 13 ) {
flag_OSSF = 1.;
}
//3e case
if(fabs(L1flavour) ==11 && fabs(L2flavour) == 11 && fabs(L3flavour) == 11) {
flag_OSSF = 1.;
}
return flag_OSSF;
}
else {
return -9999.;
}
}

float WWW::drllmin3l(){
 //---- https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00469
 if (_isOk) {
 float L1Charge = _leptonsflavour.at(0);
 float L2Charge = _leptonsflavour.at(1);
 float L3Charge = _leptonsflavour.at(2);
 float deltaRN1 = 0.;
 float deltaRN2 = 0.;
 float deltaRN3 = 0.;

if(L1Charge * L2Charge < 0){
deltaRN1 = L1.DeltaR(L2);
    }

if(L2Charge * L3Charge < 0){
deltaRN2 = L2.DeltaR(L3);
    }

if(L1Charge * L3Charge < 0){
deltaRN3 = L1.DeltaR(L3);
    }

  double dRN1 = fabs(deltaRN1);
  double dRN2 = fabs(deltaRN2);
  double dRN3 = fabs(deltaRN3);

  double delRN[3] = {dRN1,dRN2,dRN3};
  double delRN_sort[3];
  int index[3];
  TMath::Sort(3,delRN,index);
  for(int d=0; d<3; d++)
  {
  delRN_sort[d]=delRN[index[d]];
  }
  return delRN_sort[1];
 }
 else {
  return -9999.0;
 } 
}

//---- mll
float WWW::mllmin3l(){
 
 if (_isOk) {
 float L1Charge = _leptonsflavour.at(0);
 float L2Charge = _leptonsflavour.at(1);
 float L3Charge = _leptonsflavour.at(2);

double dlep1 = 0.;
double dlep2 = 0.;
double dlep3 = 0.;

if(L1Charge * L2Charge < 0){
dlep1 = (L1 + L2).M();
}

if(L2Charge * L3Charge < 0){
dlep2 = (L2 + L3).M();
}

if(L1Charge * L3Charge < 0){
dlep3 = (L1 + L3).M();
}

 double dlep[3] = {dlep1,dlep2,dlep3};
 double dlep_sort[3];
 int indax[3];
 TMath::Sort(3,dlep,indax);
 for(int a=0; a<3; a++)
  {
 dlep_sort[a]=dlep[indax[a]];
               }

return dlep_sort[1];

//  return (L1+L2).M();
 }
 else {
  return -9999.0;
 } 
}

float WWW::z4lveto(){

  float Zmass = 91.1876;

  if (_isOk) {

    return fabs(mlll() - Zmass);

  } else {
    return -9999.0;
  }
}

float WWW::dmjjmW() {

  float Wmass = 80.4;
  float mjj = 0.0;
  if (_jetOk >= 2) {
    mjj = (J1+J2).M();
    return mjj-Wmass;
  }

  return -9999.0;
}

float WWW::zveto_3l(){
float Zmass = 91.1876;

 if (_isOk) {

 float L1Charge = _leptonsflavour.at(0);
 float L2Charge = _leptonsflavour.at(1);
 float L3Charge = _leptonsflavour.at(2);
 float L1flavour = _leptonscharge.at(0);
 float L2flavour = _leptonscharge.at(1);
 float L3flavour = _leptonscharge.at(2);

double dlep1 = 0.;
double dlep2 = 0.;
double dlep3 = 0.;

if((L1Charge * L2Charge < 0) && (fabs(L1flavour) == fabs(L2flavour))){
dlep1 = (L1 + L2).M();
}

if((L2Charge * L3Charge < 0) && (fabs(L2flavour) == fabs(L3flavour))){
dlep2 = (L2 + L3).M();
}

if((L1Charge * L3Charge < 0) && (fabs(L1flavour) == fabs(L3flavour))){
dlep3 = (L1 + L3).M();
}

//cout << "L1Charge = " << L1Charge << "  L2Charge = " << L2Charge << "  L3Charge = " << L3Charge << endl;
//cout << "L1flavour = " << L1flavour << "  L2flavour = " << L2flavour << "  L3flavour = " << L3flavour << endl;
//co/ut << "dlep1 = " << dlep1 << "   dlep2 = " << dlep2 << "   dlep3 = " << dlep3 << endl;


float dilep_diff1 = fabs(dlep1-Zmass);
float dilep_diff2 = fabs(dlep2-Zmass);
float dilep_diff3 = fabs(dlep3-Zmass);

 double dlepdiff[3] = {dilep_diff1,dilep_diff2,dilep_diff3};
 double dlepdiff_sort[3];
 int indx[3];
 TMath::Sort(3,dlepdiff,indx);
 for(int a=0; a<3; a++)
  {
 dlepdiff_sort[a]=dlepdiff[indx[a]];
               }

//cout << "dlepdiff_sort[0] = " << dlepdiff_sort[0] << "dlepdiff_sort[1] = " << dlepdiff_sort[1] << "dlepdiff_sort[2] = " << dlepdiff_sort[2] << endl;

 return dlepdiff_sort[2];
 }
 else {
  return -9999.0;
 }
}

float WWW::mtw_notZ(){

  if (_isOk) {
    return sqrt(2 * notZlep.Pt() * pfmet() * (1 - cos(fabs((notZlep).DeltaPhi(MET)))));
  } else {
    return -9999.0;
  }
}

float WWW::pdgid_notZ(){

  if (_isOk) {
    return pid_notZ;
  } else {
    return -9999.0;
  }
}


float WWW::chlll(){
 if (_isOk) {
  //---- check L3
  //----      pt3>2 GeV
  if (_leptonspt.size()>2 && _leptonspt.at(2) > 2) {
   float L1Charge = _leptonsflavour.at(0);
   float L2Charge = _leptonsflavour.at(1);
   float L3Charge = _leptonsflavour.at(2);

  return L1Charge+L2Charge+L3Charge;
  }
  else { //---- if third lepton is not good
   return -9999.0;
  }
 }
 else { //---- if I don't even have 2 leptons
 return -9999.0;
 }
}

float WWW::njet_3l(){
 float njet = 0;
 for (unsigned int ijet=0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 40 && fabs(_jetseta.at(ijet))<4.7) {
   njet += 1;
  }
 }
 return njet; 
}

float WWW::nbjet_3l(){
 float nbjet = 0;
 float btag = -9999.;
 for (unsigned int ijet=0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 20 && _jetspt.at(ijet) < 40 && fabs(_jetseta.at(ijet))<4.7) {
//    cout << "number of taggable jets = " << ijet << endl;
    btag = _jetsbtag.at(ijet);
  if(btag > -0.715) {
//   cout << "BTagged Jet" << endl;
   nbjet += 1;
}
  }
 }
//cout << "Number of btagged jets = " << nbjet << endl;
 return nbjet;
}

float WWW::pfmet(){
 
 if (_isOk) {
  return MET.Pt();
 }
 else {
  return -9999.0;
 }
}

//---- pt
float WWW::pt1(){
 
 if (_isOk) {
  return L1.Pt();
 }
 else {
  return -9999.0;
 }
}


float WWW::pt2(){
 
 if (_isOk) {
  return L2.Pt();
 }
 else {
  return -9999.0;
 } 
}

float WWW::pt3(){

 if (_isOk) {
  return L3.Pt();
 }
 else {
  return -9999.0;
 }
}

//---- eta
float WWW::eta1(){
 
 if (_isOk) {
  return L1.Eta();
 }
 else {
  return -9999.0;
 }
}


float WWW::eta2(){
 
 if (_isOk) {
  return L2.Eta();
 }
 else {
  return -9999.0;
 } 
}

float WWW::eta3(){

 if (_isOk) {
  return L3.Eta();
 }
 else {
  return -9999.0;
 }
}


//---- phi
float WWW::phi1(){
 
 if (_isOk) {
  return L1.Phi();
 }
 else {
  return -9999.0;
 }
}


float WWW::phi2(){
 
 if (_isOk) {
  return L2.Phi();
 }
 else {
  return -9999.0;
 } 
}

float WWW::phi3(){

 if (_isOk) {
  return L3.Phi();
 }
 else {
  return -9999.0;
 }
}

float WWW::mlll(){
 if (_isOk) {
  return (L1+L2+L3).M();
 }
 else {
  return -9999.0;
 }
}

float WWW::dphilllmet(){

 if (_isOk) {
  return  fabs( (L1+L2+L3).DeltaPhi(MET) );
 }
 else {
  return -9999.0;
 }
}

float WWW::mTlmetjj(){

 if (_isOk && _jetOk >= 2) {
   TLorentzVector WWvec = MET + notZlep + J1 + J2;
   return  sqrt( pow(MET.Pt() + notZlep.Pt() + J1.Pt() + J2.Pt(),2) - pow(WWvec.Px(),2) - pow(WWvec.Py(),2));
 }
 else {
  return -9999.0;
 }
}

float WWW::pTlmetjj(){

 if (_isOk && _jetOk >= 2 && J2.Pt() > 30) {
   TLorentzVector WWvec = MET + notZlep + J1 + J2;
   return  WWvec.Pt();
 }
 else {
  return -9999.0;
 }
}

float WWW::pTlmetj(){

 if (_isOk && _jetOk >= 1 && J1.Pt() > 30) {
   TLorentzVector WWvec = MET + notZlep + J1 + J2;
   return  WWvec.Pt();
 }
 else {
  return -9999.0;
 }
}

float WWW::ptz() {

  if (_isOk) {
    return ((Zlep1 + Zlep2).Pt());
  } else {
    return -9999.0;
  }

}

float WWW::checkmZ() {
  if (_isOk) {
    return ((Zlep1 + Zlep2).M());
  } else {
    return -9999.0;
  }

}

float WWW::dphilmetjj(){

 if (_isOk && _jetOk >= 2 && J2.Pt() > 30) {
  return  fabs( (notZlep+MET).DeltaPhi(J1+J2) );
 }
 else {
  return -9999.0;
 }
}

float WWW::dphilmetj(){

  // cout << "In dphilmetj, _isOk = " << _isOk << " and _jetOk = " << _jetOk << endl;
 if (_isOk && _jetOk >= 1 && J1.Pt() > 30) {
  return  fabs( (notZlep+MET).DeltaPhi(J1) );
 }
 else {
  return -9999.0;
 }
}

float WWW::ptlll(){
 if (_isOk) {
  return (L1+L2+L3).Pt();
 }
 else {
  return -9999.0;
 }
}

float WWW::mtwww(){

 if (_isOk) {
  return sqrt( 2. * ptlll() * MET.Pt() * ( 1. - cos (dphilllmet()) ));
    }
     else {
       return -9999.0;
     }
   }

float WWW::pTWWW(){
 if (_isOk) {
  return (L1+L2+L3+MET).Pt();
 }
 else {
  return -9999.0;
 }
}

float WWW::mtw1_wh3l(){
 if ( L1.Pt() > 0 && MET.E() > 0 ) {
  return sqrt(2 * pt1() * pfmet() * (1 - cos(fabs((L1).DeltaPhi(MET)))));
 }
 else {
  return -9999.0;
 }
}

float WWW::mtw2_wh3l(){
 if ( L2.Pt() > 0 && MET.E() > 0 ) {
  return sqrt(2 * pt2() * pfmet() * (1 - cos(fabs((L2).DeltaPhi(MET)))));
 }
 else {
  return -9999.0;
 }
}

float WWW::mtw3_wh3l(){
 if ( L3.Pt() > 0 && MET.E() > 0 ) {
  return sqrt(2 * pt3() * pfmet() * (1 - cos(fabs((L3).DeltaPhi(MET)))));
 }
 else {
  return -9999.0;
 }
}

float WWW::minmtw_wh3l(){
 if ( L1.Pt() > 0 && L2.Pt() > 0 && L3.Pt() > 0 && MET.E() > 0 ) {
float mt1 = mtw1_wh3l();
float mt2 = mtw2_wh3l();
float mt3 = mtw3_wh3l();
float mtmin = 0.;

if(mt1 < mt2) mtmin = mt1;
else mtmin = mt2;
if(mtmin > mt3) mtmin = mt3;

  return mtmin;
 }
 else {
  return -9999.0;
 }
}

float WWW::mindphi_lmet(){
 if ( L1.Pt() > 0 && L2.Pt() > 0 && L3.Pt() > 0 && MET.E() > 0 ) {

float dphilmet1 = fabs(L1.DeltaPhi(MET));
float dphilmet2 = fabs(L2.DeltaPhi(MET));
float dphilmet3 = fabs(L3.DeltaPhi(MET));
float mindphilmet;

if(dphilmet1 < dphilmet2) mindphilmet = dphilmet1;
else mindphilmet = dphilmet2;
if(mindphilmet > dphilmet3) mindphilmet = dphilmet3;

  return mindphilmet;
 }
 else {
  return -9999.0;
 }
}

float WWW::dphilmet1_wh3l(){ 
 if ( L1.Pt() > 0 && MET.E() > 0 ) {
  return fabs((L1).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}

float WWW::dphilmet2_wh3l(){
 if ( L2.Pt() > 0 && MET.E() > 0 ) {
  return fabs((L2).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}

float WWW::dphilmet3_wh3l(){
 if ( L3.Pt() > 0 && MET.E() > 0 ) {
  return fabs((L3).DeltaPhi(MET));
 }
 else {
  return -9999.0;
 }
}



//---- pt di-lepton combinations

float WWW::pt12(){
  if (_isOk) {
    return (L1+L2).Pt();
  }
  else {
    return -9999.0;
  }
}



float WWW::pt13(){
  if (_isOk) {
    return (L1+L3).Pt();
  }
  else {
    return -9999.0;
  }
}


float WWW::pt23(){
  if (_isOk) {
    return (L2+L3).Pt();
  }
  else {
    return -9999.0;
  }
}





float WWW::ptbest(){
  if (_isOk) {
    
    float ch1 = _leptonsflavour.at(0);
    float ch2 = _leptonsflavour.at(1);
    float ch3 = _leptonsflavour.at(2);
      
    //     1 2 3  pt ordered
    //##   + + -       --> (2,3)  or   (1,3)
    //##   + - -       --> (1,2)  or   (1,3)
    //##   + - +       --> (1,2)  or   (2,3)
    
    //##   - + -       --> (1,2)  or   (2,3)
    //##   - - +       --> (1,3)  or   (2,3)
    //##   - + +       --> (1,2)  or   (1,3)
    
    
    //
    // if possible, pick the lowest pt as one of the leptons from H>WW>lvlv, due to off-shell-ness
    //
    //##   + + -       --> (2,3)  or   (1,3)
    //##   + - -       -->             (1,3)
    //##   + - +       -->             (2,3)
    
    //##   - + -       -->             (2,3)
    //##   - - +       --> (1,3)  or   (2,3)
    //##   - + +       -->             (1,3)
    
    
    //
    // in case you have 2 configurations, pick the highest pt pair
    //
    
    //##   + + -       --> (2,3)  or   (1,3)   A
    //##   + - -       -->             (1,3)   C
    //##   + - +       -->             (2,3)   B
    
    //##   - + -       -->             (2,3)   B
    //##   - - +       --> (1,3)  or   (2,3)   A
    //##   - + +       -->             (1,3)   C
    
    
    if (ch1 * ch2 > 0) {   // ---> A
      
      float pt23 = (L2+L3).Pt();
      float pt13 = (L1+L3).Pt();
      
      if (pt13 > pt23) return pt13;
      else return pt23;
      
    }
    else {
      // ---> B
      if (ch1 * ch3 > 0)     
        return (L2+L3).Pt();
      else 
        // ---> C
        return (L1+L3).Pt();
    }
    
    
  }
  else {
    return -9999.0;
  }
}






