# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#=============== Data/ Data Import ===============#
file_eq = 'midterm_dydx.txt'
mData = np.loadtxt(file_eq).T
#mData[0] is the time and mData[1] is the distance
at, ax = mData[0], mData[1]

#=============== Derivatives ===============#
N        = len( at)
dt    = at[1]-at[0]

# vectorize
a_vel = (ax[2::] - ax[0:-2])/(2*dt)
a_acc = (ax[2::] - 2*ax[1:-1] + ax[0:-2])/(dt**2)

a_vel = np.hstack( (0,a_vel, 0))
a_acc = np.hstack( (0,a_acc, 0))

#=============== plots ===============#
plt.figure()
plt.subplot(311)
plt.plot( at, ax)
plt.ylabel('Height [m]')
plt.grid(True)
plt.subplot(312)
plt.plot( at[1:-1], a_vel[1:-1])
plt.ylabel('Velocity [m/s]')
plt.grid(True)
plt.subplot(313)
plt.plot( at[1:-1], a_acc[1:-1])
plt.ylabel('Acceleration [m/s^2]')
plt.grid(True)
plt.savefig( 'Plot_#3')
plt.show()
