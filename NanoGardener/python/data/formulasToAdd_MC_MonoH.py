formulas = {}

# Common Weights

formulas['SFweight2lMH'] = 'event.puWeight*\
                          event.MHTriggerEffWeight_2l*\
                          event.Lepton_RecoSF[0]*\
                          event.Lepton_RecoSF[1]*\
                          event.EMTFbug_veto \
                          if event.nLepton > 1 else 0.'

