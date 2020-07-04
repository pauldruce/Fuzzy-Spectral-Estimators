# @Author: Paul Druce <pauldruce>
# @Date:   2020-06-21T18:40:41+01:00
# @Email:  pjdruce@gmail.com
# @Last modified by:   pauldruce
# @Last modified time: 2020-06-28T08:44:16+01:00

import numpy as np
# The random spec dim function only takes in the spectra of one geometry. Cannot process arrays of spectra
from spectralDimAndVar import specDimAndVar
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp

# %%
# Random Geometries
typ = '20' # or '13' or '11'
from RandomGeometry.helperFunction import getRanFuzSpaceEigs
randomFSEigs, g2 = getRanFuzSpaceEigs(typ)
randomFSEigs_normalised1 = randomFSEigs[0][0]/abs(randomFSEigs[0][0]).min()
eigs_shape = np.shape(randomFSEigs)
randomFSEigs_normalised=randomFSEigs
randomSpecDim= randomSpecVar=[0]*len(randomFSEigs)
for i in range(len(randomFSEigs)):
    randomSpecDim[i]= randomSpecVar[i]=[0]*len(randomFSEigs[i])
    for j in range(len(randomFSEigs[i])):
        randomFSEigs_normalised[i][j] = randomFSEigs[i][j]/abs(randomFSEigs[i][j]).min()
        randomSpecDim[i][j], randomSpecVar[i][j] = specDimAndVar(randomFSEigs_normalised[i][j],10,500)
# comb = np.dstack((g2,randomFSEigs))

# %%
for i in range(len(randomFSEigs)):
    for j in range(len(randomFSEigs[i])):
        plt.errorbar(randomSpecVar.T[0],unp.nominal_values(randomSpecVar.T[1]),yerr=unp.std_devs(randomSpecVar.T[1]))
    plt.show()



# %%
# Fuzzy Sphere
typ = '13' # or '03'
MatrixSize = 10
from FuzzySphere.fuzzySphereEigenvalues import eigs as getSphereEigs
sphereEigs = getSphereEigs(typ,MatrixSize)
sphereSpecDim, sphereSpecVar = specDimAndVar(sphereEigs,5,1000)
plt.plot(sphereSpecVar.T[0],sphereSpecVar.T[1])


# %%
#Fuzzy Torus
a=d=1
b=c=0
MatrixSize=100
from FuzzyTorus.fuzzytori import getTorusEigs
torusEigs = getTorusEigs(a,b,c,d,MatrixSize)
torusSpecDim, torusSpecVar= specDimAndVar(torusEigs,5,1000)
plt.plot(torusSpecVar.T[0],torusSpecVar.T[1])
