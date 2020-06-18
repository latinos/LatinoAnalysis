void DrawNuisances(std::string inputRootFile, std::string histoNominal, std::string histo_up, std::string histo_down, std::string outputDirPlots = "./", std::string drawYields = "0" ) {
 
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

 hUp->SetLineColor(kGreen+2);
 hUp->SetLineWidth(2);
 hUp->SetLineStyle(3);
 
 hDo->SetLineColor(kMagenta);
 hDo->SetLineWidth(2);
 hDo->SetLineStyle(2);
 
 Float_t max = hNominal->GetMaximum();
 if (hUp->GetMaximum() > max)
   max = hUp->GetMaximum();
 if (hDo->GetMaximum() > max)
   max = hDo->GetMaximum();

 hNominal->GetYaxis()->SetRangeUser(0,max*1.2);

 hNominal->Draw("histo");
 hUp->Draw("histo same");
 hDo->Draw("histo same");
 
 TLegend* leg = new TLegend(0.1,0.8,0.9,0.99);
 leg->SetFillColor(kWhite);
 if (drawYields == "1"){
   char legString[80];
   sprintf(legString,"%s: %4.2f",histoNominal.c_str(),hNominal->Integral());
   leg->AddEntry(hNominal,legString,"l");
   sprintf(legString,"%s: %4.2f (%4.2f %%)",histo_up.c_str(), hUp->Integral(), 100 * (hUp->Integral() - hNominal->Integral()) / hNominal->Integral());
   leg->AddEntry(hUp,legString,"l");
   sprintf(legString,"%s: %4.2f (%4.2f %%)",histo_down.c_str(), hDo->Integral(), 100 * (hDo->Integral() - hNominal->Integral()) / hNominal->Integral());
   leg->AddEntry(hDo,legString,"l");
 }
 else{
   leg->AddEntry(hNominal,histoNominal.c_str(),"l");
   leg->AddEntry(hUp,histo_up.c_str(),"l");
   leg->AddEntry(hDo,histo_down.c_str(),"l");
 }

 leg->Draw();
 
 gPad->SetGrid();
 
 
 //---- ratio plot
 TCanvas* ccRatio = new TCanvas("ccRatio","",800,600);
 TH1F* hReferenceRatio = (TH1F*) hNominal->Clone("Reference");
 hReferenceRatio->SetMaximum(1.1);
 hReferenceRatio->SetMinimum(0.9);
 hReferenceRatio->SetLineColor(kBlue);
 hReferenceRatio->SetLineWidth(5);
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
//   if (1./hReferenceRatio->GetBinContent(iBin+1) != 0) hReferenceRatio->SetBinError  (iBin+1, 1./hReferenceRatio->GetBinContent(iBin+1) * hReferenceRatio->GetBinError(iBin+1));
  hReferenceRatio->SetBinError  (iBin+1, 0.);
  hReferenceRatio->SetBinContent(iBin+1, 1.);
 }
 
 TH1F* hRatioUp = (TH1F*) hUp->Clone("Up");
 TH1F* hRatioDo = (TH1F*) hDo->Clone("Do");
 
 float max_ratio = 1.5;
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
   float ratio = 1;
   float den = hNominal->GetBinContent(iBin+1);
   if (den != 0) {
    ratio = hRatioUp->GetBinContent(iBin+1) / den;
   }
   hRatioUp -> SetBinContent(iBin+1, ratio);
   hRatioUp -> SetBinError  (iBin+1, 0.);
//    if (den != 0) hRatioUp -> SetBinError  (iBin+1, 1./den * hRatioUp->GetBinError(iBin+1));
   if (max_ratio < ratio) max_ratio = ratio;
 }
  hRatioUp->SetLineColor(kGreen+2);
  hRatioUp->SetLineWidth(3);
 
 for (int iBin = 0; iBin < hReferenceRatio->GetNbinsX(); iBin++) {
  float ratio = 1;
  float den = hNominal->GetBinContent(iBin+1);
  if (den != 0) {
   ratio = hRatioDo->GetBinContent(iBin+1) / den;
  }
  hRatioDo -> SetBinContent(iBin+1, ratio);
  hRatioDo -> SetBinError  (iBin+1, 0.);
//   if (den != 0) hRatioDo -> SetBinError  (iBin+1, 1./den * hRatioDo->GetBinError(iBin+1));
  if (max_ratio < ratio) max_ratio = ratio;
 }
 hRatioDo->SetLineColor(kMagenta);
 hRatioDo->SetLineWidth(2);
 
 hReferenceRatio->Draw();
 hRatioUp->Draw("same");
 hRatioDo->Draw("same");
 
 leg->Draw(); 
 gPad->SetGrid();
 
 
 TString name;
 // name = Form ("%s/cratio_%s.png", outputDirPlots.c_str(), histo_up.c_str());
 // ccRatio->SaveAs( name.Data() );
 // name = Form ("%s/cc_%s.png", outputDirPlots.c_str(), histo_up.c_str());
 // cc->SaveAs( name.Data() );

 TCanvas* ccFull = new TCanvas("ccFull","",800,800);
 TPad*    pad1   = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
 TPad*    pad2   = new TPad("pad2", "pad2", 0, 0.0, 1, 0.3);

 pad1 -> SetTopMargin   (0.08);
 pad1 -> SetBottomMargin(0.02);
 pad1 -> Draw();

 pad2 -> SetTopMargin   (0.08);
 pad2 -> SetBottomMargin(0.35);
 pad2 -> Draw();

 pad1 -> cd();

 hNominal -> Draw("histo");
 hUp      -> Draw("histo same");
 hDo      -> Draw("histo same");

 leg  -> Draw(); 
 gPad -> SetGrid();

 pad2 -> cd();
 
 hReferenceRatio->Draw();
 float rounded_max_ratio = int( 10. * (max_ratio + 0.3) ) / 10.;
 hReferenceRatio -> GetYaxis() -> SetRangeUser(0.0, rounded_max_ratio);
 hReferenceRatio->Draw();
 hRatioUp->Draw("same");
 hRatioDo->Draw("same");

 gPad -> SetGrid();

 name = Form ("%s/cc_%s_Full.png", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );
 name = Form ("%s/cc_%s_Full.pdf", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );
 name = Form ("%s/cc_%s_Full.root", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );

 hNominal -> GetYaxis() -> SetRangeUser(0.01,max*10.);
 pad1 -> SetLogy();  

 name = Form ("%s/log_cc_%s_Full.png", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );
 name = Form ("%s/log_cc_%s_Full.pdf", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );
 name = Form ("%s/log_cc_%s_Full.root", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );

}



