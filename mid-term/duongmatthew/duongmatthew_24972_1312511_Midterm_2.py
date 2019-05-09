# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:55:23 2019

@author: maduong
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#===================================================================================
#                                params
#===================================================================================
xmin, xmax = -10, 10
x0 = 1
x1 = -1
#===================================================================================
#                                def functions
#===================================================================================
def f1(x):
    return x**5 + (2/5)*x**2 - 2
def f2(x):
    return np.exp(-x/10) + x 
def f3(x):
    return 10*np.sin(x/4) + .1*(x+12)

#===================================================================================
#                                find roots
#===================================================================================
xroot1 = opt_utils.my_Secant(f1, x0, x0+10, N = 40 ) 
xroot2 = opt_utils.my_Secant(f2, x0, x0+10, N = 40 ) 
xroot3 = opt_utils.my_Secant(f3, x1, x1+10, N = 40 ) 

#===================================================================================
#                                plots
#===================================================================================
a_x = np.linspace(xmin, xmax, 1000) 

plt.figure(1)
plt.plot([xmin, xmax], [0,0], 'r--')
plt.plot(a_x, f1(a_x), 'k-', label = 'root, $x$=%.2f'%(xroot1))
plt.legend( loc = 'upper right')
plt.plot([xroot1], [f1(xroot1)], 'k*')

plt.figure(2)
plt.plot([xmin, xmax], [0,0], 'r--' )
plt.plot(a_x, f2(a_x), 'k-', label = 'root, $x$=%.2f'%(xroot2))
plt.legend( loc = 'upper right')
plt.plot([xroot2], [f2(xroot2)], 'k*')

plt.figure(3)
plt.plot([xmin, xmax], [0,0], 'r--')
plt.plot(a_x, f3(a_x), 'k-', label = 'root, $x$=%.2f'%(xroot3))
plt.legend( loc = 'upper right')
plt.plot([xroot3], [f3(xroot3)], 'k*')

plt.show()