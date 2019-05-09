#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:21:53 2019
    119 Midterm Question 1 Lumosity vs. Temp
@author: andrewquartuccio
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import Modules.opt_utils as opt

# =============================================================================
#                   Parameters
# =============================================================================

N = 990
#   Set interval of x-axis
xmin, xmax = 10, 1000
a_x = np.linspace( xmin, xmax, N)

# =============================================================================
#                   Data Import
# =============================================================================

#   Save the file name in a variable
file_in = './Data/star_luminos.txt'

#   Load Data, skip the header line, and transpose into 2 row vectors
mData = np.genfromtxt(file_in, skip_header = 1, dtype = float).T
#   Create new mData for only temps from 10 to 1000
mData_new = np.zeros((2, 990))
for i in range(10,1001):
    if(mData[0,i] >= 10 and mData[0,i] <= 1000):
        mData_new[0,i-(i-1)] = [mData_new, mData[0,i]]
        mData_new[1,i-(i-1)] = [mData_new, mData[1,i]]
# =============================================================================
#                   PL Fit
# =============================================================================

dLS = opt.lin_LS(mData_new[0], mData_new[1])

# =============================================================================
#                   Plotting
# =============================================================================

plt.figure(1)
plt.subplot(211)
plt.loglog(mData[0], mData[1], 'r--')
plt.loglog(mData_new[0], dLS['Y_hat'], 'bo')
plt.show()

os.chdir('./Data/')
plt.savefig('Midterm_Q1.png')