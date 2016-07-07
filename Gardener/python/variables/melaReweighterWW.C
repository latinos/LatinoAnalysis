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

class MelaReweighterWW{
  public:
  MelaReweighterWW(double com, double mpole, double width);
  ~MelaReweighterWW();
  
  void setMelaHiggsMassWidth(double mpole, double wpole);

  void resetMCFM_EWKParameters(double Gf=1.16639E-05, double alphaEW=1./128., double mW=80.399, double mZ=91.1876, double sin2thetaW=0.23119);

  float weightStoSBI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                    const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2);
  
  float weightStoI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2);
  
  float weightStoB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                       const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2);

  private:
  void setupDaughters(const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                      const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2);

  double _com;
  double _mpole;
  double _width;

  Mela* _mela;
  SimpleParticleCollection_t* _daughters;

};

MelaReweighterWW::MelaReweighterWW(double com, double mpole, double width):
_com(com),
_mpole(mpole),
_width(width),
_daughters(new SimpleParticleCollection_t())
{
  //TVar::VerbosityLevel verbosity = TVar::DEBUG;
  TVar::VerbosityLevel verbosity = TVar::ERROR;
  _mela =  new Mela(com, mpole, verbosity);
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  _mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  _mela->setCandidateDecayMode(TVar::CandidateDecay_WW);
  //Gf=1.16639E-05, alphaEW=1./128., mW=80.399, mZ=91.1876, sin2thetaW=0.23119
  resetMCFM_EWKParameters();
}

MelaReweighterWW::~MelaReweighterWW(){
  delete _daughters;
  delete _mela;
}

void MelaReweighterWW::setMelaHiggsMassWidth(double mpole, double wpole){
  _mela->setMelaHiggsMassWidth(mpole, wpole, 0);
}

void MelaReweighterWW::resetMCFM_EWKParameters(double Gf, double alphaEW, double mW, double mZ, double sin2thetaW){
  _mela->resetMCFM_EWKParameters(Gf, alphaEW, mW, mZ, sin2thetaW);
}


float MelaReweighterWW::weightStoSBI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2){    
  
  setupDaughters(id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2);

  float meS;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meS, false);
  else
    _mela->computeProdP(meS, false);
  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdP(meSBI, false);
  
  _mela->resetInputEvent();  
  return meSBI/meS;
}

float MelaReweighterWW::weightStoI(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2){ 

  setupDaughters(id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2);

  float meS;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  _mela->computeP(meS, false);
  float meSBI;
  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meSBI, false);
  else
    _mela->computeProdP(meSBI, false);
  float meB;
  _mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meB, false);
  else
    _mela->computeProdP(meB, false);

  _mela->resetInputEvent();
  return (meSBI-meS-meB)/meS;
}

float MelaReweighterWW::weightStoB(bool isVBF, const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                                         const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2){ 

  setupDaughters(id_l1, id_l2, id_n1, id_n2, l1, l2, n1, n2);

  float meS;
  _mela->setProcess(TVar::HSMHiggs, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meS, false);
  else
    _mela->computeProdP(meS, false);
  float meB;
  _mela->setProcess(TVar::bkgWW, TVar::MCFM, isVBF ? TVar::JJVBF : TVar::ZZGG);
  if (!isVBF)
    _mela->computeP(meB, false);
  else
    _mela->computeProdP(meB, false);

  _mela->resetInputEvent();
  return meB/meS;
}

void MelaReweighterWW::setupDaughters(const int& id_l1,  const int& id_l2, const int& id_n1, const int& id_n2,
                    const TLorentzVector& l1, const TLorentzVector& l2, const TLorentzVector& n1, const TLorentzVector& n2){
  
  _daughters->clear();
  _daughters->push_back(SimpleParticle_t(id_l1, l1));
  _daughters->push_back(SimpleParticle_t(id_l2, l2));
  _daughters->push_back(SimpleParticle_t(id_n1, n1));
  _daughters->push_back(SimpleParticle_t(id_n2, n2));

  _mela->setInputEvent(_daughters, 0, 0, false); 

}                    
