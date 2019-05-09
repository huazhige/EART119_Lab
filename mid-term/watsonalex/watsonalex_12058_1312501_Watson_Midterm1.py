# -*- coding: utf-8 -*-
"""
Midterm question 1
    - use linLS to find the best-fitting model for star luminosity
"""

import numpy as np
import matplotlib.pyplot as plt

import src.opt_utils as opt_utils


#==============================================================================
#                               load data, params
#==============================================================================
file_in = 'Data/star_luminos.txt'
mData   = np.genfromtxt(file_in).T

Tmin, Tmax = 10, 1000

T = mData[0]
L = mData[1]


#==============================================================================
#                                   run LS
#==============================================================================
sel_T   = np.logical_and( T >= Tmin, T <= Tmax)

star_LS = opt_utils.lin_LS( np.log10(T[sel_T]), np.log10(L[sel_T]))
model_L = (star_LS['a']*(T[sel_T])**star_LS['b'])
#==============================================================================
#                               plot
#==============================================================================

plt.figure()
plt.loglog( T[sel_T], L[sel_T], 'k', mfc = 'none', label = 'Observed Luminosity, L=aT^b')
plt.loglog( T[sel_T], model_L, 'r-', label = 'Modelled least-squares fit')
plt.legend( loc = 'upper right')
plt.title( 'Star Luminosity vs. Temperature')
plt.xlabel( 'Temperature (C)')
plt.ylabel( 'Luminosity (solar units)')
plt.savefig('Data/Watson_Midterm1.png', dpi = 150)
plt.show()













