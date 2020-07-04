# @Author: Paul Druce <pauldruce>
# @Date:   2020-06-21T16:40:08+01:00
# @Email:  pjdruce@gmail.com
# @Last modified by:   pauldruce
# @Last modified time: 2020-06-21T17:33:44+01:00



# This file generates the eigenvalues of the Dirac operator for the type (0,3)-Fuzzy sphere as outlined by
# Grosse and Presenadjer and also the type (1,3)-Fuzzy sphere defined by Barrett.

import os
import numpy as np
import sys

flatten = lambda l: [item for sublist in l for item in sublist]

def eigs(typ,Nt):
    if typ == '13':  # Barrett Fuzzy Sphere
        liste=[[i]*8*i for i in np.arange(1,Nt)]
        liste.append([Nt]*4*Nt)
        liste=flatten(liste)
        liste=np.array(liste)
        liste.sort()
        return liste

    if typ == '03':  # Grosse-Presenadjer fuzzy sphere
        liste=[[i]*4*i for i in np.arange(1,Nt)]
        liste.append([Nt]*2*Nt)
        liste=flatten(liste)
        liste=np.array(liste)
        liste.sort()
        return liste
    else:
        return sys.exit()

# Testing Area
# eigs('13',10)
