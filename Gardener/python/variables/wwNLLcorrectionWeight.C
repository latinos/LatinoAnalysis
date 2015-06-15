
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
 wwNLL(std::string filename, std::string mcsample);
 ~wwNLL();
 
 //! functions
 void SetPTWW( float ptl1 , float phil1,   float ptl2 , float phil2,   float ptv1 , float phiv1 ,   float ptv2 , float phiv2);
 float nllWeight(int variation, int kind = 0); //---- variation = -1, 0, 1 for down, central, up    and kind is 0=Q or 1=R
 
private:
 //! variables
 TFile* fileInput;
 TLorentzVector L1,L2,V1,V2;
 
 float ptww;
 TH1F* h_cen;
 TH1F* h_Q_down;
 TH1F* h_Q_up;
 TH1F* h_R_down;
 TH1F* h_R_up;
 
};

//! constructor
wwNLL::wwNLL(std::string filename, std::string mcsample) {
 
 //  gDirectory->cd(0);
 fileInput = new TFile(filename.c_str(),"READ");
 //  "../../data/ratio_output_nnlo.root"
 gDirectory->cd(0);
 h_cen    = (TH1F*) fileInput -> Get((std::string("ratio_") + mcsample + std::string("_central")).c_str());
 h_Q_down = (TH1F*) fileInput -> Get((std::string("ratio_") + mcsample + std::string("_Qdown")).c_str());
 h_Q_up   = (TH1F*) fileInput -> Get((std::string("ratio_") + mcsample + std::string("_Qup")).c_str());
 h_R_down = (TH1F*) fileInput -> Get((std::string("ratio_") + mcsample + std::string("_Rdown")).c_str());
 h_R_up   = (TH1F*) fileInput -> Get((std::string("ratio_") + mcsample + std::string("_Rup")).c_str());
 
 //    ratio_powheg_central
 //    ratio_powheg_Qdown
 //    ratio_powheg_Qup
 //    ratio_powheg_Rdown
 //    ratio_powheg_Rup
 
}

wwNLL::~wwNLL() {
 //  fileInput -> Close();
 //  delete fileInput;
}


//! functions
void wwNLL::SetPTWW( float ptl1 , float phil1,   float ptl2 , float phil2,   float ptv1 , float phiv1 ,   float ptv2 , float phiv2) {
 L1.SetPtEtaPhiM(ptl1, 0., phil1, 0.);
 L2.SetPtEtaPhiM(ptl2, 0., phil2, 0.);
 V1.SetPtEtaPhiM(ptv1, 0., phiv1, 0.);
 V2.SetPtEtaPhiM(ptv2, 0., phiv2, 0.);
 ptww = (L1+L2+V1+V2).Pt();
}


float wwNLL::nllWeight(int variation, int kind){
 float weight = -1;
 
 int bin = -1;
 if (variation == 0) {
  bin = h_cen -> FindBin(ptww);
  weight = h_cen -> GetBinContent (bin);
 }
 else if (variation == -1) {
  if (kind == 0) {
   bin = h_Q_down -> FindBin(ptww);
   weight = h_Q_down -> GetBinContent (bin);
  }
  if (kind == 1) {
   bin = h_R_down -> FindBin(ptww);
   weight = h_R_down -> GetBinContent (bin);
  }
 }
 else if (variation == 1) {
  if (kind == 0) {
   bin = h_Q_up -> FindBin(ptww);
   weight = h_Q_up -> GetBinContent (bin);
  }
  if (kind == 1) {
   bin = h_R_up -> FindBin(ptww);
   weight = h_R_up -> GetBinContent (bin);
  }
 }
 
 
 //  std::cout << " ptww = " << ptww << " bin = " << bin << " weight = " << weight << std::endl;
 return weight;
}



