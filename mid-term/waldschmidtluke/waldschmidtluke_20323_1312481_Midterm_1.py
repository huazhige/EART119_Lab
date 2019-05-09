#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:22:57 2019

@author: lukewaldschmidt
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

#import data
file_in = 'data/star_luminos.txt'
mData = np.genfromtxt(file_in).T

T = mData[0]
L = mData[1]



#use opt_utils to find power law fit
dLS = opt_utils.lin_LS(T,np.log(L))
L_yhat = np.exp( dLS['a']) * (np.exp( dLS['b']*T))



#plot everything
plt.figure()
plt.title('Power law exponent:' + str(dLS['R2']))
ax1 = plt.subplot(111)
ax1.plot(T,L,'ko',ms=5,mew=1.5,mfc='none',label='Observed data')
ax1.plot(T,L_yhat, 'r-', label = 'Model fit')
ax1.legend(loc=1)
plt.xlabel('Temperature')
plt.ylabel('Luminosity') 
plt.show()
plt.savefig('Midterm_1_plot.png')