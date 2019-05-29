# -*- coding: utf-8 -*-
"""
@author: Jason

Compute the values of the following definite integrals 
using Monte Carlo Integration. Compare your results 
to the exact solution. (Hint: For the first integral, 
you have to perform a coordinate transform from cartesian
to polar coordinates to solve the problem analytically).

a.) f(x,y) = (x^2 + y^2)^0.5;

b.) W(x,y) = xy^2
"""
def wxy(x,y):
    return x*y**2

#x^2 + y^2 = sin^2(theta) + cos^2(theta)
def fxy(x,y):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return np.sqrt(x**2 + y**2)
