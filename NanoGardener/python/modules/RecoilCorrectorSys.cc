///// Module taken from https://github.com/KIT-CMS/RecoilCorrections

#include "RecoilCorrectorSys.h"

RecoilCorrectorSys::RecoilCorrectorSys(TString fileName) {

  TString cmsswBase = TString( getenv ("CMSSW_BASE") );
  TString baseDir = cmsswBase + "/src";
  TString _fileName = baseDir+"/"+fileName;
  TFile * file = new TFile(_fileName);
  if (file->IsZombie()) {
    // std::cout << "file " << _fileName << " is not found...   quitting " << std::endl;
    exit(-1);
  }
  TH1D * jetBinsH = (TH1D*)file->Get("nJetBinsH");
  if (jetBinsH==NULL) {
    // std::cout << "Histogram nJetBinsH should be contained in file " << fileName << std::endl;
    // std::cout << "Check content of the file " << _fileName << std::endl;
    exit(-1);
  }

  nJetBins = jetBinsH->GetNbinsX();
  std::vector<TString> JetBins; JetBins.clear();
  for (int i=0; i<nJetBins; ++i) {
    JetBins.push_back(jetBinsH->GetXaxis()->GetBinLabel(i+1));
  }

  TString uncType[2] = {"Response",
			"Resolution"};

    TString histName = "syst";
    TH2D * hist = (TH2D*)file->Get(histName);
    if (hist==NULL) {
      // std::cout << "Histogram " << histName << " should be contained in file " << fileName << std::endl;
      // std::cout << "Check content of the file " << fileName << std::endl;
      exit(-1);
    }
    for (int xBin=0; xBin<2; ++xBin) {
      for (int yBin=0; yBin<3; ++yBin) {
	sysUnc[xBin][yBin] = hist->GetBinContent(xBin+1,yBin+1);
	// std::cout << "Systematics : "  << uncType[xBin] << " " << JetBins[yBin] << " = " << sysUnc[xBin][yBin] << std::endl;
      }
    }


    for (int j=0; j<nJetBins; ++j) {
      TString histName = JetBins[j];
      // std::cout << histName << std::endl;
      responseHist[j] = (TH1D*)file->Get(histName);
      if (responseHist[j]==NULL) {
	// std::cout << "Histogram " << histName << " should be contained in file " << fileName << std::endl;
	// std::cout << "Check content of the file " << fileName << std::endl;
	exit(-1);
      }

    }
}

void RecoilCorrectorSys::ComputeHadRecoilFromMet(float metX,
				     float metY,
				     float genVPx, 
				     float genVPy,
				     float visVPx,
				     float visVPy,
				     float & Hparal,
				     float & Hperp) {

  float genVPt = TMath::Sqrt(genVPx*genVPx+genVPy*genVPy);
  float unitX = genVPx/genVPt;
  float unitY = genVPy/genVPt;

  float unitPhi = TMath::ATan2(unitY,unitX);
  float unitPerpX = TMath::Cos(unitPhi+0.5*TMath::Pi());
  float unitPerpY = TMath::Sin(unitPhi+0.5*TMath::Pi());

  float Hx = -metX - visVPx;
  float Hy = -metY - visVPy;

  Hparal = Hx*unitX + Hy*unitY;
  Hperp = Hx*unitPerpX + Hy*unitPerpY;

}

void RecoilCorrectorSys::ComputeMetFromHadRecoil(float Hparal,
				     float Hperp,
				     float genVPx, 
				     float genVPy,
				     float visVPx,
				     float visVPy,
				     float & metX,
				     float & metY) {

  float genVPt = TMath::Sqrt(genVPx*genVPx+genVPy*genVPy);
  float unitX = genVPx/genVPt;
  float unitY = genVPy/genVPt;

  float unitPhi = TMath::ATan2(unitY,unitX);
  float unitPerpX = TMath::Cos(unitPhi+0.5*TMath::Pi());
  float unitPerpY = TMath::Sin(unitPhi+0.5*TMath::Pi());

  float det = unitX*unitPerpY - unitY*unitPerpX;
  float Hx = (Hparal*unitPerpY - Hperp*unitY)/det;
  float Hy = (Hperp*unitX - Hparal*unitPerpX)/det;

  metX = -Hx - visVPx;
  metY = -Hy - visVPy;

}

void RecoilCorrectorSys::ShiftResponseMet(float metPx,
			      float metPy,
			      float genVPx, 
			      float genVPy,
			      float visVPx,
			      float visVPy,
			      int njets,
			      float sysShift,
			      float & metShiftPx,
			      float & metShiftPy) {

  float Hparal = 0;
  float Hperp = 0;
  float genVPt = TMath::Sqrt(genVPx*genVPx+genVPy*genVPy);

  // protection against null
  if (genVPt<1.0) {
    metShiftPx = metPx;
    metShiftPy = metPy;
    return;
  }

  ComputeHadRecoilFromMet(metPx,metPy,genVPx,genVPy,visVPx,visVPy,Hparal,Hperp);

  int jets = njets; 
  if (jets>2) jets = 2; 
  if (jets<0) {
    // std::cout << "RecoilCorrectorSys::ShiftResponseMet() : Number of jets is negative !" << std::endl;
    exit(-1);
  }


  float mean = -responseHist[jets]->Interpolate(genVPt)*genVPt;
  float shift = sysShift*mean;
  Hparal = Hparal + (shift-mean);

  ComputeMetFromHadRecoil(Hparal,Hperp,genVPx,genVPy,visVPx,visVPy,metShiftPx,metShiftPy);

}

void RecoilCorrectorSys::ShiftResolutionMet(float metPx,
				float metPy,
				float genVPx, 
				float genVPy,
				float visVPx,
				float visVPy,
				int njets,
				float sysShift,
				float & metShiftPx,
				float & metShiftPy) {
 

  float Hparal = 0;
  float Hperp = 0;
  float genVPt = TMath::Sqrt(genVPx*genVPx+genVPy*genVPy);

  // protection against null
  if (genVPt<1.0) {
    metShiftPx = metPx;
    metShiftPy = metPy;
    return;
  }

  ComputeHadRecoilFromMet(metPx,metPy,genVPx,genVPy,visVPx,visVPy,Hparal,Hperp);

  int jets = njets; 
  if (jets>2) jets = 2; 
  if (jets<0) {
    // std::cout << "RecoilCorrectorSys::ShiftResponseMet() : Number of jets is negative !" << std::endl;
    exit(-1);
  }

  float mean = -responseHist[jets]->Interpolate(genVPt)*genVPt;
  Hperp = sysShift*Hperp;
  Hparal = mean + (Hparal-mean)*sysShift;

  ComputeMetFromHadRecoil(Hparal,Hperp,genVPx,genVPy,visVPx,visVPy,metShiftPx,metShiftPy);


}

void RecoilCorrectorSys::ShiftMEt(float metPx,
		      float metPy,
		      float genVPx, 
		      float genVPy,
		      float visVPx,
		      float visVPy,
		      int njets,
		      int sysType,
		      float sysShift,
		      float & metShiftPx,
		      float & metShiftPy) {

  metShiftPx=metPx;
  metShiftPy=metPy;

  if (sysType==0)
    ShiftResponseMet(metPx,
		     metPy,
		     genVPx, 
		     genVPy,
		     visVPx,
		     visVPy,
		     njets,
		     sysShift,
		     metShiftPx,
		     metShiftPy);
  else 
    ShiftResolutionMet(metPx,
		       metPy,
		       genVPx, 
		       genVPy,
		       visVPx,
		       visVPy,
		       njets,
		       sysShift,
		       metShiftPx,
		       metShiftPy);


}

void RecoilCorrectorSys::ApplyRecoilCorrectorSys(float metPx,
			 float metPy,
			 float genVPx,
			 float genVPy,
			 float visVPx,
			 float visVPy,
			 int njets,
			 int sysType,
			 int sysShift,
			 float & metShiftPx,
			 float & metShiftPy) {
 

  int jets = njets; 
  if (jets>2) jets = 2; 
  if (jets<0) {
    // std::cout << "RecoilCorrectorSys::ApplyRecoilCorrectorSys() : Number of jets is negative !" << std::endl;
    exit(-1);
  }

  int type = 0; if (sysType!=0) type = 1;

  float scale = 1 + sysUnc[type][jets];
  if (sysShift!=0) scale = 1 - sysUnc[type][jets];

  ShiftMEt(metPx,
	   metPy,
	   genVPx,
	   genVPy,
	   visVPx,
	   visVPy,
	   njets,
	   type,
	   scale,
	   metShiftPx,
	   metShiftPy);

			
}


///// Added by me: Python doesn't like getting values from "float&" operators, so do this manually instead:
float RecoilCorrectorSys::ApplyRecoilCorrectorSys_getPt(float MetPx, float MetPy, float genZPx, float genZPy, float diLepPx, float diLepPy, int njets, int sysType, int sysShift){
  float newMetPx;
  float newMetPy;
  ApplyRecoilCorrectorSys(MetPx, MetPy, genZPx, genZPy, diLepPx, diLepPy, njets, sysType, sysShift, newMetPx, newMetPy);
  return TMath::Sqrt(newMetPx*newMetPx + newMetPy*newMetPy);
}
float RecoilCorrectorSys::ApplyRecoilCorrectorSys_getPhi(float MetPx, float MetPy, float genZPx, float genZPy, float diLepPx, float diLepPy, int njets, int sysType, int sysShift){
  float newMetPx;
  float newMetPy;
  ApplyRecoilCorrectorSys(MetPx, MetPy, genZPx, genZPy, diLepPx, diLepPy, njets, sysType, sysShift, newMetPx, newMetPy);
  return TMath::ATan2(newMetPy, newMetPx);
}



