#
# mu pT scales
# Run II numbers for muons 
# numbers in % for MB (abs(eta) < 2.2) 0.5% , ME (abs(eta) > 2.2) 1.5%
# numbers from https://twiki.cern.ch/twiki/bin/view/CMS/MuonScaleResolKalman#Applying_corrections
# and from https://github.com/bachtis/Analysis/blob/KaMuCa_V3/Calibration/test/test.py
# /afs/cern.ch/user/a/amassiro/Framework/CMSSW_8_0_7/src/KaMuCa/Calibration/test/
# python test.py
#leppTscaler = {}

leppTscaler['mu'] = [
    ##   pt           eta         down/up
        (   (0.0, 10.0)    ,   (0.0, 2.2)    ,   ( 0.2 ) ), 
        (   (0.0, 10.0)    ,   (2.2, 2.5)    ,   ( 0.2 ) ), 
        (   (10.0, 20.0)   ,    (0.0, 2.2)   ,   ( 0.2 ) ), 
        (   (10.0, 20.0)   ,    (2.2, 2.5)   ,   ( 0.2 ) ), 
        (   (20.0, 30.0)   ,    (0.0, 2.2)   ,   ( 0.2 ) ), 
        (   (20.0, 30.0)   ,    (2.2, 2.5)   ,   ( 0.2 ) ), 
        (   (30.0, 40.0)   ,    (0.0, 2.2)   ,   ( 0.2 ) ), 
        (   (30.0, 40.0)   ,    (2.2, 2.5)   ,   ( 0.2 ) ), 
        (   (40.0, 50.0)   ,    (0.0, 2.2)   ,   ( 0.2 ) ), 
        (   (40.0, 50.0)   ,    (2.2, 2.5)   ,   ( 0.2 ) ), 
        (   (50.0, 100.0)  ,     (0.0, 2.2)  ,   ( 0.2 ) ), 
        (   (50.0, 100.0)  ,     (2.2, 2.5)  ,   ( 0.2 ) ), 
        (   (100.0, 200.0) ,      (0.0, 2.2) ,   ( 0.2 ) ), 
        (   (100.0, 200.0) ,      (2.2, 2.5) ,   ( 0.2 ) ), 

                     ] 



