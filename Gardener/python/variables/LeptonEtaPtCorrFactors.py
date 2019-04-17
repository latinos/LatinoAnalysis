import optparse
import numpy
import ROOT
import os.path
import math
 
from LatinoAnalysis.Gardener.gardening import TreeCloner

#  _                _                _____ _         ______ _     _____                          _   _              ______         _                 
# | |              | |              |  ___| |        | ___ \ |   /  __ \                        | | (_)             |  ___|       | |                
# | |     ___ _ __ | |_ ___  _ __   | |__ | |_ __ _  | |_/ / |_  | /  \/ ___  _ __ _ __ ___  ___| |_ _  ___  _ __   | |_ __ _  ___| |_ ___  _ __ ___ 
# | |    / _ \ '_ \| __/ _ \| '_ \  |  __|| __/ _` | |  __/| __| | |    / _ \| '__| '__/ _ \/ __| __| |/ _ \| '_ \  |  _/ _` |/ __| __/ _ \| '__/ __|
# | |___|  __/ |_) | || (_) | | | | | |___| || (_| | | |   | |_  | \__/\ (_) | |  | | |  __/ (__| |_| | (_) | | | | | || (_| | (__| || (_) | |  \__ \
# \_____/\___| .__/ \__\___/|_| |_| \____/ \__\__,_| \_|    \__|  \____/\___/|_|  |_|  \___|\___|\__|_|\___/|_| |_| \_| \__,_|\___|\__\___/|_|  |___/
#           | |                                                                                                                                     
#           |_|                                                                                                                                     
#
# author : X. Janssen / P. Lenzi
# purpose: correct for remaining high |eta| (and low pT) discrepancies after ID/Iso SF have been applied + compute total reco uncertainties

class LeptonEtaPtCorrFactors(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''correct for remaining high |eta| (and low pT) discrepancies after ID/Iso SF have been applied + compute total reco uncertainties'''
 
    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)

        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-w', '--wpdic',   dest='WPdic', help='WP Dictionnary', default='LatinoAnalysis/Gardener/python/variables/LeptonSel_cfg.py', type='string')

        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        self.WPdic = cmssw_base+'/src/'+opts.WPdic
        print self.WPdic
        if os.path.exists(self.WPdic) :
          handle = open(self.WPdic,'r')
          exec(handle)
          handle.close()
          self.ElectronWP = ElectronWP
          self.MuonWP = MuonWP
        else:
          print 'ERROR: No WP'
          exit()

    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # (Re)Create target variables
        self.namesOldBranchesToBeModified = [
          'electron_ptW_2l',
          'electron_ptW_2l_Up',
          'electron_ptW_2l_Down',
          'electron_ptW_3l',
          'electron_ptW_3l_Up',
          'electron_ptW_3l_Down',
          'electron_ptW_4l',
          'electron_ptW_4l_Up',
          'electron_ptW_4l_Down',
          'electron_etaW_2l',
          'electron_etaW_2l_Up',
          'electron_etaW_2l_Down',
          'electron_etaW_3l',
          'electron_etaW_3l_Up',
          'electron_etaW_3l_Down',
          'electron_etaW_4l',
          'electron_etaW_4l_Up',
          'electron_etaW_4l_Down',
        ]

        self.namesOldBranchesToBeModifiedVector = [
          'std_vector_lepton_etaW' ,
          'std_vector_lepton_etaW_Up' ,
          'std_vector_lepton_etaW_Down' ,
          'std_vector_lepton_ptW' ,
          'std_vector_lepton_ptW_Up' ,
          'std_vector_lepton_ptW_Down' ,
        ]

        if self.cmssw in self.ElectronWP :
          if 'TightObjWP' in self.ElectronWP[self.cmssw] :
            for iWP in self.ElectronWP[self.cmssw]['TightObjWP']  :
              self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_totSF_'+iWP)
              self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_totSF_'+iWP+'_Up')
              self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_totSF_'+iWP+'_Down')

        if self.cmssw in self.MuonWP :
          if 'TightObjWP' in self.MuonWP[self.cmssw] :
            for iWP in self.MuonWP[self.cmssw]['TightObjWP'] :
              self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_totSF_'+iWP)
              self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_totSF_'+iWP+'_Up')
              self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_totSF_'+iWP+'_Down')

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector+self.namesOldBranchesToBeModified)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES
        self.oldBranchesToBeModified = {}
        for bname in self.namesOldBranchesToBeModified:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModified[bname] = bvariable
        for bname, bvariable in self.oldBranchesToBeModified.iteritems(): self.otree.Branch(bname,bvariable,bname+'/F') 

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        #----------------------------------------------------------------------------------------------------
        # START TREE LOOP
        nentries = self.itree.GetEntries()
        savedentries = 0
        print 'Total number of entries: ',nentries
        print '- Starting eventloop'
        step = 5000

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Clear all vectors
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems() : bvector.clear()
            for bname, bvariable in self.oldBranchesToBeModified.iteritems(): bvariable[0] = 1.

            # Loop on leptons
            Nelec=0 
            electron_ptW_2l      = 1.
            electron_ptW_2l_Up   = 1.
            electron_ptW_2l_Down = 1.
            electron_ptW_3l      = 1.
            electron_ptW_3l_Up   = 1.
            electron_ptW_3l_Down = 1.
            electron_ptW_4l      = 1.
            electron_ptW_4l_Up   = 1.
            electron_ptW_4l_Down = 1.
            electron_etaW_2l      = 1.
            electron_etaW_2l_Up   = 1.
            electron_etaW_2l_Down = 1.
            electron_etaW_3l      = 1.
            electron_etaW_3l_Up   = 1.
            electron_etaW_3l_Down = 1.
            electron_etaW_4l      = 1.
            electron_etaW_4l_Up   = 1.
            electron_etaW_4l_Down = 1.

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              
              pt  = itree.std_vector_lepton_pt [iLep]
              eta = itree.std_vector_lepton_eta [iLep]
              flavour = itree.std_vector_lepton_flavour [iLep]
              if   abs (flavour) == 11 : Nelec+=1
          
              # Electron Eta Weights
              if   abs (flavour) == 11 :
                #****************************************
                #Minimizer is Linear
                #Chi2                      =      1663.99
                #NDf                       =           28
                #p0                        =      1.01583   +/-   0.000881267 
                #p1                        =   -0.0190406   +/-   0.00151742  
                #p2                        =   0.00696095   +/-   0.00106056  
                #p3                        =    0.0156002   +/-   0.00105578  
                #p4                        =  -0.00658065   +/-   0.000205578 
                #p5                        =  -0.00313692   +/-   0.000158679 

                # this is a one sided correction
                # we correct the central value
                # variation up is without the correction
                etaW      = 1.01583 \
                            - 0.0190406*eta \
                            + 0.00696095*(eta**2) \
                            + 0.0156002*(eta**3) \
                            - 0.00658065*(eta**4) \
                            - 0.00313692*(eta**5)
                etaW_Up   = 1.
                etaW_Down = etaW

                if iLep < 2 :
                  electron_etaW_2l       *= etaW
                  electron_etaW_2l_Up    *= etaW_Up
                  electron_etaW_2l_Down  *= etaW_Down
                if iLep < 3 :
                  electron_etaW_3l       *= etaW
                  electron_etaW_3l_Up    *= etaW_Up
                  electron_etaW_3l_Down  *= etaW_Down
                if iLep < 4 :
                  electron_etaW_4l       *= etaW
                  electron_etaW_4l_Up    *= etaW_Up
                  electron_etaW_4l_Down  *= etaW_Down

              # Muon Eta Weights  
              if   abs (flavour) == 13 :
                etaW      = 1.
                etaW_Up   = 1.
                etaW_Down = 1.

              self.oldBranchesToBeModifiedVector['std_vector_lepton_etaW']      .push_back(etaW)
              self.oldBranchesToBeModifiedVector['std_vector_lepton_etaW_Up']   .push_back(etaW_Up)
              self.oldBranchesToBeModifiedVector['std_vector_lepton_etaW_Down'] .push_back(etaW_Down)
   
              # Electron Pt Weights 
              if   abs (flavour) == 11 :
                # 10% symmetric error if pt < 25
                ptW      = 1.
                if pt < 25.:
                  ptW_Up = 1.1
                else:
                  ptW_Up   = 1.
                if pt < 25.:
                  ptW_Down = 0.9 
                else:
                  ptW_Down = 1.

                if iLep < 2 :
                  electron_ptW_2l       *= ptW
                  electron_ptW_2l_Up    *= ptW_Up
                  electron_ptW_2l_Down  *= ptW_Down
                if iLep < 3 :
                  electron_ptW_3l       *= ptW
                  electron_ptW_3l_Up    *= ptW_Up
                  electron_ptW_3l_Down  *= ptW_Down
                if iLep < 4 :
                  electron_ptW_4l       *= ptW
                  electron_ptW_4l_Up    *= ptW_Up
                  electron_ptW_4l_Down  *= ptW_Down


              # Muon Pt Weights 
              if   abs (flavour) == 13 :
                ptW      = 1.
                ptW_Up   = 1.
                ptW_Down = 1.

              self.oldBranchesToBeModifiedVector['std_vector_lepton_ptW']      .push_back(ptW)
              self.oldBranchesToBeModifiedVector['std_vector_lepton_ptW_Up']   .push_back(ptW_Up)
              self.oldBranchesToBeModifiedVector['std_vector_lepton_ptW_Down'] .push_back(ptW_Down)

              # Total error
              eEta_Up    = etaW_Up - etaW
              eEta_Down  = etaW    - etaW_Down
              ePt_Up     = ptW_Up - ptW
              ePt_Down   = ptW    - ptW_Down 
              eReco_Cent = itree.std_vector_lepton_recoW [iLep]
              eReco_Up   = itree.std_vector_lepton_recoW_Up [iLep] - eReco_Cent
              eReco_Down = eReco_Cent                              - itree.std_vector_lepton_recoW_Down  [iLep]
              # ... Electrons
              if self.cmssw in self.ElectronWP :
                if 'TightObjWP' in self.ElectronWP[self.cmssw] :
                  for iWP in self.ElectronWP[self.cmssw]['TightObjWP']  :
                    if   abs (flavour) == 11 :
                      exec ('eIdIso_Cent = itree.std_vector_electron_idisoW_'+iWP+'['+str(iLep)+']')
                      exec ('eIdIso_Up   = itree.std_vector_electron_idisoW_'+iWP+'_Up['+str(iLep)+'] - eIdIso_Cent')
                      exec ('eIdIso_Down = eIdIso_Cent - itree.std_vector_electron_idisoW_'+iWP+'_Down['+str(iLep)+']')
                      exec ('eIdIso_Syst = itree.std_vector_electron_idisoW_'+iWP+'_Syst['+str(iLep)+'] - eIdIso_Cent')
                      # --> Total Error
                      eTot_Cent = eReco_Cent * eIdIso_Cent 
                      eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eIdIso_Syst,2) )
                      eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eIdIso_Syst,2) )
                      #eTot_Cent = eReco_Cent * eIdIso_Cent * etaW * ptW 
                      #eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eEta_Up,2)   + math.pow(ePt_Up,2) )
                      #eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eEta_Down,2) + math.pow(ePt_Down,2) )
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP]         .push_back(eTot_Cent)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP+'_Up']   .push_back(eTot_Cent+eTot_Up)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP+'_Down'] .push_back(eTot_Cent-eTot_Down)
                    else:
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP]         .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP+'_Up']   .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totSF_'+iWP+'_Down'] .push_back(1.)
              # Muons
              if self.cmssw in self.MuonWP :
                if 'TightObjWP' in self.MuonWP[self.cmssw] :
                  for iWP in self.MuonWP[self.cmssw]['TightObjWP'] :
                    if   abs (flavour) == 13. :
                      exec ('eIdIso_Cent = itree.std_vector_muon_idisoW_'+iWP+'['+str(iLep)+']')
                      exec ('eIdIso_Up   = itree.std_vector_muon_idisoW_'+iWP+'_Up['+str(iLep)+'] - eIdIso_Cent')
                      exec ('eIdIso_Down = eIdIso_Cent - itree.std_vector_muon_idisoW_'+iWP+'_Down['+str(iLep)+']')
                      exec ('eIdIso_Syst = itree.std_vector_muon_idisoW_'+iWP+'_Syst['+str(iLep)+'] - eIdIso_Cent')
                      # --> Total Error
                      eTot_Cent = eReco_Cent * eIdIso_Cent 
                      eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eIdIso_Syst,2) )
                      eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eIdIso_Syst,2) )
                      #eTot_Cent = eReco_Cent * eIdIso_Cent * etaW * ptW
                      #eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eEta_Up,2)   + math.pow(ePt_Up,2) )
                      #eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eEta_Down,2) + math.pow(ePt_Down,2) )
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP]         .push_back(eTot_Cent)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP+'_Up']   .push_back(eTot_Cent+eTot_Up)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP+'_Down'] .push_back(eTot_Cent-eTot_Down)
                    else:
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP]         .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP+'_Up']   .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totSF_'+iWP+'_Down'] .push_back(1.)

            if   Nelec == 2 :
               electron_etaW_2l       = math.sqrt(electron_etaW_2l      ) 
               electron_etaW_2l_Up    = math.sqrt(electron_etaW_2l_Up   )
               electron_etaW_2l_Down  = math.sqrt(electron_etaW_2l_Down )
               electron_etaW_3l       = math.sqrt(electron_etaW_3l      ) 
               electron_etaW_3l_Up    = math.sqrt(electron_etaW_3l_Up   )
               electron_etaW_3l_Down  = math.sqrt(electron_etaW_3l_Down )
               electron_etaW_4l       = math.sqrt(electron_etaW_4l      ) 
               electron_etaW_4l_Up    = math.sqrt(electron_etaW_4l_Up   )
               electron_etaW_4l_Down  = math.sqrt(electron_etaW_4l_Down )
            elif Nelec == 3 :
               electron_etaW_3l       = math.pow(electron_etaW_3l      ,1./3.)
               electron_etaW_3l_Up    = math.pow(electron_etaW_3l_Up   ,1./3.)
               electron_etaW_3l_Down  = math.pow(electron_etaW_3l_Down ,1./3.)
               electron_etaW_4l       = math.pow(electron_etaW_4l      ,1./3.)
               electron_etaW_4l_Up    = math.pow(electron_etaW_4l_Up   ,1./3.)
               electron_etaW_4l_Down  = math.pow(electron_etaW_4l_Down ,1./3.)
            elif Nelec == 4 :
               electron_etaW_4l       = math.pow(electron_etaW_4l      ,1./4.)
               electron_etaW_4l_Up    = math.pow(electron_etaW_4l_Up   ,1./4.)
               electron_etaW_4l_Down  = math.pow(electron_etaW_4l_Down ,1./4.)
 
            self.oldBranchesToBeModified['electron_etaW_2l'][0]       = electron_etaW_2l      
            self.oldBranchesToBeModified['electron_etaW_2l_Up'][0]    = electron_etaW_2l_Up   
            self.oldBranchesToBeModified['electron_etaW_2l_Down'][0]  = electron_etaW_2l_Down 
            self.oldBranchesToBeModified['electron_etaW_3l'][0]       = electron_etaW_3l      
            self.oldBranchesToBeModified['electron_etaW_3l_Up'][0]    = electron_etaW_3l_Up   
            self.oldBranchesToBeModified['electron_etaW_3l_Down'][0]  = electron_etaW_3l_Down 
            self.oldBranchesToBeModified['electron_etaW_4l'][0]       = electron_etaW_4l      
            self.oldBranchesToBeModified['electron_etaW_4l_Up'][0]    = electron_etaW_4l_Up   
            self.oldBranchesToBeModified['electron_etaW_4l_Down'][0]  = electron_etaW_4l_Down 

            self.oldBranchesToBeModified['electron_ptW_2l'][0]       = electron_ptW_2l      
            self.oldBranchesToBeModified['electron_ptW_2l_Up'][0]    = electron_ptW_2l_Up   
            self.oldBranchesToBeModified['electron_ptW_2l_Down'][0]  = electron_ptW_2l_Down 
            self.oldBranchesToBeModified['electron_ptW_3l'][0]       = electron_ptW_3l      
            self.oldBranchesToBeModified['electron_ptW_3l_Up'][0]    = electron_ptW_3l_Up   
            self.oldBranchesToBeModified['electron_ptW_3l_Down'][0]  = electron_ptW_3l_Down 
            self.oldBranchesToBeModified['electron_ptW_4l'][0]       = electron_ptW_4l    
            self.oldBranchesToBeModified['electron_ptW_4l_Up'][0]    = electron_ptW_4l_Up   
            self.oldBranchesToBeModified['electron_ptW_4l_Down'][0]  = electron_ptW_4l_Down 



            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

