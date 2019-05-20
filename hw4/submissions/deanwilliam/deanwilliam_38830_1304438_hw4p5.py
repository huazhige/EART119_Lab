#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:18:20 2019

@author: williamdean

HW4p5 computing velocity and acceleration of an object in vertical motion
    using central difference approach
"""
import numpy as np
import matplotlib.pyplot as plt

mData = np.loadtxt( 'HW4_vertTraj.txt')
times, positions = mData.T[0], mData.T[1]

def central_differences(data, h=1):
    
    derivative = np.zeros(len(data))
    
    data = [0] * h + data + [0] * h
    
    for i in range(h, len(data) - h):
        derivative[i - h] = (data[i + h] - data[i - h]) / (2 * h)

    return derivative

time_step = times[1] - times[0]
h = 1
d_positions = central_differences(positions, h) / time_step
d2_positions = central_differences(d_positions[:-h], h) / time_step

plt.plot(times, positions)
plt.plot(times[:-h], d_positions[:-h])
plt.plot(times[:-4 * h], d2_positions[: -3 * h])
plt.show()
