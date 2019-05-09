# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:24:52 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#==============================================================================
#                            files, params
#==============================================================================
file_in = 'star_luminos.txt'
mData = np.genfromtxt(file_in).T
Tmin, Tmax = 10, 1000
sel_T = np.logical_and(mData[0] >= Tmin, mData[0] <= Tmax)

dLS = opt_utils.lin_LS(mData[0][sel_T], mData[1][sel_T])
print dLS['b']
#==============================================================================
#                            plots 
#==============================================================================
plt.figure(1)
plt.title('Temperature versus Luminosity Graph')
plt.plot(mData[0], mData[1], 'ko')
plt.xlabel('Temperature (Degree C)')
plt.ylabel('Luminosity (Solar Units)')


plt.figure(2)
plt.title('Logarithmic Temperature versus Luminosity Graph')
plt.loglog(mData[0][sel_T], mData[1][sel_T], 'bo', label = 'exponent, $p$=%.2f'%( dLS['b']))
plt.xlabel('Log Temperature (Degree C)')
plt.ylabel('Log Luminosity (Solar Units)')
plt.legend( loc = 'upper right')

plt.show()