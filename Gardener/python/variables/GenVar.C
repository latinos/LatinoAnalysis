
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
 void setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass);
 void setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setNeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour);
 void setMET  (float met, float metphi);
 
 //! functions
//  float pTGenVar();
//  float dphill();
//  float mll();
 
private:
 //! variables

 int  _jetOk;
 int  _lepOk;
 int  _neuOk;
 bool _metOk;
 
 std::vector<float> _jetspt;
 std::vector<float> _jetseta;
 std::vector<float> _jetsphi;
 std::vector<float> _jetsmass;
 
 std::vector<float> _leptonspt;
 std::vector<float> _leptonseta;
 std::vector<float> _leptonsphi;
 std::vector<float> _leptonsflavour;

 std::vector<float> _neutrinospt;
 std::vector<float> _neutrinoseta;
 std::vector<float> _neutrinosphi;
 std::vector<float> _neutrinosflavour;

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
}

void GenVar::setJets(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectormass) {
 _jetspt   = invectorpt;
 _jetseta  = invectoreta;
 _jetsphi  = invectorphi;
 _jetsmass = invectormass;
 
 _jetOk = 0;
 for (int ijet = 0; ijet < _jetspt.size(); ijet++) {
  if (_jetspt.at(ijet) > 0) _jetOk++;
 }
}

void GenVar::setLeptons(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 _leptonspt      = invectorpt;
 _leptonseta     = invectoreta;
 _leptonsphi     = invectorphi;
 _leptonsflavour = invectorflavour;
 
 _lepOk = 0;
 for (int ilep = 0; ilep < _leptonspt.size(); ilep++) {
  if (_leptonspt.at(ilep) > 0) _lepOk++;
 }
}



void GenVar::setNeutrinos(std::vector<float> invectorpt, std::vector<float> invectoreta, std::vector<float> invectorphi, std::vector<float> invectorflavour) {
 _neutrinospt      = invectorpt;
 _neutrinoseta     = invectoreta;
 _neutrinosphi     = invectorphi;
 _neutrinosflavour = invectorflavour;
 
 _neuOk = 0;
 for (int ineu = 0; ineu < _neutrinospt.size(); ineu++) {
  if (_neutrinospt.at(ineu) > 0) _lepOk++;
 }
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
// float GenVar::ptll(){
//  if (_isOk) {
//   return (L1+L2).Pt();
//  }
//  else {
//   return -9999.0;
//  }
// }
// 
// 
// float GenVar::yll(){
//  if (_isOk) {
//   return (L1+L2).Rapidity();
//  }
//  else {
//   return -9999.0;
//  }
// }





