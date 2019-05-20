#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:31:44 2019

@author: taylorduncan
"""

import numpy as np
import matplotlib.pyplot as plt

file_in = 'HW4_vertTraj.txt'

t,z = np.genfromtxt(file_in).T


df_dt = np.zeros(len(t))
df2_dt2 = np.zeros(len(t))

for i in range(1, len(t)-1):
   df_dt[i] = (z[i + 1] - z[i - 1])/ (t[i + 1] - t[i - 1])

for i in range(2, len(t)-2):
   df2_dt2[i] = (df_dt[i + 1] - df_dt[i - 1])/ (t[i + 1] - t[i - 1])


plt.subplot(311)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot(t,z)
ax2.plot(t,df_dt)
ax3.plot(t,df2_dt2)


plt.title("Position v. Time")
#ax2.title("Velocity v. Time")
#ax3.title("Acceleration v. Time")
plt.savefig('data')
plt.show() 