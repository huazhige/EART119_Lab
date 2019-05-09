#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:56:19 2019
        Midterm Q2 - Root Finding
@author: andrewquartuccio
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

# =============================================================================
#               X-Axis interval
# =============================================================================

a_X = np.linspace(-10,10,100)
x0 = -10

# =============================================================================
#               Define functions and derivatives
# =============================================================================

def f_x1(x):
    return x**5 + (0.4)*x**2 - 2.0

def f_x2(x):
    return np.exp(-0.1*x) + x

def f_x3(x):
    return 10*np.sin(0.25*x) + 0.1*(x+12)

def df_dx1(x):
    return 5*x**4 + (0.8)*x

def df_dx2(x):
    return 0.1*np.exp(-0.1*x) + 1

def df_dx3(x):
    return 2.5*np.cos(0.25*x) + 0.1



# =============================================================================
#               Root finding and Func Eval
# =============================================================================


a_fx1 = f_x1(a_X)
a_fx2 = f_x2(a_X)
a_fx3 = f_x3(a_X)
root1 = opt.my_Newton(f_x1, df_dx1, 0.1)
root2 = opt.my_Newton(f_x2, df_dx2, x0)
root3 = opt.my_Newton(f_x3, df_dx3, -1)

# =============================================================================
#               Plotting
# =============================================================================
print('The root of f1(x) is: %.3f') %(root1)
print('The root of f2(x) is: %.3f') %(root2)
print('The root of f3(x) is: %.3f') %(root3)

plt.figure(1)
plt.plot(a_X, a_fx1, 'r-')
plt.plot(root1, 0, 'b*')
plt.xlabel('X')
plt.ylabel('f1(x)')
plt.figure(2)
plt.plot(a_X, a_fx2, 'g-')
plt.plot(root2, 0, 'r*')
plt.xlabel('X')
plt.ylabel('f2(x)')
plt.figure(3)
plt.plot(a_X, a_fx3, 'b-')
plt.plot(root3, 0, 'g*')
plt.xlabel('X')
plt.ylabel('f3(x)')
plt.show()
