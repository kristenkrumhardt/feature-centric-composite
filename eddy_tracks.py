import numpy as np
import scipy.io as sio

def track_mat2py(file_track):
    #-- read .mat
    matdata = sio.loadmat(file_track,
                          struct_as_record = False,
                          squeeze_me = True)
    data = matdata['eddies']
    
    # u: azimuthal speed   
    fld = [ 'x', 'y', 'amp', 'area', 'u', 'age', 'Ls', 'id', 'cyc','track_day']
    eddy = {}
    for f in fld:
        if any([f == ff for ff in ['id','cyc']]) :
            eddy[f] = getattr(data,f).astype(int)
        elif f == 'age':
            eddy[f] = getattr(data,f).astype(float) * 5.
        elif f == 'track_day':
            ymmdd = getattr(data,f).astype(float)
            eddy['year'] = np.round(ymmdd / 1.0e4).astype(int)
            eddy['mon'] = np.round((ymmdd-eddy['year']*1.0e4)/1e2).astype(int)
            eddy['day'] = np.round((ymmdd-eddy['year']*1.0e4 - eddy['mon']*1e2)).astype(int)
        else:
            eddy[f] = getattr(data,f).astype(float)
    return eddy
