#ifndef multidraw_ExprFiller_h
#define multidraw_ExprFiller_h

#include "TTreeFormulaCached.h"
#include "FormulaLibrary.h"
#include "Reweight.h"

#include "TString.h"

#include <vector>

namespace multidraw {

  class FormulaLibrary;

  //! Filler object base class with expressions, a cut, and a reweight.
  /*!
   * Inherited by Plot (histogram) and Tree (tree). Does not own any of
   * the TTreeFormula objects by default.
   * Has a function to reweight but only through simple expressions. Can
   * in principle expand to allow reweight through histograms and graphs.
   */
  class ExprFiller {
  public:
    ExprFiller(TObject&, char const* reweight = "");
    ExprFiller(ExprFiller const&);
    virtual ~ExprFiller();

    void setPrintLevel(int l) { printLevel_ = l; }

    TObject const& getObj() const { return tobj_; }
    TObject& getObj() { return tobj_; }

    virtual unsigned getNdim() const = 0;
    TTreeFormulaCached* getFormula(unsigned i = 0) const { return compiledExprs_.at(i).get(); }
    Reweight const* getReweight() const { return compiledReweight_; }

    void bindTree(FormulaLibrary&);
    void unlinkTree();
    ExprFiller* threadClone(FormulaLibrary&);

    void initialize();
    void fill(std::vector<double> const& eventWeights, std::vector<bool> const* = nullptr);

    //! Merge the underlying object into the main-thread object
    void mergeBack();

    unsigned getCount() const { return counter_; }

  protected:
    // Special copy constructor for cloning
    ExprFiller(TObject&, ExprFiller const&);

    virtual void doFill_(unsigned) = 0;
    virtual ExprFiller* clone_() = 0;
    virtual void mergeBack_() = 0;

    TObject& tobj_;

    std::vector<TString> exprs_{};
    TString reweightExpr_{};
    double entryWeight_{1.};
    unsigned counter_{0};

    ExprFiller* cloneSource_{nullptr};

    int printLevel_{0};

    std::vector<TTreeFormulaCachedPtr> compiledExprs_{};
    Reweight* compiledReweight_{nullptr};
  };

}

#endif
