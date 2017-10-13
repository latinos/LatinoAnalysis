import opt parse
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
        else:
          print 'ERROR: No WP'
          exit()

    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # (Re)Create target variables
        self.namesOldBranchesToBeModifiedVector = [
          'std_vector_lepton_etaW' ,
          'std_vector_lepton_etaW_Up' ,
          'std_vector_lepton_etaW_Down' ,
          'std_vector_lepton_ptW' ,
          'std_vector_lepton_ptW_Up' ,
          'std_vector_lepton_ptW_Down' ,
        ]

        if self.cmssw in ElectronWP :
          if 'TightObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['TightObjWP']  :
              self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_totRecErr_'+iWP+'_Up')
              self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_totRecErr_'+iWP+'_Down')

        if self.cmssw in MuonWP :
          if 'TightObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['TightObjWP'] :
              self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_totRecErr_'+iWP+'_Up')
              self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_totRecErr_'+iWP+'_Down')

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES
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

            # Loop on leptons
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

              pt  = itree.std_vector_lepton_pt [iLep]
              eta = itree.std_vector_lepton_eta [iLep]
              flavour = itree.std_vector_lepton_flavour [iLep]


              # Electron Eta Weights
              if   abs (flavour) == 11 :
                etaW      = 1.
                etaW_Up   = 1.
                etaW_Down = 1.

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
                ptW      = 1.
                ptW_Up   = 1.
                ptW_Down = 1.

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
              if self.cmssw in ElectronWP :
                if 'TightObjWP' in ElectronWP[self.cmssw] :
                  for iWP in ElectronWP[self.cmssw]['TightObjWP']  :
                    if   abs (flavour) == 11 :
                      # FIXME How to get them in python ?????
                      eIdIso_Cent = 1.
                      eIdIso_Up   = 0.
                      eIdIso_Down = 0. 
                      eIdIso_Syst = 0.
                      # --> Total Error
                      eTot_Cent = eReco_Cent * eIdIso_Cent * etaW * ptW 
                      eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eEta_Up,2)   + math.pow(ePt_Up,2) )
                      eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eEta_Down,2) + math.pow(ePt_Down,2) )
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totRecErr_'+iWP+'_Up']   .push_back(eTot_Cent+eTot_Up)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totRecErr_'+iWP+'_Down'] .push_back(eTot_Cent-eTot_Down)
                    else:
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totRecErr_'+iWP+'_Up']   .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_electron_totRecErr_'+iWP+'_Down'] .push_back(1.)
              # Muons
              if self.cmssw in MuonWP :
                if 'TightObjWP' in MuonWP[self.cmssw] :
                  for iWP in MuonWP[self.cmssw]['TightObjWP'] :
                    if   abs (flavour) == 13. :
                      # FIXME How to get them in python ?????
                      eIdIso_Cent = 1.
                      eIdIso_Up   = 0.
                      eIdIso_Down = 0.
                      eIdIso_Syst = 0.
                      # --> Total Error
                      eTot_Cent = eReco_Cent * eIdIso_Cent * etaW * ptW
                      eTot_Up   = math.sqrt( math.pow(eReco_Up,2)   + math.pow(eIdIso_Up,2)   + math.pow(eEta_Up,2)   + math.pow(ePt_Up,2) )
                      eTot_Down = math.sqrt( math.pow(eReco_Down,2) + math.pow(eIdIso_Down,2) + math.pow(eEta_Down,2) + math.pow(ePt_Down,2) )
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totRecErr_'+iWP+'_Up']   .push_back(eTot_Cent+eTot_Up)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totRecErr_'+iWP+'_Down'] .push_back(eTot_Cent-eTot_Down)
                    else:
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totRecErr_'+iWP+'_Up']   .push_back(1.)
                      self.oldBranchesToBeModifiedVector['std_vector_muon_totRecErr_'+iWP+'_Down'] .push_back(1.)

            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

