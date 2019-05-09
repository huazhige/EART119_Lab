# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:02:36 2019
Problem 3
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt

file_in = 'midterm_dydx.txt'
time = np.genfromtxt(file_in, skip_header = 1, usecols = 0).T #seconds
z_t = np.genfromtxt(file_in, skip_header = 1, usecols = 1).T #meters


plt.figure(1)
ax = plt.subplot(311)
ax = plt.plot(time, z_t, label = 'original data')



#central difference with respect to z
dt = 1/len(time)
derivative = (time[2::] - time[0:-2])/(2*dt)
ax2 = plt.subplot(312)
ax2.set_xlim([-4, 4])
ax2.set_ylim([-10, 10])
ax2 = plt.plot(derivative, z_t[0:-2], label = 'first derivative')

#second derivative
second_derivative = (time[2::] - 2*time[1:-1] + time[0:-2])/(dt**2)
ax3 = plt.subplot(313)
ax3.set_xlim([-4, 4])
ax3.set_ylim([-10, 10])
ax3 = plt.plot(second_derivative, z_t[0:-2], label = 'second derivative')


plt.show()

