# -*- coding: utf-8 -*-
"""
Midterm
Anaconda 2, Python 2.7
@author: jnguy126
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
import opt_utils as utils
#=============================
# Variables
#=============================
"""
T = Temperature
L = Luminosity 
"""
a = 10 #alpha random number
b = 15 #beta random number
#=============================
# Data files
#=============================
file_in = 'star_luminos.txt'
T,L = np.genfromtxt(file_in).T
#=============================
a_x = np.linspace( 10, 1000, 9981)
a_y = a*T**b
#===================================================================================
#                           data fits
#===================================================================================
dLS = utils.lin_LS( a_x, a_y)
for tag, item in dLS.items():
    if isinstance( item, (int, float)):
        print( tag, item)
print( dLS['R2'], dLS['r_p']**2)
## same result with scipy
slope, intercept, r_p, prob, stderr = scipy.stats.linregress( a_x, a_y)
print('scipy', slope, intercept, r_p)

#===================================================================================
#                              plots
#===================================================================================
plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot( a_x, a_y, 'ko', ms = 5, mew = 1, mfc = 'none')
ax1.plot( a_x, dLS['Y_hat'], 'r--', label = 'y = %.1f x + %.1f, R2=%.2f'%( dLS['b'], dLS['a'], dLS['R2']))
# ax1.hexbin( a_x, a_y, cmap = plt.cm.Blues)
plt.xlabel( 'Temperature' )
plt.ylabel( 'Luminosity' )
ax1.legend( loc = 'upper left')
os.chdir( 'X:\Earth119\Midterm') #changed path to my folder
plt.savefig( 'Midterm prob 1')
plt.show()