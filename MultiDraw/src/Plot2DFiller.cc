#include "../interface/Plot2DFiller.h"
#include "../interface/FormulaLibrary.h"

#include <iostream>
#include <sstream>
#include <thread>

multidraw::Plot2DFiller::Plot2DFiller(TH2& _hist, char const* _xexpr, char const* _yexpr, char const* _reweight/* = ""*/) :
  ExprFiller(_hist, _reweight)
{
  exprs_.push_back(_xexpr);
  exprs_.push_back(_yexpr);
}

multidraw::Plot2DFiller::Plot2DFiller(Plot2DFiller const& _orig) :
  ExprFiller(_orig)
{
}

multidraw::Plot2DFiller::Plot2DFiller(TH2& _hist, Plot2DFiller const& _orig) :
  ExprFiller(_hist, _orig)
{
}

void
multidraw::Plot2DFiller::doFill_(unsigned _iD)
{
  if (printLevel_ > 3) {
    std::cout << "            Fill(" << compiledExprs_[0]->EvalInstance(_iD) << ", ";
    std::cout << compiledExprs_[1]->EvalInstance(_iD) << "; " << entryWeight_ << ")" << std::endl;
  }

  double x(compiledExprs_[0]->EvalInstance(_iD));
  double y(compiledExprs_[1]->EvalInstance(_iD));
  auto& hist(static_cast<TH2&>(tobj_));

  hist.Fill(x, y, entryWeight_);
}

multidraw::ExprFiller*
multidraw::Plot2DFiller::clone_()
{
  auto& myHist(static_cast<TH2&>(tobj_));

  std::stringstream name;
  name << myHist.GetName() << "_thread" << std::this_thread::get_id();

  auto* hist(static_cast<TH2*>(myHist.Clone(name.str().c_str())));

  return new Plot2DFiller(*hist, *this);
}

void
multidraw::Plot2DFiller::mergeBack_()
{
  auto& sourceHist(static_cast<TH2&>(cloneSource_->getObj()));
  sourceHist.Add(static_cast<TH2*>(&tobj_));
}
