# -*- coding: utf-8 -*-
"""

Download the following data file from canvas: HW4_vertTraj.txt. This file
represents the position, z, of an object on a vertical trajectory as a function of time.
Compute the velocity (dz/dt) and acceleration (dz2/d2t) at every point in time using a
central difference approach. Create three different subplots of position, velocity and
acceleration as a fct of t and save the figure as .png.

"""

import numpy as np
import matplotlib.pyplot as plt

mData = np.loadtxt('HW4_vertTraj.txt').T

z = mData[0]
f_z = mData[1]
delta_z = z[1::] - z[0:-1]

dfdz = (f_z[2::] - f_z[0:-2])/(2*delta_z[1::])

df2d2z = (f_z[2::] - 2*f_z[1:-1] + f_z[0:-2])/(delta_z[1::])**2

fig, (ax1, ax2, ax3) = plt.subplots( 3, 1, sharex = True, figsize = (10,12))
fig.subplots_adjust(hspace = 0.2)
plt.rcParams.update({'font.size': 22})

ax1.plot( z[0::], f_z, 'b-')
ax1.set(ylabel = 'Position')

ax2.plot(z[1:-1], dfdz, 'r-')
ax2.set(ylabel = 'Velocity')

ax3.plot(z[1:-1], df2d2z, 'g-')
ax3.set(ylabel = 'Acceleration')
ax3.set(ylim =[-12.5, -7.5])

plt.savefig('Problem 5 subplots.png')