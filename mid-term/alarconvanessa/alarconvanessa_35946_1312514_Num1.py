# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:28:44 2019

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

# Name file
inFile = 'star_luminos.txt'


#================== Data ======================================================
#import data
mData = np.genfromtxt(inFile, skip_header = 1).T


Temp = mData[0]
luminosity = mData [1]

# Change data so it only includes temperatures between 10K and 1000K
sel = np.logical_and(Temp > 10, Temp < 1000)
T = Temp[sel]
L = luminosity[sel]

#============= best fit =======================================================
#Find the line of best fit
dLS = opt.lin_LS(T, L)
print(dLS)


#============================ plot ============================================
plt.figure(1)

plt.subplot(211)
plt.loglog(T, L, 'ro', markersize = 0.5, label = 'Data')

plt.ylabel('Luminosity (Solar Units)')
plt.legend(loc = 'lower left')

plt.subplot(212)
plt.plot(T, dLS['Y_hat'], 'k-', label = 'Best fit line')
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (Solar Units)')

plt.legend(loc = 'lower left')

plt.grid(True)

plt.show()
plt.savefig('Plot1Midterm')