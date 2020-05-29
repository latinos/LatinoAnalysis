
#include <math.h>
#include <ZZMatrixElement/MELA/interface/Mela.h>

std::vector<float> melaHiggsEFT(Mela *_mela, TVar::MatrixElement ME, TVar::Production Prod, bool IsGG, bool IsReco){

  std::vector<float> mes;

  bool Decay = 0;

  if(Prod==TVar::ZZGG || Prod==TVar::ZZINDEPENDENT)Decay = 1;

  float me_hsm = -999;
  _mela->setProcess(TVar::HSMHiggs, ME, Prod);
  if(Decay)_mela->computeP(me_hsm, IsReco); 
  else     _mela->computeProdP(me_hsm, IsReco); 
  mes.push_back(me_hsm);

  float me_hm = -999;
  _mela->setProcess(TVar::H0minus, ME, Prod);
  if(Decay)_mela->computeP(me_hm, IsReco);
  else     _mela->computeProdP(me_hm, IsReco);
  mes.push_back(me_hm);

  float me_hp = -999;
  _mela->setProcess(TVar::H0hplus, ME, Prod);
  if(Decay)_mela->computeP(me_hp, IsReco);
  else     _mela->computeProdP(me_hp, IsReco);
  mes.push_back(me_hp);

  float me_hl = -999;
  _mela->setProcess(TVar::H0_g1prime2, ME, Prod);
  if(Decay)_mela->computeP(me_hl, IsReco);
  else     _mela->computeProdP(me_hl, IsReco);
  mes.push_back(me_hl);

  float me_mixhm = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.;    
  if(IsGG) _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;        
  if(Decay)_mela->computeP(me_mixhm , IsReco);
  else     _mela->computeProdP(me_mixhm , IsReco);
  mes.push_back(me_mixhm);

  float me_mixhp = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= 1.;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                    
  if(Decay) _mela->computeP(me_mixhp, IsReco);
  else      _mela->computeProdP(me_mixhp, IsReco);
  mes.push_back(me_mixhp);

  float me_mixhl = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1_PRIME2][0]= 1.;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                         
  if(Decay) _mela->computeP(me_mixhl, IsReco);
  else      _mela->computeProdP(me_mixhl, IsReco); 
  mes.push_back(me_mixhl);

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

   mes.push_back(PjjSmeared); 
   mes.push_back(PjjTrue);
   mes.push_back(avgME); 
  }

  return mes;

}


