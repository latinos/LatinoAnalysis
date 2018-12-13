#ifndef multidraw_Cut_h
#define multidraw_Cut_h

#include "TTreeFormulaCached.h"
#include "FormulaLibrary.h"

#include "TString.h"

#include <vector>

namespace multidraw {

  class ExprFiller;

  class Cut {
  public:
    Cut(char const* name, char const* expr = "");
    ~Cut();

    TString getName() const;
    void setPrintLevel(int);

    unsigned getNFillers() const { return fillers_.size(); }
    ExprFiller const* getFiller(unsigned i) const { return fillers_.at(i); }

    void setCutExpr(char const* expr) { cutExpr_ = expr; }
    TString const& getCutExpr() const { return cutExpr_; }

    void addFiller(ExprFiller& _filler) { fillers_.push_back(&_filler); }

    void bindTree(FormulaLibrary&);
    void unlinkTree();
    Cut* threadClone(FormulaLibrary&) const;

    bool cutDependsOn(TTree const*) const;

    void initialize();
    bool evaluate();
    void fillExprs(std::vector<double> const& eventWeights);

    unsigned getCount() const { return counter_; }

  protected:
    TString name_{""};
    TString cutExpr_{""};
    std::vector<ExprFiller*> fillers_{};
    int printLevel_{0};
    unsigned counter_{0};

    std::vector<bool>* instanceMask_{nullptr};
    TTreeFormulaCachedPtr compiledCut_{nullptr};
  };

}

#endif
