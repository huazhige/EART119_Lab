# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:28:21 2019

@author: Bruno Lopez
"""
'''
This program uses the central difference theorem so that
the 1st order derivative and second order derivative are found
'''


import numpy as np
import matplotlib.pyplot as plt

#Loads the text and transposes it
time, position= np.loadtxt('HW4_vertTraj.txt').T

#MArrays filled with 500 zeros made to be placeholders
df_dt = np.zeros(len(time))
df2_dt2 = np.zeros(len(time))

#Uses the central difference to find the derivative
for i in range (1, len(time) - 1):
    df_dt[i] = (position[i + 1] - position[i - 1]/ (time[i + 1]) - time[i-1])

#Uses the central difference theoprem on the first derivative
#To find the second derivative    
for j in range (2, len(time) - 2):
    df2_dt2[j] = (df_dt[j + 1] - df_dt[j - 1]/ (time[j + 1]) - time[j-1])
    

    

#makes the subplot of three figures
plt.subplot(311)
plot1 = plt.subplot(311)
plot2 = plt.subplot(312)
plot3 = plt.subplot(313)

#Plots the points
plot1.plot(time, position)
plot2.plot(time, df_dt, 'r--')
plot3.plot(time, df2_dt2, 'k--')

#Title on the x axis
plot1.set_xlabel("time (s)")
plot2.set_xlabel("time (s)")
plot3.set_xlabel("time (s)")

#Title on the y-axis
plot1.set_ylabel("Position (m)")
plot2.set_ylabel("Position (m)")
plot3.set_ylabel("Position (m)")

plt.show()

plt.savefig("Hw4 Problem 5 graph")
