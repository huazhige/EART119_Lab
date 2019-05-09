# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:22:49 2019

@author: lsknudso

Equation form:
    L = \alpha T**\beta
    take the log so:
        log (L) = \beta * Log(T) + log ( \alpha)
    Fit linearly (y = mx + b) and our parameters will be m = \beta and b = log ( \alpha)    
"""
# =============================================================================
# Importing packages and modules
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

import opt_utils as opt

# =============================================================================
# Parameters
# =============================================================================
file_in = 'star_luminos.txt'

Tmin, Tmax = 10, 1000 

# =============================================================================
# Load and select data
# =============================================================================
Data = np.loadtxt(file_in).T

sel = np.logical_and(Data[0] > Tmin, Data[0] < Tmax)

# =============================================================================
# Linear fit
# =============================================================================
dLS = opt.lin_LS(np.log10(Data[0][sel]), np.log10(Data[0][sel]))

# =============================================================================
# Plotting
# =============================================================================
plt.rcParams.update({'font.size': 12})
plt.plot(np.log10(Data[0][sel]), np.log10(Data[0][sel]), 'r+')
plt.plot(np.log10(Data[0][sel]), dLS['Y_hat'], 'b-')
plt.xlabel("log(T)")
plt.ylabel("log(L)")
plt.legend(('Data','Fit:y = %s*x+ %s\nbeta = %s\nalpha = %s'%(dLS['b'], dLS['a'], dLS['b'], 10**dLS['a'])))
plt.title("Star Temperature vs Luminocity")

plt.savefig('./Problem1fig')
plt.show()