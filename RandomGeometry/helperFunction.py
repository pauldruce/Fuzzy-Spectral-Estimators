# @Author: Paul Druce <pauldruce>
# @Date:   2020-06-21T17:54:48+01:00
# @Email:  pjdruce@gmail.com
# @Last modified by:   pauldruce
# @Last modified time: 2020-06-23T14:32:26+01:00



import os
import glob

import numpy as np

import uncertainties as unc
from uncertainties import unumpy as unp
from uncertainties.umath import *

import re


def atof(text):
    return float(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atof(c) for c in re.split('_', text) ]

num_cols=1
converters = dict.fromkeys(range(num_cols),lambda col_bytes: unc.ufloat_fromstr(col_bytes.decode("latin1")))

# This function sets up some useful variables for the random fuzzy geometry.
# It defines the available matrix size, it defines the trace of the identity element in the Clifford module.
# It also defines the phase transition value as taken from:
def randomSetup(typ):
    if typ == '13':
        M = [5,6,7,8]
        trace = 4
        PT = -3.70
    if typ=='20' or typ=='11':
        M = [5,6,7,8,9,10]
        trace = 2
        if typ == '11':
            PT=-2.40
        if typ=='20':
            PT=-2.80

    return M,PT,trace

# This function imports all of the averaged eigenvalues from
def getRanFuzSpaceEigs(typ,errors=True):
    M,PT,trace = randomSetup(typ)
    avfiles=[glob.glob('./RandomGeometry/eigenvalues/type'+typ+'/AvEv_'+str(i)+'-*.txt') for i in M ]
    # Sorts the files above into the human order of 3.7, 3.75 etc as otherwise the order is messed up.
    for a in avfiles:
        a.sort(key=natural_keys)
    # Initialising the arrays for the data for the different types
    avdata=[0]*len(M)
    uavdata=[0]*len(M)
    # Initialising arrays for the g2 values
    g2 = [0]*len(M)
    # Code get getting the eigenvalues and their errors from the files above
    for j in range(len(M)):
        g2[j] = [f.split('_')[3] for f in avfiles[j]]
        for i in range(len(g2[j])):
            g2[j][i] = float(g2[j][i])
        avdata[j] = [np.loadtxt(f) for f in avfiles[j]]
        avdata[j] = np.array(avdata[j])
        uavdata[j] = [unp.uarray(avdata[j][i][0],avdata[j][i][1]) for i in range(len(g2[j]))]
    np.dstack((g2,uavdata))
        #Line above uses the 'errors' in the file as the standard devs.
    # return data
    return uavdata, g2
