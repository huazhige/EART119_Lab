# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:05:22 2019

Taking First and Second Derivatives
"""
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                                params
#===================================================================================

file_out = 'Midterm_dydx.txt'
#===================================================================================
#                                data I/O
#===================================================================================
# save synthetic data
np.savetxt(file_out, np.array([ t, y]).T, fmt = '%10.6f%10.6f', header = 't[s]      z(t) [m]')
# re-load synthetic data for demonstration purposes
mData = np.loadtxt( file_out).T
a_t, a_y = mData[0], mData[1]

#===================================================================================
#                                derivatives etc.
#===================================================================================
N        = len( a_t) #number of data points
dt    = a_t[1]-a_t[0]  

if useForLoop == True:# solve within for loop
    a_vel = np.zeros( N) # first and last elements cannot be compute with CD
    a_acc = np.zeros( N)

    for i in range( 1, N-1):
        a_vel[i] = ( a_y[i+1] - a_y[i-1])/(2*dt) #first derivative by central difference method
        a_acc[i] = ( a_y[i+1] - 2*a_y[i] + a_y[i-1])/(dt**2) #second derivative 
"""
else: # vectorized solution
    a_vel = (a_y[2::] - a_y[0:-2])/(2*dt)
    a_acc = (a_y[2::] - 2*a_y[1:-1] + a_y[0:-2])/(dt**2)
    # add zeros at beginning and end for plotting purposes
    a_vel = np.hstack( (0,a_vel, 0))
    a_acc = np.hstack( (0,a_acc, 0))
    """

# From Week 2: fidn largest height
i = 1
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1

#===================================================================================
#                                plots
#===================================================================================
t_maxHeight = a_t[i] #define largest height
print "The largest height achieved was %f m" % (largest_height), ' at t =', t_maxHeight

#make 3 subplots and label highest y value
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

