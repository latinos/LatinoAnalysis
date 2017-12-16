#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include "TMath.h"
#include "TLorentzVector.h"
#include "TLorentzRotation.h"
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TString.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include <ZZMatrixElement/MELA/interface/Mela.h>
#include <MelaAnalytics/CandidateLOCaster/interface/MELACandidateRecaster.h>

class MelaReweighterWW{
  public:
  MelaReweighterWW(double com, double mpole, double width);
  ~MelaReweighterWW();
  
  void setMelaHiggsMassWidth(double mpole, double wpole);

  void resetMCFM_EWKParameters(double Gf=1.16639E-05, double alphaEW=1./128., double mW=80.399, double mZ=91.1876, double sin2thetaW=0.23119);

  float weightStoSBI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                    const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                    const std::vector<TLorentzVector>& associated);
  
  float weightStoI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                      const std::vector<TLorentzVector>& associated);

  float weightStoI_H(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                      const std::vector<TLorentzVector>& associated);

  float weightStoI_B(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                      const std::vector<TLorentzVector>& associated);

  float weightStoI_HB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                      const std::vector<TLorentzVector>& associated);
  
  float weightStoB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                       const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                       const std::vector<TLorentzVector>& associated);

  float weightStoH(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                       const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                       const std::vector<TLorentzVector>& associated);

  private:
  void setupDaughters(bool isVBF,
                      const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                      const std::vector<TLorentzVector>& associated);

                      

  void recast();

  double _com;
  double _mpole;
  double _width;
  MELACandidate* _candModified;

  Mela* _mela;
  MELACandidateRecaster * _recaster;
  SimpleParticleCollection_t* _daughters;
  SimpleParticleCollection_t* _associated;

};

MelaReweighterWW::MelaReweighterWW(double com, double mpole, double width):
_com(com),
_mpole(mpole),
_width(width),
_daughters(new SimpleParticleCollection_t()),
_associated(new SimpleParticleCollection_t())
{
  //TVar::VerbosityLevel verbosity = TVar::DEBUG;
  TVar::VerbosityLevel verbosity = TVar::ERROR;
  _mela =  new Mela(com, mpole, verbosity);
  // Should be called per-ME -- U. Sarica
  //_mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //_mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  _mela->setCandidateDecayMode(TVar::CandidateDecay_WW);
  _mela->selfDHzzcoupl[0/1][0][0]=1; // You need this.
  _mela->selfDHwwcoupl[0/1][0][0]=1; // You need this as well.
  _mela->selfDHggcoupl[0/1][0][0]=1;
  //Gf=1.16639E-05, alphaEW=1./128., mW=80.399, mZ=91.1876, sin2thetaW=0.23119
  //resetMCFM_EWKParameters(); // No need to call for default arguments; they are already set -- U. Sarica
  TVar::Production candScheme=TVar::JJVBF;
  _recaster =  new MELACandidateRecaster(candScheme);
  _candModified = 0;
}

MelaReweighterWW::~MelaReweighterWW(){
  delete _daughters;
  delete _mela;
  delete _associated;
}

void MelaReweighterWW::setMelaHiggsMassWidth(double mpole, double wpole){
  //_mela->setMelaHiggsMassWidth(mpole, wpole, 0);
  _mpole = mpole;
  _width = wpole;
}

void MelaReweighterWW::resetMCFM_EWKParameters(double Gf, double alphaEW, double mW, double mZ, double sin2thetaW){
  _mela->resetMCFM_EWKParameters(Gf, alphaEW, mW, mZ, sin2thetaW);
}

void MelaReweighterWW::recast(){
  if (_candModified)
    delete _candModified;
  MELACandidate* melaCand = _mela->getCurrentCandidate();
  _recaster->copyCandidate(melaCand, _candModified);
  _recaster->reduceJJtoQuarks(_candModified);
  _mela->setCurrentCandidate(_candModified);
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoSBI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){    
  
  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);

  float meS;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!isVBF)
    _mela->computeP(meS, false);
  else
    _mela->computeProdDecP(meS, false);
  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdDecP(meSBI, false);
  
  _mela->resetInputEvent();  
  return meSBI/meS;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);
 
  float meSpow;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSpow, false);
  else
    _mela->computeProdDecP(meSpow, false);
    
  //float meS;
  //_mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  // Added here -- U. Sarica
  //_mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //_mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  //_mela->computeP(meS, false);

  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdDecP(meSBI, false);

  float meHBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 0);
  //
  if (!isVBF)
    _mela->computeP(meHBI, false);
  else
    _mela->computeProdDecP(meHBI, false);
   

  //float meB;
  //_mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  //if (!isVBF)
  //  _mela->computeP(meB, false);
  //else
  //  _mela->computeProdDecP(meB, false);

  //_mela->resetInputEvent();

  //std::cout << "###  meSpow = " << meSpow << " meHBI = " << meHBI << " meSBI = " << meSBI << std::endl;
  //std::cout << "### weight = " << (meSBI-meSpow-meHBI)/meSpow << std::endl;

  return (meSBI-meSpow-meHBI)/meSpow;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoI_H(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);
 
  float meSpow;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSpow, false);
  else
    _mela->computeProdDecP(meSpow, false);

  float meH;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  //Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 0);
  //
  if (!isVBF)
    _mela->computeP(meH, false);
  else
    _mela->computeProdDecP(meH, false);

  float meS_Honly;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!isVBF)
    _mela->computeP(meS_Honly, false);
  else
     _mela->computeProdDecP(meS_Honly, false);

  _mela->resetInputEvent();

  //std::cout << "### meS = " << meS << " meSpow = " << meSpow << " meB = " << meB << " meSBI = " << meSBI << std::endl;
  //std::cout << "### weight = " << (meSBI-meS-meB)/meSpow << std::endl;

  return (meS_Honly-meH-meSpow)/meSpow;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoI_B(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);
 
  float meSpow;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSpow, false);
  else
    _mela->computeProdDecP(meSpow, false);

  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdDecP(meSBI, false);

  float meB;
  _mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meB, false);
  else
    _mela->computeProdDecP(meB, false);

  _mela->resetInputEvent();

  //std::cout << "### meS = " << meS << " meSpow = " << meSpow << " meB = " << meB << " meSBI = " << meSBI << std::endl;
  //std::cout << "### weight = " << (meSBI-meS-meB)/meSpow << std::endl;

  return (meSBI-meSpow-meB)/meSpow;

}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoI_HB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);
 
  float meSpow;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSpow, false);
  else
    _mela->computeProdDecP(meSpow, false);

  float meH;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  //Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 0);
  //
  if (!isVBF)
    _mela->computeP(meH, false);
  else
    _mela->computeProdDecP(meH, false);

  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 0);
  //
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdDecP(meSBI, false);

  float meB;
  _mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meB, false);
  else
    _mela->computeProdDecP(meB, false);

  _mela->resetInputEvent();

  //std::cout << "### meS = " << meS << " meSpow = " << meSpow << " meB = " << meB << " meSBI = " << meSBI << std::endl;
  //std::cout << "### weight = " << (meSBI-meS-meB)/meSpow << std::endl;

  return (meSBI-meB-meH)/meSpow;

}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);

  float meS;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!isVBF)
    _mela->computeP(meS, false);
  else
    _mela->computeProdDecP(meS, false);
  float meB;
  _mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJEW : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meB, false);
  else
    _mela->computeProdDecP(meB, false);

  _mela->resetInputEvent();
  return meB/meS;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaReweighterWW::weightStoH(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2, 
                                         const std::vector<TLorentzVector>& associated){ 

  setupDaughters(isVBF, id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2, associated);
 
  float meSpow;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF_S : TVar::ZZGG);
  // Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //
  if (!isVBF)
    _mela->computeP(meSpow, false);
  else
    _mela->computeProdDecP(meSpow, false);

  float meH;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  //Added here -- U. Sarica
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 0);
  //
  if (!isVBF)
    _mela->computeP(meH, false);
  else
    _mela->computeProdDecP(meH, false);


  _mela->resetInputEvent();

  //std::cout << "### meS = " << meS << " meSpow = " << meSpow << " meB = " << meB << " meSBI = " << meSBI << std::endl;
  //std::cout << "### weight = " << (meSBI-meS-meB)/meSpow << std::endl;

  return (meH)/meSpow;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void MelaReweighterWW::setupDaughters(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                    const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2,
                    const std::vector<TLorentzVector>& associated){
  
  _daughters->clear();
  _daughters->push_back(SimpleParticle_t(id_l1, l1));
  _daughters->push_back(SimpleParticle_t(id_l2, l2));
  _daughters->push_back(SimpleParticle_t(id_n1, n1));
  _daughters->push_back(SimpleParticle_t(id_n2, n2));
  _associated->clear();
  for (unsigned int i = 0; i < associated.size(); ++i){
    _associated->push_back(SimpleParticle_t(0, associated[i]));
  }

  if (_candModified != 0){
    delete _candModified;
    _candModified = 0;
  }

  _mela->resetInputEvent();
  _mela->setInputEvent(_daughters, _associated, 0, false); 
  if (isVBF){
    recast();
  }

}                    
