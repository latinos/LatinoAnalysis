
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <TMinuit.h>
#include <TF1.h>
#include <vector>

 struct XYshiftDB{
   string sample;
   vector<double> mParVar;
   string parFormula_X0_0;
   string parFormula_X1_0;
   string parFormula_X1_1;
   string parFormula_Y0_0;
   string parFormula_Y1_0;
   string parFormula_Y1_1;
   double varMin;
   double varMax;
   vector<double> X0_0ftnParameters;
   vector<double> X1_0ftnParameters;
   vector<double> X1_1ftnParameters;
   vector<double> Y0_0ftnParameters;
   vector<double> Y1_0ftnParameters;
   vector<double> Y1_1ftnParameters;
   TF1* paraFtn_X0_0;
   TF1* paraFtn_X1_0;
   TF1* paraFtn_X1_1;
   TF1* paraFtn_Y0_0;
   TF1* paraFtn_Y1_0;
   TF1* paraFtn_Y1_1;
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
 void CalcXYshiftCorr(
     string sample,
	double nVtx,
	double pfMet,
	double &corx, double &cory);

 int ParVar();
 
 //! check
 //void checkIfOk();
 
 //! set functions
 vector<XYshiftDB> v_XYshiftDB;
 
private:
 //! variables
 void Definitions(const std::string& fLine);
 void Record(const std::string& fLine);
 void BuildFormula();

 XYshiftDB tmpDB;
 double ChangeFtnPointY;
 double ChangeFtnPointX;
 TF1* corrFormula_X0;
 TF1* corrFormula_X1;
 TF1* corrFormula_Y0;
 TF1* corrFormula_Y1;
 double par_X0_0, par_X1_0, par_X1_1;
 double par_Y0_0, par_Y1_0, par_Y1_1;

 float _met;
 float _met_phi;
 
};

//! constructor
metXYshift::metXYshift(string paraFile) {
  corrFormula_X0 = new TF1("corrFormula_X0","[0]*x");
  corrFormula_X1 = new TF1("corrFormula_X1","[0]+[1]*x");
  corrFormula_Y0 = new TF1("corrFormula_Y0","[0]*x");
  corrFormula_Y1 = new TF1("corrFormula_Y1","[0]+[1]*x");
  //cout<<"Parameter file is: "<<paraFile<<endl;
  std::ifstream input(paraFile.c_str());
  if( !input )
  {
    cout<<"parameter file is not opened: "<<paraFile<<endl;;
    exit(-1);
    //throw std::runtime_error("parameter file is not opened");
  }

  v_XYshiftDB.clear();

  myDB.sample="";
  myDB.mParVar.clear();
  myDB.parFormula_X0_0="";
  myDB.parFormula_X1_0="";
  myDB.parFormula_X1_1="";
  myDB.parFormula_Y0_0="";
  myDB.parFormula_Y1_0="";
  myDB.parFormula_Y1_1="";

  myDB.X0_0ftnParameters.clear();
  myDB.X1_0ftnParameters.clear();
  myDB.X1_1ftnParameters.clear();
  myDB.Y0_0ftnParameters.clear();
  myDB.Y1_0ftnParameters.clear();
  myDB.Y1_1ftnParameters.clear();

  myDB.paraFtn_X0_0=0;
  myDB.paraFtn_X1_0=0;
  myDB.paraFtn_X1_1=0;
  myDB.paraFtn_Y0_0=0;
  myDB.paraFtn_Y1_0=0;
  myDB.paraFtn_Y1_1=0;

  std::string line;
  std::string currentDefinitions = "";
  cout<<"getline from input file"<<endl;
  myDB.sample = "";
  while (std::getline(input,line))
  {
    std::string sample = getSection(line);
    std::string tmp = getDefinitions(line);
    //cout<<"sample is : "<<sample<<endl;
    // catch sample and save previous DB
    if (!sample.empty() && tmp.empty())
    {
      if(!myDB.sample.empty()) // there is a previous DB filled.
      {
	BuildFormula();
	v_XYshiftDB.push_back(myDB);

        myDB.sample="";
        myDB.mParVar.clear();
        myDB.parFormula_X0_0="";
        myDB.parFormula_X1_0="";
        myDB.parFormula_X1_1="";
        myDB.parFormula_Y0_0="";
        myDB.parFormula_Y1_0="";
        myDB.parFormula_Y1_1="";
	myDB.X0_0ftnParameters.clear();
	myDB.X1_0ftnParameters.clear();
	myDB.X1_1ftnParameters.clear();
	myDB.Y0_0ftnParameters.clear();
	myDB.Y1_0ftnParameters.clear();
	myDB.Y1_1ftnParameters.clear();
	myDB.paraFtn_X0_0=0;
	myDB.paraFtn_X1_0=0;
	myDB.paraFtn_X1_1=0;
	myDB.paraFtn_Y0_0=0;
	myDB.paraFtn_Y1_0=0;
	myDB.paraFtn_Y1_1=0;
      }
      myDB.sample = sample;
      continue;
    }
    if (!tmp.empty())
    {
      currentDefinitions = tmp;
      //cout<<"Definitions input: "<<currentDefinitions<<endl;
      Definitions(currentDefinitions);
      continue;
    }
    if( myDB.sample != "")
    {
      Record(line);
    }
  }
  BuildFormula();
  v_XYshiftDB.push_back(myDB); // last sample to be filled

}

void metXYshift::Definitions(const std::string& fLine)
{
  std::vector<std::string> tokens = getTokens(fLine);
  // corrType N_bin binVa.. var formula
  if (!tokens.empty())
  { 
    if (tokens.size() < 8) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): Great than or equal to 8 expected tokens:"<<tokens.size();
      handleError("metXYshift::Definitions",sserr.str());
    }
    // Num.o of Parameterization Variable
    unsigned nParVar = getUnsigned(tokens[0]);
    for(unsigned i=0;i<nParVar;i++)
    {
      myDB.mParVar.push_back(getSigned(tokens[1+i]));
    }
    myDB.parFormula_X0_0 = tokens[1+nParVar];
    myDB.parFormula_X1_0 = tokens[2+nParVar];
    myDB.parFormula_X1_1 = tokens[3+nParVar];
    myDB.parFormula_Y0_0 = tokens[4+nParVar];
    myDB.parFormula_Y1_0 = tokens[5+nParVar];
    myDB.parFormula_Y1_1 = tokens[6+nParVar];

    if (tokens.size() != nParVar+7 ) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): token size should be:"<<nParVar+7<<" but it is "<<tokens.size();
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
    if (tokens.size() < 6) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): "<<"three tokens expected, "<<tokens.size()<<" provided.";
      handleError("metXYshift::Record",sserr.str());
    }
    string Axis = tokens[0];
    myDB.varMin=getFloat(tokens[1]);
    myDB.varMax=getFloat(tokens[2]);
    unsigned nPar0 = getUnsigned(tokens[3]);
    if(Axis == "X0") // one para ftn
    {
      ChangeFtnPointX = myDB.varMax;
      for(unsigned i(0); i< nPar0 ;i++)
      {
	myDB.X0_0ftnParameters.push_back(getFloat(tokens[4+i]));
      }
      if(tokens.size()-4 != nPar0)
      {
        std::stringstream sserr;
        sserr<<"X0_0 total token size: "<<tokens.size();
	handleError("metXYshift::Record",sserr.str());
      }
    }
    else if(Axis == "X1")
    {
      for(unsigned i(0); i< nPar0 ;i++)
      {
	myDB.X1_0ftnParameters.push_back(getFloat(tokens[4+i]));
      }
      unsigned nPar1 = getUnsigned(tokens[4+nPar0]);
      for(unsigned i(0); i<nPar1; i++)
      {
	myDB.X1_1ftnParameters.push_back(getFloat(tokens[5+nPar0+i]));
      }
      if(tokens.size()-5 != nPar0 + nPar1)
      {
        std::stringstream sserr;
        sserr<<"X1_1 total token size: "<<tokens.size();
	handleError("metXYshift::Record",sserr.str());
      }
    }
    else if(Axis == "Y0") // one para ftn
    {
      ChangeFtnPointY = myDB.varMax;
      for(unsigned i(0); i< nPar0 ;i++)
      {
	myDB.Y0_0ftnParameters.push_back(getFloat(tokens[4+i]));
      }
      if(tokens.size()-4 != nPar0)
      {
        std::stringstream sserr;
        sserr<<"Y0_0 total token size: "<<tokens.size();
	handleError("metXYshift::Record",sserr.str());
      }
    }
    else if(Axis == "Y1")
    {
      for(unsigned i(0); i< nPar0 ;i++)
      {
	myDB.Y1_0ftnParameters.push_back(getFloat(tokens[4+i]));
      }
      unsigned nPar1 = getUnsigned(tokens[4+nPar0]);
      for(unsigned i(0); i<nPar1; i++)
      {
	myDB.Y1_1ftnParameters.push_back(getFloat(tokens[5+nPar0+i]));
      }
      if(tokens.size()-5 != nPar0 + nPar1)
      {
        std::stringstream sserr;
        sserr<<"Y1_1 total token size: "<<tokens.size();
	handleError("metXYshift::Record",sserr.str());
      }
      //myDB.paraFtn_y = new TF1("corrPy", myDB.parFormula.c_str());
    }else handleError("Record","record is not for met X or Y");

  }
}
      


//! set functions

void metXYshift::printPara() {
  cout<<"ChangeFtnPointX:"<<ChangeFtnPointX<<" ChangeFtnPointY:"<<ChangeFtnPointY<<endl;
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    XYshiftDB tmpDB=v_XYshiftDB[i];
    cout<<tmpDB.sample<<endl;
    cout<<" parVar: "<<tmpDB.mParVar[0]
      <<" paraFtn_X0_0: "<<tmpDB.parFormula_X0_0
      <<" paraFtn_X1_0: "<<tmpDB.parFormula_X1_0
      <<" paraFtn_X1_1: "<<tmpDB.parFormula_X1_1
      <<" paraFtn_Y0_0: "<<tmpDB.parFormula_Y0_0
      <<" paraFtn_Y1_0: "<<tmpDB.parFormula_Y1_0
      <<" paraFtn_Y1_1: "<<tmpDB.parFormula_Y1_1<<endl;
    //cout<<"met range: "<<tmpDB.metMin<<" - "<<tmpDB.metMax<<endl;
    cout<<"X parameters : ";
    for(unsigned j(0);j<tmpDB.X0_0ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.X0_0ftnParameters[j];
    }
    for(unsigned j(0);j<tmpDB.X1_0ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.X1_0ftnParameters[j];
    }
    for(unsigned j(0);j<tmpDB.X1_1ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.X1_1ftnParameters[j];
    }
    cout<<endl;
    cout<<" Para. conformation from formula: ";
    for(unsigned j(0);j<tmpDB.paraFtn_X0_0->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_X0_0->GetParameter(j);
    }
    for(unsigned j(0);j<tmpDB.paraFtn_X1_0->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_X1_0->GetParameter(j);
    }
    for(unsigned j(0);j<tmpDB.paraFtn_X1_1->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_X1_1->GetParameter(j);
    }
    cout<<endl;
    cout<<"Y parameters : ";
    for(unsigned j(0);j<tmpDB.Y0_0ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.Y0_0ftnParameters[j];
    }
    for(unsigned j(0);j<tmpDB.Y1_0ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.Y1_0ftnParameters[j];
    }
    for(unsigned j(0);j<tmpDB.Y1_1ftnParameters.size();j++)
    {
      cout<<" "<<tmpDB.Y1_1ftnParameters[j];
    }
    cout<<endl;
    cout<<" Para. conformation from formula: ";
    for(unsigned j(0);j<tmpDB.paraFtn_Y0_0->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_Y0_0->GetParameter(j);
    }
    for(unsigned j(0);j<tmpDB.paraFtn_Y1_0->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_Y1_0->GetParameter(j);
    }
    for(unsigned j(0);j<tmpDB.paraFtn_Y1_1->GetNpar();j++)
    {
      cout<<" "<<tmpDB.paraFtn_Y1_1->GetParameter(j);
    }
    cout<<endl;
  }
}
int metXYshift::ParVar(){
  XYshiftDB tmpDB=v_XYshiftDB[0];
  return tmpDB.mParVar[0];
}
void metXYshift::CalcXYshiftCorr(
    string sample,
    double shiftVar,
    double met,
    double &corx, double &cory
    ){
  corx = 0;
  cory = 0;
  bool bingo(0);
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    tmpDB=v_XYshiftDB[i];
    //cout<<"tmpDB.sample: "<<tmpDB.sample<<endl;
    // check met bin
    //if(met < tmpDB.metMin || met > tmpDB.metMax ) continue;
    if(tmpDB.sample == sample)
    {
      par_X0_0 = tmpDB.paraFtn_X0_0->Eval(met);
      par_X1_0 = tmpDB.paraFtn_X1_0->Eval(met);
      par_X1_1 = tmpDB.paraFtn_X1_1->Eval(met);
      par_Y0_0 = tmpDB.paraFtn_Y0_0->Eval(met);
      par_Y1_0 = tmpDB.paraFtn_Y1_0->Eval(met);
      par_Y1_1 = tmpDB.paraFtn_Y1_1->Eval(met);

      corrFormula_X0->SetParameter(0,par_X0_0);
      corrFormula_X1->SetParameter(0,par_X1_0);
      corrFormula_X1->SetParameter(1,par_X1_1);
      corrFormula_Y0->SetParameter(0,par_Y0_0);
      corrFormula_Y1->SetParameter(0,par_Y1_0);
      corrFormula_Y1->SetParameter(1,par_Y1_1);

      if(shiftVar < ChangeFtnPointX){
        corx -= corrFormula_X0->Eval(shiftVar);
        cory -= corrFormula_Y0->Eval(shiftVar);
      }else{
        corx -= corrFormula_X1->Eval(shiftVar);
        cory -= corrFormula_Y1->Eval(shiftVar);
      }
      //corx -= tmpDB.paraFtn_x->Eval(shiftVar);
      //cory -= tmpDB.paraFtn_x->Eval(shiftVar);
      //cout<<"hEtaPlus_weight: "<<hEtaPlus_weight<<endl;
      //cout<<"corx: "<<corx<<endl;
      bingo = 1;
    }
    else continue;
  }
  if( !bingo)
  {
      std::stringstream sserr;
      sserr<<"This sample is not reserved: "<<tmpDB.sample;
      handleError("metXYshift::CalcXYshiftCorr",sserr.str());
  }

}

void metXYshift::BuildFormula(){

        myDB.paraFtn_X0_0 = new TF1("parFtn_x0_0", myDB.parFormula_X0_0.c_str());
        myDB.paraFtn_X1_0 = new TF1("parFtn_x0_1", myDB.parFormula_X1_0.c_str());
        myDB.paraFtn_X1_1 = new TF1("parFtn_x1_1", myDB.parFormula_X1_1.c_str());
        myDB.paraFtn_Y0_0 = new TF1("parFtn_y0_0", myDB.parFormula_Y0_0.c_str());
        myDB.paraFtn_Y1_0 = new TF1("parFtn_y1_0", myDB.parFormula_Y1_0.c_str());
        myDB.paraFtn_Y1_1 = new TF1("parFtn_y1_1", myDB.parFormula_Y1_1.c_str());

        for(int j(0); j<myDB.X0_0ftnParameters.size();j++)
        {
          myDB.paraFtn_X0_0->SetParameter(j, myDB.X0_0ftnParameters[j]);
        }
        for(int j(0); j<myDB.X1_0ftnParameters.size();j++)
        {
          myDB.paraFtn_X1_0->SetParameter(j, myDB.X1_0ftnParameters[j]);
        }
        for(int j(0); j<myDB.X1_1ftnParameters.size();j++)
        {
          myDB.paraFtn_X1_1->SetParameter(j, myDB.X1_1ftnParameters[j]);
        }
        for(int j(0); j<myDB.Y0_0ftnParameters.size();j++)
        {
          myDB.paraFtn_Y0_0->SetParameter(j, myDB.Y0_0ftnParameters[j]);
        }
        for(int j(0); j<myDB.Y1_0ftnParameters.size();j++)
        {
          myDB.paraFtn_Y1_0->SetParameter(j, myDB.Y1_0ftnParameters[j]);
        }
        for(int j(0); j<myDB.Y1_1ftnParameters.size();j++)
        {
          myDB.paraFtn_Y1_1->SetParameter(j, myDB.Y1_1ftnParameters[j]);
        }

}
