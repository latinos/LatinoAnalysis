//histo_monoH_600_300_CMS_monoH_MVA_em_monoH_600_300_ibin_23_statUp
//histo_monoH_600_300

void DrawNuisancesStat(std::string inputRootFile, std::string histoNominal, std::string histo_up, std::string histo_down, std::string outputDirPlots = "./", std::string drawYields = "0") {
 
 gStyle->SetOptStat(0);
 
 gStyle->SetPadTopMargin(0.21);
 
 TFile* file = new TFile (inputRootFile.c_str(),"READ");

 TH1F* hNominal = (TH1F*) file->Get(histoNominal.c_str());
 hNominal->SetTitle("");
 hNominal->SetLineColor(kBlue);
 hNominal->SetLineWidth(5);
 
 TH1F* hUpTot = (TH1F*) hNominal->Clone("Up");
 hUpTot -> SetTitle("StatUp");
 TH1F* hDoTot = (TH1F*) hNominal->Clone("Do");
 hDoTot -> SetTitle("StatDown");
 
 std::string my_histo_up   = histo_up;
 std::string my_histo_down = histo_down;

 //Building StatUp and StatDo Tot Histograms
 for (int i = 1; i < hNominal->GetNbinsX()+1; i++) {
   
   my_histo_up   = histo_up;
   my_histo_up += std::to_string(i);
   my_histo_up += "_statUp";
   
   my_histo_down = histo_down;
   my_histo_down += std::to_string(i);
   my_histo_down += "_statDown";
   
   TH1F* hUp = (TH1F*) file->Get(my_histo_up.c_str());
   TH1F* hDo = (TH1F*) file->Get(my_histo_down.c_str());

   hUpTot->SetBinContent(i, hUp->GetBinContent(i));
   hDoTot->SetBinContent(i, hDo->GetBinContent(i));
 }

 hUpTot->SetLineColor(kRed);
 hDoTot->SetLineColor(kMagenta);

 hUpTot->SetLineWidth(2);
 hUpTot->SetLineStyle(2);

 hDoTot->SetLineWidth(2);
 hDoTot->SetLineStyle(2);

 Float_t max = hNominal->GetMaximum();
 if (hUpTot->GetMaximum() > max)
   max = hUpTot->GetMaximum();
 if (hDoTot->GetMaximum() > max)
   max = hDoTot->GetMaximum();
 
 hNominal->GetYaxis()->SetRangeUser(0,max*1.2);

 char legString[80];

 TLegend* leg = new TLegend(0.1,0.8,0.9,0.99);
 leg->SetFillColor(kWhite);
 if (drawYields == "1"){
   sprintf(legString,"%s: %4.2f",histoNominal.c_str(),hNominal->Integral());
   leg->AddEntry(hNominal,legString,"l");
   sprintf(legString,"StatUp: %4.2f (%4.2f %%)",hUpTot->Integral(), 100 * (hUpTot->Integral() - hNominal->Integral()) / hNominal->Integral());
   leg->AddEntry(hUpTot,legString,"l");
   sprintf(legString,"StatDown: %4.2f (%4.2f %%)",hDoTot->Integral(), 100 * (hDoTot->Integral() - hNominal->Integral()) / hNominal->Integral());
   leg->AddEntry(hDoTot,legString,"l");
 }
 else{
   leg->AddEntry(hNominal,histoNominal.c_str(),"l");
   leg->AddEntry(hUpTot,"StatUp","l");
   leg->AddEntry(hDoTot,"StatDown","l");
}


 TCanvas* cc = new TCanvas("cc","",800,600);
 cc->cd();
 hNominal->Draw("histo");
 hUpTot  ->Draw("histo,same");
 hDoTot  ->Draw("histo,same");
 leg     ->Draw("same");
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
 
 TH1F* hRatioUp = (TH1F*) hUpTot->Clone("Up");
 TH1F* hRatioDo = (TH1F*) hDoTot->Clone("Do");
 
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
 
 gPad->SetGrid();
 
 TString name;

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
 hUpTot   -> Draw("histo same");
 hDoTot   -> Draw("histo same");

 leg  -> Draw(); 
 gPad -> SetGrid();

 pad2 -> cd();

 hReferenceRatio->Draw();
 hRatioUp->Draw("same");
 hRatioDo->Draw("same");

 gPad -> SetGrid();

 name = Form ("%s/cc_%s_Full.png", outputDirPlots.c_str(), histo_up.c_str());
 ccFull->SaveAs( name.Data() );
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



