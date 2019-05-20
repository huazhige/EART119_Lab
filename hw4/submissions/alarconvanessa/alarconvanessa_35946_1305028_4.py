# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:14:40 2019

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

#================== Defining Functions ========================================

def f1_x (x):
    return ((-x)**5) + (1/3)*x**2 + (1/2)


def f2_x (x):
    return (np.cos(x))**2 + 0.1


def f3_x (x):
    return np.sin(x/3) + 0.1*(x + 5)

t1 = np.linspace (-10, 10)

t2 = np.linspace (-3, 3)

for i in range(0, 20):
    x = opt.my_Secant( f1_x, .1, t1[i], tol = 1e-4, N = 20)
    i += 1
print ('roots for 4a)', x)

for i in range(0, 20):
    x1 = opt.my_Secant( f2_x, 0, t1[i], tol = 1e-4, N = 20)
    i += 1
print( 'roots for 4b)', x1)

for i in range(0, 6):
    x2 = opt.my_Secant( f3_x, 0, t2[i], tol = 1e-4, N = 20) 
    i += 1
    
print( 'roots for 4c)', x2)
    