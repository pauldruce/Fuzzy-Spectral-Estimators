# @Author: Paul Druce <pauldruce>
# @Date:   2020-06-21T17:57:40+01:00
# @Email:  pjdruce@gmail.com
# @Last modified by:   pauldruce
# @Last modified time: 2020-06-28T05:42:36+01:00


# Implenting this calculation in python is slow.

import numpy as np
import uncertainties as unc
from uncertainties import unumpy as unp
from uncertainties.umath import *

# This function takes in eigenvalues and spits out the spectral dimension and the spectral variance for that set of eigenvalues.
# xmax is the maximum x-axis value can take (often the variable t).
# l is the discretisation of the axis that is taken.
#RETURNS: 2 arrays
 # 1. specDim = array of pairs (x,d_s(x))
 # 2. specVar = array of pairs (x,v_s(x))
def specDimAndVar(eigs,xmax,l):
    # This is just splitting the x axis,
    xfit=np.linspace(0., xmax, num=l)

    # da = square of eigenvalues
    da=eigs*eigs
    # ds3 and dv3 are empty arrays to contain the spectral dimension (ds) and spectral variance (dv)
    specDim=[0]*l
    specVar=[0]*l
    for t in np.arange(l):
        x = xfit[t]
        sx=slx=slx2=sxs=sd=sx2=None
        # sx= a heat kernel expansion for different matrix sizes [0] = 5x5, [1] = 6x6
        # (Paul) removed the absolute as its not needed mathemacally.
        sx=unp.exp(-x*da)
        # sx = np.exp(-x*da) # Use this one if you don't need the uncertainties package.
        # slx= top of spectral dimensions t * \lambda^2 e^{-t*\lambda^2}
        slx=da*sx*x
        # slx2 = top of firt term in spectral variances
        slx2=da*da*sx*x*x
        #summing the top of spectral dimensions
        sxs=sx.sum()
        # sxs = spectral dimenions?
        # (Paul) changes the redefining of sx to just a new variable sd
        sd=slx.sum()/sxs
        # sx2 = first term in spectral variance?
        sx2=slx2.sum()/sxs
        #dv3 = spectral variance
        specVar[t]= 2*sx2-2*sd*sd
        # ds3 = spectral dimension
        specDim[t] = (2*sxs)

    # Convert the spectral dimension/variance lists into numpy arrays so we can work on them.
    specDim = np.dstack((xfit,np.array(specDim)))
    specVar = np.dstack((xfit,np.array(specVar)))
    return specDim, specVar
