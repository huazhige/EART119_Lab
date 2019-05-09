#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:54:47 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt

#import data
file_in = 'data/midterm_dydx.txt'
mData = np.genfromtxt(file_in).T

t = mData[0]
z = mData[1]


#use central difference method to find 1st and 2nd derivative
dz_dt = (z[2::] - z[0:-2]) / (t[2::] - t[0:-2])
d2z_dt2 = (z[2::] + z[0:-2] - 2*z[1:-1]) / ((t[2::] - t[0:-2])/2)**2


#plot everything
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot(t,z, 'k')
ax2.plot(t[0:-2],dz_dt, 'r')
ax3.plot(t[0:-2],d2z_dt2, 'b' )
plt.xlabel('time')
plt.show()
plt.savefig('Midterm_3_plot.png')