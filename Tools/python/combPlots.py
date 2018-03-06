#!/usr/bin/env python
import ROOT
from ROOT import *
from optparse import OptionParser
from copy import deepcopy as dc
import os,sys
import numpy
from array import *
from math import *
import subprocess
import string
from scipy.stats.mstats import mquantiles
import LatinoAnalysis.Tools.rootlogonTDR
from collections import OrderedDict

gROOT.SetBatch()
gROOT.ProcessLine('.L '+os.environ['CMSSW_BASE']+'/src/LatinoAnalysis/Tools/src/contours.cxx')
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)


class combPlot :

   def __init__(self,plotsdir,blind=True,logX=False,logY=False,sLumi='',sExtra='Preliminary'):

       self.blind   = blind
       self.logX    = logX
       self.logY    = logY
       self.Results = {}
       self.Obj2Plot= {} 
       self.resetPlot()
       self.c1      = TCanvas("c1","c1",800,800)
       self.Legend  = TLegend()
       self.isSquareCanvas=False
       self.plotsdir= plotsdir
       os.system('mkdir -p '+self.plotsdir)
       gStyle.SetPalette(1) 
       self.LumiText  = sLumi
       self.ExtraText = sExtra

   def SetBatch():
       gROOT.SetBatch()

   def resetPlot(self):
       self.Obj2Plot= {} 
       self.xAxisTitle = ""
       self.yAxisTitle = ""
       self.yMin = 'AUTO'
       self.yMax = 'AUTO'
       self.xMin = 'AUTO'
       self.xMax = 'AUTO'

   def squareCanvas(self,gridx=True,gridy=True) :
       self.c1.Close()
       self.c1 = TCanvas("c1","c1",700,700);
       self.c1.cd()
       self.c1.SetRightMargin(0.05)
       self.c1.SetTopMargin(0.07)
       self.c1.SetGridy(gridy)
       self.c1.SetGridx(gridx)
       self.isSquareCanvas = True;

   def rectangleCanvas(self,gridx=True,gridy=True):
       self.c1.Close()
       self.c1 = TCanvas("c1","c1",1200,700)
       self.c1.cd()
       #self.c1.SetRightMargin(0.05)
       self.c1.SetGridy(gridy)
       self.c1.SetGridx(gridx)
       self.isSquareCanvas = False

   def defHist(self):
       self.c1.cd()
       self.h=TH1F()
       self.h.Draw()

   def Wait(self):
       self.c1.WaitPrimitive() 

   def Save(self,Name):
       self.c1.SaveAs(self.plotsdir+'/'+Name+'.pdf')
       self.c1.SaveAs(self.plotsdir+'/'+Name+'.png')
       self.c1.SaveAs(self.plotsdir+'/'+Name+'.root')
       self.c1.SaveAs(self.plotsdir+'/'+Name+'.C')

   def treeAccess(self,tree,var=[]):
        tree.SetBranchStatus('*',0)

        _lm = numpy.array(0,'d')
        _mh = numpy.array(0,'d')
        _var=[]
        for iVar in range(len(var)): _var.append(numpy.array(0,'f'))

        tree.SetBranchStatus('limit',1)
        tree.SetBranchStatus('mh'   ,1)
        tree.SetBranchAddress('limit',_lm)
        tree.SetBranchAddress('mh',   _mh)
        if len(var)>0:
          for iVar in range(len(var)):
            tree.SetBranchStatus (var[iVar],1)
            tree.SetBranchAddress(var[iVar],_var[iVar])

          return _lm, _mh, _var 
        else:
          return _lm, _mh

   def addTitle(self):
       self.c1.cd()
 
       x1=0.10
       y1=0.90
       x2=0.99
       y2=0.98
       #if iCMS == 0 :
       #  fontSize = 0.04 
       #  if self.isSquareCanvas : fontSize = 0.027 
       #else:
       #  fontSize = 0.04 
       #  if self.isSquareCanvas : fontSize = 0.033
       fontSize = 0.04
       if self.isSquareCanvas : fontSize = 0.033  
 
       self.cmsprel = TPaveText(x1,y1,x2,y2,"brtlNDC");  
       self.cmsprel.SetTextSize(fontSize*1.3);
       self.cmsprel.SetFillColor(0)
       self.cmsprel.SetFillStyle(0)
       self.cmsprel.SetLineStyle(0)
       self.cmsprel.SetLineWidth(0)
       self.cmsprel.SetTextAlign(11)
       self.cmsprel.SetTextFont(61);
       self.cmsprel.AddText("CMS");
       self.cmsprel.SetBorderSize(0);
       self.cmsprel.Draw("same");

       self.status = TPaveText(x1*2.1,y1*1.01,x2,y2,"brtlNDC");
       self.status.SetTextSize(fontSize);
       self.status.SetFillColor(0)
       self.status.SetFillStyle(0)
       self.status.SetLineStyle(0)
       self.status.SetLineWidth(0)
       self.status.SetTextAlign(11)
       self.status.SetTextFont(52);
       self.status.AddText(self.ExtraText)
       self.status.SetBorderSize(0);
       self.status.Draw("same");


       self.lumi = TPaveText(x1,y1*1.01,x2,y2,"brtlNDC");  
       self.lumi.SetTextSize(fontSize);
       self.lumi.SetFillColor(0)
       self.lumi.SetFillStyle(0)
       self.lumi.SetLineStyle(0)
       self.lumi.SetLineWidth(0)
       self.lumi.SetTextAlign(31)
       self.lumi.SetTextFont(42);
       self.lumi.AddText(self.LumiText);
       self.lumi.SetBorderSize(0);
       self.lumi.Draw("same");
       print self.LumiText 

   def plotHorizCurve(self,Name='Curv',vX=[],vCent=[],Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       if len(vCent) != nP : sys.error("plotHorizBand: size mismatch")   
       obj =  TGraph( nP , array('d',vX) ,array('d',vCent) )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(Width)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotHorizLine(self,Name='Curv',vX=[],vCent=1,Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       obj =  TGraph( nP , array('d',vX) ,array('d',[vCent]*nP) )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(Width)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotVertLine(self,Name='Curv', vCent=1, vY=[] ,Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vY)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       obj =  TGraph( nP , array('d',[vCent]*nP) , array('d',vY)  )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(2)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotHorizBand(self,Name='Band',vX=[],vCent=[],vUp=[],vDown=[],Color=90,Style=1001,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       if len(vCent) != nP : sys.error("plotHorizBand: size mismatch")   
       if len(vUp)   != nP : sys.error("plotHorizBand: size mismatch")   
       if len(vDown) != nP : sys.error("plotHorizBand: size mismatch")   
       obj = TGraphAsymmErrors( nP , array('d',vX) , array('d',vCent) , array('d',[0.]*nP), array('d',[0.]*nP) , array('d',[vCent[i]-vDown[i] for i in range(nP)]) , array('d',[vUp[i]-vCent[i] for i in range(nP)]) )
       print obj.GetFillStyle()
       obj.SetFillStyle(Style)
       obj.SetFillColor(Color)
       obj.SetLineColor(Color) 
       obj.SetLineWidth(2) 
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Band' , 'Legend' : Legend }

   def plotPoint(self,Name='Point',vX=[],vY=[],vLeft=[],vRight=[],vDown=[],vUp=[],Color=kBlack,Style=20,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotPoint: ZERO size")
       if len(vY)    != nP : sys.error("plotPoint: size mismatch")   
       if len(vUp)   != nP : sys.error("plotPoint: size mismatch")   
       if len(vDown) != nP : sys.error("plotPoint: size mismatch")  
       if len(vLeft) != nP : sys.error("plotPoint: size mismatch")  
       if len(vRight)!= nP : sys.error("plotPoint: size mismatch")  
       obj = TGraphAsymmErrors( nP , array('d',vX) , array('d',vY) , array('d',[vX[i]-vLeft[i] for i in range(nP)]) , array('d',[vRight[i]-vX[i] for i in range(nP)] ) ,  array('d',[vY[i]-vDown[i] for i in range(nP)]) , array('d',[vUp[i]-vY[i] for i in range(nP)]) )
       obj.SetLineColor(Color) 
       obj.SetLineWidth(2) 
       obj.SetMarkerStyle(Style)
       obj.SetMarkerColor(Color)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Point' , 'Legend' : Legend }

 
   def plotAllObj(self,Order=[],onTop=False):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if onTop:iFirst=False
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot]  
       for X in Order: 
         if X in self.Obj2Plot:    
           if iFirst: 
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitle(self.xAxisTitle)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitle(self.yAxisTitle)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetLabelFont (   42)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetLabelFont (   42)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleFont (   42)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleFont (   42)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleOffset( 1.2)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleOffset( 1.2)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleSize (0.050)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleSize (0.050)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetLabelSize (0.045)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetLabelSize (0.045)
           if   self.Obj2Plot[X]['Type'] == 'Band':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].Draw("A3")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("3")   
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].Draw("ALP")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("LP") 

       self.c1.Update() 

   def plotObjLeg(self,Order=[],Title='',Position='TopRight',Ncol=1):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot] 
       NLeg = len( Order ) / Ncol
       if   'Right' in Position :
         x1 = 0.47
         x2 = 0.8  
       elif 'Left'  in Position :
         x1 = 0.17
         x2 = 0.47  
         if 'Large' in Position : x2 = 0.6
       if   'Top'   in Position :
         y1 = 0.87-(NLeg+1)*.040
         if 'Large' in Position : y1 = 0.87-(NLeg+1)*.060
         y2 = 0.87 
       elif 'Bottom' in Position : 
         y1 = 0.50-(NLeg+1)*.040
         y2 = 0.50 
       #self.Legend = TLegend(0.50,0.65,0.85,0.85)   
       self.Legend = TLegend(x1,y1,x2,y2)
       if ( Ncol > 1 ) : self.Legend.SetNColumns(Ncol); 
       self.Legend.SetTextSize(0.033)
       if 'Large' in Position : self.Legend.SetTextSize(0.04)
       self.Legend.SetFillColor(0)
       self.Legend.SetFillStyle(0)
       self.Legend.SetBorderSize(0)
       self.Legend.SetTextFont (42)
       for X in Order: 
         if X in self.Obj2Plot:    
           if   self.Obj2Plot[X]['Type'] == 'Band':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'f')
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'l')
           elif self.Obj2Plot[X]['Type'] == 'Point' :
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'p')
           elif self.Obj2Plot[X]['Type'] == 'TList':
             iFirst=1
             for I in TIter(self.Obj2Plot[X]['Obj']):
               if iFirst == 1:
                 self.Legend.AddEntry(I,self.Obj2Plot[X]['Legend'],'l')
                 iFirst=0
       if not Title == '' : self.Legend.SetHeader(Title)
       self.Legend.Draw('same')


   def findCrossingOfScan1D(self,graph,threshold,leftSide,xmin=-9e99,xmax=9e99):
       x = graph.GetX();
       y = graph.GetY();
       imin = 0

       n = graph.GetN()
       for i in range(1,n):
         if (x[i] >= xmin and x[i] <= xmax): 
           if (y[i] < y[imin]):imin = i

       print leftSide,imin,n
       imatch = -1 
       if (leftSide) :
         for i in range(imin , 0 , -1):
           if (x[i] >= xmin and x[i] <= xmax): 
             if (y[i] > threshold and y[i+1] < threshold):
               imatch = i
               break
       else:
         if imin==0:imin=1
         for i in range(imin , n ):
           if (x[i] >= xmin and x[i] <= xmax): 
             if (y[i-1] < threshold and y[i] > threshold):
               imatch = i-1 
               break


       if imatch >= 0 :
         print imatch,x[imatch]
         d1 = fabs(y[imatch] - threshold)
         d2 = fabs(y[imatch+1] - threshold) 
         return (x[imatch]*d2 + x[imatch+1]*d1)/(d1+d2) 
       else :
         return -999.

   def find2DNLLScan1D(self,graph,parVal,xmin=-9e99,xmax=9e99):

       x = graph.GetX();
       y = graph.GetY();
       n = graph.GetN()
       
       val = -999
       dx  =  999 
       for i in range(1,n):
         if abs(x[i]-parVal) < dx :
            dx  = abs(x[i]-parVal) 
            val = y[i]

       return val

# ------------------  1D Likelihood Scan 


   def readMDF1D(self,fileName,iDic={},iComb='something' ): #iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFGridObs',iDic={}):
       # Get info from comfig
       
        try:
             gROOT.ProcessLine('TFile* fTree = TFile::Open("'+fileName+'")')
             gROOT.ProcessLine('TTree*  tree = (TTree*)  fTree->Get("limit")')
             keyX=iDic['Keys'][0]
             minX=str(iDic['Min'][0])
             maxX=str(iDic['Max'][0])
             minXP=str(iDic['MinPlt'][0])
             maxXP=str(iDic['MaxPlt'][0])

             print minX,maxX,minXP,maxXP

             objName=iComb
             print objName

             # Scan
             gROOT.ProcessLine('gROOT->cd()')
             gROOT.ProcessLine('int n = tree->Draw("2*deltaNLL:'+keyX+'", TCut("abs(deltaNLL) > 0. && abs(deltaNLL) < 999") );')
             gROOT.ProcessLine('TGraph *gr = (TGraph*) gROOT->FindObject("Graph")->Clone("gr");')
             ROOT.gr.SetName('gr_'+objName);
             ROOT.gr.Sort();
             self.Obj2Plot['gr__'+objName] = { 'Obj' : ROOT.gr.Clone('gr_'+objName) , 'Type' : 'Curve' , 'Legend' : ''}
             gROOT.ProcessLine('delete gr')

             # Best Fit
            
             gROOT.ProcessLine('TGraph *gr0 = (TGraph*) gROOT->FindObject("Graph")->Clone("gr0");')
             ROOT.gr0.SetName('gr0_'+objName);
             ROOT.gr0.Sort();
             ROOT.gr0.Print()
             self.Obj2Plot['gr0__'+objName] = { 'Obj' : ROOT.gr0.Clone('gr0_'+objName) , 'Type' : 'Point' , 'Legend' : ''}
             gROOT.ProcessLine('delete gr0')

             # Set some Default Style and Legend
             self.Obj2Plot['gr__'+objName]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
             #self.Obj2Plot['gr__'+objName]['Obj'].GetXaxis().SetRangeUser(minXP,maxXP)
             self.Obj2Plot['gr__'+objName]['Obj'].GetYaxis().SetTitle("-2 #Delta ln L")
             #self.Obj2Plot['gr__'+objName]['Obj'].GetYaxis().SetRangeUser(0.00001,20.)
             #self.Obj2Plot['gr0__'+objName]['Obj'].SetMarkerColor(kRed) 

             gROOT.ProcessLine('fTree->Close()') 

        except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
 
   def MDF1D(self,plotName,PlotDic,LimFiles):
       y2Sigma=3.84
         
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.xAxisTitle = PlotDic['AxisTitle'][0]
       self.yAxisTitle = '-2 #Delta ln L'
       minXP           = PlotDic['MinPlt'][0]
       maxXP           = PlotDic['MaxPlt'][0]
       minYP           = PlotDic['MinPlt'][1]
       maxYP           = PlotDic['MaxPlt'][1]
       dX              = maxXP-minXP


       # Expected         
       self.readMDF1D(LimFiles['Exp'],PlotDic,'Exp')
       objNameExp='Exp'
       if not 'gr__Exp' in self.Obj2Plot : return
       #objNameExp=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+'Exp'+Ext+self.postFix
       

       # Observed
       if (not self.blind ) : 
         self.readMDF1D(LimFiles['Obs'],PlotDic,'Obs')
         objNameObs='Obs'
         #objNameObs=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+'Obs'+Ext+self.postFix

       # Plot 
       frame = TH1F("Frame","Frame",5,float(minXP),float(maxXP))
       frame.GetXaxis().SetTitle(self.xAxisTitle) 
       frame.GetYaxis().SetTitle(self.yAxisTitle) 
       frame.GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       frame.GetXaxis().SetNdivisions(505)
       frame.GetYaxis().SetNdivisions(505)
       frame.Draw()

       LegList=[]
       if (not self.blind ) : 
         self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineWidth(2)
         self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineStyle(1)
         self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineColor(kBlack)
         self.Obj2Plot['gr__'+objNameObs]['Obj'].Draw("samel") 
         self.Obj2Plot['gr__'+objNameObs]['Legend']= 'Observed'
         LegList.append('gr__'+objNameObs)

       self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineWidth(2)
       self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineStyle(2)
       self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineColor(kBlack)
       self.Obj2Plot['gr__'+objNameExp]['Obj'].Draw("samel")
       self.Obj2Plot['gr__'+objNameExp]['Legend']= 'Expected'
       LegList.append('gr__'+objNameExp)

       Lines=['One','Four']
       self.plotHorizLine('One' , [float(minXP),float(maxXP)] , 1 , kBlack , 9    , 1 , '1sigma')
       self.plotHorizLine('Four', [float(minXP),float(maxXP)] , y2Sigma , kBlack , 9 , 1 , '2sigma')

       # Fing 1/2 Sigma X-ing
       if self.blind : gr = self.Obj2Plot['gr__'+objNameExp]['Obj']
       else          : gr = self.Obj2Plot['gr__'+objNameObs]['Obj']
       hi68 = self.findCrossingOfScan1D(gr, 1.00, False, minXP, maxXP);
       lo68 = self.findCrossingOfScan1D(gr, 1.00, True,  minXP, maxXP);
       hi95 = self.findCrossingOfScan1D(gr, y2Sigma, False, minXP, maxXP);
       lo95 = self.findCrossingOfScan1D(gr, y2Sigma, True,  minXP, maxXP);
       dnll = self.find2DNLLScan1D(gr,1.,minXP, maxXP)


       gr = self.Obj2Plot['gr__'+objNameExp]['Obj']
       hi68Exp = self.findCrossingOfScan1D(gr, 1.00, False, minXP, maxXP);
       lo68Exp = self.findCrossingOfScan1D(gr, 1.00, True,  minXP, maxXP);
       hi95Exp = self.findCrossingOfScan1D(gr, y2Sigma, False, minXP, maxXP);
       lo95Exp = self.findCrossingOfScan1D(gr, y2Sigma, True,  minXP, maxXP);
       dnllExp = self.find2DNLLScan1D(gr,1.,minXP, maxXP)

       self.plotAllObj(Lines,True)
       self.plotObjLeg(LegList,PlotDic['LegTitle'],'TopLeftLarge')
       self.addTitle()

       self.c1.cd()
       pt = TPaveText(minXP+0.04*dX,1.05,minXP+0.12*dX,1.5);
       pt.SetBorderSize(0);
       pt.SetFillColor(0);
       pt.SetFillStyle(0);
       pt.SetTextFont(42);
       pt.SetTextSize(0.025);
       text = pt.AddText("68% CL");
       pt.Draw();

       pt2 = TPaveText(minXP+0.04*dX,3.94,minXP+0.12*dX,4.3);
       pt2.SetBorderSize(0);
       pt2.SetFillColor(0);
       pt2.SetFillStyle(0);
       pt2.SetTextFont(42);
       pt2.SetTextSize(0.025);
       text = pt2.AddText("95% CL");
       pt2.Draw();

       self.c1.Update() 
       self.Save(plotName)

       # Save values
       limFile= self.plotsdir+'/'+plotName+'.txt'
       subfile = open(limFile,'w')
       subfile.write ('Exp  '+ str(lo95Exp) + ' ' + str(lo68Exp) + ' ' + str(hi68Exp) + ' ' + str(hi95Exp)+'\n')
       if not self.blind : 
         subfile.write ('Obs  '+ str(lo95)    + ' ' + str(lo68)    + ' ' + str(hi68)    + ' ' + str(hi95) +'\n' ) 
         subfile.write ('Best '+ str(self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+' '+str(hi68-self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+' '+str(lo68-self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+'\n')
           #subfile.write ('Test '+ str(dnllExp)+' '+str(dnll) +'\n')
       subfile.close()

       self.Wait()


# ------------------  2D Likelihood Scan 

   def readMDFGrid(self,fileName,iDic={},iComb='something'): #  self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFGridObs'):
         
       gROOT.ProcessLine('TFile* fTree = TFile::Open("'+fileName+'")')
       gROOT.ProcessLine('TTree*  tree = (TTree*)  fTree->Get("limit")')
       keyX=iDic['Keys'][0]
       keyY=iDic['Keys'][1]
       minX=str(iDic['Min'][0])
       minY=str(iDic['Min'][1])
       maxX=str(iDic['Max'][0])
       maxY=str(iDic['Max'][1])

       minXP=str(iDic['MinPlt'][0])
       minYP=str(iDic['MinPlt'][1])
       maxXP=str(iDic['MaxPlt'][0])
       maxYP=str(iDic['MaxPlt'][1])

       objName=keyX+'-'+keyY
       gROOT.ProcessLine('gROOT->cd()')
       gROOT.ProcessLine('TH2* h2d=0')
       gROOT.ProcessLine('TGraph *gr0=0')
       gROOT.ProcessLine('TList* c68')
       gROOT.ProcessLine('TList* c95')
       print 'h2d = treeToHist2D(tree,"'+keyX+'","'+keyY+'","'+objName+'",TCut(""),'+minX+','+maxX+','+minY+','+maxY+')'
       gROOT.ProcessLine('h2d = treeToHist2D(tree,"'+keyX+'","'+keyY+'","'+objName+'",TCut(""),'+minX+','+maxX+','+minY+','+maxY+')')
       #if iModel == 'cVcF' and iTarget== 'MDFGridObs' : ROOT.h2d.Fill(0.67,1.5399999,2.30)
       gROOT.ProcessLine('c68 = contourFromTH2(h2d,2.30)')
       gROOT.ProcessLine('c95 = contourFromTH2(h2d,5.99)')
       gROOT.ProcessLine('gr0 = bestFit(tree,"'+keyX+'","'+keyY+'",TCut(""))')
       ROOT.gr0.Print()
       objName=iComb
       self.Obj2Plot['h2d__'+objName] = { 'Obj' : ROOT.h2d.Clone('h2d'+objName) , 'Type' : 'TH2D'  , 'Legend' : ''}
       self.Obj2Plot['c68__'+objName] = { 'Obj' : ROOT.c68.Clone('c68'+objName) , 'Type' : 'TList' , 'Legend' : ''}
       self.Obj2Plot['c95__'+objName] = { 'Obj' : ROOT.c95.Clone('c95'+objName) , 'Type' : 'TList' , 'Legend' : ''}
       self.Obj2Plot['gr0__'+objName] = { 'Obj' : ROOT.gr0.Clone('gr0'+objName) , 'Type' : 'Point' , 'Legend' : ''}
       print self.Obj2Plot['h2d__'+objName],self.Obj2Plot['h2d__'+objName]['Obj']
       gROOT.ProcessLine('delete h2d')
       gROOT.ProcessLine('delete c68')
       gROOT.ProcessLine('delete c95')
       gROOT.ProcessLine('delete gr0')
       # Set some Default Style and Legend
       self.Obj2Plot['h2d__'+objName]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
       self.Obj2Plot['h2d__'+objName]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
       self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
       self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
       self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetRangeUser(0.00001,20.)
       #for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineColor(kRed) 
       for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineWidth(3) 
       #for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineColor(kRed) 
       for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineWidth(3) 
       for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineStyle(2) 
       #self.Obj2Plot['gr0__'+objName]['Obj'].SetMarkerColor(kRed) 
       gROOT.ProcessLine('fTree->Close()') 

   def MDF2D(self,plotName,PlotDic,LimFiles):

       self.squareCanvas(False,False)
       self.c1.cd()
       self.c1.SetLeftMargin(0.15) 
       self.c1.SetRightMargin(0.2) 
       self.c1.SetTopMargin(0.07) 
       #self.c1.SetLogz()
       self.resetPlot()
       
       self.xAxisTitle = PlotDic['AxisTitle'][0]
       self.yAxisTitle = PlotDic['AxisTitle'][1]

       minXP= PlotDic['MinPlt'][0]
       minYP= PlotDic['MinPlt'][1]
       maxXP= PlotDic['MaxPlt'][0]
       maxYP= PlotDic['MaxPlt'][1]

       self.readMDFGrid(LimFiles['Exp'],PlotDic,'Exp')
       objNameExp='Exp'
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].Draw("colz")  
       self.Obj2Plot['c68__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['c95__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].Draw("samep")  
       self.addTitle()
       self.c1.Update() 
       self.Save(plotName+'_Exp')
       #self.Wait()

       # Observed 
       if (not self.blind ) : 
         self.readMDFGrid(LimFiles['Obs'],PlotDic,'Obs')
         objNameObs='Obs'
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].Draw("colz")  
         self.Obj2Plot['c68__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['c95__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")  
         self.addTitle()
         self.c1.Update() 
         self.Save(plotName+'_Obs')
         #self.Wait()

       
       self.c1.SetRightMargin(0.05)
       self.c1.SetLogz(False)
       
       frame = TH1F("Frame","Frame",5,float(minXP),float(maxXP))
       frame.GetXaxis().SetTitle(self.xAxisTitle) 
       frame.GetYaxis().SetTitle(self.yAxisTitle) 
       frame.GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       frame.GetXaxis().SetNdivisions(505)
       frame.GetYaxis().SetNdivisions(505)
       frame.Draw()
       self.Obj2Plot['c68__'+objNameExp]['Legend'] = '68% CL Expected'
       self.Obj2Plot['c95__'+objNameExp]['Legend'] = '95% CL Expected'
       self.Obj2Plot['c68__'+objNameExp]['Obj'].Draw("same")  
       for X in TIter(self.Obj2Plot['c95__'+objNameExp]['Obj']) : X.SetLineStyle(2) 
       self.Obj2Plot['c95__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].SetMarkerStyle(22)
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].Draw("samep")  
       self.Obj2Plot['gr0__'+objNameExp]['Legend']= 'Exp. for SM'
       LegList = ['gr0__'+objNameExp,'c68__'+objNameExp,'c95__'+objNameExp]
    
       if (not self.blind ) :
         self.Obj2Plot['c68__'+objNameObs]['Legend'] = '68% CL Observed'
         self.Obj2Plot['c95__'+objNameObs]['Legend'] = '95% CL Observed'
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].SetMarkerColor(kRed)  
         for X in TIter(self.Obj2Plot['c68__'+objNameObs]['Obj']) : X.SetLineColor(kRed) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineColor(kRed) 
         for X in TIter(self.Obj2Plot['c68__'+objNameObs]['Obj']) : X.SetLineWidth(3) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineWidth(3) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineStyle(2) 
         self.Obj2Plot['c68__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['c95__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")  
         self.Obj2Plot['gr0__'+objNameObs]['Legend']= 'Observed'
         LegList = ['gr0__'+objNameObs,'c68__'+objNameObs,'c95__'+objNameObs,'gr0__'+objNameExp,'c68__'+objNameExp,'c95__'+objNameExp]
       

       self.plotObjLeg(LegList,PlotDic['LegTitle'],'TopLeft')
       

       self.addTitle()
       self.c1.Update() 
       self.Save(plotName)
 


