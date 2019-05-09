# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:22:36 2019

Fit data to a power law
"""
import numpy as np
import matplotlib.pyplot as plt

file_in = 'star_luminos.txt'

#===================================================================================
#                                params
#===================================================================================
Tmin, Tmax = 11, 1000 #temperature interval

#===================================================================================
#                                Data
#===================================================================================
mData = np.loadtxt( file_in).T
T, L = mData[0], mData[1] #define variables for temperature and luminosity

#===================================================================================
#                                Plotting
#===================================================================================
a_x = np.linspace(Tmin, Tmax)
plt.plot(T, L, 'k', label = 'data plot')
plt.xlabel('Temperature')
plt.ylabel('Luminosity')