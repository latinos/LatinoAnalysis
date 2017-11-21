
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

#include <TMinuit.h>
#include <vector>


class GenVar {
public:
 //! constructor
 GenVar();
 virtual ~GenVar() {}
 
 //! check
 void checkIfOk();
 
 //! set functions
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setLeptons(std::vector<float> invectorpt,std::vector<float> invectoreta, std::vector<float> invectorphi,
                 std::vector<float> invectorflavour,
                 std::vector<float> Status,
                 std::vector<float> IsPrompt,
                 std::vector<float> MotherPID,
                 std::vector<float> MotherStatus);
 void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setNeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setMET  (float met, float metphi);
 
 void setLHELeptons  (std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setLHENeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 
 //! functions
//  float pTGenVar();
//  float dphill();
//  float mll();
 float gen_ptllmet();
 float gen_ptll();
 float gen_mll();
 float gen_llchannel();
 float gen_mlvlv();
 
 float lhe_mlvlv();
 float lhe_mWp();
 float lhe_mWm();
 
private:
 //! variables

 int  _jetOk;
 int  _lepOk;
 int  _neuOk;
 bool _metOk;
 
 std::vector<float> _jetspt;
 std::vector<float> _jetseta;
 std::vector<float> _jetsphi;
 std::vector<float> _jetsflavour;
 
 std::vector<float> _leptonspt;
 std::vector<float> _leptonseta;
 std::vector<float> _leptonsphi;
 std::vector<float> _leptonsflavour;
 std::vector<float> _leptonsStatus;
 std::vector<float> _leptonsMotherPID;
 std::vector<float> _leptonsMotherStatus;

 std::vector<float> _neutrinospt;
 std::vector<float> _neutrinoseta;
 std::vector<float> _neutrinosphi;
 std::vector<float> _neutrinosflavour;

 std::vector<float> _lhe_leptonspt;
 std::vector<float> _lhe_leptonseta;
 std::vector<float> _lhe_leptonsphi;
 std::vector<float> _lhe_leptonsflavour;

 std::vector<float> _lhe_neutrinospt;
 std::vector<float> _lhe_neutrinoseta;
 std::vector<float> _lhe_neutrinosphi;
 std::vector<float> _lhe_neutrinosflavour;

 
 float _met;
 float _met_phi;
 
};

//! constructor
GenVar::GenVar() {
 _jetOk = 0;
 _lepOk = 0;
 _neuOk = 0;
 _metOk = false;
}



//! set functions

void GenVar::setMET(float met, float metphi) {
 _met = met;
 _met_phi = metphi;
 _metOk = true;
}

void GenVar::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 _jetspt      = invectorpt;
 _jetseta     = invectoreta;
 _jetsphi     = invectorphi;
 _jetsflavour = invectorflavour;
 
 _jetOk = 0;
 for (unsigned int ijet = 0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 0) _jetOk++;
 }
}

void GenVar::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi,
                        std::vector<float> invectorflavour,
                        std::vector<float> Status,
                        std::vector<float> IsPrompt,
                        std::vector<float> MotherPID,
                        std::vector<float> MotherStatus
) {
 
 _leptonspt             = invectorpt;
 _leptonseta            = invectoreta;
 _leptonsphi            = invectorphi;
 _leptonsflavour        = invectorflavour;
 _leptonsStatus         = Status;
 _leptonsMotherPID      = MotherPID;
 _leptonsMotherStatus   = MotherStatus;
 
 _lepOk = 0;
 for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
  if (_leptonspt.at(ilep) > 0) _lepOk++;
 }
}


void GenVar::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 
 _leptonspt             = invectorpt;
 _leptonseta            = invectoreta;
 _leptonsphi            = invectorphi;
 _leptonsflavour        = invectorflavour;

 _lepOk = 0;
 for (unsigned int ilep = 0; ilep < _leptonspt.size(); ilep++) {
  if (_leptonspt.at(ilep) > 0) _lepOk++;
 }
}



void GenVar::setNeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 _neutrinospt      = invectorpt;
 _neutrinoseta     = invectoreta;
 _neutrinosphi     = invectorphi;
 _neutrinosflavour = invectorflavour;
 
 _neuOk = 0;
 for (unsigned int ineu = 0; ineu < _neutrinospt.size(); ineu++) {
  if (_neutrinospt.at(ineu) > 0) _lepOk++;
 }
}





void GenVar::setLHELeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
  
  _lhe_leptonspt             = invectorpt;
  _lhe_leptonseta            = invectoreta;
  _lhe_leptonsphi            = invectorphi;
  _lhe_leptonsflavour        = invectorflavour;
  
}



void GenVar::setLHENeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {

  _lhe_neutrinospt       = invectorpt;
  _lhe_neutrinoseta      = invectoreta;
  _lhe_neutrinosphi      = invectorphi;
  _lhe_neutrinosflavour  = invectorflavour;
  
}



//! functions

// float GenVar::njet(){
//  float njet = 0;
//  for (unsigned int ijet=0; ijet < _jetspt.size(); ijet++) {
//   if (_jetspt.at(ijet) > 30 && fabs(_jetseta.at(ijet))<4.7) {
//    njet += 1;
//   }
//  }
//  return njet; 
// }
// 
// 

float GenVar::gen_ptllmet(){
  if (_lepOk >=2 && _metOk ) {
    TLorentzVector L1,L2;
    L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0.);
    L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0.);
    
    TLorentzVector MET;
    MET.SetPtEtaPhiM(_met , 0, _met, 0.);
    return (L1+L2+MET).Pt();
  }
  else {
    return -9999.0;
  }
}


float GenVar::gen_mlvlv(){
  if (_lepOk >=2 && _metOk ) {
    TLorentzVector L1,L2;
    L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0.);
    L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0.);
    
    TLorentzVector MET;
    MET.SetPtEtaPhiM(_met , 0, _met, 0.);
    return (L1+L2+MET).M();
  }
  else {
    return -9999.0;
  }
}


float GenVar::gen_ptll(){
 if (_lepOk >=2 ) {
  TLorentzVector L1,L2;
  L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0.);
  L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0.);
  return (L1+L2).Pt();
 }
 else {
  return -9999.0;
 }
}

float GenVar::gen_mll(){
 if (_lepOk >=2 ) {
  TLorentzVector L1,L2;
  L1.SetPtEtaPhiM(_leptonspt.at(0), _leptonseta.at(0), _leptonsphi.at(0), 0.);
  L2.SetPtEtaPhiM(_leptonspt.at(1), _leptonseta.at(1), _leptonsphi.at(1), 0.);
  return (L1+L2).M();
 }
 else {
  return -9999.0;
 }
}



float GenVar::gen_llchannel(){
 if (_lepOk >=2 ) {
  return _leptonsflavour.at(0) * _leptonsflavour.at(1);
 }
 else {
  return -9999.0;
 }
}




float GenVar::lhe_mlvlv(){
  if (_lhe_leptonspt.size() > 0 ) {
    TLorentzVector L1,L2;
    L1.SetPtEtaPhiM(_lhe_leptonspt.at(0), _lhe_leptonseta.at(0), _lhe_leptonsphi.at(0), 0.);
    L2.SetPtEtaPhiM(_lhe_leptonspt.at(1), _lhe_leptonseta.at(1), _lhe_leptonsphi.at(1), 0.);
    
    TLorentzVector V1,V2;
    V1.SetPtEtaPhiM(_lhe_neutrinospt.at(0), _lhe_neutrinoseta.at(0), _lhe_neutrinosphi.at(0), 0.);
    V2.SetPtEtaPhiM(_lhe_neutrinospt.at(1), _lhe_neutrinoseta.at(1), _lhe_neutrinosphi.at(1), 0.);

    return (L1+L2+V1+V2).M();
  }
  else {
    return -9999.0;
  }
  
}

float GenVar::lhe_mWp(){
  if ( (_lhe_leptonspt.size()>1) && (_lhe_neutrinospt.size()>1) ) {
    TLorentzVector L1,L2;
    L1.SetPtEtaPhiM(_lhe_leptonspt.at(0), _lhe_leptonseta.at(0), _lhe_leptonsphi.at(0), 0.);
    L2.SetPtEtaPhiM(_lhe_leptonspt.at(1), _lhe_leptonseta.at(1), _lhe_leptonsphi.at(1), 0.);

    TLorentzVector V1,V2;
    V1.SetPtEtaPhiM(_lhe_neutrinospt.at(0), _lhe_neutrinoseta.at(0), _lhe_neutrinosphi.at(0), 0.);
    V2.SetPtEtaPhiM(_lhe_neutrinospt.at(1), _lhe_neutrinoseta.at(1), _lhe_neutrinosphi.at(1), 0.);

    if ( _lhe_leptonsflavour.at(0) < 0 ) {  // L1 = e+(-11) OR mu+(-13) OR tau+(-15)
      if ( _lhe_neutrinosflavour.at(0) > 0 ) { // V1 = nue(12) OR numu(14) OR nutau(16)
        return (L1+V1).M();
      }
      else {
        return (L1+V2).M();
      }
    }
    else {  //  L1 = e-(11) OR mu-(13) OR tau-(15)
      if ( _lhe_neutrinosflavour.at(0) > 0 ) { // V1 = nue(12) OR numu(14) OR nutau(16) 
        return (L2+V1).M();
      }
      else {
        return (L2+V2).M();
      }
    }
  }
  else {
    return -9999.0;
  }
}

float GenVar::lhe_mWm(){
  if ( (_lhe_leptonspt.size()>1) && (_lhe_neutrinospt.size()>1) ) {
    TLorentzVector L1,L2;
    L1.SetPtEtaPhiM(_lhe_leptonspt.at(0), _lhe_leptonseta.at(0), _lhe_leptonsphi.at(0), 0.);
    L2.SetPtEtaPhiM(_lhe_leptonspt.at(1), _lhe_leptonseta.at(1), _lhe_leptonsphi.at(1), 0.);

    TLorentzVector V1,V2;
    V1.SetPtEtaPhiM(_lhe_neutrinospt.at(0), _lhe_neutrinoseta.at(0), _lhe_neutrinosphi.at(0), 0.);
    V2.SetPtEtaPhiM(_lhe_neutrinospt.at(1), _lhe_neutrinoseta.at(1), _lhe_neutrinosphi.at(1), 0.);

    if ( _lhe_leptonsflavour.at(0) < 0 ) {  // L1 = e+(-11) OR mu+(-13) OR tau+(-15)
      if ( _lhe_neutrinosflavour.at(0) > 0 ) { // V1 = nue(12) OR numu(14) OR nutau(16)
        return (L2+V2).M();
      }
      else {
        return (L2+V1).M();
      }
    }
    else {  //  L1 = e-(11) OR mu-(13) OR tau-(15)
      if ( _lhe_neutrinosflavour.at(0) > 0 ) { // V1 = nue(12) OR numu(14) OR nutau(16) 
        return (L1+V2).M();
      }
      else {
        return (L1+V1).M();
      }
    }
  }
  else {
    return -9999.0;
  }
}

// 
// float GenVar::yll(){
//  if (_isOk) {
//   return (L1+L2).Rapidity();
//  }
//  else {
//   return -9999.0;
//  }
// }





