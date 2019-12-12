// 
// root -l draw_ewk_V.cxx
// From https://arxiv.org/pdf/1705.04664v2.pdf
// 

void draw_ewk_V() {

  TFile* file = new TFile ("kfactors_V.root", "READ");
  TH1F* zknum = (TH1F*) file -> Get ("EWKcorr/Z"      );    zknum->SetLineColor(kBlue);        zknum->GetXaxis()->SetTitle("V p_{T} [GeV]");    
  TH1F* zkden = (TH1F*) file -> Get ("ZJets_LO/inv_pt");    zkden->SetLineColor(kRed );        zkden->GetXaxis()->SetTitle("V p_{T} [GeV]");
  TH1F* wknum = (TH1F*) file -> Get ("EWKcorr/W"      );    wknum->SetLineColor(kBlue);        wknum->GetXaxis()->SetTitle("V p_{T} [GeV]");
  TH1F* wkden = (TH1F*) file -> Get ("WJets_LO/inv_pt");    wkden->SetLineColor(kRed );        wkden->GetXaxis()->SetTitle("V p_{T} [GeV]");
  
  TH1F* zkfact = (TH1F*) zknum -> Clone("zkfact");
  TH1F* wkfact = (TH1F*) wknum -> Clone("wkfact");
  zkfact -> Divide(zkden);
  wkfact -> Divide(wkden);
  
  TCanvas* cc_Z = new TCanvas ("cc_Z", "Z", 400, 800);
  cc_Z->Divide(1,2);
  cc_Z->cd(1);
  zknum->Draw();
  zkden->Draw("same");
  
  cc_Z->cd(2);
  zkfact->Draw();
  
  
  
  TCanvas* cc_W = new TCanvas ("cc_W", "W", 400, 800);
  cc_W->Divide(1,2);
  cc_W->cd(1);
  wknum->Draw();
  wkden->Draw("same");
  
  cc_W->cd(2);
  wkfact->Draw();
  
}

