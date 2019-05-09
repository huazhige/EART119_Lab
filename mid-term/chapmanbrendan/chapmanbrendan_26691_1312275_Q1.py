# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:24:41 2019

@author: blchapma
"""

#============================================================================
"Packages"
#============================================================================
import numpy as np
import matplotlib.pyplot as plt


#============================================================================
"Variables"
#============================================================================
tmin, tmax = 10,1000
Lum = np.genfromtxt('E:\EAR119\Python Scripts\star_luminos.txt', delimiter=',', dtype=None, names=('Temperature', 'Luminosity'))
def L(A, t, B):
    return A*(t**B)
L = A*(t**B)
#============================================================================
"Plotting"
#============================================================================

plt.plot(Lum)
plt.xlim( tmin, tmax)

    


#============================================================================
"Image"
#============================================================================


plt.savefig("Q1", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format="PNG",
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()


