# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:02:35 2019

@author: creyesor
"""
import numpy as np
import matplotlib.pyplot as plt

file_in = 'HW4_vertTraj.txt'

t,z = np.genfromtxt(file_in).T #transposes into more clean fashion

df_dt = np.zeros( len(t))
df2_dt2 = np.zeros( len(t))

for i in range(1,len(t)-1):
    df_dt[i] = (z[i+1] - z[i-1])/ (t[i+1] - [i-1])
for i in range(2,len(t)-2):
    df2_dt2[i] = (z[i+1] - df_dt[i-1])/ (t[i+1] - t[i-1])

plt.subplot(311) #3 is the amount of subplots there will be 
ax1 = plt.subplot(311) #1 is assigned to first plot
ax2 = plt.subplot(312) #2 is assigned to second plot
ax3 = plt.subplot(313) #3 is assigned to third plot

ax1.plot(t,z)
ax2.plot(t,df_dt)
ax3.plot(t,df2_dt2)


