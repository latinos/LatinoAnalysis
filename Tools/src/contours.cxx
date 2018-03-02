TGraph* bestFit(TTree *t, TString x, TString y, TCut cut) {
    int nfind = t->Draw(y+":"+x, cut + "deltaNLL == 0");
    if (nfind == 0) {
        TGraph *gr0 = new TGraph(1);
        gr0->SetPoint(0,-999,-999);
        gr0->SetMarkerStyle(34); gr0->SetMarkerSize(2.0);
        return gr0;
    } else {
        TGraph *gr0 = (TGraph*) gROOT->FindObject("Graph")->Clone();
        gr0->SetMarkerStyle(34); gr0->SetMarkerSize(2.0);
        if (gr0->GetN() > 1) gr0->Set(1);
        return gr0;
    }
}

TList* contourPlot(TTree *t, TString x, TString y, double pmin, double pmax, TGraph *bestFit) {
    int n = t->Draw(y+":"+x, Form("%f <= quantileExpected && quantileExpected <= %f && quantileExpected != 1",pmin,pmax));
    TGraph *gr = (TGraph*) gROOT->FindObject("Graph")->Clone();
    Double_t x0 = bestFit->GetX()[0], y0 = bestFit->GetY()[0];
    Double_t *xi = gr->GetX(), *yi = gr->GetY();
    int n = gr->GetN();
    for (int i = 0; i < n; ++i) { xi[i] -= x0; yi[i] -= y0; }
    gr->Sort(&TGraph::CompareArg);
    for (int i = 0; i < n; ++i) { xi[i] += x0; yi[i] += y0; }
    TList *ret = new TList();
    ret->Add(gr);
    return ret;
}

int countGridPointsFromTree(TTree *t, TString x, TCut cut, double xmin = -1, double xmax = -1) {
    if (xmin == xmax) {
        xmin = t->GetMinimum(x);
        xmax = t->GetMaximum(x);
    }
    t->Draw(Form("%s>>h1000(1000,%10g,%10g)", x.Data(),xmin-1e-4,xmax+1e-4), cut + "deltaNLL > 0");
    TH1 *h1000 = (TH1*) gROOT->FindObject("h1000");
    int bins = 0;
    for (int i = 1, n = h1000->GetNbinsX(); i <= n; ++i) {
        if (h1000->GetBinContent(i) != 0) bins++;
    }
    h1000->Delete();
    return bins;
}
TH2 *treeToHist2D(TTree *t, TString x, TString y, TString name, TCut cut, double xmin = -1, double xmax = -1, double ymin = -1, double ymax = -1, int xbins=0, int ybins=0) {
    bool hasX = (xmin != xmax), hasY = (ymin != ymax);
    if (!hasX) {
        xmin = t->GetMinimum(x);
        xmax = t->GetMaximum(x);
    } 
    if (!hasY) {
        ymin = t->GetMinimum(y);
        ymax = t->GetMaximum(y);
    }
    if (xbins == 0) xbins = countGridPointsFromTree(t,x,cut,xmin,xmax);
    if (ybins == 0) ybins = countGridPointsFromTree(t,y,cut,ymin,ymax);
    if (!hasX) {
        double dx = (xmax-xmin)/(xbins-1);
        xmin -= 0.5*dx; xmax += 0.5*dx;
        if (fabs(xmin) < 1e-5) xmin = 0;
        if (fabs(xmax) < 1e-5) xmax = 0;
    }
    if (!hasY) {
        double dy = (ymax-ymin)/(ybins-1);
        ymin -= 0.5*dy; ymax += 0.5*dy;
        if (fabs(ymin) < 1e-5) ymin = 0;
        if (fabs(ymax) < 1e-5) ymax = 0;
    }
    //std::cout << "In making " << name << ", guessed " << xbins << " bins for " << x << " from " << xmin << " to " << xmax << std::endl;
    //std::cout << "In making " << name << ", guessed " << ybins << " bins for " << y << " from " << ymin << " to " << ymax << std::endl;
    t->Draw(Form("2*deltaNLL:%s:%s>>%s_prof(%d,%10g,%10g,%d,%10g,%10g)", y.Data(), x.Data(), name.Data(), xbins, xmin, xmax, ybins, ymin, ymax), cut + "deltaNLL != 0", "PROF");
    TH2 *prof = (TH2*) gROOT->FindObject(name+"_prof");
    TH2D *h2d = new TH2D(name, name, xbins, xmin, xmax, ybins, ymin, ymax);
    for (int ix = 1; ix <= xbins; ++ix) {
        for (int iy = 1; iy <= ybins; ++iy) {
             double z = prof->GetBinContent(ix,iy);
             if (z != z) z = (name.Contains("bayes") ? 0 : 999); // protect agains NANs
             h2d->SetBinContent(ix, iy, z);
        }
    }
    h2d->SetDirectory(0);
    return h2d;
}

TList* contourFromTH2(TH2 *h2in, double threshold, int minPoints=20) {
    std::cout << "Getting contour at threshold " << threshold << " from " << h2in->GetName() << ": " << h2in->GetNbinsX() << " x " << h2in->GetNbinsY() << " = " << h2in->GetNbinsX() * h2in->GetNbinsY() << " points total." << std::endl;
    //http://root.cern.ch/root/html/tutorials/hist/ContourList.C.html
    Double_t contours[1];
    contours[0] = threshold;
    if (h2in->GetNbinsX() * h2in->GetNbinsY() > 10000) minPoints = 50;
    if (h2in->GetNbinsX() * h2in->GetNbinsY() < 900) minPoints = 5;

    TH2D *h2 = frameTH2D((TH2D*)h2in,threshold);

    h2->SetContour(1, contours);

    // Draw contours as filled regions, and Save points
    h2->Draw("CONT Z LIST");
    gPad->Update(); // Needed to force the plotting and retrieve the contours in TGraphs


    // Get Contours
    TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
    TList* contLevel = NULL;

    if (conts == NULL || conts->GetSize() == 0){
        printf("*** No Contours Were Extracted!\n");
        return 0;
    }

    TList *ret = new TList();
    for(int i = 0; i < conts->GetSize(); i++){
        contLevel = (TList*)conts->At(i);
        printf("Contour %d has %d Graphs\n", i, contLevel->GetSize());
        for (int j = 0, n = contLevel->GetSize(); j < n; ++j) {
            TGraph *gr1 = (TGraph*) contLevel->At(j);
            printf("\t graph %d with %d points\n", j,gr1->GetN());
            if (gr1->GetN() > minPoints) ret->Add(gr1->Clone());
            //break;
        }
    }
    return ret;
}

TH2D* frameTH2D(TH2D *in, double threshold){
#if 1
        // NEW LOGIC:
        //   - pretend that the center of the last bin is on the border if the frame
        //   - add one tiny frame with huge values
        double frameValue = 1000;
        if (TString(in->GetName()).Contains("bayes")) frameValue = 0.0;

	Double_t xw = in->GetXaxis()->GetBinWidth(1);
	Double_t yw = in->GetYaxis()->GetBinWidth(1);

	Int_t nx = in->GetNbinsX();
	Int_t ny = in->GetNbinsY();

	Double_t x0 = in->GetXaxis()->GetXmin();
	Double_t x1 = in->GetXaxis()->GetXmax();

	Double_t y0 = in->GetYaxis()->GetXmin();
	Double_t y1 = in->GetYaxis()->GetXmax();
        Double_t xbins[999], ybins[999]; 
        double eps = 0.1;

        xbins[0] = x0 - eps*xw - xw; xbins[1] = x0 + eps*xw - xw;
        for (int ix = 2; ix <= nx; ++ix) xbins[ix] = x0 + (ix-1)*xw;
        xbins[nx+1] = x1 - eps*xw + 0.5*xw; xbins[nx+2] = x1 + eps*xw + xw;

        ybins[0] = y0 - eps*yw - yw; ybins[1] = y0 + eps*yw - yw;
        for (int iy = 2; iy <= ny; ++iy) ybins[iy] = y0 + (iy-1)*yw;
        ybins[ny+1] = y1 - eps*yw + yw; ybins[ny+2] = y1 + eps*yw + yw;
        
	TH2D *framed = new TH2D(
			Form("%s framed",in->GetName()),
			Form("%s framed",in->GetTitle()),
			nx + 2, xbins,
			ny + 2, ybins 
			);

	//Copy over the contents
	for(int ix = 1; ix <= nx ; ix++){
		for(int iy = 1; iy <= ny ; iy++){
			framed->SetBinContent(1+ix, 1+iy, in->GetBinContent(ix,iy));
		}
	}
	//Frame with huge values
	nx = framed->GetNbinsX();
	ny = framed->GetNbinsY();
	for(int ix = 1; ix <= nx ; ix++){
		framed->SetBinContent(ix,  1, frameValue);
		framed->SetBinContent(ix, ny, frameValue);
	}
	for(int iy = 2; iy <= ny-1 ; iy++){
		framed->SetBinContent( 1, iy, frameValue);
		framed->SetBinContent(nx, iy, frameValue);
	}

	return framed;
#else
        double frameValue = 1000;
        if (TString(in->GetName()).Contains("bayes")) frameValue = 0.0;

	Double_t xw = in->GetXaxis()->GetBinWidth(1);
	Double_t yw = in->GetYaxis()->GetBinWidth(1);

	Int_t nx = in->GetNbinsX();
	Int_t ny = in->GetNbinsY();

	Double_t x0 = in->GetXaxis()->GetXmin();
	Double_t x1 = in->GetXaxis()->GetXmax();

	Double_t y0 = in->GetYaxis()->GetXmin();
	Double_t y1 = in->GetYaxis()->GetXmax();

	TH2D *framed = new TH2D(
			Form("%s framed",in->GetName()),
			Form("%s framed",in->GetTitle()),
			nx + 2, x0-xw, x1+xw,
			ny + 2, y0-yw, y1+yw
			);

	//Copy over the contents
	for(int ix = 1; ix <= nx ; ix++){
		for(int iy = 1; iy <= ny ; iy++){
			framed->SetBinContent(1+ix, 1+iy, in->GetBinContent(ix,iy));
		}
	}
	//Frame with huge values
	nx = framed->GetNbinsX();
	ny = framed->GetNbinsY();
	for(int ix = 1; ix <= nx ; ix++){
		framed->SetBinContent(ix,  1, frameValue);
		framed->SetBinContent(ix, ny, frameValue);
	}
	for(int iy = 2; iy <= ny-1 ; iy++){
		framed->SetBinContent( 1, iy, frameValue);
		framed->SetBinContent(nx, iy, frameValue);
	}

	return framed;
#endif
}

