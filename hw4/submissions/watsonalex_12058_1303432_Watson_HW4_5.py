# -*- coding: utf-8 -*-
"""
Homework 4 Part 5 - Alex Watson
    - Use Central Difference Approximation to determine dz/dt and dz2/d2t
    - create 3 subplots of position, velocity, and acceleration
"""
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                               Parameters/Data
#==============================================================================
file_in = 'Data/HW4_vertTraj.txt'
pData   = np.loadtxt( file_in).T
t, z_t  = pData[0], pData[1]
delta_t = t[1]-t[0]
#==============================================================================
#                                   Derivatives                             
#==============================================================================
dzdt   = (z_t[2::] - z_t[0:-2])/(2*delta_t)
dz2d2t = (dzdt[2::] - dzdt[0:-2])/(2*delta_t)    

#==============================================================================
#                                   Plot
#==============================================================================

plt.figure()
ax1 = plt.subplot( 311)
ax1.plot(t, z_t, 'k-')
plt.ylabel( 'Position')
ax2 = plt.subplot(312)
ax2.plot(t[0:498], dzdt, 'b-')
plt.ylabel( 'Velocity')
ax3 = plt.subplot( 313)
ax3.plot(t[0:496], dz2d2t, 'g-')
plt.ylabel( 'Acceleration')
plt.xlabel( 'Time')
file_out = 'Data/Watson_HW4_5.png'
plt.savefig(file_out, dpi = 150)
plt.show()





