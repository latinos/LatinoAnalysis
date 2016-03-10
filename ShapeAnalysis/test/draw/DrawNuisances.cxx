
void DrawNuisances(std::string inputRootFile, std::string histoNominal, std::string histo_up, std::string histo_down, std::string outputDirPlots = "./" ) {
 
 gStyle->SetOptStat(0);
 
 gStyle->SetPadTopMargin(0.21);
 
 TCanvas* cc = new TCanvas("cc","",800,600);
 
 TFile* file = new TFile (inputRootFile.c_str(),"READ");

 TH1F* hNominal = (TH1F*) file->Get(histoNominal.c_str());
 hNominal->SetTitle("");
 TH1F* hUp = (TH1F*) file->Get(histo_up.c_str());
 TH1F* hDo = (TH1F*) file->Get(histo_down.c_str());

 hNominal->SetLineColor(kBlue);
 hNominal->SetLineWidth(5);

 hUp->SetLineColor(kRed);
 hUp->SetLineWidth(2);
 hUp->SetLineStyle(2);
 
 hDo->SetLineColor(kMagenta);
 hDo->SetLineWidth(2);
 hDo->SetLineStyle(2);
 
 
 hNominal->Draw("histo");
 hUp->Draw("histo same");
 hDo->Draw("histo same");
 
 TLegend* leg = new TLegend(0.1,0.8,0.9,0.99);
 leg->SetFillColor(kWhite);
 leg->AddEntry(hNominal,histoNominal.c_str(),"l");
 leg->AddEntry(hUp,histo_up.c_str(),"l");
 leg->AddEntry(hDo,histo_down.c_str(),"l");
 leg->Draw();
 
 gPad->SetGrid();
 
 
 //---- ratio plot
 TCanvas* ccRatio = new TCanvas("ccRatio","",800,600);
 TH1F* hReferenceRatio = (TH1F*) hNominal->Clone("Reference");
 hReferenceRatio->SetMaximum(1.5);
 hReferenceRatio->SetMinimum(0.5);
 hReferenceRatio->SetLineColor(kBlue);
 hReferenceRatio->SetLineWidth(5);
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
//   if (1./hReferenceRatio->GetBinContent(iBin+1) != 0) hReferenceRatio->SetBinError  (iBin+1, 1./hReferenceRatio->GetBinContent(iBin+1) * hReferenceRatio->GetBinError(iBin+1));
  hReferenceRatio->SetBinError  (iBin+1, 0.);
  hReferenceRatio->SetBinContent(iBin+1, 1.);
 }
 
 TH1F* hRatioUp = (TH1F*) hUp->Clone("Up");
 TH1F* hRatioDo = (TH1F*) hDo->Clone("Do");
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
   float ratio = 1;
   float den = hNominal->GetBinContent(iBin+1);
   if (den != 0) {
    ratio = hRatioUp->GetBinContent(iBin+1) / den;
   }
   hRatioUp -> SetBinContent(iBin+1, ratio);
   hRatioUp -> SetBinError  (iBin+1, 0.);
//    if (den != 0) hRatioUp -> SetBinError  (iBin+1, 1./den * hRatioUp->GetBinError(iBin+1));
 }
  hRatioUp->SetLineColor(kRed);
  hRatioUp->SetLineWidth(2);
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
  float ratio = 1;
  float den = hNominal->GetBinContent(iBin+1);
  if (den != 0) {
   ratio = hRatioDo->GetBinContent(iBin+1) / den;
  }
  hRatioDo -> SetBinContent(iBin+1, ratio);
  hRatioDo -> SetBinError  (iBin+1, 0.);
//   if (den != 0) hRatioDo -> SetBinError  (iBin+1, 1./den * hRatioDo->GetBinError(iBin+1));
 }
 hRatioDo->SetLineColor(kMagenta);
 hRatioDo->SetLineWidth(2);
 
 hReferenceRatio->Draw();
 hRatioUp->Draw("same");
 hRatioDo->Draw("same");
 
 leg->Draw(); 
 gPad->SetGrid();
 
 
 TString name;
 name = Form ("%s/cratio_%s.png", outputDirPlots.c_str(), histo_up.c_str());
 ccRatio->SaveAs( name.Data() );
 name = Form ("%s/cc_%s.png", outputDirPlots.c_str(), histo_up.c_str());
 cc->SaveAs( name.Data() );
 
}



