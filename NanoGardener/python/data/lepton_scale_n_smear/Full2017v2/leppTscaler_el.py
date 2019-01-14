#
# lepton pT scales
# Run II 2017 uncertainties: From https://indico.cern.ch/event/697082/contributions/3018397/attachments/1656254/2651425/2018-05-25-EGM-ScalesSmearings.pdf
# decided to use 0.2%; and 0.5% for >500 GeV
# numbers in % 

leppTscaler['ele'] = [
    #  pt               eta         down/up
    ( (0.0, 500.0),    (0.0, 2.5), (0.2)  ),
    ( (500.0, 1000.0), (0.0, 2.5), (0.5) ),

] 
