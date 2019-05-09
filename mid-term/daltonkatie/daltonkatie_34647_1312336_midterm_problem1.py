# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:23:48 2019

@author: kardalto
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

data_star_lum = np.genfromtxt('star_luminos.txt').T

afterFitting = opt_utils.lin_LS(data_star_lum[0],data_star_lum[1]) 


a = 515.9896349043293
b = -0.24207087442733877
fitLum = []
for i in range(10,1001):
    lumosity = a*(data_star_lum[0][i]**b)
    fitLum.append(lumosity)


plt.figure(1)
plt.subplot(211)
plt.plot(data_star_lum[0],data_star_lum[1], 'ko', ms = 2)
plt.title('Star Lumosity Data')
plt.xlabel('Temperature(degree C)')
plt.ylabel('Lumosity (solar units)')
plt.subplot(212)
plt.plot(data_star_lum[0][10:1001], fitLum, 'bo', ms = 2)
plt.xlabel('Temperature(degree C)')
plt.ylabel('Fitted Lumosity (solar units)')
plt.show()
