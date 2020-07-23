// Authors:
//    - Claudia Bertella
//    - Yacine Haddad
//
// email:  yhaddad@cern.ch

// Updates 25-03-2020:
// - adding EKW corrections
// Updated 05-06-2020:
// - Adding s-channel contribution using HJets
// - Updating acceptances for POWHEG

#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cmath>

// need to include the definitions of the STXS bins, this can be found
// the HXSWG gitlab respository:
// https://gitlab.cern.ch/LHCHIGGSXS/LHCHXSWG2/STXS/blob/master/HiggsTemplateCrossSections.h

// the following tools have been used
// proVBF  : Phys.Rev.Lett. 117 (2016) no.7, 072001 [arXiv:1606.00840]
// HJets   : Phys.Rev.Lett. 111 (2013) 211802 [arXiv:1308.2932]
// Pythia8 : JHEP05 (2006) 026, Comput. Phys. Comm. 178 (2008) 852. [arXiv:0710.3820]
// Herwig7 : Eur.Phys.J. C76 (2016) no.4, 196 [arXiv:1512.01178]
// POWHEG VBFH: JHEP 1002 (2010) 037 [arXiv:0911.5299] 

// bin acceptances extracted from POWHEG VBFH (NLO)
static std::map<int, std::vector<double> > stxs_acc_powheg = {
  //stxs   total     ptH_200 mjj_60   mjj_120  mjj_350  mjj_700   mjj_1000  mjj_1500   ptHjj_25    njets_30_2
   { 200 , {0.0668,  0.0000, 0.0000,  0.0000,  0.0000,  0.0000,   0.0000,   0.0000,    0.0000,     0.0000}}, 
   { 201 , {0.0765,  0.0000, 0.0000,  0.0000,  0.0000,  0.0000,   0.0000,   0.0000,    0.0000,    -0.1821}},
   { 202 , {0.3435,  0.0000, 0.0000,  0.0000,  0.0000,  0.0000,   0.0000,   0.0000,    0.0000,    -0.8179}},
   { 203 , {0.0048,  0.0000,-0.3761,  0.0000,  0.0000,  0.0000,   0.0000,   0.0000,   -0.0126,     0.0093}},
   { 204 , {0.0096,  0.0000, 0.0192, -0.4400,  0.0000,  0.0000,   0.0000,   0.0000,   -0.0253,     0.0187}},
   { 205 , {0.0782,  0.0000, 0.1564,  0.1635, -0.6859,  0.0000,   0.0000,   0.0000,   -0.2056,     0.1525}},
   { 206 , {0.0079,  0.0000,-0.6239,  0.0000,  0.0000,  0.0000,   0.0000,   0.0000,    0.0599,     0.0155}},
   { 207 , {0.0122,  0.0000, 0.0245, -0.5600,  0.0000,  0.0000,   0.0000,   0.0000,    0.0923,     0.0239}},
   { 208 , {0.0358,  0.0000, 0.0716,  0.0749, -0.3141,  0.0000,   0.0000,   0.0000,    0.2701,     0.0698}},
   { 209 , {0.1061, -0.3265, 0.2121,  0.2218,  0.2912, -0.7233,   0.0000,   0.0000,   -0.2789,     0.2068}},
   { 210 , {0.0306, -0.0940, 0.0611,  0.0639,  0.0838, -0.2083,   0.0000,   0.0000,    0.2304,     0.0595}},
   { 211 , {0.0545, -0.1678, 0.1090,  0.1140,  0.1497,  0.2505,  -0.7179,   0.0000,   -0.1434,     0.1063}},
   { 212 , {0.0136, -0.0417, 0.0271,  0.0283,  0.0372,  0.0623,  -0.1784,   0.0000,    0.1022,     0.0264}},
   { 213 , {0.0504, -0.1550, 0.1007,  0.1052,  0.1382,  0.2313,   0.3553,  -0.7105,   -0.1324,     0.0982}},
   { 214 , {0.0111, -0.0341, 0.0222,  0.0232,  0.0305,  0.0510,   0.0783,  -0.1566,    0.0837,     0.0216}},
   { 215 , {0.0507, -0.1560, 0.1013,  0.1060,  0.1391,  0.2328,   0.3576,   0.7154,   -0.1333,     0.0988}},
   { 216 , {0.0081, -0.0248, 0.0161,  0.0168,  0.0221,  0.0370,   0.0568,   0.1136,    0.0607,     0.0157}},
   { 217 , {0.0058,  0.1466, 0.0116,  0.0121,  0.0159, -0.0394,   0.0000,   0.0000,   -0.0152,     0.0113}},
   { 218 , {0.0042,  0.1076, 0.0085,  0.0089,  0.0117, -0.0290,   0.0000,   0.0000,    0.0320,     0.0083}},
   { 219 , {0.0050,  0.1273, 0.0100,  0.0105,  0.0138,  0.0231,  -0.0661,   0.0000,   -0.0132,     0.0098}},
   { 220 , {0.0029,  0.0724, 0.0057,  0.0060,  0.0078,  0.0131,  -0.0376,   0.0000,    0.0215,     0.0056}},
   { 221 , {0.0064,  0.1628, 0.0128,  0.0134,  0.0176,  0.0295,   0.0453,  -0.0906,   -0.0169,     0.0125}},
   { 222 , {0.0030,  0.0763, 0.0060,  0.0063,  0.0083,  0.0138,   0.0212,  -0.0424,    0.0227,     0.0059}},
   { 223 , {0.0089,  0.2249, 0.0177,  0.0185,  0.0243,  0.0408,   0.0626,   0.1252,   -0.0233,     0.0173}},
   { 224 , {0.0032,  0.0821, 0.0065,  0.0068,  0.0089,  0.0149,   0.0229,   0.0457,    0.0244,     0.0063}}
};

// acceptances for VBH+VHHad: extracted from NJets (NLO) + H7
// it includes the full H+2Jets EWK calculation
static std::map<int, std::vector<double> > stxs_acc =
{ //stxs  tot     ptH200  mjj60   mjj120  mjj350  mjj700  mjj1000 mjj1500 ptHjj25 jet2
  { 200, {0.083 , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0    }}, // FWD 
  { 201, {0.0735, 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   ,-0.1762 }}, // Jet0
  { 202, {0.3438, 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0   ,-0.8238 }}, // Jet1
  { 203, {0.0082, 0.0   ,-0.4038, 0.0   , 0.0   , 0.0   , 0.0   , 0.0   ,-0.0256, 0.0164 }}, // Mjj 0-60,      PTHjj 0-25
  { 204, {0.0603, 0.0   , 0.1258,-0.5825, 0.0   , 0.0   , 0.0   , 0.0   ,-0.1876, 0.1206 }}, // Mjj 60-120,    PTHjj 0-25
  { 205, {0.0608, 0.0   , 0.1268, 0.1617,-0.5332, 0.0   , 0.0   , 0.0   ,-0.1891, 0.1216 }}, // Mjj 120-350,   PTHjj 0-25
  { 206, {0.0121, 0.0   ,-0.5962, 0.0   , 0.0   , 0.0   , 0.0   , 0.0   , 0.0681, 0.0243 }}, // Mjj 350-700,   PTHjj 0-25    , pTH 0-200
  { 207, {0.0432, 0.0   , 0.0901,-0.4175, 0.0   , 0.0   , 0.0   , 0.0   , 0.2423, 0.0865 }}, // Mjj 700-1000,  PTHjj 0-25    , pTH 0-200
  { 208, {0.0532, 0.0   , 0.111 , 0.1416,-0.4668, 0.0   , 0.0   , 0.0   , 0.2986, 0.1065 }}, // Mjj 1000-1500, PTHjj 0-25    , pTH 0-200
  { 209, {0.0702,-0.3026, 0.1465, 0.1868, 0.2682,-0.6504, 0.0   , 0.0   ,-0.2185, 0.1405 }}, // Mjj 1500-inf , PTHjj 0-25    , pTH 0-200
  { 210, {0.0289,-0.1247, 0.0604, 0.077 , 0.1105,-0.2681, 0.0   , 0.0   , 0.1624, 0.0579 }}, // Mjj 350-700,   PTHjj 0-25    , pTH 200-inf
  { 211, {0.0366,-0.1576, 0.0763, 0.0973, 0.1397, 0.2377,-0.6724, 0.0   ,-0.1138, 0.0732 }}, // Mjj 700-1000,  PTHjj 0-25    , pTH 200-inf
  { 212, {0.0118,-0.0509, 0.0246, 0.0314, 0.0451, 0.0767,-0.217 , 0.0   , 0.0662, 0.0236 }}, // Mjj 1000-1500, PTHjj 0-25    , pTH 200-inf
  { 213, {0.0335,-0.1445, 0.07  , 0.0892, 0.1281, 0.218 , 0.3371,-0.6777,-0.1043, 0.0671 }}, // Mjj 1500-inf , PTHjj 0-25    , pTH 200-inf
  { 214, {0.0093,-0.04  , 0.0193, 0.0247, 0.0354, 0.0603, 0.0932,-0.1874, 0.052 , 0.0186 }}, // Mjj 0-60,      PTHjj 25-inf
  { 215, {0.0348,-0.1498, 0.0725, 0.0925, 0.1328, 0.226 , 0.3495, 0.6955,-0.1082, 0.0696 }}, // Mjj 60-120,    PTHjj 25-inf
  { 216, {0.0069,-0.0298, 0.0144, 0.0184, 0.0264, 0.045 , 0.0695, 0.1384, 0.0388, 0.0138 }}, // Mjj 120-350,   PTHjj 25-inf
  { 217, {0.004 , 0.1332, 0.0083, 0.0106, 0.0152,-0.0368, 0.0   , 0.0   ,-0.0123, 0.0079 }}, // Mjj 350-700,   PTHjj 25-inf  , pTH 0-200
  { 218, {0.0048, 0.1623, 0.0101, 0.0129, 0.0185,-0.0448, 0.0   , 0.0   , 0.0271, 0.0097 }}, // Mjj 700-1000,  PTHjj 25-inf  , pTH 0-200
  { 219, {0.0033, 0.1118, 0.0069, 0.0089, 0.0127, 0.0216,-0.0612, 0.0   ,-0.0104, 0.0067 }}, // Mjj 1000-1500, PTHjj 25-inf  , pTH 0-200
  { 220, {0.0027, 0.0901, 0.0056, 0.0071, 0.0103, 0.0175,-0.0494, 0.0   , 0.0151, 0.0054 }}, // Mjj 1500-inf , PTHjj 25-inf  , pTH 0-200
  { 221, {0.0041, 0.1361, 0.0085, 0.0108, 0.0155, 0.0264, 0.0408,-0.082 ,-0.0126, 0.0081 }}, // Mjj 350-700,   PTHjj 25-inf  , pTH 200-inf
  { 222, {0.0026, 0.0879, 0.0055, 0.007 , 0.01  , 0.017 , 0.0263,-0.0529, 0.0147, 0.0052 }}, // Mjj 700-1000,  PTHjj 25-inf  , pTH 200-inf
  { 223, {0.0057, 0.19  , 0.0118, 0.0151, 0.0216, 0.0368, 0.0569, 0.1133,-0.0176, 0.0113 }}, // Mjj 1000-1500, PTHjj 25-inf  , pTH 200-inf
  { 224, {0.0026, 0.0886, 0.0055, 0.007 , 0.0101, 0.0172, 0.0265, 0.0528, 0.0148, 0.0053 }}  // Mjj 1500-inf , PTHjj 25-inf  , pTH 200-inf
};

// uncertainty sources
// 10 nuissances:  1 x yield, 1 x 3rd jet veto, 6 x Mjj cuts, 1 x 01->2 jetBin, 1 x PTH cut
// +---------------+---------+------------+-----------+--------+
// |     source    | FO NNLO | POWHEG NLO | HJets NLO | MIXED  |
// +---------------+---------+------------+-----------+--------+
// |   Delta_tot   |  14.972 |   15.131   |   21.539  | 21.539 |
// |   Delta_200   |  0.622  |   1.081    |   2.989   | 0.622  |
// |  Delta_Mjj60  |  8.057  |   9.511    |   8.003   | 8.003  |
// |  Delta_Mjj120 |   6.84  |   8.286    |   13.446  | 13.446 |
// |  Delta_Mjj350 |  7.389  |   5.025    |   5.385   | 7.389  |
// |  Delta_Mjj700 |  4.201  |   5.973    |   8.158   | 4.201  |
// | Delta_Mjj1000 |  3.115  |   3.545    |   7.045   | 3.115  |
// | Delta_Mjj1500 |  1.764  |   2.614    |   6.404   | 1.764  |
// |    Delta_25   |  27.387 |   2.674    |   35.46   | 27.387 |
// |   Delta_2jet  |  17.355 |   18.617   |   33.412  | 33.412 |
// +---------------+---------+------------+-----------+--------+
// std::vector<double> uncert_deltas({14.972, 0.622, 8.057,  6.84 , 7.389, 4.201, 3.115, 1.764, 27.387, 17.355}); 
// std::vector<double> uncert_deltas({15.131, 1.081, 9.511,  8.286, 5.025, 5.973, 3.545, 2.614,  2.674, 18.617}); 
// std::vector<double> uncert_deltas({21.539, 2.989, 8.003, 13.446, 5.385, 8.158, 7.045, 6.404, 35.46 , 33.412}); 
std::vector<double> uncert_deltas(   {21.539, 0.622, 8.003, 13.446, 7.389, 4.201, 3.115, 1.764, 27.387, 33.412});

// cross sections from different STXS bins
// prediction at NLO from POWEHG VBFH + PYTHIA8(dipoleShower=on)
std::map<int, double> powheg_xsec
{{ 200 ,  266.189 },
 { 201 ,  304.633 },
 { 202 , 1367.880 },
 { 203 ,   19.075 },
 { 204 ,   38.297 },
 { 205 ,  311.537 },
 { 206 ,   31.645 },
 { 207 ,   48.747 },
 { 208 ,  142.674 },
 { 209 ,  422.566 },
 { 210 ,  121.669 },
 { 211 ,  217.211 },
 { 212 ,   53.993 },
 { 213 ,  200.550 },
 { 214 ,   44.194 },
 { 215 ,  201.893 },
 { 216 ,   32.064 },
 { 217 ,   23.041 },
 { 218 ,   16.914 },
 { 219 ,   19.998 },
 { 220 ,   11.374 },
 { 221 ,   25.580 },
 { 222 ,   11.982 },
 { 223 ,   35.338 },
 { 224 ,   12.906 }};

// cross sections from different STXS bins
// prediction at NLO from HJets + POWHEG 7
std::map<int, double> hjets_xsec
{{ 200 ,  470.616 },
 { 201 ,  416.752 },
 { 202 , 1948.572 },
 { 203 ,   46.574 },
 { 204 ,  341.685 },
 { 205 ,  344.551 },
 { 206 ,   68.774 },
 { 207 ,  244.861 },
 { 208 ,  301.698 },
 { 209 ,  398.061 },
 { 210 ,  164.063 },
 { 211 ,  207.287 },
 { 212 ,   66.900 },
 { 213 ,  190.095 },
 { 214 ,   52.562 },
 { 215 ,  197.090 },
 { 216 ,   39.209 },
 { 217 ,   22.498 },
 { 218 ,   27.417 },
 { 219 ,   18.880 },
 { 220 ,   15.220 },
 { 221 ,   22.996 },
 { 222 ,   14.850 },
 { 223 ,   32.095 },
 { 224 ,   14.967 }};


// EWcorr : (1 + DeltaEW) correction factor to mutiply by the cross section
// SigPho : Incoming photon contribution 
// DeltaEW: is the yellow report definition for EW errors
std::map<int, std::vector<double> > EW_correction {
//stxs, LO    , EWcorr, SigPho,DeltaEW 
  {200,{  1.000,  1.000,  0.000,  0.000}},
  {201,{  0.000,  1.000,  0.000,  0.000}},
  {202,{  0.000,  1.000,  0.000,  0.000}},
  {203,{  6.670,  0.981,  0.081,  0.012}}, //   0 < m_jj < 60
  {214,{  6.670,  0.981,  0.081,  0.012}}, //   0 < m_jj < 60
  {204,{ 601.78,  0.938,  7.440,  0.012}}, //  60 < m_jj < 120
  {215,{ 601.78,  0.938,  7.440,  0.012}}, //  60 < m_jj < 120
  {205,{ 540.59,  0.981,  6.567,  0.012}}, // 120 < m_jj < 350
  {216,{ 540.59,  0.981,  6.567,  0.012}}, // 120 < m_jj < 350
  // pTH < 200
  {206,{ 659.75,  0.955,  9.056,  0.014}}, // 350 < m_jj < 700
  {217,{ 659.75,  0.955,  9.056,  0.014}}, // 350 < m_jj < 700
  {207,{ 318.83,  0.937,  4.820,  0.015}}, // 700 < m_jj < 1000
  {218,{ 318.83,  0.937,  4.820,  0.015}}, // 700 < m_jj < 1000
  {208,{ 275.94,  0.921,  4.481,  0.016}}, //1000 < m_jj < 1500
  {219,{ 275.94,  0.921,  4.481,  0.016}}, //1000 < m_jj < 1500
  {209,{ 251.33,  0.899,  4.798,  0.019}}, //       m_jj > 1500
  {220,{ 251.33,  0.899,  4.798,  0.019}}, //       m_jj > 1500
  // pTH > 200
  {210,{  45.72,  0.927,  0.807,  0.018}}, // 350 < m_jj < 700
  {221,{  45.72,  0.927,  0.807,  0.018}}, // 350 < m_jj < 700
  {211,{  37.91,  0.907,  0.647,  0.017}}, // 700 < m_jj < 1000
  {222,{  37.91,  0.907,  0.647,  0.017}}, // 700 < m_jj < 1000
  {212,{  44.03,  0.883,  0.765,  0.017}}, //1000 < m_jj < 1500
  {223,{  44.03,  0.883,  0.765,  0.017}}, //1000 < m_jj < 1500
  {213,{  55.99,  0.851,  1.165,  0.022}}, //       m_jj > 1500 
  {224,{  55.99,  0.851,  1.165,  0.022}}, //       m_jj > 1500
};

double vbf_ew_correction_stage_1_1(int event_STXS, bool with_imc_photon=false){
  // protection to run on other STXS bins
  if (event_STXS < 200 || event_STXS > 224) return 0.0;
  double corr = stxs_acc[event_STXS][1];
  if(with_imc_photon){
    corr *= 1.0 + (stxs_acc[event_STXS][2] / hjets_xsec[event_STXS]);
  }
  return corr;
}


// Propagation function
double vbf_uncert_stage_1_1(int source, int event_STXS, double Nsigma=1.0){
  // protection to run on other STXS bins
  if (event_STXS < 200 || event_STXS > 224) return 1.0;// protection to run on other STXS bins
  // return a single weight for a given souce
  if(source < 10){
    double delta_var = stxs_acc[event_STXS][source] * uncert_deltas[source];
    return  1.0 + Nsigma * (delta_var/hjets_xsec[event_STXS]);
  }else{
    return 0.0;
  }
};

// -------------------
// for printing only
// -------------------

// print EW corrections 
void print_ew_corr(){
  std::cout << " ======================================================== " << std::endl;
  std::cout << " === Electroweak corrections extracted from HAWK 3.0  === " << std::endl;
  std::cout << " BIN: "         << std::setw(8)
            << " (1 + D_ew) | " << std::setw(8)
            << " (1 + D_ph) | " << std::setw(8)
            << " Uncert     "   << std::endl;
  for (auto& bin : hjets_xsec) {
    std::cout <<" "<< bin.first << ": ";
    for (int s=0; s < 4; s++)
      std::cout << std::setw(8) << std::setprecision(5) << EW_correction[bin.first][s] << " | ";
    std::cout<< "" << std::endl;
  }
}

// print big table
void print_bigtable(bool relative=true){
  std::cout << " ======================================================== " << std::endl;
  if (relative)
    std::cout << " === relative uncertainties [%] " << std::endl;
  else
    std::cout << " === absolute uncertainties [fb] " << std::endl;

  std::cout << " BIN: "    << std::setw(8)
            << "Yield    | "  << std::setw(8)
            << "PTH200   | "  << std::setw(8)
            << "Mjj60    | "  << std::setw(8)
            << "Mjj120   | "  << std::setw(8)
            << "Mjj350   | "  << std::setw(8)
            << "Mjj700   | "  << std::setw(8)
            << "Mjj1000  | "  << std::setw(8)
            << "Mjj1500  | "  << std::setw(8)
            << "PTH25    | "  << std::setw(8)
            << "JET01    | "  << std::setw(8)
            << "TOT        "  << std::endl;
  for (auto& bin : hjets_xsec) {
    std::cout <<" "<< bin.first << ": ";
    double tot = 0;
    for (int s=0; s < 10; s++) {
      double uncert = 0;
      if (relative){
        uncert = vbf_uncert_stage_1_1(s, bin.first) - 1.0;
        std::cout << std::setw(8) << std::setprecision(5) << 100*uncert << " | ";
      }else{
        uncert = (vbf_uncert_stage_1_1(s, bin.first) - 1.0) * bin.second;
        std::cout << std::setw(8) << std::setprecision(4) << uncert << " | ";
      }
      tot += std::pow(uncert, 2);
    }
    if (relative)
      std::cout<< std::setw(8) << std::setprecision(5) << 100 * std::sqrt(tot) << std::endl;
    else
      std::cout<< std::setw(8) << std::setprecision(4) << std::sqrt(tot) << std::endl;
  }
  std::cout << " ======================================================== " << std::endl;
}

// correlation matrix
double _cov(int ibin, int jbin) {
  double cov_ij=0;
  for (int is=0; is < uncert_deltas.size(); ++is)
    cov_ij+=(vbf_uncert_stage_1_1(is,ibin)-1)*(vbf_uncert_stage_1_1(is,jbin)-1)*hjets_xsec[ibin]*hjets_xsec[jbin];
  return cov_ij;
}

// correlation matrix
double _corr(int ibin, int jbin) {
  if (ibin==jbin) return 1.0;
  return _cov(ibin,jbin)/sqrt(_cov(ibin,ibin)*_cov(jbin,jbin));
}
void print_corr(){
  std::cout << std::setw(8) << " --- ";
  for (auto& ibin: hjets_xsec){
    std::cout << std::setw(8) << ibin.first ;
  }
  std::cout << std::endl;
  std::cout << std::setw(8) << " --- ";
  for (auto& ibin: hjets_xsec){
    std::cout << std::setw(8) << "-----" ;
  }
  std::cout << std::endl;
  for (auto& ibin: hjets_xsec){
    std::cout << std::setw(8) << ibin.first;
    for (auto& jbin: hjets_xsec){
      std::cout << std::setw(8) << std::setprecision(2) << _corr(ibin.first, jbin.first) ;
    }
    std::cout << std::endl;
  }
}

std::vector<float> get_all_qqH_uncertainties(int event_STXS){
  std::vector<float> retval;
  for (int s=0; s < 10; s++) {
      double uncert = 0;
      retval.push_back(vbf_uncert_stage_1_1(s, event_STXS));
  }
  retval.push_back(1.+vbf_ew_correction_stage_1_1(event_STXS)); 
  return retval;
}

