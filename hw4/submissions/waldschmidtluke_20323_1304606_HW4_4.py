#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:07:31 2019

@author: lukewaldschmidt
"""

import numpy as np
import sys
sys.path.append('/Users/lukewaldschmidt/ASTR119/modules')
import opt_utils

#defining function
def f_1(x):
    return -x**5 + 1/3*x**2 + 1/2
def f_2(x):
    return (np.cos(x))**2 + 0.1
def f_3(x):
    return np.sin(x/3) + 0.1*(x+5)

print opt_utils.my_Secant( f_1, .1, .2, tol = 1e-4, N = 20)

# f1 has root at 0.157021404263

print opt_utils.my_Secant( f_2, 1, 1.1, tol = 1e-4, N = 20)

# f2 has no roots, cos^2 + .1 never hits the x-axis

print opt_utils.my_Secant( f_3, -1.2, -1.1, tol = 1e-4, N = 20)

# f3 has a root at -1.1768780402

