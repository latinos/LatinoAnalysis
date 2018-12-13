#include "../interface/Plot1DFiller.h"
#include "../interface/FormulaLibrary.h"

#include <iostream>
#include <sstream>
#include <thread>

multidraw::Plot1DFiller::Plot1DFiller(TH1& _hist, char const* _expr, char const* _reweight/* = ""*/, Plot1DFiller::OverflowMode _mode/* = kDefault*/) :
  ExprFiller(_hist, _reweight),
  overflowMode_(_mode)
{
  exprs_.emplace_back(_expr);
}

multidraw::Plot1DFiller::Plot1DFiller(Plot1DFiller const& _orig) :
  ExprFiller(_orig),
  overflowMode_(_orig.overflowMode_)
{
}

multidraw::Plot1DFiller::Plot1DFiller(TH1& _hist, Plot1DFiller const& _orig) :
  ExprFiller(_hist, _orig),
  overflowMode_(_orig.overflowMode_)
{
}

void
multidraw::Plot1DFiller::doFill_(unsigned _iD)
{
  if (printLevel_ > 3)
    std::cout << "            Fill(" << compiledExprs_[0]->EvalInstance(_iD) << "; " << entryWeight_ << ")" << std::endl;

  double x(compiledExprs_[0]->EvalInstance(_iD));
  auto& hist(static_cast<TH1&>(tobj_));

  switch (overflowMode_) {
  case OverflowMode::kDefault:
    break;
  case OverflowMode::kDedicated:
    if (x > hist.GetXaxis()->GetBinLowEdge(hist.GetNbinsX()))
      x = hist.GetXaxis()->GetBinLowEdge(hist.GetNbinsX());
    break;
  case OverflowMode::kMergeLast:
    if (x > hist.GetXaxis()->GetBinUpEdge(hist.GetNbinsX()))
      x = hist.GetXaxis()->GetBinLowEdge(hist.GetNbinsX());
    break;
  }

  hist.Fill(x, entryWeight_);
}

multidraw::ExprFiller*
multidraw::Plot1DFiller::clone_()
{
  auto& myHist(static_cast<TH1&>(tobj_));

  std::stringstream name;
  name << myHist.GetName() << "_thread" << std::this_thread::get_id();

  auto* hist(static_cast<TH1*>(myHist.Clone(name.str().c_str())));

  return new Plot1DFiller(*hist, *this);
}

void
multidraw::Plot1DFiller::mergeBack_()
{
  auto& sourceHist(static_cast<TH1&>(cloneSource_->getObj()));
  sourceHist.Add(static_cast<TH1*>(&tobj_));
}
