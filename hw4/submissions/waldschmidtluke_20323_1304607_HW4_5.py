#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:54:10 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt


file_in = 'data/HW4_vertTraj.txt'
mData = np.genfromtxt(file_in, skip_header = 1).T


t = mData[0]
z = mData[1]

dz_dt = (z[2::] - z[0:-2]) / (t[2::] - t[0:-2])
d2z_dt2 = (z[2::] + z[0:-2] - 2*z[1:-1]) / ((t[2::] - t[0:-2])/2)**2

ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot(t,z, 'k')
ax2.plot(t[0:-2],dz_dt, 'r')
ax3.plot(t[0:-2],d2z_dt2, 'b' )
plt.xlabel('time')
plt.show()
plt.savefig('HW4_5_plot.png')

