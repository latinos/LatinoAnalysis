#include "TLorentzVector.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

//
// Email exchange after DIS2014
//
// From theorist colleague, Tobias Kasprzik
// arXiv:1401.3964
// 
// arXiv:1208.3147
// arXiv:1311.5491
// arXiv:1310.3972
// arXiv:1305.5402
//


class qq2vvEWKcorrections {
public:
 //! constructor
 qq2vvEWKcorrections();
 qq2vvEWKcorrections(std::string fName);
 
 virtual ~qq2vvEWKcorrections() {}
 
 std::vector<std::vector<float> > Table_EWK;
 
 void initqq2WWEWKCorr(std::string fName = "out_qqbww_EW_L8_200_forCMS.dat" );
 std::vector<std::vector<float> > findCorrection( float sqrt_s_hat, float t_hat );
 
 float getqq2WWEWKCorr(
  float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st W
  float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd W
  float ptv1 , float etav1 , float phiv1 ,             // neutrino from 1st W
  float ptv2 , float etav2 , float phiv2 ,             // neutrino from 2nd W
  float x1   , float x2 ,                              // parton x-Bjorken
  float id1  , float id2                               // parton PDG id's
  //     float Energy = 8000.
 );
};


qq2vvEWKcorrections::qq2vvEWKcorrections() {
 initqq2WWEWKCorr();
}

qq2vvEWKcorrections::qq2vvEWKcorrections(std::string fName) {
 initqq2WWEWKCorr(fName);
}



// Init: read correction table
void qq2vvEWKcorrections::initqq2WWEWKCorr(std::string fName) {
 
 Table_EWK.clear();
 
 std::ifstream myReadFile;
 std::vector<float> Table_line;
 myReadFile.open(fName.c_str());
 
 int Start=0;
 while (!myReadFile.eof()) {
  Start++;
  std::string output;
  myReadFile >> output;
  if(Start%5!=0) Table_line.push_back(atof(output.c_str()));
  if(Start%5==0) {
   Table_line.push_back(atof(output.c_str()));
   Table_EWK.push_back(Table_line);
   Table_line.clear();
  }
 }
 
 myReadFile.close();
 
}


// find closest value in table
std::vector<std::vector<float> > qq2vvEWKcorrections::findCorrection( float sqrt_s_hat, float t_hat ) {
 std::vector<std::vector<float> > final_info;
 std::vector<float> Corrections;
 std::vector<float> sAndt;
 float min_s=9999999999., min_t=99999999999.;
 int index_s=-1, index_t=-1;
 //Find Minimum sqrt_S
 for(unsigned int i=0; i<Table_EWK.size(); i++){
  if( fabs(Table_EWK[i][0] - sqrt_s_hat) < min_s ){
   min_s = fabs(Table_EWK[i][0] - sqrt_s_hat);
   index_s = i;
  }
 }
 // Find Minimum T
 for(unsigned int j=0; j<Table_EWK.size(); j++){
  if( Table_EWK[j][0]==Table_EWK[index_s][0] && fabs(Table_EWK[j][1] - t_hat) < min_t ){
   min_t = fabs(Table_EWK[j][1] - t_hat);
   index_t = j;
  }
 }
 Corrections.push_back(Table_EWK[index_t][2]);
 Corrections.push_back(Table_EWK[index_t][3]);
 Corrections.push_back(Table_EWK[index_t][4]);
 sAndt.push_back(Table_EWK[index_t][0]);
 sAndt.push_back(Table_EWK[index_t][1]);
 final_info.push_back(Corrections);
 final_info.push_back(sAndt);
 return final_info;
}


// Get corrections from table
float qq2vvEWKcorrections::getqq2WWEWKCorr(
 float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st W
 float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd W
 float ptv1 , float etav1 , float phiv1 ,             // neutrino from 1st W
 float ptv2 , float etav2 , float phiv2 ,             // neutrino from 2nd W
 float x1   , float x2 ,                              // parton x-Bjorken
 float id1  , float id2                               // parton PDG id's
 //                       int   TypeFirst = 1 ,                                // ??????????????????????????
 //                        float Energy = 8000.
) {
 
//  float Energy = 8000.;
 float Energy = 6500.;   //---- 13 TeV ??? Was this wrong before?
 // Create lepton and neutrino vectors
 TLorentzVector l1;
 TLorentzVector l2;
 TLorentzVector v1;
 TLorentzVector v2;
 
 float me   = 0.001*0.510998928 ;
 float mmu  = 0.001*105.6583715 ;
 float mtau = 0.001*1776.82     ;
 
 float ml1(0) , ml2(0) ;
 
 if      ( idl1 == 11 ) ml1 = me   ;
 else if ( idl1 == 13 ) ml1 = mmu  ;
 else if ( idl1 == 15 ) ml1 = mtau ;
 if      ( idl2 == 11 ) ml2 = me   ;
 else if ( idl2 == 13 ) ml2 = mmu  ;
 else if ( idl2 == 15 ) ml2 = mtau ;
 
 l1.SetPtEtaPhiM(ptl1,etal1,phil1,ml1);
 l2.SetPtEtaPhiM(ptl2,etal2,phil2,ml2);
 v1.SetPtEtaPhiM(ptv1,etav1,phiv1,0.0);
 v2.SetPtEtaPhiM(ptv2,etav2,phiv2,0.0);
 
 TLorentzVector W1 = l1+v1; // W1
 TLorentzVector W2 = l2+v2; // W2
 TLorentzVector WW = W1+W2;
 
 //---- FIX
 //---- swap 1 <->2 for leptons and neutrinos, to get correctly association l-v:
 //---- use as test invariatn mass of di-leptons
 //----    needed because leptons are ordered by "pt" and not by "mother" in the input! 
 //
 // -> 1.0 value is arbitrary and coming from old code (it was 0.1) and run-1 latino trees
 //
 // if (fabs(W1.M() - 80.385) > 1.0 && fabs(W2.M() - 80.385) > 1.0) {
 //  W1 = l1+v2; // W1
 //  W2 = l2+v1; // W2
 //  WW = W1+W2;
 // }
 //---- end FIX
 
 
 float M_12   = 80.385 , M_22 = 80.385 ;
 
 TLorentzVector p1; p1.SetPxPyPzE(0.,0.,Energy*x1,Energy*x1);
 TLorentzVector p2; p2.SetPxPyPzE(0.,0.,-Energy*x2,Energy*x2);
 
 //S-HAT
 float s_hat = pow(WW.E(),2)-pow(WW.Px(),2)-pow(WW.Py(),2)-pow(WW.Pz(),2); // ScalarProd(WW) (p1+p2)^2 = (p3+p4)^2 ~ +2*p1*p2
 //T_HAT
 //float t_hat2 = TypeFirst == 1 ? p1.M()*p1.M() + M_12*M_12 - 2*( p1.E()*W1.E() - p1.Px()*W1.Px() - p1.Py()*W1.Py() - p1.Pz()*W1.Pz() ) :
 //                                p1.M()*p1.M() + M_22*M_22 - 2*( p1.E()*W2.E() - p1.Px()*W2.Px() - p1.Py()*W2.Py() - p1.Pz()*W2.Pz() )   ; //T_HAT LO
 float la1 = sqrt( pow(s_hat,2) );            //la = sqrt( pow(a,2)+pow(b,2)+pow(c,2)-2*(a*b+a*c+b*c) );
 float la2 = sqrt( pow(s_hat,2) + pow(M_12,2) + pow(M_22,2) - 2*(s_hat*M_12 + s_hat*M_22 + M_12*M_22) );
 //  Boost: boost ext. momenta in CM frame of W1,W2
 TLorentzVector W1_b = W1, W2_b = W2;
 TLorentzVector p1_b = p1, p2_b = p2;
 W1_b.Boost( -WW.BoostVector() );
 W2_b.Boost( -WW.BoostVector() );
 p1_b.Boost( -WW.BoostVector() );
 p2_b.Boost( -WW.BoostVector() );
 
 //  Uni-vector
 TLorentzVector ee1 = p1_b*(1./sqrt( pow(p1_b.X(),2)+pow(p1_b.Y(),2)+pow(p1_b.Z(),2) ));
 TLorentzVector ee2 = p2_b*(1./sqrt( pow(p2_b.X(),2)+pow(p2_b.Y(),2)+pow(p2_b.Z(),2) ));
 TLorentzVector z1  = W1_b*(1./sqrt( pow(W1_b.X(),2)+pow(W1_b.Y(),2)+pow(W1_b.Z(),2) ));
 TLorentzVector z2  = W2_b*(1./sqrt( pow(W2_b.X(),2)+pow(W2_b.Y(),2)+pow(W2_b.Z(),2) ));
 //  "effective" beam axis
 float abse = sqrt( pow(ee1.X()-ee2.X(),2) + pow(ee1.Y()-ee2.Y(),2) + pow(ee1.Z()-ee2.Z(),2) );
 TLorentzVector ee = (ee1-ee2) * (1. / abse);
 //  "effective" scattering angle
 float costh = ee.X()*z1.X()+ee.Y()*z1.Y()+ee.Z()*z1.Z();
 //  final T_HAT
 float t_hat= M_12 - (1./2.)*(s_hat+M_12-M_22) + (1/(2*s_hat))*la1*la2*costh; //Mz-1/2*s+1/(2*s)*la(s,0,0)*la(s,mZ,mZ)*costh  or: (p1-p3)^2 = (p2-p4)^2 ~ -2*p1*p3
 //Quark Type
 int quarkType = -1.;
 if(      fabs(id1)==2 && fabs(id2)==2 ) quarkType=0; //delta_uub
 else if( fabs(id1)==1 && fabs(id2)==1 ) quarkType=1; //delta_ddb
 else if( fabs(id1)==5 && fabs(id2)==5 ) quarkType=2; //delta_bbb
 else if( fabs(id1)==4 && fabs(id2)==4 ) quarkType=0; // cc as delta_buu
 else if( fabs(id1)==3 && fabs(id2)==3 ) quarkType=1; // ss as delta_bdd
 
 // Extracting corrections
 float EWK_w = 1. ;
 //  std::cout << " quarkType = " << quarkType << " id1 = " << id1 << " id2 = " << id2 << std::endl;
 if( quarkType!=-1 ){
  float sqrt_s_hat = sqrt(s_hat);
  std::vector<std::vector<float> > EWK_w2_vec = findCorrection( sqrt_s_hat, t_hat );
  float EWK_w2 = 1. + EWK_w2_vec[0][quarkType];
  EWK_w = EWK_w2;
 }
 
 return EWK_w ;
 
}



