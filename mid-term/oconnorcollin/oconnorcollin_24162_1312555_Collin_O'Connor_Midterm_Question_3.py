# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:26:54 2019

@author: colli
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#Question 3
#==============================================================================
#load file
data_file='midterm_dydx.txt'
mData=np.loadtxt(data_file).T
a_t, a_y = mData[0], mData[1]

N        = len( a_t)
dt    = a_t[1]-a_t[0]
useForLoop = False # switch between vectorized and for loop solutio

file_out = 'HW4_vertTraj.txt'
if useForLoop == True:# solve within for loop
    a_vel = np.zeros( N) # first and last elements cannot be compute with CD
    a_acc = np.zeros( N)

    for i in range( 1, N-1):
        a_vel[i] = ( a_y[i+1] - a_y[i-1])/(2*dt)
        a_acc[i] = ( a_y[i+1] - 2*a_y[i] + a_y[i-1])/(dt**2)
else: # vectorized solution
    a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
    a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)
    # add zeros at beginning and end for plotting purposes
    a_vel = np.hstack( (0,a_vel, 0))
    a_acc = np.hstack( (0,a_acc, 0))



#===================================================================================
#                                plots
#===================================================================================

plt.figure()
plt.subplot( 311)
plt.plot( a_t, a_y)
plt.ylabel('iniial z(t) [m]')
plt.xlabel('t [s]')
plt.grid( True)

plt.subplot( 312)
# skip zeros and beginning and end
plt.plot( a_t[1:-1], a_vel[1:-1])
# peak height at v = 0
plt.ylabel('Velocity (m/s)')
plt.grid( True)

plt.subplot( 313)
# skip zeros and beginning and end
plt.plot( a_t[1:-1], a_acc[1:-1])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s2)')
plt.grid( True)
plt.show()

plt.savefig('Question_3')
