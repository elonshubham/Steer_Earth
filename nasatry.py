import h5py

def Mylogger(msg):
    """Sends Out messages"""
    print(str(msg))
    f = open('InfoLog.txt', 'a')
    f.write('\n'+ '{}'.format(msg))
    f.close()


datafile = h5py.File('nasadata.HDF5', 'r')
for k in datafile['Grid'].keys():
    Mylogger('Dataset name: {}'.format(k))
    Mylogger('Dataset shape: {}'.format(datafile['Grid'][k].shape))
    Mylogger('Dataset type: {}'.format(datafile['Grid'][k].dtype))
    Mylogger(datafile['Grid'][k][()])