#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:16:18 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt

file_in = 'data/midterm_dydx.txt'
mData = np.genfromtxt(file_in).T

t = mData[0]
z = mData[1]


#use central difference method to find 1st and 2nd derivative
dz_dt = (z[2::] - z[0:-2]) / (t[2::] - t[0:-2])
d2z_dt2 = (z[2::] + z[0:-2] - 2*z[1:-1]) / ((t[2::] - t[0:-2])/2)**2


#plot everything

ax2 = plt.subplot(211)
ax3 = plt.subplot(313)

#finding T0
T0 = 10 #made up value for T0
ax2.plot(t[0:-2],dz_dt, 'r')
ax2.plot(t,T0*-2*t*np.exp(-t**2),'k')
ax3.plot(t[0:-2],d2z_dt2, 'b' )
ax3.plot(t,T0*4*t**2*np.exp(-t**2),'k')
plt.xlabel('black = exact solutions, red/blue = 1st/2nd deriv numerical')
plt.show()
plt.savefig('Midterm_bonus_plot.png')