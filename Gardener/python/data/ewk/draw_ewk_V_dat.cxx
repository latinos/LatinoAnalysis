// 
// root -l draw_ewk_V_dat.cxx
// From https://arxiv.org/pdf/1705.04664v2.pdf
// wget https://www.ippp.dur.ac.uk/~jlindert/vjets/eej.dat
//

void draw_ewk_V_dat(std::string type = "z") {
  
  std::string name = "kewk_" + type + ".dat";
  std::cout << "name = " << name << std::endl;
  std::ifstream file (name); 
  
  std::string buffer;
  int num;
  float value;
  
  float x_min[100];
  float x_max[100];
  float x_mean[100];
  float k_fact[100];
  
  
  
  while(!file.eof()) {
    getline(file,buffer);
    std::cout << "buffer = " << buffer << std::endl;
    if (buffer != "" && buffer[0] != '#'){ ///---> save from empty line at the end!
      std::stringstream line( buffer );      
      line >> x_min[num]; 
      line >> x_max[num]; 
      line >> k_fact[num];
      num++;
    } 
  }
  
  for (int i=0; i<num; i++) {
    x_mean[i] = 0.5 * (x_min[i] + x_max[i]);
  }
  
  TGraph *plot = new TGraph(num, x_mean, k_fact); 
  plot->SetMarkerColor(kBlue);
  plot->SetMarkerStyle(20);
  plot->SetMarkerSize(2);  
  plot->SetLineColor(kBlue);

  plot->Draw("APL");
  
  
  // write to file
  
  ofstream myfile;
  std::string nameOut = "kewk_" + type + "_for_python.txt";
  std::cout << "nameOut = " << nameOut << std::endl;
  myfile.open (nameOut);
  for (int i=0; i<num; i++) {
    myfile << x_mean[i] << "  " << (1+k_fact[i]) << std::endl;
  }
  myfile.close(); 
  
}

