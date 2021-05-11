#include <iostream>
using namespace std;
/*
class RooNDKeysPdfAnalyticalAnalyticalAnalyticalAnalytical : public RooNDKeysPdfAnalyticalAnalyticalAnalytical {
  
  public:
  RooNDKeysPdfAnalyticalAnalyticalAnalyticalAnalytical( const char *name, const char *title, const RooArgList &varList, const RooDataSet &data,
                          TString options = "ma", Double_t rho = 1, Double_t nSigma = 3, Bool_t rotate = kTRUE,
                          Bool_t sortInput = kTRUE) : RooNDKeysPdfAnalyticalAnalyticalAnalytical(name, title, varList, data, options, rho, nSigma, rotate, sortInput) {};

  virtual Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName) const
   {
    cout << "CIAOOOOO" << endl;      
    Int_t code=0;
    if (matchArgs(allVars,analVars,RooArgSet(_varList))) { code=1; }
      return code;
   };
                        

  ClassDef(RooNDKeysPdfAnalyticalAnalyticalAnalyticalAnalytical, 1) 
};

*/
/*****************************************************************************
 * Project: RooFit                                                           *
 * Package: RooFitModels                                                     *
 *    File: $Id: RooNDKeysPdf.h 44368 2012-05-30 15:38:44Z axel $
 * Authors:                                                                  *
 *   Max Baak, CERN, mbaak@cern.ch *
 *                                                                           *
 * Copyright (c) 2000-2005, Regents of the University of California          *
 *                          and Stanford University. All rights reserved.    *
 *                                                                           *
 * Redistribution and use in source and binary forms,                        *
 * with or without modification, are permitted according to the terms        *
 * listed in LICENSE (http://roofit.sourceforge.net/license.txt)             *
 *****************************************************************************/
#ifndef ROO_NDKEYS_PDF_analytical
#define ROO_NDKEYS_PDF_analytical

#include "RooAbsPdf.h"
#include "RooNDKeysPdf.h"
#include "RooRealProxy.h"
#include "RooSetProxy.h"
#include "RooRealConstant.h"
#include "RooDataSet.h"
#include "TH1.h"
#include "TAxis.h"
#include "TVectorD.h"
#include "TMatrixD.h"
#include "TMatrixDSym.h"
#include <map>
#include <vector>
#include <string>

class RooRealVar;
class RooArgList;
class RooArgSet;
class RooChangeTracker;

#ifndef __CINT__
//class VecVecDouble : public std::vector<std::vector<Double_t> >  { } ;
//class VecTVecDouble : public std::vector<TVectorD> { } ;
typedef std::pair<Int_t, VecVecDouble::iterator > iiPair;
typedef std::vector< iiPair > iiVec;
typedef std::pair<Int_t, VecTVecDouble::iterator > itPair;
typedef std::vector< itPair > itVec;
#else
class itPair ;
#endif

class RooNDKeysPdfAnalytical : public RooAbsPdf {

public:

  enum Mirror {NoMirror, MirrorLeft, MirrorRight, MirrorBoth,
               MirrorAsymLeft, MirrorAsymLeftRight,
               MirrorAsymRight, MirrorLeftAsymRight,
               MirrorAsymBoth };

  RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
               TString options = "ma", Double_t rho = 1, Double_t nSigma = 3, Bool_t rotate = kTRUE,
               Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const TH1 &hist, TString options = "ma",
               Double_t rho = 1, Double_t nSigma = 3, Bool_t rotate = kTRUE, Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
               const TVectorD &rho, TString options = "ma", Double_t nSigma = 3, Bool_t rotate = kTRUE,
               Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
               const RooArgList &rhoList, TString options = "ma", Double_t nSigma = 3, Bool_t rotate = kTRUE,
               Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const TH1 &hist,
               const RooArgList &rhoList, TString options = "ma", Double_t nSigma = 3, Bool_t rotate = kTRUE,
               Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, RooAbsReal &x, const RooAbsData &data, Mirror mirror = NoMirror,
               Double_t rho = 1, Double_t nSigma = 3, Bool_t rotate = kTRUE, Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const char *name, const char *title, RooAbsReal &x, RooAbsReal &y, const RooAbsData &data,
               TString options = "ma", Double_t rho = 1.0, Double_t nSigma = 3, Bool_t rotate = kTRUE,
               Bool_t sortInput = kTRUE);

  RooNDKeysPdfAnalytical(const RooNDKeysPdfAnalytical& other, const char* name=0);
  virtual ~RooNDKeysPdfAnalytical();

  virtual TObject* clone(const char* newname) const { return new RooNDKeysPdfAnalytical(*this,newname); }

  Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ;
  Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;

  inline void fixShape(Bool_t fix) {
    createPdf(kFALSE);
    _fixedShape=fix;
  }

  TMatrixD getWeights(const int &k) const;

  struct BoxInfo {
    Bool_t filled;
    Bool_t netFluxZ;
    Double_t nEventsBW;
    Double_t nEventsBMSW;
    std::vector<Double_t> xVarLo, xVarHi;
    std::vector<Double_t> xVarLoM3s, xVarLoP3s, xVarHiM3s, xVarHiP3s;
    std::map<Int_t,Bool_t> bpsIdcs;
    std::vector<Int_t> sIdcs;
    std::vector<Int_t> bIdcs;
    std::vector<Int_t> bmsIdcs;
  } ;

protected:

  RooListProxy _varList ;
  TIterator* _varItr ;   //! do not persist

  RooListProxy _rhoList;
  TIterator *_rhoItr; //! do not persist

  Double_t evaluate() const;

  void createPdf(Bool_t firstCall = kTRUE) const;
  void setOptions() const;
  void initialize() const;
  void loadDataSet(Bool_t firstCall) const;
  void mirrorDataSet() const;
  void loadWeightSet() const;
  void calculateShell(BoxInfo *bi) const;
  void calculatePreNorm(BoxInfo *bi) const;
  void sortDataIndices(BoxInfo *bi = 0) const;
  void calculateBandWidth() const;
  Double_t gauss(std::vector<Double_t> &x, std::vector<std::vector<Double_t>> &weights) const;
  void loopRange(std::vector<Double_t> &x, std::map<Int_t, Bool_t> &ibMap) const;
  void boxInfoInit(BoxInfo *bi, const char *rangeName, Int_t code) const;
  RooDataSet *createDatasetFromHist(const RooArgList &varList, const TH1 &hist) const;
  void updateRho() const;

  mutable RooDataSet *_dataP; //! do not persist
  const RooAbsData &_data;    //!
  mutable TString _options;
  mutable Double_t _widthFactor;
  mutable Double_t _nSigma;

  mutable Bool_t _fixedShape;
  mutable Bool_t _mirror;
  mutable Bool_t _debug;
  mutable Bool_t _verbose;

  mutable Double_t _sqrt2pi;
  mutable Int_t _nDim;
  mutable Int_t _nEvents;
  mutable Int_t _nEventsM;
  mutable Double_t _nEventsW;
  mutable Double_t _d;
  mutable Double_t _n;

  // cached info on variable

  mutable std::vector<std::vector<Double_t> > _dataPts;
  mutable std::vector<TVectorD> _dataPtsR;
  mutable std::vector<std::vector<Double_t> > _weights0;
  mutable std::vector<std::vector<Double_t> > _weights1;
  mutable std::vector<std::vector<Double_t> >* _weights; //!

#ifndef __CINT__
  mutable std::vector<iiVec> _sortIdcs;   //!
  mutable std::vector<itVec> _sortTVIdcs; //!
#endif

  mutable std::vector<std::string> _varName;
  mutable std::vector<Double_t> _rho;
  mutable RooArgSet _dataVars;
  mutable std::vector<Double_t> _x;
  mutable std::vector<Double_t> _x0, _x1, _x2;
  mutable std::vector<Double_t> _mean, _sigma;
  mutable std::vector<Double_t> _xDatLo, _xDatHi;
  mutable std::vector<Double_t> _xDatLo3s, _xDatHi3s;

  mutable Bool_t _netFluxZ;
  mutable Double_t _nEventsBW;
  mutable Double_t _nEventsBMSW;
  mutable std::vector<Double_t> _xVarLo, _xVarHi;
  mutable std::vector<Double_t> _xVarLoM3s, _xVarLoP3s, _xVarHiM3s, _xVarHiP3s;
  mutable std::map<Int_t,Bool_t> _bpsIdcs;
  mutable std::map<Int_t, Bool_t> _ibNoSort;
  mutable std::vector<Int_t> _sIdcs;
  mutable std::vector<Int_t> _bIdcs;
  mutable std::vector<Int_t> _bmsIdcs;

  mutable std::map<std::pair<std::string,int>,BoxInfo*> _rangeBoxInfo ;
  mutable BoxInfo _fullBoxInfo ;

  mutable std::vector<Int_t> _idx;
  mutable Double_t _minWeight;
  mutable Double_t _maxWeight;
  mutable std::map<Int_t,Double_t> _wMap;

  mutable TMatrixDSym* _covMat;
  mutable TMatrixDSym* _corrMat;
  mutable TMatrixD* _rotMat;
  mutable TVectorD* _sigmaR;
  mutable TVectorD* _dx;
  mutable Double_t _sigmaAvgR;

  mutable Bool_t _rotate;
  mutable Bool_t _sortInput;
  mutable Int_t _nAdpt;

  mutable RooChangeTracker *_tracker; //! do not persist

  public:
  /// sorter function
  struct SorterTV_L2H {
    Int_t idx;

    SorterTV_L2H (Int_t index) : idx(index) {}
    bool operator() (const itPair& a, const itPair& b) {
      const TVectorD& aVec = *(a.second);
      const TVectorD& bVec = *(b.second);
      return (aVec[idx]<bVec[idx]);
    }
  };
  void checkInitWeights() const {
     if (_weights == &_weights0 || _weights == &_weights1)
       return;
     const_cast<RooNDKeysPdfAnalytical*>(this)->calculateBandWidth();
   }

  //ClassDef(RooNDKeysPdfAnalytical, 2) // General N-dimensional non-parametric kernel estimation p.d.f
};

#endif


/*****************************************************************************
 * Project: RooFit                                                           *
 * Package: RooFitModels                                                     *
 *    File: $Id: RooNDKeysPdfAnalytical.cxx 31258 2009-11-17 22:41:06Z wouter $
 * Authors:                                                                  *
 *   Max Baak, CERN, mbaak@cern.ch *
 *                                                                           *
 * Redistribution and use in source and binary forms,                        *
 * with or without modification, are permitted according to the terms        *
 * listed in LICENSE (http://roofit.sourceforge.net/license.txt)             *
 *****************************************************************************/

/** \class RooNDKeysPdfAnalytical
    \ingroup Roofit

Generic N-dimensional implementation of a kernel estimation p.d.f. This p.d.f. models the distribution
of an arbitrary input dataset as a superposition of Gaussian kernels, one for each data point,
each contributing 1/N to the total integral of the p.d.f.
If the 'adaptive mode' is enabled, the width of the Gaussian is adaptively calculated from the
local density of events, i.e. narrow for regions with high event density to preserve details and
wide for regions with log event density to promote smoothness. The details of the general algorithm
are described in the following paper:
Cranmer KS, Kernel Estimation in High-Energy Physics.
            Computer Physics Communications 136:198-207,2001 - e-Print Archive: hep ex/0011057
For multi-dimensional datasets, the kernels are modeled by multidimensional Gaussians. The kernels are
constructed such that they reflect the correlation coefficients between the observables
in the input dataset.
**/

#include <iostream>
#include <algorithm>
#include <string>

#include "TMath.h"
#include "TMatrixDSymEigen.h"
//#include "RooNDKeysPdfAnalytical.h"
#include "RooAbsReal.h"
#include "RooRealVar.h"
#include "RooRandom.h"
#include "RooHist.h"
#include "RooMsgService.h"
#include "RooChangeTracker.h"

#include "TError.h"

using namespace std;

//ClassImp(RooNDKeysPdfAnalytical);

////////////////////////////////////////////////////////////////////////////////
/// Construct N-dimensional kernel estimation p.d.f. in observables 'varList'
/// from dataset 'data'. Options can be
///
///  - 'a' = Use adaptive kernels (width varies with local event density)
///  - 'm' = Mirror data points over observable boundaries. Improves modeling
///         behavior at edges for distributions that are not close to zero
///         at edge
///  - 'd' = Debug flag
///  - 'v' = Verbose flag
///
/// The parameter rho (default = 1) provides an overall scale factor that can
/// be applied to the bandwith calculated for each kernel. The nSigma parameter
/// determines the size of the box that is used to search for contributing kernels
/// around a given point in observable space. The nSigma parameters is used
/// in case of non-adaptive bandwidths and for the 1st non-adaptive pass for
/// the calculation of adaptive keys p.d.f.s.
///
/// The optional weight arguments allows to specify an observable or function
/// expression in observables that specifies the weight of each event.

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
                           TString options, Double_t rho, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(0), _data(data), _options(options), _widthFactor(rho),
     _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput), _nAdpt(1), _tracker(0)
{
  // Constructor
  _varItr    = _varList.createIterator() ;
  _rhoItr = _rhoList.createIterator();

  TIterator* varItr = varList.createIterator() ;
  RooAbsArg* var ;
  for (Int_t i=0; (var = (RooAbsArg*)varItr->Next()); ++i) {
    if (!dynamic_cast<RooAbsReal*>(var)) {
      coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: variable " << var->GetName()
             << " is not of type RooAbsReal" << endl ;
      R__ASSERT(0) ;
    }
    _varList.add(*var) ;
    _varName.push_back(var->GetName());
  }
  delete varItr ;

  createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Constructor

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const TH1 &hist,
                           TString options, Double_t rho, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(createDatasetFromHist(varList, hist)), _data(*_dataP),
     _options(options), _widthFactor(rho), _nSigma(nSigma), _weights(&_weights0), _rotate(rotate),
     _sortInput(sortInput), _nAdpt(1), _tracker(0)
{
   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   TIterator *varItr = varList.createIterator();
   RooAbsArg *var;
   for (Int_t i = 0; (var = (RooAbsArg *)varItr->Next()); ++i) {
      if (!dynamic_cast<RooAbsReal *>(var)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: variable " << var->GetName()
                               << " is not of type RooAbsReal" << endl;
         assert(0);
      }
      _varList.add(*var);
      _varName.push_back(var->GetName());
   }
   delete varItr;

   createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Constructor

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
                           const TVectorD &rho, TString options, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(0), _data(data), _options(options), _widthFactor(-1.0),
     _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput), _nAdpt(1), _tracker(0)
{
  _varItr    = _varList.createIterator() ;
  _rhoItr = _rhoList.createIterator();

  TIterator* varItr = varList.createIterator() ;
  RooAbsArg* var ;
  for (Int_t i=0; (var = (RooAbsArg*)varItr->Next()); ++i) {
    if (!dynamic_cast<RooAbsReal*>(var)) {
       coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: variable " << var->GetName()
                             << " is not of type RooAbsReal" << endl;
       R__ASSERT(0);
    }
    _varList.add(*var) ;
    _varName.push_back(var->GetName());
  }
  delete varItr ;

  // copy rho widths
  if( _varList.getSize() != rho.GetNrows() ) {
     coutE(InputArguments)
        << "ERROR:  RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical() : The vector-size of rho is different from that of varList."
        << "Unable to create the PDF." << endl;
     R__ASSERT(_varList.getSize() == rho.GetNrows());
  }

  // negative width factor will serve as a switch in initialize()
  // negative value means that a vector has been provided as input,
  // and that _rho has already been set ...
  _rho.resize( rho.GetNrows() );
  for (Int_t j = 0; j < rho.GetNrows(); j++) {
     _rho[j] = rho[j]; /*cout<<"RooNDKeysPdfAnalytical ctor, _rho["<<j<<"]="<<_rho[j]<<endl;*/
  }

  createPdf(); // calls initialize ...
}

////////////////////////////////////////////////////////////////////////////////
/// Backward compatibility constructor for (1-dim) RooKeysPdf. If you are a new user,
/// please use the first constructor form.

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const RooAbsData &data,
                           const RooArgList &rhoList, TString options, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(0), _data(data), _options(options), _widthFactor(-1.0),
     _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput), _nAdpt(1)
{
   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   TIterator *varItr = varList.createIterator();
   RooAbsArg *var;
   for (Int_t i = 0; (var = (RooAbsArg *)varItr->Next()); ++i) {
      if (!dynamic_cast<RooAbsReal *>(var)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: variable " << var->GetName()
                               << " is not of type RooAbsReal" << endl;
         assert(0);
      }
      _varList.add(*var);
      _varName.push_back(var->GetName());
   }
   delete varItr;

   TIterator *rhoItr = rhoList.createIterator();
   RooAbsArg *rho;
   _rho.resize(rhoList.getSize(), 1.0);

   for (Int_t i = 0; (rho = (RooAbsArg *)rhoItr->Next()); ++i) {
      if (!dynamic_cast<RooAbsReal *>(rho)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: parameter " << rho->GetName()
                               << " is not of type RooRealVar" << endl;
         assert(0);
      }
      _rhoList.add(*rho);
      _rho[i] = (dynamic_cast<RooAbsReal *>(rho))->getVal();
   }
   delete rhoItr;

   // copy rho widths
   if ((_varList.getSize() != _rhoList.getSize())) {
      coutE(InputArguments) << "ERROR:  RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical() : The size of rhoList is different from varList."
                            << "Unable to create the PDF." << endl;
      assert(_varList.getSize() == _rhoList.getSize());
   }

   // keep track of changes in rho parameters
   _tracker = new RooChangeTracker("tracker", "track rho parameters", _rhoList, true); // check for value updates
   (void)_tracker->hasChanged(true); // first evaluation always true for new parameters (?)

   createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Constructor

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, const RooArgList &varList, const TH1 &hist,
                           const RooArgList &rhoList, TString options, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(createDatasetFromHist(varList, hist)), _data(*_dataP),
     _options(options), _widthFactor(-1), _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput),
     _nAdpt(1)
{
   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   TIterator *varItr = varList.createIterator();
   RooAbsArg *var;
   for (Int_t i = 0; (var = (RooAbsArg *)varItr->Next()); ++i) {
      if (!dynamic_cast<RooAbsReal *>(var)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: variable " << var->GetName()
                               << " is not of type RooAbsReal" << endl;
         assert(0);
      }
      _varList.add(*var);
      _varName.push_back(var->GetName());
   }
   delete varItr;

   // copy rho widths
   TIterator *rhoItr = rhoList.createIterator();
   RooAbsArg *rho;
   _rho.resize(rhoList.getSize(), 1.0);

   for (Int_t i = 0; (rho = (RooAbsArg *)rhoItr->Next()); ++i) {
      if (!dynamic_cast<RooAbsReal *>(rho)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::ctor(" << GetName() << ") ERROR: parameter " << rho->GetName()
                               << " is not of type RooRealVar" << endl;
         assert(0);
      }
      _rhoList.add(*rho);
      _rho[i] = (dynamic_cast<RooAbsReal *>(rho))->getVal();
   }
   delete rhoItr;

   if ((_varList.getSize() != _rhoList.getSize())) {
      coutE(InputArguments) << "ERROR:  RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical() : The size of rhoList is different from varList."
                            << "Unable to create the PDF." << endl;
      assert(_varList.getSize() == _rhoList.getSize());
   }

   // keep track of changes in rho parameters
   _tracker = new RooChangeTracker("tracker", "track rho parameters", _rhoList, true); // check for value updates
   (void)_tracker->hasChanged(true); // first evaluation always true for new parameters (?)

   createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Constructor

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, RooAbsReal &x, const RooAbsData &data, Mirror mirror,
                           Double_t rho, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(0), _data(data), _options("a"), _widthFactor(rho),
     _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput), _nAdpt(1), _tracker(0)
{
   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   _varList.add(x);
   _varName.push_back(x.GetName());

   if (mirror != NoMirror) {
      if (mirror != MirrorBoth)
         coutW(InputArguments) << "RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical() : Warning : asymmetric mirror(s) no longer supported."
                               << endl;
      _options = "m";
   }

   createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Backward compatibility constructor for Roo2DKeysPdf. If you are a new user,
/// please use the first constructor form.

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const char *name, const char *title, RooAbsReal &x, RooAbsReal &y, const RooAbsData &data,
                           TString options, Double_t rho, Double_t nSigma, Bool_t rotate, Bool_t sortInput)
   : RooAbsPdf(name, title), _varList("varList", "List of variables", this),
     _rhoList("rhoList", "List of rho parameters", this), _dataP(0), _data(data), _options(options), _widthFactor(rho),
     _nSigma(nSigma), _weights(&_weights0), _rotate(rotate), _sortInput(sortInput), _nAdpt(1), _tracker(0)
{
   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   _varList.add(RooArgSet(x, y));
   _varName.push_back(x.GetName());
   _varName.push_back(y.GetName());

   createPdf();
}

////////////////////////////////////////////////////////////////////////////////
/// Constructor

RooNDKeysPdfAnalytical::RooNDKeysPdfAnalytical(const RooNDKeysPdfAnalytical &other, const char *name)
   : RooAbsPdf(other, name), _varList("varList", this, other._varList), _rhoList("rhoList", this, other._rhoList),
     _dataP(other._dataP != NULL ? new RooDataSet(*other._dataP) : NULL),
     _data(other._dataP != NULL ? *_dataP : other._data), _options(other._options), _widthFactor(other._widthFactor),
     _nSigma(other._nSigma), _weights(&_weights0), _rotate(other._rotate), _sortInput(other._sortInput),
     _nAdpt(other._nAdpt)
{
   _tracker = (other._tracker != NULL ? new RooChangeTracker(*other._tracker) : NULL);
   // if (_tracker!=NULL) { _tracker->hasChanged(true); }

   _varItr = _varList.createIterator();
   _rhoItr = _rhoList.createIterator();

   _fixedShape = other._fixedShape;
   _mirror = other._mirror;
   _debug = other._debug;
   _verbose = other._verbose;
   _sqrt2pi = other._sqrt2pi;
   _nDim = other._nDim;
   _nEvents = other._nEvents;
   _nEventsM = other._nEventsM;
   _nEventsW = other._nEventsW;
   _d = other._d;
   _n = other._n;
   _dataPts = other._dataPts;
   _dataPtsR = other._dataPtsR;
   _weights0 = other._weights0;
   _weights1 = other._weights1;
   if (_options.Contains("a")) {
      _weights = &_weights1;
   }
   //_sortIdcs    = other._sortIdcs;
   _sortTVIdcs = other._sortTVIdcs;
   _varName = other._varName;
   _rho = other._rho;
   _x = other._x;
   _x0 = other._x0;
   _x1 = other._x1;
   _x2 = other._x2;
   _xDatLo = other._xDatLo;
   _xDatHi = other._xDatHi;
   _xDatLo3s = other._xDatLo3s;
   _xDatHi3s = other._xDatHi3s;
   _mean = other._mean;
   _sigma = other._sigma;

   // BoxInfo
   _netFluxZ = other._netFluxZ;
   _nEventsBW = other._nEventsBW;
   _nEventsBMSW = other._nEventsBMSW;
   _xVarLo = other._xVarLo;
   _xVarHi = other._xVarHi;
   _xVarLoM3s = other._xVarLoM3s;
   _xVarLoP3s = other._xVarLoP3s;
   _xVarHiM3s = other._xVarHiM3s;
   _xVarHiP3s = other._xVarHiP3s;
   _bpsIdcs = other._bpsIdcs;
   _ibNoSort = other._ibNoSort;
   _sIdcs = other._sIdcs;
   _bIdcs = other._bIdcs;
   _bmsIdcs = other._bmsIdcs;

   _rangeBoxInfo = other._rangeBoxInfo;
   _fullBoxInfo = other._fullBoxInfo;

   _idx = other._idx;
   _minWeight = other._minWeight;
   _maxWeight = other._maxWeight;
   _wMap = other._wMap;

   _covMat = new TMatrixDSym(*other._covMat);
   _corrMat = new TMatrixDSym(*other._corrMat);
   _rotMat = new TMatrixD(*other._rotMat);
   _sigmaR = new TVectorD(*other._sigmaR);
   _dx = new TVectorD(*other._dx);
   _sigmaAvgR = other._sigmaAvgR;
}

////////////////////////////////////////////////////////////////////////////////

RooNDKeysPdfAnalytical::~RooNDKeysPdfAnalytical()
{
  if (_varItr)    delete _varItr;
  if (_rhoItr)
     delete _rhoItr;
  if (_covMat)    delete _covMat;
  if (_corrMat)   delete _corrMat;
  if (_rotMat)    delete _rotMat;
  if (_sigmaR)    delete _sigmaR;
  if (_dx)        delete _dx;
  if (_dataP)
     delete _dataP;
  if (_tracker)
     delete _tracker;

  // delete all the boxinfos map
  while ( !_rangeBoxInfo.empty() ) {
    map<pair<string,int>,BoxInfo*>::iterator iter = _rangeBoxInfo.begin();
    BoxInfo* box= (*iter).second;
    _rangeBoxInfo.erase(iter);
    delete box;
  }

  _dataPts.clear();
  _dataPtsR.clear();
  _weights0.clear();
  _weights1.clear();
  //_sortIdcs.clear();
  _sortTVIdcs.clear();
}

////////////////////////////////////////////////////////////////////////////////
/// evaluation order of constructor.

void RooNDKeysPdfAnalytical::createPdf(Bool_t firstCall) const
{
  if (firstCall) {
    // set options
    setOptions();
    // initialization
    initialize();
  }


  // copy dataset, calculate sigma_i's, determine min and max event weight
  loadDataSet(firstCall);

  // mirror dataset around dataset boundaries -- does not depend on event weights
  if (_mirror) mirrorDataSet();

  // store indices and weights of events with high enough weights
  loadWeightSet();

  // store indices of events in variable boundaries and box shell.
//calculateShell(&_fullBoxInfo);
  // calculate normalization needed in analyticalIntegral()
//calculatePreNorm(&_fullBoxInfo);

  // lookup table for determining which events contribute to a certain coordinate
  sortDataIndices();

  // determine static and/or adaptive bandwidth
  calculateBandWidth();
}

////////////////////////////////////////////////////////////////////////////////
/// set the configuration

void RooNDKeysPdfAnalytical::setOptions() const
{
  _options.ToLower();

  if( _options.Contains("a") ) { _weights = &_weights1; }
  else                         { _weights = &_weights0; }
  if( _options.Contains("m") )   _mirror = true;
  else                           _mirror = false;
  if( _options.Contains("d") )   _debug  = true;
  else                           _debug  = false;
  if( _options.Contains("v") ) { _debug = true;  _verbose = true; }
  else                         { _debug = false; _verbose = false; }

  cxcoutD(InputArguments) << "RooNDKeysPdfAnalytical::setOptions()    options = " << _options
         << "\n\tbandWidthType    = " << _options.Contains("a")
         << "\n\tmirror           = " << _mirror
         << "\n\tdebug            = " << _debug
         << "\n\tverbose          = " << _verbose
         << endl;

  if (_nSigma<2.0) {
    coutW(InputArguments) << "RooNDKeysPdfAnalytical::setOptions() : Warning : nSigma = " << _nSigma << " < 2.0. "
           << "Calculated normalization could be too large."
           << endl;
  }

  // number of adaptive width iterations. Default is 1.
  if (_options.Contains("a")) {
     if (!sscanf(_options.Data(), "%d%*s", &_nAdpt)) {
        _nAdpt = 1;
     }
  }
}

////////////////////////////////////////////////////////////////////////////////
/// initialization

void RooNDKeysPdfAnalytical::initialize() const
{
  _sqrt2pi   = sqrt(2.0*TMath::Pi()) ;
  _nDim      = _varList.getSize();
  _nEvents   = (Int_t)_data.numEntries();
  _nEventsM  = _nEvents;
  _fixedShape= kFALSE;

  _netFluxZ = kFALSE;
  _nEventsBW = 0;
  _nEventsBMSW = 0;

  if(_nDim==0) {
    coutE(InputArguments) << "ERROR:  RooNDKeysPdfAnalytical::initialize() : The observable list is empty. "
           << "Unable to begin generating the PDF." << endl;
    R__ASSERT (_nDim!=0);
  }

  if(_nEvents==0) {
    coutE(InputArguments) << "ERROR:  RooNDKeysPdfAnalytical::initialize() : The input data set is empty. "
           << "Unable to begin generating the PDF." << endl;
    R__ASSERT (_nEvents!=0);
  }

  _d         = static_cast<Double_t>(_nDim);

  vector<Double_t> dummy(_nDim,0.);
  _dataPts.resize(_nEvents,dummy);
  _weights0.resize(_nEvents,dummy);
  //_sortIdcs.resize(_nDim);
  _sortTVIdcs.resize(_nDim);

  //rdh _rho.resize(_nDim,_widthFactor);

  if (_widthFactor>0) { _rho.resize(_nDim,_widthFactor); }
  // else: _rho has been provided as external input

  _x.resize(_nDim,0.);
  _x0.resize(_nDim,0.);
  _x1.resize(_nDim,0.);
  _x2.resize(_nDim,0.);

  _mean.resize(_nDim,0.);
  _sigma.resize(_nDim,0.);

  _xDatLo.resize(_nDim,0.);
  _xDatHi.resize(_nDim,0.);
  _xDatLo3s.resize(_nDim,0.);
  _xDatHi3s.resize(_nDim,0.);

  boxInfoInit(&_fullBoxInfo,0,0xFFFF);

  _minWeight=0;
  _maxWeight=0;
  _wMap.clear();

  _covMat = 0;
  _corrMat= 0;
  _rotMat = 0;
  _sigmaR = 0;
  _dx = new TVectorD(_nDim); _dx->Zero();
  _dataPtsR.resize(_nEvents,*_dx);

  _varItr->Reset() ;
  RooRealVar* var ;
  for(Int_t j=0; (var=(RooRealVar*)_varItr->Next()); ++j) {
    _xDatLo[j] = var->getMin();
    _xDatHi[j] = var->getMax();
  }
}

////////////////////////////////////////////////////////////////////////////////
/// copy the dataset and calculate some useful variables

void RooNDKeysPdfAnalytical::loadDataSet(Bool_t firstCall) const
{
  // first some initialization
  _nEventsW=0.;

  TMatrixD mat(_nDim,_nDim);
  if (!_covMat)  _covMat = new TMatrixDSym(_nDim);
  if (!_corrMat) _corrMat= new TMatrixDSym(_nDim);
  if (!_rotMat)  _rotMat = new TMatrixD(_nDim,_nDim);
  if (!_sigmaR)  _sigmaR = new TVectorD(_nDim);

  mat.Zero();
  _covMat->Zero();
  _corrMat->Zero();
  _rotMat->Zero();
  _sigmaR->Zero();

  const RooArgSet* values= _data.get();
  vector<RooRealVar*> dVars(_nDim);
  for  (Int_t j=0; j<_nDim; j++) {
    dVars[j] = (RooRealVar*)values->find(_varName[j].c_str());
    _x0[j]=_x1[j]=_x2[j]=0.;
  }

  _idx.clear();
  for (Int_t i=0; i<_nEvents; i++) {

    _data.get(i); // fills dVars
    _idx.push_back(i);
    vector<Double_t>& point  = _dataPts[i];
    TVectorD& pointV = _dataPtsR[i];

    Double_t myweight = _data.weight(); // default is one?
    if ( TMath::Abs(myweight)>_maxWeight ) { _maxWeight = TMath::Abs(myweight); }
    _nEventsW += myweight;

    for (Int_t j=0; j<_nDim; j++) {
      for (Int_t k=0; k<_nDim; k++) {
   mat(j,k) += dVars[j]->getVal() * dVars[k]->getVal() * myweight;
      }
      // only need to do once
      if (firstCall)
   point[j] = pointV[j] = dVars[j]->getVal();

      _x0[j] += 1. * myweight;
      _x1[j] += point[j] * myweight ;
      _x2[j] += point[j] * point[j] * myweight ;
      if (_x2[j]!=_x2[j]) exit(3);

      // only need to do once
      if (firstCall) {
   if (point[j]<_xDatLo[j]) { _xDatLo[j]=point[j]; }
   if (point[j]>_xDatHi[j]) { _xDatHi[j]=point[j]; }
      }
    }
  }

  _n = TMath::Power(4./(_nEventsW*(_d+2.)), 1./(_d+4.)) ;
  // = (4/[n(dim(R) + 2)])^1/(dim(R)+4); dim(R) = 2
  _minWeight = (0.5 - TMath::Erf(_nSigma/sqrt(2.))/2.) * _maxWeight;

  for (Int_t j=0; j<_nDim; j++) {
    _mean[j]  = _x1[j]/_x0[j];
    _sigma[j] = sqrt(_x2[j]/_x0[j]-_mean[j]*_mean[j]);
  }

  for (Int_t j=0; j<_nDim; j++) {
    for (Int_t k=0; k<_nDim; k++) {
      (*_covMat)(j,k) = mat(j,k)/_x0[j] - _mean[j]*_mean[k];
    }
  }

  for (Int_t j=0; j<_nDim; j++) {
    for (Int_t k=0; k<_nDim; k++)
      (*_corrMat)(j,k) = (*_covMat)(j,k)/(_sigma[j]*_sigma[k]) ;
  }

  // use raw sigmas (without rho) for sigmaAvgR
  TMatrixDSymEigen evCalculator(*_covMat);
  TVectorD sigmaRraw = evCalculator.GetEigenValues();
  for (Int_t j=0; j<_nDim; j++) { sigmaRraw[j] = sqrt(sigmaRraw[j]); }

  _sigmaAvgR=1.;
  for (Int_t j=0; j<_nDim; j++) { _sigmaAvgR *= sigmaRraw[j]; }
  _sigmaAvgR = TMath::Power(_sigmaAvgR, 1./_d) ;

  // find decorrelation matrix and eigenvalues (R)
  if (_nDim > 1 && _rotate) {
     // new: rotation matrix now independent of rho evaluation
     *_rotMat = evCalculator.GetEigenVectors();
     *_rotMat = _rotMat->T(); // transpose
  } else {
     TMatrixD haar(_nDim, _nDim);
     TMatrixD unit(TMatrixD::kUnit, haar);
     *_rotMat = unit;
  }

  // update sigmas (rho dependent)
  updateRho();

  //// rho no longer used after this.
  //// Now set rho = 1 because sigmaR now contains rho
  // for (Int_t j=0; j<_nDim; j++) { _rho[j] = 1.; }  // reset: important!

  if (_verbose) {
     //_covMat->Print();
     _rotMat->Print();
     _corrMat->Print();
     _sigmaR->Print();
  }

  if (_nDim > 1 && _rotate) {
     // apply rotation
     for (Int_t i = 0; i < _nEvents; i++) {
        TVectorD &pointR = _dataPtsR[i];
        pointR *= *_rotMat;
     }
  }

  coutI(Contents) << "RooNDKeysPdfAnalytical::loadDataSet(" << this << ")"
                  << "\n Number of events in dataset: " << _nEvents
                  << "\n Weighted number of events in dataset: " << _nEventsW << endl;
}

////////////////////////////////////////////////////////////////////////////////
/// determine mirror dataset.
/// mirror points are added around the physical boundaries of the dataset
/// Two steps:
/// 1. For each entry, determine if it should be mirrored (the mirror configuration).
/// 2. For each mirror configuration, make the mirror points.

void RooNDKeysPdfAnalytical::mirrorDataSet() const
{
  for (Int_t j=0; j<_nDim; j++) {
     _xDatLo3s[j] = _xDatLo[j] + _nSigma * (_n * _sigma[j]);
     _xDatHi3s[j] = _xDatHi[j] - _nSigma * (_n * _sigma[j]);

     // cout<<"xDatLo3s["<<j<<"]="<<_xDatLo3s[j]<<endl;
     // cout<<"xDatHi3s["<<j<<"]="<<_xDatHi3s[j]<<endl;
  }

  vector<Double_t> dummy(_nDim,0.);

  // 1.
  for (Int_t i=0; i<_nEvents; i++) {
    vector<Double_t>& x = _dataPts[i];

    Int_t size = 1;
    vector<vector<Double_t> > mpoints(size,dummy);
    vector<vector<Int_t> > mjdcs(size);

    // create all mirror configurations for event i
    for (Int_t j=0; j<_nDim; j++) {

      vector<Int_t>& mjdxK = mjdcs[0];
      vector<Double_t>& mpointK = mpoints[0];

      // single mirror *at physical boundaries*
      if ((x[j]>_xDatLo[j] && x[j]<_xDatLo3s[j]) && x[j]<(_xDatLo[j]+_xDatHi[j])/2.) {
   mpointK[j] = 2.*_xDatLo[j]-x[j];
   mjdxK.push_back(j);
      } else if ((x[j]<_xDatHi[j] && x[j]>_xDatHi3s[j]) && x[j]>(_xDatLo[j]+_xDatHi[j])/2.) {
   mpointK[j] = 2.*_xDatHi[j]-x[j];
   mjdxK.push_back(j);
      }
    }

    vector<Int_t>& mjdx0 = mjdcs[0];
    // no mirror point(s) for this event
    if (size==1 && mjdx0.size()==0) continue;

    // 2.
    // generate all mirror points for event i
    vector<Int_t>& mjdx = mjdcs[0];
    vector<Double_t>& mpoint = mpoints[0];

    // number of mirror points for this mirror configuration
    Int_t eMir = 1 << mjdx.size();
    vector<vector<Double_t> > epoints(eMir,x);

    for (Int_t m=0; m<Int_t(mjdx.size()); m++) {
      Int_t size1 = 1 << m;
      Int_t size2 = 1 << (m+1);
      // copy all previous mirror points
      for (Int_t l=size1; l<size2; ++l) {
   epoints[l] = epoints[l-size1];
   // fill high mirror points
   vector<Double_t>& epoint = epoints[l];
   epoint[mjdx[Int_t(mjdx.size()-1)-m]] = mpoint[mjdx[Int_t(mjdx.size()-1)-m]];
      }
    }

    // remove duplicate mirror points
    // note that: first epoint == x
    epoints.erase(epoints.begin());

    // add mirror points of event i to total dataset
    TVectorD pointR(_nDim);

    for (Int_t m=0; m<Int_t(epoints.size()); m++) {
      _idx.push_back(i);
      _dataPts.push_back(epoints[m]);
      //_weights0.push_back(_weights0[i]);
      for (Int_t j=0; j<_nDim; j++) { pointR[j] = (epoints[m])[j]; }
      if (_nDim > 1 && _rotate) {
         pointR *= *_rotMat;
      }
      _dataPtsR.push_back(pointR);
    }

    epoints.clear();
    mpoints.clear();
    mjdcs.clear();
  } // end of event loop

  _nEventsM = Int_t(_dataPts.size());
}

////////////////////////////////////////////////////////////////////////////////

void RooNDKeysPdfAnalytical::loadWeightSet() const
{
  _wMap.clear();

  for (Int_t i=0; i<_nEventsM; i++) {
    _data.get(_idx[i]);
    Double_t myweight = _data.weight();
    //if ( TMath::Abs(myweight)>_minWeight ) {
      _wMap[i] = myweight;
    //}
  }

  coutI(Contents) << "RooNDKeysPdfAnalytical::loadWeightSet(" << this << ") : Number of weighted events : " << _wMap.size() << endl;
}

////////////////////////////////////////////////////////////////////////////////
/// determine points in +/- nSigma shell around the box determined by the variable
/// ranges. These points are needed in the normalization, to determine probability
/// leakage in and out of the box.

void RooNDKeysPdfAnalytical::calculateShell(BoxInfo* bi) const
{
  for (Int_t j=0; j<_nDim; j++) {
    if (bi->xVarLo[j]==_xDatLo[j] && bi->xVarHi[j]==_xDatHi[j]) {
      bi->netFluxZ = bi->netFluxZ && kTRUE;
    } else { bi->netFluxZ = kFALSE; }

    bi->xVarLoM3s[j] = bi->xVarLo[j] - _nSigma * (_n * _sigma[j]);
    bi->xVarLoP3s[j] = bi->xVarLo[j] + _nSigma * (_n * _sigma[j]);
    bi->xVarHiM3s[j] = bi->xVarHi[j] - _nSigma * (_n * _sigma[j]);
    bi->xVarHiP3s[j] = bi->xVarHi[j] + _nSigma * (_n * _sigma[j]);

    //cout<<"bi->xVarLoM3s["<<j<<"]="<<bi->xVarLoM3s[j]<<endl;
    //cout<<"bi->xVarLoP3s["<<j<<"]="<<bi->xVarLoP3s[j]<<endl;
    //cout<<"bi->xVarHiM3s["<<j<<"]="<<bi->xVarHiM3s[j]<<endl;
    //cout<<"bi->xVarHiM3s["<<j<<"]="<<bi->xVarHiM3s[j]<<endl;
  }

  map<Int_t,Double_t>::iterator wMapItr = _wMap.begin();

  //for (Int_t i=0; i<_nEventsM; i++) {
  for (; wMapItr!=_wMap.end(); ++wMapItr) {
    Int_t i = (*wMapItr).first;

    const vector<Double_t>& x = _dataPts[i];
    Bool_t inVarRange(kTRUE);
    Bool_t inVarRangePlusShell(kTRUE);

    for (Int_t j=0; j<_nDim; j++) {

      if (x[j]>bi->xVarLo[j] && x[j]<bi->xVarHi[j]) {
   inVarRange = inVarRange && kTRUE;
      } else { inVarRange = inVarRange && kFALSE; }

      if (x[j]>bi->xVarLoM3s[j] && x[j]<bi->xVarHiP3s[j]) {
   inVarRangePlusShell = inVarRangePlusShell && kTRUE;
      } else { inVarRangePlusShell = inVarRangePlusShell && kFALSE; }
    }

    // event in range?
    if (inVarRange) {
      bi->bIdcs.push_back(i);
    }

    // event in shell?
    if (inVarRangePlusShell) {
      bi->bpsIdcs[i] = kTRUE;
      Bool_t inShell(kFALSE);
      for (Int_t j=0; j<_nDim; j++) {
   if ((x[j]>bi->xVarLoM3s[j] && x[j]<bi->xVarLoP3s[j]) && x[j]<(bi->xVarLo[j]+bi->xVarHi[j])/2.) {
     inShell = kTRUE;
   } else if ((x[j]>bi->xVarHiM3s[j] && x[j]<bi->xVarHiP3s[j]) && x[j]>(bi->xVarLo[j]+bi->xVarHi[j])/2.) {
     inShell = kTRUE;
   }
      }
      if (inShell) bi->sIdcs.push_back(i); // needed for normalization
      else {
   bi->bmsIdcs.push_back(i);          // idem
      }
    }
  }

  coutI(Contents) << "RooNDKeysPdfAnalytical::calculateShell() : "
        << "\n Events in shell " << bi->sIdcs.size()
        << "\n Events in box " << bi->bIdcs.size()
        << "\n Events in box and shell " << bi->bpsIdcs.size()
        << endl;
}

////////////////////////////////////////////////////////////////////////////////
///bi->nEventsBMSW=0.;
///bi->nEventsBW=0.;

void RooNDKeysPdfAnalytical::calculatePreNorm(BoxInfo* bi) const
{
  // box minus shell
  for (Int_t i=0; i<Int_t(bi->bmsIdcs.size()); i++)
    bi->nEventsBMSW += _wMap[bi->bmsIdcs[i]];

  // box
  for (Int_t i=0; i<Int_t(bi->bIdcs.size()); i++)
    bi->nEventsBW += _wMap[bi->bIdcs[i]];

  cxcoutD(Eval) << "RooNDKeysPdfAnalytical::calculatePreNorm() : "
         << "\n nEventsBMSW " << bi->nEventsBMSW
         << "\n nEventsBW " << bi->nEventsBW
         << endl;
}

////////////////////////////////////////////////////////////////////////////////
/// sort entries, as needed for loopRange()

void RooNDKeysPdfAnalytical::sortDataIndices(BoxInfo* bi) const
{
   // will loop over all events by default
   if (!_sortInput) {
      _ibNoSort.clear();
      for (unsigned int i = 0; i < _dataPtsR.size(); ++i) {
         _ibNoSort[i] = kTRUE;
      }
      return;
   }

   itVec itrVecR;
   vector<TVectorD>::iterator dpRItr = _dataPtsR.begin();
   for (Int_t i = 0; dpRItr != _dataPtsR.end(); ++dpRItr, ++i) {
      if (bi) {
         if (bi->bpsIdcs.find(i) != bi->bpsIdcs.end())
            // if (_wMap.find(i)!=_wMap.end())
            itrVecR.push_back(itPair(i, dpRItr));
      } else
         itrVecR.push_back(itPair(i, dpRItr));
  }

  for (Int_t j=0; j<_nDim; j++) {
    _sortTVIdcs[j].clear();
    sort(itrVecR.begin(),itrVecR.end(),SorterTV_L2H(j));
    _sortTVIdcs[j] = itrVecR;
  }

  for (Int_t j=0; j<_nDim; j++) {
    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::sortDataIndices() : Number of sorted events : " << _sortTVIdcs[j].size() << endl;
  }
}

////////////////////////////////////////////////////////////////////////////////

void RooNDKeysPdfAnalytical::calculateBandWidth() const
{
  cxcoutD(Eval) << "RooNDKeysPdfAnalytical::calculateBandWidth()" << endl;

  // non-adaptive bandwidth
  // (default, and needed to calculate adaptive bandwidth)

  if(!_options.Contains("a")) {
      cxcoutD(Eval) << "RooNDKeysPdfAnalytical::calculateBandWidth() Using static bandwidth." << endl;
  }

  // fixed width approximation
  for (Int_t i=0; i<_nEvents; i++) {
    vector<Double_t>& weight = _weights0[i];
    for (Int_t j = 0; j < _nDim; j++) {
       weight[j] = _n * (*_sigmaR)[j];
       // cout<<"j: "<<j<<", _n: "<<_n<<", sigmaR="<<(*_sigmaR)[j]<<", weight="<<weight[j]<<endl;
    }
  }

  // adaptive width
  if (_options.Contains("a")) {
     cxcoutD(Eval) << "RooNDKeysPdfAnalytical::calculateBandWidth() Using adaptive bandwidth." << endl;

     double sqrt12 = sqrt(12.);
     double sqrtSigmaAvgR = sqrt(_sigmaAvgR);

     vector<Double_t> dummy(_nDim, 0.);
     _weights1.resize(_nEvents, dummy);

     std::vector<std::vector<Double_t>> *weights_prev(0);
     std::vector<std::vector<Double_t>> *weights_new(0);

     // cout << "Number of adaptive iterations: " << _nAdpt << endl;

     for (Int_t k = 1; k <= _nAdpt; ++k) {

        // cout << "  Cycle: " << k << endl;

        // if multiple adaptive iterations, need to swap weight sets
        if (k % 2) {
           weights_prev = &_weights0;
           weights_new = &_weights1;
        } else {
           weights_prev = &_weights1;
           weights_new = &_weights0;
        }

        for (Int_t i = 0; i < _nEvents; ++i) {
           vector<Double_t> &x = _dataPts[i];
           Double_t f = TMath::Power(gauss(x, *weights_prev) / _nEventsW, -1. / (2. * _d));

           vector<Double_t> &weight = (*weights_new)[i];
           for (Int_t j = 0; j < _nDim; j++) {
              Double_t norm = (_n * (*_sigmaR)[j]) / sqrtSigmaAvgR;
              weight[j] = norm * f / sqrt12; //  note additional factor of sqrt(12) compared with HEP-EX/0011057
           }
        }
     }
     // this is the latest updated weights set
     _weights = weights_new;
  }
}

////////////////////////////////////////////////////////////////////////////////
/// loop over all closest point to x, as determined by loopRange()

Double_t RooNDKeysPdfAnalytical::gauss(vector<Double_t>& x, vector<vector<Double_t> >& weights) const
{
  if(_nEvents==0) return 0.;

  Double_t z=0.;
  map<Int_t,Bool_t> ibMap;

  // determine input loop range for event x
  if (_sortInput) {
     loopRange(x, ibMap);
  }

  map<Int_t, Bool_t>::iterator ibMapItr, ibMapEnd;
  ibMapItr = (_sortInput ? ibMap.begin() : _ibNoSort.begin());
  ibMapEnd = (_sortInput ? ibMap.end() : _ibNoSort.end());

  for (; ibMapItr != ibMapEnd; ++ibMapItr) {
     Int_t i = (*ibMapItr).first;

     Double_t g(1.);

     if (i >= (Int_t)_idx.size()) {
        continue;
     } //---> 1.myline

     const vector<Double_t> &point = _dataPts[i];
     const vector<Double_t> &weight = weights[_idx[i]];

     for (Int_t j = 0; j < _nDim; j++) {
        (*_dx)[j] = x[j] - point[j];
     }

     if (_nDim > 1 && _rotate) {
        *_dx *= *_rotMat; // rotate to decorrelated frame!
     }

     for (Int_t j = 0; j < _nDim; j++) {
        Double_t r = (*_dx)[j]; // x[j] - point[j];
        Double_t c = 1. / (2. * weight[j] * weight[j]);

        // cout << "j = " << j << " x[j] = " << point[j] << " w = " << weight[j] << endl;

        g *= exp(-c * r * r);
        g *= 1. / (_sqrt2pi * weight[j]);
     }
     z += (g * _wMap[_idx[i]]);
  }
  return z;
}

////////////////////////////////////////////////////////////////////////////////
/// determine closest points to x, to loop over in evaluate()

void RooNDKeysPdfAnalytical::loopRange(vector<Double_t>& x, map<Int_t,Bool_t>& ibMap) const
{
   ibMap.clear();
   TVectorD xRm(_nDim);
   TVectorD xRp(_nDim);

   for (Int_t j = 0; j < _nDim; j++) {
      xRm[j] = xRp[j] = x[j];
   }

   if (_nDim > 1 && _rotate) {
      xRm *= *_rotMat;
      xRp *= *_rotMat;
   }
   for (Int_t j = 0; j < _nDim; j++) {
      xRm[j] -= _nSigma * (_n * (*_sigmaR)[j]);
      xRp[j] += _nSigma * (_n * (*_sigmaR)[j]);
      // cout<<"xRm["<<j<<"]="<<xRm[j]<<endl;
      // cout<<"xRp["<<j<<"]="<<xRp[j]<<endl;
  }

  vector<TVectorD> xvecRm(1,xRm);
  vector<TVectorD> xvecRp(1,xRp);

  map<Int_t,Bool_t> ibMapRT;

  for (Int_t j=0; j<_nDim; j++) {
    ibMap.clear();
    itVec::iterator lo = lower_bound(_sortTVIdcs[j].begin(), _sortTVIdcs[j].end(),
                 itPair(0,xvecRm.begin()), SorterTV_L2H(j));
    itVec::iterator hi =
       upper_bound(_sortTVIdcs[j].begin(), _sortTVIdcs[j].end(), itPair(0, xvecRp.begin()), SorterTV_L2H(j));
    itVec::iterator it = lo;

    if (j==0) {
      if (_nDim==1) { for (it=lo; it!=hi; ++it) ibMap[(*it).first] = kTRUE; }
      else { for (it=lo; it!=hi; ++it) ibMapRT[(*it).first] = kTRUE; }
      continue;
    }

    for (it=lo; it!=hi; ++it)
      if (ibMapRT.find((*it).first)!=ibMapRT.end()) { ibMap[(*it).first] = kTRUE; }

    ibMapRT.clear();
    if (j!=_nDim-1) { ibMapRT = ibMap; }
  }
}

////////////////////////////////////////////////////////////////////////////////

void RooNDKeysPdfAnalytical::boxInfoInit(BoxInfo* bi, const char* rangeName, Int_t /*code*/) const
{
  vector<Bool_t> doInt(_nDim,kTRUE);

  bi->filled = kFALSE;

  bi->xVarLo.resize(_nDim,0.);
  bi->xVarHi.resize(_nDim,0.);
  bi->xVarLoM3s.resize(_nDim,0.);
  bi->xVarLoP3s.resize(_nDim,0.);
  bi->xVarHiM3s.resize(_nDim,0.);
  bi->xVarHiP3s.resize(_nDim,0.);

  bi->netFluxZ = kTRUE;
  bi->bpsIdcs.clear();
  bi->bIdcs.clear();
  bi->sIdcs.clear();
  bi->bmsIdcs.clear();

  bi->nEventsBMSW=0.;
  bi->nEventsBW=0.;

  _varItr->Reset() ;
  RooRealVar* var ;
  for(Int_t j=0; (var=(RooRealVar*)_varItr->Next()); ++j) {
    if (doInt[j]) {
      bi->xVarLo[j] = var->getMin(rangeName);
      bi->xVarHi[j] = var->getMax(rangeName);
    } else {
      bi->xVarLo[j] = var->getVal() ;
      bi->xVarHi[j] = var->getVal() ;
    }
  }
}

////////////////////////////////////////////////////////////////////////////////

Double_t RooNDKeysPdfAnalytical::evaluate() const
{
   if (_tracker != NULL && _tracker->hasChanged(kTRUE)) {
      updateRho(); // update internal rho parameters
      // redetermine static and/or adaptive bandwidth
      calculateBandWidth();
   }

   _varItr->Reset();
   RooAbsReal *var;
   const RooArgSet *nset = _varList.nset();
   for (Int_t j = 0; (var = (RooAbsReal *)_varItr->Next()); ++j) {
      _x[j] = var->getVal(nset);
  }

  Double_t val = gauss(_x,*_weights);
  //cout<<"returning "<<val<<endl;

  if (val>=1E-20)
    return val ;
  else
    return (1E-20) ;
}

////////////////////////////////////////////////////////////////////////////////
Int_t RooNDKeysPdfAnalytical::getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* /*rangeName*/) const
{
  Int_t code=0;
  if (matchArgs(allVars,analVars,RooArgSet(_varList))) { code=1; }

  return code;

}

////////////////////////////////////////////////////////////////////////////////
/*
Double_t RooNDKeysPdfAnalytical::analyticalIntegral(Int_t code, const char* rangeName) const
{
  checkInitWeights();

  cxcoutD(Eval) << "Calling RooNDKeysPdfAnalytical::analyticalIntegral(" << GetName() << ") with code " << code
         << " and rangeName " << (rangeName?rangeName:"<none>") << endl;

  // determine which observables need to be integrated over ...
  Int_t nComb = 1 << (_nDim);
  R__ASSERT(code>=1 && code<nComb) ;

  // If the range name is defined, we loop over all data points for the kernel
  // estimation to keep the code simple. Further optimization is possible if really necessary,
  // but this is already much faster than numerical integration.
  if(rangeName) {
    // the block of code is borrowed from RooNDKeysPdfAnalytical::evaluate()
    if ( (_tracker && _tracker->hasChanged(kTRUE)) || (_weights != &_weights0 && _weights != &_weights1) ) {
      updateRho(); // update internal rho parameters
      // redetermine static and/or adaptive bandwidth
      const_cast<RooNDKeysPdfAnalytical*>(this)->calculateBandWidth();
    }

    std::vector<double> xLowerBound;
    xLowerBound.resize(_nDim);
    std::vector<double> xHigherBound;
    xHigherBound.resize(_nDim);

    std::vector<double> xLowerBoundMinShell;
    std::vector<double> xHigherBoundMinShell;
    std::vector<double> xLowerBoundMaxShell;
    std::vector<double> xHigherBoundMaxShell;
    xLowerBoundMinShell.resize(_nDim);
    xHigherBoundMinShell.resize(_nDim);
    xLowerBoundMaxShell.resize(_nDim);
    xHigherBoundMaxShell.resize(_nDim);

    TVectorD dxLowerBound(_nDim);
    TVectorD dxHigherBound(_nDim);

    _varItr->Reset() ;
    RooRealVar* var ;
    for (unsigned int j=0; (var=(RooRealVar*)_varItr->Next()); ++j) {

    //for (unsigned int j=0; j < _varList.size(); ++j) {
    //  auto var = static_cast<const RooAbsRealLValue*>(_varList.at(j));
      xLowerBound[j] = var->getMin(rangeName);
      xHigherBound[j] = var->getMax(rangeName);

      xLowerBoundMinShell[j] = xLowerBound[j] - _nSigma * (_n * _sigma[j]);
      xLowerBoundMaxShell[j] = xLowerBound[j] + _nSigma * (_n * _sigma[j]);
      xHigherBoundMinShell[j] = xHigherBound[j] - _nSigma * (_n * _sigma[j]);
      xHigherBoundMaxShell[j] = xHigherBound[j] + _nSigma * (_n * _sigma[j]);
    }

    double val = 0.;
    for (size_t i = 0; i < _dataPts.size(); ++i) {
       double g = 1.;
       const vector<Double_t> &point = _dataPts[i];
       const vector<Double_t> &weight = (*_weights)[_idx[i]];

       // skip if the data point is not in the shell of the lower bound or higher bound
       bool inShell = false;
       bool inRange = true;
       for (int j = 0; j < _nDim; j++) {
         inShell |= point[j] - xLowerBoundMinShell[j] > 0 && point[j] - xLowerBoundMaxShell[j] < 0;
         inShell |= point[j] - xHigherBoundMinShell[j] > 0 && point[j] - xHigherBoundMaxShell[j] < 0;
         inRange &= point[j] - xLowerBound[j] > 0 && point[j] - xHigherBound[j] < 0;
       }
       if( !__builtin_expect(inShell, false)) {
         if (inRange) {
           val += _wMap.at(_idx[i]);
           //cout << i << " " << _wMap.at(_idx[i]) << endl; 
         }
         continue;
       }

       for (int j = 0; j < _nDim; j++) {
          dxLowerBound[j] = xLowerBound[j] - point[j];
          dxHigherBound[j] = xHigherBound[j] - point[j];
       }

       if (_nDim > 1 && _rotate) {
          // rotate to decorrelated frame!
          dxLowerBound *= *_rotMat;
          dxHigherBound *= *_rotMat;
       }

       for (int j = 0; j < _nDim; j++) {
          if (std::abs(weight[j])>0){
            const double min = dxLowerBound[j]/(weight[j] * std::sqrt(2));
            const double max = dxHigherBound[j]/(weight[j] * std::sqrt(2));

            const double ecmin = std::erfc(std::abs(min));
            const double ecmax = std::erfc(std::abs(max));
            //cout << "min,max,ecmin,ecmax: " << min << " " << max << " " << ecmin << " " << ecmax << endl;
            g *= 0.5 * (min*max < 0.0 ? 2.0 - (ecmin + ecmax)
                                    : max <= 0. ? ecmax - ecmin : ecmin - ecmax);
          }                          
       }
       val += (g * _wMap.at(_idx[i]));
    }
    //cout << "RooNDKeysPdfAnalytical::analyticalIntegral() : Final normalization : " << val << endl;
    return val;
  }

  vector<Bool_t> doInt(_nDim,kTRUE);

  // get BoxInfo
  BoxInfo* bi(0);

  if (rangeName) {
    string rangeNameStr(rangeName) ;
    bi = _rangeBoxInfo[make_pair(rangeNameStr,code)] ;
    if (!bi) {
      bi = new BoxInfo ;
      _rangeBoxInfo[make_pair(rangeNameStr,code)] = bi ;
      boxInfoInit(bi,rangeName,code);
    }
  } else bi= &_fullBoxInfo ;

  // have boundaries changed?
  Bool_t newBounds(kFALSE);
  _varItr->Reset() ;
  RooRealVar* var ;
  for (unsigned int j=0; (var=(RooRealVar*)_varItr->Next()); ++j) {
    //auto var = static_cast<const RooAbsRealLValue*>(_varList.at(j));
    if ((var->getMin(rangeName)-bi->xVarLo[j]!=0) ||
        (var->getMax(rangeName)-bi->xVarHi[j]!=0)) {
      newBounds = kTRUE;
    }
  }

  // reset
  if (newBounds) {
    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Found new boundaries ... " << (rangeName?rangeName:"<none>") << endl;
    boxInfoInit(bi,rangeName,code);
  }

  // recalculates netFluxZero and nEventsIR
  if (!bi->filled || newBounds) {
    // Fill box info with contents
    calculateShell(bi);
    calculatePreNorm(bi);
    bi->filled = kTRUE;
    const_cast<RooNDKeysPdfAnalytical*>(this)->sortDataIndices(bi);
  }

  // first guess
  Double_t norm=bi->nEventsBW;

  if (_mirror && bi->netFluxZ) {
    // KEYS expression is self-normalized
    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Using mirrored normalization : " << bi->nEventsBW << endl;
    cout << "RooNDKeysPdfAnalytical::analyticalIntegral() : Using mirrored normalization : " << bi->nEventsBW << endl;
    return bi->nEventsBW;
  }
  // calculate leakage in and out of variable range box
  else
  {
    norm = bi->nEventsBMSW;
    if (norm<0.) norm=0.;

    for (Int_t i=0; i<Int_t(bi->sIdcs.size()); ++i) {
      Double_t prob=1.;
      const vector<Double_t>& x = _dataPts[bi->sIdcs[i]];
      const vector<Double_t>& weight = (*_weights)[_idx[bi->sIdcs[i]]];

      vector<Double_t> chi(_nDim,100.);

      for (Int_t j=0; j<_nDim; j++) {
   if(!doInt[j]) continue;

   if ((x[j]>bi->xVarLoM3s[j] && x[j]<bi->xVarLoP3s[j]) && x[j]<(bi->xVarLo[j]+bi->xVarHi[j])/2.)
     chi[j] = (x[j]-bi->xVarLo[j])/weight[j];
   else if ((x[j]>bi->xVarHiM3s[j] && x[j]<bi->xVarHiP3s[j]) && x[j]>(bi->xVarLo[j]+bi->xVarHi[j])/2.)
     chi[j] = (bi->xVarHi[j]-x[j])/weight[j];

   if (chi[j]>0) // inVarRange
     prob *= (0.5 + TMath::Erf(fabs(chi[j])/sqrt(2.))/2.);
   else // outside Var range
     prob *= (0.5 - TMath::Erf(fabs(chi[j])/sqrt(2.))/2.);
      }

      norm += prob * _wMap.at(_idx[bi->sIdcs[i]]);
    }

    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Final normalization : " << norm << " " << bi->nEventsBW << endl;
    cout << "RooNDKeysPdfAnalytical::analyticalIntegral() : Final normalization : " << norm << " " << bi->nEventsBW << endl;
    return norm;
  }
}
*/

Double_t RooNDKeysPdfAnalytical::analyticalIntegral(Int_t code, const char* rangeName) const
{
  cxcoutD(Eval) << "Calling RooNDKeysPdfAnalytical::analyticalIntegral(" << GetName() << ") with code " << code
         << " and rangeName " << (rangeName?rangeName:"<none>") << endl;

  // determine which observables need to be integrated over ...
  Int_t nComb = 1 << (_nDim);
  R__ASSERT(code>=1 && code<nComb) ;

  vector<Bool_t> doInt(_nDim,kTRUE);

  // get BoxInfo
  BoxInfo* bi(0);

  if (rangeName) {
    string rangeNameStr(rangeName) ;
    bi = _rangeBoxInfo[make_pair(rangeNameStr,code)] ;
    if (!bi) {
      bi = new BoxInfo ;
      _rangeBoxInfo[make_pair(rangeNameStr,code)] = bi ;
      boxInfoInit(bi,rangeName,code);
    }
  } else bi= &_fullBoxInfo ;

  // have boundaries changed?
  Bool_t newBounds(kFALSE);
  _varItr->Reset() ;
  RooRealVar* var ;
  for(Int_t j=0; (var=(RooRealVar*)_varItr->Next()); ++j) {
    if ((var->getMin(rangeName)-bi->xVarLo[j]!=0) ||
   (var->getMax(rangeName)-bi->xVarHi[j]!=0)) {
      newBounds = kTRUE;
    }
  }

  // reset
  if (newBounds) {
    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Found new boundaries ... " << (rangeName?rangeName:"<none>") << endl;
    boxInfoInit(bi,rangeName,code);
  }

  // recalculates netFluxZero and nEventsIR
  if (!bi->filled || newBounds) {
    // Fill box info with contents
    calculateShell(bi);
    calculatePreNorm(bi);
    bi->filled = kTRUE;
    sortDataIndices(bi);
  }

  // first guess
  Double_t norm=bi->nEventsBW;

  if (_mirror && bi->netFluxZ) {
    // KEYS expression is self-normalized
    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Using mirrored normalization : " << bi->nEventsBW << endl;
    return bi->nEventsBW;
  }
  // calculate leakage in and out of variable range box
  else
  {
    norm = bi->nEventsBMSW;
    if (norm<0.) norm=0.;

    for (Int_t i=0; i<Int_t(bi->sIdcs.size()); ++i) {
      Double_t prob=1.;
      const vector<Double_t>& x = _dataPts[bi->sIdcs[i]];
      const vector<Double_t>& weight = (*_weights)[_idx[bi->sIdcs[i]]];

      vector<Double_t> chi(_nDim,100.);

      for (Int_t j=0; j<_nDim; j++) {
         if(!doInt[j]) continue;
         if (!(fabs(weight[j])>0)) continue;
         if ((x[j]>bi->xVarLoM3s[j] && x[j]<bi->xVarLoP3s[j]) && x[j]<(bi->xVarLo[j]+bi->xVarHi[j])/2.)
           chi[j] = (x[j]-bi->xVarLo[j])/weight[j];
         else if ((x[j]>bi->xVarHiM3s[j] && x[j]<bi->xVarHiP3s[j]) && x[j]>(bi->xVarLo[j]+bi->xVarHi[j])/2.)
           chi[j] = (bi->xVarHi[j]-x[j])/weight[j];

         if (chi[j]>0) // inVarRange
           prob *= (0.5 + TMath::Erf(fabs(chi[j])/sqrt(2.))/2.);
         else // outside Var range
           prob *= (0.5 - TMath::Erf(fabs(chi[j])/sqrt(2.))/2.);
      }

      norm += prob * _wMap[_idx[bi->sIdcs[i]]];
    }

    cxcoutD(Eval) << "RooNDKeysPdfAnalytical::analyticalIntegral() : Final normalization : " << norm << " " << bi->nEventsBW << endl;
    //cout << "RooNDKeysPdfAnalytical::analyticalIntegral() : Final normalization : " << norm << " " << bi->nEventsBW << endl;
    return max(norm, 1E-20); //like evaluate - GIULIO
  }
}
 

RooDataSet *
   ////////////////////////////////////////////////////////////////////////////////

   RooNDKeysPdfAnalytical::createDatasetFromHist(const RooArgList &varList, const TH1 &hist) const
{
   std::vector<RooRealVar *> varVec;
   RooArgSet varsAndWeightSet;

   TIterator *varItr = varList.createIterator();
   RooAbsArg *var;
   for (Int_t i = 0; (var = (RooAbsArg *)varItr->Next()); ++i) {
      if (!dynamic_cast<RooRealVar *>(var)) {
         coutE(InputArguments) << "RooNDKeysPdfAnalytical::createDatasetFromHist(" << GetName() << ") WARNING: variable "
                               << var->GetName() << " is not of type RooRealVar. Skip." << endl;
         continue;
      }
      varsAndWeightSet.add(*var);                       // used for dataset creation
      varVec.push_back(static_cast<RooRealVar *>(var)); // used for setting the variables.
   }
   delete varItr;

   /// Add weight
   RooRealVar weight("weight", "event weight", 0);
   varsAndWeightSet.add(weight);

   /// determine histogram dimensionality
   unsigned int histndim(0);
   std::string classname = hist.ClassName();
   if (classname.find("TH1") == 0) {
      histndim = 1;
   } else if (classname.find("TH2") == 0) {
      histndim = 2;
   } else if (classname.find("TH3") == 0) {
      histndim = 3;
   }
   assert(histndim == varVec.size());

   if (histndim > 3 || histndim <= 0) {
      coutE(InputArguments) << "RooNDKeysPdfAnalytical::createDatasetFromHist(" << GetName()
                            << ") ERROR: input histogram dimension not between [1-3]: " << histndim << endl;
      assert(0);
   }

   /// dataset creation
   RooDataSet *dataFromHist = new RooDataSet("datasetFromHist", "datasetFromHist", varsAndWeightSet, weight.GetName());

   /// dataset filling
   for (int i = 1; i <= hist.GetXaxis()->GetNbins(); ++i) {
      // 1 or more dimension

      Double_t xval = hist.GetXaxis()->GetBinCenter(i);
      varVec[0]->setVal(xval);

      if (varVec.size() == 1) {
         Double_t fval = hist.GetBinContent(i);
         weight.setVal(fval);
         dataFromHist->add(varsAndWeightSet, fval);
      } else { // 2 or more dimensions

         for (int j = 1; j <= hist.GetYaxis()->GetNbins(); ++j) {
            Double_t yval = hist.GetYaxis()->GetBinCenter(j);
            varVec[1]->setVal(yval);

            if (varVec.size() == 2) {
               Double_t fval = hist.GetBinContent(i, j);
               weight.setVal(fval);
               dataFromHist->add(varsAndWeightSet, fval);
            } else { // 3 dimensions

               for (int k = 1; k <= hist.GetZaxis()->GetNbins(); ++k) {
                  Double_t zval = hist.GetZaxis()->GetBinCenter(k);
                  varVec[2]->setVal(zval);

                  Double_t fval = hist.GetBinContent(i, j, k);
                  weight.setVal(fval);
                  dataFromHist->add(varsAndWeightSet, fval);
               }
            }
         }
      }
   }

   return dataFromHist;
}

TMatrixD
   ////////////////////////////////////////////////////////////////////////////////
   /// Return evaluated weights

   RooNDKeysPdfAnalytical::getWeights(const int &k) const
{
   TMatrixD mref(_nEvents, _nDim + 1);

   cxcoutD(Eval) << "RooNDKeysPdfAnalytical::getWeights() Return evaluated weights." << endl;

   for (Int_t i = 0; i < _nEvents; ++i) {
      vector<Double_t> &x = _dataPts[i];
      for (Int_t j = 0; j < _nDim; j++) {
         mref(i, j) = x[j];
      }

      vector<Double_t> &weight = (*_weights)[i];
      mref(i, _nDim) = weight[k];
   }

   return mref;
}

void
   ////////////////////////////////////////////////////////////////////////////////

   RooNDKeysPdfAnalytical::updateRho() const
{
   _rhoItr->Reset();
   RooAbsReal *rho(0);
   for (Int_t j = 0; (rho = (RooAbsReal *)_rhoItr->Next()); ++j) {
      _rho[j] = rho->getVal();
   }

   if (_nDim > 1 && _rotate) {
      TMatrixDSym covMatRho(_nDim); // covariance matrix times rho parameters
      for (Int_t j = 0; j < _nDim; j++) {
         for (Int_t k = 0; k < _nDim; k++) {
            covMatRho(j, k) = (*_covMat)(j, k) * _rho[j] * _rho[k];
         }
      }
      // find decorrelation matrix and eigenvalues (R)
      TMatrixDSymEigen evCalculatorRho(covMatRho);
      *_sigmaR = evCalculatorRho.GetEigenValues();
      for (Int_t j = 0; j < _nDim; j++) {
         (*_sigmaR)[j] = sqrt((*_sigmaR)[j]);
      }
   } else {
      for (Int_t j = 0; j < _nDim; j++) {
         (*_sigmaR)[j] = (_sigma[j] * _rho[j]);
      } // * rho
   }
}


