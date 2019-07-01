import h5py
#f = h5py.File('TrainedModel_PyKeras_2017_0j.h5', 'r+')
#f = h5py.File('TrainedModel_PyKeras_2017_1j.h5', 'r+')
#f = h5py.File('TrainedModel_PyKeras_2017_2j.h5', 'r+')
#f = h5py.File('TrainedModel_PyKeras_2017_VBF.h5', 'r+')
#f = h5py.File('trainedmodel_pykeras_2017_0j.h5', 'r+')
#f = h5py.File('trainedmodel_pykeras_2017_1j.h5', 'r+')
#f = h5py.File('trainedmodel_pykeras_2017_2j.h5', 'r+')
f = h5py.File('trainedmodel_pykeras_2017_vbf.h5', 'r+')
del f['optimizer_weights']
f.close()
