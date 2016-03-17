void DrawCompare(std::string var, int nbin, float min, float max, std::string weightAndCut = "1") {
 
 weightAndCut = "(" + weightAndCut + ")*( GEN_weight_SM/abs(GEN_weight_SM) )";
 
 TTree* myTree_0 = (TTree*) _file0 -> Get("latino");
 TH1F* h_0 = new TH1F("h_0","",nbin,min,max);
 h_0->Sumw2();
 TString toDraw_0 = Form ("%s >> h_0", var.c_str());
 myTree_0->Draw(toDraw_0.Data(),weightAndCut.c_str(),"");
 float normalization_0 = h_0 -> Integral(-1,-1);
 h_0->Scale(1./normalization_0);
 
 TTree* myTree_1 = (TTree*) _file1 -> Get("latino");
 TH1F* h_1 = new TH1F("h_1","",nbin,min,max);
 h_1->Sumw2();
 TString toDraw_1 = Form ("%s >> h_1", var.c_str());
 myTree_1->Draw(toDraw_1.Data(),weightAndCut.c_str(),"");
 float normalization_1 = h_1 -> Integral(-1,-1);
 h_1->Scale(1./normalization_1);
 
 h_0->SetLineColor(kRed);
 h_1->SetLineColor(kBlue);
 
 h_0->SetLineWidth(2);
 h_1->SetLineWidth(2);
 
 
 h_0->Draw("E");
 h_1->Draw("Esame");
 
 h_0->GetXaxis()->SetTitle(var.c_str());
 h_0->SetTitle(weightAndCut.c_str());
 
 gPad->SetLogy();
 gPad->SetGrid();
 
}
