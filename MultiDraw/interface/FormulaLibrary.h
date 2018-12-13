#ifndef multidraw_FormulaLibrary_h
#define multidraw_FormulaLibrary_h

#include "TTreeFormulaCached.h"

#include "TString.h"

#include <map>
#include <list>
#include <memory>

class TTree;

namespace multidraw {

  class FormulaLibrary {
  public:
    FormulaLibrary(TTree&);
    ~FormulaLibrary() {}

    //! Create a new formula object with a shared cache.
    TTreeFormulaCachedPtr getFormula(char const* expr, bool silent = false);

    void updateFormulaLeaves();
    void resetCache();

    void prune();

  private:
    TTree& tree_;

    std::map<TString, TTreeFormulaCached::CachePtr> caches_{};
    std::list<std::weak_ptr<TTreeFormulaCached>> formulas_{};
  };

}

#endif
