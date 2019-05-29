# -*- coding: utf-8 -*-
"""
@author: Jason

 Discretize the following functions between xmin, 
 xmax using N=1000 sample points. Compute the mean 
 value of the function in the given domain and compare 
 it to the integral of the function over the same domain. 
 You can compute the integral numerically
 or analytically

a.) f(x) = sin(x) {0 < x < pi}
b.) g(x) = 2xe^x^2
"""
import numpy as np

def fx(x):
    return np.sin(x)

def gx(x):
    return 2*x* np.exp(x**2)

def integration_f_x(x):
    return (-1) * np.cos(x)

def integration_g_x(x):
    return np.exp(x**2)

def_intA = integration_f_x(np.pi) - integration_f_x(0)

def_intB = integration_g_x(1) - integration_g_x(0)

values_f = np.linspace(0, np.pi, 100)
mean_f_x = np.mean(fx(values_f))

values_g = np.linspace(0, 1, 10000)
mean_g_x = np.mean(gx(values_g))


print("Mean value of f(x): %.20f"%mean_f_x)
print("integral: %.20f"%def_intA)

print("Mean value of g(x): %.20f"%mean_g_x)
print("integral: %.20f"%def_intB)
