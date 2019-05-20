#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:40:12 2019
    HW 4 #4
@author: andrewquartuccio
"""

#=======================================================================================
#                       Imports
#=======================================================================================

import numpy as np
import matplotlib.pyplot as plt
import Modules.opt_utils as opt

#=======================================================================================
#                       Parameters
#=======================================================================================

x = np.linspace(-10, 10, 100)

#=======================================================================================
#                       Functions
#=======================================================================================

def f_x1(x):
    return -x**5 + (0.333*x**2) + 0.5

def f_x2(x):
    return np.cos(x)**2 + 0.1

def f_x3(x):
    return np.sin(0.333*x) + 0.1*(x+5)


#=======================================================================================
#                       Root Finding
#=======================================================================================

a_fx1 = f_x1(x)
a_fx2 = f_x2(x)
a_fx3 = f_x3(x)

plt.subplot(211)
plt.plot(x, a_fx1, 'r-')
plt.subplot(212)
plt.plot(x, a_fx2, 'g-')
plt.plot(x, a_fx3, 'b-')
root1 = opt.my_Secant(f_x1, -10.0, 10.0, tol=1e-4, N=20)
root2 = opt.my_Secant(f_x2, -5.0, 5.0, tol=1e-4, N=20)
root3 = opt.my_Secant(f_x3, -5.0, 5.0, tol=1e-4, N=20)

#print('The roots of f1(x) are %.3f.') %(root1)
print('There are no roots of f2(x).')
print('The roots of f3(x) are %.3f.') %(root3)