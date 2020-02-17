#include <math.h>
#include <ZZMatrixElement/MELA/interface/Mela.h>

std::vector<float> melaHiggsEFT(Mela *_mela, TVar::MatrixElement ME, TVar::Production Prod, bool useConstant){

  std::vector<float> mes;

  bool IsGG = 0;
  if(Prod==TVar::ZZGG || Prod==TVar::JJQCD)IsGG = 1;

  bool Decay = 0;
  if(Prod==TVar::ZZGG)Decay = 1;

  float me_hsm = -999;
  _mela->setProcess(TVar::HSMHiggs, ME, Prod);
  if(Decay)_mela->computeP(me_hsm, useConstant); 
  else     _mela->computeProdP(me_hsm, useConstant); 
  mes.push_back(me_hsm);

  float me_hm = -999;
  _mela->setProcess(TVar::H0minus, ME, Prod);
  if(Decay)_mela->computeP(me_hm, useConstant);
  else     _mela->computeProdP(me_hm, useConstant);
  mes.push_back(me_hm);

  float me_hp = -999;
  _mela->setProcess(TVar::H0hplus, ME, Prod);
  if(Decay)_mela->computeP(me_hp, useConstant);
  else     _mela->computeProdP(me_hp, useConstant);
  mes.push_back(me_hp);

  float me_hl = -999;
  _mela->setProcess(TVar::H0_g1prime2, ME, Prod);
  if(Decay)_mela->computeP(me_hl, useConstant);
  else     _mela->computeProdP(me_hl, useConstant);
  mes.push_back(me_hl);

  float me_mixhm = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0] = 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = 1.;    
  if(IsGG) _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;        
  if(Decay)_mela->computeP(me_mixhm , useConstant);
  else     _mela->computeProdP(me_mixhm , useConstant);
  mes.push_back(me_mixhm);

  float me_mixhp = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]=1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]=1.;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                                                
  if(Decay) _mela->computeP(me_mixhp, useConstant);
  else      _mela->computeProdP(me_mixhp, useConstant);
  mes.push_back(me_mixhp);
 
  return mes;

}


