
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <TFile.h>
#include <TH1F.h>
#include <iostream>
#include <TSystem.h>

class wwNLL {
public:
 //! constructor
 wwNLL(std::string mcsample);
 ~wwNLL();
 
 //! functions
 void SetPTWW( float ptl1 , float phil1,   float ptl2 , float phil2,   float ptv1 , float phiv1 ,   float ptv2 , float phiv2);
 void SetPTWW( float ptV1 , float phiV1,   float ptV2 , float phiV2);
 void SetPTWW( float ptV1 , float phiV1, float etaV1,   float ptV2 , float phiV2, float etaV2);

 float nllWeight(int variation, int kind = 0); //---- variation = -1, 0, 1 for down, central, up    and kind is 0=Q or 1=R
 float GetPTWW();
 float GetMWW();
 
private:
 //! variables
 TFile* fileInput;
 TLorentzVector L1,L2,V1,V2;
 TLorentzVector W1, W2;
 
 float ptww;
 float mww;
  
 TGraph* _resum_central;
 TGraph* _resum_Rup;
 TGraph* _resum_Rdown;
 TGraph* _resum_Qup;
 TGraph* _resum_Qdown;
 TGraph* _resum_5;
 
 TGraph* _mc_central;
 TGraph* _mc_Rup;
 TGraph* _mc_Rdown;
 TGraph* _mc_Qup;
 TGraph* _mc_Qdown;
 TGraph* _mc_5;
 
 
};

//! constructor
wwNLL::wwNLL(std::string mcsample, 
             std::string central,
             std::string resum_up,
             std::string resum_down,
             std::string scale_up,
             std::string scale_down,
             std::string nnlo_central,
             std::string powheg_Rdownl2nu_nlo,
             std::string powheg_Rdownl2nu_qup_nlo,
             std::string powheg_Rdownl2nu_qdown_nlo,
             std::string powheg_Rdownl2nu_sup_nlo,
             std::string powheg_Rdownl2nu_sdown_nlo,
             std::string powheg_Rdownl2nu_nnlo
) {
 
 _resum_central = new TGraph(central);
 _resum_Rup = new TGraph(resum_up);
 _resum_Rdown = new TGraph(resum_down);
 _resum_Qup = new TGraph(scale_up);
 _resum_Qdown = new TGraph(scale_down);
 _resum_5 = new TGraph(nnlo_central);
 _mc_central = new TGraph(powheg_Rdownl2nu_nlo);
 _mc_Rup = new TGraph(powheg_Rdownl2nu_qup_nlo);
 _mc_Rdown = new TGraph(powheg_Rdownl2nu_qdown_nlo);
 _mc_Qup = new TGraph(powheg_Rdownl2nu_sup_nlo);
 _mc_Qdown = new TGraph(powheg_Rdownl2nu_sdown_nlo);
 _mc_5 = new TGraph(powheg_Rdownl2nu_nnlo);
 
 ptww = -1;
 mww = -1;
 
}

wwNLL::~wwNLL() {
 //  fileInput -> Close();
 //  delete fileInput;
}


//! functions
float wwNLL::GetPTWW(){
 return ptww;
}

float wwNLL::GetMWW(){
 return mww;
}


void wwNLL::SetPTWW( float ptV1 , float phiV1, float etaV1,   float ptV2 , float phiV2, float etaV2) {
 W1.SetPtEtaPhiM(ptV1, etaV1, phiV1, 80.385);
 W2.SetPtEtaPhiM(ptV2, etaV2, phiV2, 80.385);
 ptww = (W1+W2).Pt();
 mww  = (W1+W2).M();
}

void wwNLL::SetPTWW( float ptV1 , float phiV1,   float ptV2 , float phiV2) {
 W1.SetPtEtaPhiM(ptV1, 0., phiV1, 0.);
 W2.SetPtEtaPhiM(ptV2, 0., phiV2, 0.);
 ptww = (W1+W2).Pt();
}

void wwNLL::SetPTWW( float ptl1 , float phil1,   float ptl2 , float phil2,   float ptv1 , float phiv1 ,   float ptv2 , float phiv2) {
 L1.SetPtEtaPhiM(ptl1, 0., phil1, 0.);
 L2.SetPtEtaPhiM(ptl2, 0., phil2, 0.);
 V1.SetPtEtaPhiM(ptv1, 0., phiv1, 0.);
 V2.SetPtEtaPhiM(ptv2, 0., phiv2, 0.);
 ptww = (L1+L2+V1+V2).Pt();
}

float wwNLL::nllWeight(int variation, int kind){
 float weight = -1;

//  int bin = -1;
//  
//  bin = int (320*ptww/160.);
//  
//  if (!(bin < 0 || bin >= 320)) {
//    
//   if (variation == 0) {
//    weight = _reweightingFactors_central[bin];   
//   }
//   else if (variation == -1) {
//    if (kind == 0) {
//     weight = _reweightingFactors_Qdown[bin];   
//    }
//    if (kind == 1) {
//     weight = _reweightingFactors_Rdown[bin];   
//    }
//   }
//   else if (variation == 1) {
//    if (kind == 0) {
//     weight = _reweightingFactors_Qup[bin];   
//    }
//    if (kind == 1) {
//     weight = _reweightingFactors_Rup[bin];   
//    }
//   }
//  }
 
 
 if (variation == 0) {
  weight = = ptww < 160. ? _resum_central->Eval(ptww)/_mc_central->Eval(ptww) : 1;
 }
 else if (variation == -1) {
  if (kind == 0) {
   weight = = ptww < 160. ? _resum_Qdown->Eval(ptww)/_mc_Qdown->Eval(ptww) : 1;
//    weight = _reweightingFactors_Qdown[bin];   
  }
  if (kind == 1) {
   weight = = ptww < 160. ? _resum_Rdown->Eval(ptww)/_mc_Rdown->Eval(ptww) : 1;
//    weight = _reweightingFactors_Rdown[bin];   
  }
 }
 else if (variation == 1) {
  if (kind == 0) {
   weight = = ptww < 160. ? _resum_Qup->Eval(ptww)/_mc_Qup->Eval(ptww) : 1;
//    weight = _reweightingFactors_Qup[bin];   
  }
  if (kind == 1) {
   weight = = ptww < 160. ? _resum_Rup->Eval(ptww)/_mc_Rup->Eval(ptww) : 1;
//    weight = _reweightingFactors_Rup[bin];   
  }
 }
 
 return weight;

 
}



float wwNLL::nllnnloWeight(int variation, int kind){

 
}
 




