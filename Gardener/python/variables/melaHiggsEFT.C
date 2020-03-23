#include <math.h>
#include <ZZMatrixElement/MELA/interface/Mela.h>

std::vector<float> melaHiggsEFT(Mela *_mela, TVar::MatrixElement ME, TVar::Production Prod, bool IsGG, bool IsReco){

  std::vector<float> mes;

  bool Decay = 0;
  double g2=1;
  double g4=1;

  if(Prod==TVar::ZZGG || Prod==TVar::ZZINDEPENDENT)Decay = 1;

  if(!IsReco){
   if(Decay==1){
    g2 = 1.133582;
    g4 = 1.76132;
   }else if(Prod==TVar::JJVBF){
    g2 = 0.27196538;
    g4 = 0.297979018705;
   }else if(Prod==TVar::Had_ZH || Prod==TVar::Lep_ZH){
    g2 = 0.112481;
    g4 = 0.144057;
   }else if(Prod==TVar::Had_WH || Prod==TVar::Lep_WH){
    g2 = 0.0998956;
    g4 = 0.1236136;
   }
  }

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
  _mela->selfDHzzcoupl[0][gHIGGS_VV_4][0] = g4;    
  if(IsGG) _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;        
  if(Decay)_mela->computeP(me_mixhm , IsReco);
  else     _mela->computeProdP(me_mixhm , IsReco);
  mes.push_back(me_mixhm);

  float me_mixhp = -999;
  _mela->setProcess(TVar::SelfDefine_spin0, ME, Prod);
  _mela->selfDHzzcoupl[0][gHIGGS_VV_1][0]= 1.;
  _mela->selfDHzzcoupl[0][gHIGGS_VV_2][0]= g2;   
  if(IsGG)  _mela->selfDHggcoupl[0][gHIGGS_GG_2][0]=1;                                                
  if(Decay) _mela->computeP(me_mixhp, IsReco);
  else      _mela->computeProdP(me_mixhp, IsReco);
  mes.push_back(me_mixhp);

  return mes;

}


