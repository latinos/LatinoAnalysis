{ 
 
 
 
 //  TFile fileNominal("MyRatioWWpTHistogram.root","READ");
 TFile fileNominal("MyNewRatioWWpTHistogram.root","READ");
 
 TH1F* histo = (TH1F*) fileNominal.Get("wwpt");
 ofstream myfile;
 myfile.open ("central.dat");
 for (int iBin =0; iBin < histo->GetNbinsX(); iBin++) {
  myfile << "  " << histo->GetBinCenter(iBin+1) << "     "
  << histo->GetBinContent(iBin+1) << std::endl;
 }
 myfile.close(); 
 
 
 
 
 
 TFile file("MyNLLErrorsHistogram.root","READ");
 //  TH1F* histo_scaleup = (TH1F*) file.Get("wwpt_scaleup");
 //  for (int iBin =0; iBin < histo_scaleup->GetNbinsX(); iBin++) {
 //   std::cout << "  " << histo_scaleup->GetBinCenter(iBin+1) << "     "
 //             << histo_scaleup->GetBinContent(iBin+1) << std::endl;
 //  }
 
 
 TH1F* histo_scaleup = (TH1F*) file.Get("wwpt_scaleup");
 ofstream myfile_scale_up;
 myfile_scale_up.open ("scale_up.dat");
 for (int iBin =0; iBin < histo_scaleup->GetNbinsX(); iBin++) {
  myfile_scale_up << "  " << histo_scaleup->GetBinCenter(iBin+1) << "     "
  << histo_scaleup->GetBinContent(iBin+1) << std::endl;
 }
 myfile_scale_up.close(); 
 
 
 TH1F* histo_scaledown = (TH1F*) file.Get("wwpt_scaledown");
 ofstream myfile_scale_down;
 myfile_scale_down.open ("scale_down.dat");
 for (int iBin =0; iBin < histo_scaledown->GetNbinsX(); iBin++) {
  myfile_scale_down << "  " << histo_scaledown->GetBinCenter(iBin+1) << "     "
  << histo_scaledown->GetBinContent(iBin+1) << std::endl;
 }
 myfile_scale_down.close(); 
 
 
 
 TH1F* histo_resumup = (TH1F*) file.Get("wwpt_resumup");
 ofstream myfile_resum_up;
 myfile_resum_up.open ("resum_up.dat");
 for (int iBin =0; iBin < histo_resumup->GetNbinsX(); iBin++) {
  myfile_resum_up << "  " << histo_resumup->GetBinCenter(iBin+1) << "     "
  << histo_resumup->GetBinContent(iBin+1) << std::endl;
 }
 myfile_resum_up.close(); 
 
 
 TH1F* histo_resumdown = (TH1F*) file.Get("wwpt_resumdown");
 ofstream myfile_resum_down;
 myfile_resum_down.open ("resum_down.dat");
 for (int iBin =0; iBin < histo_resumdown->GetNbinsX(); iBin++) {
  myfile_resum_down << "  " << histo_resumdown->GetBinCenter(iBin+1) << "     "
  << histo_resumdown->GetBinContent(iBin+1) << std::endl;
 }
 myfile_resum_down.close(); 
 
 
 
 
 
 
 
 
}


