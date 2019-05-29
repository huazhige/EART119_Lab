# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:03:41 2019

Discretize the following functions between xmin, xmax using N=1000 sample points.
Compute the mean value of the function in the given domain and compare it to the
integral of the function over the same domain. You can compute the integral
numerically or analytically.
"""
import numpy as np
import integrate_utils as int_utils 
import matplotlib.pyplot as plt
#================================================
#          fct definition
#================================================

def f(x):
    return np.sin(x)

def g(y):
    return 2*y*np.exp(y**2)

#================================================
#          compute mean value
#================================================
x= np.linspace(0, np.pi + (np.pi/1000), 1000)
y= np.linspace(0, 1 + 1/1000, 1000)

print np.sum(x)/1000, np.sum(y)/1000    
  
#================================================
#          compute integral 
#================================================
    #using trapezoidal method
f_int = int_utils.trapezoidal(f, 0, np.pi, 1000)
g_int = int_utils.trapezoidal(g, 0, 1, 1000)

print f_int, g_int

#================================================
#            plotting
#================================================
plt.figure(1)
ax = plt.subplot( 111)
ax.plot( x,  f(x), 'r-', lw = 1, label = 'f(x)')
ax.plot( y,  g(y),  'b-', lw = 1, label = 'g(y)')

#mean values are notably lower than values obtained through numerical integration 







