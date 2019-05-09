# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:24:49 2019

@author: Jason Minera

I took the template from the test LS code we did in class.
I chose my random seed my min and max time and i chose random values for alpha and beta.
Im not quite sure if those have to be random or if we let the program choose values for those..
I did a linspace for my t and i put the function for my y.
I called out to the text file and transposed it. (skipped the first line because of the strings)
called out to that file to get the information.
then used the Opt_utils lin_LS module to calculate the at, and ay.
In line under F_mdata it says slope,, intercept, r_p, prob etc... i dont need that information but i thought it would look
nice.
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as ou
import scipy.stats

np.random.seed( 123456)
tmin,tmax = 10, 1000

N = 1000
alpha = 0.5 # i dont know what alpha or whats beta are so im picking random numbers
beta = 2
sigma = 2.1

at = np.linspace(tmin, tmax, N)
ay = alpha*at**beta + np.random.randn( N)*sigma


file_in = 'star_luminos.txt'

mData   = np.genfromtxt( file_in, usecols=(0,1), skip_header = 1).T

F_mdata = ou.lin_LS(at, ay)
slope, intercept, r_p, prob, stderr = scipy.stats.linregress( at, ay)
print('scipy', slope, intercept, r_p)

#print(mData)

plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot( at, ay, 'ko', ms = 1, mew = 1, mfc = 'none')
plt.xlabel('Temperature')
plt.ylabel('Luminosity')

ax1.legend( loc = 'upper right')
plt.show()
