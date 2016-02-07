void drawBasew(TString nameFile){
 
 TFile file (nameFile.Data(), "READ");
 TTree* latino = (TTree*) file.Get("latino");
 
 float baseW;
 latino->SetBranchAddress("baseW", &baseW);
 latino->GetEntry(0);
 
 std::cout << " " << nameFile.Data() << "   " << baseW << std::endl;
 
 ofstream myfile;
 myfile.open ("out.txt",std::ofstream::app);
 myfile << nameFile.Data() << "   " << baseW  << " --> " <<  1./baseW  << " fb-1 " <<  std::endl;
 myfile.close(); 
 
 
}