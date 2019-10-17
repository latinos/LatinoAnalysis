#include <TMath.h>
#include <TLorentzVector.h>
#define ZMASS 91.1876
#define PI 3.14159265359
#define zwwDefault -9999
// Phi ranges in [PI, PI)

class ZWW{
  public:
    //! constructor
    ZWW();
    virtual ~ZWW(){};
    
    //! reset and check
    void reset();
    void isLepOk();
    void isJetOk();
    void isMETOk();
    void isAllOk();

    //! setter
    void setLepton(std::vector<float> pt,
                   std::vector<float> eta,
                   std::vector<float> phi,
                   std::vector<float> flavor,
                   std::vector<float> charge,
                   std::vector<float> id);

    void setJet(std::vector<float> pt,
                std::vector<float> eta,
                std::vector<float> phi,
                std::vector<float> mass,
                std::vector<float> tag);

    void setMET(float met, float phi);

    //! functions
    bool  preSelection();
//    bool  selection();
    float pfmetPhi_zh4l();
    float zMass_zh4l(int zLepIdx_[2]);
    float zPt_zh4l(int zLepIdx_[2]);
    float z0Mass_zh4l();
    float z0Pt_zh4l();
    float z1Mass_zh4l();
    float z1Pt_zh4l();
    float zaMass_zh4l();
    float zbMass_zh4l();
    float flagZ1SF_zh4l();
    float zDeltaPhi_zh4l(int zLepIdx_[2]);
    float z0DeltaPhi_zh4l();
    float z1DeltaPhi_zh4l();
    float zaDeltaPhi_zh4l();
    float zbDeltaPhi_zh4l();
    float minDeltaPhi_zh4l();
    float zDeltaR_zh4l(int zLepIdx_[2]);
    float z0DeltaR_zh4l();
    float z1DeltaR_zh4l();
    float zaDeltaR_zh4l();
    float zbDeltaR_zh4l();
    float lepMt_zh4l(int iL);
    float lep1Mt_zh4l();
    float lep2Mt_zh4l();
    float lep3Mt_zh4l();
    float lep4Mt_zh4l();
    float minMt_zh4l();  
    float z1Mt_zh4l();
    float mllll_zh4l();
    float chllll_zh4l();
    float z1dPhi_lep1MET_zh4l();
    float z1dPhi_lep2MET_zh4l();
    float z1mindPhi_lepMET_zh4l();

  private:
    //! variables
        // constants and enum
    

        // For checker
    bool isAllOk_;
    bool isLepOk_;
    bool isJetOk_;
    bool isMETOk_;
    bool flagZ1SF_;

        // For setter
    std::vector<float> lepPt_;
    std::vector<float> lepEta_;
    std::vector<float> lepPhi_;
    std::vector<float> lepFl_;
    std::vector<float> lepCh_;
    std::vector<float> lepId_;
    std::vector<float> jetPt_;
    std::vector<float> jetEta_;
    std::vector<float> jetPhi_;
    std::vector<float> jetM_;
    std::vector<float> jetTag_;
    float met_;
    float metPhi_;
    float st_;
    float minDeltaPhi_;
    float minMt_;

    float minDeltaR_;///forVHNL

        // Buffer and buffer setter
    std::vector<TLorentzVector> lepVec_;
    std::vector<TLorentzVector> jetVec_;
    void setZ0LepIdx_();
    void setZ1LepIdx_();
    void setZaZbLepIdx_();
    int z0LepIdx_[2];
    int z1LepIdx_[2];
    int zaLepIdx_[2];
    int zbLepIdx_[2];
    TLorentzVector metVec_;
    int njet_;
    int nbjet_;

        // Output for public member fcns
    bool outPreSelection_;
};

//! constructor
ZWW::ZWW(){
    reset();
}

    // Reset all private to false/zwwDefault/null vector/etc.
void ZWW::reset(){
        // For checker
    isAllOk_ = false;
    isLepOk_ = false;
    isJetOk_ = false;
    isMETOk_ = false;

        // For setter
    lepPt_. clear();
    lepEta_.clear();
    lepPhi_.clear();
    lepFl_. clear();
    lepCh_. clear();
    lepId_. clear();
    jetPt_. clear();
    jetEta_.clear();
    jetPhi_.clear();
    jetM_.  clear();
    jetTag_.clear();
    met_          = zwwDefault;
    metPhi_       = zwwDefault;
    njet_         = zwwDefault;
    nbjet_        = zwwDefault;
    st_           = zwwDefault;
    minMt_        = zwwDefault;
    minDeltaPhi_  = zwwDefault;

        // Buffer
    lepVec_.clear();
    jetVec_.clear();
//    TLorentzVector metVec_.SetXYZM(0.,0.,0.,0.);
    metVec_.SetXYZM(0.,0.,0.,0.);
    z0LepIdx_[0] = zwwDefault;
    z0LepIdx_[1] = zwwDefault;
    z1LepIdx_[0] = zwwDefault;
    z1LepIdx_[1] = zwwDefault;
    zaLepIdx_[0] = zwwDefault;
    zaLepIdx_[1] = zwwDefault;
    zbLepIdx_[0] = zwwDefault;
    zbLepIdx_[1] = zwwDefault;
    flagZ1SF_    = zwwDefault;

        // All other variables
    outPreSelection_ = false;

}

void ZWW::isLepOk(){
    // check the validity of input
    if (lepPt_.size() == lepEta_.size()&&
        lepPt_.size() == lepPhi_.size()&&
        lepPt_.size() == lepFl_.size()&&
        lepPt_.size() == lepCh_.size()&&
        lepPt_.size() == lepId_.size()){
//        lepPt_[3]!=zwwDefault){
        isLepOk_ = true;
    }
    else{
        isLepOk_ = false;
    }
}

void ZWW::isJetOk(){
    // check the validity of inputi
    if (jetPt_.size() == jetEta_.size() &&
        jetPt_.size() == jetPhi_.size() &&
        jetPt_.size() == jetTag_.size() &&
        jetPt_.size() == jetM_.size()){
        isJetOk_ = true;
    }
    else{
        isJetOk_ = false;
    }
}

void ZWW::isMETOk(){
    if (met_ > 0 && fabs(metPhi_) <PI ){
        isMETOk_ = true;
    }else{
        isMETOk_ = false;
    }
}

void ZWW::isAllOk(){
        isAllOk_ = isLepOk_*isJetOk_*isMETOk_;
        isAllOk_ = preSelection();
}


void ZWW::setLepton(std::vector<float> pt,
                    std::vector<float> eta,
                    std::vector<float> phi,
                    std::vector<float> flavor,
                    std::vector<float> charge,
                    std::vector<float> id){
    lepPt_ = pt;
    lepEta_= eta;
    lepPhi_= phi;
    lepFl_ = flavor;
    lepCh_ = charge;
    lepId_ = id;
    isLepOk();

    if (isLepOk_){
        TLorentzVector buffVec;
        for(int iVec=0; iVec < 4; iVec++){
            buffVec.SetPtEtaPhiM(lepPt_     [iVec],
                                 lepEta_    [iVec],
                                 lepPhi_    [iVec],
                                 0);
            lepVec_.push_back(buffVec);
        }
        setZ0LepIdx_();
        setZ1LepIdx_();
        setZaZbLepIdx_();
    }
}

void ZWW::setJet(std::vector<float> pt,
                 std::vector<float> eta,
                 std::vector<float> phi,
                 std::vector<float> mass,
                 std::vector<float> tag){
    jetPt_ = pt;
    jetEta_= eta;
    jetPhi_= phi;
    jetM_  = mass;
    jetTag_= tag;
    isJetOk();
}

void ZWW::setMET(float met, float phi){
    met_    = met;
    metPhi_ = phi;
 metVec_.SetPtEtaPhiM(met_, 0, metPhi_, 0.);
    isMETOk();
}

//! buffer setter
void ZWW::setZ0LepIdx_(){
    z0LepIdx_[0] = zwwDefault;
    z0LepIdx_[1] = zwwDefault;
    if ( isLepOk_ ){
        float buffBias;
        float bestBias = -1*zwwDefault;
        for(int iL=0; iL < 4; iL++){
            for(int jL=iL+1; jL < 4; jL++){
                if (lepCh_[iL] + lepCh_[jL] != 0 ){
                    continue;
                }
                if (fabs(lepFl_[iL]) != fabs(lepFl_[jL]) ){ 
                    continue;
                }
                buffBias = (lepVec_[iL]+lepVec_[jL]).M();
                if ( fabs(buffBias - ZMASS) < bestBias){
                    bestBias = fabs(buffBias-ZMASS);
                    z0LepIdx_[0] = iL;
                    z0LepIdx_[1] = jL;
                }
            }
        }
    }
}


void ZWW::setZ1LepIdx_(){
    z1LepIdx_[0] = zwwDefault;
    z1LepIdx_[1] = zwwDefault;
    if (isLepOk_){
        if (z0LepIdx_[0]!=zwwDefault){
            for(int iL=0; iL< 4 ; iL++){
                if (iL != z0LepIdx_[0] && iL != z0LepIdx_[1]){
                    if(z1LepIdx_[0] == zwwDefault){
                        z1LepIdx_[0] = iL;
                    }
                    else{
                        z1LepIdx_[1] = iL;
                    }
                }
            }
        }
    }
}
    
void ZWW::setZaZbLepIdx_(){
    zaLepIdx_[0] = zwwDefault;
    zaLepIdx_[1] = zwwDefault;
    zbLepIdx_[0] = zwwDefault;
    zbLepIdx_[1] = zwwDefault;
    if ((isLepOk_)&&
        (lepCh_[0]+lepCh_[1]+lepCh_[2]+lepCh_[3]==0)&&
        (abs(lepFl_[0])==abs(lepFl_[1]))&&(abs(lepFl_[0])==abs(lepFl_[2]))&&(abs(lepFl_[0])==abs(lepFl_[3])) ){
        setZ0LepIdx_();
        setZ1LepIdx_();
        int k = 0;
        if(z0LepIdx_[0]!=zwwDefault && z1LepIdx_[0]!=zwwDefault){ //check z0 z1 pair
            for (int jL = 0 ; jL <2 ; jL++){
                if(lepCh_[z0LepIdx_[0]]+lepCh_[z1LepIdx_[jL]]==0){  //choose the other ossf pair, four lepton need to be eeee/mmmm
                   if( fabs((lepVec_[z0LepIdx_[0]]+lepVec_[z1LepIdx_[jL]]).M()-ZMASS ) > fabs((lepVec_[z0LepIdx_[1]]+lepVec_[z1LepIdx_[(jL+1)%2]]).M()-ZMASS)){
                       k = 1;
                   }
                   zaLepIdx_[0] = z0LepIdx_[k];
                   zaLepIdx_[1] = z1LepIdx_[(jL+k)%2];
                   zbLepIdx_[0] = z0LepIdx_[(k+1)%2];
                   zbLepIdx_[1] = z1LepIdx_[jL];
               }
            }
        }
    }
}


//! functions

bool ZWW::preSelection(){
    outPreSelection_ = false;
    if ( isAllOk_ ){
        
        if ( lepCh_[0]+lepCh_[1]+lepCh_[2]+lepCh_[3]  == 0 
             && lepId_[3] > 0.5
             && lepPt_[0] > 25
             && lepPt_[1] > 15
             && lepPt_[2] > 10 
             && lepPt_[3] > 10 
             && lepPt_[4] < 10 ){
             outPreSelection_ = true;
        }

        return outPreSelection_;
    }else{
        return false;
    }
}

//lepton variables

float ZWW::mllll_zh4l(){
    if (isAllOk_){
        return (lepVec_[0]+lepVec_[1]+lepVec_[2]+lepVec_[3]).M();
    }
    else {
        return zwwDefault;
    }
}


float ZWW::pfmetPhi_zh4l(){
    if (isAllOk_){
        return metPhi_;
    }
    else{
        return zwwDefault;
    }
}

float ZWW::zMass_zh4l(int zLepIdx_[2]){
    if (isAllOk_){
        if (zLepIdx_[0]!=zwwDefault){
            return (lepVec_[zLepIdx_[0]]+lepVec_[zLepIdx_[1]]).M();
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}


float ZWW::zPt_zh4l(int zLepIdx_[2]){
    if (isAllOk_){
        if (zLepIdx_[0]!=zwwDefault){
            return (lepVec_[zLepIdx_[0]]+lepVec_[zLepIdx_[1]]).Pt();
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}


float ZWW::z0Mass_zh4l(){
    return zMass_zh4l(z0LepIdx_);
}

float ZWW::z0Pt_zh4l(){
    return zPt_zh4l(z0LepIdx_);
}

float ZWW::z1Mass_zh4l(){
    return zMass_zh4l(z1LepIdx_);
}

float ZWW::z1Pt_zh4l(){
    return zPt_zh4l(z1LepIdx_);
}

float ZWW::zaMass_zh4l(){
    return zMass_zh4l(zaLepIdx_);
}


float ZWW::zbMass_zh4l(){
    return zMass_zh4l(zbLepIdx_);
}


float ZWW::zDeltaR_zh4l(int zLepIdx_[2]){
    if(isAllOk_){
        if (zLepIdx_[0]!=zwwDefault){
            return  lepVec_[zLepIdx_[0]].DeltaR(lepVec_[zLepIdx_[1]]);
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::zaDeltaR_zh4l(){
    return zDeltaR_zh4l(zaLepIdx_);
}

float ZWW::zbDeltaR_zh4l(){
    return zDeltaR_zh4l(zbLepIdx_);
}

float ZWW::z0DeltaR_zh4l(){
    return zDeltaR_zh4l(z0LepIdx_);
}

float ZWW::z1DeltaR_zh4l(){
    return zDeltaR_zh4l(z1LepIdx_);
}

float ZWW::zDeltaPhi_zh4l(int zLepIdx_[2]){
    if (isAllOk_){
        if (zLepIdx_[0]!=zwwDefault){
            return (lepVec_[zLepIdx_[0]].DeltaPhi(lepVec_[zLepIdx_[1]]));
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}


float ZWW::z0DeltaPhi_zh4l(){
    return zDeltaPhi_zh4l(z0LepIdx_);
}

float ZWW::z1DeltaPhi_zh4l(){
    return zDeltaPhi_zh4l(z1LepIdx_);
}

float ZWW::zaDeltaPhi_zh4l(){
    return zDeltaPhi_zh4l(zaLepIdx_);
}

float ZWW::zbDeltaPhi_zh4l(){
    return zDeltaPhi_zh4l(zbLepIdx_);
}


float ZWW::minDeltaPhi_zh4l(){
    if (isAllOk_){
        minDeltaPhi_ = -1*zwwDefault;
        for(int iL=0; iL < 4; iL++){
            for(int jL=iL+1; jL < 4; jL++){
                if (lepCh_[iL] != lepCh_[jL]){
                    minDeltaPhi_ =(fabs(minDeltaPhi_) < fabs(lepVec_[iL].DeltaPhi(lepVec_[jL]))) ? minDeltaPhi_: lepVec_[iL].DeltaPhi(lepVec_[jL]);
                }
            }
        }
        return minDeltaPhi_;
    }
    else{
        return zwwDefault;
    }
}


float ZWW::z1dPhi_lep1MET_zh4l(){
    if (isAllOk_ && isLepOk_){
        setZ0LepIdx_();
        setZ1LepIdx_();
        return fabs((lepVec_[z1LepIdx_[0]]).DeltaPhi(metVec_));
            }
    else{
        return -1.*zwwDefault;
    }
}

float ZWW::z1dPhi_lep2MET_zh4l(){
    if (isAllOk_ && isLepOk_){
        setZ0LepIdx_();
        setZ1LepIdx_();
        return fabs((lepVec_[z1LepIdx_[1]]).DeltaPhi(metVec_));
            }
    else{
        return -1.*zwwDefault;
    }
}

float ZWW::z1mindPhi_lepMET_zh4l(){
    if (isAllOk_ && isLepOk_){
        setZ0LepIdx_();
        setZ1LepIdx_();
float dphi1 = fabs((lepVec_[z1LepIdx_[0]]).DeltaPhi(metVec_));
float dphi2 = fabs((lepVec_[z1LepIdx_[1]]).DeltaPhi(metVec_));
       if(dphi1 < dphi2) {
          return dphi1;
     }
       else {
          return dphi2;
     }
            }
    else{
        return -1.*zwwDefault;
    }
}

float ZWW::chllll_zh4l(){
    if (isAllOk_){
       return lepCh_[0]+lepCh_[1]+lepCh_[2]+lepCh_[3];       
    }
    else{
        return zwwDefault;
    }
}

float ZWW::minMt_zh4l(){
    if (isAllOk_){
        minMt_ = -1*zwwDefault;
        for(int iL=0; iL< 4 ; iL++){
            minMt_ = (minMt_< sqrt(2*lepVec_[iL].Pt()*met_*(1-cos(lepVec_[iL].Phi()-metPhi_)))) ? minMt_:sqrt(2*lepVec_[iL].Pt()*met_*(1-cos(lepVec_[iL].Phi()-metPhi_)));
        }
        return minMt_;
    }
    else{
        return zwwDefault;
    }
}


float ZWW::lepMt_zh4l(int iL){
    if (isAllOk_){
        return sqrt(2*lepVec_[iL].Pt()*met_*(1-cos(lepVec_[iL].Phi()-metPhi_)));
    }
    else{
        return zwwDefault;
    }
}

float ZWW::lep1Mt_zh4l(){
    return lepMt_zh4l(0);
}

float ZWW::lep2Mt_zh4l(){
    return lepMt_zh4l(1);
}

float ZWW::lep3Mt_zh4l(){
    return lepMt_zh4l(2);
}

float ZWW::lep4Mt_zh4l(){
    return lepMt_zh4l(3);
}

float ZWW::z1Mt_zh4l(){
    if(isAllOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            return sqrt(2*(lepVec_[z1LepIdx_[0]]+lepVec_[z1LepIdx_[1]]).Pt()*met_*(1-cos((lepVec_[z1LepIdx_[0]]+lepVec_[z1LepIdx_[1]]).Phi()-metPhi_)));
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::flagZ1SF_zh4l(){
    if(isAllOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            if(abs(lepFl_[z1LepIdx_[0]]) == abs(lepFl_[z1LepIdx_[1]])){
                flagZ1SF_ = 1;
                return flagZ1SF_;
            }
            else{
                flagZ1SF_= 0;
                return flagZ1SF_;
            }
        }
        else{
            return zwwDefault;
        }
    }
    else{
        return zwwDefault;
    }
}

