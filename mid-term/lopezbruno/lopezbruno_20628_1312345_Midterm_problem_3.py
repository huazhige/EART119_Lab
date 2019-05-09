# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:30:04 2019

@author: bruno
"""

import numpy as np
import matplotlib.pyplot as plt
#Loads data
time,position = np.loadtxt("midterm_dydx.txt").T

N        = len( time)
dt    = time[1]- time[0] #delta x

a_vel = np.zeros( N) #Empty placeholder arrays
a_acc = np.zeros( N)

for i in range( 1, N-1): #A for loop that gets the first and second derivative
    a_vel[i] = ( position[i+1] - position[i-1])/(2*dt)
    a_acc[i] = ( position[i+1] - 2*position[i] + position[i-1])/(dt**2)

plt.subplot(311)

#Plots the data in three different subplots
ax_1 = plt.subplot(311)
ax_2 = plt.subplot(312)
ax_3 = plt.subplot(313)

ax_1.plot(time, position)
ax_2.plot(time, a_vel, 'r--')
ax_3.plot(time, a_acc, 'k--')

ax_1.set_xlabel("time (s)")
ax_2.set_xlabel("time (s)")
ax_3.set_xlabel("time (s)")

ax_1.set_ylabel("Position (m)")
ax_2.set_ylabel("Velocity (m/s)")
ax_3.set_ylabel("Acceleration (m/s^2)")

plt.show()

plt.savefig("Midterm Problem 3 Graph")

