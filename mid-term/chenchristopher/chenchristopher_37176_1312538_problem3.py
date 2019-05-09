# -*- coding: utf-8 -*-
#python 2.7
"""
Midterm problem 3
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#load data
#==============================================================================
data = np.loadtxt('midterm_dydx.txt').T

#==============================================================================
#computations
#==============================================================================
#take derivative (central difference)
def deriv(x, y):
    deriv = [] #array of derivatives
    xderiv = [] #array of corresponding times to go with derivatives
    for i in range(1, len(x) - 1)
        deriv.append((y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1]))
        xderiv.append(x[i])
    return xderiv, deriv

#==============================================================================
#plotting
#==============================================================================
plt.figure(1, figsize = (12, 10))

#raw data
plt.subplot(311)
plt.plot(data[0], data[1])

plt.subplot(312)
plt.subplot(313)

#run the deriv and secderiv function to calculate the values and then plot them