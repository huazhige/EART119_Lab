#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:53:41 2019

@author: andrewquartuccio
"""

import numpy as np
import matplotlib.pyplot as plt

#=================================================================
#                    Parameters
#=================================================================

x0 = -9
xmin, xmax = -10, 15


#=================================================================
#                    Funct Def
#=================================================================

def f_x(x):
    return -x**2+10*x+9

def df_dx(x):
    return -2*x+10

#=================================================================
#                    Newton Meethod w/ While Loop
#=================================================================
# A)  WHILE Loop

def my_Newton(f_x, df_dx, x0):
    
    xn = float(x0)
    eps = 1e-5
    N=20
    i=0
    
    while (f_x(xn+1)-f_x(xn) < eps) or (i < N):
        x_next = xn - f_x(xn)/df_dx(xn)
        xn = x_next
        i += 1
    
    if abs(f_x(xn)<eps):
        return x_next
    else:
        return np.nan

# B)  Vectorized Solution

root_x = my_Newton(f_x, df_dx, x0)

a_x = np.linspace(xmin, xmax, 1000)

# Eval Func

a_fx     = f_x(a_x)
a_f_root = f_x(root_x)

#=================================================================
#                    Plotting Functions
#=================================================================

plt.figure(1)
plt.plot(a_x, a_fx, 'r-', ms=2)
plt.plot([root_x], [a_f_root], 'g*', ms=14)
plt.show()