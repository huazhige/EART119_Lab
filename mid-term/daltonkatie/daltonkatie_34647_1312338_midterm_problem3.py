# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:11:13 2019

@author: kardalto
"""

import numpy as np
import matplotlib.pyplot as plt

data_z = np.genfromtxt('midterm_dydx.txt', dtype = float, skip_header = 1).T

#start by ploting the original data as position over time 
plt.figure(1)
plt.subplot(221)
plt.plot( data_z[0], data_z[1], 'ro', ms = 2)
plt.title('Central Differences')
plt.xlabel( ' Time[s] ' )
plt.ylabel( ' Position[m] ' )

#create an array of zeros for velocity
data_v = np.array([np.zeros(len(data_z[0])-2), np.zeros(len(data_z[0])-2)])
#loop to fill array with time and velocity
for i in range(1, len(data_z[0])-1):
    data_v[0][i-1] = data_z[0][i-1] #fill time
    delta_z = data_z[0][i+1]-data_z[0][i-1]
    data_v[1][i-1] = (data_z[1][i+1]-data_z[1][i-1]) / delta_z #fill velocity using cental difference
    
#create an array of zeros for acceleration
data_a = np.array([np.zeros(len(data_v[0])-2), np.zeros(len(data_v[0])-2)])
#loop to fill array with time and acceleration
for i in range(1, len(data_v[0])-1):
    data_a[0][i-1] = data_v[0][i-1] #fill time
    delta_v = data_v[0][i+1]-data_v[0][i-1]
    data_a[1][i-1] = (data_v[1][i+1]-data_v[1][i-1]) / delta_v #fill accleration using central difference
    
#plot velocity over time
plt.subplot(222)
plt.plot( data_v[0], data_v[1], 'bo', ms = 2)
plt.xlabel( ' Time[s] ' )
plt.ylabel( ' Velocity[m/s] ' )
plt.show()

#plot acceleration over time
plt.subplot(223)
plt.plot( data_a[0], data_a[1], 'go', ms = 2)
plt.xlabel( ' Time[s] ' )
plt.ylabel( ' Acceleration[m/s^2] ' )
plt.show()

