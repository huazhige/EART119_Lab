# -*- coding: utf-8 -*-
"""
HW4 #5:
Download the following data file from canvas: HW4_vertTraj.txt. 
This file represents the position, z, of an object on a vertical 
trajectory as a function of time. Compute the velocity (dz/dt) and 
acceleration (dz2/d2t) at every point in time using a central difference 
approach. Create three different subplots of position, velocity and 
acceleration as a fct of t and save the figure as .png.

"""
import numpy as np
import matplotlib.pyplot as plt

#=========================================================================
                    #Variables, Functions
#=========================================================================
file_in = 'HW4_vertTraj.txt'
dir_out_Traj = 'C:\Users\Connor\OneDrive\ASTR 119\Homework\HW4'

t, z = np.genfromtxt( file_in).T        

dz_dt = np.zeros(len(t))
dz2_dt2 = np.zeros(len(t))

for i in range(1, len(t)-1):
   dz_dt[i] = (z[i + 1] - z[i - 1])/ (t[i + 1] - t[i - 1])

for i in range(2, len(t)-2):
   dz2_dt2[i] = (dz_dt[i + 1] - dz_dt[i - 1])/ (t[i + 1] - t[i - 1])


plt.subplot(311)

ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot( t, z, label = 'Pos. v Time')
ax2.plot( t, dz_dt)
ax3.plot( t, dz2_dt2)



plt.savefig('dir_out_Traj')
plt.show() 