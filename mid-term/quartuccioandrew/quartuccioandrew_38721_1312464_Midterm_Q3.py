#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:23:05 2019
        Midterm Q3 - 1st and 2nd Derivatives
@author: andrewquartuccio
"""


import numpy as np
import matplotlib.pyplot as plt
import Modules.opt_utils as opt




# =============================================================================
#               Load Data 
# =============================================================================

file_in = './Data/midterm_dydx.txt'

mData = np.genfromtxt(file_in, skip_header = 1, dtype = float).T
N = len(mData)

a_X = np.linspace(-3,3,N)
# =============================================================================
#               Central Diff
# =============================================================================

t = mData[0,:]
z = mData[1,:]
dt = mData[0,1] - mData[0,0]

a_t, a_y = mData[0], mData[1]

a_vel = np.zeros( N)
a_acc = np.zeros( N)

for i in range( 1, N-1):
    a_vel[i] = ( a_y[i+1] - a_y[i-1])/(2*dt)
    a_acc[i] = ( a_y[i+1] - 2*a_y[i] + a_y[i-1])/(dt**2)

print(a_vel,a_acc)