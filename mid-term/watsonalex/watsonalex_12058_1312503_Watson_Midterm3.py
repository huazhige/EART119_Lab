# -*- coding: utf-8 -*-
"""
Midterm question 3

    - find the first and second derivatives from some data, plot all
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                               Parameters/Data
#==============================================================================
file_in = 'Data/midterm_dydx.txt'
mData   = np.loadtxt( file_in).T
x, y  = mData[0], mData[1]
delta_t = x[1]-x[0]
#==============================================================================
#                                   Derivatives                             
#==============================================================================
dydx   = (y[2::] - y[0:-2])/(2*delta_t)
dy2d2x = (dydx[2::] - dydx[0:-2])/(2*delta_t)    

#==============================================================================
#                                   Plot
#==============================================================================

plt.figure()
plt.title( 'Derivatives of points from text file')
ax1 = plt.subplot( 311)
ax1.plot(x, y, 'k-', label = 'Initial Points')
plt.legend( loc = 'upper right')
ax2 = plt.subplot(312)
ax2.plot(x[0:4998], dydx, 'b-', label = 'First Derivative')
plt.ylabel( 'y')
plt.legend( loc = 'upper right')
ax3 = plt.subplot( 313)
ax3.plot(x[0:4996], dy2d2x, 'g-', label = 'Second Derivative')
plt.xlabel( 'X')
plt.legend( loc = 'upper right')
file_out = 'Data/Watson_Midterm3.png'
plt.savefig(file_out, dpi = 150)
plt.show()