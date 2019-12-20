rename TrainedModel_PyKeras trainedmodel_pykeras TrainedModel_PyKeras*h5
sed -i -e 's:dataset_pymva_.*/weights/:/afs/cern.ch/user/d/ddicroce/public/DYSFmva/2016_v5/:g' *PyKeras*xml
