#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:48:25 2019

@author: andreaskooi
"""

#imports 


import numpy as np
import matplotlib.pyplot as plt




#computations

file_in = 'midterm_dydx.txt'

t, z = np.genfromtxt(file_in).T


df_dt = np.zeros(len(t))
df2_dt2 = np.zeros(len(t))


#first and second derivatives using C.D. method

for i in range(1, len(t)-1):
    df_dt[i] = (z[i + 1] - z[i - 1])/ (t[i + 1] - t[i - 1])
    
for i in range(2, len(t)-2):
    df2_dt2[i] = (df_dt[i + 1] - df_dt[i - 1])/ (t[i + 1] - t[i - 1])


#plotting

plt.subplot(321)
ax1 = plt.subplot(321)
ax2 = plt.subplot(322)
ax3 = plt.subplot(325)

ax1.plot(t,z, 'r')
ax2.plot(t[1:len(t)-1],df_dt[1:len(t)-1], 'g')
ax3.plot(t[2:len(t)-2],df2_dt2[2:len(t)-2], 'b')

ax1.set_title('z versus t')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Position [m]')
ax2.set_title("first derivative versus t")
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Velocity [m/s]')
ax3.set_title('second derviative versus t')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Acceleration [m/s^2]')


plt.show()

