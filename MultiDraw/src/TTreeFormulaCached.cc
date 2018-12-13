#include "../interface/TTreeFormulaCached.h"

#include "TError.h"

ClassImp(TTreeFormulaCached)

TTreeFormulaCached::TTreeFormulaCached(char const* _name, char const* _formula, TTree* _tree, CachePtr const& _cache) :
  TTreeFormula(_name, _formula, _tree),
  fCache(_cache)
{
  if (!fCache)
    fCache.reset(new Cache);
}

Int_t
TTreeFormulaCached::GetNdata()
{
  if (fCache->fNdata < 0) {
    fCache->fNdata = TTreeFormula::GetNdata();
    fCache->fValues.assign(fCache->fNdata, std::pair<Bool_t, Double_t>(false, 0.));
  }

  return fCache->fNdata;
}

Double_t
TTreeFormulaCached::EvalInstance(Int_t _i, char const* _stringStack[]/* = nullptr*/)
{
  if (_i >= int(fCache->fValues.size()))
    return 0.;

  if (!fCache->fValues[_i].first) {
    fCache->fValues[_i].first = true;
    fCache->fValues[_i].second = TTreeFormula::EvalInstance(_i, _stringStack);
  }

  return fCache->fValues[_i].second;
}

struct ErrorHandlerReport {
  thread_local static Int_t lastErrorLevel;
  static void errorHandler(Int_t _level, Bool_t _abort, char const* _location, char const* _msg) {
    lastErrorLevel = _level;
    DefaultErrorHandler(_level, _abort, _location, _msg);
  }
};

thread_local Int_t ErrorHandlerReport::lastErrorLevel{0};

TTreeFormula*
NewTTreeFormula(char const* _name, char const* _expr, TTree* _tree, bool _silent/* = false*/)
{
  auto* originalErrh(SetErrorHandler(ErrorHandlerReport::errorHandler));
  auto originalIgnoreLevel(gErrorIgnoreLevel);
  if (_silent)
    gErrorIgnoreLevel = kFatal;

  auto* formula(new TTreeFormula(_name, _expr, _tree));

  if (_silent)
    gErrorIgnoreLevel = originalIgnoreLevel;

  SetErrorHandler(originalErrh);

  if (formula->GetTree() == nullptr || ErrorHandlerReport::lastErrorLevel == kError) {
    // compilation failed
    delete formula;
    return nullptr;
  }

  ErrorHandlerReport::lastErrorLevel = 0;

  return formula;
}

//! A wrapper for TTreeFormulaCached creation
TTreeFormulaCached*
NewTTreeFormulaCached(char const* _name, char const* _expr, TTree* _tree, TTreeFormulaCached::CachePtr const& _cache, bool _silent/* = false*/)
{
  auto* originalErrh(SetErrorHandler(ErrorHandlerReport::errorHandler));
  auto originalIgnoreLevel(gErrorIgnoreLevel);
  if (_silent)
    gErrorIgnoreLevel = kFatal;

  auto* formula(new TTreeFormulaCached(_name, _expr, _tree, _cache));

  SetErrorHandler(originalErrh);

  if (_silent)
    gErrorIgnoreLevel = originalIgnoreLevel;

  if (formula->GetTree() == nullptr || ErrorHandlerReport::lastErrorLevel == kError) {
    // compilation failed
    delete formula;
    return nullptr;
  }

  ErrorHandlerReport::lastErrorLevel = 0;

  return formula;
}
