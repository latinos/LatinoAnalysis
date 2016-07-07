
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
   string section;
   int ptclType;
   vector<string> mBinVar;
   vector<int> mParVar;
   string mFormula;
   double metXetaMin;
   double metXetaMax;
   double metYetaMin;
   double metYetaMax;
   vector<double> metXparameters;
   vector<double> metYparameters;
   //TF1* formula_x;
   //TF1* formula_y;
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
	double hEtaPlus_counts,
	double hEtaMinus_counts,
	double h0Barrel_counts,
	double h0EndcapPlus_counts,
	double h0EndcapMinus_counts,
	double gammaBarrel_counts,
	double gammaEndcapPlus_counts,
	double gammaEndcapMinus_counts,
	double hHFPlus_counts,
	double hHFMinus_counts,
	double egammaHFPlus_counts,
	double egammaHFMinus_counts,
	double &corx, double &cory);
 
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
 TF1* formula_hEtaPlus_x;
 TF1* formula_hEtaPlus_y;

 TF1* formula_hEtaMinus_x;
 TF1* formula_hEtaMinus_y;

 TF1* formula_h0Barrel_x;
 TF1* formula_h0Barrel_y;

 TF1* formula_h0EndcapPlus_x;
 TF1* formula_h0EndcapPlus_y;

 TF1* formula_h0EndcapMinus_x;
 TF1* formula_h0EndcapMinus_y;

 TF1* formula_gammaBarrel_x;
 TF1* formula_gammaBarrel_y;

 TF1* formula_gammaEndcapPlus_x;
 TF1* formula_gammaEndcapPlus_y;

 TF1* formula_gammaEndcapMinus_x;
 TF1* formula_gammaEndcapMinus_y;

 TF1* formula_hHFPlus_x;
 TF1* formula_hHFPlus_y;

 TF1* formula_hHFMinus_x;
 TF1* formula_hHFMinus_y;

 TF1* formula_egammaHFPlus_x;
 TF1* formula_egammaHFPlus_y;

 TF1* formula_egammaHFMinus_x;
 TF1* formula_egammaHFMinus_y;


 float _met;
 float _met_phi;
 
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

  myDB.section="";
  myDB.ptclType=0;
  myDB.mBinVar.clear();
  myDB.mParVar.clear();
  myDB.mFormula="";
  myDB.metXparameters.clear();
  myDB.metYparameters.clear();

  std::string line;
  std::string currentDefinitions = "";
  cout<<"getline from input file"<<endl;
  myDB.section = "";
  while (std::getline(input,line))
  {
    std::string section = getSection(line);
    std::string tmp = getDefinitions(line);
    //cout<<"section is : "<<section<<endl;
    // catch section and save previous DB
    if (!section.empty() && tmp.empty())
    {
      if(!myDB.section.empty()) // there is a previous DB filled.
      {
	v_XYshiftDB.push_back(myDB);
        myDB.section="";
        myDB.ptclType=0;
        myDB.mBinVar.clear();
        myDB.mParVar.clear();
        myDB.mFormula="";
	myDB.metXetaMin=0;
	myDB.metXetaMax=0;
	myDB.metYetaMin=0;
	myDB.metYetaMax=0;
	myDB.metXparameters.clear();
	myDB.metYparameters.clear();
      }
      myDB.section = section;
      continue;
    }
    if (!tmp.empty())
    {
      currentDefinitions = tmp;
      Definitions(currentDefinitions);
      continue;
    }
    if( myDB.section != "")
    {
      Record(line);
    }
  }
  v_XYshiftDB.push_back(myDB); // last section to be filled

  BuildFormula();
}

void metXYshift::Definitions(const std::string& fLine)
{
  std::vector<std::string> tokens = getTokens(fLine);
  // corrType N_bin binVa.. var formula
  if (!tokens.empty())
  { 
    if (tokens.size() < 6) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): Great than or equal to 6 expected tokens:"<<tokens.size();
      handleError("metXYshift::Definitions",sserr.str());
    }
    // No. of Bin Variable
    myDB.ptclType = getSigned(tokens[0]);
    unsigned nBinVar = getUnsigned(tokens[1]);
    for(unsigned i=0;i<nBinVar;i++)
    {
      myDB.mBinVar.push_back(tokens[i+2]);
    }
    // Num.o of Parameterization Variable
    unsigned nParVar = getUnsigned(tokens[nBinVar+2]);
    for(unsigned i=0;i<nParVar;i++)
    {
      myDB.mParVar.push_back(getSigned(tokens[nBinVar+3+i]));
    }
    myDB.mFormula = tokens[nParVar+nBinVar+3];
    if (tokens.size() != nParVar+nBinVar+4 ) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): token size should be:"<<nParVar+nBinVar+3<<" but it is "<<tokens.size();
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
    if(Axis == "X")
    {
      myDB.metXetaMin = getFloat(tokens[1]);
      myDB.metXetaMax = getFloat(tokens[2]);
    }
    else if(Axis == "Y")
    {
      //myDB.formula_y = new TF1("corrPy", myDB.mFormula.c_str());
      myDB.metYetaMin = getFloat(tokens[1]);
      myDB.metYetaMax = getFloat(tokens[2]);
    }else handleError("Record","record is not for met X or Y");

    unsigned nParam = getUnsigned(tokens[2+1]);
    if (nParam != tokens.size()-(2+2)) 
    {
      std::stringstream sserr;
      sserr<<"(line "<<fLine<<"): "<<tokens.size()-(2+1)<<" parameters, but nParam="<<nParam<<".";
      handleError("metXYshift::Record",sserr.str());
    }
    for (unsigned i = (2+2); i < tokens.size(); ++i)
    {
      if(Axis == "X")
      {
	myDB.metXparameters.push_back(getFloat(tokens[i]));
        //myDB.formula_x->SetParameter( i,getFloat(tokens[i]) );
      }
      if(Axis == "Y")
      {
	myDB.metYparameters.push_back(getFloat(tokens[i]));
        //myDB.formula_y->SetParameter( i,getFloat(tokens[i]) );
      }
    }
  }
}
      


//! set functions

void metXYshift::printPara() {
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    XYshiftDB tmpDB=v_XYshiftDB[i];
    cout<<tmpDB.section<<endl;
    cout<<"ptclType: "<<tmpDB.ptclType<<" parVar: "<<tmpDB.mParVar[0]
      <<" formula: "<<tmpDB.mFormula<<endl;
    cout<<"X "<<tmpDB.metXetaMin<<" "<<tmpDB.metXetaMax<<" "<<endl;
    for(unsigned j(0);j<tmpDB.metXparameters.size();j++)
    {
      cout<<" "<<tmpDB.metXparameters[j];
    }
    cout<<endl;
    for(unsigned j(0);j<tmpDB.metYparameters.size();j++)
    {
      cout<<" "<<tmpDB.metYparameters[j];
    }
    cout<<endl;
  }
}
void metXYshift::CalcXYshiftCorr(
	double hEtaPlus_counts,
	double hEtaMinus_counts,
	double h0Barrel_counts,
	double h0EndcapPlus_counts,
	double h0EndcapMinus_counts,
	double gammaBarrel_counts,
	double gammaEndcapPlus_counts,
	double gammaEndcapMinus_counts,
	double hHFPlus_counts,
	double hHFMinus_counts,
	double egammaHFPlus_counts,
	double egammaHFMinus_counts,
	double &corx, double &cory
    ){
  corx = 0;
  cory = 0;
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    tmpDB=v_XYshiftDB[i];
    //cout<<"tmpDB.section: "<<tmpDB.section<<endl;
    if(tmpDB.section == "hEtaPlus")
    {
      //cout<<"hEtaPlus_counts: "<<hEtaPlus_counts<<endl;
      corx -= formula_hEtaPlus_x->Eval(hEtaPlus_counts);
      cory -= formula_hEtaPlus_y->Eval(hEtaPlus_counts);
      //cout<<"corx: "<<corx<<endl;
    }
    else if(tmpDB.section == "hEtaMinus")
    {
      corx -= formula_hEtaMinus_x->Eval(hEtaMinus_counts);
      cory -= formula_hEtaMinus_y->Eval(hEtaMinus_counts);
    }
    else if(tmpDB.section == "h0Barrel")
    {
      corx -= formula_h0Barrel_x->Eval(h0Barrel_counts);
      cory -= formula_h0Barrel_y->Eval(h0Barrel_counts);
    }
    else if(tmpDB.section == "h0EndcapPlus")
    {
      corx -= formula_h0EndcapPlus_x->Eval(h0EndcapPlus_counts);
      cory -= formula_h0EndcapPlus_y->Eval(h0EndcapPlus_counts);
    }
    else if(tmpDB.section == "h0EndcapMinus")
    {
      corx -= formula_h0EndcapMinus_x->Eval(h0EndcapMinus_counts);
      cory -= formula_h0EndcapMinus_y->Eval(h0EndcapMinus_counts);
    }
    else if(tmpDB.section == "gammaBarrel")
    {
      corx -= formula_gammaBarrel_x->Eval(gammaBarrel_counts);
      cory -= formula_gammaBarrel_y->Eval(gammaBarrel_counts);
    }
    else if(tmpDB.section == "gammaEndcapPlus")
    {
      corx -= formula_gammaEndcapPlus_x->Eval(gammaEndcapPlus_counts);
      cory -= formula_gammaEndcapPlus_y->Eval(gammaEndcapPlus_counts);
    }
    else if(tmpDB.section == "gammaEndcapMinus")
    {
      corx -= formula_gammaEndcapMinus_x->Eval(gammaEndcapMinus_counts);
      cory -= formula_gammaEndcapMinus_y->Eval(gammaEndcapMinus_counts);
    }
    else if(tmpDB.section == "hHFPlus")
    {
      corx -= formula_hHFPlus_x->Eval(hHFPlus_counts);
      cory -= formula_hHFPlus_y->Eval(hHFPlus_counts);
    }
    else if(tmpDB.section == "hHFMinus")
    {
      corx -= formula_hHFMinus_x->Eval(hHFMinus_counts);
      cory -= formula_hHFMinus_y->Eval(hHFMinus_counts);
    }
    else if(tmpDB.section == "egammaHFPlus")
    {
      corx -= formula_egammaHFPlus_x->Eval(egammaHFPlus_counts);
      cory -= formula_egammaHFPlus_y->Eval(egammaHFPlus_counts);
    }
    else if(tmpDB.section == "egammaHFMinus")
    {
      corx -= formula_egammaHFMinus_x->Eval(egammaHFMinus_counts);
      cory -= formula_egammaHFMinus_y->Eval(egammaHFMinus_counts);
    }
    else
    {
      std::stringstream sserr;
      sserr<<"This section is not reserved: "<<tmpDB.section;
      handleError("metXYshift::CalcXYshiftCorr",sserr.str());
    }
  }
}

void metXYshift::BuildFormula(){
  for(unsigned i(0);i<v_XYshiftDB.size();i++)
  {
    tmpDB=v_XYshiftDB[i];
    //cout<<"tmpDB.section: "<<tmpDB.section<<endl;
    if(tmpDB.section == "hEtaPlus")
    {
      //cout<<"hEtaPlus_counts: "<<hEtaPlus_counts<<endl;
      formula_hEtaPlus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_hEtaPlus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_hEtaPlus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_hEtaPlus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "hEtaMinus")
    {
      formula_hEtaMinus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_hEtaMinus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_hEtaMinus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_hEtaMinus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "h0Barrel")
    {
      formula_h0Barrel_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_h0Barrel_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_h0Barrel_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_h0Barrel_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "h0EndcapPlus")
    {
      formula_h0EndcapPlus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_h0EndcapPlus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_h0EndcapPlus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_h0EndcapPlus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "h0EndcapMinus")
    {
      formula_h0EndcapMinus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_h0EndcapMinus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_h0EndcapMinus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_h0EndcapMinus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "gammaBarrel")
    {
      formula_gammaBarrel_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_gammaBarrel_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_gammaBarrel_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_gammaBarrel_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "gammaEndcapPlus")
    {
      formula_gammaEndcapPlus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_gammaEndcapPlus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_gammaEndcapPlus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_gammaEndcapPlus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "gammaEndcapMinus")
    {
      formula_gammaEndcapMinus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_gammaEndcapMinus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_gammaEndcapMinus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_gammaEndcapMinus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "hHFPlus")
    {
      formula_hHFPlus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_hHFPlus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_hHFPlus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_hHFPlus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "hHFMinus")
    {
      formula_hHFMinus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_hHFMinus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_hHFMinus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_hHFMinus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "egammaHFPlus")
    {
      formula_egammaHFPlus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_egammaHFPlus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_egammaHFPlus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_egammaHFPlus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else if(tmpDB.section == "egammaHFMinus")
    {
      formula_egammaHFMinus_x = new TF1("corrPx", tmpDB.mFormula.c_str());
      formula_egammaHFMinus_y = new TF1("corrPy", tmpDB.mFormula.c_str());
      for(int j(0); j<tmpDB.metXparameters.size();j++)
      {
        formula_egammaHFMinus_x->SetParameter(j, tmpDB.metXparameters[j]);
        formula_egammaHFMinus_y->SetParameter(j, tmpDB.metYparameters[j]);
      }
    }
    else
    {
      std::stringstream sserr;
      sserr<<"This section is not reserved: "<<tmpDB.section;
      handleError("metXYshift::CalcXYshiftCorr",sserr.str());
    }
  }
}
