
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <TMinuit.h>
#include <TF1.h>
#include <TVector2.h>
#include <vector>

#define NVTX 35
// order (as in SkimEventProducer.h) for std_vector_ptc_...
string CataList[]= {"hEtaPlus", "hEtaMinus", "h0Barrel", "h0EndcapPlus", "h0EndcapMinus",
"gammaBarrel", "gammaEndcapPlus", "gammaEndcapMinus",
"hHFPlus", "hHFMinus",
"egammaHFPlus", "egammaHFMinus",
"e", "mu",
"gammaForwardPlus", "gammaForwardMinus"};
//varType
enum {multiplicity, ngoodVertices, sumPt, pfType1, ptcMet, ptValence, metPhiNvtx};
namespace PTCType {
enum {X,h, e, mu,gamma, h0, h_HF, egamma_HF, AllPtc}; //from categories.py in MetTools/MetPhiCorrections/python/tools
}

 struct XYshiftDB{
   string ptcCatagory;
   unsigned ptcType;
   unsigned nBinVar;
   vector<string> nameBinVar;
   unsigned nParVar;
   vector<unsigned> varType;
   vector<float>    parVarRange1;
   vector<float>    parVarRange2;
   string           shiftFormula;
   string           par0Formula;
   string           ptcMetFormula;

   float binMin;
   float binMax;
   float PhiBinMin1;
   float PhiBinMax1;
   float PhiBinMin2;
   float PhiBinMax2;
   float PhiBinMin3;
   float PhiBinMax3;
   float p0ftRngMin;
   float p0ftRngMax;
   float ptcMetRngMin;
   float ptcMetRngMax;

   vector<float>    ftnParasX[NVTX+1];
   vector<float>    ftnParasY[NVTX+1];
   vector<float>    ftnParas_X;
   vector<float>    ftnParas_Y;
   vector<float>    ftnParas_Phi;
   vector<float>    ftnParas_Phi1;
   vector<float>    ftnParas_Phi2;
   vector<float>    ftnParas_Phi3;
   vector<float>    ftnParas_Par0;
   vector<float>    ftnParas_PtcMet;

   TF1* Ftn_X;
   TF1* Ftn_Y;
   TF1* FtnX[NVTX+1];
   TF1* FtnY[NVTX+1];

   TF1* Ftn_Phi;
   TF1* Ftn_Phi1;
   TF1* Ftn_Phi2;
   TF1* Ftn_Phi3;
   TF1* Ftn_Par0;
   TF1* Ftn_PtcMet;

 }myDB;

  void handleError(const std::string& fClass, const std::string& fMessage)
  {
    std::string sserr;
    sserr=fClass+" ERROR: "+fMessage;
    throw std::runtime_error(sserr);
  }

inline std::string getSection(const std::string& token)
{
  size_t iFirst = token.find ('[');
  size_t iLast = token.find (']');
  if (iFirst != std::string::npos && iLast != std::string::npos && iFirst < iLast)
    return std::string (token, iFirst+1, iLast-iFirst-1);
  return "";
}
inline std::string getDefinitions(const std::string& token)
{
  size_t iFirst = token.find ('{');
  size_t iLast = token.find ('}');
  if (iFirst != std::string::npos && iLast != std::string::npos && iFirst < iLast)
    return std::string (token, iFirst+1, iLast-iFirst-1);
  return "";
}
inline std::vector<std::string> getTokens(const std::string& fLine)
{
  std::vector<std::string> tokens;
  std::string currentToken;
  for (unsigned ipos = 0; ipos < fLine.length (); ++ipos)
  {
    char c = fLine[ipos];
    if (c == '#') break; // ignore comments
    else if (c == ' ')
    { // flush current token if any
      if (!currentToken.empty())
      {
	tokens.push_back(currentToken);
	currentToken.clear();
      }
    }
    else
      currentToken += c;
  }
  if (!currentToken.empty()) tokens.push_back(currentToken); // flush end
  return tokens;
}

inline long int getSigned(const std::string& token)
{
  char* endptr;
  unsigned result = strtol (token.c_str(), &endptr, 0);
  if (endptr == token.c_str())
    {
      std::string sserr;
      sserr="can't convert token "+token+" to signed value";
      handleError("getSigned",sserr);
    }
  return result;
}
  //----------------------------------------------------------------------
  inline float getFloat(const std::string& token)
  {
    char* endptr;
    float result = strtod (token.c_str(), &endptr);
    if (endptr == token.c_str())
      {
        std::string sserr;
        sserr="can't convert token "+token+" to float value";
	handleError("getFloat",sserr);
      }
    return result;
  }
  //----------------------------------------------------------------------
  inline unsigned getUnsigned(const std::string& token)
  {
    char* endptr;
    unsigned result = strtoul (token.c_str(), &endptr, 0);
    if (endptr == token.c_str())
      {
        std::string sserr;
        sserr="can't convert token "+token+" to unsigned value";
	handleError("getUnsigned",sserr);
      }
    return result;
  }

class metXYshift {
public:
 //! constructor
 metXYshift(string);
 virtual ~metXYshift() {}

 void printPara();
 void setPtcInfo(
     std::vector<float> std_vector_ptc_counts,
     std::vector<float> std_vector_ptc_sumPt,
     std::vector<float> std_vector_ptc_metX,
     std::vector<float> std_vector_ptc_metY);
 void setEvtInfo(
     float met, float metPhi , float nGoodVtx
     );
// int VarType();
 void CalcXYshiftCorr(
     //string ptcCatagory,
//	double nVtx,
//	double pfMet,
	double &corx, double &cory
  	);

 
 //! check
 //void checkIfOk();
 
 //! set functions
 
private:
 //! variables
 void Definitions(const std::string& fLine);
 void Record(const std::string& fLine);
 void BuildFormula();

 XYshiftDB tmpDB;
 vector<XYshiftDB> v_XYshiftDB;
 std::vector<float> ptc_counts;
 std::vector<float> ptc_sumPt;
 std::vector<float> ptc_metX;
 std::vector<float> ptc_metY;

 TVector2 *ptc_tv2;
 float ptc_met;
 float ptc_phi;
 float par0;
 float corR;

 float met_, metPhi_, nGoodVtx_;

 bool bingo;
 
};

//! constructor
metXYshift::metXYshift(string paraFile) {
  //cout<<"Parameter file is: "<<paraFile<<endl;
  std::ifstream input(paraFile.c_str());
  if( !input )
  {
    cout<<"parameter file is not opened: "<<paraFile<<endl;;
    exit(-1);
    //throw std::runtime_error("parameter file is not opened");
  }

  v_XYshiftDB.clear();

  myDB.ptcCatagory="";
  myDB.nameBinVar.clear();
  myDB.varType.clear();
  myDB.parVarRange1.clear();
  myDB.parVarRange2.clear();
  myDB.ftnParas_X.clear();
  myDB.ftnParas_Y.clear();
  myDB.ftnParas_Phi.clear();
  myDB.ftnParas_Phi1.clear();
  myDB.ftnParas_Phi2.clear();
  myDB.ftnParas_Phi3.clear();
  myDB.ftnParas_Par0.clear();
  myDB.ftnParas_PtcMet.clear();

  for(int i(0);i<=NVTX;i++){
    myDB.ftnParasX[i].clear();
    myDB.ftnParasY[i].clear();
  }


  std::string line;
  std::string currentDefinitions = "";
  cout<<"getline from input file"<<endl;
  myDB.ptcCatagory = "";
  while (std::getline(input,line))
  {
    std::string ptcCatagory = getSection(line);
    std::string tmp = getDefinitions(line);
    //cout<<"ptcCatagory is : "<<ptcCatagory<<endl;
    // catch ptcCatagory and save previous DB
    if (!ptcCatagory.empty() && tmp.empty())
    {
      if(!myDB.ptcCatagory.empty()) // there is a previous DB filled.
      {
	// dumping filled DB
	BuildFormula();
	v_XYshiftDB.push_back(myDB);

	// cleanning DB
        myDB.ptcCatagory="";
        myDB.nameBinVar.clear();
        myDB.varType.clear();
        myDB.parVarRange1.clear();
        myDB.parVarRange2.clear();
        myDB.ftnParas_X.clear();
        myDB.ftnParas_Y.clear();
        myDB.ftnParas_Phi.clear();
        myDB.ftnParas_Phi1.clear();
        myDB.ftnParas_Phi2.clear();
        myDB.ftnParas_Phi3.clear();
        myDB.ftnParas_Par0.clear();
        myDB.ftnParas_PtcMet.clear();

        for(int i(0);i<=NVTX;i++){
          myDB.ftnParasX[i].clear();
          myDB.ftnParasY[i].clear();
        }
      }
      myDB.ptcCatagory = ptcCatagory;
      continue;
    }
    if (!tmp.empty())
    {
      currentDefinitions = tmp;
      //cout<<"Definitions input: "<<currentDefinitions<<endl;
      Definitions(currentDefinitions);
      continue;
    }
    if( myDB.ptcCatagory != "")
    {
      Record(line);
    }
  }
  BuildFormula();
  v_XYshiftDB.push_back(myDB); // last ptcCatagory to be filled

}

void metXYshift::Definitions(const std::string& fLine)
{
  std::vector<std::string> tokens = getTokens(fLine);
  unsigned const TokenSize = tokens.size();
  // ptclType, nBinVar,  mBinVar(names), nParVar, {varType(varType), varTypeRange1, varTypeRange2}, formula
  if (!tokens.empty())
  { 
    if (TokenSize < 8) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): Great than or equal to 8 expected tokens:"<<tokens.size();
      handleError("metXYshift::Definitions",sserr.str());
    }
    myDB.ptcType = getUnsigned(tokens[0]);
    myDB.nBinVar = getUnsigned(tokens[1]);
    for(unsigned i=2;i< 2 + myDB.nBinVar;i++)
    {
      myDB.nameBinVar.push_back(tokens[i]);
    }
    myDB.nParVar = getUnsigned(tokens[2+myDB.nBinVar]);
    for(unsigned i=0; i< myDB.nParVar; i++){
      myDB.varType.push_back( getUnsigned(tokens[i*3 + 2+myDB.nBinVar+1]));
      myDB.parVarRange1.push_back( getFloat(tokens[i*3 + 2+myDB.nBinVar+2]));
      myDB.parVarRange2.push_back( getFloat(tokens[i*3 + 2+myDB.nBinVar+3]));
    }
    myDB.shiftFormula = tokens[ 2+myDB.nBinVar+myDB.nParVar*3 +1];
    // check the size of input parameters
    if ( TokenSize !=  2+myDB.nBinVar +1 + myDB.nParVar*3 +1 ) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): token size should be:"<<2+myDB.nBinVar + myDB.nParVar*3 +1 <<" but it is "<<TokenSize;
      handleError("Definitions",sserr.str());
    }
  }
}

void metXYshift::Record(const std::string& fLine)
{
  // quckly parse the line
  std::vector<std::string> tokens = getTokens(fLine);
  if (!tokens.empty())
  { 
    if (tokens.size() < 5) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): "<<"three tokens expected, "<<tokens.size()<<" provided.";
      handleError("metXYshift::Record",sserr.str());
    }
    string Axis = tokens[0];
    if(Axis == "X" || Axis == "Y" || Axis == "Phi"){
      myDB.binMin=getFloat(tokens[1]);
      myDB.binMax=getFloat(tokens[2]);
    }else if(Axis == "Phi1" ){
      myDB.PhiBinMin1=getFloat(tokens[1]);
      myDB.PhiBinMax1=getFloat(tokens[2]);
    }else if(Axis == "Phi2" ){
      myDB.PhiBinMin2=getFloat(tokens[1]);
      myDB.PhiBinMax2=getFloat(tokens[2]);
    }else if(Axis == "Phi3" ){
      myDB.PhiBinMin3=getFloat(tokens[1]);
      myDB.PhiBinMax3=getFloat(tokens[2]);
    }else if(Axis == "Par0"){
      myDB.p0ftRngMin = getFloat(tokens[1]);
      myDB.p0ftRngMax = getFloat(tokens[2]);
    }else if (Axis == "PtcMet"){
      myDB.ptcMetRngMin = getFloat(tokens[1]);
      myDB.ptcMetRngMax = getFloat(tokens[2]);
    }else{
      bool findAxis(false);
      for(int i(0);i<= 35;i++){ // until nvtx 35
	char Xvtx[50];
	char Yvtx[50];
	sprintf(Xvtx,"X%d",i);
	sprintf(Yvtx,"Y%d",i);
	if(Axis == Xvtx || Axis == Yvtx){
	  findAxis = true;
          myDB.binMin=getFloat(tokens[1]);
          myDB.binMax=getFloat(tokens[2]);
	}
      }
      if( !findAxis){
        std::string sserr;
        sserr=Axis+" is not defined. !!!!!!!!!!!!!!!!!!11";
        handleError("Record", sserr);
      }
    }
    unsigned nPar = getUnsigned(tokens[3]);
    if(tokens.size()-4 != nPar)
    {
      std::stringstream sserr;
      sserr<<"X Record total token size should be "<<nPar +4<<" but it is "<<tokens.size();
      handleError("metXYshift::Record",sserr.str());
    }

    if(Axis == "X") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_X.push_back(getFloat(tokens[4+i]));
      }
    }
    else if(Axis == "Y") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Y.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "Phi") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Phi.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "Phi1") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Phi1.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "Phi2") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Phi2.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "Phi3") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Phi3.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "PtcMet") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_PtcMet.push_back(getFloat(tokens[4+i]));
      }
    }else if(Axis == "Par0") 
    {
      for(unsigned i(0); i< nPar ;i++)
      {
	myDB.ftnParas_Par0.push_back(getFloat(tokens[4+i]));
      }
    }else{
      bool findAxis(false);
      for(int i(0);i<= 35;i++){ // until nvtx 35
	char Xvtx[50];
	char Yvtx[50];
	sprintf(Xvtx,"X%d",i);
	sprintf(Yvtx,"Y%d",i);
        if(Axis == Xvtx ){
          findAxis = true;
          for(unsigned j(0); j<nPar ;j++){
            myDB.ftnParasX[i].push_back(getFloat(tokens[4+j]));
          }
	}
        if(Axis == Yvtx ){
          findAxis = true;
          for(unsigned j(0); j<nPar ;j++){
            myDB.ftnParasY[i].push_back(getFloat(tokens[4+j]));
          }
        }
      }
      if(!findAxis)handleError("Record","record is not for met X or Y");
    }

  }
}
      


//! set functions

void metXYshift::printPara() {
  cout<<"Printing parameters of metXYshift @@@@@@@@@@@@@@@@@@@@"<<endl;
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    XYshiftDB tmpDB=v_XYshiftDB[i];
    cout<<"ptcCatagory: "<<tmpDB.ptcCatagory<<endl;
    cout<<"ptcType: "    <<tmpDB.ptcType<<endl;
    cout<<"nBinVar: "    <<tmpDB.nBinVar<<endl;
    for(unsigned j(0); j<tmpDB.nBinVar; j++){
      cout<<j+1<<"st binVar: "<<tmpDB.nameBinVar[j]<<endl;
    }
    cout<<"nParVar: "    <<tmpDB.nParVar<<endl;
    for(unsigned j(0); j<tmpDB.nParVar; j++){
      cout<<j+1<<"st varType: "<<tmpDB.varType[j]<<endl;
      cout<<j+1<<"st parVarRange from: "<<tmpDB.parVarRange1[j]
	<<" to : "<<tmpDB.parVarRange2[j]<<endl;
    }
    cout<<"shiftFormula: "<<tmpDB.shiftFormula<<endl;
    cout<<"binMin : "<<tmpDB.binMin<<endl;
    cout<<"binMax : "<<tmpDB.binMax<<endl;
    cout<<"PhiBinMin1 : "<<tmpDB.PhiBinMin1<<endl;
    cout<<"PhiBinMax1 : "<<tmpDB.PhiBinMax1<<endl;
    cout<<"PhiBinMin2 : "<<tmpDB.PhiBinMin2<<endl;
    cout<<"PhiBinMax2 : "<<tmpDB.PhiBinMax2<<endl;
    cout<<"PhiBinMin3 : "<<tmpDB.PhiBinMin3<<endl;
    cout<<"PhiBinMax3 : "<<tmpDB.PhiBinMax3<<endl;
    cout<<"p0ftRngMin: "<<tmpDB.p0ftRngMin<<endl;
    cout<<"p0ftRngMax: "<<tmpDB.p0ftRngMax<<endl;
    cout<<"ptcMetRngMin: "<<tmpDB.ptcMetRngMin<<endl;
    cout<<"ptcMetRngMax: "<<tmpDB.ptcMetRngMax<<endl;
    //cout<<"met range: "<<tmpDB.metMin<<" - "<<tmpDB.metMax<<endl;
    if(myDB.ftnParas_X.size() != 0){
      cout<<"X parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_X.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_X[j];
      }
      cout<<endl;
      cout<<"Y parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Y.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Y[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi.size() != 0){
      cout<<"Phi parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Phi.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Phi[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi1.size() != 0){
      cout<<"Phi1 parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Phi1.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Phi1[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi2.size() != 0){
      cout<<"Phi2 parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Phi2.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Phi2[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi3.size() != 0){
      cout<<"Phi3 parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Phi3.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Phi3[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Par0.size() != 0){
      cout<<"Par0 parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_Par0.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_Par0[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParas_PtcMet.size() != 0){
      cout<<"ptcMet parameters : ";
      for(unsigned j(0);j<tmpDB.ftnParas_PtcMet.size();j++)
      {
        cout<<" "<<tmpDB.ftnParas_PtcMet[j];
      }
      cout<<endl;
    }
    if(myDB.ftnParasX[0].size() !=0 ){
      cout<<"pfType1 parameters : "<<endl;
      for(unsigned j(0); j<=NVTX; j++){
	cout<<"X"<<j;
	for(unsigned k(0); k<tmpDB.ftnParasX[j].size(); k++){
	  cout<<" "<<tmpDB.ftnParasX[j][k];
	}
	cout<<endl;
	cout<<"Y"<<j;
	for(unsigned k(0); k<tmpDB.ftnParasY[j].size(); k++){
	  cout<<" "<<tmpDB.ftnParasY[j][k];
	}
	cout<<endl;
      }
    }
    cout<<" Para. conformation from formula: "<<endl;
    if(myDB.ftnParasX[0].size() !=0 ){
      char Xvtx[50];
      char Yvtx[50];
      for(int i(0); i<= NVTX; i++){
	sprintf(Xvtx,"X%d",i);
	sprintf(Yvtx,"Y%d",i);
        cout<<" for "<<Xvtx;
	for(int j(0); j<tmpDB.FtnX[i]->GetNpar();j++){
	  cout<<" "<<tmpDB.FtnX[i]->GetParameter(j);
	}
	cout<<endl;
        cout<<" for "<<Yvtx;
	for(int j(0); j<tmpDB.FtnY[i]->GetNpar();j++){
	  cout<<" "<<tmpDB.FtnY[i]->GetParameter(j);
	}
	cout<<endl;
      }

    }

    if(myDB.ftnParas_X.size() != 0){
      cout<<" for X";
      for(int j(0);j<tmpDB.Ftn_X->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_X->GetParameter(j);
      }
      cout<<endl;
      cout<<" for Y";
      for(int j(0);j<tmpDB.Ftn_Y->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Y->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi.size() != 0){
      cout<<" for Phi";
      for(int j(0);j<tmpDB.Ftn_Phi->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Phi->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi1.size() != 0){
      cout<<" for Phi1 "<<tmpDB.Ftn_Phi1->GetExpFormula();
      for(int j(0);j<tmpDB.Ftn_Phi1->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Phi1->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi2.size() != 0){
      cout<<" for Phi2 "<<tmpDB.Ftn_Phi2->GetExpFormula();
      for(int j(0);j<tmpDB.Ftn_Phi2->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Phi2->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Phi3.size() != 0){
      cout<<" for Phi3 "<<tmpDB.Ftn_Phi3->GetExpFormula();
      for(int j(0);j<tmpDB.Ftn_Phi3->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Phi3->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_Par0.size() != 0){
      cout<<" for Par0";
      for(int j(0);j<tmpDB.Ftn_Par0->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_Par0->GetParameter(j);
      }
      cout<<endl;
    }
    if(myDB.ftnParas_PtcMet.size() != 0){
      cout<<" for PtcMet";
      for(int j(0);j<tmpDB.Ftn_PtcMet->GetNpar();j++)
      {
        cout<<" "<<tmpDB.Ftn_PtcMet->GetParameter(j);
      }
      cout<<endl;
    }

  }
}
//int metXYshift::VarType(){
//  XYshiftDB tmpDB=v_XYshiftDB[0];
//  return tmpDB.varType[0];
//}

void metXYshift::CalcXYshiftCorr(
    //string ptcCatagory,
    //double shiftVar,
    //double met,
    double &corx, double &cory
    ){
  corx = 0;
  cory = 0;
  bingo=false;
  //cout<<"used ptcCatagory"<<endl;
  for(unsigned idb(0); idb< v_XYshiftDB.size(); idb++){
    tmpDB=v_XYshiftDB[idb];
    if(tmpDB.varType[0] !=metPhiNvtx && tmpDB.varType[0] != pfType1) for(unsigned icata(0); icata< ptc_counts.size(); icata++){
      if(tmpDB.ptcCatagory == CataList[icata]){ //the index of CataList is the same to ptc_counts
	bingo = true;
	//cout<<icata<<" "<<tmpDB.ptcCatagory<<" "<<ptc_counts[icata]<<" "<<ptc_sumPt[icata]<<" "<<ptc_metX[icata]<<" "<<ptc_metY[icata]<<endl;
	switch (tmpDB.varType[0]){
	  case multiplicity :
	       cout<<"multiplicity not setup yet"<<endl;
	       break;
	  case ngoodVertices :
	       cout<<"ngoodVertices not setup yet"<<endl;
	       break;
	  case sumPt :
	       cout<<"sumPt not setup yet"<<endl;
	       break;
	  case pfType1 :
	       cout<<"pfType1 not setup yet"<<endl;
	       //tmpDB.Ftn_X;
	       break;
	  case ptcMet :
	       //cout<<"ptcMet"<<endl;
	       ptc_tv2 = new TVector2(ptc_metX[icata], ptc_metY[icata]);
	       ptc_met = ptc_tv2->Mod();
	       if(ptc_met <= 0) break;
	       if(ptc_met < tmpDB.ptcMetRngMin) ptc_met = tmpDB.ptcMetRngMin;
	       if(ptc_met > tmpDB.ptcMetRngMax) ptc_met = tmpDB.ptcMetRngMax;
	       ptc_phi = ptc_tv2->Phi();
	       ptc_phi = TVector2::Phi_mpi_pi(ptc_phi);
	       corR = tmpDB.Ftn_Phi->Eval(ptc_phi);
	       cout<<"corR: "<<corR<<"ptc_phi: "<<ptc_phi<<endl;
	       //corR = tmpDB.Ftn_Phi->Eval(ptc_phi)*tmpDB.Ftn_PtcMet->Eval(ptc_met);
	       corx -= corR*cos(ptc_phi);
	       cory -= corR*sin(ptc_phi);
	       break;
	  case ptValence :
	       //variable_ = sqrt(ptc_metX[icata]*ptc_metX[icata] + ptc_metY[icata]*ptc_metY[icata]);
	       ptc_tv2 = new TVector2(ptc_metX[icata], ptc_metY[icata]);
	       //cout<<"catagory: "<<icata<<endl;
	       ptc_met = ptc_tv2->Mod();
	       if(ptc_met > 0){
	         ptc_phi = ptc_tv2->Phi();
	         ptc_phi = TVector2::Phi_mpi_pi(ptc_phi);
		 if(ptc_met < tmpDB.p0ftRngMax){
		   par0 = tmpDB.Ftn_Par0->Eval(ptc_met);
		 }else{
		   par0 = tmpDB.Ftn_Par0->Eval(tmpDB.p0ftRngMax);
		 }
		 if(ptc_phi > 0){
		   corR = tmpDB.Ftn_Phi->Eval(ptc_phi)/2./tmpDB.Ftn_Phi->GetParameter(0)*par0;
		 }else{
		   corR = -tmpDB.Ftn_Phi->Eval(M_PI+ptc_phi)/2./tmpDB.Ftn_Phi->GetParameter(0)*par0;
		 }
		 corx -= corR*cos(ptc_phi);
		 cory -= corR*sin(ptc_phi);
	       }
	  default :            handleError("metXYshift::CalcXYshiftCorr","check tmpDB.varType"); break;
	}
      }
    }
    else if (tmpDB.varType[0] ==metPhiNvtx){ // metPhiNvtx case
      bingo = true;
      if( metPhi_ >= tmpDB.PhiBinMin1-0.1 && metPhi_ < tmpDB.PhiBinMax1 ){
        corR = tmpDB.Ftn_Phi1->Eval(metPhi_);
      }else if( metPhi_ >= tmpDB.PhiBinMin2 && metPhi_ < tmpDB.PhiBinMax2 ){
        corR = tmpDB.Ftn_Phi2->Eval(metPhi_);
      }else if( metPhi_ >= tmpDB.PhiBinMin3 && metPhi_ < tmpDB.PhiBinMax3 + 0.1 ){
        corR = tmpDB.Ftn_Phi3->Eval(metPhi_);
      }
      corx -= corR*cos(metPhi_);
      cory -= corR*sin(metPhi_);
    }
    else if( tmpDB.varType[0] == pfType1 && tmpDB.ptcType == PTCType::AllPtc ){
      bingo = true;
      if(nGoodVtx_ > NVTX){
	if(met_<tmpDB.parVarRange2[0]){
	  corx -=tmpDB.FtnX[NVTX]->Eval(met_);
	  cory -=tmpDB.FtnY[NVTX]->Eval(met_);
	}else{
	  corx -=tmpDB.FtnX[NVTX]->Eval(tmpDB.parVarRange2[0]);
	  cory -=tmpDB.FtnY[NVTX]->Eval(tmpDB.parVarRange2[0]);
	}
      }
      else for( int i(0); i<=NVTX; i++){
	if(nGoodVtx_ == i){
	  if(met_<tmpDB.parVarRange2[0]){
	    corx -=tmpDB.FtnX[i]->Eval(met_);
	    cory -=tmpDB.FtnY[i]->Eval(met_);
	  }else{
	    corx -=tmpDB.FtnX[i]->Eval(tmpDB.parVarRange2[0]);
	    cory -=tmpDB.FtnY[i]->Eval(tmpDB.parVarRange2[0]);
	  }
	}
      }
      //cout<<"Case pfType1 && AllPtc in metXYshift.C, (corx, cory): "<<corx<<", "<<cory<<endl;
    }
  }
  if( !bingo)
  {
      std::stringstream sserr;
      sserr<<"This ptcCatagory at DB is not reserved: "<<tmpDB.ptcCatagory;
      handleError("metXYshift::CalcXYshiftCorr",sserr.str());
  }
  //cout<<" met, phi, corR, corx, cory: "<<met_<<" "<<metPhi_<<" "<<corR<<" "<<corx<<" "<<cory<<endl;

}

void metXYshift::BuildFormula(){

  if(myDB.ftnParasX[0].size() != 0){
    char idxChar[50];
    for(unsigned i(0);i<=NVTX;i++){
      sprintf(idxChar,"%d",i);
      string ftnName="FtnX"+std::string(idxChar)+myDB.ptcCatagory;
      myDB.FtnX[i] = new TF1(ftnName.c_str(),myDB.shiftFormula.c_str());
      ftnName="FtnY"+std::string(idxChar)+myDB.ptcCatagory;
      myDB.FtnY[i] = new TF1(ftnName.c_str(),myDB.shiftFormula.c_str());
      for(unsigned j(0); j<myDB.ftnParasX[i].size();j++){
        myDB.FtnX[i]->SetParameter(j,myDB.ftnParasX[i][j]);
      }
      for(unsigned j(0); j<myDB.ftnParasY[i].size();j++){
        myDB.FtnY[i]->SetParameter(j,myDB.ftnParasY[i][j]);
      }
    }
  }
  if(myDB.ftnParas_X.size() != 0){
    string ftnName="Ftn_X_"+myDB.ptcCatagory;
    myDB.Ftn_X = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    ftnName="Ftn_Y_"+myDB.ptcCatagory;
    myDB.Ftn_Y = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_X.size(); i++){
      myDB.Ftn_X->SetParameter(i, myDB.ftnParas_X[i]);
    }
    for(unsigned i(0); i<myDB.ftnParas_Y.size(); i++){
      myDB.Ftn_Y->SetParameter(i, myDB.ftnParas_Y[i]);
    }
  }
  if(myDB.ftnParas_Phi.size() != 0){
    string ftnName="Ftn_Phi_"+myDB.ptcCatagory;
    myDB.Ftn_Phi = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_Phi.size(); i++){
      myDB.Ftn_Phi->SetParameter(i, myDB.ftnParas_Phi[i]);
    }
  }
  if(myDB.ftnParas_Phi1.size() != 0){
    string ftnName="Ftn_Phi1_"+myDB.ptcCatagory;
    myDB.Ftn_Phi1 = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_Phi1.size(); i++){
      myDB.Ftn_Phi1->SetParameter(i, myDB.ftnParas_Phi1[i]);
    }
  }
  if(myDB.ftnParas_Phi2.size() != 0){
    string ftnName="Ftn_Phi2_"+myDB.ptcCatagory;
    myDB.Ftn_Phi2 = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_Phi2.size(); i++){
      myDB.Ftn_Phi2->SetParameter(i, myDB.ftnParas_Phi2[i]);
    }
  }
  if(myDB.ftnParas_Phi3.size() != 0){
    string ftnName="Ftn_Phi3_"+myDB.ptcCatagory;
    myDB.Ftn_Phi3 = new TF1(ftnName.c_str(), myDB.shiftFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_Phi3.size(); i++){
      myDB.Ftn_Phi3->SetParameter(i, myDB.ftnParas_Phi3[i]);
    }
  }
  if(myDB.ftnParas_Par0.size() != 0){
    string ftnName="Ftn_Par0_"+myDB.ptcCatagory;
    if(myDB.ftnParas_Par0.size() == 3) myDB.par0Formula = "[0]*x+[1]*x*x+[2]*x*x*x";
    else {cout<<"check ftnParas_Par0.size() is not 3 !!!!!!!!!!!!!!"<<endl; exit(-1);}
    myDB.Ftn_Par0 = new TF1(ftnName.c_str(), myDB.par0Formula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_Par0.size(); i++){
      myDB.Ftn_Par0->SetParameter(i, myDB.ftnParas_Par0[i]);
    }
  }
  if(myDB.ftnParas_PtcMet.size() != 0){
    string ftnName="Ftn_PtcMet_"+myDB.ptcCatagory;
    if(myDB.ftnParas_PtcMet.size() == 1) myDB.ptcMetFormula = "[0]*x";
    else {cout<<"check ftnParas_PtcMet.size() is not 1 !!!!!!!!!!!!!!"<<endl; exit(-1);}
    myDB.Ftn_PtcMet = new TF1(ftnName.c_str(), myDB.ptcMetFormula.c_str());
    for(unsigned i(0); i<myDB.ftnParas_PtcMet.size(); i++){
      myDB.Ftn_PtcMet->SetParameter(i, myDB.ftnParas_PtcMet[i]);
    }
  }

}

void metXYshift::setPtcInfo(std::vector<float> std_vector_ptc_counts,std::vector<float> std_vector_ptc_sumPt,std::vector<float> std_vector_ptc_metX,std::vector<float> std_vector_ptc_metY){
  ptc_counts = std_vector_ptc_counts;
  ptc_sumPt  = std_vector_ptc_sumPt;
  ptc_metX   = std_vector_ptc_metX;
  ptc_metY   = std_vector_ptc_metY;
  //cout<<"setPtcInfo "<<endl;
  //for( unsigned i(0); i<ptc_counts.size(); i++){
  //  cout<<ptc_counts[i]<<" "<<ptc_sumPt[i]<<" "<<ptc_metX[i]<<" "<<ptc_metY[i]<<endl;
  //}
}

void metXYshift::setEvtInfo(float met, float metPhi, float nGoodVtx){
  met_ = met;
  metPhi_ = metPhi;
  nGoodVtx_ = nGoodVtx;
}
