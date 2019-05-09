# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:24:43 2019

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


mData = np.loadtxt('E:\EAR119\Python Scripts\midterm_dydx.txt').T
a_t, a_y = mData[0], mData[1]

#===================================================================================
#                                derivatives
#===================================================================================
N        = len( a_t)
dt    = a_t[1]-a_t[0]

a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)
    # add zeros at beginning and end for plotting purposes
a_vel = np.hstack( (0,a_vel, 0))
a_acc = np.hstack( (0,a_acc, 0))
for i in range( 1, N-1):
        a_vel[i] = ( a_y[i+1] - a_y[i-1])/(2*dt)
        a_acc[i] = ( a_y[i+1] - 2*a_y[i] + a_y[i-1])/(dt**2)
else: # vectorized solution
    
    y = 0
# From Week 2:
    i = 1
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1

#===================================================================================
#                                plots
#===================================================================================
t_maxHeight = a_t[i]
print "The largest height achieved was %f m" % (largest_height), ' at t =', t_maxHeight
# We might also like to plot the path again just to compare
plt.figure()
plt.subplot( 311)
plt.plot( a_t, a_y)
plt.plot( [t_maxHeight], a_y[a_t == t_maxHeight], 'r*')
plt.ylabel('Height (m)')
plt.grid( True)

plt.subplot( 312)
# skip zeros and beginning and end
plt.plot( a_t[1:-1], a_vel[1:-1])
# peak height at v = 0
plt.plot( [t_maxHeight], a_vel[a_t == t_maxHeight], 'r*')
plt.ylabel('Velocity (m/s)')
plt.grid( True)

plt.subplot( 313)
# skip zeros and beginning and end
plt.plot( a_t[1:-1], a_acc[1:-1])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s2)')
plt.ylim( -g - 5, -g+5)
plt.grid( True)
plt.show()



#============================================================================
"Image"
#============================================================================


plt.savefig("Q1", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format="PNG",
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()



#============================================================================