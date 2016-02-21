void DrawPDF(std::string var, int nbin, float min, float max, std::string weightAndCut = "1", int MAXPDF = 30, int STARTPOINTPDF = 9) {
 
 TCanvas* cc = new TCanvas("cc","",800,600);
 
 TTree* myTree = (TTree*) _file0 -> Get("latino");
 TH1F* h[200];
 
 
 TH1F* hReference = new TH1F("Reference","",nbin,min,max); ;
 TString toDrawReference = Form ("%s >> Reference", var.c_str());
 myTree -> Draw(toDrawReference.Data(),weightAndCut.c_str(),"");
 hReference->SetMaximum(1.5 * hReference->GetMaximum());
 hReference->SetLineColor(kBlue);
 hReference->SetLineWidth(2);

 TLegend* leg = new TLegend(0.1,0.7,0.48,0.9);
 leg->AddEntry(hReference,"Reference","l");
 
 for (int iHisto = 0; iHisto < MAXPDF; iHisto++) {
  TString nameHisto = Form ("h_%d",iHisto);
  h[iHisto] = new TH1F(nameHisto.Data(),"",nbin,min,max); 
  h[iHisto]->Sumw2();
  TString toDraw = Form ("%s >> %s", var.c_str(),nameHisto.Data());
  TString toCut  = Form ("(%s) * (std_vector_LHE_weight[%d]/std_vector_LHE_weight[0])", weightAndCut.c_str(), iHisto+STARTPOINTPDF);
  myTree -> Draw(toDraw.Data(),toCut.Data(),"");
  h[iHisto]->SetLineColor(TColor::GetColorBright(iHisto));
  h[iHisto]->SetLineWidth(2);
  leg->AddEntry(h[iHisto],nameHisto,"l");
 }

 hReference->Draw("histo");
 hReference->GetXaxis()->SetTitle(var.c_str());
 
 for (int iHisto = 0; iHisto < MAXPDF; iHisto++) {
  h[iHisto]->Draw("histo same");  
 }

 leg->Draw();
 
//  gPad->SetLogy();
 gPad->SetGrid();
 
 
 //---- ratio plot
 TCanvas* ccRatio = new TCanvas("ccRatio","",800,600);
 TH1F* hReferenceRatio = new TH1F("Reference","",nbin,min,max); ;
 hReferenceRatio->SetMaximum(1.5);
 hReferenceRatio->SetMinimum(0.5);
 hReferenceRatio->SetLineColor(kBlue);
 hReferenceRatio->SetLineWidth(2);
 
 for (int iBin = 0; iBin < nbin; iBin++) {
  hReferenceRatio->SetBinContent(iBin+1, 1.);
 }
  
 TH1F* hRatio[200];
  
 for (int iHisto = 0; iHisto < MAXPDF; iHisto++) {
  TString nameHisto = Form ("hRatio_%d",iHisto);
  hRatio[iHisto] = new TH1F(nameHisto.Data(),"",nbin,min,max); 
  for (int iBin = 0; iBin < nbin; iBin++) {
   float ratio = 1;
   float den = hReference->GetBinContent(iBin+1);
   
   if (den != 0) {
    ratio = h[iHisto]->GetBinContent(iBin+1) / den;
   }
   
   hRatio[iHisto] -> SetBinContent(iBin+1, ratio);
  }
  
  hRatio[iHisto]->SetLineColor(TColor::GetColorBright(iHisto));
  hRatio[iHisto]->SetLineWidth(2);
 }
 
 hReferenceRatio->Draw("histo");
 hReferenceRatio->GetXaxis()->SetTitle(var.c_str());
 hReferenceRatio->GetYaxis()->SetTitle("varied / nominal");
 
 for (int iHisto = 0; iHisto < MAXPDF; iHisto++) {
  hRatio[iHisto]->Draw("histo same");  
 }
 
 gPad->SetGrid();
 
 
 
}



