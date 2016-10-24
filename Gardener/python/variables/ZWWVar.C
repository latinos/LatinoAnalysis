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
    float lep1Pt();
    float lep2Pt();
    float lep3Pt();
    float lep4Pt();
    float lep1Eta();
    float lep2Eta();
    float lep3Eta();
    float lep4Eta();
    float lep1Phi();
    float lep2Phi();
    float lep3Phi();
    float lep4Phi();
    float pfmet();
    float pfmetPhi();
    float z0mass();
    float z1mass();
    float flagZ1SF();
    float z0DeltaPhi();
    float z1DeltaPhi();
    float z1DeltaR();
//    float z1Mt();
    float mllll();
    float chllll();
    float st();
    float njet();
    float nbjet();



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

        // Buffer and buffer setter
    std::vector<TLorentzVector> lepVec_;
    std::vector<TLorentzVector> jetVec_;
    void setZ0LepIdx_();
    void setZ1LepIdx_();
    int z0LepIdx_[2];
    int z1LepIdx_[2];
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
    met_    = zwwDefault;
    metPhi_ = zwwDefault;
    njet_ = zwwDefault;
    nbjet_ = zwwDefault;
    st_ = zwwDefault;

        // Buffer
    lepVec_.clear();
    jetVec_.clear();
//    TLorentzVector metVec_.SetXYZM(0.,0.,0.,0.);
    metVec_.SetXYZM(0.,0.,0.,0.);
    z0LepIdx_[0] = zwwDefault;
    z0LepIdx_[1] = zwwDefault;
    z1LepIdx_[0] = zwwDefault;
    z1LepIdx_[1] = zwwDefault;
    flagZ1SF_   = zwwDefault;

        // All other variables
    outPreSelection_ = false;

}

void ZWW::isLepOk(){
    // check the validity of input
    if (lepPt_.size() == lepEta_.size()&&
        lepPt_.size() == lepPhi_.size()&&
        lepPt_.size() == lepFl_.size()&&
        lepPt_.size() == lepCh_.size()&&
        lepPt_.size() == lepId_.size()&&
        lepPt_[3]!=zwwDefault){
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

    if (isJetOk_){
        // build buffer here!
    }
}

void ZWW::setMET(float met, float phi){
    met_    = met;
    metPhi_ = phi;
    isMETOk();
}

//! buffer setter
void ZWW::setZ0LepIdx_(){
    z0LepIdx_[0] = zwwDefault;
    z0LepIdx_[1] = zwwDefault;
    if ( isLepOk_ ){
        float buffBias;
        float bestBias = 9999;
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
        if (z0LepIdx_[0]!=zwwDefault && z0LepIdx_[1]!=zwwDefault){
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
float ZWW::lep1Pt(){
    if (isLepOk_){
        return lepPt_[0];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep2Pt(){
    if (isLepOk_){
        return lepPt_[1];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep3Pt(){
    if (isLepOk_){
        return lepPt_[2];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep4Pt(){
    if (isLepOk_){
        return lepPt_[3];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep1Eta(){
    if (isLepOk_){
        return lepEta_[0];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep2Eta(){
    if (isLepOk_){
        return lepEta_[1];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep3Eta(){
    if (isLepOk_){
        return lepEta_[2];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep4Eta(){
    if (isLepOk_){
        return lepEta_[3];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep1Phi(){
    if (isLepOk_){
        return lepPhi_[0];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep2Phi(){
    if (isLepOk_){
        return lepPhi_[1];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep3Phi(){
    if (isLepOk_){
        return lepPhi_[2];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::lep4Phi(){
    if (isLepOk_){
        return lepPhi_[3];
    }
    else {
        return zwwDefault;
    }
}

float ZWW::mllll(){
    if (isLepOk_){
        return (lepVec_[0]+lepVec_[1]+lepVec_[2]+lepVec_[3]).M();
    }
    else {
        return zwwDefault;
    }
}

float ZWW::pfmet(){
    if (isMETOk_){
        return met_;
    }
    else{
        return zwwDefault;
    }
}

float ZWW::pfmetPhi(){
    if (isMETOk_){
        return metPhi_;
    }
    else{
        return zwwDefault;
    }
}

float ZWW::z0mass(){
    if (isLepOk_){
        if (z0LepIdx_[0]!=zwwDefault){
            return (lepVec_[z0LepIdx_[0]]+lepVec_[z0LepIdx_[1]]).M();
        }
        else{
            setZ0LepIdx_();
            if (z0LepIdx_[0]!=zwwDefault){
                return (lepVec_[z0LepIdx_[0]]+lepVec_[z0LepIdx_[1]]).M();
                }
            else{
                return zwwDefault;
            }
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::z1mass(){
    if (isLepOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            return (lepVec_[z1LepIdx_[0]]+lepVec_[z1LepIdx_[1]]).M();
        }
        else{
            setZ1LepIdx_();
            if (z1LepIdx_[0]!=zwwDefault){
                return (lepVec_[z1LepIdx_[0]]+lepVec_[z1LepIdx_[1]]).M();
                }
            else{
                return zwwDefault;
            }
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::z0DeltaPhi(){
    if (isLepOk_){
        if (z0LepIdx_[0]!=zwwDefault){
            return (lepVec_[z0LepIdx_[0]].DeltaPhi(lepVec_[z0LepIdx_[1]]));
        }
        else{
            setZ0LepIdx_();
            if (z0LepIdx_[0]!=zwwDefault){
                return (lepVec_[z0LepIdx_[0]].DeltaPhi(lepVec_[z0LepIdx_[1]]));
                }
            else{
                return zwwDefault;
            }
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::z1DeltaPhi(){
    if (isLepOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            return (lepVec_[z1LepIdx_[0]].DeltaPhi(lepVec_[z1LepIdx_[1]]));
        }
        else{
            setZ1LepIdx_();
            if (z1LepIdx_[0]!=zwwDefault){
                return (lepVec_[z1LepIdx_[0]].DeltaPhi(lepVec_[z1LepIdx_[1]]));
            }
            else{
                return zwwDefault;
            }
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::chllll(){
    if (isLepOk_){
       return lepCh_[0]+lepCh_[1]+lepCh_[2]+lepCh_[3];       
    }
    else{
        return zwwDefault;
    }
}
/*
float ZWW::mt(int idx_){
    if (isLepOk_ && isMETOk_){
        return sqrt(2*lepVec_[idx_].Pt()*met_*(1-cos(lepVec_[idx_].Phi-metPhi_)));
    }
    else{
        return zwwDefault;
    }
}

float ZWW::minZ1mt(){
    if(isLepOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            return (mt(z1LepIdx_[0])<mt(z1LepIdx_[1])) ? mt(z1LepIdx_[0]):mt(z1LepIdx_[1]);
        }
        else{
        setZ1LepIdx_();
        if (z1LepIdx_[0]!=zwwDefault){
            return (mt(z1LepIdx_[0])<mt(z1LepIdx_[1])) ? mt(z1LepIdx_[0]):mt(z1LepIdx_[1]);
            }
        else{
            return zwwDefault;
        }
    }
}
*/
float ZWW::flagZ1SF(){
    if(isLepOk_){
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
            setZ1LepIdx_();
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
    }
    else{
        return zwwDefault;
    }
}

float ZWW::z1DeltaR(){
    if(isLepOk_){
        if (z1LepIdx_[0]!=zwwDefault){
            return  lepVec_[z1LepIdx_[0]].DeltaR(lepVec_[z1LepIdx_[1]]);
        }
        else{
            setZ1LepIdx_();
            if (z1LepIdx_[0]!=zwwDefault){
                return  lepVec_[z1LepIdx_[0]].DeltaR(lepVec_[z1LepIdx_[1]]);
            }
            else{
                return zwwDefault;
            }
        }
    }
    else{
        return zwwDefault;
    }
}

float ZWW::njet(){
    if(isJetOk_){
        njet_ = 0;
        for (unsigned int ijet = 0; ijet < jetPt_.size(); ijet++){
            if(jetPt_[ijet] > 40 && fabs(jetEta_[ijet])<4.7){
                njet_ +=1;
            }
        }
        return njet_;
    }
    else{
        return zwwDefault;
    }
}

float ZWW::nbjet(){
    if(isJetOk_){
        nbjet_ = 0;
        for (unsigned int ijet = 0; ijet < jetPt_.size(); ijet++){
            if(jetPt_[ijet] > 20 && jetPt_[ijet] <40  && fabs(jetEta_[ijet]<4.7)){
                if(jetTag_[ijet] > 0.875){
                    nbjet_ +=1;
                }
            }
        }
        return nbjet_;
    }
    else {
        return zwwDefault;
    }
}

float ZWW::st(){ 
    if(isLepOk_ && isJetOk_ && isMETOk_){
        st_ = 0; 
        for(unsigned int ilep = 0; ilep < lepPt_.size(); ilep++){
            if(lepPt_[ilep] > 0){
                st_ += lepPt_[ilep];
            }
        }
        for(unsigned int ijet = 0; ijet < jetPt_.size(); ijet++){
            if(jetPt_[ijet] > 0){
                st_ += jetPt_[ijet];
            }
        }
        st_ += met_;
        return st_;
    }
    else{
        return zwwDefault;
    }
}
