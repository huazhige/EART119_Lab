# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:15:05 2019

@author: emlowhit
"""


#=============================================================================
#                       IMPORTS
#=============================================================================
import numpy as np
import matplotlib.pyplot as plt


#=============================================================================
#                       PARAMS
#=============================================================================
ForLoop = True

v0 = 10 #m/s
g = 9.81 #m/s^2
n = 200
t = np.linspace(0 ,1, n)

z = v0*t - (1/2)*g*t**2

file_out = 'midterm_dydx.txt'
#=============================================================================
#                       DATA
#=============================================================================

np.savetxt(file_out, np.array([t, z]).T, fmt = '%10.6f%10.6f', header = 't[s]        z[m]')
mData = np.loadtxt(file_out).T
a_t, a_z = mData[0], mData[1] 


#=============================================================================
#                       DERIVATIVES
#=============================================================================
N = len(a_t)
dt = a_t[1]-a_t[0]
if ForLoop == True:
    a_v = np.zeros(N)
    a_a = np.zeros(N)
    
    for i in range(1, N-1):
        a_v[i] = ( a_z[i+1] - a_z[i-1])/(2*dt)
        a_a[i] = ( a_z[i+1] - 2*a_z[i] + a_z[i-1])/(dt**2)
        a_v = np.hstack( (0,a_v, 0))
        a_a = np.hstack( (0,a_a, 0))

#=============================================================================
#                      PLOTS
#=============================================================================



plt.figure(3)
plt.subplot( 311)
plt.plot( a_t, a_z)

plt.ylabel('Distance [m]')
plt.grid(True)

plt.subplot(312)
plt.plot(a_t[1:-1], a_v[1:-1])

plt.ylabel('Velocity (m/s)')
plt.grid( True)

plt.subplot( 313)
plt.plot( a_t[1:-1], a_a[1:-1])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s2)')
plt.ylim( -g - 5, -g+5)
plt.grid( True)
plt.show()


