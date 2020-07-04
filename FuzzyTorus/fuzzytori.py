# @Author: Paul Druce <pauldruce>
# @Date:   2020-06-21T16:45:18+01:00
# @Email:  pjdruce@gmail.com
# @Last modified by:   pauldruce
# @Last modified time: 2020-06-21T21:35:26+01:00

# This file contains the function to generate the fuzzy torus eigenvalues for the lattice parameters (a,b,c,d). The variable Nt denotes the matrix-algebra dimension for the fuzzy torus.

import os
import numpy as np
import sys
import matplotlib.pyplot as plt

flatten = lambda l: [item for sublist in l for item in sublist]

np.seterr(divide='ignore', invalid='ignore')

# This function generates the q-number [q] = sin(pi*q/ Nt)/sin(pi/Nt). This is a specific version of a more general q-num. See any text book on quantum groups for more info.
def qnum(num,Nt):
    temp=np.sin((np.pi*num)/Nt)/np.sin(np.pi/Nt)
    return temp


def torEig(a,b,c,d,k,l,Nt):
    temp = (qnum(a*k - b*l,Nt)**2) + (qnum(d*l - c*k,Nt)**2)
    temp2 = np.sqrt(temp)/qnum(a*d-b*c,Nt)
    return temp2


def getTorusEigs(a,b,c,d,Nt):
    liste=[[torEig(a,b,c,d,n,m,Nt),-1*torEig(a,b,c,d,n,m,Nt)]*2 for n in np.arange((-Nt)//2 + ((a+c)%2)/2,Nt//2 + ((a+c)%2)/2) for m in np.arange((-Nt)//2 + ((b+d)%2)/2,Nt//2 + ((b+d)%2)/2)]
    # for n in np.arange((-Nt)//2 + ((a+c)%2)/2,Nt//2 + ((a+c)%2)/2):
    #    for m in np.arange((-Nt)//2 + ((b+d)%2)/2,Nt//2 + ((b+d)%2)/2):
    #        liste.append(torEig(a,b,c,d,n,m,Nt))
    #        liste.append(torEig(a,b,c,d,n,m,Nt))
    #        liste.append(-1*torEig(a,b,c,d,n,m,Nt))
    #        liste.append(-1*torEig(a,b,c,d,n,m,Nt))
    # to account for the global multiplicity we need to have each eigenvalue twice
    liste = flatten(liste)
    liste = np.array(liste)
    liste.sort()
    return liste


# # Testing functions
# a=d=1
# b=c=0
# torusEigs(a,b,c,d,10)
