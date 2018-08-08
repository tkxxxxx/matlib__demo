# matlib__demo
import numpy as np

def loaddata():
    data = open('13_2017.csv','r').readlines()
    #data = [l.split(',') for l in data]
    lats = [np.float(l[10]) for l in data[1:]]
    lons = [np.float(l[11]) for l in data[1:]]
    souon = [np.float(l[6]) for l in data[1:]]

    return {'lats':lats,'lons':lons,'souon':souon}
