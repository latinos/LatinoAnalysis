#include "../interface/FormulaLibrary.h"

#include <iostream>
#include <sstream>

multidraw::FormulaLibrary::FormulaLibrary(TTree& _tree) :
  tree_(_tree)
{
}

TTreeFormulaCachedPtr
multidraw::FormulaLibrary::getFormula(char const* _expr, bool _silent/* = false*/)
{
  std::shared_ptr<TTreeFormulaCached::Cache> cache;

  auto fItr(caches_.find(_expr));
  if (fItr != caches_.end())
    cache = fItr->second;

  auto* formula(NewTTreeFormulaCached("formula", _expr, &tree_, cache, _silent));
  if (formula == nullptr) {
    std::stringstream ss;
    ss << "Failed to compile expression \"" << _expr << "\"";
    if (!_silent)
      std::cerr << ss.str() << std::endl;
    throw std::invalid_argument(ss.str());
  }

  if (fItr == caches_.end())
    caches_.emplace(TString(_expr), formula->GetCache());

  TTreeFormulaCachedPtr ptr(formula);
  formulas_.emplace_back(ptr);

  return ptr;
}

void
multidraw::FormulaLibrary::updateFormulaLeaves()
{
  for (auto& form : formulas_)
    form.lock()->UpdateFormulaLeaves();
}

void
multidraw::FormulaLibrary::resetCache()
{
  for (auto& ec : caches_)
    ec.second->fNdata = -1;
}

void
multidraw::FormulaLibrary::prune()
{
  auto itr(formulas_.begin());
  while (itr != formulas_.end()) {
    if (itr->expired())
      itr = formulas_.erase(itr);
    else
      ++itr;
  }
}
