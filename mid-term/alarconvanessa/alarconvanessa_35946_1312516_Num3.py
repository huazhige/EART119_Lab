# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:14:03 2019

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt


inFile = 'midterm_dydx.txt'

Data = np.genfromtxt(inFile).T

t = Data[0]
z = Data[1]

"""
central difference formula is 

f'(z)  =  f(x + h) - f(x - h)/2h

I don't have enough time!

"""
dzdt = np.diff(z, n = 1)
dz2dt2 = np.diff(z, n = 2)

print(np.size(t[0:4498]))#==================== plots ===================================================
plt.figure(1)

plt.subplot(311)
plt.plot(t, z, label = 'Data')
plt.ylabel('z(t) [m]')
plt.xlabel('t [s]')

plt.subplot(312)
plt.plot(t[0:np.size(dzdt)], dzdt, label = "z'")
plt.ylabel('[m/s]')

plt.subplot(313)
plt.plot(t[0:np.size(dz2dt2)], dz2dt2, label = "z''")

plt.legend(loc= 'best')

plt.savefig('number3midterm')


