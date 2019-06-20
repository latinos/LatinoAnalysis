def mlj(pt1,eta1,phi1,pt2,eta2,phi2):
  l=ROOT.TLorentzVector()
  l.SetPtEtaPhiM(pt1,eta1,phi1,0.)
  j=ROOT.TLorentzVector()
  j.SetPtEtaPhiM(pt2,eta2,phi2,0.)
  return (l+j).M()

self.mlj = mlj

self.method = "BDTG"

self.weightsPath = "LatinoAnalysis/Gardener/python/data/TMVAMulticlass_BDTG_Mattia1.weights.xml"

self.inputVariables = [
"mjj",
"mll",
"ptll",
"detajj",
"dphill",
"std_vector_jet_pt[0]",
"std_vector_jet_pt[1]",
"std_vector_jet_eta[0]",
"std_vector_jet_eta[1]",
"(abs(2*std_vector_lepton_eta[0]-std_vector_jet_eta[0]-std_vector_jet_eta[1])+abs(2*std_vector_lepton_eta[1]-std_vector_jet_eta[0]-std_vector_jet_eta[1]))/detajj",
"mlj(std_vector_lepton_pt[0],std_vector_lepton_eta[0],std_vector_lepton_phi[0],std_vector_jet_pt[0],std_vector_jet_eta[0],std_vector_jet_phi[0])",
"mlj(std_vector_lepton_pt[0],std_vector_lepton_eta[0],std_vector_lepton_phi[0],std_vector_jet_pt[1],std_vector_jet_eta[1],std_vector_jet_phi[1])",
"mlj(std_vector_lepton_pt[1],std_vector_lepton_eta[1],std_vector_lepton_phi[1],std_vector_jet_pt[0],std_vector_jet_eta[0],std_vector_jet_phi[0])",
"mlj(std_vector_lepton_pt[1],std_vector_lepton_eta[1],std_vector_lepton_phi[1],std_vector_jet_pt[1],std_vector_jet_eta[1],std_vector_jet_phi[1])",
"std_vector_jet_cmvav2[0]",
"std_vector_jet_cmvav2[1]", 
]

self.outputBranches = [
"class0",
"class1",
"class2",
"class3",
]

self.inputFormulas = [
"event.mjj",
"event.mll",
"event.ptll",
"event.detajj",
"event.dphill",
"event.std_vector_jet_pt[0]",
"event.std_vector_jet_pt[1]",
"event.std_vector_jet_eta[0]",
"event.std_vector_jet_eta[1]",
"(abs(2*event.std_vector_lepton_eta[0]-event.std_vector_jet_eta[0]-event.std_vector_jet_eta[1])+abs(2*event.std_vector_lepton_eta[1]-event.std_vector_jet_eta[0]-event.std_vector_jet_eta[1]))/event.detajj",
"self.mlj(event.std_vector_lepton_pt[0],event.std_vector_lepton_eta[0],event.std_vector_lepton_phi[0],event.std_vector_jet_pt[0],event.std_vector_jet_eta[0],event.std_vector_jet_phi[0])",
"self.mlj(event.std_vector_lepton_pt[0],event.std_vector_lepton_eta[0],event.std_vector_lepton_phi[0],event.std_vector_jet_pt[1],event.std_vector_jet_eta[1],event.std_vector_jet_phi[1])",
"self.mlj(event.std_vector_lepton_pt[1],event.std_vector_lepton_eta[1],event.std_vector_lepton_phi[1],event.std_vector_jet_pt[0],event.std_vector_jet_eta[0],event.std_vector_jet_phi[0])",
"self.mlj(event.std_vector_lepton_pt[1],event.std_vector_lepton_eta[1],event.std_vector_lepton_phi[1],event.std_vector_jet_pt[1],event.std_vector_jet_eta[1],event.std_vector_jet_phi[1])",
"event.std_vector_jet_cmvav2[0]",
"event.std_vector_jet_cmvav2[1]",
]
