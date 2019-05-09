# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:04:24 2019

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

#================= Equations ==================================================
x0 = -10
x1 = 10
x = np.arange(-10, 10, 1)
# a
def a(x):
    return x**5 + (2/5)*x**2 - 2

def b(x):
    return np.exp(-x/10) + x

def c(x):
    return 10*np.sin(x/4) + 0.1*(x + 12)

#============= roots ==========================================================
for i in range (0, 10):
    a = opt.my_Secant(a(x), 0, x[i])
    aF = np.append(aF, a)
print( aF)

