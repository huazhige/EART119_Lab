# -*- coding: utf-8 -*-

"""
Discretize the following functions between xmin, xmax using N=1000 sample points.
Compute the mean value of the function in the given domain and compare it to
the integral of the function over the same domain.
You can compute the integral numerically or analytically.

a) f(x) = sin(x) ; (0 < x < pi)
b) g(x) = 2x(e**(x**2) ; (0 < x < 1)
"""
#============================ imports==========================================

import numpy as np

pi = np.pi
e = np.exp(1)

#======================define functions up in here ============================

def f_x(x):
    return np.sin(x)

def g_x(x):
    return (2*x) * (e**(x**2))

#===================analytically defined integrals ============================

def int_f_x(x):
    return (-1) * np.cos(x)

def int_g_x(x):
    return (e**(x**2))

#=============print(f_x(pi/2), g_x(1), int_f_x(pi), int_g_x(0))================
    
def_intA = int_f_x(pi) - int_f_x(0)

def_intB = int_g_x(1) - int_g_x(0)

#=====================Evaluate 1000 sample points =============================

values_1 = np.linspace(0, pi, 1000)
mean_f_x = np.mean(f_x(values_1))

values_2 = np.linspace(0, 1, 1000)
mean_g_x = np.mean(g_x(values_2))

#=============================Results =========================================

print("Mean value of f(x): %32.20f"%mean_f_x)
print("Analytically solved integral: %.20f"%def_intA)

print("Mean value of g(x): %32.20f"%mean_g_x)
print("Analytically solved integral: %.20f"%def_intB)

"""

Mean value of f(x):           0.63598262847222897243
Analytically solved integral: 2.00000000000000000000
Mean value of g(x):           1.71928302212668948634
Analytically solved integral: 1.71828182845904509080

"""