rename TrainedModel_PyKeras trainedmodel_pykeras TrainedModel_PyKeras*h5
sed -i -e 's:dataset_pymva_.*/weights/:/afs/cern.ch/user/d/ddicroce/work/Latinos/CMSSW_9_4_9/src/LatinoAnalysis/NanoGardener/python/data/DYSFmva/2016/:g' *PyKeras*xml
