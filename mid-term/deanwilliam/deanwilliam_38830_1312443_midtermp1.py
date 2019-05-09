#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:21:53 2019

@author: williamdean
"""
import opt_utils as utils
import numpy as np
import matplotlib.pyplot as plt

# load data
star = np.genfromtxt('data/star_luminos.txt')
T, L = star.T[0], star.T[1]

#print ( T, L)

Tmin, Tmax = 10, 1000

# fit data
dLS = utils.lin_LS( ( T), ( L))
for tag, item in dLS.items():
    if isinstance( item, (int, float)):
        print( tag, item)

#L = alpha*T**beta
#at_bin_T, aN_bin_L   = seis_utils.eqRate( at_AS)
#sel_t = np.logical_and( at_bin_T >= dPar['Tmin'], at_bin_L <= dPar['Tmax'])

plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot( T, L, 'ko', ms = 5, mew = 1, mfc = 'none')
#a_x = np.linspace( Tmin, Tmax, 1000)
#plt.plot( star)

plt.xlabel( 'Temperature(degree C)')
plt.ylabel( 'Luminosity(solar units)')
plt.title( 'Model of Temperature vs. Luminosity')
ax1.legend( loc = 'upper right')
plt.grid( True)