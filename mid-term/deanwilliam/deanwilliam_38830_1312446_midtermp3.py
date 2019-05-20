#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:59:55 2019

@author: williamdean
MIdterm problem 3 using central differences to take 1st and 2nd derivative
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt( 'midterm_dydx.txt')

times, positions = data.T[0], data.T[1]


def central_differences(data, h=1):
    derivative = np.zeros(len(data))
    data = ([0] * h + data + [0] * h)
    for i in range(h, len(data) - h):
        derivative[i - h] = (data[i + h] - data[i - h]) / (2 * h)
        
    return derivative

time_step = times[1] - times[0]
h = 1
d_positions = central_differences(positions, h) / time_step
d2_positions = central_differences(d_positions[:-h], h) / time_step

plt.plot(times, positions, 'b')
plt.plot(times[:-h], d_positions[:-h], 'g')
plt.plot(times[:-4 * h], d2_positions[: -3 * h], 'orange')
plt.xlabel( 'Time(s)')
plt.ylabel( 'Position(m)')
plt.title( 'Objects motion, velocity, and acceleration over time')
plt.show()
