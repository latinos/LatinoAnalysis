//STANDARD ROOT INCLUDES
#include <TH2.h>
#include <TROOT.h>
#include <TH1.h>
#include <TH2.h>
#include <TProfile.h>
#include <TCanvas.h>
#include <TTree.h>
#include <TFile.h>
#include <TChain.h>
#include <TChainElement.h>
#include <TLegend.h>
#include <TDirectory.h>
#include <TStyle.h>
#include <TGraphAsymmErrors.h>
#include <TGraphErrors.h>
#include <TMatrixT.h>
#include <TVectorT.h>
#include <Math/GenVector/Cartesian3D.h>
#include <utility>
#include <Math/GenVector/PxPyPzE4D.h>
#include <TGraph.h>
#include <TLine.h>
#include <THStack.h>
#include <TLorentzVector.h>
#include <TMath.h>
#include <TVector3.h>
#include <TSystem.h>
#include <TRandom3.h>
#include <TLegend.h>
#include <TString.h>

////STANDARD C++ INCLUDES
#include <time.h>
#include <stdio.h> /* printf */
#include <math.h> /* sqrt */
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#include <vector>
#include <stdlib.h>

#define PI 3.141592653589793
#define angle 180/3.141592654

using namespace std;

class DYCalc{
public:
   //contructor
   DYCalc() {};
   virtual ~DYCalc() {};
   float k_MC(TString sFile , TString sNum , TString sDen);
   float Ek_MC(TString sFile , TString sNum , TString sDen);
   float R_outin_MC(TString sFile , TString sNum , TString sDen);
   float ER_outin_MC(TString sFile , TString sNum , TString sDen);
   float N_DY(float R , float Nin , float k , float Neu, float Nvv );
   float EN_DY(float R , float Nin , float k , float Neu, float Nvv, float ER, float ENin, float Ek, float ENeu, float ENvv );
};


float DYCalc::k_MC(TString sFile , TString sNum , TString sDen){
   TFile *KffFile = new TFile(sFile,"READ");
   float Num = ((TH1F*) KffFile->Get(sNum))->Integral();
   float Den = ((TH1F*) KffFile->Get(sDen))->Integral();
   KffFile->Close();
   return sqrt( Num / Den );
}

float DYCalc::Ek_MC(TString sFile , TString sNum , TString sDen){
   TFile *KffFile = new TFile(sFile,"READ");
   float Num = ((TH1F*) KffFile->Get(sNum))->Integral();
   float Den = ((TH1F*) KffFile->Get(sDen))->Integral();
   float ENum = ((TH1F*) KffFile->Get(sNum))->GetBinError(1);
   float EDen = ((TH1F*) KffFile->Get(sDen))->GetBinError(1);
   KffFile->Close();
   return 0.5 * sqrt( pow((ENum/Num),2) + pow((EDen/Den),2) ) * k_MC(sFile , sNum , sDen);
}

float DYCalc::R_outin_MC(TString sFile , TString sNum , TString sDen){
   TFile *RFile = new TFile(sFile,"READ");
   map<string,TH1F*> histos;
   histos["DY_R_out"] = (TH1F*)RFile->Get(sNum);
   histos["DY_R_in"]  = (TH1F*)RFile->Get(sDen);
   float R = histos["DY_R_out"]->Integral()/histos["DY_R_in"]->Integral() ;
   RFile->Close();
   return R ;
}

float DYCalc::ER_outin_MC(TString sFile , TString sNum , TString sDen){
   TFile *RFile = new TFile(sFile,"READ");
   map<string,TH1F*> histos;
   histos["DY_R_out"] = (TH1F*)RFile->Get(sNum);
   histos["DY_R_in"]  = (TH1F*)RFile->Get(sDen);
   TH1F* HR_outin_MC  = new TH1F("HR_outin_MC","HR_outin_MC",1,0,2);
   HR_outin_MC->Divide(histos["DY_R_out"],histos["DY_R_in"],1,1,"b");
   float ER = HR_outin_MC->GetBinError(1);
   RFile->Close();
   return ER;   
}

float DYCalc::N_DY(float R , float Nin , float k , float Neu, float Nvv ){
  return R * ( Nin - (k * Neu * 0.5) - Nvv);
}

float DYCalc::EN_DY(float R , float Nin , float k , float Neu, float Nvv, float ER, float ENin, float Ek, float ENeu, float ENvv ){

   //cout <<"ERROR: " <<   R   << " " <<  Nin   << " " <<  k   << " " <<  Neu  << " " <<  Nvv  << " " <<  ER  << " " <<  ENin  << " " <<  Ek  << " " <<  ENeu  << " " <<  ENvv << endl;

  /*
  Neu = 0.0001   ;
  cout << N_DY(R, Nin, k, Neu, Nvv) << endl;
  cout << pow((ER/R),2) << endl;
  cout << sqrt( pow(ENin,2) + pow(ENvv,2) + pow((0.5*Neu*k*sqrt(pow((ENeu/Neu),2)+pow((Ek/k),2))),2)) << endl;
  cout << Nin - (k * Neu * 0.5) - Nvv << endl;
  */
  return  N_DY(R, Nin, k, Neu, Nvv)*sqrt( pow((ER/R),2) + pow((( sqrt( pow(ENin,2) + pow(ENvv,2) + pow((0.5*Neu*k*sqrt(pow((ENeu/Neu),2)+pow((Ek/k),2))),2)) )/( Nin - (k * Neu * 0.5) - Nvv )),2));



}

/*

class DY{
public:
   //contructor
   DY(TString sKffFile, TString sRFile);
   ~DY(); 
   
   //functions
   void  Print();
   float k_MC_ee_0j(); 
   float Ek_MC_ee_0j(); 
   float k_MC_uu_0j(); 
   float Ek_MC_uu_0j(); 
   float k_MC_ee_1j(); 
   float Ek_MC_ee_1j(); 
   float k_MC_uu_1j(); 
   float Ek_MC_uu_1j(); 
   float R_outin_MC_0j_ee(); 
   float ER_outin_MC_0j_ee(); 
   float R_outin_MC_0j_uu(); 
   float ER_outin_MC_0j_uu(); 
   float R_outin_MC_1j_ee(); 
   float ER_outin_MC_1j_ee(); 
   float R_outin_MC_1j_uu(); 
   float ER_outin_MC_1j_uu();
   
private:
   map<string,TH1F*> histos;
   float N_DY_k_0j_ee_in;
   float N_DY_k_0j_ee_out;
   float N_DY_k_0j_uu_in;
   float N_DY_k_0j_uu_out;
   float EN_DY_k_0j_ee_in;
   float EN_DY_k_0j_uu_in;
   float N_DY_k_1j_ee_in;
   float N_DY_k_1j_ee_out;
   float N_DY_k_1j_uu_in;
   float N_DY_k_1j_uu_out;
   float EN_DY_k_1j_ee_in;
   float EN_DY_k_1j_uu_in;
   float N_DY_R_0j_ee_in;
   float N_DY_R_0j_ee_out;
   float N_DY_R_0j_uu_in;
   float N_DY_R_0j_uu_out;
   float N_DY_R_0j_df_in;
   float N_DY_R_0j_df_out;
   float EN_DY_R_0j_ee_in;
   float EN_DY_R_0j_uu_in;
   float N_DY_R_1j_ee_in;
   float N_DY_R_1j_ee_out;
   float N_DY_R_1j_uu_in;
   float N_DY_R_1j_uu_out;
   float N_DY_R_1j_df_in;
   float N_DY_R_1j_df_out;
   float EN_DY_R_1j_ee_in;
   float EN_DY_R_1j_uu_in;
   TFile *KffFile ;
   TFile *RFile ;
};

DY::DY(TString sKffFile, TString sRFile){
   KffFile = new TFile(sKffFile,"READ");
   RFile   = new TFile(sRFile,"READ");
   histos["DY_k_0j_ee_in"]  = (TH1F*)KffFile->Get("0j_ee_in/events/histo_DY");
   histos["DY_k_0j_ee_out"] = (TH1F*)KffFile->Get("0j_ee_out/events/histo_DY");
   histos["DY_k_0j_uu_in"]  = (TH1F*)KffFile->Get("0j_uu_in/events/histo_DY");
   histos["DY_k_0j_uu_out"] = (TH1F*)KffFile->Get("0j_uu_out/events/histo_DY");
   histos["DY_k_1j_ee_in"]  = (TH1F*)KffFile->Get("1j_ee_in/events/histo_DY");
   histos["DY_k_1j_ee_out"] = (TH1F*)KffFile->Get("1j_ee_out/events/histo_DY");
   histos["DY_k_1j_uu_in"]  = (TH1F*)KffFile->Get("1j_uu_in/events/histo_DY");
   histos["DY_k_1j_uu_out"] = (TH1F*)KffFile->Get("1j_uu_out/events/histo_DY");
   N_DY_k_0j_ee_in  = histos["DY_k_0j_ee_in"]->Integral();
   N_DY_k_0j_ee_out = histos["DY_k_0j_ee_out"]->Integral();
   N_DY_k_0j_uu_in  = histos["DY_k_0j_uu_in"]->Integral();
   N_DY_k_0j_uu_out = histos["DY_k_0j_uu_out"]->Integral();
   EN_DY_k_0j_ee_in = histos["DY_k_0j_ee_in"]->GetBinError(1);
   EN_DY_k_0j_uu_in = histos["DY_k_0j_uu_in"]->GetBinError(1);
   N_DY_k_1j_ee_in  = histos["DY_k_1j_ee_in"]->Integral();
   N_DY_k_1j_ee_out = histos["DY_k_1j_ee_out"]->Integral();
   N_DY_k_1j_uu_in  = histos["DY_k_1j_uu_in"]->Integral();
   N_DY_k_1j_uu_out = histos["DY_k_1j_uu_out"]->Integral();
   EN_DY_k_1j_ee_in = histos["DY_k_1j_ee_in"]->GetBinError(1);
   EN_DY_k_1j_uu_in = histos["DY_k_1j_uu_in"]->GetBinError(1);
   
   histos["DY_R_0j_ee_in"]  = (TH1F*)RFile->Get("0j_ee_in/events/histo_DY");
   histos["DY_R_0j_ee_out"] = (TH1F*)RFile->Get("0j_ee_out/events/histo_DY");
   histos["DY_R_0j_uu_in"]  = (TH1F*)RFile->Get("0j_uu_in/events/histo_DY");
   histos["DY_R_0j_uu_out"] = (TH1F*)RFile->Get("0j_uu_out/events/histo_DY");
   histos["DY_R_0j_df_in"]  = (TH1F*)RFile->Get("0j_df_in/events/histo_DY");
   histos["DY_R_0j_df_out"] = (TH1F*)RFile->Get("0j_df_out/events/histo_DY");
   histos["DY_R_1j_ee_in"]  = (TH1F*)RFile->Get("1j_ee_in/events/histo_DY");
   histos["DY_R_1j_ee_out"] = (TH1F*)RFile->Get("1j_ee_out/events/histo_DY");
   histos["DY_R_1j_uu_in"]  = (TH1F*)RFile->Get("1j_uu_in/events/histo_DY");
   histos["DY_R_1j_uu_out"] = (TH1F*)RFile->Get("1j_uu_out/events/histo_DY");
   histos["DY_R_1j_df_in"]  = (TH1F*)RFile->Get("1j_df_in/events/histo_DY");
   histos["DY_R_1j_df_out"] = (TH1F*)RFile->Get("1j_df_out/events/histo_DY");
   N_DY_R_0j_ee_in  = histos["DY_R_0j_ee_in"]->Integral();
   N_DY_R_0j_ee_out = histos["DY_R_0j_ee_out"]->Integral();
   N_DY_R_0j_uu_in  = histos["DY_R_0j_uu_in"]->Integral();
   N_DY_R_0j_uu_out = histos["DY_R_0j_uu_out"]->Integral();
   N_DY_R_0j_df_in  = histos["DY_R_0j_df_in"]->Integral();
   N_DY_R_0j_df_out = histos["DY_R_0j_df_out"]->Integral();
   EN_DY_R_0j_ee_in = histos["DY_R_0j_ee_in"]->GetBinError(1);
   EN_DY_R_0j_uu_in = histos["DY_R_0j_uu_in"]->GetBinError(1);
   N_DY_R_1j_ee_in  = histos["DY_R_1j_ee_in"]->Integral();
   N_DY_R_1j_ee_out = histos["DY_R_1j_ee_out"]->Integral();
   N_DY_R_1j_uu_in  = histos["DY_R_1j_uu_in"]->Integral();
   N_DY_R_1j_uu_out = histos["DY_R_1j_uu_out"]->Integral();
   N_DY_R_1j_df_in  = histos["DY_R_1j_df_in"]->Integral();
   N_DY_R_1j_df_out = histos["DY_R_1j_df_out"]->Integral();
   EN_DY_R_1j_ee_in = histos["DY_R_1j_ee_in"]->GetBinError(1);
   EN_DY_R_1j_uu_in = histos["DY_R_1j_uu_in"]->GetBinError(1);
}
DY::~DY(){
   RFile->Close();
   KffFile->Close();
}

void DY::Print(){
   cout << N_DY_R_0j_ee_in <<endl;
}

float DY::k_MC_ee_0j(){
   return sqrt( N_DY_k_0j_ee_in / N_DY_k_0j_uu_in );
}

float DY::Ek_MC_ee_0j(){
   return 0.5 * sqrt( pow((EN_DY_k_0j_ee_in/N_DY_k_0j_ee_in),2) + pow((EN_DY_k_0j_uu_in/N_DY_k_0j_uu_in),2) ) * k_MC_ee_0j();
}

float DY::k_MC_uu_0j(){
   return sqrt( N_DY_k_0j_uu_in / N_DY_k_0j_ee_in );
}

float DY::Ek_MC_uu_0j(){
   return 0.5 * sqrt( pow((EN_DY_k_0j_ee_in/N_DY_k_0j_ee_in),2) + pow((EN_DY_k_0j_uu_in/N_DY_k_0j_uu_in),2) ) * k_MC_uu_0j();
}
   
float DY::k_MC_ee_1j(){
   return sqrt( N_DY_k_1j_ee_in / N_DY_k_1j_uu_in );
}

float DY::Ek_MC_ee_1j(){
   return 0.5 * sqrt( pow((EN_DY_k_1j_ee_in/N_DY_k_1j_ee_in),2) + pow((EN_DY_k_1j_uu_in/N_DY_k_1j_uu_in),2) ) * k_MC_ee_1j();
}

float DY::k_MC_uu_1j(){
   return sqrt( N_DY_k_1j_uu_in / N_DY_k_1j_ee_in );
}

float DY::Ek_MC_uu_1j(){
   return 0.5 * sqrt( pow((EN_DY_k_1j_ee_in/N_DY_k_1j_ee_in),2) + pow((EN_DY_k_1j_uu_in/N_DY_k_1j_uu_in),2) ) * k_MC_uu_1j();
}

float DY::R_outin_MC_0j_ee(){
   TH1F* HR_outin_MC_0j_ee = new TH1F("R_outin_MC_0j_ee","R_outin_MC_0j_ee",1,0,2);
   HR_outin_MC_0j_ee->Divide(histos["DY_R_0j_ee_out"],histos["DY_R_0j_ee_in"],1,1,"b");
   return HR_outin_MC_0j_ee->Integral();
}

float DY::R_outin_MC_0j_uu(){
   TH1F* HR_outin_MC_0j_uu = new TH1F("R_outin_MC_0j_uu","R_outin_MC_0j_uu",1,0,2);
   HR_outin_MC_0j_uu->Divide(histos["DY_R_0j_uu_out"],histos["DY_R_0j_uu_in"],1,1,"b");
   return HR_outin_MC_0j_uu->Integral();
}

float DY::ER_outin_MC_0j_ee(){
   TH1F* HER_outin_MC_0j_ee = new TH1F("ER_outin_MC_0j_ee","ER_outin_MC_0j_ee",1,0,2);
   HER_outin_MC_0j_ee->Divide(histos["DY_R_0j_ee_out"],histos["DY_R_0j_ee_in"],1,1,"b");
   return HER_outin_MC_0j_ee->GetBinError(1);
}

float DY::ER_outin_MC_0j_uu(){
   TH1F* HER_outin_MC_0j_uu = new TH1F("ER_outin_MC_0j_uu","ER_outin_MC_0j_uu",1,0,2);
   HER_outin_MC_0j_uu->Divide(histos["DY_R_0j_uu_out"],histos["DY_R_0j_uu_in"],1,1,"b");
   return HER_outin_MC_0j_uu->GetBinError(1);
}

float DY::R_outin_MC_1j_ee(){
   TH1F* HR_outin_MC_1j_ee = new TH1F("R_outin_MC_1j_ee","R_outin_MC_1j_ee",1,0,2);
   HR_outin_MC_1j_ee->Divide(histos["DY_R_1j_ee_out"],histos["DY_R_1j_ee_in"],1,1,"b");
   return HR_outin_MC_1j_ee->Integral();
}

float DY::R_outin_MC_1j_uu(){
   TH1F* HR_outin_MC_1j_uu = new TH1F("R_outin_MC_1j_uu","R_outin_MC_1j_uu",1,0,2);
   HR_outin_MC_1j_uu->Divide(histos["DY_R_1j_uu_out"],histos["DY_R_1j_uu_in"],1,1,"b");
   return HR_outin_MC_1j_uu->Integral();
}

float DY::ER_outin_MC_1j_ee(){
   TH1F* HER_outin_MC_1j_ee = new TH1F("ER_outin_MC_1j_ee","ER_outin_MC_1j_ee",1,0,2);
   HER_outin_MC_1j_ee->Divide(histos["DY_R_1j_ee_out"],histos["DY_R_1j_ee_in"],1,1,"b");
   return HER_outin_MC_1j_ee->GetBinError(1);
}

float DY::ER_outin_MC_1j_uu(){
   TH1F* HER_outin_MC_1j_uu = new TH1F("ER_outin_MC_1j_uu","ER_outin_MC_1j_uu",1,0,2);
   HER_outin_MC_1j_uu->Divide(histos["DY_R_1j_uu_out"],histos["DY_R_1j_uu_in"],1,1,"b");
   return HER_outin_MC_1j_uu->GetBinError(1);
}

*/
