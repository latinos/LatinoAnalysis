
#include <math.h>
#include <JHUGenMELA/MELA/interface/Mela.h>

#include <cstdio>
#include <cmath>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <map>

std::map<TString, float> melaHiggsEFT(Mela *_mela, TVar::MatrixElement ME, TVar::Production Prod, bool IsGG, bool IsReco){

  std::map<TString, float> mes; 

  bool Decay = 0;
  bool IsGGjj = 0;

  if(Prod==TVar::ZZGG || Prod==TVar::ZZINDEPENDENT)Decay = 1;
  if(Prod==TVar::JJQCD) IsGGjj = 1;

  float me_hsm = -999;
  _mela->setProcess(TVar::HSMHiggs, ME, Prod);
  if(Decay)_mela->computeP(me_hsm, IsReco); 
  else     _mela->computeProdP(me_hsm, IsReco); 

  float me_hm = -999;
  _mela->setProcess(TVar::H0minus, ME, Prod);
  if(Decay)_mela->computeP(me_hm, IsReco);
  else     _mela->computeProdP(me_hm, IsReco);

  float me_hp = -999;
  _mela->setProcess(TVar::H0hplus, ME, Prod);
  if(Decay)_mela->computeP(me_hp, IsReco);
  else     _mela->computeProdP(me_hp, IsReco);

  float me_hl = -999;
  _mela->setProcess(TVar::H0_g1prime2, ME, Prod);
  if(Decay)_mela->computeP(me_hl, IsReco);
  else     _mela->computeProdP(me_hl, IsReco);

  float me_hlzg = -999;   
  _mela->setProcess(TVar::H0_Zgsg1prime2, ME, Prod);
  if(Decay)_mela->computeP(me_hlzg, IsReco);
  else     _mela->computeProdP(me_hlzg, IsReco);

  float me_mixhm = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.;   
  if(IsGGjj)_mela->selfDHggcoupl[0][gHIGGS_GG_4][0]=1;    
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;      
  if(Decay) _mela->computeP(me_mixhm , IsReco);
  else      _mela->computeProdP(me_mixhm , IsReco);

  float me_mixhp = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                 
  if(Decay) _mela->computeP(me_mixhp, IsReco);
  else      _mela->computeProdP(me_mixhp, IsReco);

  float me_mixhl = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;
  if(Decay) _mela->computeP(me_mixhl, IsReco);
  else      _mela->computeProdP(me_mixhl, IsReco); 

  float me_mixhlzg = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]=1;
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;
  if(Decay) _mela->computeP(me_mixhlzg, IsReco);
  else      _mela->computeProdP(me_mixhlzg, IsReco); 

  mes.insert({"me_hsm",     me_hsm});
  mes.insert({"me_hm",      me_hm});
  mes.insert({"me_hp",      me_hp});
  mes.insert({"me_hl",      me_hl});
  mes.insert({"me_hlzg",    me_hlzg});
  mes.insert({"me_mixhm",   me_mixhm});
  mes.insert({"me_mixhp",   me_mixhp});
  mes.insert({"me_mixhl",   me_mixhl});
  mes.insert({"me_mixhlzg", me_mixhlzg});

  /////// VH corrections //////
  // replace the true BW V shape with a parameterized one more suitable for smearing effects on jets.
  // Average ME constant for int KDs, depends on mH

  if((Prod==TVar::Had_WH || Prod==TVar::Had_ZH) && IsReco){

   float PjjSmeared = -999;
   float PjjTrue    = -999;
   float avgME      = -999;

   _mela->setProcess(TVar::HSMHiggs, ME, Prod);
   _mela->computeDijetConvBW(PjjSmeared, false);
   _mela->computeDijetConvBW(PjjTrue, true);
   _mela->computeProdP(avgME, IsReco); 
   _mela->getConstant(avgME); // call after computeProdP

   mes.insert({"PjjSmeared", PjjSmeared});
   mes.insert({"PjjTrue",    PjjTrue});
   mes.insert({"avgME",      avgME});
  
  }

  ///// MEs for SMEFT interpretation /////

  if(IsReco==0){  

   float cw  = 0.8768;
   float sw  = 0.4808;
   float mZ  = 91.2;
   float LambdaQ = 100.0;

   // L1ZZ (g1prime2) = 0, g2 = 1
   float g2_eft_L1WW = -2*sw*sw*LambdaQ*LambdaQ/(mZ*mZ*(cw*cw-sw*sw));
   float g2_eft_L1Zg = -2*cw*sw*LambdaQ*LambdaQ/(mZ*mZ*(cw*cw-sw*sw));
   // L1ZZ (g1prime2) = 1, g2 = 0
   float L1ZZ_eft_L1WW = 1/(cw*cw-sw*sw);
   float L1ZZ_eft_L1Zg = 2*cw*sw/(cw*cw-sw*sw); 

   float me_eft_hm = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_4][0] = cw*cw; 
   if(IsGGjj)_mela->selfDHggcoupl[0][gHIGGS_GG_4][0]=1;    
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;      
   if(Decay) _mela->computeP(me_eft_hm , IsReco);
   else      _mela->computeProdP(me_eft_hm , IsReco);

   float me_eft_hp = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_2][0]= cw*cw;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= g2_eft_L1WW;  
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= g2_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                 
   if(Decay) _mela->computeP(me_eft_hp, IsReco);
   else      _mela->computeProdP(me_eft_hp, IsReco);

   float me_eft_hl = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1;   
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= L1ZZ_eft_L1WW;   
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= L1ZZ_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;
   if(Decay) _mela->computeP(me_eft_hl, IsReco);
   else      _mela->computeProdP(me_eft_hl, IsReco); 

   float me_eft_mixhm = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_4][0] = cw*cw; 
   if(IsGGjj)_mela->selfDHggcoupl[0][gHIGGS_GG_4][0]=1;    
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;      
   if(Decay) _mela->computeP(me_eft_mixhm , IsReco);
   else      _mela->computeProdP(me_eft_mixhm , IsReco);

   float me_eft_mixhp = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_2][0]= cw*cw;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= g2_eft_L1WW;  
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= g2_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                 
   if(Decay) _mela->computeP(me_eft_mixhp, IsReco);
   else      _mela->computeProdP(me_eft_mixhp, IsReco);

   float me_eft_mixhl = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1][0] = 1.; 
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1;   
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= L1ZZ_eft_L1WW;   
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= L1ZZ_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;
   if(Decay) _mela->computeP(me_eft_mixhl, IsReco);
   else      _mela->computeProdP(me_eft_mixhl, IsReco); 


   float me_eft_mixpm = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_2][0]= cw*cw;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= g2_eft_L1WW;  
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= g2_eft_L1Zg;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_4][0] = cw*cw; 
   if(IsGGjj)_mela->selfDHggcoupl[0][gHIGGS_GG_4][0]=1;    
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;      
   if(Decay) _mela->computeP(me_eft_mixpm , IsReco);
   else      _mela->computeProdP(me_eft_mixpm , IsReco);

   float me_eft_mixpl = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1;   
   _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_2][0]= cw*cw;  
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= L1ZZ_eft_L1WW + g2_eft_L1WW;  
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= L1ZZ_eft_L1Zg + g2_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                 
   if(Decay) _mela->computeP(me_eft_mixpl, IsReco);
   else      _mela->computeProdP(me_eft_mixpl, IsReco);

   float me_eft_mixml = -999;
   _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
   _mela->differentiate_HWW_HZZ=true;
   _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.; 
   _mela->selfDHwwcoupl[0][gHIGGS_VV_4][0] = cw*cw; 
   _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1;   
   _mela->selfDHwwcoupl[0][gHIGGS_VV_1_PRIME2][0]= L1ZZ_eft_L1WW;   
   _mela->selfDHzzcoupl[0][gHIGGS_ZA_1_PRIME2][0]= L1ZZ_eft_L1Zg;
   if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;
   if(Decay) _mela->computeP(me_eft_mixml, IsReco);
   else      _mela->computeProdP(me_eft_mixml, IsReco); 

   mes.insert({"me_eft_hm",    me_eft_hm});
   mes.insert({"me_eft_hp",    me_eft_hp});
   mes.insert({"me_eft_hl",    me_eft_hl});
   mes.insert({"me_eft_mixhm", me_eft_mixhm});
   mes.insert({"me_eft_mixhp", me_eft_mixhp});
   mes.insert({"me_eft_mixhl", me_eft_mixhl});
   mes.insert({"me_eft_mixpm", me_eft_mixpm});
   mes.insert({"me_eft_mixpl", me_eft_mixpl});
   mes.insert({"me_eft_mixml", me_eft_mixml});
  
  }

  return mes;

}


