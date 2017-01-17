#include "TLorentzVector.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>


//Code developped by Nicolas Postiau for the 2l2nu group



class qq2wvEWKcorrections {
public:
 //! constructor
 qq2wvEWKcorrections();
 qq2wvEWKcorrections(std::string fName);
 
 virtual ~qq2wvEWKcorrections() {}
 
 std::vector<std::vector<float> > Table_EWK;
 
 void initqq2WVEWKCorr(std::string fName = "out_qqbww_EW_L8_200_forCMS.dat" );
 std::vector<float> findCorrection( float sqrt_s_hat, float t_hat );
 
 std::vector<float> getqq2WVEWKCorr(
  float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st W
  float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd W
  float ptv1 , float etav1 , float phiv1 , float idv1 , // neutrino from 1st W
  float ptv2 , float etav2 , float phiv2 , float idv2 , // neutrino from 2nd W
  float x1   , float x2 ,                              // parton x-Bjorken
  float id1  , float id2,                               // parton PDG id's
  float isVV                         //   0 = isZZ, 1 = isWZ
  //     float Energy = 8000.
 );
};


qq2wvEWKcorrections::qq2wvEWKcorrections() {
 initqq2WVEWKCorr();
}

qq2wvEWKcorrections::qq2wvEWKcorrections(std::string fName) {
 initqq2WVEWKCorr(fName);
}



// Init: read correction table
void qq2wvEWKcorrections::initqq2WVEWKCorr(std::string fName) {
 
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
  if(Start%5==0){
    Table_line.push_back(atof(output.c_str()));
    Table_EWK.push_back(Table_line);
    Table_line.clear();
  }

 }
 myReadFile.close();
 
}







// find closest value in table
std::vector<float> qq2wvEWKcorrections::findCorrection( float sqrt_s_hat, float t_hat ) {
 
  unsigned int j = 0;
  float best = 0.8E+04; //highest value of sqrt s hat in the table
  if( sqrt_s_hat > best) j = 39800; //in the very rare case where we have bigger s than our table (table is for 8TeV and we run at 13TeV)
  else{
    for(unsigned int i = 0 ; i < 40000 ; i = i+200){
      if(fabs(sqrt_s_hat - Table_EWK[i][0]) < best){
        best = fabs(sqrt_s_hat - Table_EWK[i][0]);
        j = i;
      }
      else break ;
    }
  }
  best = Table_EWK[j+199][1];
  if(t_hat > best) j = j+199; //in the very rare case where we have bigger t than our table
  else{
    best = 0.1E+09;
    for(unsigned int k = j ; k < j + 200 ; k++){
      if(fabs(t_hat - Table_EWK[k][1]) < best){
        best = fabs(t_hat - Table_EWK[k][1]);
        j = k;
      }
      else break ;
    }
  }
  std::vector<float> EWK_w2_vec;
  EWK_w2_vec.push_back(Table_EWK[j][2]); //ewk corrections for quark u/c
  EWK_w2_vec.push_back(Table_EWK[j][3]); //ewk corrections for quark d/s
  EWK_w2_vec.push_back(Table_EWK[j][4]); //ewk corrections for quark b
  return EWK_w2_vec ;
}
  
  
  
  

 //The main function, will return the kfactor
 //Same code is used for ZZ and WZ.
 
 // Get corrections from table
 std::vector<float> qq2wvEWKcorrections::getqq2WVEWKCorr(
   float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st V , and the charged lepton in case of W
   float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd V
   float ptv1 , float etav1 , float phiv1 , float idv1 , // neutrino from 1st V
   float ptv2 , float etav2 , float phiv2 , float idv2 , // neutrino/lepton from 2nd V
   float x1   , float x2 ,                              // parton x-Bjorken
   float id1  , float id2,                              // parton PDG id's
   float isVV                         //   0 = isZZ, 1 = isWZ
 ) {
   
   float kFactor = 1;
   
   int isZZ = 0;
   int isWZ = 0;
   
   if (isVV == 0) isZZ = 1;
   if (isVV == 1) isWZ = 1;
   
   
   // Create lepton and neutrino vectors
   TLorentzVector l1;
   TLorentzVector l2;
   TLorentzVector v1;
   TLorentzVector v2;
   
   float me   = 0.001*0.510998928 ;
   float mmu  = 0.001*105.6583715 ;
   float mtau = 0.001*1776.82     ;
   
   float ml1(0) , ml2(0) ;
   float mv1(0) , mv2(0) ;
   
   if      ( fabs(idl1) == 11 ) ml1 = me   ;
   else if ( fabs(idl1) == 13 ) ml1 = mmu  ;
   else if ( fabs(idl1) == 15 ) ml1 = mtau ;
   else                         ml1 = 0;  
   
   if      ( fabs(idl2) == 11 ) ml2 = me   ;
   else if ( fabs(idl2) == 13 ) ml2 = mmu  ;
   else if ( fabs(idl2) == 15 ) ml2 = mtau ;
   else                         ml2 = 0;  

   if      ( fabs(idv1) == 11 ) mv1 = me   ;
   else if ( fabs(idv1) == 13 ) mv1 = mmu  ;
   else if ( fabs(idv1) == 15 ) mv1 = mtau ;
   else                         mv1 = 0;  
   
   if      ( fabs(idv2) == 11 ) mv2 = me   ;
   else if ( fabs(idv2) == 13 ) mv2 = mmu  ;
   else if ( fabs(idv2) == 15 ) mv2 = mtau ;
   else                         mv2 = 0;  
   

   l1.SetPtEtaPhiM(ptl1,etal1,phil1,ml1);
   l2.SetPtEtaPhiM(ptl2,etal2,phil2,ml2);
   v1.SetPtEtaPhiM(ptv1,etav1,phiv1,mv1);
   v2.SetPtEtaPhiM(ptv2,etav2,phiv2,mv2);
   
   TLorentzVector V1 = l1+v1; // V1
   TLorentzVector V2 = l2+v2; // V2
   TLorentzVector VV = V1+V2;
   

   
   TLorentzVector VV_t(VV.X(),VV.Y(),VV.Z(),VV.T()); //Need TLorentzVectors for several methods (boosts)
   TLorentzVector V1_t(V1.X(),V1.Y(),V1.Z(),V1.T());
   TLorentzVector V2_t(V2.X(),V2.Y(),V2.Z(),V2.T());
   
   double s_hat = pow(VV.M(),2); // s_hat = center-of-mass energy of 2 vector boson system
   
   //Boost quarks and V1
   TLorentzVector V1_b = V1_t;
   TLorentzVector p1_b, p2_b;
   double energy = 6500. ; //13 TeV in total
   p1_b.SetXYZT(0.,0.,x1*energy,x1*energy); //x1 = fraction of momentum taken by the particle initiating the hard process
   p2_b.SetXYZT(0.,0.,-x2*energy,x2*energy);
   V1_b.Boost( -VV_t.BoostVector()); //Inverse Lorentz transformation, to get to the center-of-mass frame
   p1_b.Boost( -VV_t.BoostVector());
   p2_b.Boost( -VV_t.BoostVector());
   
   
   
   
   //Unitary vectors
   TLorentzVector V1_b_u = V1_b*(1/V1_b.P()); //Normalized to 1
   TLorentzVector p1_b_u = p1_b*(1/p1_b.P());
   TLorentzVector p2_b_u = p2_b*(1/p2_b.P());
   
   //Effective beam axis
   TLorentzVector diff_p = p1_b_u - p2_b_u;
   TLorentzVector eff_beam_axis = diff_p*(1./diff_p.P());
   double cos_theta = eff_beam_axis.X()*V1_b_u.X() + eff_beam_axis.Y()*V1_b_u.Y() + eff_beam_axis.Z()*V1_b_u.Z();
   
   double m_z = 91.1876; //Z bosons assumed to be on-shell
   double m_w = 80.385;
   double t_hat = 0.;
   
   if(isZZ) t_hat = m_z*m_z - 0.5*s_hat + cos_theta * sqrt( 0.25*s_hat*s_hat - m_z*m_z*s_hat );
   if(isWZ){
     double b = 1./2./sqrt(s_hat) * sqrt(pow(s_hat-m_z*m_z-m_w*m_w,2) - 4*m_w*m_w*m_z*m_z);
     double a = sqrt(b*b + m_z*m_z);
     t_hat = m_z*m_z - sqrt(s_hat) * (a - b * cos_theta); //awful calculation, needed to put ourselves to the center-of-mass frame with the 2 particles having a different mass !
   }
   
   int quark_type = 0; //Flavour of incident quark
   quark_type = fabs(id1);
//    if(genIncomingQuarks.size() > 0) quark_type = fabs(genIncomingQuarks[0].pdgId()); //Works unless if gg->ZZ process : it shouldn't be the case as we're using POWHEG
   
   std::vector<float> Correction_vec = findCorrection( sqrt(s_hat), t_hat ); //Extract the corrections for the values of s and t computed
   
//    std::cout << " quark_type = " << quark_type;
   
   if (quark_type==1) kFactor = 1. + Correction_vec[1]; //d
   if (quark_type==2) kFactor = 1. + Correction_vec[0]; //u
   if (quark_type==3) kFactor = 1. + Correction_vec[1]; //s as d
   if (quark_type==4) kFactor = 1. + Correction_vec[0]; //c as u
   if (quark_type==5) kFactor = 1. + Correction_vec[2]; //b  //Notice that the quark types are irrelevant for the case of WZ (same numbers in the last 3 columns -- see table).
   
//    std::cout << " kFactor = " << kFactor << std::endl;
   
   if (sqrt(s_hat)< 2*m_z     && isZZ) kFactor = 1.; //Off-shell cases, not corrected to avoid non-defined values for t.
   if (sqrt(s_hat)< m_z + m_w && isWZ) kFactor = 1.;
   
//    std::cout << " s_hat = " << s_hat << " :: kFactor = " << kFactor << std::endl;
   
   //Computing the associated error:
   //Warning, several methods could be used.
   //In Run 1, CMS used (kFactor-1)*(kFactor_QCD -1) for all rho
   //And ATLAS used : 0 for rho < 0.3 and 1 for rho >0.3
   //
   //Here is an implementation that is using a mix of the two. It may change in the future (but the change won't be critical)
   double kFactor_QCD = 1.;
   if (isZZ)             kFactor_QCD = 15.99/9.89; //From arXiv1105.0020
   if (isWZ && idl1 > 0) kFactor_QCD = 28.55/15.51; //for W+Z
   if (isWZ && idl1 < 0) kFactor_QCD = 18.19/9.53; //for W-Z
   
   
   //Definition of rho
   double rho = 0.;
   if(isZZ){
     double rho = (l1 + l2 + v1 + v2).Pt();
     rho = rho/(l1.Pt() + l2.Pt() + v1.Pt() + v2.Pt());
   }
   if(isWZ){
     double rho = (l1 + l2 + v1 + v2).Pt();
     rho = rho/(l1.Pt() + l2.Pt() + v1.Pt() + v2.Pt());
   }
   
   float ewkCorrections_error = 0;
   
   if ( rho<0.3 ) ewkCorrections_error = fabs ((kFactor-1)*(kFactor_QCD -1));
   else           ewkCorrections_error = fabs (1-kFactor);
   
   //At this point, we have the relative error on the delta_ewk ( = k_ewk -1 )
   //Let's - instead - return the absolute error on k: we do delta_ewk* the_relative_errir_on_it. This gives absolute error on delta, and so on k
   ewkCorrections_error = fabs (ewkCorrections_error*kFactor);
   
   //For WZ, contribution from gamma-induced processes
   double gamma_induced_uncertainty = 0.;
   if(isWZ){
     //We multiply the kFactor from virtual processes (computed above) with the one from gamma-induced processes (based on a fit form a separate study)
     if (idl1 > 0) kFactor = kFactor*(1 + 0.00559445 - 5.17082e-6 * sqrt(s_hat) + 3.63331e-8 * s_hat); //W+Z
     if (idl1 < 0) kFactor = kFactor*(1 + 0.00174737 + 1.70668e-5 * sqrt(s_hat) + 2.26398e-8 * s_hat); //W-Z
     //IMPORTANT NOTICE: these numbers are dependent on the vector boson cuts of the analysis. These should not be used directly (need to perform the computation of the gamma-induced part first).
     
     //Uncertainty due to WZ gamma-induced contribution is set to 0 with a very good approximation (less than 0.1%) when using the LUXqed photon PDF (instead of NNPDF23)
     if (idl1 > 0) gamma_induced_uncertainty = 0.;
     if (idl1 < 0) gamma_induced_uncertainty = 0.;
     ewkCorrections_error = sqrt(pow(ewkCorrections_error,2) + pow(gamma_induced_uncertainty,2));
   }
   
   
   std::vector <float> value_and_error;
   value_and_error.push_back(kFactor);
   value_and_error.push_back(ewkCorrections_error);
   
   return value_and_error; 

}
   
   
   
   
   
