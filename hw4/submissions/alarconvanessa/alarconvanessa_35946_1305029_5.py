# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:42:44 2019

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt
import os

fileName = 'HW4_vertTraj.txt'
mData = np.genfromtxt(fileName, skip_header = 0).T
#print (mData)

t = mData[0]
z = mData[1]

#first derivative
h = t[1] - t[0]

"""
dz = np.array([1])
for i in range (1, np.size(t)):
    der_z = (z[i] + z[i-1])/(2*h)
    dz = np.append(dz, der_z)
    i += 1
  
print (dz)
"""

dz = np.diff(z, n = 1)
d2z = np.diff(z, n = 2)
plt.figure(1)

plt.subplots_adjust(hspace = 0.2)

plt.subplot(311)
plt.title('position')
plt.plot(mData[0], mData[1], 'r-', label = 'Path')

plt.subplot(312)
plt.title('velocity')
plt.plot(mData[0, 1::], dz, label = 'dz/dt')

plt.subplot(313)
plt.title('acceleration')
plt.ylim(-10, 10)
plt.plot(t[0:-2], d2z, 'k-', label = 'd2/dt2')
plt.legend(loc = 'best')
plt.show()


