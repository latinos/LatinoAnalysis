import os
import sys
import glob
import shutil

samples = [
    "WmToLNu_WmTo2J",
    "WmToLNu_ZTo2J",
    "WpToLNu_WmTo2J",
    "ZTo2L_ZTo2J",
    "WpTo2J_WmToLNu",
    "WmTo2J_ZTo2L",
    "WpToLNu_ZTo2J",
    "WpTo2J_ZTo2L",
    "WpToLNu_WpTo2J"
]

samples += [s+"_QCD" for s in samples]

basepath = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano"
trash = basepath + "/Trash/"

prods = [ "Summer16_102X_nAODv7_Full2016v7", "Fall2017_102X_nAODv7_Full2017v7","Autumn18_102X_nAODv7_Full2018v7"]
steps = ["MCl1loose{0}v7", "MCl1loose{0}v7__MCCorr{0}v7", "MCl1loose{0}v7__MCCorr{0}v7__MCCombJJLNu{0}",]

systs = [ 'JES','JER','MET','ElepT', 'MupT', 'fatjetJES', 'fatjetJER', 'fatjetJMR', 'fatjetJMS']


for prod, year in zip(prods,["2016","2017","2018"]):
    for step in steps:
        ystep = step.format(year)
        path = os.path.join(basepath, prod, ystep) 
        for s in samples:
            print path+"/nanoLatino_"+s+"__part*.root"
            files = glob.glob(path+"/nanoLatino_"+s+"__part*.root")
            for f in files: 
                try:
                    if not os.path.exists(trash+"/"+ ystep+ "/"): os.makedirs(trash+"/"+ ystep+ "/")
                    shutil.move(f, trash+"/"+ ystep+ "/")
                except Exception as e:
                    print e

for prod, year in zip(prods,["2016","2017","2018"]):
    for sys in systs:
        for d in ["up","do"]:
            step = "MCl1loose{0}v7__MCCorr{0}v7__MCCombJJLNu{0}".format(year)+"_"+sys + d
            path = os.path.join(basepath, prod, step) 
            for s in samples:
                print path+"/nanoLatino_"+s+"__part*.root"
                files = glob.glob(path+"/nanoLatino_"+s+"__part*.root")
                for f in files: 
                    try:
                        if not os.path.exists(trash+"/"+ step+ "/"): os.makedirs(trash+"/"+ step+ "/")
                        shutil.move(f, trash+"/"+ step+ "/")
                    except Exception as e:
                        print e
