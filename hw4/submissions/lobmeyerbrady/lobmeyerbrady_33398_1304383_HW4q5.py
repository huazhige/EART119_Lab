# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:07:29 2019

@author: Brady
"""

import numpy as np
import matplotlib.pyplot as plt
vT= 'HW4_vertTraj.txt'

vData = np.genfromtxt( vT, skip_header = 1, usecols=(0,1)).T
#print vData

t = vData[0]
z = vData[1]
a_t = (z/t)
dt=.002004
plt.subplot(311)
plt.plot(t, z, 'r-')

a_sin= np.sin
dfdt_CD = (np.sin(a_t +dt)-np.sin(a_t-dt))/dt
print dfdt_CD
plt.subplot(312)
plt.plot (t, dfdt_CD, 'k-')


a_t2 = dfdt_CD
dfdt2_CD = (np.sin(a_t2 +dt)-np.sin(a_t2-dt))/dt
plt.subplot(313)
plt.plot(t, dfdt2_CD, 'b-')