#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:41:05 2019

@author: jtbabbe
"""

import numpy as np
import matplotlib.pyplot as plt

#===================================================================
#           read data
#===================================================================

file_out = 'HW4_vertTraj.txt'
mData = np.loadtxt( file_out).T
t = mData[0]
z = mData[1]

dt = (t[1::] - t[0:-1])
#===================================================================
#           find values using CD
#===================================================================

dzdt_CD = (z[2::] - z[0:-2])/(2*dt[1::]) 
d2zdt2_CD = (dzdt_CD[2::] - dzdt_CD[0:-2])/(2*dt[3::]) 
#===================================================================
#           plot
#===================================================================

plt.figure()
ax1 = plt.subplot(311)
ax1.plot(t, z)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('f(t)')

ax2 = plt.subplot(312)
ax2.plot( t[:-2], dzdt_CD)
plt.grid(True)
plt.xlabel('t')
plt.ylabel("f'(t)")

ax3 = plt.subplot(313)
ax3.plot(t[:-4], d2zdt2_CD)
plt.grid(True)
plt.xlabel('t')
plt.ylabel("f''(t)")

plt.savefig( 'Eart_119_hw4.5_plot.png')





























