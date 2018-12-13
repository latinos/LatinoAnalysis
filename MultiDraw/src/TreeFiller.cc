#include "../interface/TreeFiller.h"
#include "../interface/FormulaLibrary.h"

#include "TDirectory.h"

#include <iostream>
#include <sstream>
#include <thread>

multidraw::TreeFiller::TreeFiller(TTree& _tree, char const* _reweight) :
  ExprFiller(_tree, _reweight)
{
  _tree.Branch("weight", &entryWeight_, "weight/D");

  bvalues_.reserve(NBRANCHMAX);
}

multidraw::TreeFiller::TreeFiller(TreeFiller const& _orig) :
  ExprFiller(_orig),
  bnames_(_orig.bnames_)
{
  auto& tree(static_cast<TTree&>(tobj_));

  tree.SetBranchAddress("weight", &entryWeight_);

  bvalues_.reserve(NBRANCHMAX);
  bvalues_ = _orig.bvalues_;

  for (unsigned iB(0); iB != bvalues_.size(); ++iB)
    tree.SetBranchAddress(bnames_[iB], &bvalues_[iB]);
}

multidraw::TreeFiller::TreeFiller(TTree& _tree, TreeFiller const& _orig) :
  ExprFiller(_tree, _orig),
  bnames_(_orig.bnames_)
{
  auto& tree(static_cast<TTree&>(tobj_));

  tree.SetBranchAddress("weight", &entryWeight_);

  bvalues_.reserve(NBRANCHMAX);
  bvalues_ = _orig.bvalues_;

  for (unsigned iB(0); iB != bvalues_.size(); ++iB)
    tree.SetBranchAddress(bnames_[iB], &bvalues_[iB]);
}

multidraw::TreeFiller::~TreeFiller()
{
  if (cloneSource_ != nullptr)
    static_cast<TTree&>(tobj_).ResetBranchAddresses();
}

void
multidraw::TreeFiller::addBranch(char const* _bname, char const* _expr)
{
  if (bvalues_.size() == NBRANCHMAX)
    throw std::runtime_error("Cannot add any more branches");

  bvalues_.resize(bvalues_.size() + 1);
  static_cast<TTree&>(tobj_).Branch(_bname, &bvalues_.back(), TString::Format("%s/D", _bname));

  bnames_.emplace_back(_bname);
  exprs_.emplace_back(_expr);
}

void
multidraw::TreeFiller::doFill_(unsigned _iD)
{
  if (printLevel_ > 3)
    std::cout << "            Fill(";

  for (unsigned iE(0); iE != compiledExprs_.size(); ++iE) {
    bvalues_[iE] = compiledExprs_[iE]->EvalInstance(_iD);

    if (printLevel_ > 3) {
      std::cout << bvalues_[iE];
      if (iE != compiledExprs_.size() - 1)
        std::cout << ", ";
    }
  }

  if (printLevel_ > 3)
    std::cout << "; " << entryWeight_ << ")" << std::endl;

  static_cast<TTree&>(tobj_).Fill();
}

multidraw::ExprFiller*
multidraw::TreeFiller::clone_()
{
  auto& myTree(static_cast<TTree&>(tobj_));

  std::stringstream name;
  name << myTree.GetName() << "_thread" << std::this_thread::get_id();

  // Thread-unsafe - in newer ROOT versions we can do new TTree(name.str().c_str(), myTree.GetTitle(), 99, myTree.GetDirectory());
  TDirectory::TContext(myTree.GetDirectory());
  auto* tree(new TTree(name.str().c_str(), myTree.GetTitle()));

  return new TreeFiller(*tree, *this);
}

void
multidraw::TreeFiller::mergeBack_()
{
  auto& sourceTree(static_cast<TTree&>(cloneSource_->getObj()));
  TObjArray arr;
  arr.Add(&tobj_);
  sourceTree.Merge(&arr);
}
