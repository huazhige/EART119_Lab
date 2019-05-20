# -*- coding: utf-8 -*-
#python 2.7
"""
Given the trajectory data of an object, plots the position, velocity, and acceleration as a 
function of time
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#load data
#==============================================================================
data = np.loadtxt('HW4_vertTraj.txt').T

#==============================================================================
#function definitions
#==============================================================================
#central limit derivative
def cld(x, y):
    """
    Input: x - array of x-values
           y - array of y-values
    Output: deriv - array of derivatives by find slope between subsequent points
            derivtime - array of times corresponding to derivatives by averaging subsequent times
    """
    deriv = [] 
    derivtime = [] 
    for i in range(1, len(x)):
        deriv.append((y[i] - y[i - 1]) / (x[i] - x[i - 1]))
        derivtime.append((x[i] + x[i - 1]) / 2)
    return deriv, derivtime

#==============================================================================
#computations
#==============================================================================
#velocity
vel, veltime = cld(data[0], data[1])

#acceleration
accel, acceltime = cld(veltime, vel)

#==============================================================================
#plotting
#==============================================================================
plt.figure(1, figsize = (12, 10))

#position vs time
plt.subplot(311)
plt.plot(data[0], data[1])
plt.xlabel('Time [s]')
plt.ylabel('z(t) [m]')

#velocity vs time
plt.subplot(312)
plt.plot(veltime, vel)
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')

#acceleration vs time
plt.subplot(313)
plt.ylim(-15, -5)
plt.plot(acceltime, accel)
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s^2]')

plt.savefig('kinematicgraphs.png')